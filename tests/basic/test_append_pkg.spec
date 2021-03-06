# -*- mode: python -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# This tests the not well documented and seldom used feature of having
# the PYZ-archive in a separate file (.pkg).

__testname__ = 'test_pyz-as-external-file'

a = Analysis([__testname__ + '.py'],
             pathex=[])
pyz = PYZ(a.pure)
exe = EXE(append_pkg=False,
          pyz,
          a.scripts,
          exclude_binaries=1,
          name= __testname__ + '.exe',
          debug=False,
          strip=False,
          upx=False,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               name=__testname__)
