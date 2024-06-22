#p2
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

#p3
#goal: 計算出飛行員在接近光速時的時間流逝
#tp:乘坐飛船的人的旅行時間
#td:到達目的地的光的時間

v = input_velocity = float(input("輸入飛船的速度:"))
c = 299792458

percentage_of_light_speed = v / c 
print("相對於光年的速度的比率:",percentage_of_light_speed)

gamma = 1 / ((1 - (v**2 / c**2))**0.5)
print("時間的變化:",gamma)

#travel to Alpha Centauri
the_time_astronauts_travel = 4.3 / gamma
print("Travel time to Alpha Centauri =",the_time_astronauts_travel)
#travel to Barnard’s Star
the_time_astronauts_travel = 6.0 / gamma
print("Travel time to Barnard’s Star =",the_time_astronauts_travel)
#travel to Betelgeuse
the_time_astronauts_travel = 309.0 / gamma
print("Travel time to Betelgeuse =",the_time_astronauts_travel)
#travel to Andromeda Galaxy
the_time_astronauts_travel = 2000000.0 / gamma
print("Travel time to Andromeda Galaxy =",the_time_astronauts_travel)

#p4
h1 = float(input("input the height of the 1st ball:"))
m1 = float(input("input the mass of the 1st ball:"))
m2 = float(input("input the mass of the 2nd ball:"))

g = 9.8

#第一顆球滑到水平面的速度
v1 = (2 * g * h1)**0.5
v2 = (m1 * (v1**2) / m2)**0.5

print("the velocity of the 1st ball after slide:",v1)
print("the velocity of the 1st ball after collision:",v2)




