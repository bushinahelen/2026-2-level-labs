"""
Language detection starter.
"""
from main import tokenize, calculate_frequencies, get_top_n_words, remove_stop_words

# pylint: disable=unused-variable, duplicate-code

def main() -> None:
    """
    Launches an implementation.
    """
    with open("lab_1_classify_profile/assets/texts/de.txt", "r", encoding="utf-8") as file:
        de_text = file.read()
    with open("lab_1_classify_profile/assets/texts/unknown.txt", "r", encoding="utf-8") as file:
        unknown_text = file.read()
    with open("lab_1_classify_profile/assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    with open("lab_1_classify_profile/assets/texts/en.txt", "r", encoding="utf-8") as file:
        en_text = file.read()
    result = None

    tokens = tokenize(unknown_text)
    print(tokens)

    tokens_without_stopwords = remove_stop_words(tokens, stopwords)
    print(tokens_without_stopwords)

    freq_dict = calculate_frequencies(tokens_without_stopwords)
    print(freq_dict)

    top_words = get_top_n_words(freq_dict, 10)
    print(top_words)

    assert result, "Detection result is None"


if __name__ == "__main__":
    main()
