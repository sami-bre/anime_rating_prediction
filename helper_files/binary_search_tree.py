# data = ["action", "amine", "horror", "romance", "comedy", "drama"]

class Binary_tree:
    """remember that this class assumes to recieve stripped lowercase strings."""
    def __init__(self):
        self.head = ''
        self.dic = dict()
        self.arr = []
        

    def insert(self, element):
        if self.head == '':
            self.head = element
            self.dic[self.head] = ["", ""]
            self.arr.append(self.head)
        else:
            self.insert_with_head(self.head, element)

    def insert_with_head(self, head, element):
        if element == head:
            return                      # one base case
        choice = self.dic[head]
        left = element < head
        if left:
            if choice[0] == '':
                choice[0] = element     # another base case
                self.dic[element] = ['', '']
                self.arr.append(element)
            else:
                self.insert_with_head(choice[0], element)       # one recursive case
        else:
            if choice[1] == '':
                choice[1] = element     # yet another base case
                self.dic[element] = ['', '']
                self.arr.append(element)
            else:
                self.insert_with_head(choice[1], element)       # another recursive case


    def get_as_array(self):
        return self.arr

