import sys

def main():
	while True:
		a = rnd(4)
		greeting = ['hello', 'hi', 'hullo', 'hey']
		inp = input("You:")
		print("Bot:", end="")
		if inp.lower() in greeting:
			print(greeting[a])
		if inp.lower() == "sup":
			print("Cool.")
		if inp.lower() == "bye" or inp.lower() == "goodbye" or inp.lower() == "byebye":
			print("Bye")
			sys.exit()

if __name__ == "__main__":
    main()