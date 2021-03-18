def task(array):
    '''Сложность O(2n)'''
    if isinstance(array, list):
        data = ''.join(str(i) for i in array)
    else:
        data = array

    index = data.find('0')
    if index == -1:
        raise ValueError('Error! There is no 0 in the array')
    else:
        return index



if __name__ == '__main__':
    print(task("111111111111111111111111100000000"))
    print(task([1, 1, 1, 1, 0]))
    print(task([1, 1, 1, 1]))
