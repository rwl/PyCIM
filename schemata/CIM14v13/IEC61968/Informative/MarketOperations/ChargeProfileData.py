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

class ChargeProfileData(Element):

    def __init__(self, sequence=0, value=0.0, timeStamp='', BillDeterminant=None, ChargeProfile=None, **kw_args):
        """Initializes a new 'ChargeProfileData' instance.

        @param sequence: The sequence number of the profile. 
        @param value: The value of an interval given a profile type (amount, price, or quantity), subject to the UOM. 
        @param timeStamp: The date and time of an interval. 
        @param BillDeterminant:
        @param ChargeProfile:
        """
        #: The sequence number of the profile.
        self.sequence = sequence

        #: The value of an interval given a profile type (amount, price, or quantity), subject to the UOM.
        self.value = value

        #: The date and time of an interval.
        self.timeStamp = timeStamp

        self._BillDeterminant = None
        self.BillDeterminant = BillDeterminant

        self._ChargeProfile = None
        self.ChargeProfile = ChargeProfile

        super(ChargeProfileData, self).__init__(**kw_args)

    def getBillDeterminant(self):
        
        return self._BillDeterminant

    def setBillDeterminant(self, value):
        if self._BillDeterminant is not None:
            filtered = [x for x in self.BillDeterminant.ChargeProfileData if x != self]
            self._BillDeterminant._ChargeProfileData = filtered

        self._BillDeterminant = value
        if self._BillDeterminant is not None:
            self._BillDeterminant._ChargeProfileData.append(self)

    BillDeterminant = property(getBillDeterminant, setBillDeterminant)

    def getChargeProfile(self):
        
        return self._ChargeProfile

    def setChargeProfile(self, value):
        if self._ChargeProfile is not None:
            filtered = [x for x in self.ChargeProfile.ChargeProfileData if x != self]
            self._ChargeProfile._ChargeProfileData = filtered

        self._ChargeProfile = value
        if self._ChargeProfile is not None:
            self._ChargeProfile._ChargeProfileData.append(self)

    ChargeProfile = property(getChargeProfile, setChargeProfile)

