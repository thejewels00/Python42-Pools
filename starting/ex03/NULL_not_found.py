def NULL_not_found(object: any) -> int:

    ty =  type(object)
    if ty.__name__ == "NoneType" and object == None :
        print(f"Nothng : {object} {ty}")
    elif ty.__name__ == "float" and object != object :
        print(f"Cheese : {object} {ty}")
    elif ty.__name__ == "int" and object == 0 :
        print(f"Zero : {object} {ty}")
    elif ty.__name__ == "str" and object == '' :
        print(f"Empty : {object} {ty}")
    elif ty.__name__ == "bool" and object == False :
        print(f"Fake : {object} {ty}")
    else :
        print("Type not Found")
        return 1
    
    return 0