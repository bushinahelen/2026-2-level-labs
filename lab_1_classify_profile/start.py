"""
Language detection starter.
"""
from lab_1_classify_profile.main import (
    tokenize,
    remove_stop_words,
    calculate_frequencies,
    get_top_n_words, create_language_profile, check_profile
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
    tokens_without_stopwords = remove_stop_words(tokens, stopwords)
    freq_dict = calculate_frequencies(tokens_without_stopwords)
    dictionary = get_top_n_words(freq_dict, 7)

    # de_profile = create_language_profile("de", de_text, stopwords)
    # en_profile = create_language_profile("en", en_text, stopwords)
    # assert check_profile(de_profile) and check_profile(en_profile), "Detection result is None"

    assert dictionary, "Detection result is None"
    print(dictionary)


if __name__ == "__main__":
    main()
