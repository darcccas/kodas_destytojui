class Text:
    def __init__(self, txt: str):
        self.txt = txt

    def text_split(self) -> list:
        return self.txt.split()

    def find_word(self, fragment: str = "lge") -> list:
        return [
            word
            for word in self.text_split()
            if all(letter in word for letter in fragment)
        ]

    def find_word_len(self, word_len: int = 3) -> list:
        return [word for word in self.text_split() if len(word) >= word_len]


ran_txt = "Home is where the heart belongs, where comfort wraps around like a warm embrace. In the sanctuary of home, memories bloom, echoing laughter and stories. Home, a haven from life's storms, where every corner whispers tales of love and warmth. Home, the nucleus of belonging, where dreams take flight and souls find solace. Home, sweet home, where echoes of laughter and joy resonate through the walls, imprinting a sense of belonging that lingers in the heart forever."

txt = Text(ran_txt)

print(txt.find_word("is"))
print(txt.find_word_len(7))
