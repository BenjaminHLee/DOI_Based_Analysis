from crossref.restful import Works
import sys
import time

works = Works()


def crossref_ref_by_count(doi):
    work = works.doi(doi)
    if work == None:
        return -1
    else:
        return work['is-referenced-by-count']

# print(crossref_ref_by_count("10.1108/07363760110410263"))
# print(works.query("10.1108/07363760110410263"))
# print(works.query("10.1108/07363760110410263" + "&mailto=benlee@nuevaschool.org"))

if __name__ == "__main__":

    works.query("unable to specify mailto in works.query call&mailto=" + sys.argv[3])

    f = open(sys.argv[2], "w")
    f.write("doi,citedby_crossref")
    f.close()

    f = open(sys.argv[2], "a")

    for doi in sys.argv[1].split(',\n'):
        time.sleep(0.1);
        citedby = crossref_ref_by_count(doi)
        if citedby == -1:
            # Couldn't find doi, don't add it
            ()
        else:
            # Append doi to csv
            f.write("\n" + doi + "," + str(citedby))

    f.close()
