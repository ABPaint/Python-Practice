length = int(input("How long is your sequence? "))
n1, n2 = 0,1
count = 0

if length == 1:
    print("Fibonacci sequence upto",length,":")
    print(n1)
else:
    print("Fibonacci sequnce:")
    while count < length:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1