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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CUContractorItem(IdentifiedObject):
    """Compatible unit contractor item.
    """

    def __init__(self, bidAmount=0.0, activityCode='', CompatibleUnits=None, status=None, *args, **kw_args):
        """Initializes a new 'CUContractorItem' instance.

        @param bidAmount: The amount that a given contractor will charge for performing this unit of work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param CompatibleUnits:
        @param status:
        """
        #: The amount that a given contractor will charge for performing this unit of work. 
        self.bidAmount = bidAmount

        #: Activity code identifies a specific and distinguishable unit of work. 
        self.activityCode = activityCode

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self.status = status

        super(CUContractorItem, self).__init__(*args, **kw_args)

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CUContractorItems if q != self]
            self._CompatibleUnits._CUContractorItems = filtered
        for r in value:
            if self not in r._CUContractorItems:
                r._CUContractorItems.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CUContractorItems:
                obj._CUContractorItems.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CUContractorItems:
                obj._CUContractorItems.remove(self)
            self._CompatibleUnits.remove(obj)

    status = None

