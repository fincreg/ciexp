FROM rockylinux:8

RUN dnf -y group install "Development Tools"
RUN dnf -y install epel-release
RUN dnf -y install rpmdevtools rpmlint

RUN mkdir -p /root/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

VOLUME /root/rpmbuild
