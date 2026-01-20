import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
calories = [2100, 2400, 1900, 2200, 2500]

fig, ax = plt.subplots(figsize=(6,4))

ax.bar (days, calories, color ='skyblue')
#ax.fill (days, calories , color ='skyblue')
ax.set_ylabel("calories burned this week ")
ax.set_xlabel("calories")


plt.plot(days,calories,'o',color='red')
plt.show()