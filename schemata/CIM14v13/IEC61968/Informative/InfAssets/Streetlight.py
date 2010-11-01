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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class Streetlight(ElectricalAsset):
    """Streetlight asset.
    """

    def __init__(self, lampKind='highPressureSodium', lightRating=0.0, armLength=0.0, AttachedToPole=None, StreetlightAssetModel=None, *args, **kw_args):
        """Initializes a new 'Streetlight' instance.

        @param lampKind: Lamp kind currently installed. Values are: "highPressureSodium", "other", "metalHalide", "mercuryVapor"
        @param lightRating: Actual power rating of light. 
        @param armLength: Length of arm of this specific asset. Note that a new light may be placed on an existing arm. 
        @param AttachedToPole: Streetlight(s) may be attached to a pole.
        @param StreetlightAssetModel:
        """
        #: Lamp kind currently installed. Values are: "highPressureSodium", "other", "metalHalide", "mercuryVapor"
        self.lampKind = lampKind

        #: Actual power rating of light. 
        self.lightRating = lightRating

        #: Length of arm of this specific asset. Note that a new light may be placed on an existing arm. 
        self.armLength = armLength

        self._AttachedToPole = None
        self.AttachedToPole = AttachedToPole

        self._StreetlightAssetModel = None
        self.StreetlightAssetModel = StreetlightAssetModel

        super(Streetlight, self).__init__(*args, **kw_args)

    def getAttachedToPole(self):
        """Streetlight(s) may be attached to a pole.
        """
        return self._AttachedToPole

    def setAttachedToPole(self, value):
        if self._AttachedToPole is not None:
            filtered = [x for x in self.AttachedToPole.SupportStreetlights if x != self]
            self._AttachedToPole._SupportStreetlights = filtered

        self._AttachedToPole = value
        if self._AttachedToPole is not None:
            self._AttachedToPole._SupportStreetlights.append(self)

    AttachedToPole = property(getAttachedToPole, setAttachedToPole)

    def getStreetlightAssetModel(self):
        
        return self._StreetlightAssetModel

    def setStreetlightAssetModel(self, value):
        if self._StreetlightAssetModel is not None:
            filtered = [x for x in self.StreetlightAssetModel.Streetlights if x != self]
            self._StreetlightAssetModel._Streetlights = filtered

        self._StreetlightAssetModel = value
        if self._StreetlightAssetModel is not None:
            self._StreetlightAssetModel._Streetlights.append(self)

    StreetlightAssetModel = property(getStreetlightAssetModel, setStreetlightAssetModel)

