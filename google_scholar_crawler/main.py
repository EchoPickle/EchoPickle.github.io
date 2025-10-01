from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
print("DEBUG: script started!")
scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
print("DEBUG: GOOGLE_SCHOLAR_ID =", scholar_id)

print("DEBUG: start search_author_id")
author: dict = scholarly.search_author_id(scholar_id)
print("DEBUG: finished search_author_id")

print("DEBUG: start scholarly.fill")
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
print("DEBUG: finished scholarly.fill")

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))

print("DEBUG: start saving gs_data.json")
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)
print("DEBUG: saved gs_data.json")

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
print("DEBUG: saved gs_data_shieldsio.json")