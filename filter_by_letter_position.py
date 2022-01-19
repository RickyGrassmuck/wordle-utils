import os
import sys

def debug_print(msg):
  if os.environ.get("DEBUG") is not None:
    print(f"[DEBUG] {msg}")
  return

def word_matches_filter(word, filter_list):
  debug_print(f"Checking for match: {word}")
  for i, char in enumerate(filter_list):
    if char is None:
      continue
    if word[i] != char:
      return False
  return True

def read_word_list(filepath):
  try:
    with open(filepath, "r") as word_file:
      data = word_file.read()
      data_stripped = data.rstrip("\n")
      words = data_stripped.split("\n")
    return words
  except FileNotFoundError:
    print(f"File not found: {filepath}\n")
    exit(1)

def parse_args(args):
  filter_list = [None, None, None, None, None]
  for a in args:
    position_str, char = a.split(":")
    try:
      pos = int(position_str)
      if pos > 6:
        print(f"\nInvalid Position [{a}]: {pos} must be between 1 - 5\n")
        exit(1)
      if pos < 1:
        print(f"\nInvalid Position [{a}]: {pos} must be between 1 - 5\n")
        exit(1)
      if len(char) != 1:
        print(f"\nInvalid Position [{a}]: {pos} must be between 1 - 5\n")
        exit(1)
      if not char.isalpha():
        print(f"\nFilter value must be a single ascii letter - Arg: {a} Value: {char}\n")
        exit(1)
    except TypeError as e:
      print(f"Error: {e}")
      exit(1)

    filter_list[pos - 1] = char
  return filter_list

def _help():
  print('''
  Usage:
    filter_by_letter_position.py wordlist_file [filter]...
  Parameters:
    wordlist_file: Path to the file containing the newline separated list of words to filter
    filter: A string in the format `<pos>:<letter>`. Multiple filter arguments can be provided
  Example:
    ** find words where the first letter is a and the third is s 
      python3 filter_by_letter_position.py wordlist.txt 1:a 3:s
  '''
  )

if __name__ == '__main__':
  if sys.argv[1] == "--help":
    _help()
    exit(0)
  words = read_word_list(sys.argv[1])
  filter_list = parse_args(sys.argv[2:])
  
  matches = []
  for w in words:
    if word_matches_filter(w, filter_list):
      matches.append(w)
  
  print("\n".join(matches))