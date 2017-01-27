str = 'X-DSPAM-Confidence: 0.8475'
copos= str.find (':')
print copos
host=str[copos+2:]
print host
fl=float(host)

