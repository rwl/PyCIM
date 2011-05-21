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

class BusNameMarker(IdentifiedObject):
    """Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """

    def __init__(self, ReportingGroup=None, ConnectivityNode=None, *args, **kw_args):
        """Initialises a new 'BusNameMarker' instance.

        @param ReportingGroup: The reporting group to which this BusNameMarker belongs.
        @param ConnectivityNode: The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
        """
        self._ReportingGroup = None
        self.ReportingGroup = ReportingGroup

        self._ConnectivityNode = []
        self.ConnectivityNode = [] if ConnectivityNode is None else ConnectivityNode

        super(BusNameMarker, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ReportingGroup", "ConnectivityNode"]
    _many_refs = ["ConnectivityNode"]

    def getReportingGroup(self):
        """The reporting group to which this BusNameMarker belongs.
        """
        return self._ReportingGroup

    def setReportingGroup(self, value):
        if self._ReportingGroup is not None:
            filtered = [x for x in self.ReportingGroup.BusNameMarker if x != self]
            self._ReportingGroup._BusNameMarker = filtered

        self._ReportingGroup = value
        if self._ReportingGroup is not None:
            if self not in self._ReportingGroup._BusNameMarker:
                self._ReportingGroup._BusNameMarker.append(self)

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def getConnectivityNode(self):
        """The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
        """
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        for x in self._ConnectivityNode:
            x.BusNameMarker = None
        for y in value:
            y._BusNameMarker = self
        self._ConnectivityNode = value

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

    def addConnectivityNode(self, *ConnectivityNode):
        for obj in ConnectivityNode:
            obj.BusNameMarker = self

    def removeConnectivityNode(self, *ConnectivityNode):
        for obj in ConnectivityNode:
            obj.BusNameMarker = None

