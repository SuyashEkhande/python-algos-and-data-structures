"""
Dynamic Programming Algorithms

This module contains classic dynamic programming problems and their solutions
with explanations of the approach and time complexity analysis.
"""


def fibonacci_dp(n):
    """
    Fibonacci using Dynamic Programming - O(n) time, O(n) space
    Classic example of optimization from recursive O(2^n) to linear time.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n):
    """
    Space-optimized Fibonacci - O(n) time, O(1) space
    Only keep track of the last two values.
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def longest_common_subsequence(text1, text2):
    """
    Longest Common Subsequence (LCS) - O(m*n) time and space
    Find length of longest subsequence common to both strings.
    
    Example: "ABCDGH" and "AEDFHR" -> "ADH" (length 3)
    """
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_with_string(text1, text2):
    """
    LCS that returns the actual subsequence string, not just length.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))


def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack Problem - O(n*W) time and space
    Each item can be taken at most once.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
    
    Returns:
        Maximum value that can be obtained
    """
    n = len(weights)
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i - 1][w]
            
            # Take item i-1 if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    return dp[n][capacity]


def knapsack_with_items(weights, values, capacity):
    """
    0/1 Knapsack that returns which items to take.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    # Backtrack to find items
    items = []
    i, w = n, capacity
    
    while i > 0 and w > 0:
        # If value didn't come from above, item was included
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)  # Add item index
            w -= weights[i - 1]
        i -= 1
    
    return dp[n][capacity], list(reversed(items))


def coin_change(coins, amount):
    """
    Coin Change Problem - O(amount * len(coins)) time
    Find minimum number of coins to make the given amount.
    
    Returns -1 if amount cannot be made.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """
    Coin Change II - Count number of ways to make amount.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    
    return dp[amount]


def longest_increasing_subsequence(nums):
    """
    Longest Increasing Subsequence (LIS) - O(n²) DP solution
    Find length of longest strictly increasing subsequence.
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def lis_optimized(nums):
    """
    LIS using Binary Search - O(n log n) time
    More efficient approach using patience sorting concept.
    """
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        left, right = 0, len(tails)
        
        # Binary search for position
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements, append
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)


def edit_distance(word1, word2):
    """
    Edit Distance (Levenshtein Distance) - O(m*n) time and space
    Minimum operations (insert, delete, replace) to convert word1 to word2.
    """
    m, n = len(word1), len(word2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]


def max_subarray_sum(nums):
    """
    Maximum Subarray Sum (Kadane's Algorithm) - O(n) time, O(1) space
    Find contiguous subarray with maximum sum.
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_product_subarray(nums):
    """
    Maximum Product Subarray - O(n) time, O(1) space
    Find contiguous subarray with maximum product.
    """
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result


def house_robber(nums):
    """
    House Robber Problem - O(n) time, O(1) space
    Rob houses to maximize money without robbing adjacent houses.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1


def house_robber_circular(nums):
    """
    House Robber II - Houses arranged in a circle
    Can't rob both first and last house.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    # Case 1: Rob houses 0 to n-2 (exclude last)
    case1 = house_robber(nums[:-1])
    
    # Case 2: Rob houses 1 to n-1 (exclude first)
    case2 = house_robber(nums[1:])
    
    return max(case1, case2)


def palindrome_partitioning_min_cuts(s):
    """
    Palindrome Partitioning II - O(n²) time and space
    Find minimum cuts needed to partition string into palindromes.
    """
    n = len(s)
    
    # Create palindrome lookup table
    is_palindrome = [[False] * n for _ in range(n)]
    
    # Every single character is palindrome
    for i in range(n):
        is_palindrome[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
    
    # DP for minimum cuts
    cuts = [0] * n
    
    for i in range(n):
        if is_palindrome[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = float('inf')
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
    
    return cuts[n - 1]


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Dynamic Programming Examples ===")
    
    # Fibonacci
    print("\n1. Fibonacci Numbers:")
    n = 10
    print(f"Fibonacci({n}) = {fibonacci_dp(n)}")
    print(f"Fibonacci({n}) optimized = {fibonacci_optimized(n)}")
    
    # LCS
    print("\n2. Longest Common Subsequence:")
    text1, text2 = "ABCDGH", "AEDFHR"
    lcs_length = longest_common_subsequence(text1, text2)
    lcs_string = lcs_with_string(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': length = {lcs_length}, string = '{lcs_string}'")
    
    # Knapsack
    print("\n3. 0/1 Knapsack Problem:")
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value = knapsack_01(weights, values, capacity)
    max_value_with_items, items = knapsack_with_items(weights, values, capacity)
    print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"Maximum value: {max_value}")
    print(f"Items to take (indices): {items}")
    
    # Coin Change
    print("\n4. Coin Change:")
    coins = [1, 3, 4]
    amount = 6
    min_coins = coin_change(coins, amount)
    ways = coin_change_ways(coins, amount)
    print(f"Coins: {coins}, Amount: {amount}")
    print(f"Minimum coins needed: {min_coins}")
    print(f"Number of ways: {ways}")
    
    # LIS
    print("\n5. Longest Increasing Subsequence:")
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_length = longest_increasing_subsequence(nums)
    lis_optimized_length = lis_optimized(nums)
    print(f"Array: {nums}")
    print(f"LIS length: {lis_length}")
    print(f"LIS length (optimized): {lis_optimized_length}")
    
    # Edit Distance
    print("\n6. Edit Distance:")
    word1, word2 = "horse", "ros"
    distance = edit_distance(word1, word2)
    print(f"Edit distance between '{word1}' and '{word2}': {distance}")
    
    # Maximum Subarray
    print("\n7. Maximum Subarray Sum:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(nums)
    print(f"Array: {nums}")
    print(f"Maximum subarray sum: {max_sum}")
    
    # Maximum Product Subarray
    print("\n8. Maximum Product Subarray:")
    nums = [2, 3, -2, 4]
    max_prod = max_product_subarray(nums)
    print(f"Array: {nums}")
    print(f"Maximum product subarray: {max_prod}")
    
    # House Robber
    print("\n9. House Robber:")
    houses = [2, 7, 9, 3, 1]
    max_money = house_robber(houses)
    circular_houses = [2, 3, 2]
    max_money_circular = house_robber_circular(circular_houses)
    print(f"Houses: {houses}")
    print(f"Maximum money (linear): {max_money}")
    print(f"Houses (circular): {circular_houses}")
    print(f"Maximum money (circular): {max_money_circular}")
    
    # Palindrome Partitioning
    print("\n10. Palindrome Partitioning (Min Cuts):")
    s = "aab"
    min_cuts = palindrome_partitioning_min_cuts(s)
    print(f"String: '{s}'")
    print(f"Minimum cuts for palindrome partitioning: {min_cuts}")
    
    print(f"\nNote: All DP solutions optimize recursive approaches by:")
    print("1. Memoization (top-down) or Tabulation (bottom-up)")
    print("2. Avoiding redundant computations")
    print("3. Trading space for time complexity improvements")