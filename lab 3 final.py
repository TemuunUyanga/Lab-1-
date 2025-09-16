import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta_deg):
    #Convert theta from degrees to radians
    theta_rad = math.radians(theta_deg)
    x = round (r * math.cos(theta_rad), 5)
    y = round (r * math.sin(theta_rad), 5)
    return (x, y)
r = float(input("Enter the r (radius): "))
theta = float(input("Enter theta (angle in degrees (θ): "))
print(f"{polar_to_cartesian(r, theta)}")
    

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r = round(math.sqrt(x**2 + y**2), 5)
    theta = round(math.degrees(math.atan2(y, x)), 5)
    return (r, theta)

#input the values for x and y
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

#output the results
print (f"Polar coordinate (r,theta in degrees): {cartesian_to_polar(x, y)}")
print () 



# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    #Converstion of phi from degrees to radians
    phi_rad = math.radians(phi)
    omega = 2 * math.pi * f
    x_t = round(A * math.cos(omega * t + phi_rad), 5)
    return x_t

#input the values for A, f, phi and t
A = float(input("Enter the amplitude (A): "))
f = float(input("Enter the frequency (f): ")) 
phi = float(input("Enter the phase (phi in degrees): "))
t = float(input("Enter the time (t): "))

#output the results
print(f"Position of pendulum x(t): {pendulum_position(A, f, phi, t)}")
print ()