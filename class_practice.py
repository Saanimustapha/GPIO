
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

number = int(input('Number: '))
numbers = [1,56,234,87,4,76,24,69,90,135]
num = is_even(number)

print(list(filter(is_even,numbers)))


def is_even(number):
    if number % 2 == 0:
        return not(True)
    else:
        return not(False)
    

number = int(input('Number: '))
numbers = [1,56,234,87,4,76,24,69,90,135]

print(list(filter(is_even,numbers)))







