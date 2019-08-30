class MinStack:
    def __init__(self):
        # do intialization if necessary
        self.array = []

        """
        @param: number: An integer
        @return: nothing
        """

    def push(self, number):
        # write your code here
        self.array.append(number)
        """
        @return: An integer
        """

    def pop(self):
        # write your code here
        if self.array:
            num = self.array.pop()
        else:
            raise LookupError('stack is empty!')
        return num
        """
        @return: An integer
        """

    def min(self):
        # write your code here
        num = self.array[0]
        for min in self.array:
            if min < num:
                num = min
        return num

if __name__ == '__main__':
    s = MinStack()
    s.push(1)
    print(s.min())
    s.push(2)
    print(s.min())