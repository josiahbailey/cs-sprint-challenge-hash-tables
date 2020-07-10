

def finder(files, queries):
    """
    YOUR CODE HERE

    loop through paths and split each string
    add the last split word in each string and its index to object
    like so obj[last word] = i

    loop through queries and check for key in object
    if key is in object add object[key] to output 
    """
    words = {}
    output = []

    for i in range(0, len(files)):
        item = files[i]
        arr = item.split("/")
        length = len(arr) - 1
        if arr[length] in words:
            words[arr[length]].append(i)
        else:
            words[arr[length]] = [i]

    for item in queries:
        if item in words:
            for i in words[item]:
                output.append(files[i])

    return output


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bar/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
