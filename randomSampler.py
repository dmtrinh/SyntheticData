#!/usr/bin/python

"""
randomSampler.py: A quick and dirty utility to randomly sample a dataset

Author:  dmtrinh, 2021
"""

import pandas as pd
import random
import sys
import time

if len(sys.argv) < 4:
    print("Syntax:\n  randomSampler inputFile sampleSize outputFile")

else:
    startTime = time.time()

    inputFile = sys.argv[1]
    sampleSize = int(sys.argv[2])
    outputFile = sys.argv[3]

    print(f"  ==> Sampling [{sampleSize}] rows from [{inputFile}] ...")

    # count number of records in file excluding the header
    n = sum(1 for line in open(inputFile, "r", encoding='utf-8')) - 1

    # build sample list; the 0-indexed header will not be included in the skip list
    skip = sorted( random.sample( range(1,n+1), n-sampleSize ) )
    df = pd.read_csv(inputFile, skiprows=skip, low_memory=False)

    # dump dataframe out to csv file
    print(f"  <== writing out to [{outputFile}]")
    df.to_csv(outputFile, index=False)

    endTime = time.time()
    print(f"Total runtime: {endTime - startTime}")

