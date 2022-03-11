def addition():
    list1 = [1,3,4]
    list2 = [2,4,5]
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            result.append(list1[i]+list2[j])
    print(result)

if __name__ == '__main__':
    addition()