def myfun1():
    print("myfun1 is called.")

def myfun2():
    print("myfun2 is called, and it will now call myfun1.")
    myfun1()

print("Calling myfun2()...")
myfun2()
