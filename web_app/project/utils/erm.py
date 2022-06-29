import requests
import csv
from SPARQLWrapper import SPARQLWrapper, JSON

def get_context(question, lang):
    URL = "https://demos.isl.ics.forth.gr/LODsyndesisIE/rest-api/getEntities"
    PARAMS = {'text':question,'equivalentURIs':'false','ERtools':'DBS_WAT'}
    resp = requests.get(url = URL, params = PARAMS)
    resp_text = resp.text.split('\n')
    if resp.status_code == 200 and len(resp_text) > 1:
        entity = resp_text[1].split("\t")[1]
    else:
        return '', ''
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("SELECT ?text WHERE { <"+entity+"> dbo:abstract ?text .filter(lang(?text)='"+lang+"')}")

    # Convert results to JSON format
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    context = result["results"]["bindings"][0]["text"]["value"]
    print(entity)
    return context, entity