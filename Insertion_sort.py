def insertion_sort(input_list):
    for i in range(len(input_list)-1):
        indexi = i
        indexj = i+1
        print("indexi=",indexi)
        print("indexj=",indexj)
        while indexi >=0:
            if input_list[indexi]>input_list[indexj]:
                print("swapping")
                temp = input_list[indexi]
                input_list[indexi] = input_list[indexj]
                input_list[indexj] = temp
                indexi = indexi - 1
                indexj = indexj - 1
            else:
                indexi = indexi - 1
        print("List update:",input_list)
    print("Final list =",input_list)

insertion_sort([9,5,4,6,8,9,3])
