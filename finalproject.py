import csv
import json
import sqlite3
import requests

import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from secrets import *

# SETTING UP DATABASES

DBNAME = 'db.db'

f1 = open("PovertyEstimates.csv")
f2 = open("Unemployment.csv")

poverty_csv = csv.reader(f1)
next(poverty_csv, None)

unemployment_csv = csv.reader(f2)
next(unemployment_csv, None)

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

try:
    conn = sqlite3.connect(DBNAME)
    # print(sqlite3.version)
    cur = conn.cursor()
except Error as e:
    print(e)

statement = '''
    DROP TABLE IF EXISTS 'Poverty';
'''
cur.execute(statement)

statement = '''
    DROP TABLE IF EXISTS 'Unemployment';
'''

cur.execute(statement)
conn.commit()


# Create Poverty Table
statement = """
    CREATE TABLE 'Poverty' (
    "Id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "FIPStxt" INTEGER,
    "State" TEXT,
    "Area_name" TEXT,
    "Rural-urban_Continuum_Code_2003" INTEGER,
    "Urban_Influence_Code_2003" INTEGER,
    "Rural-urban_Continuum_Code_2013" INTEGER,
    "Urban_Influence_Code_2013" INTEGER,
    "POVALL_2016" INTEGER,
    "CI90LBAll_2016" INTEGER,
    "CI90UBALL_2016" INTEGER,
    "PCTPOVALL_2016" REAL,
    "CI90LBALLP_2016" REAL,
    "CI90UBALLP_2016" REAL,
    "POV017_2016" INTEGER,
    "CI90LB017_2016" INTEGER,
    "CI90UB017_2016" INTEGER,
    "PCTPOV017_2016" REAL,
    "CI90LB017P_2016" REAL,
    "CI90UB017P_2016" REAL,
    "POV517_2016" INTEGER,
    "CI90LB517_2016" INTEGER,
    "CI90UB517_2016" INTEGER,
    "PCTPOV517_2016" REAL,
    "CI90LB517P_2016" REAL,
    "CI90UB517P_2016" REAL,
    "MEDHHINC_2016" INTEGER,
    "CI90LBINC_2016" INTEGER,
    "CI90UBINC_2016" INTEGER,
    "POV05_2016" INTEGER,
    "CI90LB05_2016" INTEGER,
    "CI90UB05_2016" INTEGER,
    "PCTPOV05_2016" REAL,
    "CI90LB05P_2016" REAL,
    "CI90UB05P_2016" REAL
);
"""
cur.execute(statement)

for i in poverty_csv:

    insertion = (None, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29], i[30], i[31], i[32], i[33])
    # print(insertion)
    statement = "INSERT INTO 'Poverty' "
    statement += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(statement, insertion)

conn.commit()

# Create Unemployment Table
statement = """
    CREATE TABLE 'Unemployment' (
    "Id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "FIPStxt" INTEGER,
    "State" TEXT,
    "Area_name" TEXT,
    "Rural_urban_continuum_code_2013" INTEGER,
    "Urban_influence_code_2013" INTEGER,
    "Metro_2013" INTEGER,
    "Civilian_labor_force_2007" INTEGER,
    "Employed_2007" INTEGER,
    "Unemployed_2007" INTEGER,
    "Unemployment_rate_2007" REAL,
    "Civilian_labor_force_2008" INTEGER,
    "Employed_2008" INTEGER,
    "Unemployed_2008" INTEGER,
    "Unemployment_rate_2008" REAL,
    "Civilian_labor_force_2009" INTEGER,
    "Employed_2009" INTEGER,
    "Unemployed_2009" INTEGER,
    "Unemployment_rate_2009" REAL,
    "Civilian_labor_force_2010" INTEGER,
    "Employed_2010" INTEGER,
    "Unemployed_2010" INTEGER,
    "Unemployment_rate_2010" REAL,
    "Civilian_labor_force_2011" INTEGER,
    "Employed_2011" INTEGER,
    "Unemployed_2011" INTEGER,
    "Unemployment_rate_2011" REAL,
    "Civilian_labor_force_2012" INTEGER,
    "Employed_2012" INTEGER,
    "Unemployed_2012" INTEGER,
    "Unemployment_rate_2012" REAL,
    "Civilian_labor_force_2013" INTEGER,
    "Employed_2013" INTEGER,
    "Unemployed_2013" INTEGER,
    "Unemployment_rate_2013" REAL,
    "Civilian_labor_force_2014" INTEGER,
    "Employed_2014" INTEGER,
    "Unemployed_2014" INTEGER,
    "Unemployment_rate_2014" REAL,
    "Civilian_labor_force_2015" INTEGER,
    "Employed_2015" INTEGER,
    "Unemployed_2015" INTEGER,
    "Unemployment_rate_2015" REAL,
    "Civilian_labor_force_2016" INTEGER,
    "Employed_2016" INTEGER,
    "Unemployed_2016" INTEGER,
    "Unemployment_rate_2016" REAL,
    "Median_Household_Income_2016" INTEGER,
    "Med_HH_Income_Percent_of_State_Total_2016" REAL
);
"""
cur.execute(statement)

