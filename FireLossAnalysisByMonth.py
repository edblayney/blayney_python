import datetime
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Create the database
con = sqlite3.connect('/Users/edblayney/desktop/GitHub/blayney_python/FireLoss.db3')

# Create table
df = pd.read_csv('/Users/edblayney/desktop/GitHub/blayney_python/PropLoss.csv', names=['ID', 'Date', 'Total_Loss'], parse_dates=True)
df.to_sql("propertyloss", con, if_exists='replace', index=False)
cur = con.cursor()
con.commit()

# Query & group data
results = cur.execute("""SELECT strftime('%m', Date) AS 'month', SUM(Total_Loss/1000) as 'SumPropLoss / 1000' 
    FROM propertyloss 
    WHERE ID <> 'ID' AND Total_Loss > 0 GROUP BY month""")

# Add data to lists to prepare for visualization
months = []
SumPropLossByMonth = []
for row in results:
    SumPropLossByMonth.append(row[1])
    months.append(row[0])

# Visualize data

plt.bar(months, SumPropLossByMonth, color = 'red')
plt.ylabel("Property Loss in $ / 1000")
plt.xlabel("Month")
plt.title("Total Property Loss by Month of the Year")

plt.show()

plt.savefig('FireLossByMonthofYear.png')

# Close the Connection
con.close()

