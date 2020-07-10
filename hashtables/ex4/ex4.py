def has_negatives(a):
    """
    YOUR CODE HERE
    """
    output = []
    nums = {}
    for item in a:
        if item in nums:
            if item < 0:
                output.append(item - item - item)
            else:
                output.append(item)
        else:
            if item > 0:
                num = item - (item + item)
                nums[num] = num
            else:
                num = item - item - item
                nums[num] = num
            nums[num] = num

    return output


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
