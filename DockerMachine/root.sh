docker run --rm -v "/Users/flex/:/macOS" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name linuxctf -i linuxctf
docker exec -u root -it linuxctf /bin/bash