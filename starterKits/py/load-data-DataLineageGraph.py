#!/usr/bin/env python
# coding: utf-8

# # 1 - TigerGraph Schema Refresh Job
# 
# This script is used to automatically refresh the Stanza TigerGraph instance on TGCloud
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Create load jobs
#     4. Run load jobs
# 


# FETCH PACKAGES
import subprocess
import sys

import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# 
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "https://tg-se-demo-hub.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123" 

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# Create load jobs

print(conn.gsql('''
   
USE GRAPH DataLineageGraph

GRANT DATA_SOURCE tg_s3_data_source TO GRAPH DataLineageGraph

CREATE LOADING JOB DataLineageGraph_load_job FOR GRAPH DataLineageGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Account.tsv\'}" TO VERTEX Account VALUES ($"primary_id", $"Name", $"Parentid", $"BillingStreet", $"BillingCity", $"BillingState", $"BillingPostalCode", $"BillingCountry", $"Phone", $"Website", $"Industry", $"AnnualRevenue", $"NumberofEmployees", $"Description", $"AccountOwnerid", $"CreatedDate", $"CreatedByid", $"LastModifiedDate", $"LastModifiedByid", $"LastActivityDate", $"AccountSource") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Campaign.tsv\'}" TO VERTEX Campaign VALUES ($"primary_id", $"Name", $"Parentid", $"Campaign_Type", $"Status", $"StartDate", $"EndDate", $"BudgetedCost", $"ActualCost", $"IsActive", $"Description", $"Number_Of_Leads", $"Number_Of_Converted_Leads", $"Number_Of_Responses", $"Number_Of_Opportunities", $"Number_Of_Won_Opportunities", $"Amount_All_Opportunities", $"Amount_Won_Opportunities", $"Hierarchy_Number_Of_Leads", $"Hierarchy_Number_Of_Converted_Leads", $"Hierarchy_Number_Of_Contacts", $"Hierarchy_Number_Of_Responses", $"Hierarchy_Number_Of_Opportunities", $"Hierarchy_Number_Of_Won_Opportunities", $"Hierarchy_Amount_Won_Opportunities", $"Hierarchy_Amount_All_Opportunities", $"Hierarchy_Budgeted_Cost", $"Hierarchy_Actual_Cost", $"Campaign_Owner_id", $"CreatedDate", $"LastModifiedDate", $"LastModifiedByid") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Contact.tsv\'}" TO VERTEX Contact VALUES ($"primary_id", $"Contact_id", $"FirstName", $"LastName", $"Phone", $"Email", $"Title", $"Department", $"LeadSource", $"Description", $"Contact_Ownerid", $"Has_Opted_Out_Of_Email", $"DoNotCall", $"CreatedDate", $"CreatedByid", $"LastModifiedDate", $"LastModifiedByid", $"Agree_to_Free_Trial_Lic_Agreement", $"Free_Trial_License_key", $"Free_Trial_Project_Notes", $"Free_Trial_Start_date", $"Free_Trial_Follow_Up_Notes", $"Free_Trial_Status", $"Signed_Up_For_Free_Trial_On", $"Dev_Edition_Agree_to_Lic_Agreement", $"Dev_edition_Date_Signed_Up", $"Free_Trial_Renewed_Date", $"LinkedIn_Profile", $"Goal_of_Developer_Edition_Trial", $"Employee_Band", $"Original_Lead_Source", $"Updated") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Lead.tsv\'}" TO VERTEX Lead VALUES ($"primary_id", $"FirstName", $"LastName", $"Title", $"Company", $"City", $"State", $"LeadSource", $"Status", $"Industry", $"Ownerid", $"HasOptedOutOfEmail", $"IsConverted", $"ConvertedDate", $"ConvertedAccountId", $"ConvertedContactId", $"ConvertedOpportunityId", $"IsUnreadByOwner", $"CreatedDate", $"CreatedById", $"LastModifiedDate", $"LastModifiedById", $"LastActivityDate", $"DoNotCall", $"LastTransferDate", $"Free_Trial_License_Key__c", $"Free_Trial_Start_Date__c", $"Signed_up_for_free_trial_on__c", $"Agree_to_FT_LicenseAgreement__c", $"Free_Trial_Project_Notes__c", $"Free_Trial_Follow_Up_Notes__c", $"Started_Test_Drive__c", $"Free_Trial_Status__c", $"LinkedIn_Profile__c", $"Dev_Edition_Agree_to_License_Agreement__c", $"Dev_Edition_Date_Signed_Up__c", $"Free_Trial_Renewed_Date__c", $"Goals_of_Developer_Edition__c", $"Goal_of_Developer_Edition_Other__c", $"Employee_Band__c", $"Are_you_familar_with_Graph_db__c", $"Competitor_Notes__c", $"Use_Graph_Score__c", $"What_s_your_interest_in_TigerGraph__c", $"Interest_Notes__c", $"Interest_Score__c", $"What_capabilities_are_you_looking_for__c", $"Do_you_have_a_timeline__c", $"Contacts_Role__c", $"Title_Rank__c", $"Timeline_Score__c", $"Role_Score__c", $"Title_Score__c", $"How_do_you_want_to_deploy_o__c", $"SQL_SCORE__c", $"Original_Lead_Source__c", $"Event_Notes_L__c", $"DiscoverOrg_EmployeeID__c", $"DiscoverOrg_CompanyID__c") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/CampaignMember.tsv\'}" TO VERTEX CampaignMember VALUES ($"primary_id", $"IsDeleted", $"CampaignId", $"LeadId", $"ContactId", $"Status", $"HasResponded", $"IsPrimary", $"CreatedDate", $"CreatedById", $"LastModifiedDate", $"LastModifiedById", $"SystemModstamp", $"FirstRespondedDate") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Opportunity.tsv\'}" TO VERTEX Opportunity VALUES ($"primary_id", $"IsDeleted", $"AccountID", $"IsPrivate", $"Name", $"Description", $"StageName", $"StageSortOrder", $"Amount", $"Probability", $"ExpectedRevenue", $"CloseDate", $"Opportunity_Type", $"NextStep", $"LeadSource", $"IsClosed", $"IsWon", $"ForecastCategory", $"ForecastCategoryName", $"CampaignId", $"HasOpportunityLineItem", $"Pricebook2Id", $"Ownerid", $"CreatedDate", $"CreatedById", $"LastModified", $"LastModifiedById", $"SystemModstamp", $"LastActivityDate", $"LastStageChangeDate", $"FiscalYear", $"FiscalQuarter", $"Budget_Confirmed__c", $"Discovery_Completed__c", $"ROI_Analysis_Completed__c", $"Referral_Partner_Company__c", $"Stage_Moved_to_POC__c", $"Are_you_familiar_with_Graph_db_O__c", $"Competitor_Notes_O__c", $"Contacts_Role_o__c", $"Do_you_have_a_timeline__c", $"How_do_you_want_to_deploy_o__c", $"Interest_Notes_o__c", $"Interest_Score_o__c", $"Role_Score_o__c", $"SQL_SCORE_o__c", $"Timeline_Score_o__c", $"Title_Rank__c", $"Title_Score_o__c", $"Use_Graph_Score_o__c") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Industry.tsv\'}" TO VERTEX Industry VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/LeadSource.tsv\'}" TO VERTEX LeadSource VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/ContactOnDate.tsv\'}" TO VERTEX ContactOnDate VALUES ($"primary_id", $"source", $"modifiedDate", $"email", $"phone", $"title") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/belongs_to.tsv\'}" TO EDGE belongs_to VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/converted.tsv\'}" TO EDGE converted VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/is_active_as.tsv\'}" TO EDGE is_active_as VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/is_part_of.tsv\'}" TO EDGE is_part_of VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Has_Role.tsv\'}" TO EDGE Has_Role VALUES ($"from", $"to", $"role", $"id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Has.tsv\'}" TO EDGE Has VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/Is_Driven_By.tsv\'}" TO EDGE Is_Driven_By VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/is_connected_to.tsv\'}" TO EDGE is_connected_to VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/belongs_to_industry.tsv\'}" TO EDGE belongs_to_industry VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/created_by.tsv\'}" TO EDGE created_by VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/is_from.tsv\'}" TO EDGE is_from VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/comes_from.tsv\'}" TO EDGE comes_from VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/comes_from_the.tsv\'}" TO EDGE comes_from_the VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/is_for_the.tsv\'}" TO EDGE is_for_the VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/DataLineage/wasUpdated.tsv\'}" TO EDGE wasUpdated VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}

RUN LOADING JOB DataLineageGraph_load_job USING EOF="true"
DROP JOB DataLineageGraph_load_job
''', options=[]))
