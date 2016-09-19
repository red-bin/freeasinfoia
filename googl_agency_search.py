import search
from csepy import googlecse 

search_fh = open('/home/matt/states/search_terms.txt','r')
search_terms = map(str.strip,search_fh.readlines())

to_search = [ i for i in reader ]

reader = csv.reader(search_fh)

x = googlecse(SECRET_KEY='', CSE_ID='')

for agency_name,location  in to_search:
    search = '"%s" "%s" "%s" "%s"' % (agency_name, location, "foia", "contact")
    y = x.results(query=search)
    agency_results = {'agency_name':agency_name, 'location':location, 'results':y.result_list}
    final_results.append(agency_results)
    time.sleep(1)
