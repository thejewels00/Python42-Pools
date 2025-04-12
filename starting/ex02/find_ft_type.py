def all_thing_is_obj(object: any) -> int:

    ty = type(object)
    if ty.__name__ == "str":
        print(f"{object} is in the kitchen : {ty}")
    elif ty.__name__ in ['int', 'NoneType', 'float', 'complex']:
        print("Type not found")
    else:
        print(f"{ty.__name__.capitalize()} : {ty}")
    return 42





