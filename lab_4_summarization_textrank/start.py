"""
TextRank summarizer starter
"""

# pylint:disable=unused-variable, unused-import, duplicate-code

from main import SentencePreprocessor, SentenceEncoder

def main() -> None:
    """
    Launches an implementation.

    In any case returns, None is returned
    """
    with open(
        "lab_4_summarization_textrank/assets/article_701.txt", "r", encoding="utf-8"
    ) as text_file:
        text = text_file.read()
    with open(
        "lab_4_summarization_textrank/assets/stop_words.txt", "r", encoding="utf-8"
    ) as text_file:
        stop_words = tuple(text_file.read().split("\n"))
    result = None
    sentence_processor = SentencePreprocessor(stop_words, '.!?')
    sentences = sentence_processor.get_sentences(text)
    sentence_encoder = SentenceEncoder()
    sentence_encoder.encode_sentences(sentences)
    assert all(sentence.get_encoded() for sentence in sentences)


if __name__ == "__main__":
    main()
