import glob
import os

package = 'com.tencent.mm'
for file in glob.glob('apk/' + package + '/**/*.class', recursive=True):
    if '$' in os.path.basename(file):
        continue
    relpath = os.path.relpath(file, 'apk/' + package)
    relfile = 'apk/' + package + '/java/' + relpath.replace('.class', '.java')
    if not os.path.exists(relfile):
        print(relfile)