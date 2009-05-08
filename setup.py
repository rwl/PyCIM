#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="CIM",
    description="Python implementation of the Common Information Model.",
    author="Richard W. Lincoln",
    author_email="r.w.lincoln@gmail.com",
    url="http://rwl.github.com/cim",
    version="13.19.1",
    license="GPLv2",
    entry_points={"gui_scripts": ["cim_vm = CIM.ViewModel.Main:main",
                                  "cim = CIM.Plugin.Run:main"]},
    install_requires=["Traits>=3.0.3", "EnvisageCore>=3.0.2",
        "EnvisagePlugins>=3.0.2"],
    include_package_data=True,
    packages=find_packages(),
    test_suite = "CIM.Test",
    zip_safe=False
)

# EOF -------------------------------------------------------------------------
