import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    '''this function slices a list of lists from start to end'''
    print("My shape is :", np.shape(family))
    sliced = family[start:end]
    print("My new shape is :", np.shape(sliced))
    return sliced


# if __name__ == "__main__":
#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))

