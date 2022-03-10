'''
#1-11
input("push any key and then press enter")
input("please enter your name and then press enter")
input("please enter your age and then press enter")
name = input("please enter your name and then press enter")
age = input("please enter your age and then press enter")
fav_movie = input("please enter your favorite movie and then press enter")
book = input("please enter a book and then press enter")
adjective = input("please enter an adjective and then press enter")
noun = input("please enter a noun and then press enter")
verb = input("please enter a verb and then press enter")
print(f"hi {name} your age is {age} your favorite movie is {fav_movie} a book you like is {book} an adjective is {adjective} and noun is {noun} and a verb is {verb} ")
'''
'''
#12-17
age_1 = int(input ("what is your age"))
print (f"your age in ten years will be{age_1 + 10}")
print(f"you were born in {2022 - age_1}")
apples = int(input ("how many apples do you have?"))
friends = int(input("how many friends do you have?"))
sharedapples = int(apples//friends)
leftovers = (apples%friends) 
print(f"your friends will have {sharedapples} each ")
print(f"You'll have {leftovers} apples left.")
'''
#18-34
'''
pizzas = int(input("how many pizzas do you want?"))
people_feeding = int(input("how many people are you feeding"))
slices_each = (pizzas*8) 

print (f"everyopne will have {slices_each//people_feeding} slices each with {slices_each%people_feeding} left over")


money = int(input("how much money do you have?"))
tv_cost = int(input("how much does the tv cost?"))
print(f"you will have {money-tv_cost} money ,left over if you buy the tv")
print(f"if you wait for a 20 percent discount the tv will cost {0.8 * tv_cost}")
'''
'''
bitcoins = float(input("how many bitcoins do you have?"))
bitcoin_value = 57167.84 
print(f"your bitcoins are worth ${bitcoins * bitcoin_value}")

week_money = int(input("how much money do you earn per week, after tax"))
tax = float(input("what is the tax rate as a decimal, eg:0.15"))
print(f" you will take home ${week_money * (1 - tax) } ")
'''
book_name = input("type the name of a book here -->")
print(book_name.upper())
print(book_name.lower())
print(book_name.title())

num = int(input("please enter a number"))
print( book_name * num)


