# SentenceRebuilder

## Overview
`SentenceRebuilder` is a Python program that reconstructs a sentence by joining words according to specified lengths. Given a list of words and a list of lengths, the program will output a formatted sentence, using the specified number of characters from each word.

## Features
- Reads a sentence and word lengths directly from user input.
- Rebuilds the sentence based on specified lengths.
- Returns a concise output with each word truncated to its specified length.

## Example

```python
# Import or define the rebuild_sentence function and helper functions in sentence_rebuilder.py
from sentence_rebuilder import rebuild_sentence, read_user_word, read_user_word_length

# Example usage
words = read_user_word()  # Input: "the sky is blue"
lengths = read_user_word_length()  # Input: "3 2 2 1"
result = rebuild_sentence(words, lengths)
print(result)  # Output: "the sk is b"
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/mahditalaldev/SentenceRebuilder.git
    cd SentenceRebuilder
    ```

2. Run the program and follow the prompts to enter a sentence and the word lengths.

3. Example usage:
    - When prompted, enter a sentence:
      ```
      enter your sentence : the sky is blue
      ```
    - Then enter the lengths for each word:
      ```
      enter length of each word : 3 2 2 1
      ```

    - The program will output:
      ```
      the sk is b
      ```

## Function Details
- **`rebuild_sentence(words, lengths)`**:
  - **Arguments**: 
    - `words` (list of str): A list of words to be truncated.
    - `lengths` (list of int): The length to which each word should be truncated.
  - **Returns**: A single formatted sentence string with words truncated as specified.

- **`read_user_word()`**:
  - **Returns**: A list of words entered by the user.

- **`read_user_word_length()`**:
  - **Returns**: A list of word lengths entered by the user.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
