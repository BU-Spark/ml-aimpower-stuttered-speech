#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip3 install jiwer
# !pip3 install nltk
# !pip3 install wn
# !pip3 install opencc
# !pip3 install sent2vec
# !pip3 install transformers torch scikit-learn
# !pip3 install pynlpir
# !pip3 install jieba


# In[9]:


import pandas as pd
import numpy as np
import jiwer
from nltk.translate.bleu_score import sentence_bleu
import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import torch
from sent2vec.vectorizer import Vectorizer
from scipy.spatial.distance import cosine
nltk.download('punkt')
import jieba
from nltk.corpus import wordnet as wn


# In[10]:


# https://www.nltk.org/howto/wordnet.html
# https://stackoverflow.com/questions/63514884/does-wordnet-python-nltk-interface-includes-any-measure-of-semantic-relatedness
def calculate_wordnet_first(reference, hypothesis):
    ref_lemmas = [wn.lemmas(word, lang='cmn')[0] for word in jieba.lcut(reference) if wn.lemmas(word, lang='cmn')] # only top 1
    hyp_lemmas = [wn.lemmas(word, lang='cmn')[0] for word in jieba.lcut(hypothesis) if wn.lemmas(word, lang='cmn')]
    similarities = []
    for ref_lemma in ref_lemmas:
        for hyp_lemma in hyp_lemmas:
            similarity = wn.wup_similarity(ref_lemma.synset(), hyp_lemma.synset())
            if similarity:
                similarities.append(similarity)
    if similarities:
        return sum(similarities) / len(similarities)
    else:
        return 0.0

def calculate_wordnet_all(reference, hypothesis):
    try:
        ref_lemmas = [lemmas for word in jieba.lcut(reference) for lemmas in wn.lemmas(word, lang='cmn')] # consider all candidates
        hyp_lemmas = [lemmas for word in jieba.lcut(hypothesis) for lemmas in wn.lemmas(word, lang='cmn')]
        similarities = []
        for ref_lemma in ref_lemmas:
            for hyp_lemma in hyp_lemmas:
                similarity = wn.wup_similarity(ref_lemma.synset(), hyp_lemma.synset())
                if similarity:
                    similarities.append(similarity)
        if similarities:
            return sum(similarities) / len(similarities)
        else:
            return 0.0
    except AttributeError:
        return np.nan


# https://github.com/stanfordnlp/GloVe # only has English
# https://www.kaggle.com/datasets/chongjiujjin/chinese-word-embedding-glove-dim-128?resource=download # Chinese vector embeddings
glove_embeddings = {}
with open('../../evaluation/vectors.txt', 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype='float32')
        glove_embeddings[word] = vector
def calculate_glove(reference, hypothesis):
    ref_vectors = [glove_embeddings[word] for word in jieba.lcut(reference) if word in glove_embeddings]
    hyp_vectors = [glove_embeddings[word] for word in jieba.lcut(hypothesis) if word in glove_embeddings]
    if not ref_vectors or not hyp_vectors:
        return 0.0
    ref_mean_vector = np.mean(ref_vectors, axis=0).reshape(1, -1)
    hyp_mean_vector = np.mean(hyp_vectors, axis=0).reshape(1, -1)
    return cosine_similarity(ref_mean_vector, hyp_mean_vector)[0][0]


# https://huggingface.co/google-bert/bert-base-chinese # 'bert-base-chinese'
## https://github.com/ymcui/Chinese-BERT-wwm/blob/master/README_EN.md # advanced CWS included version
bert_tokenizer = BertTokenizer.from_pretrained('hfl/rbt3')
bert_model = BertModel.from_pretrained('hfl/rbt3')
def calculate_bert(reference, hypothesis):
    ref_inputs = bert_tokenizer(reference, return_tensors='pt')
    hyp_inputs = bert_tokenizer(hypothesis, return_tensors='pt')
    with torch.no_grad():
        ref_outputs = bert_model(**ref_inputs)
        hyp_outputs = bert_model(**hyp_inputs)
    ref_embedding = ref_outputs.last_hidden_state.mean(dim=1)
    hyp_embedding = hyp_outputs.last_hidden_state.mean(dim=1)
    return cosine_similarity(ref_embedding, hyp_embedding)[0][0].item()


# https://pypi.org/project/sent2vec/
def calculate_sent2vec(reference, hypothesis):
    vectorizer = Vectorizer()
    vectorizer.run([reference, hypothesis,])
    vectors = vectorizer.vectors
    return cosine(vectors[0], vectors[1])


# In[11]:

def generate_evaluation_df(modelname):

    df_merged = pd.read_csv(f'processed_{modelname}_evaluation.csv', index_col=0)

    WER = []
    CER = []
    BLEU = []
    WordNet_first = []
    WordNet_all = []
    GloVe = []
    BERT = []
    Sent2Vec = []
    for i in range(df_merged.shape[0]):
        reference = df_merged['ground_truth_cleaned'].iloc[i]
        hypothesis = df_merged[modelname].iloc[i]
        if not isinstance(reference, str) or not isinstance(hypothesis, str):
            WER.append(np.nan)
            CER.append(np.nan)
            BLEU.append(np.nan)
            WordNet_first.append(np.nan)
            WordNet_all.append(np.nan)
            GloVe.append(np.nan)
            BERT.append(np.nan)
            Sent2Vec.append(np.nan)
        else:
            WER.append(jiwer.wer(' '.join(jieba.lcut(reference)), ' '.join(jieba.lcut(hypothesis))))
            CER.append(jiwer.cer(reference, hypothesis))
            BLEU.append(sentence_bleu([jieba.lcut(reference)], jieba.lcut(hypothesis)))
            WordNet_first.append(calculate_wordnet_first(reference, hypothesis))
            WordNet_all.append(calculate_wordnet_all(reference, hypothesis))
            GloVe.append(calculate_glove(reference, hypothesis))
            BERT.append(calculate_bert(reference, hypothesis))
            Sent2Vec.append(calculate_sent2vec(reference, hypothesis))
        
    df_merged['WER'] = WER
    df_merged['CER'] = CER
    df_merged['BLEU'] = BLEU
    df_merged['WordNet_first'] = WordNet_first
    df_merged['WordNet_all'] = WordNet_all
    df_merged['GloVe'] = GloVe
    df_merged['BERT'] = BERT
    df_merged['Sent2Vec'] = Sent2Vec

    df_merged.to_csv(f'processed_{modelname}_evaluation.csv')


# In[ ]:


modelnames = ['Whisper_tiny', 'Whisper_tiny_cleaned', 'Whisper_large', 'Whisper_large_cleaned', 'GoogleCloud', 'GoogleCloud_cleaned', 'Wav2vec', 'Wav2vec_cleaned', 'WeNet', 'WeNet_cleaned', 'Azure', 'Azure_cleaned']
for modelname in modelnames:
    generate_evaluation_df(modelname)
    print(f'{modelname} success!')
