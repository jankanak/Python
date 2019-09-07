def ka(iterable,func):
    it=iter( iterable)
    while(True):
        try:
            tb=next(it)
        except StopIteration:
            print("end of loops")
            break
        else:
            func(tb)
            
    


ka("kanak",print)