for i in unemployment_csv:

    insertion = (None, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29], i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37], i[38], i[39], i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47])
    # print(insertion)
    statement = "INSERT INTO 'Unemployment' "
    statement += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(statement, insertion)

conn.commit()

cache_fname = "fproject_cache.json"
try:
    cache_file = open(cache_fname, "r")
    cache_contents = cache_file.read()
    cache_diction = json.loads(cache_contents)
    cache_file.close()
except:
    cache_diction = {}

class Yelp_Listing():
    def __init__(self, init_tuple):
        self.name = init_tuple[0]
        self.something_else = init_tuple[1]


def pingYelp(search_term, location, offset=None):
    baseURL = "https://api.yelp.com/v3/businesses/search"
    header = {"Authorization": "Bearer {}".format(API_KEY)}
    params = {}
    params["term"] = search_term
    params["location"] = location

    #First Request
    params["limit"] = 50
    params["offset"] = offset
    unique_id = baseURL + "?term=" + search_term + "?location=" + location + "?offset=" + str(params["offset"])
    # print(unique_id)

    if unique_id in cache_diction:
        # print("Getting cached data...")
        return cache_diction[unique_id]
    else:
        # print("Making a request for new data...")
        response = requests.get(baseURL, headers=header, params=params).text
        cache_diction[unique_id] = json.loads(response)
        dumped_json_cache = json.dumps(cache_diction, indent=2)
        f = open(cache_fname,"w")
        f.write(dumped_json_cache)
        f.close()
        return cache_diction[unique_id]

# Create Yelp Table
statement = "DROP TABLE IF EXISTS 'Yelp'"
cur.execute(statement)
conn.commit()

statement = """
    CREATE TABLE 'Yelp' (
    "Id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Yelp_Id" Text,
    "Alias" TEXT,
    "Name" TEXT,
    "Image_URL" TEXT,
    "Is_Closed" TEXT,
    "URL" TEXT,
    "Review_Count" INTEGER,
    "Category1" TEXT,
    "Category2" TEXT,
    "Category3" TEXT,
    "Rating" REAL,
    "Latitude" REAL,
    "Longitude" REAL,
    "Price" TEXT,
    "Address1" TEXT,
    "Address2" TEXT,
    "Address3" TEXT,
    "City" TEXT,
    "Zip_Code" TEXT,
    "State" TEXT,
    "Country" TEXT,
    "Phone" TEXT,
    "Distance" REAL
);
"""

cur.execute(statement)

