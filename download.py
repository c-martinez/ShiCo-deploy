import os
import sys
import requests
from clint.textui import progress

# times = "https://doi.org/10.5281/zenodo.1494140"
# kb = "https://doi.org/10.5281/zenodo.1189327"
doi = sys.argv[1]

# Download record-metadata
headers_meta = {'Accept': 'application/vnd.codemeta.ld+json'}
codemeta = requests.get(doi, headers=headers_meta, allow_redirects=True)
codemeta_json = codemeta.json()

# Download zenodo record info via API
repository_url = codemeta_json['codeRepository']
repository_url = repository_url.replace("zenodo.org/record/", "zenodo.org/api/records/")
headers_json = {'Accept': 'application/json'}
record = requests.get(repository_url, headers=headers_json, allow_redirects=True)
record_data = record.json()

# Make sure download dir exists
downloadDir = 'download/'
if not os.path.exists(downloadDir):
    os.mkdir(downloadDir)

for f in record_data['files']:
    url = f['links']['download']
    r = requests.get(url, allow_redirects=True, stream=True)

    # Save to file -- with progress bar
    filename = downloadDir + f['filename']
    with open(filename, 'wb') as fout:
        print('Downloading %s'%f['filename'])
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                fout.write(chunk)
                fout.flush()
