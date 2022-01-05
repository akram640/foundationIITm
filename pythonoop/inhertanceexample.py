class Question:
    def __init__(self,statement,marks):
        self.statement = statement
        self.marks = marks

    def print_question(self):
        print(self.statement)

    def update_marks(self,marks):
        self.marks = marks


class NAT(Question):
    def __init__(self,statement,marks,answer):
        super().__init__(statement,marks)
        self.answer = answer

    def update_answer(self,answer):
        self.answer = answer


## Method Overriding

class MCQ(Question):
    def __init__(self,statement,marks,ops,c_ops):
        super().__init__(statement,marks)
        self.ops = ops
        self.c_ops = c_ops

    def print_question(self):
        super().print_question()
        # Assume there are only four options
        op_index = ['(a)','(b)','(c)','(d)',]
        for i in range(4):
            print(op_index[i],self.ops[i])

q_nat = NAT('What is 1 + 2',1,3)
q_nat.update_marks(4)
print(q_nat.marks)


q_mcq = MCQ('What is the capital of India?',2,['chennai','Mumbai','kolkota','New Delhi'],['New Delhi'])

q_mcq.print_question()
