from word import Word

class WordCollection:
    def __init__(self):
        self._words = []

    @classmethod
    def from_file(cls, filepath):
        collection = cls()
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 2:
                    continue
                text, pos = parts
                try:
                    collection.add(Word(text, pos))
                except ValueError:
                    continue
        return collection
    
    def add(self, word):
        if not isinstance(word, Word):
            raise TypeError("Only Word instances may be added.")
        self._words.append(word)

    def filter_by_pos(self, part_of_speech):
        pos = part_of_speech.strip().lower()
        result = WordCollection()
        for w in self._words:
            if w.part_of_speech == pos:
                result.add(w)
        return result
    
    def sorted_words(self, reverse=False):
        result = WordCollection()
        result._words = sorted(self._words, reverse=reverse)
        return result
    
    def __len__(self):
        return len(self._words)
    
    def __getitem__(self, index):
        return self._words[index]
    
    def __contains__(self, item):
        return item in self._words
    
    def __iter__(self):
        return iter(self._words)
    
    def __repr__(self):
        return f"WordCollection({len(self._words)} words)"