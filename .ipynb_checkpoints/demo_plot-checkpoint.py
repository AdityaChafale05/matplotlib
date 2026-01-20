#with plt.xkcd():   (use  indentation)         #use this for comic style plot 

""" To check for available styles in matplotlib 
    plt.style.available
    
    for implementing a style:
    plt.style.use('style_name')
"""


# Import matplotlib's pyplot module for data visualization
import matplotlib.pyplot as plt 


# List of months used for x-axis (Jan to Dec)
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

#prices of Ram in 2024-25
prices_2025 = [3200,3300,3450,3600,3800,3950,4100,4050,3900,3700,3550,3400]
prices_2024 = [1100,1120,1180,1240,1290,1250,1250,350,420,560,700,850]

plt.plot(
    months,                    #data for months
    prices_2025,               #data for prices in 2025
    color="red",               #line color (red)
    linestyle=':',             #line style (dotted line)
    marker='o',                #marker style (circle)
    label='2025'               #label for the legend
    )

plt.plot(months,           #data for months
        prices_2024,       #data for prices in 2024        
        color="blue",      #line color (blue)
        linestyle='--',    #line style (dashed line)
        marker='^',        #marker style (triangle)
        label='2024'       #label for the legend
        )
# Label the x-axis
plt.xlabel("Months")

# Label the y-axis
plt.ylabel("Cost (₹)")

plt.title("DDR4 8GB RAM Prices (2024–2025)")

# Enable grid for better readability
plt.grid(True)

# Display legend to differentiate between years
plt.legend()

# Render the plot on screen
plt.show()

    