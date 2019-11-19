def minVertex(S, C):
	min = -1
	for i in range(0,len(S)):
		if S[i]==0 and (min == -1 or C[i]<C[min]):
			min = i    
	return min
    
def prim(G):
	#Graph G to be defined as an adjacency matrix
	C = list()
	S = list()
	P = list()
	for i in range(0, len(G)):
		C.append(-1)
		S.append(0)
		P.append(-1)
	S[0] = 1
	for v in range(0,len(G)):
		for w in range(0,len(G)):
			if G[v][w] > 0:
				if G[v][w] < C[w] or C[w]==-1:
					P[w] = v
					C[w] = G[v][w]

		v = minVertex(S,C)
		S[v]=1
	return (P,C,S) 

