class Word:
    VALID_PARTS = {"n", "v", "adj", "adv", "prep"}

    def __init__(self, text, part_of_speech):
        pos = part_of_speech.strip().lower()
        if pos not in Word.VALID_PARTS:
            raise ValueError(f"Invalid part of speech: {part_of_speech!r}")
        self._text = text.strip().lower()
        self._part_of_speech = pos

    @property
    def text(self):
        return self._text
    
    @property
    def part_of_speech(self):
        return self._part_of_speech
    
    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return (self._text == other._text and self._part_of_speech == other._part_of_speech)
    
    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        if self._part_of_speech != other._part_of_speech:
            return self._part_of_speech < other._part_of_speech
        return self._text < other._text
    
    def __gt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        if self._part_of_speech != other._part_of_speech:
            return self._part_of_speech > other._part_of_speech
        return self._text > other._text
    
    def __hash__(self):
        return hash((self._text, self._part_of_speech))
    
    def __repr__(self):
        return f"Word({self._text!r}, {self._part_of_speech!r})"
    
    def __str__(self):
        return self._text