from flask import Blueprint, request
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

from config import SUMMARY_SENTENCE_COUNT, APP_NAME

summarize_text_path = Blueprint('summarize_text',APP_NAME)


@summarize_text_path.route('/summarize', methods=['POST'])
def summarize_text():
    """
    Summarize the incoming text and return a 3 sentence summary.
    :param request: Incoming request dict with the text to summarize
    :return str: A summary of the incoming text
    """
    input_text = request.json['text']
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=SUMMARY_SENTENCE_COUNT)
    summary_output = ''
    for sentence in summary:
        summary_output += str(sentence)
    return summary_output
