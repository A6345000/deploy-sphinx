# create a template class for the calculation engine:
# this class will be return a recursive function to calculate the value of the fibonacci sequence.
# The class will include docstrings for each function and the class itself.

class FibonacciEngine:
    """
    A class to calculate the Fibonacci sequence using a recursive function.

    .. math::
        F(n) = F(n-1) + F(n-2)

    .. math::
        F(0) = 0
        
    .. math::
        F(1) = 1
        
    Attributes:
        n (int): The position in the Fibonacci sequence to calculate.
    """

    def __init__(self, n):
        """
        Initializes the FibonacciEngine with a given position in the sequence.

        Args:
            n (int): The position in the Fibonacci sequence to calculate.

        """
        self.n = n

    def calculate(self):
        """
        Calculates the Fibonacci number at the given position using recursion.

        Returns:
            int: The Fibonacci number at the given position.
        """
        return self._fibonacci_recursive(self.n)

    def _fibonacci_recursive(self, n):
        """
        A private recursive function to calculate the Fibonacci number.

        Args:
            n (int): The position in the Fibonacci sequence to calculate.

        Returns:
            int: The Fibonacci number at the given position.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self._fibonacci_recursive(n - 1) + self._fibonacci_recursive(n - 2)
