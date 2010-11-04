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

from CIM14v13.IEC61968.Informative.EnergyScheduling.Profile import Profile

class ChargeProfile(Profile):
    """A type of profile for financial charges
    """

    def __init__(self, unitOfMeasure='', frequency='', numberInterval=0, type='', BillDeterminant=None, PassTroughBill=None, ChargeProfileData=None, *args, **kw_args):
        """Initializes a new 'ChargeProfile' instance.

        @param unitOfMeasure: The unit of measure applied to the value attribute of the profile data. 
        @param frequency: The calculation frequency, daily or monthly. 
        @param numberInterval: The number of intervals in the profile data. 
        @param type: The type of profile.  It could be amount, price, or quantity. 
        @param BillDeterminant:
        @param PassTroughBill:
        @param ChargeProfileData:
        """
        #: The unit of measure applied to the value attribute of the profile data.
        self.unitOfMeasure = unitOfMeasure

        #: The calculation frequency, daily or monthly.
        self.frequency = frequency

        #: The number of intervals in the profile data.
        self.numberInterval = numberInterval

        #: The type of profile.  It could be amount, price, or quantity.
        self.type = type

        self._BillDeterminant = None
        self.BillDeterminant = BillDeterminant

        self._PassTroughBill = None
        self.PassTroughBill = PassTroughBill

        self._ChargeProfileData = []
        self.ChargeProfileData = [] if ChargeProfileData is None else ChargeProfileData

        super(ChargeProfile, self).__init__(*args, **kw_args)

    def getBillDeterminant(self):
        
        return self._BillDeterminant

    def setBillDeterminant(self, value):
        if self._BillDeterminant is not None:
            self._BillDeterminant._ChargeProfile = None

        self._BillDeterminant = value
        if self._BillDeterminant is not None:
            self._BillDeterminant._ChargeProfile = self

    BillDeterminant = property(getBillDeterminant, setBillDeterminant)

    def getPassTroughBill(self):
        
        return self._PassTroughBill

    def setPassTroughBill(self, value):
        if self._PassTroughBill is not None:
            filtered = [x for x in self.PassTroughBill.ChargeProfiles if x != self]
            self._PassTroughBill._ChargeProfiles = filtered

        self._PassTroughBill = value
        if self._PassTroughBill is not None:
            self._PassTroughBill._ChargeProfiles.append(self)

    PassTroughBill = property(getPassTroughBill, setPassTroughBill)

    def getChargeProfileData(self):
        
        return self._ChargeProfileData

    def setChargeProfileData(self, value):
        for x in self._ChargeProfileData:
            x._ChargeProfile = None
        for y in value:
            y._ChargeProfile = self
        self._ChargeProfileData = value

    ChargeProfileData = property(getChargeProfileData, setChargeProfileData)

    def addChargeProfileData(self, *ChargeProfileData):
        for obj in ChargeProfileData:
            obj._ChargeProfile = self
            self._ChargeProfileData.append(obj)

    def removeChargeProfileData(self, *ChargeProfileData):
        for obj in ChargeProfileData:
            obj._ChargeProfile = None
            self._ChargeProfileData.remove(obj)

