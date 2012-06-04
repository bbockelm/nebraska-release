Name:           nebraska-release
Version:        1.0 
Release:        1%{?dist}
Summary:        Nebraska yum repository configuration

Group:          System Environment/Base 
License:        GPL
URL:            https://github.com/bbockelm/nebraska-release

Source0:        nebraska.repo
Source1:        nebraska-testing.repo
Source2:		nebraska-el6.repo
Source3:		nebraska-testing-el6.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%if 0%{?el6}
Requires:      redhat-release >=  6
%else
Requires:      redhat-release >=  5
Requires:      python-hashlib
%endif

%description
%{summary}

%prep
%if 0%{?el6}
cp %{SOURCE2} nebraska.repo
cp %{SOURCE3} nebraska-testing.repo
%else
cp %{SOURCE0} nebraska.repo
cp %{SOURCE1} nebraska-testing.repo
%endif

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

install -p -m 0644 nebraska.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/nebraska.repo
install -p -m 0644 nebraska-testing.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/nebraska-testing.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/nebraska.repo
%config(noreplace) /etc/yum.repos.d/nebraska-testing.repo


%changelog
* Mon Jun 04 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 1.0-1
- Initial creation of the nebraska-release RPM.

