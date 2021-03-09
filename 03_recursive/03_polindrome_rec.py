def polindrome(word):
	if len(word) <= 1:
		return True # polindrome
	if word[0] != word[-1]:
		return False
	return polindrome(word[1:-1])

# nikita = False
# alalala = True
# ala = True 