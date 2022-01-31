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
host = "https://mov-rec-tgws.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH HealthCareFAERSGraph

CREATE GRAPH HealthCareFAERSGraph()
USE GRAPH HealthCareFAERSGraph

CREATE SCHEMA_CHANGE JOB HealthCareFAERSGraph_change_job FOR GRAPH HealthCareFAERSGraph {

ADD VERTEX ReportedCase(PRIMARY_ID primaryid UINT, caseid UINT, caseversion UINT, fda_dt DATETIME, mfr_sndr STRING, reporter_country STRING, occr_country STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX PharmaCompany(PRIMARY_ID primaryid STRING, mfr_sndr STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX DrugSequence(PRIMARY_ID sequence_id STRING, seqid UINT, role_cod STRING, drugname STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Drug(PRIMARY_ID drug_id STRING, drugname STRING, prod_ai STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Reaction(PRIMARY_ID reaction_id STRING, pt STRING, drug_rec_act STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Outcome(PRIMARY_ID outcome_id STRING, outc_code STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX ReportSource(PRIMARY_ID reportsource_id STRING, rpsr_code STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Patient(PRIMARY_ID primaryid UINT, age FLOAT, age_code STRING, age_grp STRING, sex STRING, weight FLOAT, wt_code STRING, occp_cod STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Therapy(PRIMARY_ID therapy_id STRING, dsg_drug_seq UINT, start_date DATETIME, end_date DATETIME) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX Indication(PRIMARY_ID indication_id STRING, indi_drug_seq UINT, indi_pt STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD VERTEX vertex_type_1(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE";
ADD UNDIRECTED EDGE hasOutcomes(FROM ReportedCase, TO Outcome);
ADD UNDIRECTED EDGE hasReactions(FROM ReportedCase, TO Reaction);
ADD UNDIRECTED EDGE hasReportSources(FROM ReportedCase, TO ReportSource);
ADD UNDIRECTED EDGE hasPatient(FROM ReportedCase, TO Patient);
ADD UNDIRECTED EDGE hasSequences(FROM ReportedCase, TO DrugSequence);
ADD UNDIRECTED EDGE hasDrugs(FROM DrugSequence, TO Drug);
ADD UNDIRECTED EDGE isUsedInTherapy(FROM DrugSequence, TO Therapy);
ADD UNDIRECTED EDGE hasIndications(FROM DrugSequence, TO Indication);
ADD UNDIRECTED EDGE relatedTo(FROM ReportedCase, TO PharmaCompany);
ADD UNDIRECTED EDGE similarCaseTo(FROM ReportedCase, TO ReportedCase, wt FLOAT);
}

RUN SCHEMA_CHANGE JOB HealthCareFAERSGraph_change_job
DROP JOB HealthCareFAERSGraph_change_job
''', options=[])
