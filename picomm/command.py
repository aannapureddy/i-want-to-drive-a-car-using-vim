# Eventual stuff
# Lock: c
# Engine: c
# Throttle: I
# Brake: c
# Parking brake: c
# Drive, neutral, and reverse: H
# Music: I
# Steering angle: i 
# Cruise: c
# Horn: c
# Car alarm: c
# Headlights: c

# cclccHlicccc

from struct import pack, unpack
def encode(throttle, steering):
    return pack('ii', throttle, steering)

def decode(packed):
    return unpack('ii', packed)

cmd = encode(120, 120)
print(cmd)
print(decode(cmd))