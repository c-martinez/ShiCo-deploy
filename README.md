# Deploying ShiCo

This repository is meant to illustrate how [existing software](https://github.com/NLeSC/ShiCo) can be used with different datasets ([times](https://doi.org/10.5281/zenodo.1494140), [kb](https://doi.org/10.5281/zenodo.1189327) and [german news papers](https://doi.org/10.5281/zenodo.3255285)), enabling scholars to carry out research on different resources.

## Instructions for deploying ShiCo

We assume that you are [able to run Docker images](https://docs.docker.com/get-started/).

**NOTE:** on SE-Linux, make sure you can mount files -- you can run `setenforce 0` (although it may lead to vulnerabilities in your system) or you [change the label in the container context](https://docs.docker.com/engine/reference/commandline/run/) as shown [here](https://prefetch.net/blog/2017/09/30/using-docker-volumes-on-selinux-enabled-servers/).

You can run the scripts provided in this repo to download the ShiCo data and deploy a ShiCo instance.

### Download data for a given model

Use datahugger to download data:
```bash
datahugger https://doi.org/10.5281/zenodo.1494140 download
```

where DOI can be:

| Dataset | DOI  |
|---|---|
| times | https://doi.org/10.5281/zenodo.1494140 |
| kb    | https://doi.org/10.5281/zenodo.1189327 |
| German historic newspapers* | https://doi.org/10.5281/zenodo.3255285 |

**Note:** German newspapers contains 3 sets of `chronicling_america`, `europeana` and `sbb`, which can be deployed separately.

### Convert to gensim

Run the `convert.py` script:
```bash
python convert.py
```

Or, for the German newspapers:
```bash
python convert.py SET_NAME
```
where SET_NAME can be one of: `chronicling_america`, `europeana` or `sbb`.

### Deploy dockers

Run the `start.sh` bash script:
```bash
./start.sh
```

You should now have a ShiCo backend running on port 8000 and frontend running on port 3000 of your localhost. Visit http://localhost:3000/ to use your instance of ShiCo.
