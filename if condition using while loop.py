#same program using if condition: (Same output, no change in output, coding lines different, large number of codes)

if count <= 5:
    print(2,end=" ")
count=count+1
if count <= 5:
    print(3,end=" ")
count=count+1
if count <= 5:
    print(4,end=" ")
count=count+1
if count <= 5:
    print(5,end=" ")
count=count+1

#same program using while loop (Same output, no change in output, coding lines different, small number of codes)
#positive index number

count = 5
while count <= 500:
    print(count, end = " ")
    count=count+1


# reverse print
count = 5
while count >=1:
    print(count, end = " ")
    count=count-1


#using if condition (%)
count = 50
while count >=1:
    if count%5==0:
        print()
    print(count, end = " ")
    count=count-1


#find even numbers using while:
count = 1
while count<=10:
    if count%2==0:
        print(count)
    count=count+1


#find odd numbers using while: (using not count method)
count = 0
while count<=20:
    if not count%2==0:
        print(count)
    count=count+1

#find odd numbers using while: (using not equal method)
count = 0
while count<=20:
    if count%2 != 0:
        print(count)
    count=count+1

#find odd numbers using while: (using %3 method)
count = 0
while count<=20:
    if count%3 == 0:
        print(count)
    count=count+1

#find odd numbers using while: (using %3 and %4 method)
count = 0
while count<=30:
    if count%3 == 0 and count%4 == 0:
        print(count)
    count=count+1

#find total numbers using while:
total = 0
no = 1
while no<=5:
    total = total + no
    no=no+1
print(total)

#find multiply numbers using while:
total = 1
no = 1
while no<=5:
    total = total * no
    no=no+1
print(total)

#using break statement:
no = 1
while no<=5:
    print(no)
    if no==5:
        break
    no=no+1


#using continue statement
no = 1
while no<=10:
    if no == 5:
        no = no + 1
        continue

    print(no)
    no = no + 1

