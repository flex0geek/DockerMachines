FROM ubuntu:20.04
ENV LC_CTYPE C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update 
RUN apt-get install -yq ruby gcc make wget curl git vim gdb clang llvm lld llvm-dev bsdmainutils libstdc++-10-dev python3 python3-pip python3-dev automake flex bison build-essential libglib2.0-dev libpixman-1-dev python3-setuptools
RUN apt-get install -yq file binwalk flashrom golang-go 
RUN gem install one_gadget
RUN cd /root/ && wget https://www.sudo.ws/dist/sudo-1.8.31p2.tar.gz && tar -xvf sudo-1.8.31p2.tar.gz && cd sudo-1.8.31p2 && ./configure && make && make install
RUN cd /root/ && git clone https://github.com/AFLplusplus/AFLplusplus && cd AFLplusplus && make source-only && make install
RUN useradd -ms /bin/bash user
# RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
RUN cd /root/ && git clone https://github.com/projectdiscovery/nuclei-templates.git
RUN pip install ipython
RUN pip install pwntools
RUN sudo -H python3 -m pip install ROPgadget
RUN bash -c "$(wget https://gef.blah.cat/sh -O -)"
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;31m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$ "' >> /home/user/.bashrc
USER user
WORKDIR /home/user
