"Fetch a resource from a URL and safe to a file"
# MCS 275 Spring 2023 Lecture 39

import sys
from urllib.request import urlopen
from urllib.error import URLError
import argparse

# fetch.py 'http://example.com' out.html
# should access "http://example.com"
# save the payload (HTML) to a file called "out.html"

parser = argparse.ArgumentParser()
parser.add_argument("url",help="URL of the resource to fetch")
parser.add_argument("outfn",help="Output filename")

# process sys.argv into named arguments that we declared above
# or exit with a nice usage message if anything is wrong
args = parser.parse_args()

try:
    with urlopen(args.url) as r:
        with open(args.outfn, "wb") as fp:
            fp.write(r.read())
    print("Wrote '{}'".format(args.outfn))
except ValueError as e:
    # urlopen rejects this as a URL
    print("ERROR: Not recognized as a URL:", args.url)
except URLError as e:
    # Failure in urlopen
    print("ERROR: Fetching URL failed:", str(e))
