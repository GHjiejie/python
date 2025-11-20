# 数组操作方法

my_list = [1, 2, 3, 4, 5]

# 查找元素索引


def find_index(element, data_list=my_list) -> bool:
    try:
        index = data_list.index(element)
        # 如果找到了返回index
        if (index >= 0):
            print(f"Found element {element} at index {index}")
        return True
    except ValueError:
        # 如果没有找到返回-1
        print(f"Element {element} not found in the list.")
        return False


# find_index(4, my_list)
# 删除元素


def delete_element(element: int, data_list: list) -> list:
    """
    @param element: 要删除的元素
    @param data_list: 要删除元素的数组
    @return: 返回删除元素后的数组

    """
    try:
        if find_index(element, data_list):
            print(f"在数组中找到元素 {element}，执行删除操作。")
            data_list.remove(element)
            return data_list
        else:
            print(f"在数组中未找到元素 {element}，不执行删除操作。")
            return data_list

    except ValueError:
        print(
            f"Element {element} not found in the list. No deletion performed.")
        return data_list


# delete_element(0, my_list)

# 添加元素


def add_element(element: int, data_list: list) -> list:
    """
    @param element: 要添加的元素
    @param data_list: 要添加元素的数组
    @return: 返回添加元素后的数组

    """
    data_list.append(element)
    return data_list


# 设置变量接受添加元素后的数组
new_list = add_element(6, my_list)
print("List after adding element:", new_list)


# print("Find index of 4:", find_index(9,my_list))

# # 元组
# my_tuple = (1, 2, 3, 4, 5)

# print("Tuple:", my_tuple)
# # 字典
# my_dict = {'a': 1, 'b': 2, 'c': {
#                 'd': 3,
#                 'e': 4
#            }
#            }
# print("Dictionary:", my_dict)
