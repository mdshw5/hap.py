#!/usr/bin/env python

# Compare two summary csv files

import sys

def csvread(filename):
    f = open(filename)
    
    header = None
    rows = []
    for l in f:
        l = l.replace("\n", "")
        if not header:
            header = l.split(",")
        else:
            rows.append(l.split(","))
    
    data = {}
    for r in rows:
        label = r[0]
        for i in xrange(1, len(r)):
            if header[i] not in data:
                data[header[i]] = {}
            data[header[i]][label] = float(r[i])
    f.close()
    return data


def main():
    data1 = csvread(sys.argv[1])
    data2 = csvread(sys.argv[2])

    for metric in [  # "TRUTH.TOTAL", "QUERY.TOTAL", #  -- these will vary by +/- 2
                   "METRIC.Recall.HC", "METRIC.Precision.HC"]:
        for field in ["Locations.SNP", "Locations.SNP.het", "Locations.INDEL", "Locations.INDEL.het"]:
            print metric + " / " + field
            print data1[metric][field]
            print data2[metric][field]
            if ( "%.3g" % data1[metric][field] ) != ( "%.3g" % data2[metric][field] ):
                raise "Failed: Results should be the same"

if __name__ == '__main__':
    main()