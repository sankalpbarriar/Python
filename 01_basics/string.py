# chai="Lemon Tea"
# print(chai)
# print(chai[0:5])
# print(chai[0:8:2])
# print(chai[:-1])  # Lemon Te



# chai=" Masala tea "
# print(chai)
# print(chai.upper()) 
# print(chai.lower())
# print(chai.strip())

# chai="Lemon, Ginger, Masala, Mint"
# print(chai.split(", "))

# chai="Lemon Tea"
# print(chai.find('Tea'))

chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))
 

#list into string using join operation
l1=["masala","lemon","ginger"]
print(",".join(l1))


chai="MBA chai walla"
for letter in chai:
    print(letter)


chai=r"c:\user\pwd "   # Raw string
print(chai)