def populate_table(results):
    for i in results["businesses"]:
        id = i["id"]
        alias = i["alias"]
        name = i["name"]
        image_url = i["image_url"]
        is_closed = i["is_closed"]
        url = i["url"]
        review_count = i["review_count"]
        rating = i["rating"]

        try:
            category1 = i["categories"][0]["alias"]
            category2 = i["categories"][1]["alias"]
            category3 = i["categories"][2]["alias"]
        except:
            category1 = ""
            category2 = ""
            category3 = ""
        latitude = i["coordinates"]["latitude"]
        longitude = i["coordinates"]["longitude"]

        try:
            price = i["price"]
        except:
            price = ""

        address1 = i["location"]["address1"]
        address2 = i["location"]["address2"]
        address3 = i["location"]["address3"]
        city = i["location"]["city"]
        zip_code = i["location"]["zip_code"]
        country = i["location"]["country"]
        state = i["location"]["state"]
        display_address = i["location"]["display_address"]
        phone = i["display_phone"]
        distance = i["distance"]

        insertion = (None, id, alias, name, image_url, is_closed, url, review_count, category1, category2, category3, rating, latitude, longitude, price, address1, address2, address3, city, zip_code, state, country, phone, distance)
        # print(insertion)

        statement = "INSERT INTO 'Yelp' "
        statement += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(statement, insertion)
        conn.commit()


