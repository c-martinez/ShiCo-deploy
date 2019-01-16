import os
import glob
import gensim
import tarfile

downloadDir = 'download/'
gensimDir = 'gensim/'

# Extract files if compressed
tarFiles = glob.glob(downloadDir + '*.tgz')
for tar in tarFiles:
    print('Extracting %s'%tar)
    tf = tarfile.open(tar)
    tf.extractall(downloadDir)

# Convert files to gensim format
models = glob.glob(downloadDir + '*[!vocab].w2v')
os.mkdir(gensimDir)
for modelName in models:
    print('Converting %s'%modelName)
    newModelName = modelName.replace(downloadDir, gensimDir)
    model = gensim.models.KeyedVectors.load_word2vec_format(modelName, binary=True)
    model.save(newModelName)
