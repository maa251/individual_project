# Script that retrieves Wikipedia page content using the MediaWiki Rest API
# and a simple http get request. The name of the page is passed as a
# command-line paramter

import sys;
import requests;

# Retrieves the title of the article we want to look up from the command-line
# arguments and returns it
# Returns blank String if not command-line argument is provided
def get_title():
    if len(sys.argv) == 0:
        return "";
    return sys.argv[0];

# Returns the Wikipedia page with the supplied title as a JSON object
# TODO: Handle bad requests better. Currently returning an empty JSON object
# if request is not succesful
def get_wiki_content(title):
    payload = {'action':'query','format':'json','prop':'revisions','titles':title,'rvprop':'content'}
    r = requests.get('https://wikipedia.org/w/api.php?', params=payload);
    if r.status_code == 200:
        return r.json;
    return {};
    
        
