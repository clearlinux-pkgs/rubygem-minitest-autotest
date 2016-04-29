#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-minitest-autotest
Version  : 1.0.2
Release  : 8
URL      : https://rubygems.org/downloads/minitest-autotest-1.0.2.gem
Source0  : https://rubygems.org/downloads/minitest-autotest-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-minitest-autotest-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
= minitest-autotest
home :: https://github.com/seattlerb/minitest-autotest
rdoc :: http://docs.seattlerb.org/minitest-autotest

%package bin
Summary: bin components for the rubygem-minitest-autotest package.
Group: Binaries

%description bin
bin components for the rubygem-minitest-autotest package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n minitest-autotest-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-minitest-autotest.gemspec

%build
gem build rubygem-minitest-autotest.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
minitest-autotest-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/minitest-autotest-1.0.1 && rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/minitest-autotest-1.0.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/History.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/bin/autotest
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/autoupdate.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/bundler.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/fixtures.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/isolate.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/migrate.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/once.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/preload.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/rcov.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/restart.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/autotest/timestamp.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/lib/minitest/autotest.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/test/test_minitest/test_autorun.rb
/usr/lib64/ruby/gems/2.3.0/gems/minitest-autotest-1.0.2/test/test_minitest/test_good.rb
/usr/lib64/ruby/gems/2.3.0/specifications/minitest-autotest-1.0.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/autotest
