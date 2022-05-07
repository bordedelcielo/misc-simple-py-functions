# with enumerate()
def is_consecutive(input_list):
    print(f'Here is input_list: {input_list}.')
    for index,value in enumerate(input_list[:-1]):
        print(f'Here is value + 1: {value + 1}. Here is index + 1: {index + 1}.')
        if value + 1 != input_list[index+1]:
            return False
    return True

print(is_consecutive([7,8,9]))
print(is_consecutive([7,8,10]))

print([7,8,9])
print([7,8,9][:-1])

# slice syntax
# [starting_place : ending_place (python stops before getting to this value) : order (use -1 to reverse a list)]
print(4 + 1)

# Testing for sortedness (a consecutive list will be sorted)
# Testing by whether 
def is_consecutive(input_list):
    # Make sure this is sort
    duplicate_list = input_list
    input_list.sort()
    if input_list != duplicate_list:
        return False
    print(f'Here is input_list: {input_list}. Here is set(input_list): {set(input_list)}.')
    # if len(set(input_list)) != len(input_list):
    #     return False
    length = len(input_list)
    print(f'Here is length: {length}. Here is sorted_list[-1] - sorted_list[0]: {input_list[-1] - input_list[0]}')

    if input_list[-1] - input_list[0] == length - 1:
        return True
    else:
        return False

print(is_consecutive([7,8,9]))
print(is_consecutive([7,8,10]))
print(is_consecutive([7,11,9]))
print(is_consecutive([7,9,10]))