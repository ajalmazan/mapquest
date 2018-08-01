import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd%7Cluu821u2nq%2Cb5%3Do5-94a5uf'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'

def mapquest_search_url(start:str, end:list) ->str:
    '''
    Create url for mapquest search
    '''
    
    search_parameters = [
        ('from',start),('to',end)
        ]

    return BASE_MAPQUEST_URL+'key='+MAPQUEST_API_KEY+'&'\
    +urllib.parse.urlencode(search_parameters, doseq=True)
        
def get_result(url: str) -> 'json':
    '''
    Read url and return json data
    '''

    response = None

    try:
    
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
      
        if response != None:
            response.close()


