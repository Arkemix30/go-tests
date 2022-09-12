def piramid_prim(n: int):
    # If n is lower or equal to 0, then we return 0
    if n <= 0:
        return 0
    # For loop iteration for printing purposes
    data = [ str(i) for i in range(n,0,-1)]
    # Join array for output printing as string
    print("".join(data))
    # Calling function for recursion
    return piramid_prim(n-1)
