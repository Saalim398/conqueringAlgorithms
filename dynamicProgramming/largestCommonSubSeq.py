#largest Common Sub Seq usinf recurrsion
def lcs(i, j):
    if i >= len(a) or j >= len(b):
        return 0
    elif a[i] == b[j]:
        return 1 + lcs(i+1, j+1)
    else:
        return max(lcs(i+1, j), lcs(i, j+1))

a = "hello"
b = "shell"

print("Length of LCS:", lcs(0, 0))
