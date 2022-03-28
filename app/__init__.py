from app.anagram import AnagramService
from flask import Flask, request

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    service = AnagramService()
    service.load_dictionary('resources/dictionary.txt')

    @app.route('/')
    def acceptAnagramRequest():
        term = request.args.get("term", default="", type=str)
        return {
            "anagrams": service.get_anagrams(term),
        }

    return app