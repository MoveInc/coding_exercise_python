
class AnagramService:

    def __init__(self) -> None:
        self.dictionary = []

    def load_dictionary(self, filename) -> None:
        result = []
        with open(filename, 'r') as file:
            for word in file.readlines():
                result.append(word.strip())
        
        self.dictionary = result


    def get_anagrams(self, term):
        anagrams = []
        # your implementation here
        return anagrams

