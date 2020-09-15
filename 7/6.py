# Your function definition goes here
def valid_date(param):
    if len(param) != 8:
        return False    
    
    parameter = param.split(sep='.')
    if len(parameter) != 3:
        return False
    for i in range(len(parameter)):
        if parameter[i].isnumeric() == False:
            return False 
    if 1 <= int(parameter[0]) <= 31:
        if 1 <= int(parameter[1]) <= 12:
            if 0 <= int(parameter[2]) <= 99:
                return True
            

    


date_str = input("Enter a date: ")
if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  