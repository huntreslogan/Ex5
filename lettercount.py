
import string




def count_letters(filename):

	
	letters = []
	letter_count=[]
	count = 0
	text_file = open(filename)
	for line in text_file:
		line = line.rstrip()
		words = line.split()
		
		for letter in word:
			if letter in letters:
				position = letters.index(letter)
				letter_count[position] += 1
			elif letter in string.punctuation:
				continue
			else:
				letters.append(letter)
				letter_count[position] += 1
				

				

	for i in range(len(letters)):
		print "There are %d %s's in %s" % (letter_count[i], letters[i], filename)

def main():
	print count_letters("twain.txt")

if __name__ == "__main__":
	main()
