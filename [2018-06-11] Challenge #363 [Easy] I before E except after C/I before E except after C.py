w = str(input("Check: ").lower())
v = 0

for i in range(len(w)):
    if w[i] == "e" and w[i+1] == "i":
        if w[i-1] != "c":
            v = 0
            break
        else:
            v = 1
            break

    elif w[i] == "i" and w[i+1] == "e":
        if w[i-1] != "c":
            v = 1
            break
        else:
            v = 0
            break
    else:
        v = 1

if v == 1:
    print("True")
else:
    print("False")
