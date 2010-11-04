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

from CIM14v13.IEC61970.ControlArea.ControlArea import ControlArea

class SubControlArea(ControlArea):
    """SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """

    def __init__(self, Flowgate=None, Export_EnergyTransactions=None, Import_EnergyTransactions=None, HostControlArea=None, PartOf=None, SideA_TieLines=None, GeneratingUnits=None, SideB_TieLines=None, **kw_args):
        """Initializes a new 'SubControlArea' instance.

        @param Flowgate: A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        @param Export_EnergyTransactions: Energy is transferred between interchange areas
        @param Import_EnergyTransactions: Energy is transferred between interchange areas
        @param HostControlArea: The interchange area  may operate as a control area
        @param PartOf: A transmission path's service point is part of an interchange area
        @param SideA_TieLines: The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param GeneratingUnits: A GeneratingUnit injects energy into a SubControlArea.
        @param SideB_TieLines: The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        self._Flowgate = []
        self.Flowgate = [] if Flowgate is None else Flowgate

        self._Export_EnergyTransactions = []
        self.Export_EnergyTransactions = [] if Export_EnergyTransactions is None else Export_EnergyTransactions

        self._Import_EnergyTransactions = []
        self.Import_EnergyTransactions = [] if Import_EnergyTransactions is None else Import_EnergyTransactions

        self._HostControlArea = None
        self.HostControlArea = HostControlArea

        self._PartOf = []
        self.PartOf = [] if PartOf is None else PartOf

        self._SideA_TieLines = []
        self.SideA_TieLines = [] if SideA_TieLines is None else SideA_TieLines

        self._GeneratingUnits = []
        self.GeneratingUnits = [] if GeneratingUnits is None else GeneratingUnits

        self._SideB_TieLines = []
        self.SideB_TieLines = [] if SideB_TieLines is None else SideB_TieLines

        super(SubControlArea, self).__init__(**kw_args)

    def getFlowgate(self):
        """A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        """
        return self._Flowgate

    def setFlowgate(self, value):
        for x in self._Flowgate:
            x._SubControlArea = None
        for y in value:
            y._SubControlArea = self
        self._Flowgate = value

    Flowgate = property(getFlowgate, setFlowgate)

    def addFlowgate(self, *Flowgate):
        for obj in Flowgate:
            obj._SubControlArea = self
            self._Flowgate.append(obj)

    def removeFlowgate(self, *Flowgate):
        for obj in Flowgate:
            obj._SubControlArea = None
            self._Flowgate.remove(obj)

    def getExport_EnergyTransactions(self):
        """Energy is transferred between interchange areas
        """
        return self._Export_EnergyTransactions

    def setExport_EnergyTransactions(self, value):
        for x in self._Export_EnergyTransactions:
            x._Export_SubControlArea = None
        for y in value:
            y._Export_SubControlArea = self
        self._Export_EnergyTransactions = value

    Export_EnergyTransactions = property(getExport_EnergyTransactions, setExport_EnergyTransactions)

    def addExport_EnergyTransactions(self, *Export_EnergyTransactions):
        for obj in Export_EnergyTransactions:
            obj._Export_SubControlArea = self
            self._Export_EnergyTransactions.append(obj)

    def removeExport_EnergyTransactions(self, *Export_EnergyTransactions):
        for obj in Export_EnergyTransactions:
            obj._Export_SubControlArea = None
            self._Export_EnergyTransactions.remove(obj)

    def getImport_EnergyTransactions(self):
        """Energy is transferred between interchange areas
        """
        return self._Import_EnergyTransactions

    def setImport_EnergyTransactions(self, value):
        for x in self._Import_EnergyTransactions:
            x._Import_SubControlArea = None
        for y in value:
            y._Import_SubControlArea = self
        self._Import_EnergyTransactions = value

    Import_EnergyTransactions = property(getImport_EnergyTransactions, setImport_EnergyTransactions)

    def addImport_EnergyTransactions(self, *Import_EnergyTransactions):
        for obj in Import_EnergyTransactions:
            obj._Import_SubControlArea = self
            self._Import_EnergyTransactions.append(obj)

    def removeImport_EnergyTransactions(self, *Import_EnergyTransactions):
        for obj in Import_EnergyTransactions:
            obj._Import_SubControlArea = None
            self._Import_EnergyTransactions.remove(obj)

    def getHostControlArea(self):
        """The interchange area  may operate as a control area
        """
        return self._HostControlArea

    def setHostControlArea(self, value):
        if self._HostControlArea is not None:
            filtered = [x for x in self.HostControlArea.SubControlAreas if x != self]
            self._HostControlArea._SubControlAreas = filtered

        self._HostControlArea = value
        if self._HostControlArea is not None:
            self._HostControlArea._SubControlAreas.append(self)

    HostControlArea = property(getHostControlArea, setHostControlArea)

    def getPartOf(self):
        """A transmission path's service point is part of an interchange area
        """
        return self._PartOf

    def setPartOf(self, value):
        for x in self._PartOf:
            x._MemberOf = None
        for y in value:
            y._MemberOf = self
        self._PartOf = value

    PartOf = property(getPartOf, setPartOf)

    def addPartOf(self, *PartOf):
        for obj in PartOf:
            obj._MemberOf = self
            self._PartOf.append(obj)

    def removePartOf(self, *PartOf):
        for obj in PartOf:
            obj._MemberOf = None
            self._PartOf.remove(obj)

    def getSideA_TieLines(self):
        """The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._SideA_TieLines

    def setSideA_TieLines(self, value):
        for x in self._SideA_TieLines:
            x._SideA_SubControlArea = None
        for y in value:
            y._SideA_SubControlArea = self
        self._SideA_TieLines = value

    SideA_TieLines = property(getSideA_TieLines, setSideA_TieLines)

    def addSideA_TieLines(self, *SideA_TieLines):
        for obj in SideA_TieLines:
            obj._SideA_SubControlArea = self
            self._SideA_TieLines.append(obj)

    def removeSideA_TieLines(self, *SideA_TieLines):
        for obj in SideA_TieLines:
            obj._SideA_SubControlArea = None
            self._SideA_TieLines.remove(obj)

    def getGeneratingUnits(self):
        """A GeneratingUnit injects energy into a SubControlArea.
        """
        return self._GeneratingUnits

    def setGeneratingUnits(self, value):
        for x in self._GeneratingUnits:
            x._SubControlArea = None
        for y in value:
            y._SubControlArea = self
        self._GeneratingUnits = value

    GeneratingUnits = property(getGeneratingUnits, setGeneratingUnits)

    def addGeneratingUnits(self, *GeneratingUnits):
        for obj in GeneratingUnits:
            obj._SubControlArea = self
            self._GeneratingUnits.append(obj)

    def removeGeneratingUnits(self, *GeneratingUnits):
        for obj in GeneratingUnits:
            obj._SubControlArea = None
            self._GeneratingUnits.remove(obj)

    def getSideB_TieLines(self):
        """The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._SideB_TieLines

    def setSideB_TieLines(self, value):
        for x in self._SideB_TieLines:
            x._SideB_SubControlArea = None
        for y in value:
            y._SideB_SubControlArea = self
        self._SideB_TieLines = value

    SideB_TieLines = property(getSideB_TieLines, setSideB_TieLines)

    def addSideB_TieLines(self, *SideB_TieLines):
        for obj in SideB_TieLines:
            obj._SideB_SubControlArea = self
            self._SideB_TieLines.append(obj)

    def removeSideB_TieLines(self, *SideB_TieLines):
        for obj in SideB_TieLines:
            obj._SideB_SubControlArea = None
            self._SideB_TieLines.remove(obj)

