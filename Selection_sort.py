def selection_sort(input_list):
    for i in range(len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if input_list[j]<input_list[i]:
                temp = input_list[j]
                input_list[j]=input_list[i]
                input_list[i] = temp
    print(input_list)

selection_sort([12,10,3,19,80,3])
selection_sort([21,343,6,6,7,123,23,23,6,7,78899,234])
