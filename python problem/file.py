try:
    with open('F:\New folder\kanak.txt')as fobj:
        contents=fobj.read()
        print(contents)
except Exception as e:
    print("File error:",e)
