def diszito(n, sz):
    print()
    for i in range(n):
        print(sz, sep="", end="")
    print("\n")



for f in range(1, 5):
    diszito(80, "*")
    print(f, ". feladat", sep="")
    diszito(75, "-")
