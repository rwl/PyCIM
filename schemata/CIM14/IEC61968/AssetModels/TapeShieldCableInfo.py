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

from CIM14.IEC61968.AssetModels.CableInfo import CableInfo

class TapeShieldCableInfo(CableInfo):
    """Tape shield cable data.
    """

    def __init__(self, tapeThickness=0.0, tapeLap=0.0, *args, **kw_args):
        """Initialises a new 'TapeShieldCableInfo' instance.

        @param tapeThickness: Thickness of the tape shield, before wrapping. 
        @param tapeLap: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        """
        #: Thickness of the tape shield, before wrapping.
        self.tapeThickness = tapeThickness

        #: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
        self.tapeLap = tapeLap

        super(TapeShieldCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["tapeThickness", "tapeLap"]
    _attr_types = {"tapeThickness": float, "tapeLap": float}
    _defaults = {"tapeThickness": 0.0, "tapeLap": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

