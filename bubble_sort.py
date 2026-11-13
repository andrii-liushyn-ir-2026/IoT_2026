def find_unpaired_number(sequence):
    n = len(sequence)
    result = None
    
    for i in range(n):
        num = sequence[i]
        target = -num
        found_counterpart = False
        
        for j in range(n):
            if sequence[j] == target:
                found_counterpart = True
                break
        
        if not found_counterpart:
            result = num
            break

    return result


if __name__ == "__main__":
    test1 = [1, -1, 2, -2, 3]
    test2 = [-3, 1, 2, 3, -1, -4, -2]
    test3 = [1, -1, 2, -2, 3, 3]

    print("Результати виконання:")
    print(f"{test1} => {find_unpaired_number(test1)}")
    print(f"{test2} => {find_unpaired_number(test2)}")
    print(f"{test3} => {find_unpaired_number(test3)}")

# aawrihghbhaetjkgnjkerj
# something something
