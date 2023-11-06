def binary_search(sorted_list,target_num,start_point=0,end_point=None):
    search_flag = False
    if end_point ==None:
        end_point = len(sorted_list)-1
    if start_point < end_point:
        mid_point = (end_point+start_point)//2
        if sorted_list[mid_point] == target_num:
            search_flag = True
            print(target_num,"Exists in the list at",sorted_list.index(target_num))
        elif sorted_list[mid_point] > target_num:
            end_point = mid_point-1
            binary_search(sorted_list, target_num,start_point,end_point)
        elif sorted_list[mid_point] < target_num:
            start_point = mid_point+1
            binary_search(sorted_list,target_num,start_point,end_point)
        elif not search_flag:
            print(target_num,"Value does not exist")

sorted_list =[1,2,3,4,5,6,7,8,9,10,11,12,13]
binary_search(sorted_list,14)
binary_search(sorted_list,0)
binary_search(sorted_list,5)
