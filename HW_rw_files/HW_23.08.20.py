from os import path

filename = "menu.txt"
file_order = "order.txt"
if path.exists(filename) and path.exists(file_order):
    print( f"file found!")
    file = open(filename, "r")
    data = file.readline().split("|"or "\n")
    p_name = data[0]
    p_price = data[1]
    p_value = data[2]

    file = open(file_order, "r")
    data1 = file.readline().split("|"or "\n")
    or_name = data1[0]
    or_quantity = data1[1]

    print(20*"#","MENU",20*"#")
    print(data[0], "   pret:",data[1],data[2])
    #print(data1)
    total= int(data1[1])*int(data[1])
    print(f' comanda este facuta in suma de: {total}{data[2]}')
    print(f'#'*40)
else:
    print( f" Error!!!")
###########
# cu restul rindurilor numi iesa...

