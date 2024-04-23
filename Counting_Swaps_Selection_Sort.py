def count_swaps(lst):

    swaps = 0

    for i in range(len(lst)):
        min_index = 1

        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if lst[i] < lst[min_index]:
            lst[i],lst[min_index] = lst[min_index],lst[i]
            swaps += 1

    return swaps

data = list(map(int, input().split()))

result = count_swaps(data)

print(result)
