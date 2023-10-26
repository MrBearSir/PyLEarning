largest = None
smallest = None
sum =  0
cnt = 0
avg = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        avg = sum / cnt
        break
    try:
        num = int(num)
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
        sum = sum + num
        cnt = cnt + 1
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
print("Avarage is", avg)
print("Count of inputs is", cnt)
