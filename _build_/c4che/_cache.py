AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
CC = ['/usr/bin/gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '6', '3')
CFLAGS = ['-DHAVE_CONFIG_H', '-g', '-DGEANY_DEBUG', '-DGTK']
CFLAGS_GIO = ['-pthread']
CFLAGS_GMODULE = ['-pthread', '-pthread']
CFLAGS_GTHREAD = ['-pthread', '-pthread']
CFLAGS_GTK = ['-pthread']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-DNDEBUG', '-DGTK', '-DSCI_LEXER', '-DG_THREADS_IMPL_NONE']
CXXFLAGS_GIO = ['-pthread']
CXXFLAGS_GMODULE = ['-pthread', '-pthread']
CXXFLAGS_GTHREAD = ['-pthread', '-pthread']
CXXFLAGS_GTK = ['-pthread']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DEFINES = ['HAVE_FCNTL_H=1', 'HAVE_FNMATCH_H=1', 'HAVE_GLOB_H=1', 'HAVE_SYS_TIME_H=1', 'HAVE_SYS_TYPES_H=1', 'HAVE_SYS_STAT_H=1', 'HAVE_STDLIB_H=1', 'STDC_HEADERS=1', 'HAVE_REGCOMP=1', 'HAVE_FGETPOS=1', 'HAVE_FTRUNCATE=1', 'HAVE_MKSTEMP=1', 'HAVE_STRSTR=1', 'LOCALEDIR="/usr/local/share/locale"', 'DATADIR="/usr/local/share"', 'HAVE_LOCALE_H=1', 'HAVE_GTK=1', 'HAVE_GLIB=1', 'HAVE_GMODULE=1', 'HAVE_GIO=1', 'GTK_VERSION="2.24.10"', 'HAVE_GTHREAD=1', 'DOCDIR="/usr/local/share/doc/geany"', 'LIBDIR="/usr/local/lib"', 'MANDIR="/usr/local/share/man"', 'ENABLE_NLS=1', 'GEANY_LOCALEDIR="/usr/local/share/locale"', 'GEANY_DATADIR="/usr/local/share"', 'GEANY_DOCDIR="/usr/local/share/doc/geany"', 'GEANY_LIBDIR="/usr/local/lib"', 'GEANY_PREFIX="/usr/local"', 'PACKAGE="geany"', 'VERSION="1.24"', 'REVISION="2f120d7"', 'GETTEXT_PACKAGE="geany"', 'HAVE_PLUGINS=1', 'HAVE_SOCKET=1', 'HAVE_VTE=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/geany'
HAVE_PLUGINS = 1
HAVE_REGCOMP = 1
HAVE_SOCKET = 1
HAVE_VTE = 1
INCLUDES_GIO = ['/usr/include/glib-2.0', '/usr/lib/i386-linux-gnu/glib-2.0/include']
INCLUDES_GLIB = ['/usr/include/glib-2.0', '/usr/lib/i386-linux-gnu/glib-2.0/include']
INCLUDES_GMODULE = ['/usr/include/glib-2.0', '/usr/lib/i386-linux-gnu/glib-2.0/include']
INCLUDES_GTHREAD = ['/usr/include/glib-2.0', '/usr/lib/i386-linux-gnu/glib-2.0/include']
INCLUDES_GTK = ['/usr/include/gtk-2.0', '/usr/lib/i386-linux-gnu/gtk-2.0/include', '/usr/include/atk-1.0', '/usr/include/cairo', '/usr/include/gdk-pixbuf-2.0', '/usr/include/pango-1.0', '/usr/include/gio-unix-2.0/', '/usr/include/glib-2.0', '/usr/lib/i386-linux-gnu/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng12']
INTLTOOL = ['/usr/bin/perl', '/usr/bin/intltool-merge']
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_GIO = ['gio-2.0', 'gobject-2.0', 'glib-2.0']
LIB_GLIB = ['glib-2.0']
LIB_GMODULE = ['gmodule-2.0', 'rt', 'glib-2.0']
LIB_GTHREAD = ['gthread-2.0', 'rt', 'glib-2.0']
LIB_GTK = ['gtk-x11-2.0', 'gdk-x11-2.0', 'atk-1.0', 'gio-2.0', 'pangoft2-1.0', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo', 'pango-1.0', 'freetype', 'fontconfig', 'gobject-2.0', 'glib-2.0']
LIB_ST = '-l%s'
LINKFLAGS_GIO = ['-pthread']
LINKFLAGS_GMODULE = ['-pthread', '-Wl,--export-dynamic', '-pthread']
LINKFLAGS_GTHREAD = ['-pthread', '-pthread']
LINKFLAGS_GTK = ['-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
LOCALEDIR = '/usr/local/share/locale'
MANDIR = '/usr/local/share/man'
MSGFMT = '/usr/bin/msgfmt'
PERL = '/usr/bin/perl'
PKGCONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr/local'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
cfg_files = ['/home/juvasquezg/clones/geany/_build_/config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = '%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_FCNTL_H', 'HAVE_FNMATCH_H', 'HAVE_GLOB_H', 'HAVE_SYS_TIME_H', 'HAVE_SYS_TYPES_H', 'HAVE_SYS_STAT_H', 'HAVE_STDLIB_H', 'STDC_HEADERS', 'HAVE_REGCOMP', 'HAVE_FGETPOS', 'HAVE_FTRUNCATE', 'HAVE_MKSTEMP', 'HAVE_STRSTR', 'LOCALEDIR', 'DATADIR', 'HAVE_LOCALE_H', 'HAVE_GTK', 'HAVE_GLIB', 'HAVE_GMODULE', 'HAVE_GIO', 'GTK_VERSION', 'HAVE_GTHREAD', 'DOCDIR', 'LIBDIR', 'MANDIR', 'ENABLE_NLS', 'GEANY_LOCALEDIR', 'GEANY_DATADIR', 'GEANY_DOCDIR', 'GEANY_LIBDIR', 'GEANY_PREFIX', 'PACKAGE', 'VERSION', 'REVISION', 'GETTEXT_PACKAGE', 'HAVE_PLUGINS', 'HAVE_SOCKET', 'HAVE_VTE']
gtk_package_name = 'gtk+-2.0'
is_win32 = False
macbundle_PATTERN = '%s.bundle'
minimum_gtk_version = '2.16.0'
use_gtk3 = False
