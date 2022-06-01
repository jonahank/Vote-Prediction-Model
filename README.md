# Identifying and Analysing political quotes from the Danish Parliament related to climate change using NLP
## Available resources
+ **KlimaBERT**, a sequence-classifier for Danish texts fine-tuned to predict whether political quotes are climate-related. When predicting the class "climate-related" (positive class), the model achieves a F1-score of 0.97, Precision of 0.97, and Recall of 0.97.  
+ **Two annotated datasets** from the Danish Parliament in the period from 2012 to 2022; FT-Meetings containing political quotes from the public meetings, and FT-Votes containing all votes from the public voting-data.
+ **Vote prediction-model**, using a hybrid setup (NLP- & ML-techniques) to train a classification-model to predict how Danish politicians vote on climate-related bills.

## KlimaBERT
Please see this repository for:
+ the labelling process required to train the model
+ the fine-tuning flow using the pre-trained DaBERT-model
+ scoring the two unlabelled datasets to create FT-Meetings and FT-Votes



## Two annotated datasets
The two annotated datasets can be acessed at: (link comming soon!)


## Vote prediction-model
Please see this repository for the hybrid setup used to train the model:
+ using the pre-trained DaBERT-model to transform summaries of bills
+ using a Danish version of the Word2Vec-method to create sequence-embeddings
+ encoding categorical variables; party-affiliation of the voting politicians and the party proposed the bill in question
+ training the model as a Random Forest Classifier


## References
BERT:
Devlin, J., M.-W. Chang, K. Lee, and K. Toutanova (2018). Bert: Pre-training of deep
bidirectional transformers for language understanding.
https://arxiv.org/abs/1810.04805

DaBERT:
Certainly (2021). Certainly has trained the most advanced danish bert model to date.
https://www.certainly.io/blog/danish-bert-model/.

Danish Word2Vec:
Sørensen, N. H. (2020). Word2vec model.
//korpus.dsl.dk/resources/licences/dslopen.html

## Acknowledgements
The majority of this work is build using the Python libraries by [Hugging Face](https://huggingface.co/) and build upon the work of the team behind the [DaBERT-model](https://www.certainly.io/blog/norwegian-bert-model/)!

The resources are created through the work of my Master's thesis, so I would like to thank my supervisors [Leon Derczynski](https://www.derczynski.com/itu/) and [Vedran Sekara](https://vedransekara.github.io/) for the great support throughout the project! And a HUGE thanks to [Gustav Gyrst](https://github.com/Gyrst) for great sparring and co-development of the tools you find in this repo. 
