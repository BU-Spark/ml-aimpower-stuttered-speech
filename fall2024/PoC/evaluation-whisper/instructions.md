# Instruction
The scripts are to be run in a strict order because of the importation of CSV dataframe variables for `pandas.read_csv()`. The order is as the following:

```mermaid
A(whisper-stu-eval.ipynb) --> B(whipser-len-eval.ipynb) --> C(whisper-len-stu-corr.ipynb)
```