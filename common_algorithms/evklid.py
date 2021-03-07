def get_GCS(a, b):
	"""Calculate the Greatest Common Divisior (GCS),
		for numbers a & b, with Euclidean algorithm,
		return GCS

	"""
	if a<b:
		a, b = b, a
	while b>0:
		a, b = b, a%b
	return a


def test_GCS(): 
	#-- test №1 -----------------------------
	a = 28
	b = 35
	res = get_GCS(a, b)
	if res == 7:
		print("#test_1 == OK")
	else: 
		print("#test_1 == False")

test_GCS()

