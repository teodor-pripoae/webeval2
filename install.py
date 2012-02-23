import os
import platform
import tarfile
import urllib
import shutil

class InstalationFail(Exception):
    pass


class PackageInstaller():
    dist_installers = {
            "Fedora": "yum -y install",
            "Ubuntu": "apt-get install -y ",
    }


    def install(self, info):
        f = getattr(self, "install_" + platform.system().lower(), None)

        if f is not None:
            f(info)
            return

        if info.has_key(platform.linux_distribution()[0]):
            dist = platform.linux_distribution()[0]
            pkg_name = info[dist]

            ret = os.system("sudo %s %s" % (self.dist_installers[dist],  pkg_name))

            if ret != 0:
                raise InstalationFail("Failed to install %s ", pkg_name)

            return

        if info.has_key("default"):
            info["default"](self)
        else:
            raise InstalationFail("Could not install a pakcage")



    def install_from_source(self, url):
        filename = url.split("/")[-1]

        print "Downloading %s from %s." % (filename, url)
        urllib.urlretrieve(url, filename)

        tar = tarfile.open(filename)
        print "Extracting"
        tar.extractall()

        folder_name, ext = os.path.splitext(filename)

        if ext[0] != "t":
            folder_name = os.path.splitext(folder_name)[0]

        print "Installing"
        err_code = os.system("cd %s; ./configure --prefix=/usr/ ; make ; sudo make install " % folder_name)

        if err_code:
            raise InstalationFail("Failed to install from source.")

        os.remove(filename)
        shutil.rmtree(folder_name)


def setup_setuptools_from_source(installer):
    def get_download_link():
        version=".".join(platform.python_version().split(".")[:2])
        return  (
            "http://pypi.python.org/packages/%s/s/setuptools/setuptools-0.6c11-py%s.egg"% (version, version),
            "setuptools-0.6c11-py%s.egg" % version
        )

    url, name = get_download_link()
    urllib.urlretrieve(url, name)

    os.system("sudo sh %s" % name )
    os.system("rm %s" % name)


def program_exists(name):
    for path in os.environ["PATH"].split(":"):
        if os.path.exists(os.path.join(path, name)):
            return True
    return False

def setup_setuptools():
    if program_exists("easy_install"):
        return

    installer = PackageInstaller()

    installer.install({
        "Fedora": "python-setuptools", 
        "Ubuntu": "python-setuptools",
        "default": setup_setuptools_from_source,
    })


def setup_python_development_headers_from_source(installer):
    ver = platform.python_version()
    url = "http://python.org/ftp/python/%s/Python-%s.tgz" % (ver, ver)

    installer.install_from_source(url)
   
def setup_python_development_headers():
    def check_header_existence(name):
        include_folders = ["/usr/include"]
        ver = ".".join(platform.python_version_tuple()[:2])

        for folder in include_folders:
            py_folder = os.path.join(folder, "python%s" % ver)
            if os.path.exists(py_folder):
                if os.path.exists(os.path.join(py_folder, name)):
                    return True
        return False

    if check_header_existence("Python.h"):
        return

    installer = PackageInstaller()
    installer.install({
        "Fedora": "python-devel",
        "Ubuntu": "python-dev",
        "default": setup_python_development_headers_from_source
    })

def setup_gcc_from_source(installer):
    version = "4.6.2"
    url = "ftp://ftp.mpi-sb.mpg.de/pub/gnu/mirror/gcc.gnu.org/pub/gcc/releases/gcc-4.6.2/gcc-%s.tar.gz" % version
    installer.install_from_source(url)


def setup_gcc():
    if program_exists("gcc"):
        return 
    installer = PackageInstaller()
    installer.install({
        "Fedora": "gcc",
        "Ubuntu": "gcc",
        "default": setup_gcc_from_source
    })

def setup_python_packages():
    os.system("sudo scripts/bundle")


def setup_django_project():
    shutil.copy("settings.py.sample", "settings.py")
    shutil.copy("config/databases.py.sample", "config/databases.py")

    os.system("./manage.py syncdb")
    os.system("./manage.py migrate")

def setup_sqlite_from_source(installer):
    installer.install_from_source("http://www.sqlite.org/sqlite-autoconf-3071000.tar.gz")

def setup_sqlite():
    installer = PackageInstaller()
    err =  os.system("sudo easy_install pysqlite")
    if err:
        installer.install({
            "Fedora" : "sqlite-devel",
            "Ubuntu" : "libsqlite3-dev",
            "default": setup_sqlite_from_source,
        })
        if os.system("sudo easy_install pysqlite"):
            raise InstalationFail("Failled to install pysqlite.")



if __name__ == "__main__":
    #setting up platform dependent packages
    setup_gcc()
    setup_setuptools()
    setup_python_development_headers()
    setup_sqlite()

    #setting up python packages with easy_install

    setup_python_packages()

    #setting up django project

    setup_django_project()

