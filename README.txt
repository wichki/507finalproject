Overview
This program display information and charts related to poverty, unemployment and grocery stores (or access to fresh food). Charts available include: line chart unemployment rates for a county, its state and the national average for a specified time frame from 2007-2013; national unemployment map of counties for a specified year (2007-2013); national poverty map of counties just for 2016 (only available information); and a pie chart breaking down different categories of food sources available in a city, like grocery stores, farmer's markets and fresh markets.

Class:
I created class for each Yelp listing. I pinged the Yelp API, received and parsed the response object and populated a database Yelp table, which I pulled from based on a user's input. I then used that information to create a Yelp Listing object, which contained all of its relevant information. I used the Yelp Listing objects to create the pie chart, based on the instances' variables.

Function:
My primary function processes the user's command and then create the appropriate map, line chart or pie chart based on available information. 

APIs
This program uses Plotly and Yelp, both of which require API keys. Users can put their Yelp API key in a separate "secrets.py" file in the same folder as the program. To set your plotly key, visit https://plot.ly/python/getting-started/. More information can be found in the requirements.txt

Warnings
There are certain IDs in the CSV files that Plotly does not recognize and it will throw an warning message. Please note that this does not affect the data presentation. The unrecognized codes are general state codes used by the US Government. The map presents information on a county-by-county level.

Also, the charts may take some time to be created. All of the data is pulled from the database, but the number of counties is large (over 3000). The line charts and pie charts do not require as much time.

Commands available:

map
	Description: Creates a country or state chloropleth map.

	Example commands: "map national unemployment 2013", "map national poverty" or "map state ca 	unemployment 2009"

	Options:
		* national | state
		Description: Specifies a country or state within which to limit the
		results.

		* unemployment | poverty [poverty information only available for 2016 and just for the 		national level]
		Description: Specifies displaying unemployment or poverty information. Please note that 		not all combination of options are not possible.

		* year [available years: 2007-2013]
		Description: Specifies which year to display for unemployment information only.

linechart
	Description: Creates a line chart of county, state and national unemployment rates for a 	specific county for years that span 2007-2013.

	Example commands: "linechart state ca san francisco" or "linechart state mi washtenaw"

	Options:
	
		* state [e.g. az, mi or ca]
		Description: Specifies which state the county is in.

		* county [e.g. washtenaw, san francisco, los angeles]
		Description: Specifies which county information to display.

yelp
	Description: Creates a pie chart of grocery stores, farmer's markets,

	Example commands: "yelp state ca San Francisco", "yelp state ca Ann Arbor", "yelp state wa 	Seattle"

	Options:

		* state [e.g. az, mi or ca]
		Description: Specifies which state to display.

		* city name [e.g. San Francisco, Brooklyn, Austin]
		Description: Specifies a city within the the specified state. Please note that the city 		name is properly capitalized (see examples).
