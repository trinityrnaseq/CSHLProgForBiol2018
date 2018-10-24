#!/usr/bin/env python

import os, sys

usage = "\n\n\tusage: {} kmer_length filename.fastq num_top_kmers\n\n".format(sys.argv[0])

if len(sys.argv) < 4:
    sys.stderr.write(usage)
    sys.exit(1)


def main():

    # capture command-line arguments
    kmer_length = int(sys.argv[1])
    fastq_filename = sys.argv[2]
    num_top_kmers = int(sys.argv[3])

    # hash table for storing the (kmer, count) data
    kmer_dict = {}

    # parse sequences from fastq file
    fh = open(fastq_filename)
    counter = 0
    for line in fh:
        line = line.rstrip()
        counter += 1
        if counter % 4 == 2: #sequence line
            count_kmers(kmer_dict, kmer_length, line)

    # sort the kmers by count, descendingly
    # http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
    sorted_kmers = sorted(kmer_dict.keys(), key= lambda x: kmer_dict[x], reverse=True)
    
    # report output
    counter = 0
    for kmer in sorted_kmers:
        count = kmer_dict[kmer]
        print("{}\t{}".format(kmer, count))
        counter += 1
        if counter >= num_top_kmers:
            break

    sys.exit(0)


def count_kmers(kmer_dict, kmer_length, sequence):

    
    for i in range(0, len(sequence) - kmer_length +1):
        # extract the kmer as a substring
        kmer = sequence[i:(i+kmer_length)]
        
        if kmer in kmer_dict:
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 1

    return


if __name__ == '__main__':
    main()
    
