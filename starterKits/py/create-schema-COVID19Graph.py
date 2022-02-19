#!/usr/bin/env python

# # 1 - TigerGraph Schema Refresh Job
# 
# These scripts are used to automatically refresh the a TigerGraph instance on TGCloud (or EC2)
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Run schema change job
#     3. Create load jobs
#     4. Run load jobs
# 

# FETCH PACKAGES
import sys
import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "http://localhost"
username = "tigergraph"
password = "tigergraph"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH COVID19Graph

CREATE GRAPH COVID19Graph()
USE GRAPH COVID19Graph

CREATE SCHEMA_CHANGE JOB COVID19Graph_change_job FOR GRAPH COVID19Graph {

ADD VERTEX City(PRIMARY_ID city_id STRING, city STRING, elementary_school_count UINT, kindergarten_count UINT, university_count UINT, academy_ratio DOUBLE, elderly_population_ratio DOUBLE, elderly_alone_ratio DOUBLE, nursing_home_count UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Province(PRIMARY_ID province_id STRING, province STRING, population UINT, area FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Country(PRIMARY_ID id STRING, country STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX SearchStat(PRIMARY_ID id STRING, cold FLOAT, flu FLOAT, pneumonia FLOAT, coronavirus FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX WeatherStat(PRIMARY_ID id STRING, code UINT, avg_temp DOUBLE, min_temp DOUBLE, max_temp DOUBLE, precipitation DOUBLE, max_wind_speed DOUBLE, most_wind_direction DOUBLE, avg_relative_humidity DOUBLE) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX InfectionCase(PRIMARY_ID id STRING, infection_case STRING, confirmed UINT, ic_group BOOL) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX Year_(PRIMARY_ID id STRING, year_ INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Month_(PRIMARY_ID id STRING, month_ INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Day_(PRIMARY_ID id STRING, day_ INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX TravelEvent(PRIMARY_ID id STRING, latitude FLOAT, longitude FLOAT, visited_date DATETIME, travel_type STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Patient(PRIMARY_ID patient_id STRING, global_num UINT, birth_year UINT, infection_case STRING, contact_number UINT, symptom_onset_date DATETIME, confirmed_date DATETIME, released_date DATETIME, deceased_date DATETIME, state STRING, disease STRING, sex STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE PROVINCE_IN_COUNTRY(FROM Country, TO Province);
ADD UNDIRECTED EDGE CITY_IN_PROVINCE(FROM City, TO Province);
ADD UNDIRECTED EDGE WEATHER_CONDITION(FROM Province, TO WeatherStat, wc_date DATETIME);
ADD UNDIRECTED EDGE CASE_IN_CITY(FROM InfectionCase, TO City, latitude FLOAT, longitude FLOAT);
ADD UNDIRECTED EDGE CASE_IN_PROVINCE(FROM InfectionCase, TO Province);
ADD UNDIRECTED EDGE YEAR_MONTH(FROM Year_, TO Month_);
ADD UNDIRECTED EDGE MONTH_DAY(FROM Month_, TO Day_);
ADD UNDIRECTED EDGE SEARCH_STAMP(FROM Day_, TO SearchStat);
ADD UNDIRECTED EDGE WEATHER_STAMP(FROM Day_, TO WeatherStat);
ADD UNDIRECTED EDGE TRAVEL_EVENT_IN(FROM TravelEvent, TO City);
ADD UNDIRECTED EDGE TRAVEL_STAMP(FROM Day_, TO TravelEvent);
ADD DIRECTED EDGE INFECTED_BY(FROM Patient, TO Patient) WITH REVERSE_EDGE="reverse_INFECTED_BY";
ADD UNDIRECTED EDGE BELONGS_TO_CASE(FROM Patient, TO InfectionCase);
ADD UNDIRECTED EDGE CONFIRM_STAMP(FROM Day_, TO Patient);
ADD UNDIRECTED EDGE SYMPTOM_STAMP(FROM Day_, TO Patient);
ADD UNDIRECTED EDGE RELEASED_STAMP(FROM Day_, TO Patient);
ADD UNDIRECTED EDGE BIRTH_STAMP(FROM Year_, TO Patient);
ADD UNDIRECTED EDGE DECEASE_STAMP(FROM Day_, TO Patient);
ADD UNDIRECTED EDGE PATIENT_FROM_CITY(FROM Patient, TO City);
ADD UNDIRECTED EDGE PATIENT_FROM_PROVINCE(FROM Patient, TO Province);
ADD UNDIRECTED EDGE PATIENT_FROM_COUNTRY(FROM Patient, TO Country);
ADD UNDIRECTED EDGE PATIENT_TRAVELED(FROM Patient, TO TravelEvent);
}

RUN SCHEMA_CHANGE JOB COVID19Graph_change_job
DROP JOB COVID19Graph_change_job
''', options=[])
