class RateLimiter:
    """
    A dummy class to demonstrate docstring formatting.

    This class serves as an example for creating a Python class with a constructor and a simple method.

    Example:
        .. code-block:: python

            rate_limiter = RateLimiter(10)
            rate_limiter.increment(5)
            >>> 15

    Attributes:
        value (int): An integer value that can be incremented.

    """

    def __init__(self, value: int):
        """
        Initialize the DummyClass with a value.

        Args:
            value (int): The initial value to be stored in the class.
        """
        self.value = value

    def increment(self, amount: int) -> int:
        """
        Increment the stored value by a specified amount.

        Args:
            amount (int): The amount to increment the value by.

        Returns:
            int: The new value after incrementing.
        """
        self.value += amount
        return self.value