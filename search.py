def sequential_search(seq_list,target_num):
    search_flag = 0
    for i in range(len(seq_list)):
        if seq_list[i] == target_num:
            print("Found the target number",target_num,"at index",i,".")
            search_flag = 1;
        if search_flag == 0:
            print("Target Number Does Not Exist. Search Unsuccessful.")
seq_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
target_num = input("Please enter the target number : ")
sequential_search(seq_list,int(target_num))
