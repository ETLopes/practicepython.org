palin = input('Digite uma palavra que seja um palindromo: ').lower()
rev = palin[::-1]

if palin == rev:
	print('Essa palavra é um palíndromo')
else:
	print('Essa palavra não é um palíndromo')


def reverse(word):
	x = ''
	for i in range(len(word))
		x += word[len(word)-1-i]
		return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
print('This is NOT a Palindrome')