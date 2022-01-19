#!/usr/bin/python3

import sys

def get_word_list(filepath):
  try:
    with open(filepath, "r") as word_file:
      data = word_file.read()
      words = data.split("\n")
    return words
  except FileNotFoundError:
    print(f"File not found: {filepath}\n")
    _help()
    exit(1)

def save_results(save_filepath, results):
  try:
    with open(save_filepath, "w") as save_file:
      save_file.write(results)
  except PermissionError as pe:
    print(f"\nUnable to save file: {save_filepath} - {pe.strerror}\n")
    exit(1)

def get_heterograms(word_list):
  heterograms = []
  for word in word_list:
    chars = set([char for char in word])
    if len(chars) == 5:
      heterograms.append(word)
  return heterograms

def _help():
  print('''
  Usage:
    get_heterograms.py wordlist_file results_file
  Parameters:
    wordlist_file: Path to the file containing the newline separated list of words to use
    results_file: Path to file where the results will be saved 
  '''
  )

if __name__ == '__main__':
  if sys.argv[1] == "--help":
    _help()
    exit(0)

  all_words_file = sys.argv[1]
  save_file = sys.argv[2]
  words = get_word_list(all_words_file)
  heterograms = get_heterograms(word_list=words)
  save_results(save_file, "\n".join(heterograms))
  print(F"{len(heterograms)} results saved to {save_file}")

          

