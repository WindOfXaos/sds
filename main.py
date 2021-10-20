from getUrls import *
from downClips import *
from splitClips import *
import sys

def main():
    print("Getting links...")
    link = sys.argv[1]
    numVids = sys.argv[2]
    chunks = sys.argv[3]
    try: browser = sys.argv[4]
    except: browser = 'edge' # (default) browser edge.     
    get(link, numVids, browser)

    print("Downloading videos...")
    down()

    print("Processing videos")
    split(chunks)

if __name__ == '__main__':
    main()