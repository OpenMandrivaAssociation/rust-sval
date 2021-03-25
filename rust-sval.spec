# check disabled to avoid circular dependencies (quickcheck)
%bcond_with check
%global debug_package %{nil}

%global crate sval

Name:           rust-%{crate}
Version:        1.0.0~alpha.5
Release:        1%{?dist}
Summary:        No-std, object-safe serialization framework

# Upstream license specification: Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
%if %{with check}
BuildRequires:  (crate(quickcheck/default) >= 0.9.0 with crate(quickcheck/default) < 0.10.0)
BuildRequires:  (crate(wasm-bindgen-test/default) >= 0.3.0 with crate(wasm-bindgen-test/default) < 0.4.0)
BuildRequires:  (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
%endif
%endif

%global _description %{expand:
No-std, object-safe serialization framework.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval) = 1.0.0~alpha.5
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/default) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/alloc) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arbitrary-depth-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/arbitrary-depth) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(smallvec) >= 1.0.0 with crate(smallvec) < 2.0.0)
Requires:       crate(sval) = 1.0.0~alpha.5
Requires:       crate(sval/alloc) = 1.0.0~alpha.5

%description -n %{name}+arbitrary-depth-devel %{_description}

This package contains library source intended for building other packages
which use "arbitrary-depth" feature of "%{crate}" crate.

%files       -n %{name}+arbitrary-depth-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/derive) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(sval_derive/default) >= 1.0.0~alpha.5 with crate(sval_derive/default) < 2.0.0)
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fmt-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/fmt) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+fmt-devel %{_description}

This package contains library source intended for building other packages
which use "fmt" feature of "%{crate}" crate.

%files       -n %{name}+fmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/serde) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5
Requires:       crate(sval/serde1) = 1.0.0~alpha.5

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/serde1) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5
Requires:       crate(sval/serde1_lib) = 1.0.0~alpha.5

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1_lib-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/serde1_lib) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(serde) >= 1.0.104 with crate(serde) < 2.0.0)
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+serde1_lib-devel %{_description}

This package contains library source intended for building other packages
which use "serde1_lib" feature of "%{crate}" crate.

%files       -n %{name}+serde1_lib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+smallvec-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/smallvec) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(smallvec) >= 1.0.0 with crate(smallvec) < 2.0.0)
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+smallvec-devel %{_description}

This package contains library source intended for building other packages
which use "smallvec" feature of "%{crate}" crate.

%files       -n %{name}+smallvec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/std) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5
Requires:       crate(sval/alloc) = 1.0.0~alpha.5

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval_derive-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/sval_derive) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(sval_derive/default) >= 1.0.0~alpha.5 with crate(sval_derive/default) < 2.0.0)
Requires:       crate(sval) = 1.0.0~alpha.5

%description -n %{name}+sval_derive-devel %{_description}

This package contains library source intended for building other packages
which use "sval_derive" feature of "%{crate}" crate.

%files       -n %{name}+sval_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval/test) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval) = 1.0.0~alpha.5
Requires:       crate(sval/std) = 1.0.0~alpha.5

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages
which use "test" feature of "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
