import sys
import os
import glob
import gensim
import tarfile

downloadDir = 'download/'
extractDir = 'extracted/'
gensimDir = 'gensim/'

subset = sys.argv[1] if len(sys.argv)>1 else ''
os.mkdir(gensimDir)

# Extract files if compressed
tarFiles = glob.glob(downloadDir + '*.tgz') + \
           glob.glob(downloadDir + '*' + subset + '*.tar.gz')
for tar in tarFiles:
    print('Extracting %s'%tar)
    tf = tarfile.open(tar)
    tf.extractall(extractDir)

# Convert files to gensim format
models = glob.glob(extractDir + '**/*[!vocab].w2v')
for modelName in models:
    print('Converting %s'%modelName)
    newModelName = gensimDir + os.path.basename(modelName)
    model = gensim.models.KeyedVectors.load_word2vec_format(modelName, binary=True)
    model.save(newModelName)
