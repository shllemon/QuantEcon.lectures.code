"""

@author: dgevans

"""

import numpy as np

class baseline_CES:
    beta = 0.9

    sigma = 2.

    gamma = 2.

    Pi = 0.5 *np.ones((2,2))

    G = np.array([0.1,0.2])

    Theta = np.ones(2)

    transfers = False

    #derivatives of utiltiy function
    def U(self,c,n):
        sigma = self.sigma
        if sigma == 1.:
            U = np.log(c)
        else:
            U = (c**(1-sigma)-1)/(1-sigma)
        return U - n**(1+self.gamma)/(1+self.gamma)

    def Uc(self,c,n):
        return c**(-self.sigma)

    def Ucc(self,c,n):
        return -self.sigma*c**(-self.sigma-1.)

    def Un(self,c,n):
        return -n**self.gamma

    def Unn(self,c,n):
        return -self.gamma * n**(self.gamma-1.)

#Model 1
M1_CES = baseline_CES()

#Model 2

M2_CES = baseline_CES()
M2_CES.G = np.array([0.15])
M2_CES.Pi = np.ones((1,1))
M2_CES.Theta = np.ones(1)

#Model 3 with time varying

M_time_example_CES = baseline_CES()

M_time_example_CES.Pi = np.array([[0., 1., 0.,   0.,  0., 0.],
                                  [0., 0., 1.,   0.,  0., 0.],
                                  [0., 0., 0., 0.5, 0.5,  0.],
                                  [0., 0., 0., 0.,   0.,  1.],
                                  [0., 0., 0., 0.,   0.,  1.],
                                  [0., 0., 0., 0.,   0.,  1.]])

M_time_example_CES.G = np.array([0.1, 0.1, 0.1, 0.2, 0.1, 0.1])
M_time_example_CES.Theta = np.ones(6) # Theta can in principle be random
