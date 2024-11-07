# SentenceRebuilder

## Overview
`SentenceRebuilder` is a Python program with a function that reconstructs a sentence by joining words according to specified lengths. Given a list of words and a list of lengths, the program will return a formatted sentence using the specified number of characters from each word.

## Features
- Accepts a list of words and corresponding word lengths.
- Rebuilds the sentence based on provided lengths.
- Returns a concise output with each word truncated to its specified length.

## Example

```python
from sentence_rebuilder import rebuild_sentence

# Example usage
words = ["the", "sky", "is", "blue"]
lengths = [3, 2, 2, 1]
result = rebuild_sentence(words, lengths)
print(result)  # Output: "the sk is b"
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/mahditalaldev/SentenceRebuilder.git
    cd SentenceRebuilder
    ```
   
2. Run the program and provide words and lengths as in the example.

## Function Details
- **`rebuild_sentence(words, lengths)`**:
  - **Arguments**: 
    - `words` (list of str): A list of words to be truncated.
    - `lengths` (list of int): The length to which each word should be truncated.
  - **Returns**: A single formatted sentence string.

## License
This project is licensed under the MIT License.
