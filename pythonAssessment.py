def count_specific_word(text, word):
    # Split the text into words and count the occurrences of the specific word
    words = text.split()
    return words.count(word)


def calculate_average_word_length(text):
    # Split the text into words and calculate the total length and count of words
    words = text.split()
    total_length = sum(len(word) for word in words)
    word_count = len(words)

    # Avoid division by zero
    if word_count == 0:
        return 0.0

    return total_length / word_count


def count_paragraphs(text):
    # Split the text into paragraphs based on newline characters
    paragraphs = text.split('\n\n')
    return len(paragraphs)


def count_sentences(text):
    # Split the text into sentences based on punctuation marks
    sentences = text.split('.')
    return len(sentences) - 1  # Subtract 1 to account for the last split being empty if text ends with a period


# Entry point for testing the functions
if __name__ == "__main__":
    # Get user input for text
    print("=== Text Manipulation Tool ===")
    sample_text = input("Enter the text you want to analyze: ")
    
    # Get user input for the specific word to count
    word_to_count = input("Enter the word you want to count: ")
    
    print("\n--- Results ---\n")
    
    # Test the count_specific_word function 
    result = count_specific_word(sample_text, word_to_count)
    print(f"The word '{word_to_count}' appears {result} times in the text.")

    # Test the calculate_average_word_length function
    average_length = calculate_average_word_length(sample_text)
    print(f"The average word length in the text is {average_length:.2f} characters.")

    # Test the count_paragraphs function
    paragraph_count = count_paragraphs(sample_text)
    print(f"The number of paragraphs in the text is {paragraph_count}.")

    # Test the count_sentences function
    sentence_count = count_sentences(sample_text)
    print(f"The number of sentences in the text is {sentence_count}.")


    