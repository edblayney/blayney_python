# blayney_python

Ed Blayney's Python for Data Final Project- Code Louisville Spring 2018

## Question

Is there more property damage due to fires in colder months than warmer ones?

## Methods

* Create a jupyter notebook to communicate my analysis
* Pulled property damage due to fire data from the Louisville Fire Department on data.louisvilleky.gov. 
* Saved the csv to my GitHub folder and proceeded to load the data into a sqlite3 database. 
* Used a SQL query to aggregate the property loss due to fire by month of the year eliminating any fires that didn’t result in property damage. Also, I divided the total loss for each month by 1000 to reduce clutter on the visualization. 
* Visualized the data using plt.bar to visualize total property loss by month of the year. 
* Then I created a CSV from intellicast.com of the historic monthly average highs and lows for each month of the year, and dropped it into my jupyter notebook next to my plot.

## Results

It appears there is a significant jump in property loss due to fires in colder months, particularly when the average low temperature drops below 40 degrees fahrenheit. 

## Special Requirements

None
