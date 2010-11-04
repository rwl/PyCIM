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

from CIM14v13.IEC61968.Assets.ElectricalInfo import ElectricalInfo

class CurrentTransformerInfo(ElectricalInfo):
    """Used to define either the required additional electrical properties of a type of Current Transformer (CT) or a CT Model.
    """

    def __init__(self, tertiaryFlsRating=0.0, secondaryFlsRating=0.0, primaryFlsRating=0.0, CurrentTransformerTypeAsset=None, secondaryRatio=None, CurrentTransformerAssets=None, CurrentTransformerAssertModels=None, primaryRatio=None, tertiaryRatio=None, *args, **kw_args):
        """Initializes a new 'CurrentTransformerInfo' instance.

        @param tertiaryFlsRating: Full load secondary (FLS) rating for tertiary winding. 
        @param secondaryFlsRating: Full load secondary (FLS) rating for secondary winding. 
        @param primaryFlsRating: Full load secondary (FLS) rating for primary winding. 
        @param CurrentTransformerTypeAsset:
        @param secondaryRatio: Ratio for the secondary winding tap changer.
        @param CurrentTransformerAssets:
        @param CurrentTransformerAssertModels:
        @param primaryRatio: Ratio for the primary winding tap changer.
        @param tertiaryRatio: Ratio for the tertiary winding tap changer.
        """
        #: Full load secondary (FLS) rating for tertiary winding.
        self.tertiaryFlsRating = tertiaryFlsRating

        #: Full load secondary (FLS) rating for secondary winding.
        self.secondaryFlsRating = secondaryFlsRating

        #: Full load secondary (FLS) rating for primary winding.
        self.primaryFlsRating = primaryFlsRating

        self._CurrentTransformerTypeAsset = None
        self.CurrentTransformerTypeAsset = CurrentTransformerTypeAsset

        self.secondaryRatio = secondaryRatio

        self._CurrentTransformerAssets = []
        self.CurrentTransformerAssets = [] if CurrentTransformerAssets is None else CurrentTransformerAssets

        self._CurrentTransformerAssertModels = []
        self.CurrentTransformerAssertModels = [] if CurrentTransformerAssertModels is None else CurrentTransformerAssertModels

        self.primaryRatio = primaryRatio

        self.tertiaryRatio = tertiaryRatio

        super(CurrentTransformerInfo, self).__init__(*args, **kw_args)

    def getCurrentTransformerTypeAsset(self):
        
        return self._CurrentTransformerTypeAsset

    def setCurrentTransformerTypeAsset(self, value):
        if self._CurrentTransformerTypeAsset is not None:
            self._CurrentTransformerTypeAsset._CurrentTransformerInfo = None

        self._CurrentTransformerTypeAsset = value
        if self._CurrentTransformerTypeAsset is not None:
            self._CurrentTransformerTypeAsset._CurrentTransformerInfo = self

    CurrentTransformerTypeAsset = property(getCurrentTransformerTypeAsset, setCurrentTransformerTypeAsset)

    # Ratio for the secondary winding tap changer.
    secondaryRatio = None

    def getCurrentTransformerAssets(self):
        
        return self._CurrentTransformerAssets

    def setCurrentTransformerAssets(self, value):
        for x in self._CurrentTransformerAssets:
            x._CurrentTransformerInfo = None
        for y in value:
            y._CurrentTransformerInfo = self
        self._CurrentTransformerAssets = value

    CurrentTransformerAssets = property(getCurrentTransformerAssets, setCurrentTransformerAssets)

    def addCurrentTransformerAssets(self, *CurrentTransformerAssets):
        for obj in CurrentTransformerAssets:
            obj._CurrentTransformerInfo = self
            self._CurrentTransformerAssets.append(obj)

    def removeCurrentTransformerAssets(self, *CurrentTransformerAssets):
        for obj in CurrentTransformerAssets:
            obj._CurrentTransformerInfo = None
            self._CurrentTransformerAssets.remove(obj)

    def getCurrentTransformerAssertModels(self):
        
        return self._CurrentTransformerAssertModels

    def setCurrentTransformerAssertModels(self, value):
        for x in self._CurrentTransformerAssertModels:
            x._CurrentTransformerInfo = None
        for y in value:
            y._CurrentTransformerInfo = self
        self._CurrentTransformerAssertModels = value

    CurrentTransformerAssertModels = property(getCurrentTransformerAssertModels, setCurrentTransformerAssertModels)

    def addCurrentTransformerAssertModels(self, *CurrentTransformerAssertModels):
        for obj in CurrentTransformerAssertModels:
            obj._CurrentTransformerInfo = self
            self._CurrentTransformerAssertModels.append(obj)

    def removeCurrentTransformerAssertModels(self, *CurrentTransformerAssertModels):
        for obj in CurrentTransformerAssertModels:
            obj._CurrentTransformerInfo = None
            self._CurrentTransformerAssertModels.remove(obj)

    # Ratio for the primary winding tap changer.
    primaryRatio = None

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = None

