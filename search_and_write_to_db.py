from daftlistings import Daft, SaleType
from datetime import date
import MySQLdb

# Open database connection
# Edit with your database credentials
db = MySQLdb.connect("localhost","<username>","<password>","daftlistings" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Configure Daft.ie research
today = date.today()
area_array = ["Galway City Centre","Galway City Suburbs","Galway Commuter Towns"]

for x in area_array:
    daft = Daft()
    daft.set_area(x)
    daft.set_county("Galway City")
    daft.set_listing_type(SaleType.HOUSES)
    daft.set_min_beds(3)
    daft.set_max_price(300000)

    print("## Searching in " + x)

    # Launch the research
    listings = daft.search()

    # List data in the database

    for listing in listings:
        try:
            beds = listing.bedrooms
            address = listing.formalised_address
            link = listing.daft_link
            price = listing.price
            value = (today, x, beds, address, link, price)

            cursor.execute('INSERT INTO Galway VALUES (%s, %s, %s, %s, %s, %s)', value)
    
        except Exception as e:
            print("## Error: Impossible to retrieve " + link)
            print(e)
            pass

print("## Done Searching")

try:
    # Commit changes in the database
    db.commit()
    print("## Data written successfully to the database")
except:
    # Roolback changes in the database
    print("## Error: Could not commit")
    db.rollback()

# disconnect from server
print("## Closing database connection and exiting")
db.close()
