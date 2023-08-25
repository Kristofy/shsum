# SHSUM
## Description
An application capable of producing a consise summary of a manual page with usefull examples

## Intended Usecase
Example:  

```bash 
$ shsum ls
  # ls can be used to list the content of a dirictory
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
It implements the following [paper](https://arxiv.org/pdf/2109.00859v1.pdf)

The newer codeT5 model is codeT5+, also known as codeT5p, and it implements the following [paper](https://arxiv.org/pdf/2305.07922.pdf)

## Gathering data
The training data is not provided in this repository, instead a collection of fetching scripts are provided that should gather, compile and clean up the training data.  

### Requirements for the fetching scripts
- To gather the commads run 
```bash
compgen -c | grep -v '^_'| grep -v '[][(){}]' | grep -v '!' > data/commands
```
  - This will generate a list of all commands available on the system

- Get the tldr pages
```bash
git clone --depth=1 https://github.com/tldr-pages/tldr.git data/tldr
```
  - This will clone the tldr repository into the data folder
- Get the summaries from cheat.sh
```bash
mkdir data/cheat
cat data/commands | xargs -I {} curl -P 12 --header "Accept-Encoding: UTF-8" "https://cheat.sh/{}" -o "data/cheat/{}.md"
```
  - Adjust -P to the number of parallel downloads you want to run



