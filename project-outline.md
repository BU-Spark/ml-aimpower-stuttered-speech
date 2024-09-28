# Technical Project Outline

## *Wai Yuen (Wylliam) Cheng, Mary Choe, Lingjie (Leslie) Yuan, Yol-Emma (Emma) Yeillard, 2024-09-24 v0.0.1-dev*

## Overview

The project is called “Benchmarking Chinese Stuttered Speech Recordings Against Speech Recognition Models”. We want to train an AI NLP model to be able to recognize and understand stuttered speech in Chinese. We will develop a set of visualizations and final report that discusses the fluency biases and includes a deeper understanding, reflection, and curation of existing results.There are numerous plots already created (around 50), but they lack sufficient explanation and discussion. We will provide detailed interpretations of the graphs to help understand and diagnose fluency biases in existing ASR models.

### A. Provide a solution in terms of human actions to confirm if the task is within the scope of automation through AI.

A human would listen carefully to the stuttered speech perhaps at a slower speed, and transcribe it into written words.

In response to stuttered speech, human response typically involves:
	1. Seek for repetition of speech to make sure message
	2. Increase the contextual awareness of the conversation involving stuttered
      - Understanding the overall message to confirm the relevant words in stuttered speech
	3. Demand for writing or spelling as usually the last resort 

### B. Problem Statement:

This project is a speech recognition and natural language processing problem to recognize sequences of words through post processed audio signals and reconstruct the portion of sequences that the speech recognition model alone was not capable of recognizing as a word.

The problem is the bias with speech recognition models implemented for difficult disciplines in this case stuttered speech. AI models are unable to accurately transcribe stuttered speech, which makes the current speech recognition frameworks underrepresenting individuals with speech disabilities. 

### C. Checklist for project completion

1. Identify the causes behind hallucinations in the current NLP speech model
Evaluate against the speech model developed in summer 2024 semester
2. Solve/Mitigate the hallucinations in the current model

### D. Outline a path to operationalization.

The operationalized end point for this project would be an accurate speech to text AI model for stuttered speech. A specific example would be when people call companies with an automated bot. Our model would help the bot understand the person if they have stuttered speech. Another example would be captioning live broadcasts if the person speaking has a stutter.

The technology for the project involves fundamental speech recognition models, audio processing, etc. On top of speech recognition, existing model frameworks also implement language models to validate the content of the audio scribed. Whether the project involves a language model as an add-on is subject to the next meeting with client and project manager.


## Resources
1. https://github.com/BU-Spark/pitne-aimpower 
2. [The 10 Best Data Visualization Examples | Tableau](https://www.tableau.com/learn/articles/best-beautiful-data-visualization-examples)
3. [Data Visualisation Resources - Data Viz Excellence, Everywhere (visualisingdata.com)](https://visualisingdata.com/resources/)
### Data Sets
_Not Available As Of Completion of this Outline_

### References
1. Koenecke, A., Choi, A. S. G., Mei, K. X., Schellmann, H., & Sloane, M. (2024). Careless Whisper: Speech-to-Text Hallucination Harms. Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT). Retrieved from https://facctconference.org/static/papers24/facct24-111.pdf.
2. Li, Q., & Wu, S. (2024). Towards Fair and Inclusive Speech Recognition for Stuttering: Community-led Chinese Stuttered Speech Dataset Creation and Benchmarking. Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT). Retrieved from https://facctconference.org/static/papers24/facct24-111.pdf.
3. Wu, S. (2024). The World is Designed for Fluent People: Benefits and Challenges of Videoconferencing Technologies for People Who Stutter. Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT). Retrieved from https://facctconference.org/static/papers24/facct24-111.pdf.

## Weekly Meeting Updates

### Monday 9/23
We met our PM for the first time and learned more about the client and project. This project is a non-profit project for our client at the current stage. It is not meant for monetization but to actually help people with stuttered speech.

## Questions from Team
1. On top of recognizing speech from audio, in order to achieve good performance, would we implement a language model as a complementary step to the audio recognition?



/***********************************************************************************************************/
The project should begin with a high-level analysis of the dataset to understand the overall structure and what the data represents. This initial step will help set the stage for the main task, which is to analyze the hallucination patterns found in the models. 
The goal is to identify the causes behind these hallucinations,
 and optionally, work towards resolving them.
/***********************************************************************************************************/
