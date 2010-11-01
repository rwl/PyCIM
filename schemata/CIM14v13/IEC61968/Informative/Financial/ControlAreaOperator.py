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

class ControlAreaOperator(ErpOrganisation):
    """Operates the Control Area. Approves and implements energy transactions. Verifies both Inter-Control Area and Intra-Control Area transactions for the power system before granting approval (and implementing) the transactions.
    """

    def __init__(self, AncillaryService=None, ControlledBy=None, TieLines=None, *args, **kw_args):
        """Initializes a new 'ControlAreaOperator' instance.

        @param AncillaryService: Sale of ancillary services provided by ControlAreaOperators.
        @param ControlledBy: A ControlAreaCompany controls a ControlArea.
        @param TieLines: A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
        """
        self._AncillaryService = []
        self.AncillaryService = [] if AncillaryService is None else AncillaryService

        self._ControlledBy = None
        self.ControlledBy = ControlledBy

        self._TieLines = []
        self.TieLines = [] if TieLines is None else TieLines

        super(ControlAreaOperator, self).__init__(*args, **kw_args)

    def getAncillaryService(self):
        """Sale of ancillary services provided by ControlAreaOperators.
        """
        return self._AncillaryService

    def setAncillaryService(self, value):
        for x in self._AncillaryService:
            x._ControlAreaOperator = None
        for y in value:
            y._ControlAreaOperator = self
        self._AncillaryService = value

    AncillaryService = property(getAncillaryService, setAncillaryService)

    def addAncillaryService(self, *AncillaryService):
        for obj in AncillaryService:
            obj._ControlAreaOperator = self
            self._AncillaryService.append(obj)

    def removeAncillaryService(self, *AncillaryService):
        for obj in AncillaryService:
            obj._ControlAreaOperator = None
            self._AncillaryService.remove(obj)

    def getControlledBy(self):
        """A ControlAreaCompany controls a ControlArea.
        """
        return self._ControlledBy

    def setControlledBy(self, value):
        if self._ControlledBy is not None:
            self._ControlledBy._Controls = None

        self._ControlledBy = value
        if self._ControlledBy is not None:
            self._ControlledBy._Controls = self

    ControlledBy = property(getControlledBy, setControlledBy)

    def getTieLines(self):
        """A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
        """
        return self._TieLines

    def setTieLines(self, value):
        for p in self._TieLines:
            filtered = [q for q in p.ControlAreaOperators if q != self]
            self._TieLines._ControlAreaOperators = filtered
        for r in value:
            if self not in r._ControlAreaOperators:
                r._ControlAreaOperators.append(self)
        self._TieLines = value

    TieLines = property(getTieLines, setTieLines)

    def addTieLines(self, *TieLines):
        for obj in TieLines:
            if self not in obj._ControlAreaOperators:
                obj._ControlAreaOperators.append(self)
            self._TieLines.append(obj)

    def removeTieLines(self, *TieLines):
        for obj in TieLines:
            if self in obj._ControlAreaOperators:
                obj._ControlAreaOperators.remove(self)
            self._TieLines.remove(obj)

