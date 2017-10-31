from distutils.core import setup, Extension

module = Extension("myModule",sources=["myModule.c"])
setup(name="anypackageName",version="1.0",description="package for myModule",ext_modules=[module])


