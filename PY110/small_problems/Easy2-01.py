# Write a function that takes a floating point number 
# representing an angle between 0 and 360 degrees and 
# returns a string representing that angle in degrees, 
# minutes, and seconds. 
# You should use a degree symbol (°) to represent degrees,
# a single quote (') to represent minutes, and a double 
# quote (") to represent seconds. 
# There are 60 minutes in a degree, and 60 seconds in a minute.

# Examples 

# 30 --> "30°00'00"
# 76.73 --> "76°43'48"
# 254.6 --> "254°35'59"" or dms(254.6) == "254°36'00"
# 93.034773 --> "93°02'05"
# 0 --> "0°00'00"

# This is a very confusing question
# Minutes:Seconds are angle units, not time
# 76.73 is like saying 76 degrees (out of 360) and then
# 73% of the way to the 77th degree, and represent that 73%
# as minutes:seconds for some historical reason

# Data
# Input is floating point number
# Output will be an f-string
# Need three different calculated values
# Degree will be float converted via floor division to integer
# minutes will be int 
# Seconds will be int

# Algorithm
# Convert original input float to int_num using floor division (degrees_int)
# Obtain fraction by subtracting degrees_int from original float
# Let's use an example: 76.73 -> 76 43 48
# 76 floor division by 1, convert to int, gives 76 (call this degrees_int)
# (76.73 - 76) * 60 gives 43.8 minutes
# 43.8 floor division by 1 gives 43 (call this minutes_int)
# 43.8 - 43 gives 0.8 minutes
# 0.8 * 60 gives seconds (call this seconds_int)
# Assemble everything with an f-string and return

DEGREE = "\u00B0"
def dms(deg_float):
    degrees_int = int(deg_float)
    minutes_float = (deg_float - degrees_int) * 60
    minutes_int = int(minutes_float)
    seconds_float = minutes_float - minutes_int
    seconds_int = int((seconds_float) * 60)
    return f"{degrees_int}{DEGREE}{minutes_int:02d}'{seconds_int:02d}\""

# All of these examples should print True
print(dms(30)) # == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")



