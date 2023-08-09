# program using while loop in Strings:
name = " "
while not name == "deepika":
    name = input("what is your name ")

# to find length of alphabets
name = input("what is your name? ")
length = len (name)
i=0
while i<length:
    if name[i] in Deepika ["a","e", "i", "o", "u"]:
        print(name[i])
    i+=1


# to find length of numbers
email_id = input("what is your email id? ")
length = len(email_id)
i=0
count=0
while i<length:
    if email_id[i]>= "0" and email_id[i]<= "9":
        print(email_id[i])
        count+=1
    i+=1
print("count of numbers", count)


# to find length of alphabets
email_id = input("what is your email id? ")
length = len(email_id)
i=0
count=0
while i<length:
    if email_id[i]>= "a" and email_id[i]<= "z":
        print(email_id[i])
        count+=1
    i+=1
print("count of alpha", count)


#to find tables
no = 1
while no<=10:
    print(no, " * 4 = ", no*4)
    no+=1


#to find total
choice = " "
total = 0
while not choice== 'no':
    mark =int(input("enter your mark "))
    total= total+mark
    choice = input ("type no to stop ")
else:
    print("Total is", total)


##divisible by  divisor
no= 17
div=2
while div<no:
    if no%div==0:
        print(div)
    div+=1


#divisible by common divisor
no1, no2 = 10, 200
div=2
while div<=no1:
    if no1%div==0  and no2%div==0:
        print(div)
    div+=1


# to find GCD
no1, no2 = 100, 200
    div = 2
    while div <= no1:
        if no1 % div == 0 and no2 % div == 0:
            last = div
            print(div)
        div += 1
    else:
        print("last divisor", last)

#to find LCM
no1, no2 = 3, 7
big = no1 if no1>=no2 else no2
while True:
    if big%no1==0  and big%no2==0:
        print("LCM is ", big)
        break
    big+=1


# to find prime numbers:
no= int(input("enter your number "))
div=2
while div<no:
    if no%div==0:
        print("not prime")
        break
    div+=1
else:
    print("prime")


# to find fibonacci numbers:
    f = -1
    s = 1
    count = 1
    while count <= 8:
        t = f + s
        print(t)
        f = s
        s = t
        count = count + 1

# to find fibonacci numbers:
 f = -1
    s = 1
    count = 1
    while True:
        t = f + s
        print(t)
        if t == 34:
            break
        f = s
        s = t
        count = count + 1


# to find reverse of digits
bread = int(input("enter any number "))
count= 0
while bread>0:
    print(bread%10, end= " ")
    count=count+1
    bread = bread//10
else:
    print("count of digits", count)


# to find total and count of digit
    bread = int(input("enter any number "))
    count = 0
    total = 0
    while bread > 0:
        total = total + bread % 10
        count = count + 1
        bread = bread // 10
    else:
        print("count of digits", count)
        print("Addition of of digits", total)


# To Find Armstrong Value
bread = int(input("enter any number "))
no = bread
total= 0
while bread>0:
    dig = bread%10
    digpower = dig*dig*dig
    total = total + digpower
    bread = bread//10
else:
    if total == no:
        print("Armstrong")
    else:
        print("Not Armstrong")


# to find binary digits:
no = 4
binary " "
while no>0:
    rem = no%2
    binary = str(rem) + binary
    no= no//2
else:
    print(binary)

