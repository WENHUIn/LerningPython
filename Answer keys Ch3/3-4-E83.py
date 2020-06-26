## Display justices by party of appointing president.
justices = ["Scalia R", "Kennedy R", "Thomas R", "Ginsburg D",
            "Breyer D", "Roberts R", "Alito R", "Sotomayor D", "Kagan D"]
demAppointees = []
repAppointees = []
for justice in justices:
    if justice[-1] == 'D':
        demAppointees.append(justice[:-2])
    else:
        repAppointees.append(justice[:-2])
namesD = ", ".join(demAppointees)
namesR = ", ".join(repAppointees)
print("Democratic appointees:", namesD)
print("Republican appointees:", namesR)
