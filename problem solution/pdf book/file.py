def print_two(arg1,arg2):
    print("The name are %s %s"%(arg1,arg2))
def print_one(arg1):
    print("The name is %s"%(arg1))
def print_none():
    print("How are you")
def print_three(*args):
    arg1,arg2,arg3=args
    print("the name are%s%s%s"%(arg1,arg2,arg3))
print_two("kanak","hassan")
print_one("kanak")
print_none()
print_three("kanak","hassan","cse")
    
    
