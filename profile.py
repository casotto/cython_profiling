#!/usr/bin/env python
# encoding: utf-8
# filename: profile.py

import pstats, cProfile

from calc_pi.calc_py1 import approx_pi as approx_py
cProfile.runctx("approx_py()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
print "first python version"
s.strip_dirs().sort_stats("time").print_stats()


from calc_pi.calc_pyx1 import approx_pi as approx_pyx1

cProfile.runctx("approx_pyx1()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
print "python code compiled in cython"
s.strip_dirs().sort_stats("time").print_stats()


from calc_pi.calc_pyx2 import approx_pi as approx_pyx2

cProfile.runctx("approx_pyx2()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
print "second cython implementation"
s.strip_dirs().sort_stats("time").print_stats()


from calc_pi.calc_pyx3 import approx_pi

cProfile.runctx("approx_pi()", globals(), locals(), "Profile.prof")
print "third cython implementation"
s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
# TODO: here results are different from http://docs.cython.org/en/latest/src/tutorial/profiling_tutorial.html



