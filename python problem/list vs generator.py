import mem_profile
import random
import time
names=['kanak','hasan','pabna']
majors=['c','c++','java']
print('memory(before):{}mb'.format(mem_profile.memory_usage_resource()))
def people_list(num_people):
    result=[]
    for i in xrange(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
            }
        result.append(person)
        return result
def people_generator(num_people):
    for i in xrange(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
            }
        yield person

t1=time.clock()
people=people_list(1000000)
t2=time.clock()

print('memory(after):{}mb'.format(mem_profile.memory_usage_resource()))
print('Took{}seconds'.format(t2-t1))
    
     
