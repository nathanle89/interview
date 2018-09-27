class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.currentMinStack = []
        self.elementsLength = 0
        self.currentMinLength = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        self.elementsLength += 1
        if self.currentMinLength == 0 or x <= self.currentMinStack[-1]:
            self.currentMinStack.append(x)
            self.currentMinLength += 1

    def pop(self):
        """
        :rtype: void
        """
        if self.elementsLength == 0:
            return

        if self.top() == self.currentMinStack[-1]:
            self.currentMinStack.pop()
            self.currentMinLength -= 1
        self.elements.pop()
        self.elementsLength -= 1

    def top(self):
        """
        :rtype: int
        """
        if self.elementsLength == 0:
            return None

        return self.elements[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.currentMinLength == 0:
            return None

        return self.currentMinStack[-1]

solution = MinStack()

solution.push(-2)
solution.push(0)
solution.push(-3)
print(solution.getMin())
solution.pop()
print(solution.top())
print(solution.getMin())

