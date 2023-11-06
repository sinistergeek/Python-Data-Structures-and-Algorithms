def hash(list_items,size):
    temp_list = []
    for i in range(size):
        temp_list.append(i)
    print(temp_list)
    hash_table = dict.fromkeys(temp_list)
    print(hash_table)
    for item in list_items:
        i = item%size
        hash_table[i] = item
    print("value of hash table is :",hash_table)

list_items = [18,12,45,34,89,4]
hash(list_items,8)
