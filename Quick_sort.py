def find_pivot(input_list,first,last):
    pivot = input_list[last]
    left_pointer = first 
    right_pointer = last -1
    pivot_flag = True
    while pivot_flag:
        if input_list[left_pointer]>pivot:
            if input_list[right_pointer]<pivot:
                temp=input_list[right_pointer]
                input_list[right_pointer]=input_list[left_pointer]
                input_list[left_pointer]=temp
                right_pointer = right_pointer-1
                left_pointer = left_pointer+1
            else:
                right_pointer = right_pointer -1
        else:
            if input_list[right_pointer]<pivot:
                left_pointer = left_pointer + 1
            else:
                left_pointer = left_pointer +1
                right_pointer = right_pointer -1
        if left_pointer >= right_pointer:
            temp = input_list[last]
            input_list[last] = input_list[left_pointer]
            input_list[left_pointer] = temp
            pivot_flag = False
    return left_pointer
def quickSort(input_list):
    first = 0
    last = len(input_list)-1
    qsHelper(input_list,first,last)
def qsHelper(input_list,first,last):
    if first<last:
        partition = find_pivot(input_list,first,last)
        qsHelper(input_list,first,partition-1)
        qsHelper(input_list,partition+1,last)
input_list =[15,37,8,20,50,7,28,2,13]
quickSort(input_list)
print(input_list)
