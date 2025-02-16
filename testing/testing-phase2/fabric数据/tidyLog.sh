#!/bin/bash

# direction
dir=$1

# all childDir in direction
for childDir in $(ls $dir); do
    # scan all file with "Tape.log"
    for file in $(find $dir/$childDir -name "*Tape.log"); do
        # line contains "level=debug" but not contains "CreateChaincodeProposal" or "CommitAtPeers:"
        # then remove this line
        sed -n '/level=info/p;/level=debug/ { /CreateChaincodeProposal/p; /CommitAtPeers:/p; }' $file > $file.tidy
        rm $file
    done
done
