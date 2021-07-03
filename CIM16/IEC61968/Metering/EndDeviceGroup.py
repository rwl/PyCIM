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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class EndDeviceGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """

    def __init__(self, groupAddress=0, EndDeviceControls=None, EndDevices=None, DemandResponseProgram=None, *args, **kw_args):
        """Initialises a new 'EndDeviceGroup' instance.

        @param groupAddress: Address of this end device group. 
        @param EndDeviceControls: All end device controls sending commands to this end device group.
        @param EndDevices: All end devices this end device group refers to.
        @param DemandResponseProgram: Demand response program for this group of end devices.
        """
        #: Address of this end device group.
        self.groupAddress = groupAddress

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._EndDevices = []
        self.EndDevices = [] if EndDevices is None else EndDevices

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        super(EndDeviceGroup, self).__init__(*args, **kw_args)

    _attrs = ["groupAddress"]
    _attr_types = {"groupAddress": int}
    _defaults = {"groupAddress": 0}
    _enums = {}
    _refs = ["EndDeviceControls", "EndDevices", "DemandResponseProgram"]
    _many_refs = ["EndDeviceControls", "EndDevices"]

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

    def getEndDevices(self):
        """All end devices this end device group refers to.
        """
        return self._EndDevices

    def setEndDevices(self, value):
        for p in self._EndDevices:
            filtered = [q for q in p.EndDeviceGroups if q != self]
            self._EndDevices._EndDeviceGroups = filtered
        for r in value:
            if self not in r._EndDeviceGroups:
                r._EndDeviceGroups.append(self)
        self._EndDevices = value

    EndDevices = property(getEndDevices, setEndDevices)

    def addEndDevices(self, *EndDevices):
        for obj in EndDevices:
            if self not in obj._EndDeviceGroups:
                obj._EndDeviceGroups.append(self)
            self._EndDevices.append(obj)

    def removeEndDevices(self, *EndDevices):
        for obj in EndDevices:
            if self in obj._EndDeviceGroups:
                obj._EndDeviceGroups.remove(self)
            self._EndDevices.remove(obj)

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

