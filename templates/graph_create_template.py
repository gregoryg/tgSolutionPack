#!/usr/bin/env python
# coding: utf-8

# # 1 - TigerGraph Schema Create Job
# 
# This script is used to automatically refresh the a TigerGraph instance on TGCloud
# The steps included are:
#
#     1. Create Schema
#     2. Create load jobs
#     3. Run load jobs
# 

# ### 1.3.1 - Installing and Importing Packages
# For this lab the critical package we will need is the pyTigerGraph package which is community built python connector. 
#

# FETCH ypTigerGraph package
import subprocess
import sys
subprocess.call('pip install pyTigerGraph -t /tmp/ --no-cache-dir'.split())

import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# 
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host="https://se-demo-bob.i.tgcloud.io"
graphname="cust360"
username="tigergraph"
password="*****" 

conn=tg.TigerGraphConnection(host=host, graphname=graphname, username=username, password=password)

secret=conn.createSecret()
token=conn.getToken(secret, setToken=True)
##print(token)

# 1. CREATE SCHEMA 
print(conn.gsql(''' USE GLOBAL

CREATE VERTEX Calendar() WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false"


''', options=[]))


# 2. Create load jobs
print(conn.gsql('''
USE GRAPH cust360

CREATE DATA_SOURCE S3 se_access_key="{'file.reader.settings.fs.s3a.access.key':'AKIA45R5O******','file.reader.settings.fs.s3a.secret.key':'AInBOILQ7IOUNXrR24LWTe*******'}" FOR GRAPH stanzaStage

BEGIN
CREATE LOADING JOB load_job FOR GRAPH cust360 {
   DEFINE FILENAME buttonCategoryData="$stanza_stage_key:{'file.uris':'s3://tg-stanza-data-bucket/stage/buttoncategories.json'}";
   LOAD buttonCategoryData TO VERTEX Category VALUES($"_id":"$oid", $"activities",$"calendar",$"facebook":"user",$"facebook":"page", $"facebook":"picture",$"keys", $"name",$"shortname",$"updated",$"recommendations",$"scraperCreated",$"created",$"logo",$"isDeleted",$"attractionId") USING JSON_FILE="true";
   LOAD buttonCategoryData TO TEMP_TABLE t7 (catoid, actoid) VALUES ($"_id":"$oid", flatten_json_array($"activities",$"$oid")) USING JSON_FILE ="true";
   LOAD TEMP_TABLE t7 TO EDGE cat_has_activities VALUES ($"catoid", $"actoid");
}
END

''', options=[]))

# 3. Run load job
print(conn.gsql('''USE GRAPH cust360
   RUN LOADING JOB load_job USING EOF="true"
'''))
