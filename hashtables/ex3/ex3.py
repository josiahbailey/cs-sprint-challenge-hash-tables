def intersection(arrays):
    """
    YOUR CODE HERE

    solution:
    loop over list
    loop over sub list within list
    save all items in first list to object
    on second loop save only the items that were already in the object
    so on so on
    """
    nums = {}
    output = []
    for item in arrays[0]:
        nums[item] = item

    for array in arrays:
        current = {}
        for item in array:
            if item in nums:
                current[item] = item
        nums = current
    for item in nums.values():
        output.append(item)
    return output


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
