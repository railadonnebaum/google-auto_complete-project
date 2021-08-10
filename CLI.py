try:
    from auto_implement import Auto_Implement
    from initialize_db import Initialize_DB
    from trie import Trie
except ImportError:
    print("Need to fix the installation")
    raise


class CLI:
    def __init__(self):
        self.__auto_implement = Auto_Implement()
        self.__initialize_db = Initialize_DB()
        self.__trie = Trie()

    def run(self):
        print("Loading the files and preparing the system...")
        self.__initialize_db.run(self.__trie)
        while True:
            user_input = input("The system is ready. Enter your text:\n")
            while user_input[-1] != "#":
                res = self.__auto_implement.run(self.__trie, user_input[:20])
                if res:
                    print("Here are 5 suggestions")
                    for i in range(len(res)):
                        print(f'{i + 1}.{res[i]}')
                else:
                    print("query doe's not exit")
                    break
                user_input += input(user_input)
