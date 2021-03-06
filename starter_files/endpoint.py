import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://71e27e1f-4c3e-43c2-b152-ae58f9d13ede.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'r1ByzorqfEUyYO2iVzEAh9PPnv2uDwcm'

# Two sets of data to score, so we get two results back
data = {"data":
        [
    {
      "age": 35,
      "job": "technician",
      "marital": "single",
      "education": "university degree",
      "default": "no",
      "housing": "no",
      "loan": "yes",
      "contact": "cellular",
      "month": "jul",
      "day_of_week": "wed",
      "duration": 109,
      "campaign": 3,
      "pdays": 999,
      "previous": 0,
      "poutcome": "nonexistent",
      "emp.var.rate": 1.4,
      "cons.price.idx": 93.918,
      "cons.conf.idx": -42.7,
      "euribor3m": 4963,
      "nr.employed": 5228.1
    }
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


