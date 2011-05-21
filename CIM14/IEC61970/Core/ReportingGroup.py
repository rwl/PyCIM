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

class ReportingGroup(IdentifiedObject):
    """A reporting group is used for various ad-hoc groupings used for reporting.
    """

    def __init__(self, ReportingSuperGroup=None, TopologicalNode=None, BusNameMarker=None, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'ReportingGroup' instance.

        @param ReportingSuperGroup: Reporting super group to which this reporting group belongs.
        @param TopologicalNode: The topological nodes that belong to the reporting group.
        @param BusNameMarker: The BusNameMarkers that belong to this reporting group.
        @param PowerSystemResource: PSR's which belong to this reporting group.
        """
        self._ReportingSuperGroup = None
        self.ReportingSuperGroup = ReportingSuperGroup

        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        self._BusNameMarker = []
        self.BusNameMarker = [] if BusNameMarker is None else BusNameMarker

        self._PowerSystemResource = []
        self.PowerSystemResource = [] if PowerSystemResource is None else PowerSystemResource

        super(ReportingGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ReportingSuperGroup", "TopologicalNode", "BusNameMarker", "PowerSystemResource"]
    _many_refs = ["TopologicalNode", "BusNameMarker", "PowerSystemResource"]

    def getReportingSuperGroup(self):
        """Reporting super group to which this reporting group belongs.
        """
        return self._ReportingSuperGroup

    def setReportingSuperGroup(self, value):
        if self._ReportingSuperGroup is not None:
            filtered = [x for x in self.ReportingSuperGroup.ReportingGroup if x != self]
            self._ReportingSuperGroup._ReportingGroup = filtered

        self._ReportingSuperGroup = value
        if self._ReportingSuperGroup is not None:
            if self not in self._ReportingSuperGroup._ReportingGroup:
                self._ReportingSuperGroup._ReportingGroup.append(self)

    ReportingSuperGroup = property(getReportingSuperGroup, setReportingSuperGroup)

    def getTopologicalNode(self):
        """The topological nodes that belong to the reporting group.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x.ReportingGroup = None
        for y in value:
            y._ReportingGroup = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.ReportingGroup = self

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.ReportingGroup = None

    def getBusNameMarker(self):
        """The BusNameMarkers that belong to this reporting group.
        """
        return self._BusNameMarker

    def setBusNameMarker(self, value):
        for x in self._BusNameMarker:
            x.ReportingGroup = None
        for y in value:
            y._ReportingGroup = self
        self._BusNameMarker = value

    BusNameMarker = property(getBusNameMarker, setBusNameMarker)

    def addBusNameMarker(self, *BusNameMarker):
        for obj in BusNameMarker:
            obj.ReportingGroup = self

    def removeBusNameMarker(self, *BusNameMarker):
        for obj in BusNameMarker:
            obj.ReportingGroup = None

    def getPowerSystemResource(self):
        """PSR's which belong to this reporting group.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        for p in self._PowerSystemResource:
            filtered = [q for q in p.ReportingGroup if q != self]
            self._PowerSystemResource._ReportingGroup = filtered
        for r in value:
            if self not in r._ReportingGroup:
                r._ReportingGroup.append(self)
        self._PowerSystemResource = value

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def addPowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self not in obj._ReportingGroup:
                obj._ReportingGroup.append(self)
            self._PowerSystemResource.append(obj)

    def removePowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self in obj._ReportingGroup:
                obj._ReportingGroup.remove(self)
            self._PowerSystemResource.remove(obj)

