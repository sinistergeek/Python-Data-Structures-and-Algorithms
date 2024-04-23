# THis how recurisve on merge_sort works
# def merge_sort(lst):
#
#     if len(lst) <= 1:
#         return lst
#
#     print(f'lst: {lst}')
#
#     mid = len(lst) // 2 
#     
#     print(f'mid: {lst[mid]}')
#
#     left = merge_sort(lst[: mid])
#     print(f'Left partition: {left}')
#
#     right = merge_sort(lst[mid: ])
#     print(f'Right partition: {right}')
#
#     return '---'
#
# data = [6,8,1,4,5,3,7,2]
# merge_sort(data)

def merge(left,right):
    output = [ ]
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

print(merge([5],[8]))
print(merge([8],[5]))
print(merge([3,4],[7,10]))
print(merge([3,4],[7,10,11]))
