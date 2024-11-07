def rebuild_sentence(words, lengths):
    # initialize empty string to saves the trimmed words
    trimmed_words = []
    
    # Loop through each word and its length
    for i in range(len(words)):
        word = words[i]          # Get the current word 
        length = lengths[i]      # Get the corresponding length
        
        # Trim the word according to length
        trimmed_word = word[:length]
        
        # Add the trimmed word to the list
        trimmed_words.append(trimmed_word)
    
    # Join the trimmed words  with spaces for the final sentence
    result = " ".join(trimmed_words)
    
    return result

# simple test
print(rebuild_sentence(["the", "sky", "is", "blue"], [3, 2, 2, 1]))  # Output: "the sk is b"
