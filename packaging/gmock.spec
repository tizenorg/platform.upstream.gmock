Name:       gmock
Version:    1.7.0
Release:    1
Summary:    C++ mocking framework
Group:      Development/Testing
License:    BSD-2.0 and Apache-2.0
Vendor:     Google Inc.
URL:        https://code.google.com/p/googlemock/
Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}.manifest
BuildRequires: cmake

%description
Framework for writing and using C++ mock classes on a variety of platforms

%package devel
Summary:    Development headers and libs for gmock
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Conflicts:  gtest-devel

%description devel
Standard header files for use when developing gmock based apps

%prep
%setup -q
cp %{SOURCE1} .

%build
%cmake . -DPKG_VERSION=%{version}
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE LICENSE.apache-2.0
%{_libdir}/*.so.*
%manifest %{name}.manifest

%files devel
%{_includedir}/gmock
%{_includedir}/gtest
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so
%manifest %{name}.manifest
%{_libdir}/pkgconfig/*.pc
