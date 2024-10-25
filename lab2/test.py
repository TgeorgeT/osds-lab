from pwn import *

context.arch = "amd64"
print(
    len(
        asm(
            """
    pop rdi
    xor rsi, rsi
    xor rdx, rdx
    xor rax, rax
    add rax, 59
    syscall
    """
        )
    )
)
