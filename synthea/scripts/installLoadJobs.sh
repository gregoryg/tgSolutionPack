#!/bin/bash

gsql < ./synthea/scripts/loadOrganizations.gsql
gsql < ./synthea/scripts/loadEncounters.gsql
gsql < ./synthea/scripts/loadPatientSymptoms.gsql
gsql < ./synthea/scripts/loadImaging.gsql
gsql < ./synthea/scripts/loadPayerTransitions.gsql
gsql < ./synthea/scripts/loadImmunizations.gsql
gsql < ./synthea/scripts/loadPayers.gsql
gsql < ./synthea/scripts/loadProcedures.gsql
gsql < ./synthea/scripts/loadAllergies.gsql
gsql < ./synthea/scripts/loadMedications.gsql
gsql < ./synthea/scripts/loadProviders.gsql
gsql < ./synthea/scripts/loadAttributes.gsql
gsql < ./synthea/scripts/loadObservations.gsql
gsql < ./synthea/scripts/loadZips.gsql
gsql < ./synthea/scripts/loadCareplans.gsql
gsql < ./synthea/scripts/loadOrganizations.gsql
gsql < ./synthea/scripts/loadConditions.gsql
gsql < ./synthea/scripts/loadPatient.gsql
gsql < ./synthea/scripts/loadDevices.gsql

## gsql < ./synthea/scripts/loadLocations.gsql
## gsql < ./synthea/scripts/loadPatientNotes.gsql
