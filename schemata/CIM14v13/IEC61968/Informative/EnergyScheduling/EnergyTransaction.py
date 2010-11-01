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

from CIM14v13.IEC61968.Common.Document import Document

class EnergyTransaction(Document):
    """Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.
    """

    def __init__(self, receiptPointP=0.0, state=None, energyMin=0.0, firmInterchangeFlag=False, congestChargeMax=0.0, reason='', deliveryPointP=0.0, CurtailmentProfiles=None, Export_SubControlArea=None, EnergyTransId=None, Import_SubControlArea=None, EnergyPriceCurves=None, LossProfiles=None, EnergyProfiles=None, EnergyProduct=None, *args, **kw_args):
        """Initializes a new 'EnergyTransaction' instance.

        @param receiptPointP: Receipt point active power 
        @param state: { Approve | Deny | Study } 
        @param energyMin: Transaction minimum active power if dispatchable 
        @param firmInterchangeFlag: Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences. 
        @param congestChargeMax: Maximum congestion charges in monetary units 
        @param reason: 
        @param deliveryPointP: Delivery point active power 
        @param CurtailmentProfiles: An EnergyTransaction may be curtailed by any of the participating entities.
        @param Export_SubControlArea: Energy is transferred between interchange areas
        @param EnergyTransId:
        @param Import_SubControlArea: Energy is transferred between interchange areas
        @param EnergyPriceCurves:
        @param LossProfiles: An EnergyTransaction may have a LossProfile.
        @param EnergyProfiles: An EnergyTransaction must have at least one EnergyProfile.
        @param EnergyProduct: The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        #: Receipt point active power 
        self.receiptPointP = receiptPointP

        #: { Approve | Deny | Study } 
        self.state = state

        #: Transaction minimum active power if dispatchable 
        self.energyMin = energyMin

        #: Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences. 
        self.firmInterchangeFlag = firmInterchangeFlag

        #: Maximum congestion charges in monetary units 
        self.congestChargeMax = congestChargeMax

 
        self.reason = reason

        #: Delivery point active power 
        self.deliveryPointP = deliveryPointP

        self._CurtailmentProfiles = []
        self.CurtailmentProfiles = [] if CurtailmentProfiles is None else CurtailmentProfiles

        self._Export_SubControlArea = None
        self.Export_SubControlArea = Export_SubControlArea

        self._EnergyTransId = []
        self.EnergyTransId = [] if EnergyTransId is None else EnergyTransId

        self._Import_SubControlArea = None
        self.Import_SubControlArea = Import_SubControlArea

        self._EnergyPriceCurves = []
        self.EnergyPriceCurves = [] if EnergyPriceCurves is None else EnergyPriceCurves

        self._LossProfiles = []
        self.LossProfiles = [] if LossProfiles is None else LossProfiles

        self._EnergyProfiles = []
        self.EnergyProfiles = [] if EnergyProfiles is None else EnergyProfiles

        self._EnergyProduct = None
        self.EnergyProduct = EnergyProduct

        super(EnergyTransaction, self).__init__(*args, **kw_args)

    def getCurtailmentProfiles(self):
        """An EnergyTransaction may be curtailed by any of the participating entities.
        """
        return self._CurtailmentProfiles

    def setCurtailmentProfiles(self, value):
        for x in self._CurtailmentProfiles:
            x._EnergyTransaction = None
        for y in value:
            y._EnergyTransaction = self
        self._CurtailmentProfiles = value

    CurtailmentProfiles = property(getCurtailmentProfiles, setCurtailmentProfiles)

    def addCurtailmentProfiles(self, *CurtailmentProfiles):
        for obj in CurtailmentProfiles:
            obj._EnergyTransaction = self
            self._CurtailmentProfiles.append(obj)

    def removeCurtailmentProfiles(self, *CurtailmentProfiles):
        for obj in CurtailmentProfiles:
            obj._EnergyTransaction = None
            self._CurtailmentProfiles.remove(obj)

    def getExport_SubControlArea(self):
        """Energy is transferred between interchange areas
        """
        return self._Export_SubControlArea

    def setExport_SubControlArea(self, value):
        if self._Export_SubControlArea is not None:
            filtered = [x for x in self.Export_SubControlArea.Export_EnergyTransactions if x != self]
            self._Export_SubControlArea._Export_EnergyTransactions = filtered

        self._Export_SubControlArea = value
        if self._Export_SubControlArea is not None:
            self._Export_SubControlArea._Export_EnergyTransactions.append(self)

    Export_SubControlArea = property(getExport_SubControlArea, setExport_SubControlArea)

    def getEnergyTransId(self):
        
        return self._EnergyTransId

    def setEnergyTransId(self, value):
        for x in self._EnergyTransId:
            x._EnergyTransId = None
        for y in value:
            y._EnergyTransId = self
        self._EnergyTransId = value

    EnergyTransId = property(getEnergyTransId, setEnergyTransId)

    def addEnergyTransId(self, *EnergyTransId):
        for obj in EnergyTransId:
            obj._EnergyTransId = self
            self._EnergyTransId.append(obj)

    def removeEnergyTransId(self, *EnergyTransId):
        for obj in EnergyTransId:
            obj._EnergyTransId = None
            self._EnergyTransId.remove(obj)

    def getImport_SubControlArea(self):
        """Energy is transferred between interchange areas
        """
        return self._Import_SubControlArea

    def setImport_SubControlArea(self, value):
        if self._Import_SubControlArea is not None:
            filtered = [x for x in self.Import_SubControlArea.Import_EnergyTransactions if x != self]
            self._Import_SubControlArea._Import_EnergyTransactions = filtered

        self._Import_SubControlArea = value
        if self._Import_SubControlArea is not None:
            self._Import_SubControlArea._Import_EnergyTransactions.append(self)

    Import_SubControlArea = property(getImport_SubControlArea, setImport_SubControlArea)

    def getEnergyPriceCurves(self):
        
        return self._EnergyPriceCurves

    def setEnergyPriceCurves(self, value):
        for p in self._EnergyPriceCurves:
            filtered = [q for q in p.EnergyTransactions if q != self]
            self._EnergyPriceCurves._EnergyTransactions = filtered
        for r in value:
            if self not in r._EnergyTransactions:
                r._EnergyTransactions.append(self)
        self._EnergyPriceCurves = value

    EnergyPriceCurves = property(getEnergyPriceCurves, setEnergyPriceCurves)

    def addEnergyPriceCurves(self, *EnergyPriceCurves):
        for obj in EnergyPriceCurves:
            if self not in obj._EnergyTransactions:
                obj._EnergyTransactions.append(self)
            self._EnergyPriceCurves.append(obj)

    def removeEnergyPriceCurves(self, *EnergyPriceCurves):
        for obj in EnergyPriceCurves:
            if self in obj._EnergyTransactions:
                obj._EnergyTransactions.remove(self)
            self._EnergyPriceCurves.remove(obj)

    def getLossProfiles(self):
        """An EnergyTransaction may have a LossProfile.
        """
        return self._LossProfiles

    def setLossProfiles(self, value):
        for x in self._LossProfiles:
            x._EnergyTransaction = None
        for y in value:
            y._EnergyTransaction = self
        self._LossProfiles = value

    LossProfiles = property(getLossProfiles, setLossProfiles)

    def addLossProfiles(self, *LossProfiles):
        for obj in LossProfiles:
            obj._EnergyTransaction = self
            self._LossProfiles.append(obj)

    def removeLossProfiles(self, *LossProfiles):
        for obj in LossProfiles:
            obj._EnergyTransaction = None
            self._LossProfiles.remove(obj)

    def getEnergyProfiles(self):
        """An EnergyTransaction must have at least one EnergyProfile.
        """
        return self._EnergyProfiles

    def setEnergyProfiles(self, value):
        for x in self._EnergyProfiles:
            x._EnergyTransaction = None
        for y in value:
            y._EnergyTransaction = self
        self._EnergyProfiles = value

    EnergyProfiles = property(getEnergyProfiles, setEnergyProfiles)

    def addEnergyProfiles(self, *EnergyProfiles):
        for obj in EnergyProfiles:
            obj._EnergyTransaction = self
            self._EnergyProfiles.append(obj)

    def removeEnergyProfiles(self, *EnergyProfiles):
        for obj in EnergyProfiles:
            obj._EnergyTransaction = None
            self._EnergyProfiles.remove(obj)

    def getEnergyProduct(self):
        """The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        return self._EnergyProduct

    def setEnergyProduct(self, value):
        if self._EnergyProduct is not None:
            filtered = [x for x in self.EnergyProduct.EnergyTransactions if x != self]
            self._EnergyProduct._EnergyTransactions = filtered

        self._EnergyProduct = value
        if self._EnergyProduct is not None:
            self._EnergyProduct._EnergyTransactions.append(self)

    EnergyProduct = property(getEnergyProduct, setEnergyProduct)

