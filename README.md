# DOI Analysis Tools
Resources mostly centered around analysis of paper statistics.



## AltmetricsByDOI.py

Fetches Altmetrics data via Altmetric API and exports in a .csv format.

#### Requirements:

- Python 3
- [jsonv](https://github.com/archan937/jsonv.sh) and its dependencies

#### Usage: 
`$ python AltmetricsByDOI.py DOIs CSV_headers OutputFile`

where:

- <a id="Usage_DOIs">DOIs</a> is a comma-newline-separated list of DOIs in string format.  
  `"10.1007/s10669-015-9577-y,\\n10.3139/9783446431775.001,\\n10.1053/trre.2003.1"`

- CSV_headers is a comma-separated string of desired fields to be included in the output csv. All headers should be available through the [Altmetric API](https://api.altmetric.com/docs/call_doi.html).  
  `"doi,readers_count"`
  
- <a id="Usage_OutputFile">OutputFile</a> is a string that names the file to be output to. It should have the extension .csv.  
  `AltmetricsByDOI.csv`
  

## CrossrefCitationsByDOI.py

Gets Crossref cited-by counts by DOI and exports in a .csv format.

#### Requirements

- Python 3
- [Crossref REST API python library](https://github.com/fabiobatalha/crossrefapi)

#### Usage:
`$ python CrossrefCitationsByDOI.py DOIs OutputFile Email`

where:

- DOIs: See <a href="#Usage_DOIs">above</a>.

- OutputFile: See <a href="#Usage_OutputFile">above</a>.

- Email is a string that contains the email to send with crossref requests. See [Crossref REST API page](https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service) for more information.  
  `"example@example.com"`


## GScholarCitationsByDOI.py
**Currently requires captcha** every dozen or so attempts; recommended use is not to do so.

#### Requirements

- Python 3
- [Scholarly](https://pypi.org/project/scholarly/)

#### Usage:
`$ python GScholarCitationsByDOI.py DOIs OutputFile`

where:

- DOIs: See <a href="#Usage_DOIs">above</a>.

- OutputFile: See <a href="#Usage_OutputFile">above</a>.


## Credits

These tools are made possible thanks to:
- jsonv by Paul Engel
- Altmetric
- Crossref
- Scholarly
- Google Scholar  

and Stack Overflow.
