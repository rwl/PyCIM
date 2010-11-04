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

class BillDeterminant(Document):

    def __init__(self, calculationLevel='', precisionLevel='', unitOfMeasure='', configVersion='', numberInterval=0, ChargeProfile=None, ChargeProfileData=None, UserAttributes=None, *args, **kw_args):
        """Initializes a new 'BillDeterminant' instance.

        @param calculationLevel: Level in charge calculation order. 
        @param precisionLevel: The level of precision in the current value. 
        @param unitOfMeasure: The UOM for the current value of the Bill Determinant. 
        @param configVersion: The version of configuration of calculation logic in the settlement. 
        @param numberInterval: Number of intervals of bill determiant in trade day, eg 300 for five minute intervals. 
        @param ChargeProfile:
        @param ChargeProfileData:
        @param UserAttributes:
        """
        #: Level in charge calculation order.
        self.calculationLevel = calculationLevel

        #: The level of precision in the current value.
        self.precisionLevel = precisionLevel

        #: The UOM for the current value of the Bill Determinant.
        self.unitOfMeasure = unitOfMeasure

        #: The version of configuration of calculation logic in the settlement.
        self.configVersion = configVersion

        #: Number of intervals of bill determiant in trade day, eg 300 for five minute intervals.
        self.numberInterval = numberInterval

        self._ChargeProfile = None
        self.ChargeProfile = ChargeProfile

        self._ChargeProfileData = []
        self.ChargeProfileData = [] if ChargeProfileData is None else ChargeProfileData

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        super(BillDeterminant, self).__init__(*args, **kw_args)

    def getChargeProfile(self):
        
        return self._ChargeProfile

    def setChargeProfile(self, value):
        if self._ChargeProfile is not None:
            self._ChargeProfile._BillDeterminant = None

        self._ChargeProfile = value
        if self._ChargeProfile is not None:
            self._ChargeProfile._BillDeterminant = self

    ChargeProfile = property(getChargeProfile, setChargeProfile)

    def getChargeProfileData(self):
        
        return self._ChargeProfileData

    def setChargeProfileData(self, value):
        for x in self._ChargeProfileData:
            x._BillDeterminant = None
        for y in value:
            y._BillDeterminant = self
        self._ChargeProfileData = value

    ChargeProfileData = property(getChargeProfileData, setChargeProfileData)

    def addChargeProfileData(self, *ChargeProfileData):
        for obj in ChargeProfileData:
            obj._BillDeterminant = self
            self._ChargeProfileData.append(obj)

    def removeChargeProfileData(self, *ChargeProfileData):
        for obj in ChargeProfileData:
            obj._BillDeterminant = None
            self._ChargeProfileData.remove(obj)

    def getUserAttributes(self):
        
        return self._UserAttributes

    def setUserAttributes(self, value):
        for p in self._UserAttributes:
            filtered = [q for q in p.BillDeterminants if q != self]
            self._UserAttributes._BillDeterminants = filtered
        for r in value:
            if self not in r._BillDeterminants:
                r._BillDeterminants.append(self)
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self not in obj._BillDeterminants:
                obj._BillDeterminants.append(self)
            self._UserAttributes.append(obj)

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self in obj._BillDeterminants:
                obj._BillDeterminants.remove(self)
            self._UserAttributes.remove(obj)

