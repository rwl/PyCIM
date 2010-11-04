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

from CIM14v13.IEC61968.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation

class CustomerConsumer(ErpOrganisation):
    """The energy buyer in the energy marketplace.
    """

    def __init__(self, ServicePoint=None, TieLines=None, **kw_args):
        """Initializes a new 'CustomerConsumer' instance.

        @param ServicePoint: A CustomerConsumer may have one or more ServicePoints.
        @param TieLines: A  ControlAreaOperator or CustomerConsumer may ring their perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        """
        self._ServicePoint = []
        self.ServicePoint = [] if ServicePoint is None else ServicePoint

        self._TieLines = []
        self.TieLines = [] if TieLines is None else TieLines

        super(CustomerConsumer, self).__init__(**kw_args)

    def getServicePoint(self):
        """A CustomerConsumer may have one or more ServicePoints.
        """
        return self._ServicePoint

    def setServicePoint(self, value):
        for x in self._ServicePoint:
            x._CustomerConsumer = None
        for y in value:
            y._CustomerConsumer = self
        self._ServicePoint = value

    ServicePoint = property(getServicePoint, setServicePoint)

    def addServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._CustomerConsumer = self
            self._ServicePoint.append(obj)

    def removeServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._CustomerConsumer = None
            self._ServicePoint.remove(obj)

    def getTieLines(self):
        """A  ControlAreaOperator or CustomerConsumer may ring their perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        """
        return self._TieLines

    def setTieLines(self, value):
        for x in self._TieLines:
            x._CustomerConsumer = None
        for y in value:
            y._CustomerConsumer = self
        self._TieLines = value

    TieLines = property(getTieLines, setTieLines)

    def addTieLines(self, *TieLines):
        for obj in TieLines:
            obj._CustomerConsumer = self
            self._TieLines.append(obj)

    def removeTieLines(self, *TieLines):
        for obj in TieLines:
            obj._CustomerConsumer = None
            self._TieLines.remove(obj)

