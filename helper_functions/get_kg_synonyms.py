import json
import requests

from config import *
from urllib.parse import urlencode


def _get_kg_synonyms(token, version):
    url = 'https://preview.nferx.com/nucleus-api/v1/get_entities_for_token'
    params = {'token': token,
              'version': version,
              'fold_related': 1}
    params = urlencode(params)
    r = requests.get('{}?{}'.format(url, params), auth=AUTH)
    try:
        return r.json()
    except json.JSONDecodeError:
        pass


def get_kg_synonyms(token, version='nucleus_v1_6_1_2', entity_types=None, return_pref_token=False):
    synonyms = _get_kg_synonyms(token, version)
    if return_pref_token:
        blank = token
    else:
        blank = [token]

    if not synonyms:
        return blank
    if not synonyms['success']:
        return blank

    synonyms = synonyms['result']['data']
    if entity_types:
        synonyms = [s for s in synonyms if s['entity_type'] in entity_types]

    if not len(synonyms):
        return blank

    synonyms = synonyms[0]
    if return_pref_token:
        return synonyms['PREFERRED_TOKEN']

    synonyms = synonyms['tokens']
    synonyms = [k for k, v in synonyms.items() if v['attributes']['good_synonym']]

    return synonyms