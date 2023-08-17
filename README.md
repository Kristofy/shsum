# SHSUM
## Description
An application capable of producing a consise summary of a manual page with usefull examples

## Intended Usecase
Example:  

```bash 
$ shsum ls
  ls can be used to list the content of a dirictory
  # list the current directory
  `ls`
  # list all including hidden
  `ls -a`
  # list with additional information
  `ls -l` 
```
## Base model
A t5 text-to-text transformer, previously trained on general NPL tasks as well as on [CodeSearchNet](https://arxiv.org/pdf/1909.09436.pdf)  
The moddel is available on huggingface as [Salesforce/codet5-base](https://huggingface.co/Salesforce/codet5-base)

## Gathering data
The training data is not provided in this repository, instead a collection of fetching scripts are provided that should gather, compile and clean up the training data.  

### Requirements for the fetching sripts
- TODO



