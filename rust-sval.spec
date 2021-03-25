%bcond_without check
%global debug_package %{nil}

%global crate sval

Name:           rust-%{crate}
Version:        0.5.2
Release:        1
Summary:        No-std, object-safe serialization framework

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/sval
Source:         %{crates_source}
# Avoid circular dependency by dropping quickcheck test
# (quickcheck needs log, log needs sval)
Patch0:		sval-0.5.2-no-quickcheck-dep.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
No-std, object-safe serialization framework.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arbitrary-depth-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-depth-devel %{_description}

This package contains library source intended for building other packages
which use "arbitrary-depth" feature of "%{crate}" crate.

%files       -n %{name}+arbitrary-depth-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fmt-devel %{_description}

This package contains library source intended for building other packages
which use "fmt" feature of "%{crate}" crate.

%files       -n %{name}+fmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_lib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_lib-devel %{_description}

This package contains library source intended for building other packages
which use "serde_lib" feature of "%{crate}" crate.

%files       -n %{name}+serde_lib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_no_std-devel %{_description}

This package contains library source intended for building other packages
which use "serde_no_std" feature of "%{crate}" crate.

%files       -n %{name}+serde_no_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_std-devel %{_description}

This package contains library source intended for building other packages
which use "serde_std" feature of "%{crate}" crate.

%files       -n %{name}+serde_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+smallvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smallvec-devel %{_description}

This package contains library source intended for building other packages
which use "smallvec" feature of "%{crate}" crate.

%files       -n %{name}+smallvec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sval_derive-devel %{_description}

This package contains library source intended for building other packages
which use "sval_derive" feature of "%{crate}" crate.

%files       -n %{name}+sval_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages
which use "test" feature of "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
