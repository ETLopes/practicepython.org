a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
pergunta = int(input('Me diga um número: ')) 

for i in a:
	if i < pergunta:
		b.append(i)
	else:
		pass

print(b)