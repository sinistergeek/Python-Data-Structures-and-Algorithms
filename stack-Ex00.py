class paranthesis_match:
    opening_brackets = ["(","{","["]
    closing_brackets = [")","}","]"]

    #declare constructor
    def __init__(self,expression):
        self.expression = expression
        self.stack=[]

    #push operation
    def push(self,element):
        self.stack.append(element)

    #pop operation
    def pop(self):
        if self.stack == []:
            print("Unbalanced Paranthesis")
        else:
            self.stack.pop()

    def is_match(self):

        print("expression is = ",self.expression)
        if len(self.expression)%2 == 0:
            for element in self.expression:
                print("evaluating",element)
                if element in self.opening_brackets:
                    print("It is an opening bracket -", element,"Pushing to stack")
                    self.push(element)
                    print("Pushed", element,"on to stack the stack is",self.stack)
                elif element in self.closing_brackets:
                    x=self.stack.pop()
                    print("time to pop element is",x)
                    if self.opening_brackets.index(x) == self.closing_brackets.index(element):
                        print("Match Found")
                    else:
                        print("Match not found - check paranthesis")
                        return;
        else:
            print("Unbalanced Paranthesis")
pm = paranthesis_match("([{}])")
pm.is_match()
