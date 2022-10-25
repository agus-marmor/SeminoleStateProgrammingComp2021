def main():
    num = int(input("Enter an integer number > 0 "))
    temp = num
    list = []

    while True:
        if temp == 1:
            print("Glad Number")
            break
        elif temp in list:
            print("Not a Glad Number")
            break
        else:
            list.append(temp)
            temp = sum_digits(temp)


def sum_digits(num):
    if num == 1:
        return 1
    else:
        tempSTR = str(num)
        temp = 0
        for i in range(len(tempSTR)):
            temp += int(pow(int(tempSTR[i]), 2))
        return temp


main()
