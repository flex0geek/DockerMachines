docker run --rm -v "/Users/flex/:/pwd" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name linux -i linux
docker exec -u root -it linux /bin/bash
