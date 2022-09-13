def piramid_prim(n: int, pointer:int = 0, output: str = ""):
    # If N is lower or equal to 0, then we return 0
    if n <= 0:
        return 0
    # If output string is empty, we set current N value to pointer
    if output == "":
        pointer=n
    # If pointer is equal to 0, then we print the curren output
    # and we decrease N value for next N iteration
    if pointer <= 0:
        print(output)
        return piramid_prim(n-1, n-1, output="")
    # Saving pointer value to outpout string and decreasing pointer value for iteration
    output += str(pointer)
    return piramid_prim(n, pointer-1, output)