def obvious_search(L,k):
    for x in L:
        if x == k:
            return True
    return False


L = list(range(100))

a = obvious_search(L,708)
