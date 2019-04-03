# $1: List of DOIs, CSV
# $2: File name to write to
# Usage: DoiToCsv ListOfDOINumbersCSVTitle

#Example: python DoiToCsv.py "10.1007/s10669-015-9577-y,\\n10.3139/9783446431775.001,\\n10.1053/trre.2003.1" "altmetrics.csv"

import sys
import subprocess
import time

# csv_headers = "doi,title,journal,pmid,uri,cohorts.pub,cohorts.sci,cohorts.com,cohorts.doc,altmetric_id,is_oa,cited_by_fbwalls_count,cited_by_gplus_count,cited_by_msm_count,cited_by_posts_count,cited_by_rh_count,cited_by_tweeters_count,cited_by_weibo_count,cited_by_wikipedia_count,cited_by_patents_count,cited_by_accounts_count,score,history.1y,history.6m,history.3m,history.1m,history.1w,history.6d,history.5d,history.4d,history.3d,history.2d,history.1d,history.at,url,readers.citeulike,readers.mendeley,readers.connotea,readers_count"

def doi_to_csv(doi_list, csv_headers, file_name):
    #OVERWRITE file and add headers
    f = open(file_name, "w")
    f.write(csv_headers + "\n")
    f.close()

    for doi in doi_list.split(',\n'):
        #All possible because of the Altmetric api
        #If this script stops working, check that you're not over the request limit
            #Check request headers and find following:
                #x-dailyratelimit-limit, x-dailyratelimit-remaining
                #x-hourlyratelimit-limit, x-hourlyratelimit-remaining
        url = "https://api.altmetric.com/v1/doi/" + doi
        response = subprocess.check_output(['curl', url])
        #Default format of response is Bytes, decode to str
        response = response.decode()
        #Not Found DOIs are simply not added to the .csv.
        if (response != "Not Found"):
            #Bug in jsonv means that we have to have at least two elements in the jsonv input
            response = "[" + response + "," + response + "]"
            #Convert to string and prep for subprocess command format by replacing all instances of ' character
            response = response.replace("\'", "&apos;")
            #Pretty-print, convert to csv, take first one (because we passed the same thing twice), and append to file
            command = "echo \'" + response + "\' | python -m json.tool | jsonv " + csv_headers + " | head -n 1 >> " + file_name
            subprocess.run(command, shell=True)
        #At the request of Altmetric, limit responses to 1 per second
        time.sleep(1);

if __name__ == "__main__":
    if (sys.argv[1] == "-v" or sys.argv[1] == "--version"):
        print("v1.1")
    elif (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print('''
            DoiToCsv v1.1

            Usage: python DoiToCsv.py string_of_dois string_of_headers string_file_name

            Takes in a list of DOIs and makes an Altmetric API request, parses
            the response, and writes the comma-separated list of values
            corresponding to the specified headings to the provided file.

            string_of_dois: comma-separated list of DOIs. Should have a comma and a
            newline after every DOI.
                (ex: 10.1007/s10858-015-9995-7,\\n10.1210/me.2015-1133)

            string_of_headers: comma-separated list of csv headers. See the
            Altmetric API reference for a full list of valid csv headers.
                (ex: doi,title,journal,pmid,uri,cohorts.pub,cohorts.sci,cohorts.com,cohorts.doc,altmetric_id)

            string_file_name: file to be OVERWRITTEN.
                (ex: AltmetricsByDOI.csv)


            This script is made possible thanks to a number of resources, including:
                jsonv by Paul Engel
                Altmetric
        ''')
    else:
        doi_to_csv(sys.argv[1], sys.argv[2], sys.argv[3])

#Altmetric csv_headers example: doi,title,journal,pmid,uri,cohorts.pub,cohorts.sci,cohorts.com,cohorts.doc,altmetric_id,is_oa,cited_by_fbwalls_count,cited_by_gplus_count,cited_by_msm_count,cited_by_posts_count,cited_by_rh_count,cited_by_tweeters_count,cited_by_weibo_count,cited_by_wikipedia_count,cited_by_patents_count,cited_by_accounts_count,score,history.1y,history.6m,history.3m,history.1m,history.1w,history.6d,history.5d,history.4d,history.3d,history.2d,history.1d,history.at,url,readers.citeulike,readers.mendeley,readers.connotea,readers_count
