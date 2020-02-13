from spack import *


class Libpressio(CMakePackage):
    """A generic abstraction for the compression of dense tensors"""

    homepage = "https://github.com/codarcode/libpressio"
    url      = "https://github.com/robertu94/libpressio/archive/0.31.1.tar.gz"
    git      = "https://github.com/robertu94/libpressio"

    version('master', branch='master')
    version('0.31.1', sha256='32c1fd8319fbbb844a0a252d44761f81f17c6f3549daadce47e81524d84605a4')
    version('0.31.0', sha256='9d4bc8b2c1a210a58f34216cebe7cd5935039d244b7e90f7e2792bda81ff7ddc')
    version('0.30.1', sha256='e2249bdced68d80a413de59f8393922553a8900a14e731030e362266e82a9af8')
    version('0.30.0', sha256='91de53099d9381e3744e7a1ac06d2db0f9065378c4d178328b78ac797ee3ec65')
    version('0.29.1', sha256='ced1e98fbd383669e59ec06d2e0c15e27dbceda9ac5569d311c538b2fe6d3876')
    version('0.29.0', sha256='a417a1d0ed75bd51131b86fba990502666d8c1388ad6282b3097aa461ccf9785')
    version('0.28.0', sha256='5c4e0fe8c7c80615688f271b57b35ee9d924ac07c6d3d56d0303e610338ed332')
    version('0.27.1', sha256='3f7d2401ff8b113781d93c5bf374f47ca35b2f962634c6310b73620da735e63d')
    version('0.27.0', sha256='387ee5958de2d986095cda2aaf39d0bf319d02eaeeea2a565aea97e6a6f31f36')
    version('0.26.0', sha256='c451591d106d1671c9ddbb5c304979dd2d083e0616b2aeede62e7a6b568f828c')


    variant('blosc', default=True, description='support the blosc lossless compressors')
    variant('fpzip', default=True, description='support for the FPZIP lossy compressor')
    variant('hdf5', default=True, description='support reading and writing from hdf5 files')
    variant('magick', default=True, description='support the imagemagick image compressors')
    variant('mgard', default=True, description='support for the MAGARD error bounded lossy compressor')
    variant('python', default=False, description='build the python wrappers')
    variant('sz', default=True, description='support for the SZ error bounded lossy compressor')
    variant('zfp', default=True, description='support for the ZFP error bounded lossy compressor')
    variant('boost', default=False, description='support older compilers using boost')

    depends_on('boost', when="+boost")
    depends_on('c-blosc', when="+blosc")
    depends_on('fpzip', when="+fpzip")
    depends_on('hdf5', when="+hdf5")
    depends_on('imagemagick', when="+magick")
    depends_on('mgard', when="+mgard")
    depends_on('python@3:', when="+python")
    depends_on('swig@3.12:', when="+python", type="build")
    depends_on('sz', when="+sz")
    depends_on('zfp', when="+zfp")

    def cmake_args(self):
        args = []
        if "+python" in self.spec:
            args.append("-DBUILD_PYTHON_WRAPPERS=ON")
        if "+hdf5" in self.spec:
            args.append("-DLIBPRESSIO_HAS_HDF=ON")
        if "+sz" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZ=ON")
        if "+zfp" in self.spec:
            args.append("-DLIBPRESSIO_HAS_ZFP=ON")
        if "+fpzip" in self.spec:
            args.append("-DLIBPRESSIO_HAS_FPZIP=ON")
        if "+blosc" in self.spec:
            args.append("-DLIBPRESSIO_HAS_BLOSC=ON")
        if "+magick" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MAGICK=ON")
        if "+mgard" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MGARD=ON")
        if "+boost" in self.spec:
            args.append("-DLIBPRESSIO_CXX_VERSION=11")


        return args
