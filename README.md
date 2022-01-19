# Wordle Utils

## What is this?

Just a repo with some utilities that are helpful for solving wordle puzzles. Nothing fancy here and more may be added. If you have something that you think would be useful, open a Pull Request!

## Requirements

- Python 3.6+ 
- That's it!

## get_heterograms.py

***Heterogram: A word of phrase in which no letter occurs more than once***

Generates a new file containing only heterograms found in the provided wordlist.

```text
Usage:
    get_heterograms.py wordlist_file results_file
Parameters:
    wordlist_file: Path to the file containing the newline separated list of words to use
    results_file: Path to file where the results will be saved

```

### Example

```shell
  python3 get_heterograms.py word-lists/wordle.txt word-lists/heterograms.txt
```

## filter_by_letter_position.py

Takes a new-line separated list of words and 1 or more filter definitions (see below) and returns any words from the provided list that match the filter parameters.

```text
  Usage:
    filter_by_letter_position.py wordlist_file [filter]...
  Parameters:
    wordlist_file: Path to the file containing the newline separated list of words to filter
    filter: A string in the format `<pos>:<letter>`. Multiple filter arguments can be provided
```

### Examples

***find words where the first letter is "a" and the third is "s"***

```shell
  python3 filter_by_letter_position.py word-lists/heterograms.txt 1:a 3:s
```

