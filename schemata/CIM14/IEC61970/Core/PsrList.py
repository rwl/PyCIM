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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PsrList(IdentifiedObject):
    """Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """

    def __init__(self, typePSRList='', PowerSystemResources=None, **kw_args):
        """Initializes a new 'PsrList' instance.

        @param typePSRList: Type of power system resources in this list. 
        @param PowerSystemResources:
        """
        #: Type of power system resources in this list.
        self.typePSRList = typePSRList

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        super(PsrList, self).__init__(**kw_args)

    def getPowerSystemResources(self):
        
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.PsrLists if q != self]
            self._PowerSystemResources._PsrLists = filtered
        for r in value:
            if self not in r._PsrLists:
                r._PsrLists.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._PsrLists:
                obj._PsrLists.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._PsrLists:
                obj._PsrLists.remove(self)
            self._PowerSystemResources.remove(obj)

