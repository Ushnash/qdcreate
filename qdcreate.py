#!/bin/python

#Name: Ush Shukla (Red Hat Inc.)
#Date: 2018-04-19
#
#Description: This script complements the 'qdmanage' utility included with the QPid-Dispatch Router (QDR).
#             It allows users to extend their router network via a file, and persist the extended configuration to disk.


import subprocess
import argparse
import json

#Parse out the command line
parser=argparse.ArgumentParser()
parser.add_argument('infile',help="name of the file containing data for qdmanage")
parser.add_argument('-o','--outfile',help="file to append the results to. Ideally, this is an existing qdrouterd.conf file. If absent, data is written to STDOUT.")
args = parser.parse_args()

#Create a pointer to the input file and pass it to qdmanage for reading
infile = open(args.infile,'rU')

#call qdmanage with the input file's contents. Capture the output
try:
   result = subprocess.check_output(['qdmanage','create','--stdin'],stdin=infile,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as err:
   print "Error! " + err.output
   exit()

#The call succeeded. Begin the task of appending the input data to the conf file.
#Load the input data as a JSON object
injson = json.loads(result)

#Loop through the items in the input file.
#Rearrange them to take the form:
#type{
#     attribute_name:attribute_value
#   }
#To achieve this:
##Create a dictionary that represents our final output json
##Use the "type" attribute provided in the input json as the first key of our new dictionary
##Remove the "type" attribute from the input json
##Assign the resulting dictionary to the new key, above
##Create a JSON from this & modify it to our desired form

#Var to store final output
finalstr=""

for item in injson:

  #Temporary dictionary object which Python's JSON parser can operate on
  tempdict={}

  #save off our type, and remove it from the incoming JSON
  header=item['type']
  del item['type']

  #create a single entry in our new dictionary with the "type" as a key
  tempdict[header] = item

   #massage the JSON into the format we need (note: the final string is *NOT* correct JSON)
  tempstr=json.dumps(tempdict,indent=2).replace('"','').replace(':','',1).replace(',','').lstrip('{').rstrip('}')
  finalstr+=tempstr

#Write to the output file if we have it, otherwise print to screen
if args.outfile:
    outfile=open(args.outfile,'a+')
    outfile.write(finalstr)
    outfile.close()
else:
    print finalstr
