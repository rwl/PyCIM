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

class Pnode(IdentifiedObject):
    """A pricing node is directly associated with a connectivity node.  It is a pricing location for which market participants submit their bids, offers, buy/sell CRRs, and settle.
    """

    def __init__(self, usage='', isPublic=False, beginPeriod='', endPeriod='', type='', ConnectivityNode=None, RTO=None, DeliveryTransactionBids=None, Measurements=None, ReceiptTransactionBids=None, FTRs=None, RegisteredResources=None, PnodeClearing=None, **kw_args):
        """Initializes a new 'Pnode' instance.

        @param usage: Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub' 
        @param isPublic: True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions 
        @param beginPeriod: Start date-time of the period in which the price node definition is valid. 
        @param endPeriod: End date-time of the period in which the price node definition is valid 
        @param type: Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B) 
        @param ConnectivityNode:
        @param RTO:
        @param DeliveryTransactionBids:
        @param Measurements:
        @param ReceiptTransactionBids:
        @param FTRs:
        @param RegisteredResources: A registered resource injects power at one or more connectivity nodes related to a pnode
        @param PnodeClearing:
        """
        #: Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub'
        self.usage = usage

        #: True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions
        self.isPublic = isPublic

        #: Start date-time of the period in which the price node definition is valid.
        self.beginPeriod = beginPeriod

        #: End date-time of the period in which the price node definition is valid
        self.endPeriod = endPeriod

        #: Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B)
        self.type = type

        self._ConnectivityNode = None
        self.ConnectivityNode = ConnectivityNode

        self._RTO = None
        self.RTO = RTO

        self._DeliveryTransactionBids = []
        self.DeliveryTransactionBids = [] if DeliveryTransactionBids is None else DeliveryTransactionBids

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ReceiptTransactionBids = []
        self.ReceiptTransactionBids = [] if ReceiptTransactionBids is None else ReceiptTransactionBids

        self._FTRs = []
        self.FTRs = [] if FTRs is None else FTRs

        self._RegisteredResources = []
        self.RegisteredResources = [] if RegisteredResources is None else RegisteredResources

        self._PnodeClearing = None
        self.PnodeClearing = PnodeClearing

        super(Pnode, self).__init__(**kw_args)

    def getConnectivityNode(self):
        
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        if self._ConnectivityNode is not None:
            self._ConnectivityNode._Pnode = None

        self._ConnectivityNode = value
        if self._ConnectivityNode is not None:
            self._ConnectivityNode._Pnode = self

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

    def getRTO(self):
        
        return self._RTO

    def setRTO(self, value):
        if self._RTO is not None:
            filtered = [x for x in self.RTO.Pnodes if x != self]
            self._RTO._Pnodes = filtered

        self._RTO = value
        if self._RTO is not None:
            self._RTO._Pnodes.append(self)

    RTO = property(getRTO, setRTO)

    def getDeliveryTransactionBids(self):
        
        return self._DeliveryTransactionBids

    def setDeliveryTransactionBids(self, value):
        for x in self._DeliveryTransactionBids:
            x._Delivery_Pnode = None
        for y in value:
            y._Delivery_Pnode = self
        self._DeliveryTransactionBids = value

    DeliveryTransactionBids = property(getDeliveryTransactionBids, setDeliveryTransactionBids)

    def addDeliveryTransactionBids(self, *DeliveryTransactionBids):
        for obj in DeliveryTransactionBids:
            obj._Delivery_Pnode = self
            self._DeliveryTransactionBids.append(obj)

    def removeDeliveryTransactionBids(self, *DeliveryTransactionBids):
        for obj in DeliveryTransactionBids:
            obj._Delivery_Pnode = None
            self._DeliveryTransactionBids.remove(obj)

    def getMeasurements(self):
        
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x._Pnode = None
        for y in value:
            y._Pnode = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Pnode = self
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Pnode = None
            self._Measurements.remove(obj)

    def getReceiptTransactionBids(self):
        
        return self._ReceiptTransactionBids

    def setReceiptTransactionBids(self, value):
        for x in self._ReceiptTransactionBids:
            x._Receipt_Pnode = None
        for y in value:
            y._Receipt_Pnode = self
        self._ReceiptTransactionBids = value

    ReceiptTransactionBids = property(getReceiptTransactionBids, setReceiptTransactionBids)

    def addReceiptTransactionBids(self, *ReceiptTransactionBids):
        for obj in ReceiptTransactionBids:
            obj._Receipt_Pnode = self
            self._ReceiptTransactionBids.append(obj)

    def removeReceiptTransactionBids(self, *ReceiptTransactionBids):
        for obj in ReceiptTransactionBids:
            obj._Receipt_Pnode = None
            self._ReceiptTransactionBids.remove(obj)

    def getFTRs(self):
        
        return self._FTRs

    def setFTRs(self, value):
        for p in self._FTRs:
            filtered = [q for q in p.Pnodes if q != self]
            self._FTRs._Pnodes = filtered
        for r in value:
            if self not in r._Pnodes:
                r._Pnodes.append(self)
        self._FTRs = value

    FTRs = property(getFTRs, setFTRs)

    def addFTRs(self, *FTRs):
        for obj in FTRs:
            if self not in obj._Pnodes:
                obj._Pnodes.append(self)
            self._FTRs.append(obj)

    def removeFTRs(self, *FTRs):
        for obj in FTRs:
            if self in obj._Pnodes:
                obj._Pnodes.remove(self)
            self._FTRs.remove(obj)

    def getRegisteredResources(self):
        """A registered resource injects power at one or more connectivity nodes related to a pnode
        """
        return self._RegisteredResources

    def setRegisteredResources(self, value):
        for x in self._RegisteredResources:
            x._Pnode = None
        for y in value:
            y._Pnode = self
        self._RegisteredResources = value

    RegisteredResources = property(getRegisteredResources, setRegisteredResources)

    def addRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            obj._Pnode = self
            self._RegisteredResources.append(obj)

    def removeRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            obj._Pnode = None
            self._RegisteredResources.remove(obj)

    def getPnodeClearing(self):
        
        return self._PnodeClearing

    def setPnodeClearing(self, value):
        if self._PnodeClearing is not None:
            self._PnodeClearing._Pnode = None

        self._PnodeClearing = value
        if self._PnodeClearing is not None:
            self._PnodeClearing._Pnode = self

    PnodeClearing = property(getPnodeClearing, setPnodeClearing)

