FROM ubuntu:latest
RUN apt-get update && apt-get install -y openssh-server nginx
# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'root:redhat' | chpasswd
#password for user login
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
EXPOSE 22
# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]