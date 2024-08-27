Name:       experiment
Version:    1.0
Release:    1%{?dist}
Summary:    Experimental package

License:    Experimental
# Source0:    experiment-1.0.tar.gz

# BuildRequires:  sqlite-devel

%description
This is a test to build RPM/SRPM using GitHub Action.

%prep

# %setup -c

%build
echo "#!/bin/bash\n\necho EXECUTED" > $RPM_BUILD_DIR/executable

%install
install -d $RPM_BUILD_ROOT/opt/exp
install -m 755 $RPM_BUILD_DIR/executable $RPM_BUILD_ROOT/opt/exp/executable

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/exp/executable

%changelog


