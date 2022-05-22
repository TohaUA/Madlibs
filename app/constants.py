import enum


@enum.unique
class WordType(enum.Enum):
    ADJECTIVE = 'adjective'
    VERB = 'verb'
    NOUN = 'noun'
