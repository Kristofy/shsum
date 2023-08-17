# TODO / Roadmap

## Write model summary
- [ ] Summarize the purpose of the application
- [ ] Give examples of the expected behaviour
- [ ] Information about the base model


## Generate training data
- [ ] Get linux commands
- [ ] Querry man pages
- [ ] Get summary with tldr
- [ ] Get summary with bropages
- [ ] Get summary with cheat.sh
- [ ] Clean up the training data


## Training
- [ ] Look into the tokenizer used by the base model
- [ ] Check the best optimizer and loss function for fine-tuning (based on similar projects)
- [ ] Set up a small playground in google collab, which automatically updates and saves a modell on HuggingFace
  - [ ] Save on Error
  - [ ] Save on Finish
  - [ ] Perhaps track the progress in a versioning system so it is reversablex


## Application
- [ ] Write application leveraging the above mentioned finetuned model
  - [ ] If possible use the Huggigface api to querry the model
  - [ ] look into cpu consumption


## Finish up documentation
- [ ] Complete the README
- [ ] Write a huggingface card and make the model public

