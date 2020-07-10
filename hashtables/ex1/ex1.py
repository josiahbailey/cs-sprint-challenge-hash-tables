def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    inputs: list of weights, weight limit
    output: tuple with 2 weights that equal the limit
    implement object somehow to speed the process up from O(n^2) to O(n)

    solution 1:
    loop in range of limit that saves every sum combination of aditives in dictionary

    loop through weights
    add each weight to a dictionary
    until an aditive is found and check if its counterpart is also found
    if so return them in a tuple
    """
    sums = {}
    check = {}

    for i in range(0, limit):
        new_sum = limit - i
        sums[new_sum] = i
    sums[0] = limit

    for i in range(0, length):
        item = weights[i]
        if item in check:
            if i > check[item][1]:
                return (i, check[item][1])
            else:
                return (check[item][1], i)
        if item in sums:
            check[sums[item]] = [item, i]

    return None


print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
