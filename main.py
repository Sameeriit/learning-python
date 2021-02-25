'''
'''#Full_name = 'Sameer Ahmad'
#age = 20
#is_new = True
#Name = input('What is your name? ')
#favorite_color = input('your favorite colour? ')
#print(Name +' likes '+ favorite_color)
'''type_converter
birth_year = input('birth year? ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)'''
#weight converter pond to kg
'''Weight_lbs = input('Weight (lbs): ')
Weight_kg = float(Weight_lbs) * 0.45
print(Weight_kg )'''
#pond to kg
#Weight_kg = input('weight (kg): ')
#Weight_lbs = int(Weight_kg)/0.45
#print(Weight_lbs)
#string
'''course = 'pythont'
another = course[1:-1]
print(another)'''
#formated string
first = 'john'
last = 'smith'
#message = first + '[' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
'''mail = '''
'''hi sameer 
i have seen you are very interested in our course
you are most valuable for us 
we welcome you in our course
thank you
team SAM !'''
#print(mail)''''''
#string methods
#counting the characters
#course = input('write string: ')
course = 'i gonna fuck you '

'''print(course.upper())
print(course.lower())
print(course)
print(len(course))
print(course.replace('life', 'energy'))'''
print('fuck' in course)
#arithmatic expresion
'''print(10+3)
print(10-2)
print(10/3)
print(10//3)
print(10%3)
print(10*3)
print(10**3)'''
#augumented expresion
x=10
#x+=3
x-=3
print(x)
# oparetor prcedence order
x=10+3*2**2
print(x )
# parenthesis
#exponentiation 2**3
#multiplication or division
#addition or multiplication
'''x=(2 + 3) * 10 -3
print(x)
#working with number
x= 2.9
print(round(x))
print(abs(x))
import math
print(math.ceil(x))'''
#condition
#if statement
'''is_hot = False
is_cold = True
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print(" it's  a cold day")
    print("wear warm cloths")
else:
    print("it's a lovely day")
print("enjoy  your day")'''
#Exercise
'''price of a house is $1M
if buyer has good credit,
   they need to put down 10%
otherwise
    they need to put down 20%
print the down payment'''
'''price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")'''
#logical operator
#AND and OR
'''has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
'''
#comperision operator
'''temprature = 30
if temprature < 30 :
    print("it's a hot day")
else:
    print("it's not a hot day")
'''
#exersize
'''Name = input("Enter Your wife  Name: ")
if len(Name) < 3:
    print("Name Must be at least 3 characters. ")
elif len(Name) >50:
    print("Name Must be maximum 50 characters.")
else:
    print("Name looks good")
'''