import numpy as np

class PIDNN:
    def __init__(self,iterations = 100):
        self.iterations = sampletime
        self.W1 = np.array([1,1,1,-1,-1,-1]).reshape(2,3) # Input layer weights
        self.W2 = np.array([np.random.randn(3,1)]) # Hidden layer weights
        self.error = 0
        self.reference = 0
        self.xH2 = 0
        self.xH3 = 0
        self.e = [0]
        self.lr = 0.05 # learning rate
        self.y = [0]
        self.u = [0,0]
        self.XH = 0
        self.itertations = 0
    def update_u(self,u):
        self.u.append(u)

    def NN(self,current,reference):
        self.reference = reference
        self.error = reference - current
        inputs = np.array([reference,current])


        # Outputs of input layer
        OH = np.dot(inputs,self.W1)
        XH = np.array([self.XH1(OH[0]),self.XH2(OH[1]),self.XH3(OH[2])])
        XY = XH[0]*self.W2[0] + XH[1]*self.W2[1] + XH[2]*self.W2[2]


        # Update values
        self.e.append(self.error)
        self.y.append(XY)
        self.XH = XH
        print(len(self.u))

        # Backpropagation
        self.BP()
        self.xH2 = self.XH[1]
        self.xH3 = self.XH[2]
        print('P : {}, I : {}, D : {}'.format(self.W2[0],self.W2[1],self.W2[2]))

        return(self.W2)

    def XH1(self,u1):
        if u1 > 1: return 1
        elif u1 < -1 : return -1
        elif u1 <= 1 and u1 >= -1: return u1

    def XH2(self,u2):
        if u2 + self.xH2 > 1 or u2 > 1: return 1
        elif u2 < -1 or u2 + self.xH2 < -1: return -1
        elif u2 + self.xH2 <=1 and u2 + self.xH2 >= -1: return float(u2 + self.xH2)

    def XH3(self,u3):
        if u3 - self.xH3 > 1 or u3 > 1: return 1
        elif u3 < -1 or u3 - self.xH3 < -1: return -1
        elif u3 - self.xH3 <= 1 and u3 - self.xH3 >= -1: return float(self.xH3 + u3)

    def BP(self): # Backpropagation
        delta = np.sign((self.y[-1]-self.y[-2])/(self.u[-1] - self.u[-2]))
        J = (1/(2*len(self.e))) * sum(list(map(lambda x : x*x,self.e)))
        dJ = (1/len(self.e)) * sum(self.e)
        print(dJ)

        gd = (self.lr*dJ*(-1)*delta*self.XH.reshape(3,1))
        self.W2 = self.W2 - (self.lr*dJ*(-1)*delta*self.XH.reshape(3,1))
        self.W2 = np.array(list(map(lambda x : abs(x),self.W2)))
        '''
        self.W2[0] = self.W2[0] - (self.lr*dJ*(-1)*delta*self.XH[0])
        self.W2[1] = self.W2[1] - (self.lr*dJ*(-1)*delta*self.XH[1])
        self.W2[2] = self.W2[2] - (self.lr*dJ*(-1)*delta*self.XH[2])
        '''
        print('XH : {}, E = {}%, All values are: {}'.format(self.XH, self.error*100,self.XH[0]==self.XH[1]))
