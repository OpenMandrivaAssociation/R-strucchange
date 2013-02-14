%bcond_with bootstrap
%global packname  strucchange
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4_7
Release:          1
Summary:          Testing, Monitoring, and Dating Structural Changes
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-7.tar.gz
Requires:         R-graphics R-stats R-zoo R-sandwich R-graphics R-stats 
Requires:         R-lmtest R-car R-e1071 R-tseries R-foreach 
%if %{without bootstrap}
Requires:         R-dynlm
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-graphics R-stats R-zoo R-sandwich R-graphics R-stats
BuildRequires:    R-lmtest R-car R-e1071 R-tseries R-foreach
%if %{without bootstrap}
BuildRequires:    R-dynlm
%endif

%description
Testing, monitoring and dating structural changes in (linear) regression
models. strucchange features tests/methods from the generalized
fluctuation test framework as well as from the F test (Chow test)
framework. This includes methods to fit, plot and test fluctuation
processes (e.g., CUSUM, MOSUM, recursive/moving estimates) and F
statistics, respectively. It is possible to monitor incoming data online
using fluctuation processes. Finally, the breakpoints in regression models
with structural changes can be estimated together with confidence
intervals. Emphasis is always given to methods for visualizing the data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
