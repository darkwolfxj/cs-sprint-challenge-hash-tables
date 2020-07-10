def has_negatives(a):
    index = {}
    result = []
    for num in a:
        if abs(num) in index:
            index[abs(num)] += 1
            if index[abs(num)] > 1 and abs(num) not in result:
                result.append(abs(num))
        else:
            index[abs(num)] = 1 

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
