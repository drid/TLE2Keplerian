from math import pi
import pyastro
from datetime import datetime, timedelta
from sys import stdin

def MM2SMA(MM):
	MU = 398600.4418
	# ! Convert Mean motion from revs/day to rad/s  
	MM = MM*((2*pi)/86400)
	return (MU/(MM**2))**(1.0/3.0)

def checksum(line):
    """Compute the TLE checksum."""
    return (sum((int(c) if c.isdigit() else c == '-') for c in line[0:-1]) % 10) == int(line[-1]) 

print "Enter TLE including object title:"

TLE=[]
TLE.append(stdin.readline().strip())
TLE.append(stdin.readline().strip())
TLE.append(stdin.readline().strip())

if TLE[1][:2] != '1 ' or checksum(TLE[1]) == False:
	print "Not a TLE"
	exit()
if TLE[2][:2] != '2 'or checksum(TLE[2]) == False:
	print "Not a TLE"
	exit()

SatName = TLE[0]
(line,SAT,Desgnator,TLEEpoch,MM1,MM2,BSTAR,EType,ElementNum) = TLE[1].split()
(line,SATNum,Inc,RAAN,Ecc,AoP,MA,MM) = TLE[2].split()[:8]
EpochY = int(TLEEpoch[:2])
if EpochY > 56:
	EpochY+=1900
else:
	EpochY+=2000
EpochD = float(TLEEpoch[2:])
MA = float(MA)
MM = float(MM)
Ecc = float('0.'+Ecc)
SMA = MM2SMA(MM)
TA = pyastro.kepler(MA,Ecc)

print "Year:",EpochY,"\nDay:",EpochD,"\nInc:",Inc,"\nRAAN:",RAAN,
"\nEcc:",Ecc,"\nAoP:",AoP,"\nMA:",MA,"\nMM:",MM, "TA:", TA, "SMA:", SMA
Epoch = (datetime(EpochY-1,12,31) + timedelta(EpochD)).strftime("%d %b %Y %H:%M:%S.%f")[:-3]
print "Epoch:", Epoch

print("\nCreate Spacecraft "+SatName+";\n" +
		"GMAT "+SatName+".Id = '"+SATNum+"';\n" +
		"GMAT "+SatName+".DateFormat = UTCGregorian;\n" +
		"GMAT "+SatName+".Epoch = '"+Epoch+"';\n" +
		"GMAT "+SatName+".CoordinateSystem = EarthMJ2000Eq;\n" +
		"GMAT "+SatName+".DisplayStateType = Keplerian;\n" +
		"GMAT "+SatName+".SMA = "+str(SMA)+";\n" +
		"GMAT "+SatName+".ECC = "+str(Ecc)+";\n" +
		"GMAT "+SatName+".INC = "+str(Inc)+";\n" +
		"GMAT "+SatName+".RAAN = " + str(RAAN) + ";\n" +
		"GMAT "+SatName+".AOP = " + str(AoP) + ";\n" +
		"GMAT "+SatName+".TA = "+str(TA)+";\n")