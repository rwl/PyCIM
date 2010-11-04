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

class MarketStatementLineItem(IdentifiedObject):
    """An individual line item on a statement.
    """

    def __init__(self, previousISOAmount=0.0, intervalNumber='', netQuantity=0.0, intervalDate='', previousAmount=0.0, netISOAmount=0.0, netPrice=0.0, currentAmount=0.0, netISOQuantity=0.0, previousQuantity=0.0, quantityUOM='', previsouPrice=0.0, previousISOQuantity=0.0, currentISOAmount=0.0, currentQuantity=0.0, currentPrice=0.0, netAmount=0.0, currentISOQuantity=0.0, MarketStatement=None, PassThroughBill=None, ContainerMarketStatementLineItem=None, ComponentMarketStatementLineItem=None, UserAttributes=None, *args, **kw_args):
        """Initializes a new 'MarketStatementLineItem' instance.

        @param previousISOAmount: Previous ISO settlement amount. 
        @param intervalNumber: The number of intervals. 
        @param netQuantity: Net settlement quantity, subject to the UOM. 
        @param intervalDate: The date of which the settlement is run. 
        @param previousAmount: Previous settlement amount. 
        @param netISOAmount: Net ISO settlement amount. 
        @param netPrice: Net settlement price. 
        @param currentAmount: Current settlement amount. 
        @param netISOQuantity: Net ISO settlement quantity. 
        @param previousQuantity: Previous settlement quantity, subject to the UOM. 
        @param quantityUOM: The unit of measure for the quantity element of the line item. 
        @param previsouPrice: Previous settlement price. 
        @param previousISOQuantity: Previous ISO settlement quantity. 
        @param currentISOAmount: Current ISO settlement amount. 
        @param currentQuantity: Current settlement quantity, subject to the UOM. 
        @param currentPrice: Current settlement price. 
        @param netAmount: Net settlement amount. 
        @param currentISOQuantity: Current ISO settlement quantity. 
        @param MarketStatement:
        @param PassThroughBill:
        @param ContainerMarketStatementLineItem:
        @param ComponentMarketStatementLineItem:
        @param UserAttributes:
        """
        #: Previous ISO settlement amount.
        self.previousISOAmount = previousISOAmount

        #: The number of intervals.
        self.intervalNumber = intervalNumber

        #: Net settlement quantity, subject to the UOM.
        self.netQuantity = netQuantity

        #: The date of which the settlement is run.
        self.intervalDate = intervalDate

        #: Previous settlement amount.
        self.previousAmount = previousAmount

        #: Net ISO settlement amount.
        self.netISOAmount = netISOAmount

        #: Net settlement price.
        self.netPrice = netPrice

        #: Current settlement amount.
        self.currentAmount = currentAmount

        #: Net ISO settlement quantity.
        self.netISOQuantity = netISOQuantity

        #: Previous settlement quantity, subject to the UOM.
        self.previousQuantity = previousQuantity

        #: The unit of measure for the quantity element of the line item.
        self.quantityUOM = quantityUOM

        #: Previous settlement price.
        self.previsouPrice = previsouPrice

        #: Previous ISO settlement quantity.
        self.previousISOQuantity = previousISOQuantity

        #: Current ISO settlement amount.
        self.currentISOAmount = currentISOAmount

        #: Current settlement quantity, subject to the UOM.
        self.currentQuantity = currentQuantity

        #: Current settlement price.
        self.currentPrice = currentPrice

        #: Net settlement amount.
        self.netAmount = netAmount

        #: Current ISO settlement quantity.
        self.currentISOQuantity = currentISOQuantity

        self._MarketStatement = None
        self.MarketStatement = MarketStatement

        self._PassThroughBill = None
        self.PassThroughBill = PassThroughBill

        self._ContainerMarketStatementLineItem = None
        self.ContainerMarketStatementLineItem = ContainerMarketStatementLineItem

        self._ComponentMarketStatementLineItem = []
        self.ComponentMarketStatementLineItem = [] if ComponentMarketStatementLineItem is None else ComponentMarketStatementLineItem

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        super(MarketStatementLineItem, self).__init__(*args, **kw_args)

    def getMarketStatement(self):
        
        return self._MarketStatement

    def setMarketStatement(self, value):
        if self._MarketStatement is not None:
            filtered = [x for x in self.MarketStatement.MarketStatementLineItem if x != self]
            self._MarketStatement._MarketStatementLineItem = filtered

        self._MarketStatement = value
        if self._MarketStatement is not None:
            self._MarketStatement._MarketStatementLineItem.append(self)

    MarketStatement = property(getMarketStatement, setMarketStatement)

    def getPassThroughBill(self):
        
        return self._PassThroughBill

    def setPassThroughBill(self, value):
        if self._PassThroughBill is not None:
            self._PassThroughBill._MarketStatementLineItem = None

        self._PassThroughBill = value
        if self._PassThroughBill is not None:
            self._PassThroughBill._MarketStatementLineItem = self

    PassThroughBill = property(getPassThroughBill, setPassThroughBill)

    def getContainerMarketStatementLineItem(self):
        
        return self._ContainerMarketStatementLineItem

    def setContainerMarketStatementLineItem(self, value):
        if self._ContainerMarketStatementLineItem is not None:
            filtered = [x for x in self.ContainerMarketStatementLineItem.ComponentMarketStatementLineItem if x != self]
            self._ContainerMarketStatementLineItem._ComponentMarketStatementLineItem = filtered

        self._ContainerMarketStatementLineItem = value
        if self._ContainerMarketStatementLineItem is not None:
            self._ContainerMarketStatementLineItem._ComponentMarketStatementLineItem.append(self)

    ContainerMarketStatementLineItem = property(getContainerMarketStatementLineItem, setContainerMarketStatementLineItem)

    def getComponentMarketStatementLineItem(self):
        
        return self._ComponentMarketStatementLineItem

    def setComponentMarketStatementLineItem(self, value):
        for x in self._ComponentMarketStatementLineItem:
            x._ContainerMarketStatementLineItem = None
        for y in value:
            y._ContainerMarketStatementLineItem = self
        self._ComponentMarketStatementLineItem = value

    ComponentMarketStatementLineItem = property(getComponentMarketStatementLineItem, setComponentMarketStatementLineItem)

    def addComponentMarketStatementLineItem(self, *ComponentMarketStatementLineItem):
        for obj in ComponentMarketStatementLineItem:
            obj._ContainerMarketStatementLineItem = self
            self._ComponentMarketStatementLineItem.append(obj)

    def removeComponentMarketStatementLineItem(self, *ComponentMarketStatementLineItem):
        for obj in ComponentMarketStatementLineItem:
            obj._ContainerMarketStatementLineItem = None
            self._ComponentMarketStatementLineItem.remove(obj)

    def getUserAttributes(self):
        
        return self._UserAttributes

    def setUserAttributes(self, value):
        for p in self._UserAttributes:
            filtered = [q for q in p.ErpStatementLineItems if q != self]
            self._UserAttributes._ErpStatementLineItems = filtered
        for r in value:
            if self not in r._ErpStatementLineItems:
                r._ErpStatementLineItems.append(self)
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self not in obj._ErpStatementLineItems:
                obj._ErpStatementLineItems.append(self)
            self._UserAttributes.append(obj)

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self in obj._ErpStatementLineItems:
                obj._ErpStatementLineItems.remove(self)
            self._UserAttributes.remove(obj)

