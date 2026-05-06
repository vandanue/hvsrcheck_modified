# File name     : geopsy_hvsrcheck.py
# Info          : Program to check reliable and clear peak of H/V curve from Geopsy file (.hv)
# Update        : 26th March 2020
# Written by    : Aulia Khalqillah,S.Si.,M.Si
# Email         : auliakhalqillah.mail@gmail.com
# Source        : GUIDELINES FOR THE IMPLEMENTATION OF THE H/V SPECTRAL RATIO TECHNIQUE ON AMBIENT VIBRATIONS
#                 MEASUREMENTS, PROCESSING AND INTERPRETATION, SESAME European research project
#                 WP12 – Deliverable D23.12 [ftp://ftp.geo.uib.no/pub/seismo/SOFTWARE/SESAME/USER-GUIDELINES/SESAME-HV-User-Guidelines.pdf]
#
# USAGE         : Using hvsrcheck.py as modules file
#                 example: hvsrcheck(input)
#                 input is dictionary type.
#                 "You just need to add the .hv and .log files in filename and logname variable that you have"
# TESTED        : Python >= 3.7
# ------------------------------------------------------------------------------------------------------------------------------------------
# EDITED        : - 24 Nov 2024, Michael Partogi. Solving hvcheck module for returning clear peak criteria
#                 - 12 Jan 2025, Annora Vandanu Erlangga. Add script to read .log dan .hv files in batch processing for SESAME criteria
# ------------------------------------------------------------------------------------------------------------------------------------------

import os
from hvcheck.io import read_hv_file, read_log_file
from hvcheck.hvcheck import hvsrcheck
from hvcheck.report import print_report, all_output, save_csv

# Change the folder to your .hv and .log files
os.chdir(r"/media/vandanu/HDD/00_College/Asdos/Kulon_Progo/passive_seismic/hvsr")
csv_files = "kulon_progo.csv"

def process_hvsr(prefix):

    filename = f"{prefix}.hv"
    logname = f"{prefix}.log"

    if not os.path.exists(filename):

        print(f"{filename} not found")
        return

    if not os.path.exists(logname):

        print(f"{logname} not found")
        return

    data = read_hv_file(filename)

    window, winlength = read_log_file(logname)

    data["window"] = window
    data["winlength"] = winlength

    results = hvsrcheck(data)

    print_report(data, results)
    all_output(data, results)
    save_csv(data, results, csv_files)


def main():

    if os.path.exists(csv_files):
        os.remove(csv_files)

    files = [
        f for f in os.listdir()
        if f.endswith(".hv")
    ]

    prefixes = sorted(
        {f[:-3] for f in files},
        key=lambda x: int(x[1:])
    )

    for prefix in prefixes:

        process_hvsr(prefix)


if __name__ == "__main__":
    main()