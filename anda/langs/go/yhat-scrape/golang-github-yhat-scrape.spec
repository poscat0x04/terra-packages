# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/yhat/scrape
%global goipath         github.com/yhat/scrape
%global commit          24b7890b0945459dbf91743e4d2ac5d75a51fee2

%gometa -f


%global common_description %{expand:
A simple, higher level interface for Go web scraping.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           golang-%{goname}
Version:        0
Release:        %autorelease -p
Summary:        A simple, higher level interface for Go web scraping

License:        BSD-2-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog