## Calculate the distance from a storm.
prompt = "Enter number of seconds between lightning and thunder: "
numberOfSeconds = float(input(prompt))
distance = numberOfSeconds / 5
distance = round(distance, 2)
print("Distance from storm:", distance, "miles.")
