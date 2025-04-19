# Create a dummy python class with a constructor and simple method. 
# Both constructor and method should have docstrings to describe purpose, arguments, and return values.
# Make sure the docstrings are compatible with Sphinx:

class RateLimiter:
    """
    A dummy class to demonstrate docstring formatting.

    This class serves as an example for creating a Python class with a constructor and a simple method.
    """

    def __init__(self, value: int):
        """
        Initialize the DummyClass with a value.

        :param value: An integer value to initialize the class.
        """
        self.value = value

    def increment(self, amount: int) -> int:
        """
        Increment the stored value by a specified amount.

        :param amount: The amount to add to the stored value.
        :return: The new value after incrementing.
        """
        self.value += amount
        return self.value