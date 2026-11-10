"""
Generation by NGrams starter
"""

from main import GreedyTextGenerator, NGramLanguageModel, TextProcessor


def main() -> None:
    """
    Launches an implementation.

    In any case returns, None is returned
    """
    with open(
        "./lab_3_generate_by_ngrams/assets/Harry_Potter.txt", "r", encoding="utf-8"
    ) as text_file:
        text = text_file.read()

    text_processor = TextProcessor('_')
    encoded_corpus = text_processor.encode(text)
    n_gram_language_model = NGramLanguageModel(encoded_corpus, n_gram_size=7)
    n_gram_language_model.build()
    greedy_text_generator = GreedyTextGenerator(n_gram_language_model, text_processor)
    generated_text = greedy_text_generator.run('Vernon', 51)
    print(generated_text)

if __name__ == "__main__":
    main()