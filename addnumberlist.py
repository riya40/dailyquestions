
def addnumbers():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    result = []
    for i in range(0, len(array), 2):
        result.append(array[i]+array[i+1])
    print(result)


if __name__ == '__main__':
    addnumbers()