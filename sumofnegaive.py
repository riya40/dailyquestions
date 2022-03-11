def printing_number():
    input_array = [34, 54, 67, -78]
    resultant_array = []
    for i in range(len(input_array)):
        if input_array[i] > 0:
            if input_array[i] % 2 == 0:
                print("positive", input_array[i])
                resultant_array.append(input_array[i])
        else:
            print("negative")


if __name__== '__main__':
    printing_number()