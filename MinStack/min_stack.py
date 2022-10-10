class MinStack:

    def __init__(self):
        self.my_list = []

        

    def push(self, val: int) -> None:
        self.my_list.append(val);

        

    def pop(self) -> None:
        del self.my_list[-1]

        

    def top(self) -> int:
        return self.my_list[-1]
        

    def getMin(self) -> int:
        new_list = self.my_list.copy()
        new_list.sort()
        return new_list[0]