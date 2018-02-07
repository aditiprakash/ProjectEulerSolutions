

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
products = []
for i in range(999,0,-1):
	for j in range(999,0,-1):
		product = i * j
		rev = str(product)
		rev = int(rev[::-1])
		if product ==  rev:
			# print(i,"*",j,"=",product)
			products.append(product)
			break
	
print(max(products))