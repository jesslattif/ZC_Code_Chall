# cURL from command line: curl --data "eat_more_lunch=yes_please" https://zerocater.com/web_dev_challenge/  -> returns git URL with message:
"""Take the hexadecimal digest of the MD5 hash of the string "All I really want to do is eat some pie" and enter it in the form on the original page."""

import hashlib as h

message = h.md5("All I really want to do is eat some pie".encode("utf8"))

print message.digest()

print message.digest()
# .decode("utf8")? No, that doesn't work - 'utf8' codec can't decode byte 0xbf in position 2: invalid start byte


print message.hexdigest()

