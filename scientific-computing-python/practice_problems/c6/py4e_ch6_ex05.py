str = 'X-DSPAM-Confidence: 0.8475 '
cololoc = str.find(':')
print(cololoc)
piece = str[cololoc + 2:]
print(piece)
fpiece = float(piece)
print(fpiece)
print(fpiece + 1000)
