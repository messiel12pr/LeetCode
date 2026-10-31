'''

    225. Implement Stack using Queues

'''

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return None

        counter = len(self.queue) - 1

        while counter != 0:
            self.queue.append(self.queue.pop(0))
            counter -= 1

        return self.queue.pop(0)

    def top(self) -> int:
        if not self.queue:
            return None

        counter = len(self.queue) - 1

        while counter != 0:
            self.queue.append(self.queue.pop(0))
            counter -= 1

        top_element = self.queue.pop(0)  
        self.queue.append(top_element)

        return top_element

    def empty(self) -> bool:
        if not self.queue:
            return True  

        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
