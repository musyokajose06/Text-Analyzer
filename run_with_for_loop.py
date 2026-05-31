from pythonAssessment import (
    count_specific_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences,
)


def main():
    test_cases = [
        {"text": "Hello world! Hello everyone. Welcome to the world of Python.", "word": "Hello"},
        {"text": "", "word": "test"},
        {"text": "One. Two. Three.", "word": "One"},
    ]

    for i, case in enumerate(test_cases, start=1):
        text = case["text"]
        word = case["word"]
        print(f"Case {i}:")
        print(f"  count_specific_word: {count_specific_word(text, word)}")
        print(f"  calculate_average_word_length: {calculate_average_word_length(text):.2f}")
        print(f"  count_paragraphs: {count_paragraphs(text)}")
        print(f"  count_sentences: {count_sentences(text)}")
        print()


if __name__ == "__main__":
    main()
