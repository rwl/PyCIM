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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class SeriesCompensator(ConductingEquipment):
    """A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.
    """

    def __init__(self, r=0.0, x=0.0, **kw_args):
        """Initializes a new 'SeriesCompensator' instance.

        @param r: Positive sequence resistance. 
        @param x: Positive sequence reactance. 
        """
        #: Positive sequence resistance.
        self.r = r

        #: Positive sequence reactance.
        self.x = x

        super(SeriesCompensator, self).__init__(**kw_args)

