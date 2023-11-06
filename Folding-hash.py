def hash(list_items,size):
    temp_list = []
    for i in range(size):

        temp_list.append(i)
    hash_table = dict.fromkeys(temp_list)
    for item in list_items:
        i = item%size
        hash_table[i]=item
    return hash_table
def convert_to_string(input_list):
    phone_list=[]
    for i in input_list:
        temp_string = str(i)
        temp_list = list(temp_string)
        phone_list.append(temp_list)
    return phone_list
def folding_hash(input_list):
    hash_final = []
    while len(input_list)>0:
        hash_val = 0
        for element in input_list:
            while len(element)>1:
                string1 = element[0]
                string2 = element[1]
                str_combine = string1 + string2
                int_combine = int(str_combine)
                hash_val += int_combine
                element.pop(0)
                element.pop(0)
            if len(element) > 0:
                hash_val += int(element[0])
            else:
                pass
            hash_final.append(hash_val)
        return hash_final

phone_list = [1231255,33455235,123123123,63403496]
str_phone_values = convert_to_string(phone_list)
folded_value = folding_hash(str_phone_values)
folding_hash_table = hash(folded_value,11)
print(folding_hash_table)
