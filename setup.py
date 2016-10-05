from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
from setuptools.extension import Extension
from Cython.Compiler.Options import directive_defaults

directive_defaults['linetrace'] = True
directive_defaults['binding'] = True
# to avoid annoying errors
directive_defaults['cdivision'] = True

extensions = [Extension("calc_pi.calc_pyx1", ["calc_pi\calc_pyx1.pyx"]),
              Extension("calc_pi.calc_pyx2", ["calc_pi\calc_pyx2.pyx"]),
              Extension("calc_pi.calc_pyx3", ["calc_pi\calc_pyx3.pyx"])]
# Use cythonize on the extension object.
setup(name="calc_pi",
      packages=["calc_pi"],
      ext_modules=cythonize(extensions),
      include_dirs=[np.get_include()])
