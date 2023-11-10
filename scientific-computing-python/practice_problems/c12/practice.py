url = input('URL: ')
try:
    if '/' in url:
        url_split = url.split('/', 3)
        print(url_split)
        url_only = str(url_split[2])
        print(url_only)
    else:
        #print(url, ' is not a valid url link.')
        exit()

except:
    print(url, ' is not a valid url link.')
    exit()
