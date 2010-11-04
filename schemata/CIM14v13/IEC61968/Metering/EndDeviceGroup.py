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

class EndDeviceGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """

    def __init__(self, groupAddress=0, DemandResponseProgram=None, EndDeviceAssets=None, EndDeviceControls=None, **kw_args):
        """Initializes a new 'EndDeviceGroup' instance.

        @param groupAddress: Address of this end device group. 
        @param DemandResponseProgram: Demand response program for this group of end devices.
        @param EndDeviceAssets: All end device assets this end device group refers to.
        @param EndDeviceControls: All end device controls sending commands to this end device group.
        """
        #: Address of this end device group.
        self.groupAddress = groupAddress

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        super(EndDeviceGroup, self).__init__(**kw_args)

    def getDemandResponseProgram(self):
        """Demand response program for this group of end devices.
        """
        return self._DemandResponseProgram

    def setDemandResponseProgram(self, value):
        if self._DemandResponseProgram is not None:
            filtered = [x for x in self.DemandResponseProgram.EndDeviceGroups if x != self]
            self._DemandResponseProgram._EndDeviceGroups = filtered

        self._DemandResponseProgram = value
        if self._DemandResponseProgram is not None:
            self._DemandResponseProgram._EndDeviceGroups.append(self)

    DemandResponseProgram = property(getDemandResponseProgram, setDemandResponseProgram)

    def getEndDeviceAssets(self):
        """All end device assets this end device group refers to.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for p in self._EndDeviceAssets:
            filtered = [q for q in p.EndDeviceGroups if q != self]
            self._EndDeviceAssets._EndDeviceGroups = filtered
        for r in value:
            if self not in r._EndDeviceGroups:
                r._EndDeviceGroups.append(self)
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            if self not in obj._EndDeviceGroups:
                obj._EndDeviceGroups.append(self)
            self._EndDeviceAssets.append(obj)

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            if self in obj._EndDeviceGroups:
                obj._EndDeviceGroups.remove(self)
            self._EndDeviceAssets.remove(obj)

    def getEndDeviceControls(self):
        """All end device controls sending commands to this end device group.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x._EndDeviceGroup = None
        for y in value:
            y._EndDeviceGroup = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._EndDeviceGroup = self
            self._EndDeviceControls.append(obj)

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._EndDeviceGroup = None
            self._EndDeviceControls.remove(obj)

