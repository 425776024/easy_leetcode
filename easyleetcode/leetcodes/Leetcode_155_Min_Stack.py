
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
            return
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            # Push top of min stack again
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack) > 0:
            # Much simple than solution 1
            # But use more space
            self.min_stack.pop()
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return None
