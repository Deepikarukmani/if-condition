#LOOP statements:
#for loop

for i in range(0,10):
    print(i)

#if using odd & Even

a = int(input("enter your value"))
print(a)
print(type(a))
if a%2==0:
    print("even")
else:
    print("odd")

#for loop using if condition

values = [90,97, 87, 65, 25, 39,10,20,40]

for i in values:
    if i%2==0:
        print("even number : ", i)
    if not i%2==0:
        print("odd number : ", i)

#task from guvi using if condition:

marks = int(input("Enter your marks:  "))
if marks<35:
    print("sorry you have failed in the exam")
elif marks>=35 and marks<40:
    print("you have passed in the exam")
elif marks>=40 and marks<50:
    print("passed in Second Class")
elif marks>=50 and marks<90:
    print("passed in First Class")
elif marks>=90:
    print("passed in First Class with distinction")


