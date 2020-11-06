import numpy as np

class PID():
    def __init__(self,P,I,D):
        self.P = P
        self.I = I
        self.D = D
        self.t_previous = 0
        self.last_error = 0
        self.E = 0

    def output(self,t_current,desired_speed,current_speed):
        delta = t_current - self.t_previous
        error = desired_speed - current_speed
        
        self.E += self.E * delta
        
        proportional = self.P * error
        integral = self.I * self.E
        derivative = self.D * ((error-self.last_error)/delta)

        output = proportional + integral + derivative
        
        # Update
        self.last_error = error
        self.t_previous = t_current
        
        return output



class Pure_pursuit():
    def __init__(self,k,waypoints):
        self.k = k # constant
        self.waypoints = waypoints # waypoints to follow by car
        self.L = 2.9 # The distance between front and rear axel, the distance to front axel from center of gravity is 1.5

    def output(self,xc,yc,vc,yaw): # xc - current x position(center of gravity), yc- current y position(center of gravity)
        # Stanley works on rear axel position, xr - current rear x position, yr - current rear y position
        xr,yr = (xc - 1.4*np.cos(yaw)),(yc - 1.4*np.sin(yaw))

        # look-ahead distance(ld) is a function with variable vc - current speed ld(vc) = k*vc, according to the paper ld should be a value between 3-25
        ld = self.k*vc

        # Calculations to find goal points(gx,gy) which distance to our position(xr,yr) is the closest value to look-ahead distance
        distance = np.array([(ld - np.sqrt(np.power(xr-self.waypoints[i][0],2)+np.power(yr-self.waypoints[i][1],2))) for i in range(len(self.waypoints))])
        index = int(np.where(distance == distance.min())[0])
        gx,gy = self.waypoints[index][0],self.waypoints[index][1]

        # Alpha is a half of curvature between goal points and current position
        alpha = np.arctan2(gy-yr,gx-xr) - yaw
        steering_angle = np.arctan2(2*1.5*np.sin(alpha)/ld,1.0)

        return steering_angle
