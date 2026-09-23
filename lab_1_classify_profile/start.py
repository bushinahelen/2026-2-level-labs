"""
Language detection starter.
"""
from lab_1_classify_profile.main import (
    tokenize,
    remove_stop_words,
    calculate_frequencies,
    get_top_n_words
)

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

    tokens = tokenize(de_text)
    if tokens is None:
        return None

    tokens_without_stopwords = remove_stop_words(tokens, stopwords)
    if tokens_without_stopwords is None:
        return None

    freq_dict = calculate_frequencies(tokens_without_stopwords)
    if freq_dict is None:
        return None

    result = get_top_n_words(freq_dict, 7)
    if result is None:
        return None

    assert result, "Detection result is None"
    print(result)


if __name__ == "__main__":
    main()
