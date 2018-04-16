# Script that retrieves Wikipedia page content using the MediaWiki Rest API
# and a simple http get request. The name of the page is passed as a
# command-line paramter

import sys;
import json;
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
        print(r.json);
        return r.json;
    return {};


# Writes JSON data to file.
# This is used to pass the json to the C program
# TODO : LOOK INTO PIPES INSTEAD OF FILES TO PASS DATA
def JSON_to_file(data, filepath):
    file = open(filepath, "w");
    file.write(json.dumps(data));
    file.close();
    

def main():
    title = get_title();
    data = get_wiki_content(title);
    JSON_to_file(data, title + ".txt");

if __name__ == __main__:
    main();
     
    
    
        
