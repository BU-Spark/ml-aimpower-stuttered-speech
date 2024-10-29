# EDA Explanation

## Dataset Breakdown

The dataset is organized in the following hierarchy:

```Audio Portion of Dataset [audio_deid_full]
<sample-id>
│	meeting_<sample-id>.wav 	(audio of the entire interview)
└───────recitation			(directory of the instructed words to be read)
│	└───────<sample-id>_<start-timestamp>_<end-timestamp>.wav
└───────segments			(directory of audio segments from casual conversation)
	└───────<sample-id>_<start-timestamp>_<end-timestamp>.wav 
```

```Transcription Portion of Dataset [updated_annotated_deid_full]
<sample-id>
│	D<sample-id>_A.txt 		(transcript of interviewee from casual conversation)
│	D<sample-id>_B.txt		(transcript of moderator from casual conversation)
│	P<sample-id>.txt		(transcript of specifically instructed words to be read by interviewee)
```
