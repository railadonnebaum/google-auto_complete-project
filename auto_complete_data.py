try:
    import linecache
    from dataclasses import dataclass
except ImportError:
    print("Need to fix the installation")
    raise

@dataclass
class AutoCompleteData:
    def __init__(self, offset, source_text, score):
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score
        self.__completed_sentence = self.get_from_file_by_offset()

    def __str__(self) -> str:
        return f"{self.__completed_sentence} ({self.__source_text} {self.__score})"

    def get_from_file_by_offset(self):
        return linecache.getline(self.__source_text, self.__offset + 1)[:-2]

    def get_offset(self):
        return self.__offset

    def get_source_text(self):
        return self.__source_text
