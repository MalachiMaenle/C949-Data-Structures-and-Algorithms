def linear_search(_numbers, _key):
    for i in range(len(_numbers)):
        if _numbers[i] == _key:
            return i
    return -1