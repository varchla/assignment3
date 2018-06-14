#ques 1

a=input("enter no.")
l=[]
l.append(a)
print(l)

#ques 2

b=["google","apple","facebook","microsoft","tesla"]
b.append(l)
print(b)

#ques 3

a=[1,2,3,12,21,34,2]
print(a.count(2))

#ques 4

a=[8,67,89,1]
a.sort()
print(a)

#ques 5

a=[1,2,3]
b=[4,5,6]
print(a+b)

#ques 6

a=[1,2,3,4]
a.pop()
print(a)
a.append(6)
print(a)

#opt ques

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


