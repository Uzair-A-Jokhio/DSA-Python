def linear_search(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return True
    return False

def binary_search(list_value:list, value:int):
    first = 0
    last = len(list_value) - 1
    while first <= last:
        middle = (first + last)//2
        if list_value[middle] == value:
            return True
        elif list_value[middle] < value:
            first = middle +1
        else:
            last = middle - 1



if __name__ == "__main__":
    list_number = [22,3,5,7,3,8,1,89]
    sort_number = list_number.sort
    print(sort_number)
    print(f"the value is: {binary_search(sort_number, 1)}")
