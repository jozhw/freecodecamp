# usiing the re package - for more information look up re.sub on python.org

import re
mstring = '2343243242j, ##sdkfsdfk8888****'
#clearnstring = re.sub('[^A-Za-z0-9]+', '', mstring)
    #above works to get all numbers and letters and join
#clearnstring = re.sub('\W+','', mstring )
    #above works to get all numbers and letter and join
clearnstring = re.sub('[^A-Za-z]', '', mstring)
print(clearnstring)
