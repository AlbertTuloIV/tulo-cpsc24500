import random

class StoryTemplate:
    def __init__(self, name, pattern):
        self._name = name
        self._pattern = list(pattern)

    @property
    def name(self):
        return self._name
    
    @property
    def pattern(self):
        return self._pattern
    
    def generate(self, words):
        tokens = []
        for token in self._pattern:
            if token.startswith("{") and token.endswith("}"):
                pos = token[1:-1]
                pool = words.filter_by_pos(pos)
                if len(pool) == 0:
                    tokens.append(token)
                else:
                    tokens.append(str(random.choice(list(pool))))
        
        sentence = " ".join(tokens).strip()
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        return sentence + "."
    
TEMPLATES = [
    StoryTemplate("Adventure", [
        "The", "{adj}", "{n}", "{v}", "{adv}",
        "{prep}", "the", "{adj}", "{n}"
    ]),
    StoryTemplate("Mystery", [
        "A", "{adj}", "{n}", "{adv}", "{v}",
        "while", "the", "{n}", "{v}",
        "{prep}", "the", "{n}"
    ]),
    StoryTemplate("Simple", [
        "The", "{adj}", "{n}", "{v}", "{adv}"
    ]),
]