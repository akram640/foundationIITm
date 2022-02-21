def binary_search(L,k):
    '''This function is an alternative for the obivous search.
    It does exactly what is expected from the obivous search, but in an efficient way. This method is popularly colled the binary search.'''

    b = 0
    e = len(L)-1
    
    while(b < e):
        m = (e-b)//2 + b
        if L[m] == k:
            return m
        if L[m] < k :
            b = m + 1
        else:
            e = m - 1

    return -1
