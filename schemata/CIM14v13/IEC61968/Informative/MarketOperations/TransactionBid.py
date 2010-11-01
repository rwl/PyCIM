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

from CIM14v13.IEC61968.Informative.MarketOperations.Bid import Bid

class TransactionBid(Bid):
    """Bilateral or scheduled transactions for energy and ancillary services considered by market clearing process
    """

    def __init__(self, Delivery_Pnode=None, Receipt_Pnode=None, EnergyTransId=None, EnergyProfiles=None, *args, **kw_args):
        """Initializes a new 'TransactionBid' instance.

        @param Delivery_Pnode:
        @param Receipt_Pnode:
        @param EnergyTransId:
        @param EnergyProfiles:
        """
        self._Delivery_Pnode = None
        self.Delivery_Pnode = Delivery_Pnode

        self._Receipt_Pnode = None
        self.Receipt_Pnode = Receipt_Pnode

        self._EnergyTransId = None
        self.EnergyTransId = EnergyTransId

        self._EnergyProfiles = []
        self.EnergyProfiles = [] if EnergyProfiles is None else EnergyProfiles

        super(TransactionBid, self).__init__(*args, **kw_args)

    def getDelivery_Pnode(self):
        
        return self._Delivery_Pnode

    def setDelivery_Pnode(self, value):
        if self._Delivery_Pnode is not None:
            filtered = [x for x in self.Delivery_Pnode.DeliveryTransactionBids if x != self]
            self._Delivery_Pnode._DeliveryTransactionBids = filtered

        self._Delivery_Pnode = value
        if self._Delivery_Pnode is not None:
            self._Delivery_Pnode._DeliveryTransactionBids.append(self)

    Delivery_Pnode = property(getDelivery_Pnode, setDelivery_Pnode)

    def getReceipt_Pnode(self):
        
        return self._Receipt_Pnode

    def setReceipt_Pnode(self, value):
        if self._Receipt_Pnode is not None:
            filtered = [x for x in self.Receipt_Pnode.ReceiptTransactionBids if x != self]
            self._Receipt_Pnode._ReceiptTransactionBids = filtered

        self._Receipt_Pnode = value
        if self._Receipt_Pnode is not None:
            self._Receipt_Pnode._ReceiptTransactionBids.append(self)

    Receipt_Pnode = property(getReceipt_Pnode, setReceipt_Pnode)

    def getEnergyTransId(self):
        
        return self._EnergyTransId

    def setEnergyTransId(self, value):
        if self._EnergyTransId is not None:
            filtered = [x for x in self.EnergyTransId.EnergyTransId if x != self]
            self._EnergyTransId._EnergyTransId = filtered

        self._EnergyTransId = value
        if self._EnergyTransId is not None:
            self._EnergyTransId._EnergyTransId.append(self)

    EnergyTransId = property(getEnergyTransId, setEnergyTransId)

    def getEnergyProfiles(self):
        
        return self._EnergyProfiles

    def setEnergyProfiles(self, value):
        for x in self._EnergyProfiles:
            x._TransactionBid = None
        for y in value:
            y._TransactionBid = self
        self._EnergyProfiles = value

    EnergyProfiles = property(getEnergyProfiles, setEnergyProfiles)

    def addEnergyProfiles(self, *EnergyProfiles):
        for obj in EnergyProfiles:
            obj._TransactionBid = self
            self._EnergyProfiles.append(obj)

    def removeEnergyProfiles(self, *EnergyProfiles):
        for obj in EnergyProfiles:
            obj._TransactionBid = None
            self._EnergyProfiles.remove(obj)

