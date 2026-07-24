#in this we are creating a dictionary and increasing the index value by 1
#the get method helps if the key doesnt exist

class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        a=[]
        for i in d:
            a.append([i,d[i]])

        
        return a

