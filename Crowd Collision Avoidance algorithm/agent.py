import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

class Agent(object):


    def __init__(self, csvParameters, Rad_sensingor = 10, goalRadiusSq=1):

        self.id = int(csvParameters[0]) # the id of the agent
        self.gid = int(csvParameters[1]) # the group id of the agent
        self.pos = np.array([float(csvParameters[2]), float(csvParameters[3])]) # the position of the agent
        self.vel = np.zeros(2) # the velocity of the agent
        self.goal = np.array([float(csvParameters[4]), float(csvParameters[5])]) # the goal of the agent
        self.prefspeed = float(csvParameters[6]) # the preferred speed of the agent
        self.gvel = self.goal-self.pos # the goal velocity of the agent
        self.gvel = self.gvel/(sqrt(self.gvel.dot(self.gvel )))*self.prefspeed
        self.maxspeed = float(csvParameters[7]) # the maximum sped of the agent
        self.radius = float(csvParameters[8]) # the radius of the agent
        self.goalRadiusSq =goalRadiusSq # parameter to determine if agent is close to the goal
        self.atGoal = False # has the agent reached its goal?
        self.Rad_sensingor = Rad_sensingor # the sensing radius
        self.vnew = np.zeros(2) # the new velocity of the agent



    def computeNewVelocity(self, neighbors=[]):
        agent_array_neighbors = []  # create an empty list for the neighbors
        function_cost = []    # create an empty list for the cost function

        alpha = 1         # declare alpha as given
        beta = 1    #declare beta as given
        gamma = 2  #declare gamma as given

        H = 20  #create a sampling rate that is easily variable    #HERE THE 'H' VALUE CAN BE SET 200 FOR CROSSING AGENTS

        theta  = np.pi*np.random.uniform(0,2,H)         # declare angle for cartesian value in root(Rcos(theta and Rsin(theta)))
        radius = np.sqrt(np.random.uniform(0,4,H))      # declare radius value for cartesian value in root(Rcos(theta and Rsin(theta)))

        Vcandidate_x = radius*np.cos(theta)      #Candidate velocity along X- coordinate
        Vcandidate_y = radius*np.sin(theta)      #Candidate velocity along Y- coordinate
        Vsample = np.array([Vcandidate_x, Vcandidate_y]) #Array for the candidate velocity
        Vsample = Vsample.transpose()

        """print(radius.size)
        print(Vcandidate_x[1])
        print('vel in x {}'.format(Vcandidate_x))
        plt.figure()
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.axis('equal')
        plt.scatter(Vcandidate_x, Vcandidate_y, s = None)
        plt.show()
        print(np.array([]))
        """
        for Vcandidate in Vsample:
            ttc=[]    #Empty array for time to collision
            tc =[]    #Empty array for the minimum time to collision

            for agent in neighbors:     #DETERMINATION OF THE NEIGHBOR AGENTS WITHIN THE SENSING RADIUS
                if agent != self:  #Create a condition to avoid the repetition of agent's occurence in the list
                    Rad_sensing = sqrt(((self.pos[0] - agent.pos[0])**2) + (self.pos[1] - agent.pos[1])**2)   #Calculation for the sensing radius
                    if Rad_sensing <= self.Rad_sensingor:       #Condition for checking the distance with the sensing radius
                        #print('For these agents {}, these are the neighbors {}'.format(self.id, agent.id))   #Neighbors are determined here
                        agent_array_neighbors.append(agent)
                        length_radius   = self.radius + agent.radius    #Total radius
                        relative_position     =  agent.pos - self.pos
                        c = relative_position.dot(relative_position) - length_radius*length_radius

                        V_relative = agent.vel - Vcandidate
                        a = V_relative.dot(V_relative)
                        b = relative_position.dot(V_relative)
                        dtrmnt = b*b - a*c
                        if dtrmnt>=0 and b<0:   #Conditions for time for collision values
                            tau = c/(-b + sqrt(dtrmnt))
                            if tau <=0:
                                tau = 0
                        else:
                            tau = float('inf')
                    else:
                        pass
                        tau = float('inf')
                    ttc.append(tau)

            tc = min(ttc)   #Adding the minimum time to collision values to the list


            first_velocity = Vcandidate - self.gvel     #Difference between the candidate velocity and the goal velocity
            first_cost = sqrt(first_velocity.dot(first_velocity))
            second_velocity = Vcandidate - self.vel     #Difference between the candidate velocity and the goal velocity
            first_self_cost = sqrt(second_velocity.dot(second_velocity))
            cost_funct_goal = alpha*first_cost
            second_self_cost = beta*first_self_cost
            if tc!=0:   #Condition for avoiding the time to collision
                safety_function = gamma/tc      #Safety parameter in the cost function
                function_cost.append(cost_funct_goal+second_self_cost+safety_function)  #The cost function
            else:
                function_cost.append(float('inf'))

        cost_index = np.argmin(function_cost)    #The new velocity equation with respect to the cost function
        cost_minimum = min(function_cost)   #Calculation for minimum cost function
        V_new = np.array(Vsample[cost_index])
        if not self.atGoal:
            self.vnew[:] = V_new[:]   # here I just set the new velocity to be the goal velocity
            # self.vnew[:] = self.gvel[:]

    def update(self, dt):

        if not self.atGoal:
            self.vel[:] = self.vnew[:]
            self.pos += self.vel*dt   #update the position

            # compute the goal velocity for the next time step. Do not modify this
            self.gvel = self.goal - self.pos
            distGoalSq = self.gvel.dot(self.gvel)
            if distGoalSq < self.goalRadiusSq:
                self.atGoal = True  # goal has been reached
            else:
                self.gvel = self.gvel/sqrt(distGoalSq)*self.prefspeed
