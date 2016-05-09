#!/usr/bin/python3

def slicer(seq):
    return seq[:1] + seq[-1:] if len(seq) > 1 else seq