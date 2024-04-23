
def perform_partial_sort(lst,n):
    for i in range(1,n):
        key = lst[i]
        j = i -1
        while j>=0 and key < lst[j]:
            lst[j+1] =lst[j]
            j = j - 1

        lst[j + 1] = key
    return lst[:n]

data = list(map(int,input().split()))
n = int(input())
sorted_partial_list = perform_partial_sort(data,n)
print(sorted_partial_list)
