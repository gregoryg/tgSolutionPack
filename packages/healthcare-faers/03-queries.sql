USE GRAPH HealthcareFaers
CREATE QUERY jaccard_nbor_reaction(VERTEX source, STRING etype, INT topK, INT sampSize) FOR GRAPH HealthcareFaers {
	//example: ReportedCase=100640876, etype=hasReactions, topK=100, sampSize=100
/* This query calculates the Jaccard Similarity between a given vertex and every other vertex.
Jaccard similarity = intersection_size / (size_A + size_B - intersection_size)
1. The JSON and FILE version keeps the top k pairs of vertices. The result in FILE version is not in order.
2. The Attribute version insert edges between the pairs, with the score as an edge attribute.
   A similarity edge with one FLOAT attribute in the schema is required for this version.
*/
        SumAccum<INT> @intersection_size, @@set_size_A, @set_size_B;
        SumAccum<FLOAT> @similarity;
        SumAccum<INT> @@tSize;

        Start (ANY) = {source};
        Start = SELECT s
        	FROM Start:s
                ACCUM @@set_size_A += s.outdegree(etype);

        Subjects = SELECT t
                   FROM Start:s-(etype:e)-:t;

        Others = SELECT t
                 FROM Subjects:s -(:e)- :t
                 SAMPLE sampSize EDGE when s.outdegree(etype) > sampSize
                 WHERE t != source
                 ACCUM t.@intersection_size += 1,
                       t.@set_size_B = t.outdegree(etype)
                 POST-ACCUM t.@similarity = t.@intersection_size*1.0/(@@set_size_A + t.@set_size_B - t.@intersection_size),
                        @@tSize += 1
                 ORDER BY t.@similarity DESC
                 LIMIT topK;


        PRINT Others;
        PRINT @@tSize;
}
CREATE QUERY mostReportedDrugsForCompany_v2(STRING companyName, INT k, STRING role) FOR GRAPH HealthcareFaers {
  #companyName=PFIZER, K=5,role=PS
	# Keep count of how many times each drug is mentioned.
	SumAccum<INT> @numCases;

   # 1. Find all the cases where the given pharma company is the 'mfr_sndr'
  Company ={PharmaCompany.*};
  Cases = SELECT c
  	FROM Company:s -(relatedTo:e)-> ReportedCase:c
	  WHERE s.mfr_sndr == companyName
	;

	#. 2. Find all the drug sequences for the selected cases.
	DrugSeqs = SELECT ds
	  FROM Cases:c -(hasSequences:e)-> DrugSequence:ds
    WHERE (role == "" OR ds.role_cod == role)
  ;

	# 3. Count the occurences of each drug mentioned in each drug sequence.
	TopDrugs = SELECT d
	  FROM DrugSeqs:ds -(hasDrugs:e)-> Drug:d
	  ACCUM d.@numCases += 1
	  ORDER BY d.@numCases DESC
	  LIMIT k
	;

	PRINT TopDrugs;
}
CREATE query topSideEffectsForTopDrugs(STRING companyName, INT k, STRING role)
   FOR GRAPH HealthcareFaers {
	  #companyName=PFIZER, K=5,role=PS

   # Define a heap structure which sorts the reaction map (below) by count
	TYPEDEF TUPLE<STRING name, INT cnt> tally;
	HeapAccum<tally>(k, cnt DESC) @topReactions;

	# Keep count of how many times each reaction or drug is mentioned.
	ListAccum<STRING> @reactionList;
	SumAccum<INT> @numCases;
	MapAccum<STRING, INT> @reactionTally;

   # 1. Find all the cases where the given pharma company is the 'mfr_sndr'
  Company ={PharmaCompany.*};
  Cases = SELECT c
  	FROM Company:s -(relatedTo:e)-> ReportedCase:c
	  WHERE s.mfr_sndr == companyName
	;

	# 2. For each case, attach a list of its reactions
	Tally = SELECT r
	  FROM Cases:c -(hasReactions:e)-> Reaction:r
	  ACCUM c.@reactionList += r.pt;

	# 3. Find all the drug sequences for the selected cases, and transfer
	#    the reaction list to the drug sequence.
	DrugSeqs = SELECT ds
	  FROM Cases:c -(hasSequences:e)-> DrugSequence:ds
    WHERE (role == "" OR ds.role_cod == role)
		ACCUM ds.@reactionList = c.@reactionList
  ;

	# 4. Count the occurences of each drug mentioned in each drug sequence.
	#    Also count the occurences of each reaction.
	TopDrugs = SELECT d
	  FROM DrugSeqs:ds -(hasDrugs:e)-> Drug:d
	  ACCUM d.@numCases += 1,
      FOREACH reaction in ds.@reactionList DO
		    d.@reactionTally += (reaction -> 1)
		  END
	  ORDER BY d.@numCases DESC
	  LIMIT k
	;

	# 5. Find only the Top K side effects for each selected Drug
	TopDrugs = SELECT d
		 FROM TopDrugs:d
		 ACCUM
		   FOREACH (reaction, cnt) IN d.@reactionTally DO
		     d.@topReactions += tally(reaction,cnt)
		   END
		 ORDER BY d.@numCases DESC
		;

	PRINT TopDrugs[TopDrugs.prod_ai, TopDrugs.@numCases, TopDrugs.@topReactions];
}

INSTALL QUERY ALL
