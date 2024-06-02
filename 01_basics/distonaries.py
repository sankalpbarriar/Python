d1={
    '1':'sankalp',
    '2':'prerena',
    '3':'komal'
}
print(d1)

chai_types={'Masala':'Spicy','Ginger':'zesty','Green':'Mild'}
print(chai_types)

#iteration
for i in chai_types:
    print(i,chai_types[i])
  
#length of the dictionary
print(len(chai_types))
  
#pop --> not like list 
chai_types.pop('Ginger')
print(chai_types)

#pop item--> removes last item from the dictionary
chai_types.popitem()
print(chai_types)

#adding new item to the dictionary
chai_types['Black']='strong'
print(chai_types)

#dictionary within dictionary
tea_shop={"Chai":{'Masala':'spicy','Ginger':'zesty'},
          "Tea":{'Green':'mild','Black':'mild'} 
        }
print(tea_shop)

#dictionary comprehension
squared_nums={x:x**2 for x in range(10)}
print(squared_nums)

#constructing new dictionary from keys and values
keys=['Masala', 'Ginger', 'Lemon']
default_values='Delicious'
new_dict=dict.fromkeys(keys,default_values)
print(new_dict) 