## Calculate training heart rate.
age = float(input("Enter your age: "))
rhr = int(input("Enter your resting heart rate: "))
thr = .7 * (220 - age) + (.3 * rhr)
print("Training heart rate:", round(thr), "beats/minute.")
                
