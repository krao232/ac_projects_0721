import requests
import nferx_py.fn as nf
nf.authenticate('krao@nference.net', '32ad1c0c62b498557a46099d65c6ddb8')
AUTH = nf.AUTH
from nferx_py.utils import clean_string5

url = "https://preview.nferx.com/nucleus-api/v2/get_entities_for_token?fold_related=1&token_info=attributes%2Curl%2Chighest_priority_type%2Csources_claiming_synonym&token_sources=1&token={}"


def get_nucleus_pref_name(drug): 
    drug_token = clean_string5(drug)
    res = requests.get(url.format(drug_token), auth=AUTH)
    try:
        return res.json()['result']['data'][0]['PREFERRED_TOKEN']
    except: 
        return 'not_found'