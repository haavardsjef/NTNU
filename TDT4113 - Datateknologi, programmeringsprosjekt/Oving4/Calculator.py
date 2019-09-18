"""Calculator by Håvard Hjelmeseth for TDT4113"""
import numpy
import numbers
from Function import Function, Operator
from Container import Queue, Stack


class Calculator:
    """Calculator class"""

    def __init__(self):
        # Definethe functions supported by linking them to Python
        # functions. These can be made elsewhere in the program ,
        # or imported ( e . g . , from numpy)
        self.functions = {"EXP": Function(numpy.exp),
                          "LOG": Function(numpy.log),
                          "SIN": Function(numpy.sin),
                          "COS": Function(numpy.cos),
                          "SQRT": Function(numpy.sqrt)}
        # Define the operators supported.
        # Link them to Python functions ( here : from numpy)
        self.operators = {"PLUSS": Operator(numpy.add, 0),
                          "GANGE": Operator(numpy.multiply, 1),
                          "DELE": Operator(numpy.divide, 1),
                          "MINUS": Operator(numpy.subtract, 0)}
        # Define the output−queue . The parse_text method fills this with RPN.
        # The evaluate output  queue method evaluates it.
        self.output_queue = Queue()

    def handle_RPN(self):
        stack = Stack()
        for element in self.output_queue._items:
            if isinstance(element, numbers.Number):
                stack.push(element)
            elif isinstance(element, Function):
                result = element.execute(stack.pop())
                stack.push(result)
            elif isinstance(element, Operator):
                a = stack.pop()
                b = stack.pop()
                result = element.execute(b, a)
                stack.push(result)
            else:
                raise Exception("Element ", element, " is not of a valid type")
        return stack.pop()

    def shunting_yard(self, input_queue):
        output_queue = Queue()
        operator_stack = Stack()
        for element in input_queue._items:
            if isinstance(element, numbers.Number):
                output_queue.push(element)
            elif isinstance(element, Function):
                operator_stack.push(element)
            elif element == "(":
                operator_stack.push(element)
            elif element == ")":
                while operator_stack.peek() != "(":
                    output_queue.push(operator_stack.pop())
                operator_stack.pop()
            elif isinstance(element, Operator):
                while (not operator_stack.is_empty()) and (isinstance(operator_stack.peek(), Function) or (isinstance(operator_stack.peek(), Operator) and operator_stack.peek().strength >= element.strength)):
                    output_queue.push(operator_stack.pop())
                operator_stack.push(element)
            else:
                raise Exception("Element ", element, " is not of a valid type")
        while not operator_stack.is_empty():
            output_queue.push(operator_stack.pop())
        self.output_queue = output_queue


    def string_parser(self, string):
        """Handles string parsing"""
        


def test_calculator():
    """Test the calculator class"""
    calc = Calculator()
    print(calc.functions["EXP"].execute(calc.operators["PLUSS"].execute(
        1, calc.operators["GANGE"].execute(2, 3))))

def test_RPN():
    """Tests that handling RPN works"""
    calc = Calculator()
    calc.output_queue.push(1)
    calc.output_queue.push(2)
    calc.output_queue.push(3)
    calc.output_queue.push(calc.operators["GANGE"])
    calc.output_queue.push(calc.operators["PLUSS"])
    calc.output_queue.push(calc.functions["EXP"])
    print(calc.handle_RPN())

def test_shunting_yard():
    """Test the shunting_yard algorithm"""
    calc = Calculator()
    input_queue = Queue()
    input_queue.push(calc.functions["EXP"])
    input_queue.push("(")
    input_queue.push(1)
    input_queue.push(calc.operators["PLUSS"])
    input_queue.push(2)
    input_queue.push(calc.operators["GANGE"])
    input_queue.push(3)
    input_queue.push(")")
    calc.shunting_yard(input_queue)
    print(calc.handle_RPN())



test_shunting_yard()
input()
