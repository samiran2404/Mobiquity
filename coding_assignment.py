class Process:
    def __init__(self, string):
        self.string = string
        self.nre = []

    def string_process(self):
        list_of_elements = list(self.string)
        for item in list_of_elements:
            if list_of_elements.count(item) == 1:
                self.nre.append(item)

        if len(self.nre) == 0:
            return None
        else:
            return self.nre[-1]


x = Process("abcbcbabcbabdecbbabcb")

y = x.string_process()

print(y)