def process_command(command):

    commands = ["map", "linechart", "exit", "help"]

    parameters = ["national", "state"]

    subparameters = ["unemployment", "poverty"]

    years = ["2007", "2008", "2009", "2010", "2011", "2012", "2013"]

    states_abbr = ["al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga",
              "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md",
              "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj",
              "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc",
              "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"]

    states = {
         "al":'Alabama',"ak":'Alaska',"az":'Arizona',"ar":'Arkansas',"ca":'California',"co":'Colorado', "ct":'Connecticut',"de":'Delaware',"fl":'Florida',"ga":'Georgia',"hi":'Hawaii',"id":'Idaho',
         "il":'Illinois',"in":'Indiana',"ia":'Iowa',"ks":'Kansas',"ky":'Kentucky',"la":'Louisiana',
         "me":'Maine', "md":'Maryland', "ma":'Massachusetts', "mi":'Michigan', "mn":'Minnesota',
         "ms":'Mississippi', "mo":'Missouri',"mt":'Montana',"ne":'Nebraska',"nv":'Nevada',
         "nh":'New Hampshire', "nj":'New Jersey', "nm":'New Mexico', "ny":'New York',
         "nc":'North Carolina', "nd":'North Dakota', "oh":'Ohio',
         "ok":'Oklahoma',"or":'Oregon', "pa":'Pennsylvania', "ri":'Rhode Island',
         "sc":'South Carolina',"sd":'South Dakota',"tn":'Tennessee',"tx":'Texas',"ut":'Utah',
         "vt":'Vermont',"va":'Virginia',"wa":'Washington',"wv":'West Virginia',
         "wi":'Wisconsin',"wy":'Wyoming'}

    # county information

    sql_select = "SELECT Area_name "
    sql_from = "FROM Unemployment "

    statement = sql_select + sql_from
    # print(statement)
    results = cur.execute(statement).fetchall()

    processed_command = {
        "command": "",
        "parameter": "",
        "subparameter": "",
        "state_abbr": "",
        "state": "",
        "year": "",
        "county": "",
    }

    # Splitting the command
    parse_input = command.split()
    # print(parse_input)
    for i in parse_input:
        if i in commands:
            processed_command["command"] = i
        elif i in parameters:
            processed_command["parameter"] = i
        elif i in subparameters:
            processed_command["subparameter"] = i
        elif i in states_abbr:
            processed_command["state_abbr"] = i
        elif i in years:
            processed_command["year"] = i
        elif i == "county" and len(parse_input) == 6:
            # print(parse_input.index(i))
            word_before = parse_input.index(i) - 1
            processed_command["county"] = parse_input[word_before]
        elif i == "county" and len(parse_input) > 6:
            # print(parse_input.index(i))
            two_word_county = parse_input[3] + " " + parse_input[4]
            # print(two_word_county)
            processed_command["county"] = two_word_county

    # print(processed_command)

    # MAP NATIONAL UNEMPLOYMENT COMMAND
    if processed_command["command"] == "map":
        if processed_command["parameter"] == "national" and processed_command["subparameter"] == "unemployment":
            sql_select = "SELECT FIPStxt, Area_name, Unemployment_rate_"
            sql_select += processed_command["year"] + " "
            sql_from = "FROM Unemployment "
            sql_join = ""
            sql_on = ""
            sql_where = ""
            sql_group = ""
            sql_having = ""
            sql_order = ""

            sql_limit = ""

            statement = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
            # print(statement)

            results = cur.execute(statement).fetchall()
            # print(results)

            fips = []
            counties = []
            unemployment_rate = []

            for i in results:
                fips.append(i[0])
                counties.append(i[1])
                try:
                    unemployment_rate.append(float(i[2]))
                except:
                    unemployment_rate.append(0)

            colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
                          "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
                          "#08519c","#0b4083","#08306b"]
            endpts = list(np.linspace(1, 12, len(colorscale) - 1))
            # fips = df_sample['FIPS'].tolist()
            # values = df_sample['Unemployment Rate (%)'].tolist()

            fig = ff.create_choropleth(
                fips=fips, values=unemployment_rate,
                binning_endpoints=endpts,
                colorscale=colorscale,
                show_state_data=False,
                show_hover=True, centroid_marker={'opacity': 0},
                asp=2.9, title='USA by Unemployment % ' + processed_command["year"],
                legend_title='% unemployed'
            )

            py.plot(fig, filename='choropleth_full_usa')
            return results

    # MAP NATIONAL POVERTY COMMAND
    if processed_command["command"] == "map":
        if processed_command["parameter"] == "national" and processed_command["subparameter"] == "poverty":
            sql_select = "SELECT FIPStxt, Area_name, PCTPOVALL_2016 "
            # sql_select += processed_command["year"] + " "
            sql_from = "FROM Poverty "
            sql_join = ""
            sql_on = ""
            sql_where = ""
            sql_group = ""
            sql_having = ""
            sql_order = ""

            sql_limit = ""

            statement = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
            # print(statement)

            results = cur.execute(statement).fetchall()
            # print(results)

            fips = []
            counties = []
            poverty_rate = []

            for i in results:
                fips.append(i[0])
                counties.append(i[1])
                try:
                    poverty_rate.append(float(i[2]))
                except:
                    poverty_rate.append(0)

            colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
                          "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
                          "#08519c","#0b4083","#08306b"]
            endpts = list(np.linspace(1, 25, len(colorscale) - 1))
            # fips = df_sample['FIPS'].tolist()
            # values = df_sample['Unemployment Rate (%)'].tolist()

            fig = ff.create_choropleth(
                fips=fips, values=poverty_rate,
                binning_endpoints=endpts,
                colorscale=colorscale,
                show_state_data=False,
                show_hover=True, centroid_marker={'opacity': 0},
                asp=2.9, title='USA by Unemployment % 2016',
                legend_title='% unemployed'
            )
            py.plot(fig, filename='choropleth_full_usa')
            return results

    # MAP STATE UNEMPLOYMENT COMMAND
    if processed_command["command"] == "map":
        if processed_command["parameter"] == "state":
            sql_select = "SELECT FIPStxt, Area_name, Unemployment_rate_"
            sql_select += processed_command["year"] + " "
            sql_from = "FROM Unemployment "
            sql_join = ""
            sql_on = ""
            sql_where = "WHERE STATE="
            sql_where += "'" + processed_command["state_abbr"].upper() + "'"
            sql_group = ""
            sql_having = ""
            sql_order = ""

            sql_limit = ""

            statement = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
            # print(statement)

            results = cur.execute(statement).fetchall()
            # print(results)

            fips = []
            counties = []
            unemployment_rate = []

            for i in results[1:]:
                fips.append(i[0])
                counties.append(i[1])
                try:
                    unemployment_rate.append(float(i[2]))
                except:
                    unemployment_rate.append(0)

            # print(unemployment_rate)

            endpts = list(np.mgrid[min(unemployment_rate):max(unemployment_rate):9j])
            colorscale = ["#030512","#1d1d3b","#323268","#3d4b94","#3e6ab0",
                          "#4989bc","#60a7c7","#85c5d3","#b7e0e4","#eafcfd"]

            scope = states[processed_command["state_abbr"]].split()

            # print(scope)

            fig = ff.create_choropleth(
                fips=fips, values=unemployment_rate, scope=scope, show_state_data=True,
                colorscale=colorscale, binning_endpoints=endpts, round_legend_values=True,
                plot_bgcolor='rgb(229,229,229)',
                paper_bgcolor='rgb(229,229,229)',
                legend_title='Unemployment Rate by County',
                county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                exponent_format=True,
            )
            py.plot(fig, filename='')
            return results


    # MAP LINECHART COMMAND
    x_years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    #county
    y_1 = ()

    #state
    y_2 = ()

    #national
    y_3 = (5.1, 6, 9.2, 9.6, 8.9, 8.1, 7.6, 6.5, 5.7, 5.4)

    national_average = []
    if processed_command["command"] == "linechart":
        if processed_command["parameter"] == "state":
            #get county unemployment data
            sql_select = "SELECT Unemployment_rate_2007, Unemployment_rate_2008, Unemployment_rate_2009, Unemployment_rate_2010, Unemployment_rate_2011, Unemployment_rate_2012, Unemployment_rate_2013, Unemployment_rate_2014, Unemployment_rate_2015, Unemployment_rate_2016 "
            sql_from = "FROM Unemployment "
            sql_join = ""
            sql_on = ""
            sql_where = "WHERE STATE="
            sql_where += "'" + processed_command["state_abbr"].upper() + "' "
            sql_where += "AND Area_name LIKE "
            sql_where += "'" + processed_command["county"] + " %County%'"
            sql_group = ""
            sql_having = ""
            sql_order = ""

            sql_limit = ""

            statement = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
            # print(statement)

            results = cur.execute(statement).fetchall()
            # print(results)
            for i in results:
                y_1 = i
            # print(y_1)

            #get statewide unemployment data
            sql_select = "SELECT AVG(Unemployment_rate_2007), AVG(Unemployment_rate_2008), AVG(Unemployment_rate_2009), AVG(Unemployment_rate_2010), AVG(Unemployment_rate_2011), Unemployment_rate_2012, Unemployment_rate_2013, Unemployment_rate_2014, Unemployment_rate_2015, AVG(Unemployment_rate_2016) "
            sql_from = "FROM Unemployment "
            sql_join = ""
            sql_on = ""
            sql_where = "WHERE Area_name="
            sql_where += "'" + states[processed_command["state_abbr"]] + "' "
            # sql_where += "AND Area_name LIKE "
            # sql_where += "'" + processed_command["county"] + " %County%'"
            sql_group = ""
            sql_having = ""
            sql_order = ""

            sql_limit = ""

            statement2 = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
            # print(statement)

            results2 = cur.execute(statement2).fetchall()
            # print(results2)
            for i in results2:
                y_2 = i
            # print(y_2)

            # COUNTY
            trace0 = go.Scatter(
                x = x_years,
                y = y_1,
                name = processed_command['county']
            )

            # STATE
            trace1 = go.Scatter(
                x = x_years,
                y = y_2,
                name = states[processed_command['state_abbr']]
            )

            # NATIONAL
            trace2 = go.Scatter(
                x = x_years,
                y = y_3,
                name = "National"
            )

            data = [trace0, trace1, trace2]

            py.plot(data, filename='basic-line')
            return results

