import sys
import fairly

# times = "https://doi.org/10.5281/zenodo.1494140"
# kb = "https://doi.org/10.5281/zenodo.1189327"
doi = sys.argv[1]
downloadDir = 'download/'

# Open a remote dataset
dataset = fairly.dataset(doi)

# Store dataset to a local directory (i.e. clone dataset)
print('Will download the following files: ')
for f in dataset.files:
    print('  ', f)
local_dataset = dataset.store(downloadDir)