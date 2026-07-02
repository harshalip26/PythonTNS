i = 5
print(i)
str1 = "My name is John Doe"
print(str1)
flt = 12.678
print(flt)
bln = True
print(bln)

print(type(i))
print(type(str))
print(type(flt))
print(type(bln))

i = 5
print(i)
i = "Changed to a String"
print(i)

# Arithmatic operation 
print("\n Arithmatic operators")
a = 21
b = 10
c = 0

c = a + b
print ("a: {} b: {} a+b: {}".format(a,b,c))

c = a - b
print ("a: {} b: {} a-b: {}".format(a,b,c) )

c = a * b
print ("a: {} b: {} a*b: {}".format(a,b,c))

c = a / b
print ("a: {} b: {} a/b: {}".format(a,b,c))

c = a % b
print ("a: {} b: {} a%b: {}".format(a,b,c))

a = 2
b = 3
c = a**b 
print ("a: {} b: {} a**b: {}".format(a,b,c))

a = 10
b = 5
c = a//b 
print ("a: {} b: {} a//b: {}".format(a,b,c))


# comparison aoperators
print("\n Comparison operators")
a = 21
b = 10
if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")


#assignment operator
print("\nAssignment Operators")
a = 21
b = 10
c = 0
print ("a: {} b: {} c : {}".format(a,b,c))
c = a + b
print ("a: {}  c = a + b: {}".format(a,c))

c += a
print ("a: {} c += a: {}".format(a,c))

c *= a
print ("a: {} c *= a: {}".format(a,c))

c /= a 
print ("a: {} c /= a : {}".format(a,c))

c  = 2
print ("a: {} b: {} c : {}".format(a,b,c))
c %= a
print ("a: {} c %= a: {}".format(a,c))

c **= a
print ("a: {} c **= a: {}".format(a,c))

c //= a
print ("a: {} c //= a: {}".format(a,c))

print("\n string concat")
i = 5
j = 6
print(i+j)
# 
str1 = "John "
str2 = "Doe"
print(str1 + str2)

print("\n Conditions in python")
# Checking Conditions
x = 7
y = 9
if x == y:
    print("Equal")
else: 
    print("Inequal")

print("\n Multiple conditions")    
x = 7
y = 9
if x == 7 and y < 10:
    print("Condition Met Multiline Block")
    print("Condition Met")
else:
    print("Condition not Met  Multiline Block")
    print("Condition not Met")

x = 7
y = 9
if x == y:
    print("Equal")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")    

print("\n checking boolean")    
x = True
if x == False:
    print(x)
else:
    print(False)

# Nested ‘if’
x = 7
y = 9
if x < y:
    if x > 5:
        print("Nested Condition Met")
    else:
        print("Inner nested False Block")
else:
    print("Outer nested False Block")    

l = 5
m = 0 
i = 0
while l > 0:
    m += l  # m = m + l
    l-=1    # l = l - 1
    i+=1    # i = i + 1
    print("Iteration ", i)
print("Final value of m = ", m)    

print("\n for loop")
WeekdaysList = ["Sunday", "Monday", "Tuesday"]
for x in WeekdaysList:
    print(x)

# Example of 'for' loop for a Tuple
CountryTuple = ("India", "US", "UK", "Germany")
for x in CountryTuple:
    print( x)    

# Example of 'for' loop for a Set
PlayerSet = {"Ronaldo", "Messi", "Neymar"}
for x in PlayerSet:
    print(x)