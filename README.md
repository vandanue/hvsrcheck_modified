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
File Name		: SN30.hv
f0			: 1.24 Hz
A0			: 4.01
Kg			: 12.97
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 5 out of 6
H/V IS CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  f0 = 1.24 > 0.25
RELIABLE 2: CRITERIA FULFILLED 			  n_c = 397.32 > 200
RELIABLE 3: CRITERIA FULFILLED 			  σA(f) = 0.33 < 2.00 (f0 > 0.5 Hz)

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA FULFILLED 		 A_H/V(0.31 Hz) = 1.51 < A0/2 = 2.01
CLEAR PEAK 2: CRITERIA FULFILLED 		 A_H/V(1.77 Hz) = 1.95 < A0/2 = 2.01
CLEAR PEAK 3: CRITERIA FULFILLED 		  A_0 = 4.01 > 2
CLEAR PEAK 4: CRITERIA NOT FULFILLED 		  f_0 = 1.24 Hz outside [1.18, 1.30] Hz
CLEAR PEAK 5: CRITERIA FULFILLED 		  σf = 0.11 within ε(f0) = 0.12
CLEAR PEAK 6: CRITERIA FULFILLED 		  σ_A(f0) = 1.26 within θ(f0) = 1.78
-----------------------------------------------------------------------



-----------------------------------------------------------------------
File Name		: SN31.hv
f0			: 1.41 Hz
A0			: 4.58
Kg			: 14.82
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 6 out of 6
H/V IS CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  f0 = 1.41 > 0.25
RELIABLE 2: CRITERIA FULFILLED 			  n_c = 565.51 > 200
RELIABLE 3: CRITERIA FULFILLED 			  σA(f) = 0.40 < 2.00 (f0 > 0.5 Hz)

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA FULFILLED 		 A_H/V(0.36 Hz) = 1.00 < A0/2 = 2.29
CLEAR PEAK 2: CRITERIA FULFILLED 		 A_H/V(1.85 Hz) = 2.27 < A0/2 = 2.29
CLEAR PEAK 3: CRITERIA FULFILLED 		  A_0 = 4.58 > 2
CLEAR PEAK 4: CRITERIA FULFILLED 		  f_0 = 1.41 Hz inside [1.34, 1.48] Hz
CLEAR PEAK 5: CRITERIA FULFILLED 		  σf = 0.10 within ε(f0) = 0.14
CLEAR PEAK 6: CRITERIA FULFILLED 		  σ_A(f0) = 1.19 within θ(f0) = 1.78
-----------------------------------------------------------------------



-----------------------------------------------------------------------
File Name		: SN32.hv
f0			: 2.29 Hz
A0			: 2.43
Kg			: 2.57
-----------------------------------------------------------------------
CRITERIA FOR A RELIABLE H/V CURVE
RELIABLE 1: OK
RELIABLE 2: OK
RELIABLE 3: OK

CLEAR PEAK SUMMARY: 5 out of 6
H/V IS CLEAR PEAK

-----------------------------------------------------------------------
RELIABILITY OUTPUT
RELIABLE 1: CRITERIA FULFILLED 			  f0 = 2.29 > 0.25
RELIABLE 2: CRITERIA FULFILLED 			  n_c = 1282.19 > 200
RELIABLE 3: CRITERIA FULFILLED 			  σA(f) = 0.24 < 2.00 (f0 > 0.5 Hz)

CLEAR PEAK OUTPUT
CLEAR PEAK 1: CRITERIA FULFILLED 		 A_H/V(0.58 Hz) = 1.12 < A0/2 = 1.21
CLEAR PEAK 2: CRITERIA FULFILLED 		 A_H/V(4.67 Hz) = 1.21 < A0/2 = 1.21
CLEAR PEAK 3: CRITERIA FULFILLED 		  A_0 = 2.43 > 2
CLEAR PEAK 4: CRITERIA FULFILLED 		  f_0 = 2.29 Hz inside [2.18, 2.40] Hz
CLEAR PEAK 5: CRITERIA NOT FULFILLED 		  σf = 0.35 exceeds ε(f0) = 0.11
CLEAR PEAK 6: CRITERIA FULFILLED 		  σ_A(f0) = 1.17 within θ(f0) = 1.58
-----------------------------------------------------------------------

```
To run with your Geopsy files, you just need change the file name and log name in `geopsy_hvsrcheck.py` file.

# CONTACT
This code has been written by Aulia Khalqillah,S.Si.,M.Si (2020)<br>
Email: auliakhalqillah.mail@gmail.com 
# EDITED        : 
- 24 Nov 2024, Michael Partogi. Solving hvcheck module for returning clear peak criteria.
- 12 Jan 2025, Annora Vandanu Erlangga. Add script to read .log dan .hv files in batch processing for SESAME criteria.

Email: annora.vandanu@ui.ac.id
