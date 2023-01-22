%global forgeurl https://github.com/odra/tcp_pubsub
%global branch f36

%forgemeta -i

Name:    tcp_pubsub
Version: 1.0.3
Release: 1%{?dist}
Summary: A minimal publish-subscribe library that transports data via TCP
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: g++
BuildRequires: cmake
BuildRequires: asio-devel
BuildRequires: recycle-devel


%description
tcp_pubsub is a minimal publish-subscribe library that transports data via TCP. The project is CMake based. The dependencies are integrated as git submodules. In your own Project you can either use those submodules as well, or provide the dependencies in your own manner.

tcp_pubsub does not define a message format but only transports binary blobs. It does however define a protocol around that, which is kept as lightweight as possible.

%package devel
Summary: Eclipse tcp_pubsub header and cmake development files

%description devel
Eclipse tcp_pubsub header and cmake development files

%package libs
Summary: Eclipse tcp_pubsub library files

%description libs
Eclipse tcp_pubsub library files

%prep
%forgesetup

%build
%cmake \
    -Dasio_INCLUDE_DIR=%{_includedir}/asio \
    -Drecycle_INCLUDE_DIR=%{_includedir}/recycle \
    -DBUILD_CSHARP_BINDING=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files devel

%{_includedir}/tcp_pubsub/callback_data.h
%{_includedir}/tcp_pubsub/executor.h
%{_includedir}/tcp_pubsub/publisher.h
%{_includedir}/tcp_pubsub/subscriber.h
%{_includedir}/tcp_pubsub/subscriber_session.h
%{_includedir}/tcp_pubsub/tcp_pubsub_export.h
%{_includedir}/tcp_pubsub/tcp_pubsub_logger.h
%{_includedir}/tcp_pubsub/tcp_pubsub_version.h
%{_prefix}/lib/cmake/tcp_pubsub/tcp_pubsubConfig.cmake
%{_prefix}/lib/cmake/tcp_pubsub/tcp_pubsubTargets.cmake
%{_prefix}/lib/cmake/tcp_pubsub/tcp_pubsubTargets-release.cmake

%files libs
%{_prefix}/lib/libtcp_pubsub.so.1.0.3
%{_prefix}/lib/libtcp_pubsub.so.1
%{_prefix}/lib/libtcp_pubsub.so

%files
%license LICENSE
%doc README.md

%changelog
* Sat Jan 21 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.0.3-1
- First version being packaged
