import re
from flask import Flask

class Orange:
	oranges = []
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created!")
		self.oranges.append(self)
	def __repr__(self):
		return self.color

	def rot(self, days, temp):
		self.mold = days * temp




o = Orange(4,"dark")
print(o)

def hangman(word):
	wrong = 0
	stages = 	["",
				"_________           ",
				"|       |           ",
				"|       0           ",
				"|      /|\\          ",
				"|      / \\          ",
				"|                   ",
				"|                   ",
				"|                   ",
				]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("Hangman")
	wrong = 0
	print(stages[0])
	print(stages[1])
	print(stages[2])

	while not win :
		guess = input("Guess Letter: ")
		if len(guess) > 1 :
			guess = guess[0]
		if guess in rletters:
			board = list(board)
			board[rletters.index(guess)] = guess
			board = "".join(board)
		else:
			wrong += 1
		for i in range(wrong+2):
			print(stages[i])
		print(board)
		if wrong > 3:
			break
		elif board == word:
			win = True
	if win :
		print( "you win")
	else :
		print( "you lose")

x = None 
if x is None:
	print("x is None")
else:
	print("x is not none ")

d = Orange(3, "green")
print( d.oranges)
x = "222, 333, blah, hi, cal, 333. 24534"
print(re.findall("\d*",x))

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello"
app.run(port=8000)
