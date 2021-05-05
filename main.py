import justdial
import indiamart
import json

india_mart = indiamart.run.run()

with open('Scraped/indiamart.json', 'a') as outfile:
    outfile.write(json.dumps(india_mart, indent=0))
    outfile.write('\n')

just_dial= justdial.run.run()

with open('Scraped/justdial.json', 'a') as outfile:
    outfile.write(json.dumps(just_dial, indent=0))
    outfile.write('\n')