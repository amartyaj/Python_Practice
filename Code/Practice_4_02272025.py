print("\nNumber of islands:")


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


print("\nBalanced Brackets:")


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
balanced_brackets = BalancedBrackets()
test_cases = ["{}()", "{()}", "({()})", "{[}]", "{{{{", "))"]

for s in test_cases:
    print(f"'{s}' is balanced: {balanced_brackets.is_balanced(s)}")


print("\nString Subsequences:")


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


print("\nPalindrome Check:")


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

print(is_palindrome("abracadabra"))
print(is_palindrome("arbadadabra"))


print("\nWell formed parentheses:")


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


n = 3
combinations = generate_parenthesis(n)
print(f"All combinations of well-formed parentheses for n = {n}:")
for combo in combinations:
    print(combo)


print("\nLongest substring after removing longest repeated substring:")


def longest_substring_after_removal(s):
    if not s:
        return ""

    # Function to find the longest repeated substring
    def find_longest_repeated_substring(s):
        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i + 1, n):
                # Get the substring from i to j
                substring = s[i:j]
                # Check if this substring appears again in the string
                if s.count(substring) > 1 and len(substring) > len(longest):
                    longest = substring
        return longest

    # Find the longest repeated substring
    longest_repeated = find_longest_repeated_substring(s)

    # If no repeated substring exists, return the original string
    if not longest_repeated:
        return s

    # Remove all occurrences of the longest repeated substring
    result = s.replace(longest_repeated, "")

    return result


# Example usage
for input_string in [
    "HelloThereSIMPLEHELLOUSECASEHelloThere",
    "helloheloINterviewhellohelo",
    "1234568776655523123456",
]:
    output = longest_substring_after_removal(input_string)
    print("Longest substring after removing the longest repeated substring:", output)


print("\nLongest substring:")


def lengthOfLongestSubstring(s):
    maxLen = 1
    if s == "":
        return 0  # Dealing with one edge case
    for i in range(len(s)):
        substring = s[i]  # Initialising the substring
        for j in range(
            i + 1, len(s)
        ):  # Starting to append characters to substring from i+1
            if (
                s[j] not in substring
            ):  # As long as its not repeating. "not in" can be used to check if the character isn't already there in the substring
                substring = substring + s[j]
                maxLen = max(
                    maxLen, len(substring)
                )  # Updating maxLen if it is greater than the existing maxLen
            else:
                break
    return maxLen


print(lengthOfLongestSubstring("abcdab"))
