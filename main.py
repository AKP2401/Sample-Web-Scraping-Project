import indiamart
import json

india_mart = indiamart.run.run()

with open('Scraped/indiamart.json', 'a') as outfile:
    outfile.write(json.dumps(india_mart, indent=0))
    outfile.write('\n')