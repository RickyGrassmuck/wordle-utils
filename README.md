# Wordle Utils

## What is this?

Just a repo with some utilities that are helpful for solving wordle puzzles. Nothing fancy here and more may be added. If you have something that you think would be useful, open a Pull Request!

## Requirements

- Python 3.6+

## Setup
  
  ```pip3 install click```

## Usage

Takes a new-line separated list of words and 1 or more filter definitions (see below) and returns any words from the provided list that match the filter parameters.

```shell
Usage: main.py [OPTIONS] [FILTER_STRINGS]...

  Filter words from a word list

  FILTER_STRINGS are strings in the format `pos:char`

  Example: main.py -l answers 1:s 3:a

Options:
  -e, --exclude TEXT              Exclude results with this string
  -p, --pager / -np, --no-pager   Use the shells pager when printing output
  -c, --show-count BOOLEAN
  -l, --word-list [accepted_guesses|answers|heterograms]
  --help
```

## utils/get_heterograms.py

***Heterogram: A word of phrase in which no letter occurs more than once***

Generates a new file containing only heterograms found in the provided wordlist.

```text
Usage:
    get_heterograms.py wordlist_file results_file
Parameters:
    wordlist_file: Path to the file containing the newline separated list of words to use
    results_file: Path to file where the results will be saved

```
