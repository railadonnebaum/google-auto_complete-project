try:
    from string import ascii_lowercase
except ImportError:
    print("Need to fix the installation")
    raise


class Auto_Implement:
    def __init__(self):
        pass

    def run(self, trie, string):
        res = trie.search(string, 0, [])
        if len(res) >= 5:
            return res
        res = self.switching_manipulation(trie, string, res, -1)
        if len(res) >= 5:
            return res
        res = self.erase_manipulation(trie, string, res, -2)
        if len(res) >= 5:
            return res
        res = self.insert_manipulation(trie, string, res, -2)
        if len(res) >= 5:
            return res
        res = self.switching_manipulation(trie, string, res, -2, 3)
        if len(res) >= 5:
            return res
        res = self.switching_manipulation(trie, string, res, -3, 2)
        if len(res) >= 5:
            return res
        res = self.switching_manipulation(trie, string, res, -4, 1)
        if len(res) >= 5:
            return res
        res = self.erase_manipulation(trie, string, res, -4, 3)
        if len(res) >= 5:
            return res
        res = self.insert_manipulation(trie, string, res, -4, 3)
        if len(res) >= 5:
            return res
        res = self.switching_manipulation(trie, string, res, -5, 0)
        if len(res) >= 5:
            return res
        res = self.insert_manipulation(trie, string, res, -6, 2)
        if len(res) >= 5:
            return res
        res = self.erase_manipulation(trie, string, res, -6, 2)
        if len(res) >= 5:
            return res
        res = self.insert_manipulation(trie, string, res, -8, 1)
        if len(res) >= 5:
            return res
        res = self.erase_manipulation(trie, string, res, -8, 1)
        if len(res) >= 5:
            return res
        res = self.insert_manipulation(trie, string, res, -10, 0)
        if len(res) >= 5:
            return res
        res = self.erase_manipulation(trie, string, res, -10, 0)
        return res

    def switching_manipulation(self, trie, string, res, score, index=None):
        if index is None and len(string) > 5:
            for i in range(len(string) - 1, 5):
                for letter in ascii_lowercase:
                    if len(res) >= 5:
                        return res
                    temp_string = string[:i] + letter + string[i + 1:]
                    res = trie.search(temp_string, score - 1, res)
        elif index is None:
            return res
        else:
            for letter in ascii_lowercase:
                if len(res) >= 5:
                    return res
                temp_string = string[:index] + letter + string[index + 1:]
                res = trie.search(temp_string, score - 1, res)
        return res

    def erase_manipulation(self, trie, string, res, score, index=None):
        if index is None and len(string) > 4:
            for i in range(4, len(string) + 1):
                if len(res) >= 5:
                    return res
                res = trie.search(string[:i - 1] + string[i:], score - 1, res)
        elif index is None:
            return res
        else:
            res = trie.search(string[:index - 1] + string[index:], score - 1, res)
        return res

    def insert_manipulation(self, trie, string, res, score, index=None):
        if index == None and len(string) > 4:
            for i in range(len(string), 4):
                if len(res) >= 5:
                    return res
                for j in range(97, 123):
                    res = trie.search(string[:i] + chr(j) + string[i:], score - 1, res)
        elif index is None:
            return res
        else:
            res = trie.search(string[:index] + " " + string[index:], score - 1, res)
        return res
