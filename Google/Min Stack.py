'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

        
class MinStack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        currentMin = None
        if self.stack:currentMin = min(self.getMin(), x)
        else: currentMin = x
        self.stack.append((x, currentMin))
        #print("push", self.stack)
        
    def pop(self) -> None:
        if self.stack: self.stack.pop()
    
            
    def top(self) -> int:
        if self.stack: return self.stack[len(self.stack)-1][0]
        

    def getMin(self) -> int:
        if self.stack:return self.stack[len(self.stack)-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
Thinking behind this seemed unintutitive. What you want to do is keep track of the current minimum at every at every point in the stack. 
This way when you remove the top of the stack the next value will know what the min value for the new stack is. 
Seems naive when you figure it out but honestly took a while to think about. Maybe there's a way to do this wiht less space
'''
