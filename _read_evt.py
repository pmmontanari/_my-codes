# -*- coding: utf-8 -*-
"""
Code to parse an evt file from Lunitek into Pandas and, if wanted, into an HDF.

Purpose: (What this script does.)
     Small explanation pharagraph.

Context: (Why it does what it does)
    Small explanation pharagraph.

Usage: (How to use it)
    General instructions. Limit to one phrase or two. 

Created on Thu Dec 25 15:34:00 2025

@author: pmmontanari (pmmontanari@proton.me)
"""

# --- User packages ---
import pandas as pd

# --- GLOBALS ---
EVT_FILE = "/path/to/file.evt"

def _read_evt(EVT_FILE) -> pd.DataFrame:
    with open(EVT_FILE,'r') as f:
        lines = [line.rstrip().replace('CH', '').split(' ') for line in f.readlines() if not (line.startswith('#'))]
    
    NAMES = ["channel", "tin_s", "tout_s", "amplitude_mV", "noscillations", "energy"]
    df = pd.DataFrame(lines, names=NAMES)
    return df

def main():
    _read_evt(EVT_FILE)

if __name__ == "__main__":
    __name__()