# process_command("linechart state ca sacramento county 2007")

def load_help_text():
    with open('help.txt') as f:
        return f.read()

def interactive_prompt():
    # valid_commands = ["map", "linechart"]
    # valid_parameters = []
    # states = ["al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga",
    #           "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md",
    #           "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj",
    #           "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc",
    #           "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"]

    help_text = load_help_text()
    response = ''
    while response != 'exit':
        response = input('Enter a command: ')
        info = process_command(response)

        if response == "exit":
            exit()
        elif response == "help":
            print(help_text)
            continue
        if info:
            pass
        else:
            print("Command not recognized: ", response)

        # if response == 'help':
        #     print(help_text)
        #     continue

# results1 = pingYelp("farmer's market", "washtenaw")
# results2 = pingYelp("farmer's market", "washtenaw", 51)
#
# populate_table(results1)
# populate_table(results2)
#
# # TESTING SQLITE STATEMENTS FOR TABLES
# sql_select = "SELECT Name, Latitude, Longitude "
# sql_from = "FROM Yelp "
# sql_join = ""
# sql_on = ""
# sql_where = "WHERE Category1 = 'farmersmarket' or Category1 = 'grocery' or Category2 = 'farmersmarket' or Category2 = 'grocery' or Category3= 'farmersmarket' or Category3 ='grocery'"
# sql_group = ""
# sql_having = ""
# sql_order = ""
# sql_limit = ""
#
# statement = sql_select + sql_from + sql_join + sql_on + sql_where + sql_group + sql_having + sql_order + sql_limit
# # print(statement)
#
# results = cur.execute(statement).fetchall()
# # print(results)
#
#
# # PLOTTING THINGS
#
# business_names1 = []
# lat_vals1 = []
# lng_vals1 = []
# count=0
#
# for i in results:
#     # print(i)
#     business_names1.append(i[0])
#     lat_vals1.append(i[1])
#     lng_vals1.append(i[2])
#     count += 1
#
# # print(count)
#
# min_lat = 10000
# max_lat = -10000
# min_lon = 10000
# max_lon = -10000
#
# for str_v in lat_vals1:
#     v = float(str_v)
#     if v < min_lat:
#         min_lat = v
#     if v > max_lat:
#         max_lat = v
# for str_v in lng_vals1:
#     v = float(str_v)
#     if v < min_lon:
#         min_lon = v
#     if v > max_lon:
#         max_lon = v
#
# lat_axis = [min_lat, max_lat]
# lon_axis = [min_lon, max_lon]
#
# center_lat = (max_lat+min_lat) / 2
# center_lon = (max_lon+min_lon) / 2
#
# max_range = max(abs(max_lat - min_lat), abs(max_lon - min_lon))
# padding = max_range * .10
# lat_axis = [min_lat - padding, max_lat + padding]
# lon_axis = [min_lon - padding, max_lon + padding]
#
# fips = ['06021', '06023', '06027',
#         '06029', '06033', '06059',
#         '06047', '06049', '06051',
#         '06055', '06061']
#
# trace1 = dict(
# type = "scattergeo",
# locationmode = "USA-states",
# lon = lng_vals1,
# lat = lat_vals1,
# text = business_names1,
# mode = "markers",
# marker = dict(
#     size = 12,
#     opacity = 0.8,
#     reversescale = True,
#     autocolorscale = False,
#     symbol = "square",
#     color = "blue")
# )
#
# # trace2 = dict(
# # type = ""
# # )
#
# values = range(11)
#
# data = [trace1]
#
# center_lat = (max_lat+min_lat) / 2
# center_lon = (max_lon+min_lon) / 2
#
# layout = dict(
# title = 'Nearby Places',
# geo = dict(
#     scope='usa',
#     projection=dict( type='albers usa' ),
#     showland = True,
#     landcolor = "rgb(250, 250, 250)",
#     subunitcolor = "rgb(100, 217, 217)",
#     countrycolor = "rgb(217, 100, 217)",
#     lataxis = {'range': lat_axis},
#     lonaxis = {'range': lon_axis},
#     center = {'lat': center_lat, 'lon': center_lon },
#     countrywidth = 3,
#     subunitwidth = 3
#     ),
# )
#
# # fig = dict(data=data, layout=layout, fips=fips)
# # fig = ff.create_choropleth(fips=fips, data=data, values=values)
# # py.plot(fig, validate=False)
#
# # print(business_names, latitudes, longitudes)
#
# # FIPS_List = []
# # States_List = []
# # Counties_List = []
# # Unemployment_Rate_2007 = []
# # results = cur.execute(statement).fetchall()
# # for i in results:
# #     FIPS_List.append(i[0])
# #     States_List.append(i[1])
# #     Counties_List.append(i[2][:-4])
# #     Unemployment_Rate_2007.append(i[3])
#
# # get total number
# # total = 0
# # number = 0
# # for i in Unemployment_Rate_2007:
# #     if i == "":
# #         pass
# #     else:
# #         total += float(int(i))
# #         number += 1
# #
# # average_unemployment_2007 = total/number
# # print(average_unemployment_2007)
#

# print(len(process_command("map state az unemployment 2013")))
# process_command("map national unemployment 2012")


if __name__=="__main__":
    interactive_prompt()
