def computepay(h, r):
    if h <= 40:
        p = h * r 
    else:
        p = ((h - 40) * 1.5 * r) + 40 * r
    return p

h = input("Enter Hours:")
r = input("Enter Rate:")
try:
    h = float(h)
    r = float(r)
except:
    print("Please enter valid values for yor Hours worked and pay rate.")
    quit()
p = computepay(h, r)
print("Pay", p)