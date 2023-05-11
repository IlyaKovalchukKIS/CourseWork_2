class Player:
    def __init__(self, name_user: str):
        self.name_user = name_user
        self.use_word = []

    def __repr__(self):
        return f"class Player({self.name_user} - name_user)"

    def use_user_word(self, word_user: str):
        if word_user not in self.use_word:
            self.use_word.append(word_user)
