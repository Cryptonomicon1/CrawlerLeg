# Main Formula Given by...
# http://atcpublications.com/Sample_pages_from_FDG.pdf

# Calculate Crawler Leg Muscle and Shell Size

# Pm = Force of Muscles per cross sectional area
# Ft = total force of average strength of human = (weight + 20lb)/leg_count
# l = leg count
# SIGMA_h_max = maximum bending stress of bone
# Zh = human bone factor = 0.78*Rhb^3
# Rhb = radius of human bone = sqrt(Ahb/pi)
# Ahb = cross sectional area of human bone = 3.6*10^-4 N/m^2 = 3.6*10^2 N/mm^2
# L = will show up but will be eliminated

# SIGMA_c_max = max crawler bone stress = 18.9 N/mm^2
# Zc = crawler bone factor = 0.78(Ro^4 - Ri^4)/Ro
# Ro = Outer radius of crawler bone/leg
# Ri = inner radius of crawler leg = sqrt(Atm/pi)
# Atm = total cross sectional area of inner crawler leg
# Am = cross sectional area of spider muscle = 0.6*Atm
# Sig_ratio = Ratio of human bone strength to crab shell strength = SIGMA_h_max / SIGMA_c_max

# Mini proof #1
# Ri = sqrt(Atm/pi)
# Atm = Am/0.6
# Ri = sqrt( (Am/0.6) / pi)
# Ri = sqrt( Am/ (0.6pi) )													(eq. A)

# Mini proof #2
# Am = (Ft / Pm) / 2														(eq. B)

# Mini proof #3
# Ri = sqrt( ( (Ft/Pm)/2 ) / (0.6pi) )
# Ri = sqrt( Ft / (1.2*Pm*pi) )												(eq. C)

# SIGMA_h_max = Sig_ratio*SIGMA_c_max										(eq. 1)
# Fh*Lh/Zh = Sig_ratio*Fc*Lc/Zc												(eq. 2)

# Lh = Lc and Fh = Fc So...

# SIG_ratio*Zh = Zc															(eq. 3)

# Substitute Equations for Z

# SIG_ratio*0.78*Rhb^3 = 0.78*(Ro^4 - Ri^4)/Ro								(eq. 4)
# SIG_ratio*sqrt(Ahb/pi)^3 = ( Ro^4 - sqrt( Am / (0.6pi) )^4 ) / Ro			(eq. 5)
# SIG_ratio*(Ahb/pi)^(3/2) = ( Ro^4 - (Am/(0.6pi))^2 ) / Ro					(eq. 6)

# Substitute Equation B

# SIG_ratio*(Ahb/pi)^(3/2) = ( Ro^4 - ( Ft / ( 2*Pm / (0.6pi) ) )^2 ) / Ro	(eq. 7)
# SIG_ratio*(Ahb/pi)^(3/2) = ( Ro^4 - ( Ft / (2*Pm*0.6*pi) )^2 ) / Ro		(eq. 8)
# 0 = Ro^4 - Ro*SIG_ratio*(Ahb/pi)^(3/2) - ( Ft / (1.2*Pm*pi) )^2			(eq. 9)

from math import pi
from sympy import Eq, var, solve

# https://www.jiskha.com/search/index.cgi?query=The+femur+is+a+bone+in+the+leg+whose+minium+cross-sectional+area+is+about+3.60+10-4+m2.+A+compressional+force+in+excess+of+6.90+104+N+will+fracture+this+bone
Ahb = 3.6*10**2

# 80kg * 9.81 m/s^2 + 4legs * 20lb * 0.45359235 kg/lb
Ft = (80*9.81 + 4*20*0.45359235)/2

# https://link.springer.com/article/10.1007/BF00696087
# 6.3 kg/cm^2 * 9.81 m/s^2 / (100mm^2 / 1cm^2)
Pm = 6.3*9.81/100

# http://www.musculoskeletalcore.wustl.edu/mm/files/Understanding%203pt%20Bending%20outcomes.pdf
SIGMA_h_max = 173.7 # SIGMA = P*L/(0.78*Rh^3)

# http://maeresearch.ucsd.edu/mckittrick/pubs/2008_JMBBM_3_208_BioMatsReview.pdf
SIGMA_c_max = 18.9
SIG_ratio = SIGMA_h_max / SIGMA_c_max

Ri = ( Ft/(1.2*Pm*pi) )**(1/2)

var('R')
eq = Eq(R**4 - R*SIG_ratio*(Ahb/pi)**(3/2) - ( Ft / (1.2*Pm*pi) )**2, 0) # Solve Quartic Equation
Ro = solve(eq)

print(" ")
print("Ro=", Ro[1], "mm or", float(Ro[1])/25.4, "inches") # Result 2/4 of the Quartic Equation is typically the positive non-complex resulto

print(" ")
print("Ri=", Ri, "mm or", Ri/25.4, "inches")
print(" ")

# Pin Size

# pins = number of pins per leg
# legs = number of legs crawler walks on
# sf = safety factor
# w_mult = multiple of weight for joint force
# weight = weight
# shear_strength = strength of material

pins = 1.5
legs = 4
sf = 3
w_mult = 15*30
weight = 80*9.81
shear_strength = 20

Area = w_mult*weight*sf/(0.5*shear_strength*legs*pins)

Rpin = (Area/pi)**(1/2)

print("Rpin =", Rpin, "mm or", Rpin/25.4, "inches")
print(" ")
