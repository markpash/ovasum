import tarfile
import sys
import hashlib


# .mf file parser, returns hashes nicely
def mfparser(hashfile):
    hashdict = {'ovf': [], 'vmdk': []}
    for line in hashfile:
        line = str(line, 'utf-8')
        if '.ovf' in line:
            hashdict['ovf'].append(line[-41:-1])
        elif '.vmdk' in line:
            hashdict['vmdk'].append(line[-41:-1])
    return hashdict


hashes = {}

# accept loads of inputs from cli, you can use "python ovasum.py *.ova"
for filename in sys.argv[1:]:

    # only process .ova inputs
    if filename.endswith('.ova'):
        print('\n' + 'checking ' + filename)
        try:
            with tarfile.open(filename) as ova:

                # find and process .mf file first
                for member in ova.getmembers():
                    if member.isfile() and member.name.endswith('mf'):
                        with ova.extractfile(member) as hashfile:
                            hashes = mfparser(hashfile)

                # find other files and check hashes
                for member in ova.getmembers():
                    if member.isfile() and member.name.endswith('ovf'):
                        ovfsha1 = hashlib.sha1()
                        with ova.extractfile(member) as ovf:
                            while True:
                                data = ovf.read(65536)
                                if not data:
                                    break
                                ovfsha1.update(data)
                            if ovfsha1.hexdigest() in hashes['ovf']:
                                print('ovf: PASSED')
                            else:
                                print('ovf: FAILED')
                    if member.isfile() and member.name.endswith('vmdk'):
                        vmdksha1 = hashlib.sha1()
                        with ova.extractfile(member) as vmdk:
                            while True:
                                data = vmdk.read(65536)
                                if not data:
                                    break
                                vmdksha1.update(data)
                            if vmdksha1.hexdigest() in hashes['vmdk']:
                                print('vmdk: PASSED')
                            else:
                                print('vmdk: FAILED')

        except:
                print('something went wrong on that file')
