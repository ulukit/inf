def decimal(n):
    counter = 1
    dec = 0
    for digit in str(n):
        dec += int(digit)*(2**(len(str(n))-counter))
        counter += 1
    return(dec)
def binary(decimal):
    i = -1
    bin = []
    greatest = 0
    while True:
        i += 1
        if 2**i <= decimal:
            greatest = i
            continue
        else:
            break
    while greatest >= 0:
        if (decimal-2**greatest) >= 0:
            decimal = decimal-2**greatest
            bin.append(1)
        else:
            bin.append(0)
        greatest -= 1
    for i in bin:
        print(i, end="")

num1 = int(input("prve cislo: "))
num2 = int(input("druhe cislo: "))
op = int(input("aka operacia\n1.+\n2.-\n3.*\n4./\n: "))
if op == 1:
    print(binary(decimal(num1)+decimal(num2)))
elif op == 2:
    print(binary(decimal(num1)-decimal(num2)))
elif op == 3:
    print(binary(decimal(num1)*decimal(num2)))
elif op == 4:
    print(binary(decimal(num1)/decimal(num2)))
else:
    print("a co si kokot")