


def number_round_stylized(number):
    number = float(number)
    if 1 <= number < 1000:
        return number
    elif 1000 <= number < 1000000:
        number = number / 10
        number = round(number)
        number = str(number / 100)
        number = f'{number}k'
        return number
    elif number > 1000000:
        number = number / 10000
        number = round(number)
        number = str(number / 100)
        number = f'{number}M'
        return number
    else:
        number1 = str(number)
        number1 = number1.split('.')[1]
        print(number1)
        scaler = 0
        for digit in number1:
            if digit == '0':
                scaler += 1
            else:
                break
        print(scaler)
        scaler += 2
        if scaler > 0:
            print(number, 'p')
            number = number * (10**scaler)
            print(number, 'k')
            number = round(number)
            print(number, 'g')
            number = number / (10**scaler)
            print(number, 'e')
            return number
        else:
            number = float(number)
            number = number * 1000
            number = round(number)
            number = number / 1000
            return number

print(number_round_stylized(0.0001954811039481))

# number = 0.0001
# number = number * (10**3)
# print(number)