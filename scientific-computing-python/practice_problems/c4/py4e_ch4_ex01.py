hrs = input("Enter First Hours:")
rte = input("Enter First Rate:")
hrs2 = input("Enter Second Hours:")
rte2 = input ("Enter Second Rate:")

fhrs = float(hrs)
frte = float(rte)
fhrs2 = float(hrs2)
frte2 = float(rte2)

def computepay(h, r):
    if h >= 40:
        p = (h - 40)*(r*1.5) + 40 * r
    else:
        p = h * r
    return p

p = computepay(fhrs, frte)
ps = computepay(fhrs2, frte2)
print("Pay", p, "or", ps)
