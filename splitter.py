#incredibly hacky, but works with pickled data from muckrock.py
#This is needed because the API doesn't directly provide email addresses.

def stats2():
    results = []
    for key,val in pages.items():
        page_result = {}
        splitval = val.splitlines()
        agency_name = [ re.sub('<[^>]+>','',i) for i in splitval if i.startswith('<h1>') ][0]
        state =  [ re.sub('<[^>]+>','',i) for i in splitval if i.startswith('<h2>') ][0]
        page_result['state'] = state
        page_result['agency-name'] = agency_name
        page_result['url'] = key
        idx = splitval.index('<dl class="stats">')
        splitval = splitval[idx:]
        endidx = splitval.index('</dl>')
        splitval = splitval[1:endidx]
        splitval = ''.join(splitval)
        splitval = re.split('<dt>',splitval)
        for i in splitval:
            isplit = re.split('<\/*d[td]> *',i)
            ikey =  isplit.pop(0)
            if re.match('^ *$',ikey):
                continue
            ivals = re.split('<[^>]*>',''.join(isplit))
            ivals = [ j for j in ivals if j and not re.match('^ *$',j) ]
            page_result[ikey] = ivals
        results.append(page_result)
    return results
