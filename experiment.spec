Name:       experiment
Version:    %{version}
Release:    %{release}%{?dist}
Summary:    Experimental package

License:    Experimental
# Source0:    experiment-1.0.tar.gz

BuildRequires:  sqlite-devel

%description
This is a test to build RPM/SRPM using GitHub Action.

%prep

# %setup -c

%build
make

%install
install -d $RPM_BUILD_ROOT/opt/exp
install -m 755 $RPM_BUILD_DIR/hello $RPM_BUILD_ROOT/opt/exp/hello

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/exp/hello

%changelog


