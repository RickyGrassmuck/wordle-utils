#!/usr/bin/env python3

from email.policy import default
import os
import click

APPDIR = os.path.dirname(os.path.realpath(__file__))

def debug_print(msg):
  if os.environ.get("DEBUG") is not None:
    click.echo(f"[DEBUG] {msg}")
  return

def console_print(pager: bool, msg: str):
  if pager:
    click.echo_via_pager(msg)
  else:
    click.echo(msg)

def filter_words(words, excludes, filters):
  matches = []
  for w in words:
    if word_matches_filter(w, excludes, filters):
      matches.append(w)
  return matches

def word_matches_filter(word, excludes, filters):
  debug_print(f"Checking for match: {word}")
  for i, char in enumerate(filters):
    if char is None:
      continue
    if word[i] != char:
      return False
  if len(excludes) > 0:
    for ex in excludes:
      if ex in word:
        return False
  return True

def read_word_list(filepath):
  word_list_file = click.open_file(filepath)
  data = word_list_file.read().rstrip("\n").split("\n")
  word_list_file.close()
  return data

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

@click.command()
@click.option('-e', '--exclude', default=[], required=False, multiple=True, help="Exclude results with this string")
@click.option('-p/-np', '--pager/--no-pager', default=True,  help="Use the shells pager when printing output")
@click.option( '-c', '--show-count', default=False)
@click.option('-l', '--word-list', type=click.Choice(['accepted_guesses', 'answers', 'heterograms']), default="accepted_guesses")
@click.argument('filter_strings', nargs=-1, required=False)
def find_words(exclude, pager, show_count, word_list, filter_strings):
  """
  Filter words from a word list
  
  FILTER_STRINGS are strings in the format `pos:char`

  Example: main.py -l answers 1:s 3:a
  """
  debug_print(f"Excludes={exclude} wordlist-file={word_list} filter_string={filter_strings}")
  words = read_word_list(os.path.join(APPDIR, "word-lists", f"{word_list}.txt"))
  filter_list = parse_args(filter_strings)
  results = filter_words(words, exclude, filter_list)
  console_print(pager, "\n".join(results))
  if show_count:
    click.echo(f"Total Words: {len(results)}")

if __name__ == '__main__':
  find_words()