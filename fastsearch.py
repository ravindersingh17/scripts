#!/usr/bin/env python3
import os, sys

from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.fields import Schema, TEXT, ID

index_dir = os.path.join(os.path.expanduser("~"), ".fsearches")
search_dir = os.path.join(os.path.expanduser("~"), "lava_x1/MT6580-Kernel-3.18-master")
SLIM = 20

def create_db(root, extensions = []):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), \
            content=TEXT, textdata=TEXT(stored=True))

    if not os.path.exists(index_dir): os.mkdir(index_dir)

    ix = create_in(index_dir, schema)
    writer = ix.writer()

    for parent, dirs, files in os.walk(root):
        for f in files:
            if extensions and f.split(".")[-1] not in extensions: continue
            fullpath = os.path.join(parent, f)
            try: ftext = open(fullpath).read()
            except UnicodeDecodeError: continue
            writer.add_document(title=f, path=fullpath, \
                    content=ftext, textdata=ftext)
    writer.commit()

def search(query_str):
    ix = open_dir(index_dir)
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        for r in searcher.search(query, limit=SLIM):
            yield r["path"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fastsearch <searchterm>| --index")
        sys.exit(1)

    query_str = " ".join(sys.argv[1:]).strip()

    if query_str == "--index":
        print("Building index. Please wait...")
        create_db(search_dir, ["c", "h"])
        print("Indexing finished")
    else:
        for p in search(query_str):
            print("File: " + p)
            print(os.popen("grep -n \"%s\" %s" %(query_str, p)).read())
