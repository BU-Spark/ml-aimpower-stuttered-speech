# Dataset Documentation

## Project Overview
Our project is _Benchmarking Chinese Stuttered Speech Recordings Against Speech Recognition Models_. We aim at carrying out multilingual ASR model biases against Chinese stuttering phenomenons, quantifying the relationships between speech disabilities and performance of models. Our client is AImpower.org, specifically working with Dr. Shaomei Wu (shaomei@aimpower.org). This project is under DS549 the Spark! Machine Learning Practicum course.
Github: [https://github.com/BU-Spark/ml-aimpower-stuttered-speech](https://github.com/BU-Spark/ml-aimpower-stuttered-speech)
Google Drive: 

## Dataset Information
The dataset we used in our project is created by AImpower.org, established based on the 70 interviews with Chinese-speaking individuals with stuttering speech disabilities. The dataset is stored on SCC `/projectnb/ds549/project/AImpower/datasets`. 
Keywords for Dataset:
* Automatic Speech Recognition
* Bias in machine learning
* Natural Language Processing
* Wav2Vec
* Whisper
* Azure
* Google Cloud
* WeNet
* Multilingual ASR
* Speech-To-Text Models

This dataset is particularly designed to assess the biases of different models against stuttering phenomenon in Chinese. 

## Preprocessing, Cleaning, & Labeling
The dataset was first preprocessed into segments by collaborators at AImpower.org. Each audio file was broken down further into much shorter segments (0.5 to 18 seconds). The version retrieved by Spark! has already been segmented by AImpower.org. 

## Uses
This dataset has been used under inference of various ASR models (Whisper Tiny, Whisper Large, WeNet, Wav2Vec, Azure, Google Cloud) to generate textual transcription. The transcriptions have been used for model performance evaluations and comparisons. 

## Distribution
Access is internal (restricted). The client does not authorize release of dataset. 

## Maintenance
Several preprocessing of existing data can be implemented for this dataset. For each audio segment, they can be concatenated and form a larger chunk of audio data that might yield different results in inference. 