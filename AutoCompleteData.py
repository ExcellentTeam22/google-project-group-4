from dataclasses import dataclass
import linecache


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def __hash__(self):
        return hash((self.completed_sentence,self.source_text,self.offset))
    def set_score(self, score):
        self.score = score

    def __str__(self):
        return f'{self.completed_sentence} ({self.source_text} {self.offset})'

