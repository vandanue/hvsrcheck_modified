# HVSR CHECK FOR RELIABLE AND CLEAR PEAK OF H/V CURVE
This is a program to check reliable and clear peak of H/V curve from Geopsy file (.hv) called `hvsrcheck`.<br>
The program has been written based on information from project SESAME, [(2004)](https://sesame.geopsy.org/Delivrables/Del-D23-HV_User_Guidelines.pdf)

# REQUIRED
1. Numpy
2. Pandas
3. Python 3 (Recommended >=3.7)

# INSTALL
1. Install the `hvsrcheck`

Type the following command to install the modules of `hvsrcheck`:
```
pip install .
```

2. Install the requirement library

```
pip install -r requirement.txt
```

change `pip` to `pip3` if you are using Linux

# USAGE
Go to test folder and run the `geopsy_hvsrcheck.py` by following command:
```
python geopsy_hvsrcheck.py
```

change `python` to `python3` if you are using Linux

if the modules has been successfully installed, the information of reliable and clear peak will show up, like this:
```
-----------------------------------------------------------------------
File Name		: S51.hv
-----------------------------------------------------------------------

CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 5 out of 6
H/V IS CLEAR PEAK



-----------------------------------------------------------------------
File Name		: S50.hv
-----------------------------------------------------------------------

CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 5 out of 6
H/V IS CLEAR PEAK



-----------------------------------------------------------------------
File Name		: S30.hv
-----------------------------------------------------------------------

CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 2 out of 6
H/V IS NOT CLEAR PEAK

```

To run with your Geopsy files, you just need change the file name and log name in `geopsy_hvsrcheck.py` file.

# NOTE
The file of `geopsy_hvsrcheck.py` will read if the line of header of Geopsy file (.hv) has 6 lines header, for an example:
```
0 # GEOPSY output version 1.1
1 # Number of windows = 58
2 # f0 from average	7.59876
3 # Number of windows for f0 = 58
4 # f0 from windows	7.25987	6.744	7.77574
5 # Peak amplitude	1.0481
6 # Frequency	Average	Min	Max
7 0.1	0.0222796	0.0109096	0.0454994 <<< start the first data at 7th line
```
so, if you want to extract the data based on this example, you have to put the `index` equal to 7 at 43th line of `geopsy_hvsrcheck.py`, because the first data of H/V at 7th line. Remember, in Python the index is started from 0!
If you have the line of header of Geopsy file (.hv) more than 6 line, you just need readjust the `index` number where the index first data is.
# CONTACT
This code has been written by Aulia Khalqillah,S.Si.,M.Si (2020)<br>
Email: auliakhalqillah.mail@gmail.com 
# EDITED        : 
- 24 Nov 2024, Michael Partogi. Solving hvcheck module for returning clear peak criteria.
- 12 Jan 2025, Annora Vandanu Erlangga. Add script to read .log dan .hv files in batch processing for SESAME criteria.

Email: annora.vandanu @ui.ac.id
