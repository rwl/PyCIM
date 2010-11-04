# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.Element import Element

class PackageDependenciesCIMVeresion(Element):
    """The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.
    """

    def __init__(self, date='', vesion='', **kw_args):
        """Initializes a new 'PackageDependenciesCIMVeresion' instance.

        @param date: Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated. 
        @param vesion: The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package. 
        """
        #: Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated.
        self.date = date

        #: The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package.
        self.vesion = vesion

        super(PackageDependenciesCIMVeresion, self).__init__(**kw_args)

