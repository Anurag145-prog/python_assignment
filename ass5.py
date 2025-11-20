value = 0xCAFE  
last = value & 0xF                 
count = ((last & 1) != 0) + ((last & 2) != 0) + ((last & 4) != 0) + ((last & 8) != 0)
atLeast3 = (count >= 3)
reversed_val = ((value & 0x00FF) << 8) | ((value & 0xFF00) >> 8)
rotated_val = ((value << 4) | (value >> 12)) & 0xFFFF  

print("Original value:      ", hex(value))
print("At least 3 LSB bits on:", atLeast3)
print("Reversed bytes:      ", hex(reversed_val))
print("4-bit rotated value: ", hex(rotated_val))
