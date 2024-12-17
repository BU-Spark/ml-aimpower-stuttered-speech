# Dataset Documentation

## Project Overview  
Our project is _Benchmarking Chinese Stuttered Speech Recordings Against Speech Recognition Models_. We aim at carrying out multilingual ASR model biases against Chinese stuttering phenomenons, quantifying the relationships between speech disabilities and performance of models. Our client is AImpower.org, specifically working with Dr. Shaomei Wu (shaomei@aimpower.org). This project is under DS549 the Spark\! Machine Learning Practicum course.

- Github: [https://github.com/BU-Spark/ml-aimpower-stuttered-speech](https://github.com/BU-Spark/ml-aimpower-stuttered-speech)  
- Google Drive: [AIMpower.org: AIMpower - Google Drive](https://drive.google.com/drive/folders/1WN3abR5_gX2T0AP70qtJ6SvkJcsICHt8)

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
* Audio segmentation  
* Stuttering 

This dataset is specifically designed to assess the biases of various ASR models toward stuttering phenomena in Chinese. This project is part of a broader effort to make technology more accessible. Our analysis focuses on disfluency biases across different types of stuttering.

## Composition  
The dataset is self-contained and consists of audio files and corresponding transcripts. The audio files are WAV recordings of interviews, containing both conversational and command speech with instances of stuttered speech. The transcripts are in TXT format and include verbatim transcriptions of the spoken content, with annotations for different types of stuttering. 

The client has emphasized the intention to keep the dataset private, and there may be confidential data included, such as identifying details within the transcripts.   
There is no explicit reference to any external resources or external dataset dependencies. The dataset does not rely on external resources like websites or other datasets. The dataset is self-contained and does not link to any external data that would need to remain constant over time.

Further data splits may not be necessary, as the preprocessing phase included aligning audio segments with their corresponding transcripts based on timestamps. However, the dataset could potentially be further split by stuttering type to facilitate more targeted analysis.

There are no apparent errors or redundancies identified in the dataset within the groundtruth.

Additionally, there are no offensive or sensitive content issues identified within the dataset, though the presence of personal introductions or stuttered speech may raise privacy concerns.

## Preprocessing, Cleaning, & Labeling  
The dataset was first preprocessed into segments by collaborators at AImpower.org. Each audio file was broken down further into much shorter segments (0.5 to 18 seconds). The version retrieved by Spark\! has already been segmented by AImpower.org. 

The “raw” data, the audio and original transcriptions of each interview, was provided by Aimpower. Link to the “raw” dataset: [Datasets - Google Drive](https://drive.google.com/drive/folders/1QVXbks0MO7lEDnM43ZGQHOXHewbdHaIc)

The code used to preprocess the data (by segmenting the audio files based on the timestamps found in the transcripts) can be found the summer group’s notebook: [Preprocessing_AudioSegmenting.ipynb](https://github.com/BU-Spark/ml-aimpower-stuttered-speech/blob/main/DataPreprocessing_AudioSegmenting.ipynb).

## Uses  
This dataset has been used under inference of various ASR models (Whisper Tiny, Whisper Large, WeNet, Wav2Vec, Azure, Google Cloud) to generate textual transcription. The transcriptions have been used for model performance evaluations and comparisons. 

## Distribution  
Access is internal (restricted). The client does not authorize release of dataset. 

## Maintenance  
Several preprocessing of existing data can be implemented for this dataset. For each audio segment, they can be concatenated and form a larger chunk of audio data that might yield different results in inference.   
