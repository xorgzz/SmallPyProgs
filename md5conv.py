import hashlib as hl
import sys
print((hl.md5(sys.argv[1].encode())).hexdigest())
