Overview
This program display information and charts related to poverty, unemployment and grocery stores (or access to fresh food). Charts available include: line chart unemployment rates for a county, its state and the national average for a specified time frame from 2007-2013; national unemployment map of counties for a specified year (2007-2013); national poverty map of counties just for 2016 (only available information); and a pie chart breaking down different categories of food sources available in a city, like grocery stores, farmer's markets and fresh markets.

APIs
This program uses Plotly and Yelp, both of which require API keys. Users can put their Yelp API key in a separate "secrets.py" file in the same folder as the program. To set your plotly key, visit https://plot.ly/python/getting-started/.

Warnings
There are certain IDs in the CSV files that Plotly does not recognize and it will throw an warning message. Please note that this does not affect the data presentation. The unrecognized codes are general state codes used by the US Government. The map presents information on a county-by-county level.

Also, the charts may take some time to be created. All of the data is pulled from the database, but the number of counties is large (over 3000). The line charts and pie charts do not require as much time.

Commands available:

map
	Description: Creates a country or state chloropleth map.

	Example commands: "map national unemployment 2013", "map national poverty" or "map state ca unemployment 2009"

	Options:
		* national | state
		Description: Specifies a country or state within which to limit the
		results.

		* unemployment | poverty [poverty information only available for 2016]
		Description: Specifies whether to sort by rating or cocoa percentage

		* year [available years: 2007-2013]
		Description: Specifies which year to display for unemployment information only.

linechart
	Description: Creates a line chart of county, state and national unemployment rates for a specific county for 	years that span 2007-2013.

	Example commands: "linechart state ca san francisco county" or "linechart state mi washtenaw county"

	Options:
	
		* state [e.g. az, mi or ca]
		Description: Specifies which state the county is in.

		* county [e.g. washtenaw, san francisco, los angeles]
		Description: Specifies which county information to display.

yelp
	Description: Creates a pie chart of grocery stores, farmer's markets,

	Example commands: "yelp state ca San Francisco", "yelp state ca Ann Arbor", "yelp 	state wa Seattle"

	Options:

		* state [e.g. az, mi or ca]
		Description: Specifies which state to display.

		* city name [e.g. San Francisco, Brooklyn, Austin]
		Description: Specifies a city within the the specified state. Please note that the city name is properly capitalized (see examples).
