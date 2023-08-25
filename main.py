#!/bin/env python3

import sys
import os

import concurrent.futures
import json

from cached import *
from util import *

COMMAND_LIST_FILE = "./data/commands"
DATASET_DIR = "./dataset"
TLDR_PAGES_DIR = "./data/tldr/pages"
CHEAT_DIR = "./data/cheat"

def get_command_list():
  with open(COMMAND_LIST_FILE) as f:
    return f.read().splitlines()

commands = get_command_list()

@measure
@cached()
def get_tldr_pages():
  """returns a list of tldr pages"""
  tldr_pages = [(page, os.path.splitext(path.split(page)[1])[0]) for page in get_files_in_dir(TLDR_PAGES_DIR)]
  tldr_pages = [(command, path) for (path, command) in tldr_pages if command in commands]
  tldr_pages = dict(tldr_pages)

  tldr_pages_dict = dict()
  def get_page(command):
    if command not in tldr_pages:
      return command, ''
    with open(tldr_pages[command]) as f:
      summary = f.read().strip()
      return command, summary
    
  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_page, command) for command in commands]
    
    for future in concurrent.futures.as_completed(futures):
        command, man_page = future.result()
        tldr_pages_dict[command] = man_page
  
  return tldr_pages_dict

@measure
@cached()
def get_man_pages():
  man_pages_dict = dict()

  # for command in commands:
  #   man_pages_dict[command] = os.popen(f"man {command}").read().strip()
  
  # # multi-threaded
  def get_page(command):
    man_page = os.popen(f"man {command}").read().strip()
    return command, man_page

  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_page, command) for command in commands]
    
    for future in concurrent.futures.as_completed(futures):
        command, man_page = future.result()
        man_pages_dict[command] = man_page

  return man_pages_dict

@measure
@cached()
def get_cheat_pages():
  cheat_pages_dict = dict()

  # for command in commands:
  #   path = f"{os.path.join(CHEAT_DIR, command)}.md"
  #   cheat_pages_dict[command] = os.popen(f"sed 's/[^[:print:]]\[[^a-zA-Z]*[a-zA-Z]//g' {path}").read().strip()

  # multi-threaded
  def get_page(command):
    path = f"{os.path.join(CHEAT_DIR, command)}.md"
    cheat_page = os.popen(f"sed 's/[^[:print:]]\[[^a-zA-Z]*[a-zA-Z]//g' {path}").read().strip()
    return command, cheat_page
  
  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_page, command) for command in commands]
    
    for future in concurrent.futures.as_completed(futures):
        command, cheat_page = future.result()
        cheat_pages_dict[command] = cheat_page

  return cheat_pages_dict

def main():
  man_pages = get_man_pages()
  tldr_pages = get_tldr_pages()
  cheat_pages = get_cheat_pages()

  print(cheat_pages['bc'])

if __name__ == "__main__":
  main()

