Name:           ros-kinetic-ompl
Version:        1.2.3
Release:        0%{?dist}
Summary:        ROS ompl package

Group:          Development/Libraries
License:        BSD
URL:            http://ompl.kavrakilab.org
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel

%description
OMPL is a free sampling-based motion planning library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 04 2018 Mark Moll <mmoll@rice.edu> - 1.2.3-0
- Autogenerated by Bloom

* Sat Nov 19 2016 Ioan Sucan <isucan@google.com> - 1.2.1-1
- Autogenerated by Bloom

* Sun Oct 02 2016 Ioan Sucan <isucan@google.com> - 1.2.1-0
- Autogenerated by Bloom

* Thu Jun 23 2016 Ioan Sucan <isucan@google.com> - 1.2.0-0
- Autogenerated by Bloom

* Wed Jun 15 2016 Ioan Sucan <isucan@google.com> - 1.1.3535-0
- Autogenerated by Bloom

