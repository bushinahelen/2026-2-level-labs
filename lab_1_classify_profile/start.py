"""
Language detection starter.
"""
from main.py import tokenize, calculate_frequencies, get_top_n_words, remove_stop_words

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
    assert result, "Detection result is None"

print(tokenize(text))
print(remove_stop_words(tokens, stop_words))
print(calculate_frequencies(tokens))
print(get_top_n_words(freq_dict, top_n))


if __name__ == "__main__":
    main()
