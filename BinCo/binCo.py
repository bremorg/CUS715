def binCo(n,k):
	if n==k or k<=0:
		return 1
	if k > (n/2):
		k = n-k
	B = ([1]*2)+([0]*(k-1))
	for i in range(0,n-1):
		j = k
		while j > 0:
			B[j] = B[j]+B[j-1]
			j = j - 1
	return B[k]