def computepay(hours, rate) :
    # print("In computepay", hours,rate)
    if hours > 40:
        # print("Overtime")
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5) #Overtime at 1.5x rate
        # print(reg,otp)
        pay = reg + otp
    else: 
        # print("Regular")
        pay = hours * rate

    # print("Returning",pay)
    return pay

sh = input("Enter Hours: ")
try:
    fh = float(sh)
except:
    print("ERROR: please enter numeric input")
    quit()

sr = input("Enter Rate: ")
try:
    fr = float(sr)
except:
    print("ERROR: please enter numeric input")
    quit()

xp = computepay(fh,fr)

print("Pay: $",xp)