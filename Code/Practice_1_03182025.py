#!/usr/bin/env python3


def trapped_rainwater(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    water = 0

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(height[i], left_max[i - 1])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])

    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


if __name__ == "__main__":
    heights = [4, 3, 2, 1, 2, 5]
    # heights = [2, 1, 1, 1, 2]

    total_water = trapped_rainwater(heights)
    print(total_water)
