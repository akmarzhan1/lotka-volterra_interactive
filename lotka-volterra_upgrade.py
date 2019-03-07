from scipy import integrate
from matplotlib.widgets import Slider

#initializing parameters
b = 0.3
d = 0.75
a=0.9
c=0.5

#lotka-volterra equation 
def lotka_volterra(X, t=0, a=0.9, c=0.5, b=0.3, d=0.75): #growth rate of prey and predator
    return np.array([ a*X[0] -   b*X[0]*X[1] ,  
                     -c*X[1] + d*b*X[0]*X[1] ])


t = np.linspace(0, 100,  5000) # time
initial_conditions = np.array([10, 5]) # initials conditions: 10 prey and 5 predators  

fig, ax = plt.subplots() #creating figures
plt.subplots_adjust(left=0.25, bottom=0.25) #adjusting them

l1, l2, = plt.plot(t, integrate.odeint(lotka_volterra, initial_conditions, t, (a, c, b, d))) 
#integrating a system of differential equations (this is why the graph in the end looks like it is not increasing as time goes)

axcolor = 'black' #creating places for the sliders
aa = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
cc = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
bb = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
dd = plt.axes([0.25, 0.0, 0.65, 0.03], facecolor=axcolor)

#creating sliders 
aaa = Slider(aa, 'Growth rate of prey', 0.0, 1.0, valinit=0.9)
ccc = Slider(cc, 'Death rate of predator', 0.0, 1.0, valinit=0.5)
bbb = Slider(bb, 'Death rate of prey', 0.0, 1.0, valinit=0.3)
sss = Slider(dd, 'Birth rate of predator', 0.0, 1.0, valinit=0.75)

#creating functions that update the graph as the parameters are changed on slides
def update(val):
    a=aaa.val
    c=ccc.val
    b=bbb.val
    d=ddd.val
    x=integrate.odeint(lotka_volterra, initial_conditions, t, (a, c, b, d))
    l1.set_ydata(x[:,0])
    l2.set_ydata(x[:,1])
    fig.canvas.draw_idle() 
    
#actually updating the parameters
aaa.on_changed(update)
ccc.on_changed(update)
bbb.on_changed(update)
ddd.on_changed(update)

#showing the graph
plt.show()
