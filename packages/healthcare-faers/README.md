# Healthcare - Drug Interactions / FAERS

Drug interactions through a populace.

# Data
Public url at https://tigergraph-testdrive-testdata.s3.amazonaws.com/healthcare/healthcare-data.tgz
SE bucket for SEs at s3://gjgeksbackup/healthcare-data.tgz

Unarchive to `/home/tigergraph/mydata/healthcare-faers/data/`

The data set for this is somewhat larger than many of our packages here.

## Expected counts for loaded data

# Fixes and enhancements
## Enhancement idea: add reactions vertices as in Test Drive

    The graph and data taken from our web site does not exactly match the graph and data used on the Test Drive.  The test drive has additional nodes regarding drugs and their reactions that this one lacks.

    One interesting query that could be added by the additional vertex types is `top_reaction_by_opiod`
