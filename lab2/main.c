#include <unistd.h>

int main()
{
    const char *bash = "/bin/bash";
    execve(bash, NULL, NULL);
}