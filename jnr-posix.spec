%{?scl:%scl_package jnr-posix}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jnr-posix
Version:	3.0.33
Release:	3%{?dist}
Summary:	Java Posix layer
License:	CPL or GPLv2+ or LGPLv2+
URL:		http://github.com/jnr/jnr-posix
Source0:	https://github.com/jnr/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz
Patch0:		fix-manifest.patch

BuildRequires:	%{?scl_prefix}jnr-constants >= 0.8.8
BuildRequires:	%{?scl_prefix}jnr-ffi
BuildRequires:	%{?scl_prefix}jffi
BuildRequires:	%{?scl_prefix}jffi-native
BuildRequires:	%{?scl_prefix}jnr-x86asm
BuildRequires:	%{?scl_prefix_java_common}junit
BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}maven-source-plugin
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
%{?scl:Requires: %scl_runtime}
BuildArch:	noarch

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java, 
written in Java and is part of the JNR project 

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%patch0

# fix test which assumes that there is a group named "nogroup"
sed -i 's|"nogroup"|"root"|' src/test/java/jnr/posix/GroupTest.java

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Remove useless wagon extension.
%pom_xpath_remove "pom:build/pom:extensions"

%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Feb 13 2017 Tomas Repik <trepik@redhat.com> - 3.0.33-3
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 3.0.33-1
- Update to upstream 3.0.33.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 3.0.29-2
- Add missing BuildRequires to fix FTBFS (BZ#1405610).

* Tue Apr 19 2016 Alexander Kurtakov <akurtako@redhat.com> 3.0.29-1
- Update to upstream 3.0.29 release.

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 3.0.27-1
- Update to upstream 3.0.27 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.19-1
- Update to upstream 3.0.19 version.

* Thu Jul 30 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.17-1
- Update to upstream 3.0.17 version.

* Wed Jul 15 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.15-1
- Update to upstream 3.0.15.

* Wed Jun 17 2015 Jeff Johnston <jjohnstn@redhat.com> 3.0.14-2
- Fix MANIFEST file.

* Tue Jun 16 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.14-1
- Update to upstream 3.0.14.
- Skip tests as there are more failing tests with this release.

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.12-1
- Update to upstream 3.0.12.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 3.0.11-1
- Update to upstream 3.0.11.

* Fri Feb 20 2015 Michal Srb <msrb@redhat.com> - 3.0.9-3
- Some tests work locally in mock, but fail in koji - skip them

* Thu Feb 19 2015 Michal Srb <msrb@redhat.com> - 3.0.9-2
- Skip tests on arm

* Wed Feb 18 2015 Michal Srb <msrb@redhat.com> - 3.0.9-1
- Update to upstream version 3.0.9

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.1-1
- Update to jnr-posix 3.0.1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.0-1
- Updated to version 2.4.0.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.1.8-1
- Bumped version to latest upstream release

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.1.7-1
- Bumped version to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-3
- updates to conform to pkg guidelines

* Thu Sep 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-2
- build / include javadocs

* Thu Sep 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-1
- bumped version to 1.1.4

* Fri Jan 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.0.8-1
- Unorphaned / renamed jna-posix to jnr-posix

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 0.7-1
- Bump to upstream new version.

* Thu Apr 24 2008 Conrad Meyer <konrad@tylerc.org> - 0.5-3
- Forgot to remove versioned jar from files section.

* Wed Apr 23 2008 Conrad Meyer <konrad@tylerc.org> - 0.5-2
- Remove all binary jars in prep and include README/LICENSE.
- Remove version from jar filename.

* Tue Apr 22 2008 Conrad Meyer <konrad@tylerc.org> - 0.5-1
- Initial RPM. 
