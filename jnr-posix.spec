%global git_commit 024c489
%global cluster wmeissner

Name:           jnr-posix
Version:        1.1.4
Release:        4%{?dist}
Summary:        Java Posix layer
Group:          Development/Libraries
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}/
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz
Patch0:         jnr_posix_fix_jar_dependencies.patch

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  jnr-constants
BuildRequires:  jaffl
BuildRequires:  jffi
BuildRequires:  objectweb-asm

Requires:       java
Requires:       jpackage-utils
Requires:       jnr-constants
Requires:       jaffl
Requires:       jffi
Requires:       objectweb-asm

BuildArch:      noarch

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java, 
written in Java and is part of the JNR project 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n wmeissner-%{name}-%{git_commit}
%patch0
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

mkdir build_lib
build-jar-repository -s -p build_lib jaffl jffi constantine objectweb-asm/asm \
                                     objectweb-asm/analysis objectweb-asm/commons \
                                     objectweb-asm/tree objectweb-asm/util objectweb-asm/xml


%build
ant jar
ant javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# pom
%add_to_maven_depmap org.jruby.ext.posix %{name} %{version} JPP %{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jnr-posix.pom

%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-3
- updates to conform to pkg guidelines

* Fri Sep 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-2
- build / include javadocs

* Fri Sep 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.4-1
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
