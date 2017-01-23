import os
import glob
import queue
import subprocess
import threading

package = 'com.ximalaya.ting.android'
javapath = 'apk/' + package + '/java'
if not os.path.exists(javapath):
    os.makedirs(javapath)
q = queue.Queue()

classes = glob.glob('apk/' + package + '/**/*.class', recursive=True)
for file in classes:
    q.put(file)


def decomplie_class():
    while True:
        file = q.get()
        relpath = os.path.relpath(file, 'apk/' + package)
        if '$' in os.path.basename(file):
            pass
        else:
            tarpath = 'apk/' + package + '/java/' + os.path.dirname(relpath)
            if os.path.exists(tarpath + '/' + os.path.splitext(os.path.basename(file))[0] + '.java'):
                print(tarpath + '/' + os.path.basename(file) + 'exists')
            else:
                if not os.path.exists(tarpath):
                    try:
                        os.makedirs(tarpath)
                    except:
                        pass

                nested_class = []
                for file2 in glob.glob(os.path.dirname(file) + '/*.class'):
                    if os.path.basename(file2).startswith(os.path.basename(file)[0] + '$'):
                        nested_class.append(file2)
                commend = ('java -jar fernflower.jar'.split(' '))
                commend.append(file)
                commend.extend(nested_class)
                commend.append(tarpath)
                subprocess.call(commend)
        q.task_done()


for i in range(10):
    t = threading.Thread(target=decomplie_class)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()

q.join()
