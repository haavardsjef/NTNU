"""Function classes"""
import numbers
import numpy


class Function:
    """Function class"""

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """Executes function"""
        # Check type
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        # Report
        if debug is True:
            print("Function: " + self.func.__name__ + "({:f}) = {:f}".format(element, result))
        # Go home
        return result


class Operator:
    """Operator class"""

    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, element1, element2, debug=True):
        """Executes operation"""
        # Check type
        if not isinstance(element1, numbers.Number):
            raise TypeError("Cannot execute operation if element is not a number")
        result = self.operation(element1, element2)
        # Report
        if debug is True:
            print("Function: " + self.operation.__name__ +
                  "({:f},{:f}) = {:f}".format(element1, element2, result))
        # Go home
        return result

def test_operators():
    """Test that operators function properly"""
    add_op = Operator(numpy.add, 0)
    multiply_op = Operator(numpy.multiply, 1)
    print(add_op.execute(1, 2))
    print(add_op.execute(1, multiply_op.execute(2, 3)))

def test_functions():
    """Test that functions function properly"""
    exponential_func = Function(numpy.exp)
    sin_func = Function(numpy.sin)
    print(exponential_func.execute(sin_func.execute(0)))
