def getKeys(dct):
    return dct.keys()

def compare_dicts(dict1: dict, dict2: dict) -> dict:
    """
    :param dict1: Fist dictionary to compare
    :param dict2: Second dictionary to compare
    :return: A dictionary with the keys and the indices where the values are NOT equal
    """
    diff_dict = {}
    dict1_keys = getKeys(dict1)
    dict2_keys = getKeys(dict2)
    for key1 in dict1_keys:
        for key2 in dict2_keys:
            if key1 == key2:
                diff_dict[key1] = compare_lists(dict1[key1], dict2[key2])
                break
    return diff_dict


def compare_lists(list1: list, list2: list) -> list:
    """

    :param list1: List number one
    :param list2: List number two
    :return: Return the indices where the values are not equal NOTE: idx starts from 0
    """
    diff_idx = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                diff_idx.append(i)
        return diff_idx
    else:
        raise ImportError(" Lists do not have the same length")

if __name__ == '__main__':
    dict1 = {}
    dict2 = {}
    diff_dict = compare_dicts(dict1, dict2)
    print(diff_dict)