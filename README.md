# TLE2Keplerian

Converts TLE to Keplerian coordinates.  
Generates GMAT Spacecraft code

**This project has moved to [GitLab](https://gitlab.com/drid/TLE2Keplerian)**

## Usage
```bash
python TLE2Keplerian.py
```
and enter TLE with title at the prompt  
or
```bash
echo "UPSAT                   
1 42716U 98067LX  17191.45501040  .00015767  00000-0  22714-3 0  9990
2 42716  51.6403 281.7542 0005278  48.0757 312.0684 15.56192276  8267"| python TLE2Keplerian.py
```
or
```bash
cat singleTLE.txt | python TLE2Keplerian.py
```
**Output**
```bash
Year: 2017 
Day: 191.4550104 
Inc: 51.6403 
RAAN: 281.7542 
Ecc: 0.0005278
AoP: 48.0757 
MA: 312.0684 
MM: 15.56192276 
TA: 312.067942103 
SMA: 6776.82604314
Epoch: 10 Jul 2017 10:55:12.898

Create Spacecraft UPSAT;
GMAT UPSAT.Id = '42716';
GMAT UPSAT.DateFormat = UTCGregorian;
GMAT UPSAT.Epoch = '10 Jul 2017 10:55:12.898';
GMAT UPSAT.CoordinateSystem = EarthMJ2000Eq;
GMAT UPSAT.DisplayStateType = Keplerian;
GMAT UPSAT.SMA = 6776.82604314;
GMAT UPSAT.ECC = 0.0005278;
GMAT UPSAT.INC = 51.6403;
GMAT UPSAT.RAAN = 281.7542;
GMAT UPSAT.AOP = 48.0757;
GMAT UPSAT.TA = 312.067942103;
```
