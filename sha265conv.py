from hashlib import sha256
import sys
print(sha256(sys.argv[1].encode("utf-8")).hexdigest())
