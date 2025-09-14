# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g= 9.81 #Acceleration due to gravity
    height = h0 - 0.5 * g * t**2
    return height #Height can not be negative

# calling my calculate height function (1 second, 50)
t = int(input("Enter the time (seconds): "))
h0 = int (input("Enter the initial height(meters): "))
print(f"Height after {t} seconds: {calculate_height(h0,t)} m ")

# calling my calculate height function (2 second, 50)
t = int(input("Enter the time (seconds): "))
h0 = int (input("Enter the initial height(meters): "))
print(f"Height after {t} seconds: {calculate_height(h0,t)} m ")


# calling my calculate height function (3 second, 50)
t = int(input("Enter the time (seconds): "))
h0 = int (input("Enter the initial height(meters): "))
print(f"Height after {t} seconds: {calculate_height(h0,t)} m ")


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    Distance = V0 * t #Distance = Velocity * time
    return Distance


V0 = int(input("The velocity the car was is going at is (in m/s):")) #velocity is in meters/second

t = int(input("Enter time for car (in seconds): "))
Velocity1= calculate_car_distance(t)
print(f"The distance the car has travelled at 1 second is: {Velocity1} m")

t = int(input("Enter time for car (in seconds): "))
Velocity2= calculate_car_distance(t)
print(f"The distance the car has travelled at 2 second is :{Velocity2} m")

t = int(input("Enter time for car (in seconds): "))
Velocity3= calculate_car_distance(t)
print(f"The distance the car has travelling at 3 second is : {Velocity3} m")

