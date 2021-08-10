try:
    from auto_complete_data import AutoCompleteData
except ImportError:
    print("Need to fix the installation")
    raise


class TrieNode:
    alphabet_size = 29

    # Trie node class
    def __init__(self, end=False):
        self.__children = [None] * type(self).alphabet_size
        # isEndOfWord is True if node represent the end of the word
        self.__is_end = end

    def set(self, char, val):
        if char == " ":
            self.__children[28] = val
            return
        self.__children[ord(char) - 97] = val

    def get(self, char):
        if char == " ":
            return self.__children[28]
        return self.__children[ord(char) - 97]

    def get_end(self):
        return self.__is_end

    def set_end(self, val):
        self.__is_end = val

    def add_child(self, char, end=False):
        node = TrieNode(end)
        self.set(char, node)

    def dfs(self, arr_completes, score):
        if self.get_end():
            for complete in self.get_end():
                if len(arr_completes) >= 5:
                    return
                exist = False
                for obj in arr_completes:
                    if obj.get_offset() == complete[0] and obj.get_source_text() == complete[1]:
                        exist = True
                        break
                if not exist:
                    arr_completes.append(AutoCompleteData(complete[0], complete[1], score))
            return
        for i in self.__children:
            if i is not None:
                i.dfs(arr_completes, score)
        return arr_completes

    def add_end(self, auto_complete):
        self.__is_end.append(auto_complete)
