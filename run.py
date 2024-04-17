from flask import Flask, request

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from config import APP_NAME, SUMMARY_SENTENCE_COUNT

app = Flask(APP_NAME)


@app.route('/summarize', methods=['POST'])
def summarize_text():
    # Parse the input text
    input_text = request.json['text']
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, sentences_count=SUMMARY_SENTENCE_COUNT)
    summary_output = ''

    for sentence in summary:
        summary_output += str(sentence)

    return summary_output


if __name__ == '__main__':
    app.run()
