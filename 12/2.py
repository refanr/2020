def remove_evens(a_list):
    new_list = a_list[:]
    for l in new_list:
        i = int(l)
        if i%2==0:
            a_list.remove(l)
        
    return list    

def remove_evens2(list):
    new_list=[]
    for i in list:
        if int(i)%2!=0:
            new_list.append(i)
    return new_list

# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)