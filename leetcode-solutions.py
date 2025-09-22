#3110
word = "hello"
score = 0
for i in range(len(word) - 1):
	score += abs(ord(word[i]) - ord(word[i + 1]))
print(score)



