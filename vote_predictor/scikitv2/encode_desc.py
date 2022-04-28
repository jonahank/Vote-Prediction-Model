from transformers import Trainer, BertForSequenceClassification, BertTokenizer
from datasets import load_metric, Dataset
import numpy as np
import torch
import pandas as pd

def compute_metrics(eval_preds):
    metric = load_metric("glue", "mrpc")
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

def encode(rows, trainer):
    ## Row must consist of [["input_ids", "token_type_ids", "attention_mask"]]
    ds = Dataset.from_pandas(pd.DataFrame(rows))
    prediction = trainer.predict(ds)
    return prediction[0]

def tokenize_description(df, party, path_to_models,verbose=False):
    if verbose: print(f"Loading tokenizer ...")
    checkpoint = path_to_models + party
    tokenizer = BertTokenizer.from_pretrained(checkpoint)
    
    def tokenize(batch):
        tokenized_batch = tokenizer(batch['text'], padding=True, truncation=True, max_length=512)
        return tokenized_batch

    if verbose: print(f"Tokenizing all description texts ...")
    tokenized_description = Dataset.from_pandas(df[["description_text"]].rename(columns={"description_text":"text"}), preserve_index=False).map(tokenize, batched=True)
    tokenized_description = tokenized_description.remove_columns(["text"])
    tokenized_description.set_format("torch")
    df_tokenized = df.join(tokenized_description.to_pandas())
    if verbose: print(f"Tokenizing all description texts completed!")
    return df_tokenized


def transform_description(df, party, path_to_models, num_labels=2, verbose=False):
    if verbose: print(f"Loading model for {party} ...")
    checkpoint = path_to_models + party
    model = BertForSequenceClassification.from_pretrained(checkpoint, num_labels=num_labels)

    ## Set to use GPU
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    model.to(device)
    device

    trainer = Trainer(
        model,
        compute_metrics=compute_metrics,
    )

    if verbose: print(f"Transforming all tokenized texts for {party} ...")
    m = torch.nn.Softmax(dim=-1)
    weight_pred = encode(df[["input_ids", "token_type_ids", "attention_mask"]], trainer)
    weight_for = []
    weight_against = []
    if num_labels == 2:
        for input in weight_pred:
            input2 = torch.from_numpy(input)
            (i,k) = m(input2) #i=against, k=for
            weight_for.append(k.item())
            weight_against.append(i.item())
    elif num_labels == 3:
        for input in weight_pred:
            input2 = torch.from_numpy(input)
            (i,j,k) = m(input2) #i=against, j=neutral, k=for
            weight_for.append(k.item())
            weight_against.append(i.item())

    df[f"{party}_weight_for"] = weight_for
    df[f"{party}_weight_against"] = weight_against
    if verbose: print(f"Transforming all tokenized texts for {party} completed!")

    return df
