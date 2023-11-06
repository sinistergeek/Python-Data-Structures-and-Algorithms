def bubble_sort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)-i-1):
            if input_list[j]>input_list[j+1]:
                temp = input_list[j]
                input_list[j]=input_list[j+1]
                input_list[j+1] = temp
    print(input_list)
x =[7,1,3,5,2,5]
print("Executing Bubble sort for ",x)
bubble_sort(x)
y=[23,67,12,3,56,84,98,34]
print("Executing Bubble sort for ",y)
bubble_sort(y)
