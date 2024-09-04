#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a series of prime number removal games.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list of integers where each integer n represents
        the upper limit of the set {1, 2, ..., n} for each round.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If there is no clear winner.

    Raises:
        None.
    """
    # Handle cases with invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores for Ben and Maria
    ben = 0
    maria = 0

    # Create a list 'a' with elements initialized to 1 for prime number
    # determination, where the length is the maximum value in nums plus 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]

    # Mark 0 and 1 as non-prime numbers in the list 'a'
    a[0], a[1] = 0, 0

    # Apply the Sieve of Eratosthenes to identify prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Play the game for each round defined in nums
    for i in nums:
        # Ben wins if the count of prime numbers in the range [1, i] is even
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner based on the number of rounds won
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Eliminates multiples of a given prime number from a list, marking them
    as non-prime.

    Args:
        ls (list of int): A list representing potential prime numbers.
        x (int): The prime number whose multiples are to be removed.

    Returns:
        None.

    Raises:
        None.
    """
    # Mark multiples of x as non-prime by setting corresponding elements to 0
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
