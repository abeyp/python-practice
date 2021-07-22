#given a list of strings, return a list with all of the elements in reverse order, and reverse the spelling of each string element
#ex: ["fizz", "buzz"] -> ["zzub", "zzif"]



input_str = ['Revelling, maths, decolor, hangout, smectic, Nicola, terrorizer, ruthenic, precede, unequalness, Ketoxime, addictedness, eyeservant, disproof, roentgenologically, Unacoustical, hypnotizing, bay, unecstatic, preoceanic, Mightiest, intersesamoid, dross, bigotry, especialness']
#code to split string into seperate words
input_str = input_str[0].replace(", ", " ").split()


def reverse_func(words):
		words.reverse()
		rev_str = []
		for word in words:
			w = len(word)
			slicedstr = word[w::-1]
			rev_str.append(slicedstr)
		print(rev_str)

reverse_func(input_str)


