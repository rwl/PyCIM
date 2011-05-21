# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class EndDeviceGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """

    def __init__(self, groupAddress=0, EndDeviceAssets=None, EndDeviceControls=None, DemandResponseProgram=None, *args, **kw_args):
        """Initialises a new 'EndDeviceGroup' instance.

        @param groupAddress: Address of this end device group. 
        @param EndDeviceAssets: All end device assets this end device group refers to.
        @param EndDeviceControls: All end device controls sending commands to this end device group.
        @param DemandResponseProgram: Demand response program for this group of end devices.
        """
        #: Address of this end device group.
        self.groupAddress = groupAddress

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        super(EndDeviceGroup, self).__init__(*args, **kw_args)

    _attrs = ["groupAddress"]
    _attr_types = {"groupAddress": int}
    _defaults = {"groupAddress": 0}
    _enums = {}
    _refs = ["EndDeviceAssets", "EndDeviceControls", "DemandResponseProgram"]
    _many_refs = ["EndDeviceAssets", "EndDeviceControls"]

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
            x.EndDeviceGroup = None
        for y in value:
            y._EndDeviceGroup = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDeviceGroup = self

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDeviceGroup = None

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
            if self not in self._DemandResponseProgram._EndDeviceGroups:
                self._DemandResponseProgram._EndDeviceGroups.append(self)

    DemandResponseProgram = property(getDemandResponseProgram, setDemandResponseProgram)

