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

from CIM14v13.IEC61970.Wires.Conductor import Conductor

class DCLineSegment(Conductor):
    """A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.
    """

    def __init__(self, dcSegmentInductance=0.0, dcSegmentResistance=0.0, *args, **kw_args):
        """Initializes a new 'DCLineSegment' instance.

        @param dcSegmentInductance: Inductance of the DC line segment. 
        @param dcSegmentResistance: Resistance of the DC line segment. 
        """
        #: Inductance of the DC line segment.
        self.dcSegmentInductance = dcSegmentInductance

        #: Resistance of the DC line segment.
        self.dcSegmentResistance = dcSegmentResistance

        super(DCLineSegment, self).__init__(*args, **kw_args)

