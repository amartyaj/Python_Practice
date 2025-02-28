#!/usr/bin/env python3


# Comparator class
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


# Closest numbers with same difference:
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


# Binary substrings:
# The 0's and 1's are grouped consecutively (e.g., 01, 10, 0011, 1100, 000111, etc.).
# The number of 0's in the substring is equal to the number of 1's in the substring.
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


# Minimum sum after k operations:
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


# Sorted subsequences:
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


# Number of courses with prerequisites:
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


# Maximize stock profit:
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


# Palindrome check
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = "".join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


# Example usage
input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


# Given n pairs of parentheses, generate all combinations of well-formed parentheses
def generate_parenthesis(n):
    def backtrack(open_count, close_count, current, result):
        # Base case: if we've used all parentheses, add the current combination to the result
        if open_count == n and close_count == n:
            result.append(current)
            return

        # If we can add an opening parenthesis, do so
        if open_count < n:
            backtrack(open_count + 1, close_count, current + "(", result)

        # If we can add a closing parenthesis, do so
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ")", result)

    result = []
    backtrack(0, 0, "", result)
    return result


if __name__ == "__main__":
    n = 3
    combinations = generate_parenthesis(n)
    print(f"All combinations of well-formed parentheses for n = {n}:")
    for combo in combinations:
        print(combo)


# Longest substring appearing exactly once (//String Str="HelloThereSIMPLEHELLOUSECASEHelloThere”, //String Str1=malayalamSampleStringmalayalam;)
def longest_unique_substring(s):
    # Dictionary to store the frequency of each substring
    substring_freq = {}

    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring in substring_freq:
                substring_freq[substring] += 1
            else:
                substring_freq[substring] = 1

    # Filter substrings that appear exactly once
    candidates = [substring for substring, freq in substring_freq.items() if freq == 1]

    # If no such substring exists, return an empty string
    if not candidates:
        return ""

    # Find the longest substring
    longest = max(candidates, key=lambda x: (len(x), s.index(x)))

    return longest


# Example usage
input_string1 = "helloheloINterviewhellohelo"
output1 = longest_unique_substring(input_string1)
print("Longest substring appearing exactly once (string example):", output1)

input_string2 = "1234568776655523123456"
output2 = longest_unique_substring(input_string2)
print("Longest substring appearing exactly once (numeric example):", output2)


# Number of islands (vertically or horizontally connected 1s form a single island - Confirm whether diagonal would also count, looks like it would)
def find_num_unique_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0
    unique_islands = set()

    def dfs(row, col, origin_row, origin_col, shape):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return

        # Mark the cell as visited
        grid[row][col] = 0

        # Record the relative position of the cell with respect to the origin
        shape.add((row - origin_row, col - origin_col))

        # Explore all 8 neighbors (horizontal, vertical, and diagonal)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                dfs(row + i, col + j, origin_row, origin_col, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Initialize a set to store the shape of the current island
                shape = set()
                dfs(r, c, r, c, shape)

                # Add the shape to the set of unique islands
                unique_islands.add(frozenset(shape))
                num_islands += 1

    return (num_islands, len(unique_islands))


if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]

    num_islands, num_unique_islands = find_num_unique_islands(matrix)
    print(f"Number of islands: {num_islands}")
    print(f"Number of unique islands: {num_unique_islands}")


# Trapped Rainwater:
def trap(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water


# Balanced brackets:
class BalancedBrackets:
    def is_balanced(self, s):
        """
        Determines if the given string of brackets is balanced.
        """
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map.values():  # Opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # Closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Ignore non-bracket characters (if any)
                continue

        # If the stack is empty, the string is balanced
        return not stack


# Example usage
if __name__ == "__main__":
    balanced_brackets = BalancedBrackets()
    test_cases = ["{}()", "{()}", "({()})", "{[}]", "{{{{", "))"]

    for s in test_cases:
        print(f"'{s}' is balanced: {balanced_brackets.is_balanced(s)}")

# Time complexity: O(n)
# Space complexity: O(n)


# Building Construction:
def max_sum_of_heights(maxHeight):
    n = len(maxHeight)
    if n == 0:
        return 0

    # Left pass: Ensure no building is a valley on its left side
    left = [0] * n
    left[0] = maxHeight[0]
    for i in range(1, n):
        left[i] = min(maxHeight[i], left[i - 1])

    # Right pass: Ensure no building is a valley on its right side
    right = [0] * n
    right[-1] = maxHeight[-1]
    for i in range(n - 2, -1, -1):
        right[i] = min(maxHeight[i], right[i + 1])

    # Calculate the final heights and their sum
    heights = [max(left[i], right[i]) for i in range(n)]
    return sum(heights)


# Example usage
maxHeight = [5, 10, 5, 10, 5]
print(f"Maximum possible sum of heights: {max_sum_of_heights(maxHeight)}")

# Time complexity: O(n)
# Space complexity: O(n)


# Student Class:
class Student:
    # Class-level variable to track the next enrollment number
    next_enrollment_number = 1

    def __init__(self, name):
        # Assign the current enrollment number to the student
        self.enrollment_number = Student.next_enrollment_number
        # Increment the enrollment number for the next student
        Student.next_enrollment_number += 1
        # Store the student's name
        self.name = name

    def __str__(self):
        # Return the student's information in the required format
        return f"{self.enrollment_number}: {self.name}"


# Example usage
if __name__ == "__main__":
    # Register students
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Charlie")

    # Print student information
    print(student1)  # Output: 1: Alice
    print(student2)  # Output: 2: Bob
    print(student3)  # Output: 3: Charlie


# Palindrome substrings:
def count_palindromic_substrings(s):
    n = len(s)
    # Create a DP table to store whether a substring is a palindrome
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0  # To store the total number of palindromic substrings

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Check for substrings longer than 2
    for length in range(3, n + 1):  # Length of the substring
        for i in range(n - length + 1):  # Starting index of the substring
            j = i + length - 1  # Ending index of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count


# Example usage
s = "tacocat"
print(f"Total number of palindromic substrings: {count_palindromic_substrings(s)}")

# Time complexity: O(n^2)
# Space complexity: O(n^2)
