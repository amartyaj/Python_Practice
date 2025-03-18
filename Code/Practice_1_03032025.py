#!/usr/bin/env python3


def clean_up(amount, coins):
    pass

    coins.sort()
    coins = list(set(coins))
    coins = [coin for coin in coins if coin <= amount]
    coins.reverse()

    result = coins
    return result


def calc_path(amount, coins):
    pass

    def backtrack(target, start, path, result):
        pass
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(coins)):
            if coins[i] > target:
                # result.append(path)
                continue

            backtrack(target - coins[i], i, path + [coins[i]], result)

    start = 0
    path = []
    result = []

    backtrack(amount, start, path, result)

    return result


if __name__ == "__main__":
    pass

    N = 5
    C = [2, 3, 1, 6, 7, 8, 9, 5, 1, 2, 3, 4]

    C = clean_up(N, C)
    paths = calc_path(N, C)

    print(paths)


def clean_up(amount, coins):
    pass

    coins.sort()
    coins = list(set(coins))
    coins = [coin for coin in coins if coin <= amount]
    coins.reverse()

    result = coins
    return result


def calc_path(amount, coins):
    pass

    def backtrack(target, start, path, result):
        pass
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(coins)):
            if coins[i] > target:
                # result.append(path)
                continue

            backtrack(target - coins[i], i, path + [coins[i]], result)

    start = 0
    path = []
    result = []

    backtrack(amount, start, path, result)

    return result


if __name__ == "__main__":
    pass

    N = 5
    C = [2, 3, 1, 6, 7, 8, 9, 5, 1, 2, 3]

    C = clean_up(N, C)
    paths = calc_path(N, C)

    print(paths)


class Comparator:
    def compare(self, a, b):
        """
        Compare two values (string, number, or list of numbers).
        Returns:
            -1 if a < b
            0 if a == b
            1 if a > b
        """
        if isinstance(a, str) and isinstance(b, str):
            return self._compare_strings(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return self._compare_numbers(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return self._compare_number_lists(a, b)
        else:
            raise TypeError("Unsupported types for comparison")

    def _compare_strings(self, a: str, b: str) -> int:
        """
        Compare two strings.
        """
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def _compare_numbers(self, a: (int, float), b: (int, float)) -> int:
        """
        Compare two numbers (int or float).
        """
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def _compare_number_lists(self, a: list, b: list) -> int:
        """
        Compare two lists of numbers.
        Lists are compared element-wise.
        """
        for x, y in zip(a, b):
            if x < y:
                return -1
            elif x > y:
                return 1
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0


# Example usage
if __name__ == "__main__":
    comparator = Comparator()

    # Compare strings
    print(comparator.compare("apple", "banana"))  # Output: -1 ("apple" < "banana")

    # Compare numbers
    print(comparator.compare(10, 5))  # Output: 1 (10 > 5)

    # Compare lists of numbers
    print(
        comparator.compare([1, 2, 3], [1, 2, 4])
    )  # Output: -1 ([1, 2, 3] < [1, 2, 4])
    print(comparator.compare([1, 2, 3], [1, 2, 3]))  # Output: 0 (lists are equal)
    print(
        comparator.compare([1, 2, 3, 4], [1, 2, 3])
    )  # Output: 1 (first list is longer)


def closest_numbers(numbers):
    if not numbers or len(numbers) < 2:
        return []

    # Sort the array
    numbers.sort()

    # Find the minimum absolute difference
    min_diff = float("inf")
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff < min_diff:
            min_diff = diff

    # Find all pairs with the minimum absolute difference
    pairs = []
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff == min_diff:
            pairs.append((numbers[i - 1], numbers[i]))

    # Print the pairs
    for pair in pairs:
        print(pair[0], pair[1])


# Example usage
if __name__ == "__main__":
    numbers = [6, 2, 4, 10]
    closest_numbers(numbers)


def count_binary_substrings(s):
    if not s:
        return 0

    result = 0
    prev_count = 0
    curr_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_count += 1
        else:
            # When a transition occurs, calculate the number of valid substrings
            result += min(prev_count, curr_count)
            prev_count = curr_count
            curr_count = 1

    # Handle the last group of 0s or 1s
    result += min(prev_count, curr_count)

    return result


# Example usage
if __name__ == "__main__":
    s = "001101"
    print("Number of valid binary substrings:", count_binary_substrings(s))


def minimize_sum(nums, k):
    for _ in range(k):
        # Find the index of the largest element in the array
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i

        # Perform the operation on the largest element
        largest = nums[max_index]
        new_value = (largest // 2) + (1 if largest % 2 != 0 else 0)
        nums[max_index] = new_value

    # Calculate the sum of the final array
    return sum(nums)


# Example usage
if __name__ == "__main__":
    nums = [10, 20, 7]
    k = 4
    result = minimize_sum(nums, k)
    print("Minimized sum after", k, "operations:", result)


def generate_subsequences(s):
    def backtrack(index, path):
        if index == len(s):
            if path:  # Exclude the empty string
                subsequences.append("".join(path))
            return
        # Include the current character
        backtrack(index + 1, path + [s[index]])
        # Exclude the current character
        backtrack(index + 1, path)

    subsequences = []
    backtrack(0, [])
    subsequences.sort()  # Sort the subsequences alphabetically
    return subsequences


# Example
s = "xyz"
result = generate_subsequences(s)
print(result)


def can_finish(numCourses, prerequisites):
    # Step 1: Build the graph using a list of lists
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # Step 2: Detect cycles using DFS
    visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited

    def has_cycle(course):
        if visited[course] == 1:
            return True  # Cycle detected
        if visited[course] == 2:
            return False  # Already processed, no cycle

        visited[course] = 1  # Mark as visiting

        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True

        visited[course] = 2  # Mark as visited
        return False

    # Step 3: Check for cycles in all courses
    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True


# Example usage
if __name__ == "__main__":
    # Example 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print("Example 1:", can_finish(numCourses1, prerequisites1))  # Output: True

    # Example 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print("Example 2:", can_finish(numCourses2, prerequisites2))  # Output: False


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the potential profit
        potential_profit = price - min_price
        # Update the maximum profit if the potential profit is greater
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit


# Example usage
if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Max profit for prices1:", max_profit(prices1))  # Output: 5

    prices2 = [7, 6, 4, 3, 1]
    print("Max profit for prices2:", max_profit(prices2))  # Output: 0

    prices3 = [7, 2, 5, 3, 6, 4, 1]
    print("Max profit for prices3:", max_profit(prices3))  # Output: 4
