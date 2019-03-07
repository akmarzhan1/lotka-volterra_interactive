#sets parameters
prey_incr_rate = 1 #sets the parameter for the prey increase rate 
inter_prob = 0.5 #sets the parameter for the interaction probability with the wolves
pred_decr = 0.3 #sets the parameter for the predator death rate 
prob_encounters = 0.2 #sets the parameter for the probability of encounters 
time_step = 0.01 #specifies the time step of the algorithm
t = np.arange(0, 110, time_step) #specifies the time range and number of time steps

prey = np.empty_like(t) #creates an empty array with the same size as the time array
predator= np.empty_like(t) #creates an empty array with the same size as the time array
prey[0] = 10 #sets initial population of prey
predator[0] = 1 #sets the initial population of predators

for i in range(1, len(t)): #creates a loop for updating and recording the values of prey and predator populations
    prey[i] = prey[i-1] + time_step * (prey_incr_rate * prey[i-1] - inter_prob * predator[i-1] * prey[i-1]) 
    #Lotka-Volterra equation for the prey population dynamics 
    predator[i] = predator[i-1] + time_step * (prob_encounters * predator[i-1] * prey[i-1] - pred_decr * predator[i-1])
    #Lotka-Volterra equation for the predator population dynamics 

print("Final prey population is", prey[-1], "\n Final predator population is",predator[-1])
plt.plot(t, prey, color='green') #plotting the prey on the graph with respect to time
plt.plot(t, predator, color='orange') #plotting the predator on the graph with respect to time
plt.xlabel('Time (a.u.?)') #labels the x-axis
plt.grid() #creates a grid
plt.ylabel('Population size') #labels the y-axis
plt.legend(('Prey', 'Predators'), loc='upper left') #puts the legend in the upper right corner 
