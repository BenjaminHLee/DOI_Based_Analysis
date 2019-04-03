import scholarly
import sys
import time

def get_cite_count_by_doi(doi):
    query = scholarly.search_pubs_query(doi)
    try:
        result = next(query).fill()
        return(result.citedby) # Return citedby count
    except:
        return(-1) # Couldn't find doi via scholar

if __name__ == "__main__":

    f = open(sys.argv[2], "w")
    f.write("doi,citedby_gscholar")
    f.close()

    f = open(sys.argv[2], "a")

    for doi in sys.argv[1].split(',\n'):
        citedby = get_cite_count_by_doi(doi)
        time.sleep(1) # try not to get blocked from google scholar
        if citedby == -1:
            # Couldn't find doi, don't add it
            ()
        else:
            # Append doi to csv
            f.write("\n" + doi + "," + str(citedby))

    f.close()
