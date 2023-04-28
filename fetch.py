"Fetch a resource from a URL and safe to a file"
# MCS 275 Spring 2023 Lecture 39-41

import sys
from urllib.request import urlopen
from urllib.error import URLError

# fetch.py 'http://example.com' out.html
# should access "http://example.com"
# save the payload (HTML) to a file called "out.html"

# Expect sys.argv to have length 3: script name, URL, output filename
if len(sys.argv) not in [2, 3]:
    print("Usage: {} URL OUTFILENAME".format(sys.argv[0]))
    exit(1)
elif len(sys.argv) == 2:
    # no output filename was specified; use a default
    print("Warning: Using default output filename 'out.html'")
    print("(This may not match the type of payload in the HTTP request.)")
    outfn = "out.html"
else:
    outfn = sys.argv[2]

url = sys.argv[1]

try:
    with urlopen(url) as r:
        with open(outfn, "wb") as fp:
            fp.write(r.read())
    print("Wrote '{}'".format(outfn))
except ValueError as e:
    # urlopen rejects this as a URL
    print("ERROR: Not recognized as a URL:", url)
except URLError as e:
    # Failure in urlopen
    print("ERROR: Fetching URL failed:", str(e))
