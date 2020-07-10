# Your code here



def finder(files, queries):
    index = {}
    result = []
    
    for route in files:
        file = route.split("/").pop()
        if file in index:
            index[file].append(route)
        else:
            index[file] = [route]
    for query in queries:
        if query in index:
            for route in index[query]:
                result.append(route)
    return sorted(result, key=lambda x: len(x))


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
