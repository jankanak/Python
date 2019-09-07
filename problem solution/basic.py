.print("kanak hassan:",24)
print("is it greater?",5<2)
ball=80
print("there are ",ball,"availabale")
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars -drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
print ("We can transport", carpool_capacity, "people today.")
print("Hey %s there." %"7.0")
myname='kanak hassan'
my_age=23
my_height=180
print("my name is %s"%myname)
print("%d  my current age"%my_age)
print("my height is %d taller"%my_height)
a=10
b=20
c=a+b
d=b-a
print ("He's got %d eyes and %d hair=%d" % (a,b,c))
print("subtracting %d and %d the result is =%d" %(a,b,b-d))
x="there are %d types of people" %10
print(x)
print("i said :%r"%x)
hilarious=False
joke="is is so funny %r"
print(joke%hilarious)
e="kanak"
s="hassan"
print(e)
print(s)
formatter="%r%r%r%r"
print(formatter%(14,12,3,4))
print(formatter%("one","two","three","four"))
print(formatter%(True,False,True,False))
print(formatter%(formatter,formatter,formatter,formatter))
print (formatter % ( "I had this thing.",
 "That you could type up right.",
 "But it didn't sing.",
 "So I said goodnight."))
day="sat sun mon tue wed thr fri"
month="jan \n feb\n mar\n apr\n may \n"
print("the day by day of a week are:",day)
print("the months are :",month)
print("""         i am kanak hassan. 
      i am a student of pabna university of science
      and technology""")
tabby_cat="\t \t i am tabbed i."
persian_cat="i am splilt \n on a line"
backslash_cat="i am \\a \\cat"
print (tabby_cat)
print(persian_cat)
print(backslash_cat)
fat_cat="""I shall do a list:
     \t*burger
     \f*chicken fry
     \b*fried rice
     """
print(fat_cat)

from sys import argv
third=argv
first=argv
print("your third variable is :",third)
print("your third variable is :",first)

from sys import argv
script=argv
user_name=argv
promt='>'
print("Hi %s I am the %s script"%(user_name,script))
print("I would like to ask you some question")
print("do you like me %s"%user_name)
likes=input(promt)
print("where do you live%s?"%user_name)
lives=input(promt)
print(""" al right so you said %r about liking me .
you live in %r .not sure where that  is """%(likes,lives))
