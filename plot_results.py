import matplotlib.pyplot as plt 
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import datetime as dt
import MySQLdb

# Open database connection
# Edit with your database credentials
db = MySQLdb.connect("localhost","root","AdriPi180","daftlistings" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Setting the figure size
fig = plt.figure()

# Plot Galway City Centre
cursor.execute("SELECT date, area, averagePrice FROM GalwayReview WHERE area='Galway City Centre';")
X = []
for row in cursor:
    if not row[0] in X:
        X.append(row[0])

## Set dates as X
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%b-%d'))
plt.gca().xaxis.set_major_locator(DayLocator(interval=5))

## Plot results as Y1
Y1 = [] 
for row in cursor:
    Y1.append(row[2])
plt.plot(X,Y1, label="Galway City Centre")

# Plot Galway City Suburbs
cursor.execute("SELECT date, area, averagePrice FROM GalwayReview WHERE area='Galway City Suburbs';")
Y2 = []
for row in cursor:
    Y2.append(row[2])
plt.plot(X,Y2, label="Galway City Suburbs")

# Plot Galway Commuter Towns
cursor.execute("SELECT date, area, averagePrice FROM GalwayReview WHERE area='Galway Commuter Towns';")
Y3 = []
for row in cursor:
    Y3.append(row[2])
plt.plot(X,Y3, label="Galway Commuter Towns")

# Labeling the X-axis 
plt.xlabel('Date') 

# Labeling the Y-axis 
plt.ylabel('Price') 

# Give a title to the graph
plt.title('Average price of houses per area') 
     
# Show a legend on the plot 
plt.legend()

# Rotates dates
plt.gcf().autofmt_xdate()

#Saving the plot as an image
fig.savefig('price_average.png', bbox_inches='tight', dpi=150)
