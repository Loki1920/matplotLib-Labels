import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.plot(x, y)
plt.title('sport watch data',loc = 'center',fontdict = font1)
plt.xlabel("average pulse",fontdict = font2)
plt.ylabel("calories burn",fontdict=font2)
plt.show()
