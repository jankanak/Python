class hashmap:
    def __init__(self):
        self.size=6
        self.map=[None]*self.size
    def _get_hash(self,key):
        hash=0
        for char in str(key):
            hash+=ord(char)
        return hash%self.size
    def add(self,key,value):
        key_hash=self._get_hash(key)
        key_value=[key,value]
         
        if self.map[key_hash] is None:
            self.map[key_hash]=list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    pair[1]=value
                    return True
            self.map[key_hash].append(key_value)
            return True
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

h=hashmap()
h.add('kanak','140120')
h.add('kank','14020')
h.add('kank','120')
h.print()
