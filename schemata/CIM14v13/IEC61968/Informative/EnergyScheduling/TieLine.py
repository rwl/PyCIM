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

from CIM14v13.Element import Element

class TieLine(Element):

    def __init__(self, SideA_HostControlArea=None, SideB_HostControlArea=None, SideA_SubControlArea=None, CustomerConsumer=None, SideB_SubControlArea=None, DynamicEnergyTransaction=None, ControlAreaOperators=None, *args, **kw_args):
        """Initializes a new 'TieLine' instance.

        @param SideA_HostControlArea: A HostControlArea can have zero or more tie lines.
        @param SideB_HostControlArea: A HostControlArea can have zero or more tie lines.
        @param SideA_SubControlArea: The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param CustomerConsumer: A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        @param SideB_SubControlArea: The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param DynamicEnergyTransaction: A dynamic energy transaction can act as a pseudo tie line.
        @param ControlAreaOperators: A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
        """
        self._SideA_HostControlArea = None
        self.SideA_HostControlArea = SideA_HostControlArea

        self._SideB_HostControlArea = None
        self.SideB_HostControlArea = SideB_HostControlArea

        self._SideA_SubControlArea = None
        self.SideA_SubControlArea = SideA_SubControlArea

        self._CustomerConsumer = None
        self.CustomerConsumer = CustomerConsumer

        self._SideB_SubControlArea = None
        self.SideB_SubControlArea = SideB_SubControlArea

        self._DynamicEnergyTransaction = None
        self.DynamicEnergyTransaction = DynamicEnergyTransaction

        self._ControlAreaOperators = []
        self.ControlAreaOperators = [] if ControlAreaOperators is None else ControlAreaOperators

        super(TieLine, self).__init__(*args, **kw_args)

    def getSideA_HostControlArea(self):
        """A HostControlArea can have zero or more tie lines.
        """
        return self._SideA_HostControlArea

    def setSideA_HostControlArea(self, value):
        if self._SideA_HostControlArea is not None:
            filtered = [x for x in self.SideA_HostControlArea.SideA_TieLines if x != self]
            self._SideA_HostControlArea._SideA_TieLines = filtered

        self._SideA_HostControlArea = value
        if self._SideA_HostControlArea is not None:
            self._SideA_HostControlArea._SideA_TieLines.append(self)

    SideA_HostControlArea = property(getSideA_HostControlArea, setSideA_HostControlArea)

    def getSideB_HostControlArea(self):
        """A HostControlArea can have zero or more tie lines.
        """
        return self._SideB_HostControlArea

    def setSideB_HostControlArea(self, value):
        if self._SideB_HostControlArea is not None:
            filtered = [x for x in self.SideB_HostControlArea.SideB_TieLines if x != self]
            self._SideB_HostControlArea._SideB_TieLines = filtered

        self._SideB_HostControlArea = value
        if self._SideB_HostControlArea is not None:
            self._SideB_HostControlArea._SideB_TieLines.append(self)

    SideB_HostControlArea = property(getSideB_HostControlArea, setSideB_HostControlArea)

    def getSideA_SubControlArea(self):
        """The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._SideA_SubControlArea

    def setSideA_SubControlArea(self, value):
        if self._SideA_SubControlArea is not None:
            filtered = [x for x in self.SideA_SubControlArea.SideA_TieLines if x != self]
            self._SideA_SubControlArea._SideA_TieLines = filtered

        self._SideA_SubControlArea = value
        if self._SideA_SubControlArea is not None:
            self._SideA_SubControlArea._SideA_TieLines.append(self)

    SideA_SubControlArea = property(getSideA_SubControlArea, setSideA_SubControlArea)

    def getCustomerConsumer(self):
        """A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        """
        return self._CustomerConsumer

    def setCustomerConsumer(self, value):
        if self._CustomerConsumer is not None:
            filtered = [x for x in self.CustomerConsumer.TieLines if x != self]
            self._CustomerConsumer._TieLines = filtered

        self._CustomerConsumer = value
        if self._CustomerConsumer is not None:
            self._CustomerConsumer._TieLines.append(self)

    CustomerConsumer = property(getCustomerConsumer, setCustomerConsumer)

    def getSideB_SubControlArea(self):
        """The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._SideB_SubControlArea

    def setSideB_SubControlArea(self, value):
        if self._SideB_SubControlArea is not None:
            filtered = [x for x in self.SideB_SubControlArea.SideB_TieLines if x != self]
            self._SideB_SubControlArea._SideB_TieLines = filtered

        self._SideB_SubControlArea = value
        if self._SideB_SubControlArea is not None:
            self._SideB_SubControlArea._SideB_TieLines.append(self)

    SideB_SubControlArea = property(getSideB_SubControlArea, setSideB_SubControlArea)

    def getDynamicEnergyTransaction(self):
        """A dynamic energy transaction can act as a pseudo tie line.
        """
        return self._DynamicEnergyTransaction

    def setDynamicEnergyTransaction(self, value):
        if self._DynamicEnergyTransaction is not None:
            filtered = [x for x in self.DynamicEnergyTransaction.TieLines if x != self]
            self._DynamicEnergyTransaction._TieLines = filtered

        self._DynamicEnergyTransaction = value
        if self._DynamicEnergyTransaction is not None:
            self._DynamicEnergyTransaction._TieLines.append(self)

    DynamicEnergyTransaction = property(getDynamicEnergyTransaction, setDynamicEnergyTransaction)

    def getControlAreaOperators(self):
        """A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
        """
        return self._ControlAreaOperators

    def setControlAreaOperators(self, value):
        for p in self._ControlAreaOperators:
            filtered = [q for q in p.TieLines if q != self]
            self._ControlAreaOperators._TieLines = filtered
        for r in value:
            if self not in r._TieLines:
                r._TieLines.append(self)
        self._ControlAreaOperators = value

    ControlAreaOperators = property(getControlAreaOperators, setControlAreaOperators)

    def addControlAreaOperators(self, *ControlAreaOperators):
        for obj in ControlAreaOperators:
            if self not in obj._TieLines:
                obj._TieLines.append(self)
            self._ControlAreaOperators.append(obj)

    def removeControlAreaOperators(self, *ControlAreaOperators):
        for obj in ControlAreaOperators:
            if self in obj._TieLines:
                obj._TieLines.remove(self)
            self._ControlAreaOperators.remove(obj)

