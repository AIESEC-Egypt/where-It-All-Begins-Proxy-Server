from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.


query_igv = """
    query Opportunities {
        opportunities(filters: {programmes: 7, status: "open"}, page: 1, per_page: 3000) {
            data {
                all_slots {
                    nodes {
                        available_openings
                        start_date
                    }
                }
                home_lc {
                    full_name
                }
                title                      
                id
            }
        }
    }
"""

query_igta = """
    query Opportunities {
        opportunities(filters: {programmes: 8, status: "open"}, page: 1, per_page: 3000) {
            data {
                all_slots {
                    nodes {
                        available_openings
                        start_date
                    }
                }
                home_lc {
                    full_name
                }
                title
                id
                sub_product {
                    name
                }
                specifics_info {
                    salary
                    salary_currency {
                        name
                    }
                }
                opportunity_duration_type {
                    duration_type
                }
            }
        }
    }
"""

query_igte = """
    query Opportunities {
        opportunities(filters: {programmes: 9, status: "open"}, page: 1, per_page: 3000) {
            data {
                all_slots {
                    nodes {
                        available_openings
                        start_date
                    }
                }
                home_lc {
                    full_name
                }
                title
                id
                specifics_info {
                    salary
                    salary_currency {
                        name
                    }
                }
                opportunity_duration_type {
                    duration_type
                }
            }
        }
    }
"""

access_token = ""
url = "https://gis-api.aiesec.org/graphql?access_token=" + access_token # paste your Content API endpoint
headers = {"contentType": "application/json", "Accept": "application/json",}


def igv_opens(req):
  payload = {"query": query_igv}
  r = requests.post(url, json=payload, headers=headers)
  json_data = r.json()
  return JsonResponse(json_data)

def igta_opens(req):
  payload = {"query": query_igta}
  r = requests.post(url, json=payload, headers=headers)
  json_data = r.json()
  return JsonResponse(json_data)

def igte_opens(req):
  payload = {"query": query_igte}
  r = requests.post(url, json=payload, headers=headers)
  json_data = r.json()
  return JsonResponse(json_data)
