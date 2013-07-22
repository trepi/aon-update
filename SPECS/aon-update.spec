# 
#                                            _       _       
#                                           | |     | |      
#    __ _  ___  _ __         _   _ _ __   __| | __ _| |_ ___ 
#   / _` |/ _ \| '_ \   _   | | | | '_ \ / _` |/ _` | __/ _ \
#  | (_| | (_) | | | | |_|  | |_| | |_) | (_| | (_| | ||  __/
#   \__,_|\___/|_| |_|       \__,_| .__/ \__,_|\__,_|\__\___|
#                                 | |                        
#                                 |_|                        
# 
# 

%define port     			7654
%define logfilename     	aon-update.log

%define aon-update_user     aon-update
%define aon-update_group    %{aon_user}

%define aon-update_home     %{_libdir}/aon-update

%define aon-updatectl		%{_bindir}/aon-update

%define yumconfdir			%{_sysconfdir}/yum


Name:           aon-update
Version:        %{version}
Release:        %{release}%{?dist}%{?repo}
Epoch:          0
Summary:        The skeleton package which defines a simple aon iNetServer system..
License:       	rtrepiana software license.
URL:            http://github.com/rtrepiana/aon-update
Source0: 	*
Group:          System Environment/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires: 	python-devel

Requires:		yum-updatesd
Requires:		python-cheetah
Requires:       python-twisted-web

%description
.


%prep

cp -r %{SOURCE0} .

%build

make all

pushd src
	sed -i "s|@NAME|%{name}-%{version}|g" aon-update.init
	sed -i "s|@SERVICE|%{name}|g" aon-update.init
	sed	-i "s|@EXEC|%{_sbindir}/aon-update|g" aon-update.init

	sed -i "s|@TAP|web.tap|g" aon-update
	sed -i "s|@CFG|%{_sysconfdir}/aon-update.cfg|g" aon-update
	sed -i "s|@RUNDIR|%{_localstatedir}/%{name}|g" aon-update

	sed -i "s|@PORT|%{port}|g" aon-update.cfg
	sed -i "s|@LOGFILENAME|%{logfilename}|g" aon-update.cfg

popd	


%install
pushd src
	python ./setup.py install --prefix="${RPM_BUILD_ROOT}/%{_prefix}"

	install -D -m 755 aon-update ${RPM_BUILD_ROOT}%{_sbindir}/aon-update
	install -D -m 755 aon-update.init $RPM_BUILD_ROOT%{_initrddir}/aon-update
	install -D -m 644 aon-update.cfg  $RPM_BUILD_ROOT%{_sysconfdir}/aon-update.cfg
	
popd

install -dm 755 ${RPM_BUILD_ROOT}%{_localstatedir}/%{name}/www
pushd www
	for dir in $(find . -type d); do 
		install -dm 755 ${RPM_BUILD_ROOT}%{_localstatedir}/%{name}/www/$dir
	done
	for file in $(find . -type f); do 
		install -m 644 $file ${RPM_BUILD_ROOT}%{_localstatedir}/%{name}/www/$file
	done
popd

install -dm 700 ${RPM_BUILD_ROOT}%{_localstatedir}/log/%{name}


%post

# make tap file
pushd %{_localstatedir}/%{name} > /dev/null
	mktap web --port=%{port} --logfile=%{_localstatedir}/log/%{name}/%{logfilename} --path=%{_localstatedir}/%{name}/www 
popd > /dev/null
# Register the httpd service
/sbin/chkconfig --add %{name}

/sbin/service %{name} condrestart &>/dev/null

# Change yum-updatesd configuration for download new packages
if [ -f "%{yumconfdir}/yum-updatesd.conf" ] && \
	egrep '^.*do_download.*=.*no.*$' %{yumconfdir}/yum-updatesd.conf > /dev/null; then 
	sed -i.%{name}.save \
	-e 's/^.*\(do_download.*=\).*$/# changed by %{name}\
\1 yes/'\
	%{yumconfdir}/yum-updatesd.conf
	
	if /sbin/service yum-updatesd status > /dev/null; then
		/sbin/service yum-updatesd stop
	fi

	/sbin/service yum-updatesd start
fi


%preun
if [ $1 = 0 ]; then
	/sbin/service %{name} stop > /dev/null 2>&1
	/sbin/chkconfig --del %{name}
fi


%files
%defattr(-, root, root, 0755)

%{_sbindir}/*
%{_initrddir}/*
%{_localstatedir}/%{name}/*
/usr/lib/python*/site-packages/*

%config(noreplace) %{_sysconfdir}/*

%doc README COPYING BUGS

%attr(0700,root,root) %dir %{_localstatedir}/log/%{name}



%changelog
* Thu May 19  2009 Raúl Trepiana <rtrepiana@gmail.com> - 
0:0.0.1-17%{?dist}%{?repo}
- Make pages not cacheable and force a modification check at each visit (expires=0)
* Thu Apr 03  2009 Raúl Trepiana <rtrepiana@gmail.com> - 
0:0.0.1-1%{?dist}%{?repo}
- initial release


