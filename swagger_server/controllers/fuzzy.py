def fuzzy_compare(string1, string2):
    n1, n2 = len(string1), len(string2)
    if string1 == string2: return 0
    if string1 == '': return n2
    if string2 == '': return n1

    lev_matrix = [[ 0 for i in range(n1+1) ] for j in range(n2+1) ]
    for i in range(n1+1): lev_matrix[0][i] = i
    for j in range(n2+1): lev_matrix[j][0] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            val = min(lev_matrix[j-1][i]+1, lev_matrix[j][i-1]+1, (lev_matrix[j-1][i-1]+1 if string1[i-1] != string2[j-1] else lev_matrix[j-1][i-1]))
            lev_matrix[j][i] = val

    return lev_matrix[n2][n1]
