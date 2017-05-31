#!/usr/bin/python

import re

with open('./Reuter_Corpus/reut2-000.sgm') as f:
    data_lines = f.readlines()

dateRE = re.compile(r"^<DATE>\s*(?P<Date>.+?) (?P<Time>.+?)<\/DATE>$")
regexps = [
        re.compile(r"^<TITLE>\s*(?P<Title>.+?)<\/TITLE>"),
        re.compile(r"<DATELINE>\s*(?P<Location>.+?),")
        ]

cells = []
for data in data_lines:
    data = data.strip()
    date = dateRE.search(data)
    if date is not None:
        cells.append(date.groupdict())
        continue
    for expression in regexps:
        result = expression.search(data)
        if result is not None:
            cells[-1].update(result.groupdict())

for cell in cells:
    print "\n"
    try:
        print "%s: %s" % ("Date", cell["Date"])
        print "%s: %s" % ("Time", cell["Time"])
        print "%s: %s" % ("Title", cell["Title"])
        print "%s: %s" % ("Location", cell["Location"])
    except KeyError:
        pass
