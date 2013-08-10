# cURL from command line: curl --data "eat_more_lunch=yes_please" https://zerocater.com/web_dev_challenge/  -> returns git URL with message:
"""Take the hexadecimal digest of the MD5 hash of the string "All I really want to do is eat some pie" and enter it in the form on the original page."""

import hashlib as h

message = h.md5("All I really want to do is eat some pie")

print message.hexdigest()

