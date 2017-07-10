from math import pi
import pyastro
from datetime import datetime, timedelta

# def MA2TA (MA,Ecc):
	
#  	EA = MA = radians(MA)

#  	for cntr in range(0,6):
#  		a = EA-(Ecc * sin(EA)) - MA
#  		b = 1-(Ecc * cos(EA))
#  		EA = EA - (a/b)
#    	a = cos(EA) - Ecc
#    	b = 1 - (Ecc * cos(EA))
#    	print a/b
#    	TA = acos(a / b)

#  	if TA > pi:
#  		TA = pi + (pi - TA)
# 	return degrees(TA)

def MM2SMA(MM):
	MU = 398600.4418
	# ! Convert Mean motion from revs/day to rad/s  
	MM = MM*((2*pi)/86400)
	return (MU/(MM**2))**(1.0/3.0)


TLE = [
	"1 42716U 98067LX  17190.68440267  .00012619  00000-0  18341-3 0  9994",
	"2 42716  51.6404 285.6070 0005210  46.3490 313.7933 15.56166765  8144"
	]

(line,SAT,Desgnator,TLEEpoch,MM1,MM2,BSTAR,EType,Elementnum) = TLE[0].split()
(line,SATNum,Inc,RAAN,Ecc,AoP,MA,MM,RevNum) = TLE[1].split()

EpochY = int(TLEEpoch[:2])
if EpochY > 56:
	EpochY+=1900
else:
	EpochY+=2000
EpochD = float(TLEEpoch[2:])
MA = float(MA)
MM = float(MM)
Ecc = float('0.'+Ecc)
# EpochY, EpochD, Inc, RAAN, ECC, AoP, MA, MM, TA, SMA, MJD, TAfromMA, SMAfromMM, MJDfromEpoch

print "Year",EpochY,"\nday",EpochD,"\nInc",Inc,"\nRAAN",RAAN,"\nEcc",Ecc,"\nAoP",AoP,"\n-MA",MA,"\n-MM",MM

# print "TA:", MA2TA(MA,Ecc)
print "TA:", pyastro.kepler(MA,Ecc)
print "SMA:", MM2SMA(MM)
Epoch = (datetime(EpochY-1,12,31) + timedelta(EpochD)).strftime("%d %b %Y %H:%M:%S.%f")[:-3]
print "Epoch:", Epoch

print("\nCreate Spacecraft TLE_SC;\n" +
		"GMAT TLE_SC.DateFormat = UTCGregorian;\n" +
		"GMAT TLE_SC.Epoch = '"+Epoch+"';\n" +
		"GMAT TLE_SC.CoordinateSystem = EarthMJ2000Eq;\n" +
		"GMAT TLE_SC.DisplayStateType = Keplerian;\n" +
		"GMAT TLE_SC.SMA = 6821;\n" +
		"GMAT TLE_SC.ECC = 0.000140300000001036;\n" +
		"GMAT TLE_SC.INC = 98.7;\n" +
		"GMAT TLE_SC.RAAN = " + str(RAAN) + ";\n" +
		"GMAT TLE_SC.AOP = " + str(AoP) + ";\n" +
		"GMAT TLE_SC.TA = 259.0715000000072;\n")