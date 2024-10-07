# Research 

*** 

## Related Work
* [“The World is Designed for Fluent People”: Benefits and Challenges of Videoconferencing Technologies for People Who Stutter](https://www.shaomei.info/pdfs/Stuttering_VC_preprint.pdf) 
    * “The World is Designed for Fluent People: Benefits and Challenges of Videoconferencing Technologies for People Who Stutter” introduces the background of the AImPower project. This paper studies the experience of people who stutter (PWS) with video conferencing (VC) and VC technologies. It talks about the challenges that PWS might face and the potential solutions to address these issues. Through the description, we can see that PWS indeed faces a lot of difficulties. And this literature primarily provides insights for our project in two aspects, dataset and assistive technologies. 
    * The author interviewed 13 PWS to discuss the personal background, characteristics of one’s stutter, experience of VC, etc. These interviews are transcribed as part of the dataset for our project. Limited by the selection of interviewees and the diversity of the geographical and cultural backgrounds, the data set needs to be extended in the future.  
    * This paper offers us three assistive technologies that can support PWS. What we should focus on is speech operated technology. This technique tries to tune the automatic speech recognition models (ASR) to better detect and recognize stuttering speech. And the papers referred to in this part can be our future research direction.
* [Towards Fair and Inclusive Speech Recognition for Stuttering:Community-led Chinese Stuttered Speech Dataset Creation and Benchmarking](https://www.shaomei.info/pdfs/CHI24-stuttered-speech-dataset.pdf)
    * “Towards Fair and Inclusive Speech Recognition for Stuttering: Community-led Chinese Stuttered Speech Dataset Creation and Benchmarking” is written by Qisheng Li and Shaomei Wu. They explore the difficulties people with a stutter face specifically from Automatic Speech Recognition (ASR) models in conversational AI. 
    * About 1% of the world's stutters and ASRs have difficulty understanding stuttered speech and are three to four times more likely to transcribe the speech wrong compared to non-stuttered speech. They created the first stuttered speech dataset in Mandarin Chinese collected from 72 speakers. The StammerTalk dataset allows for a wide range of technical exploration and innovation around stuttered speech. 
    * One finding is the importance of situational context to understand stuttered speech. There are different kinds of stuttering that need to be accounted for. Also, the frequency and distribution of stuttering highly varies from person to person. This research is preliminary and with this dataset extended research should and can be conducted.
* [Careless Whisper: Speech-to-Text Hallucination Harms](https://facctconference.org/static/papers24/facct24-111.pdf)
    * It has been found that OpenAI Whisper is highly accurate when transcribing speech. ~1% of audio transcriptions were found to be entirely made up.
        * “38% of hallucinations include explicit harms such as perpetuating violence, making up inaccurate associations, or implying false authority.”
    * These hallucinations disproportionately affected marginalized groups such as African American English Speakers, stuttered speech and non-English audios. Some examples include
        * The accuracy of a transcription can increase when the speaker code switches
    * Categorizing hallucinations: The listed threats are considered first order threats, which were considered to have a direct harm - often on the speaker. These types of transcripts can perpetuate the misinformation the model has been trained on and can directly impact vulnerable groups such as children
        * Perpetuation of violence
            * “Hallucinations in this category include explicit portrayals of (a) physical violence or death, (b) sexual innuendo, and (c) demographic-based stereotypes”
        * Inaccurate associations
            * “Hallucinations in this category include references to (a) made up names and/or locations, (b) made up human relationships, or (c) made up health statuses.”
        * False Authority
            * “Hallucinations in this category include (a) language reflective of video-based authorities (such as Youtubers or newscasters), (b) thanking viewers or specific groups, and (c) linking to websites”
            * A high volume of hallucinations fell into that category because GPT-4 was trained on over a million hours of youtube videos




***

## Open Source Projects & Existing Technologies
* [OpenAI Whisper](https://arxiv.org/pdf/2212.04356)
    * Training preparation
        * 680000 hours of audio
        * Differentiating text and non-text audio
            * If non-text, do not use the audio & transcript pair for the training process of Whisper
        * Audios are broken into 30-second segments
        * Initial training to understand the quality of data, remove low quality consequently &rarr; _potential biases with unclear audio or speech_
    * _“audio is re-sampled to 16,000 Hz, and an 80-channel log-magnitude Mel spectrogram representation is computed on 25-millisecond windows with a stride of 10 milliseconds.”_
    * Model architecture
        * Transformer (encoder & decoder)
            * Decoder: audio-conditional language model
            * Encoder: mainly handle audio encoding
            * Particular tags are added to indicate the specific features of audio such as no text, procedures to carry out over the audio (translate or transcribe …) &rarr; specifying tasks
    * Evaluation metrics
        * Word Error Rate
        ![Whisper Model WER](https://github.com/BU-Spark/ml-aimpower-stuttered-speech/tree/dev/assets/whisper-performance-wer.png)
* [Facebook Wav2Vec 2.0](https://arxiv.org/pdf/2006.11477)
    * Dataset
        * 53.2k hours of audio 
    * Evaluation Metrics
        * Phoneme error rate
        * Word error rate
    * Model Architecture
        * Convolutional Network &rarr; Processing Audio Files & Increasing Dimensions
        * 24 Transformer Blocks (LLM)
    * Emphasis
        * Low resource training can still achieve high performance \n
    **Wav2Vec 2.0 no multilingual features reported in the paper. But there are repositories that demonstrated application with Wav2Vec 2.0 in Mandarin Speech Recognition[example repo](https://github.com/kehanlu/Mandarin-Wav2Vec2)**
* [WeNet 2.0](https://arxiv.org/pdf/2203.15455)
    * Model Architecture
        * Bidirectional encoding & decoding
        * N-gram language model
    * Addressed contextual biases but not the quality of the audio dataset or input
        * Focus more on biases in content reconstruction. To some extent this can help with stuttered speech recognition but the objective is not directly for support of that purpose. \n
    **WeNet 2.0 was designed to support Mandarin Chinese, as indicated in the paper with plenty of examples implementing audio recognition and sequential prediction on Chinese text.**
* [NVIDIA STT Canary](https://arxiv.org/pdf/2406.19674)
    * Model Architecture
        * FastConformer encoder & Transformer decoder
        * Utilizes labeling of actions, similar to Whisper from OpenAI ⇒ support multitasking
    * Datasets & Preparations
        * Consist of multiple languages and diverse datasets (does not contain Chinese however)
        * Addressed the problem of utterance &rarr; can be applicable over stuttered speech
        * Definition of hallucination: producing transcripts when input audio contains no speech
    * Inference
        * Followed by more online research, inferences with Mandarin is possible with NVIDIA Canary model 
* [Meta Seamless M4T](https://scontent-lga3-1.xx.fbcdn.net/v/t39.2365-6/369747868_602316515432698_2401716319310287708_n.pdf?_nc_cat=106&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=uGUYVevo9OgQ7kNvgHXKeh0&_nc_ht=scontent-lga3-1.xx&_nc_gid=AZRLYCUGcMC3N1VBv-wgyIH&oh=00_AYCxsQmvYgDbP291ifapxKN_wadzSdWVDLQAvnmRzwuk8Q&oe=6708DCF9)
    * No direct description over the Seamless M4T model architecture was found. However, it emphasizes multilingualism and multimodality. 
    * It also detailed the problems of responsible AI, including biases, and provides considerations and evaluations on the models on comparisons between masculine and feminine voices, language types, genders. No evaluations and discussions with stuttered speech, utterance, or accent were found.









