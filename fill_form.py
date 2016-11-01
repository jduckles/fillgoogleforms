import requests
import yaml
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fields",
    help="A yaml document mapping field_name to GForm field id")
parser.add_argument("values",
    help="A yaml document mapping field_name to value")
parser.add_argument("url",
    help="The URL of the google form to fill")

def fill_form(fields,values,url):
    fields_file = yaml.load(open(fields, 'r').read())
    values_file = yaml.load(open(values, 'r').read())
    out = {}
    for k,v in fields_file.items():
        if k in values_file.keys():
            out[v] = values_file[k]
        else:
            out[v] = "NA"
    r = requests.get(url, params=out)
    return(r.url)

if __name__ == "__main__":
    args = parser.parse_args()
    fields = args.fields
    values = args.values
    url = args.url
    print(fill_form(fields,values,url))
