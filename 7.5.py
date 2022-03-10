#question 1
print("welcome to mr whippy's online ordering")
ice_creams = int(input("how many ice creams do you want?"))
if ice_creams >= 20 :
	print("there is not enough ice creams")
else:
	print("your order has been taken")

#question 2
how_far = int(input("please enter how far you will be travelling in km"))
if how_far >= 200:
	print("remember to fill up on fuel before you go")
else:
	print("have a good trip")

#question 3
age = int(input("how old are you"))
if age >= 18:
	print("you are an adult")
else :
	print("you are young")

#question 4
fav_movie = input("what is your favorite movie")
if fav_movie == "lord of the rings":
	print("you have excellent taste")
else:
	print("lord of the rings is clearly the better film")

#question 5
darth_p = input ("have you heard the tale of darth plagueis the wise?")
if darth_p == "no":
	print("Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life")
else:
	print("you must be a fan")

#question 6
passion_of_christ = input("who directed the movie pasion of christ")
if passion_of_christ.lower() == "mel gibson":
	print("correct!")
else:
	print("Mel Gibson directed it")

#question 7
score = 0
question1 = input("What is the capital of New Zealand?")
if question1.lower() == "wellington":
	score = score + 1
else :
	score = score

question2 = input("What kind of food is Penne?")
if question2.lower() == "pasta":
	score = score + 1
else:
	score = score

question3= input("What sport did David Beckham play?")
if question3.lower() == "football":
	score = score + 1
else :
	score = score

question4 = input("From what grain is the Japanese spirit Sake made?")
if question4.lower() == "rice":
	score = score + 1
else :
	score = score

question5 = input("What’s longer, a nautical mile or a mile?")
if question5.lower() == "nautical":
	score = score + 1
else :
	score = score

print(f"your score is {score}/5")


