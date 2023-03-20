# converts a current directory name like C:\Users\Erikt\ShiCo-deploy to //c/users/erikt/shico-deploy

import os
import re

pwd = os.getcwd()
pwd = re.sub("\\\\", "/", pwd)
pwd = re.sub(":", "", pwd)
pwd = re.sub("^", "//", pwd)
pwd = pwd.lower()
print(pwd)
