#!/usr/local/opt/python/bin/python2.7

import json
import os
import re
import sys

from postal.parser import parse_address
from pprint import pprint

filepath= '%s/foia_agencies.json.1' % os.environ['HOME']

def agencies_fh(filepath):
    return open(filepath, 'r')

def agencies_json(filepath=filepath):
    raw_file = agencies_fh(filepath).readlines()
    ret = json.loads('\n'.join(raw_file))

    return ret

def is_agency_type(a_name, a_type):
    return re.search('.*%s.*' % a_type, a_name, re.IGNORECASE)

def agency_class(agency_name):
    all_types = ['police','library', 'court', 'sheriff', 
                 'Attorney General', 'election', 'school district',
                 'clerk', 'Finance', 'correction',
                 'public safety', 'revenue', 'highway patrol', 'transportation',
                 'fire department', 'district Attorney', 'beach',
                 'animal control', 'college', 'university', 'law Enforcement',
                 'secretary of state', 'school', 'city council', 'commissioners',
                 'lottery', 'governor', 'health', 'mayor']
    agency_type = [ t for t in all_types if is_agency_type(agency_name, t)]

    if len(agency_type) > 0:
        return agency_type[0]

    return 

def categ_address(address):
    return parse_address(address)
    

def fix_agency(agency_json):
    email = agency_json['E-mail Address']
    address = agency_json['Mailing Address']
    agency_name = agency_json['name']
    fax = agency_json['Fax Number']

    agency_type = agency_class(agency_name)
    parsed_address = categ_address('\n'.join(address))

    ret = {'email': email,
           'address': address,
           'parsed_address': parsed_address,
           'agency_name': agency_name,
           'fax_no': fax,
           'agency_type': agency_type}
    
    return ret

print json.dumps([ fix_agency(a) for a in agencies_json() ])
