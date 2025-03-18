def product_of_others(nums):
    # Calculate the product of all elements in the list
    total_product = 1
    for num in nums:
        total_product *= num

    # Generate the output by dividing the total product by each element
    output = []
    for num in nums:
        output.append(str(total_product // num))

    return "*".join(output)


# Example usage
input_list = [2, 6, 3, 7]
output = product_of_others(input_list)
print("Output:", output)  # Output: 6*3*7, 2*3*7, 2*6*7, 2*6*3
