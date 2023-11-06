def shell_sort(input_list):
    #step 1 Calculate the size n = len(input_list)
    n = len(input_list)
    #step 2 Calculate the gap k = n/2
    k = n//2

    #step 3 create a loop for sorting

    while k>0:
        print(k)
        for j in range(n):
            for i in range(int(k),n):
                temp = input_list[i]
                if input_list[i] < input_list[i-int(k)]:
                    input_list[i] = input_list[i-int(k)]
                    input_list[i-int(k)] = temp
        k = k//2
    print(input_list)

shell_sort([10,9,89,30,11,1,36,31,16,4])

