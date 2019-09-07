def square(nums):
    for i in nums:
        yield(i*i)      
number=square([1,2,3,4,5])
for nums in number:
    print(nums) 
my_num=(x*x for x in [3,6,7,8])
print(list(my_num))
for nums in my_num:
    print(nums) 
