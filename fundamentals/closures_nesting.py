"""
Nested Functions
A nested function is a function defined inside another function.
It is useful for encapsulating helper functions within a scope.
The inner function can access variables from the outer function.
The inner function cannot be called outside its enclosing function.

Closures
A closure is a nested function that remembers variables in its scope.
It allows the inner function to retain values even after
the outer function has executed and returned.
Closures are created when the inner function references variables
from the enclosing function and is returned to the caller.
"""

def discount_calculator(discount_rate):
    """
    Outer function that sets the dicount rate.
    (Will remember the outer function argument values as closure call
    Returns an inner function that calculates the discounted prices.
    """

    # Nested function
    def calculate(price):
        """
        Inner function that calculates the discounted price.
        It 'remembers' the discount_rate from the outer function when it
        was created as a closure.
        """
        discounted_price = price - (price * discount_rate / 100)
        return discounted_price
    
    return calculate # Return the nested function (closure)


# Create a 10% discount calculator
ten_percent_discount = discount_calculator(10)

# Create a 25% discount calculator
twenty_five_percent_discount = discount_calculator(25)

# Use the discount calculators closures
original_price = 1000
print(f"Original Price: {original_price}")
print(f"10% Discount: {ten_percent_discount(original_price):.0f}")
print(f"25% Discount: {twenty_five_percent_discount(original_price):.0f}")