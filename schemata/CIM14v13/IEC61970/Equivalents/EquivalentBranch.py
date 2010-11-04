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

from CIM14v13.IEC61970.Equivalents.EquivalentEquipment import EquivalentEquipment

class EquivalentBranch(EquivalentEquipment):
    """The class represents equivalent branches.
    """

    def __init__(self, r=0.0, x=0.0, **kw_args):
        """Initializes a new 'EquivalentBranch' instance.

        @param r: Positive sequence series resistance of the reduced branch. 
        @param x: Positive sequence series reactance of the reduced branch. 
        """
        #: Positive sequence series resistance of the reduced branch.
        self.r = r

        #: Positive sequence series reactance of the reduced branch.
        self.x = x

        super(EquivalentBranch, self).__init__(**kw_args)

