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
File Name		: S53.hv
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 2 out of 6
H/V IS NOT CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  11.29 > 0.3333333333333333
RELIABLE 2: CRITERIA FULFILLED 			  6773.40 > 200
RELIABLE 3: CRITERIA FULFILLED 			  0.93 < 2

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA NOT FULFILLED 		  A_H/V(f⁻) < 1.81
CLEAR PEAK 2: CRITERIA NOT FULFILLED 		  A_H/V(f⁺) < 1.81
CLEAR PEAK 3: CRITERIA FULFILLED 		  3.62 > 2
CLEAR PEAK 4: CRITERIA NOT FULFILLED 		  f_0 GREATER THAN 5%
CLEAR PEAK 5: CRITERIA NOT FULFILLED 		  1.32 > 0.56
CLEAR PEAK 6: CRITERIA FULFILLED 		  1.15 < 1.58
-----------------------------------------------------------------------



-----------------------------------------------------------------------
File Name		: S6.hv
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 4 out of 6
H/V IS NOT CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  21.85 > 0.4
RELIABLE 2: CRITERIA FULFILLED 			  10380.79 > 200
RELIABLE 3: CRITERIA FULFILLED 			  0.66 < 2

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA NOT FULFILLED 		  A_H/V(f⁻) < 1.94
CLEAR PEAK 2: CRITERIA FULFILLED 		  A_H/V(f⁺) < 1.94
CLEAR PEAK 3: CRITERIA FULFILLED 		  3.89 > 2
CLEAR PEAK 4: CRITERIA FULFILLED 		  f_0 ± 5%
CLEAR PEAK 5: CRITERIA NOT FULFILLED 		  1.82 > 1.09
CLEAR PEAK 6: CRITERIA FULFILLED 		  1.24 < 1.58
-----------------------------------------------------------------------



-----------------------------------------------------------------------
File Name		: S32.hv
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 5 out of 6
H/V IS CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  7.83 > 0.25
RELIABLE 2: CRITERIA FULFILLED 			  5638.19 > 200
RELIABLE 3: CRITERIA FULFILLED 			  0.62 < 2

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA FULFILLED 		  A_H/V(f⁻) < 1.65
CLEAR PEAK 2: CRITERIA FULFILLED 		  A_H/V(f⁺) < 1.65
CLEAR PEAK 3: CRITERIA FULFILLED 		  3.29 > 2
CLEAR PEAK 4: CRITERIA FULFILLED 		  f_0 ± 5%
CLEAR PEAK 5: CRITERIA NOT FULFILLED 		  0.43 > 0.39
CLEAR PEAK 6: CRITERIA FULFILLED 		  1.16 < 1.58
-----------------------------------------------------------------------
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

Email: annora.vandanu@ui.ac.id
