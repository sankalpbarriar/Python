tea_variety=['black','Oolong','ginger','white']
# tea_variety[3]='lemon'
print(tea_variety)
# tea_variety[2:3]='lemon'   #it consdiers lemon as an array
# print(tea_variety) 

#to solve this pass it as an array
tea_variety[2:3]=['lemon'] 
print(tea_variety)

print(tea_variety[1:1])
tea_variety[1:1]=['test','test']
print(tea_variety)

tea_variety[1:3]=[]      #insert nothing
print(tea_variety)

for tea in tea_variety:
    print(tea) 


#list comprehension
l1=[1,2,3,4,5]
l2=[i**2 for i in range(10) ]
print(l2)
