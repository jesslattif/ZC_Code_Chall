"""Take the hexadecimal digest of the MD5 hash of the string "All I really want to do is eat some pie" and enter it in the form on the original page."""

import hashlib as h

message = h.md5("All I really want to do is eat some pie".encode("utf8"))

print message.digest()

print message.digest()
# .decode("utf8")

print message.hexdigest()

