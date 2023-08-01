number = int(input("enter a five digit number "))
q = 1
s = str()
# s = ''
while q <= 10000:
    r = number//q
    multiple = r%10
    s += str(multiple)
    q *= 10
print(s)
number = int(input("enter a five digit number "))
sum = 0
q = 1
while q <= 10000:
    r = number//q
    multiple = r%10
    print(multiple)
    q *= 10
    sum += multiple
print(sum)