

class Anagram:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError("Word must be a string")
        self.word = sorted(word.lower()) 

    def match(self, word_list):
        if not isinstance(word_list, list):
            raise ValueError("Input must be a list")

        matches = []
        for w in word_list:
            if sorted(w.lower()) == self.word:
                matches.append(w)
        return matches
