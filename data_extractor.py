from selectorlib import Extractor
import requests

r = requests.get('https://www.timeanddate.com/weather/usa/san-francisco')

c = r.text

extractor = Extractor.from_yaml_file('temperature.yaml')

e = extractor.extract(c)

print(extractor)

e