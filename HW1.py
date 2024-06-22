Force = float(input("enter the force:"))
mass_m1 = float(input("enter the mass of m1:"))
distance = float(input("enter the distance:"))

𝐺 = 6.67 * (10**-11)
c = float(299792458)

#formula 1 

mass_m2 = ((distance**2) * Force)/( 𝐺 * mass_m1)

print("the mass of m2 is:", mass_m2)

#formula 2

E = mass_m2 * (c**2)

print(" the energy E of the object 2 is:",E)
