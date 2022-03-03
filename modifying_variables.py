#Variables
money = 200
hat = 20
top = 30
pants = 15
belt = 60
shoes = 40

print (f"you have ${money}")
do_you_want_hat = input("do you what to buy a hat yes or no")
if do_you_want_hat == "yes":
	print ("you are buying a hat")
else:
	print ("yes you do")
	print ("purchasing hat...")
money = money-20 
print(f"you now have ${money}")

print("\n")
do_you_want_top = input("do you what to buy a top yes or no")
if do_you_want_top == "yes":
	print ("you are buying a top")
else:
	print ("yes you do")
	print ("purchasing top...")
money = money-30
print(f"you now have ${money}")

print("\n")
do_you_want_pants = input("do you what to buy a pants yes or no")
if do_you_want_pants == "yes":
	print ("you are buying a pants")
else:
	print ("yes you do")
	print ("purchasing pants...")
money = money-15
print(f"you now have ${money}")

print("\n")
do_you_want_belt = input("do you what to buy a belt yes or no")
if do_you_want_belt == "yes":
	print ("you are buying a belt")
else:
	print ("yes you do")
	print ("purchasing belt...")
money = money-60
print(f"you now have ${money}")

print("\n")
do_you_want_shoes = input("do you what to buy shoes yes or no")
if do_you_want_shoes == "yes":
	print ("you are buying a shoes")
else:
	print ("yes you do")
	print ("purchasing shoes...")
money = money-40
print(f"you now have ${money}")