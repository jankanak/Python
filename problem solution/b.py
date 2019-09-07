import re
def main():
    line="i am kanak hassan "
    matchresult=re.match("i am kanak hassan",line,re.M|re.I)
    if matchresult:
        print("match found :"+matchresult.group())
    else:
        print("no match is found")
    searchresult=re.search("kAnak",line,re.M|re.I)
    if searchresult:
        print ("search found:"+searchresult.group())
    else:
        print("no search found ")
if __name__ =='__main__':
    main()
