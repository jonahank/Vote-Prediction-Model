import pandas as pd
from encode_desc import transform_description, tokenize_description

## Load data
df_test = pd.read_pickle("./c_test_V2.1.pkl")
df_test["set"] = 'test'
df = pd.read_pickle("./c_train_V2.1.pkl")
df["set"] = 'train'
print(len(df))
df = pd.concat([df, df_test])
print(len(df))

df = df.drop_duplicates(subset='description_text').reset_index(drop=True)
df = df.drop(columns=["index"])
df["vote_caller"] = df["vote_caller"].astype(str)
print(len(df))

## Tokenize data
df_tokenized = tokenize_description(df, "Venstre", "../BL/models_binary_party/", True)
print(len(df_tokenized))
df_tokenized.head(3)

## Transform vote-summaries into party probs
parties = ["Alternativet", "Dansk Folkeparti", "Det Konservative Folkeparti", "Det Radikale Venstre", "Enhedslisten", "Liberal Alliance", "Socialdemokratiet", "Socialistisk Folkeparti" ,"Venstre"]
df_trans = df_tokenized
for party in parties:
    df_trans = transform_description(df_trans, party, "../BL/models_binary_party/", 2, True)

df_trans.head(3)


## Save to pickle
df_trans.to_pickle("c_all_w_party_probs_v2.1.pkl")