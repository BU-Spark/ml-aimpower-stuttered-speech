# Content
This subdirectory consists mainly of analysis python notebooks. 

# Metrics
We are using:
* WER - Calculated using **Levenschtein Distance Algorithm**
* ROUGE Score - A combination of `Jieba` and `rouge_chinese` library

# Attempts
We have attempted to draw relationship between stuttering count and performance by the followings:
* plotting stuttering count to performance metrics => no pattern found
* plotting audio length to performance metrics => no pattern found

# Notes
* We are thinking about the indirect performance analysis assuming audio length implies less stuttering count => no evidence for assumption

# Issues
* Some `pandas` parsed dataframe has mismatched ground truth to the original ground truth transcription data file provided. We are checking if the parsing has gone wrong, otherwise removing those transcripts for analysis.