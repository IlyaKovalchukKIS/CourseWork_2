class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"class BasicWord({self.word} - word,\n" \
               f"{self.subwords} - sudwords)"

    def check_subwords(self, user_subword):
        return user_subword in self.subwords
