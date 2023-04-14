import requests

url = 'http://localhost:5000/results'
r = requests.post(url, json={"sensor2": 641.82, "sensor3": 1589.70,
                             "sensor4": 1400.60, "sensor7": 554.36,
                             "sensor8": 2388.06, "sensor9": 9046.19,
                             "sensor11": 47.47, "sensor12": 521.66,
                             "sensor13": 2388.02, "sensor14": 8138.62,
                             "sensor15": 8.4195, "sensor17": 392.00,
                             "sensor20": 39.06, "sensor21": 23.42})

print(r.json())
