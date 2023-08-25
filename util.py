#!/bin/env python3

import sys
import os
import time

def measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

def get_files_in_dir(dir):
  """returns a list of files in a directory, including subdirectories"""
  files = []
  for file in os.listdir(dir):
    entry_path = os.path.join(dir, file)
    files += get_files_in_dir(entry_path) if os.path.isdir(entry_path) else [entry_path]
    
  return files
