# Steps to run

## Download data for a given model

```python
import requests
import os

record = requests.get("https://zenodo.org/api/records/1494141")
record_data = record.json()
downloadDir = 'download/'

os.mkdir(downloadDir)
for f in record_data['files']:
    url = f['links']['self']
    filename = downloadDir + f['key']
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
```
Run:
```bash
python download.py DOI
```

where DOI can be:

# times = "https://doi.org/10.5281/zenodo.1494140"
# kb = "https://doi.org/10.5281/zenodo.1189327"


## Convert to gensim

```python
import glob
import gensim

downloadDir = 'download/'
gensimDir = 'gensim/'

models = glob.glob(downloadDir + '*[!vocab].w2v')

os.mkdir(gensimDir)
for modelName in models:
    newModelName = modelName.replace(downloadDir, gensimDir)
    model = gensim.models.KeyedVectors.load_word2vec_format(modelName, binary=True)
    model.save(newModelName)
```

Run:
```bash
python convert.py
```


## Deploy dockers

```bash
docker run --rm -d --name shico_backend -p 8000:8000 -v $PWD/gensim/:/home/shico/word2vec/ -v $PWD/backend/:/tmp/config/ "cmartinez/shico"
docker run --rm -d --name shico_front -p 3000:3000 -v $PWD/frontend/:/tmp/config/ "cmartinez/shico-frontend"
```

Run:
```bash
./start.sh
```
