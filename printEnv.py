for i in range(0,8):
    print("")
    for j in range(0,8):
        if (i == 0 and j == 0) or (i == 7 and j == 7):
            print("\\", end = " ")

        elif (i == 0 and j == 7) or (i == 7 and j == 0):
            print("/", end = " ")

        elif (i == 0 or i == 7):
            print("".join(str(j)), end = " ")

        elif (j == 0 or j == 7):
            print("".join(str(i)), end = " ")

        else:
            print("-", end = " ")
