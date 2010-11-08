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
            self._ReportingGroup._BusNameMarker.append(self)

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def getConnectivityNode(self):
        """The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
        """
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        for x in self._ConnectivityNode:
            x._BusNameMarker = None
        for y in value:
            y._BusNameMarker = self
        self._ConnectivityNode = value

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

    def addConnectivityNode(self, *ConnectivityNode):
        for obj in ConnectivityNode:
            obj._BusNameMarker = self
            self._ConnectivityNode.append(obj)

    def removeConnectivityNode(self, *ConnectivityNode):
        for obj in ConnectivityNode:
            obj._BusNameMarker = None
            self._ConnectivityNode.remove(obj)

