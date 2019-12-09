def min3(a,b,c):
	temp = min(a,b)
	return min(temp,c)

def MinDistanceMatrix(str1, str2):
	T = list()
	for x in range(0,len(str2)+1):
		T.append(range(x,len(str1)+1+x))

	for i in range(1,(len(str2)+1)):
		for j in range(1,len(str1)+1):
			if str2[i-1] == str1[j-1]:
				T[i][j] = T[i-1][j-1]
			else:
				T[i][j] = 1 + min3(T[i-1][j-1], T[i][j-1], T[i-1][j])
	return T

def MinDistance(str1,str2):
	return MinDistanceMatrix(str1, str2)[len(str2)][len(str1)]