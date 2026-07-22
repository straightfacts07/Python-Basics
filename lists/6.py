#write a progam to remove the dupliicates in a list\
nums=[1,2,1,2,3,4,5]


for i in nums:
    print(nums.count(i))
    if nums.count(i)>1:
        nums.remove(i)
print(nums)