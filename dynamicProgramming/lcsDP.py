def lcs(a,b):
    m = len(a)
    n = len(b)

    lcsmat = [[0] * (n+1) for x in range(m+1)]
    

    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                lcsmat[i][j] = 1+lcsmat[i-1][j-1]
            else:
                lcsmat[i][j] = max(lcsmat[i-1][j], lcsmat[i][j-1])
    for row in lcsmat:
        print(' '.join(f'{val:3}' for val in row))

    lcsStr = []
    i,j = m,n
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            lcsStr.append(a[i-1])
            i-=1
            j-=1
        elif lcsmat[i-1][j] > lcsmat[i][j-1]:
            i-=1
        else:
            j-=1
    lcsStr.reverse()
    return lcsmat[m][n],''.join(lcsStr)
a = "longest"
b = "stone"

print("Length of LCS:", lcs(a,b))
