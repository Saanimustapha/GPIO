def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

number = int(input('Number: '))
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_even,numbers)))


result = (lambda x : x % 2 == 0)
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(result,numbers)))



def is_even(number):
    if number % 2 == 0:
        return not(True)
    else:
        return not(False)
    

number = int(input('Number: '))
numbers = [1,56,234,87,4,76,24,69,90,135]

print(list(filter(is_even,numbers)))



def join_strings(words):
    sentence = ''
    for word in words:
        sentence += word
        sentence += ' '
    return sentence

Words = ['My','name','is','kelvin']
result = join_strings(Words)
print(result)



#Create a list out of only the positive numbers from this list:
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positiveNumbers = []
for number in numbers:
    if number > 0:
        positiveNumbers += [number,]
        
print(positiveNumbers)

#Create a list containing only the even numbers from this list
numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
evenNumbers = []
for number in numbers:
    if number % 2 == 0:
        evenNumbers += [number,]
        
print(evenNumbers)

#Create a list containing tuples of the uppercase version and the length of the following words
words = ["hello", "my", "name", "is", "Sam"]
listOfInfo = []
for word in words:
    upperCase=word.upper()
    length = len(word)
    Tuple = (upperCase,length)
    listOfInfo += [(upperCase,length),]
    
print(listOfInfo)

#A class is a single unit consisting of attributes and methods from which objects can
#be instantiated from.

class Person(object):
    def __init__(self,name,dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth
    def speak(self):
        print('Hello')
    def walk(self):
        print('Walking away')
    def get_name(self):
        return name
    def get_age(self):
        return dateOfBirth
    

class Student(Person):
    def __init__(self,name,dateOfBirth,courseNames):
        super().__init__(name,dateOfBirth)
        self.courseNames = courseNames
    def get_courses():
        return courseNames
    def speak():
        print("I'm so tired!")
        

