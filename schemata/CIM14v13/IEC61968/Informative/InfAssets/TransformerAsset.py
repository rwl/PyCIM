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

from CIM14v13.IEC61968.Assets.Asset import Asset

class TransformerAsset(Asset):
    """A specific physical (vs. logical) transformer.
    """

    def __init__(self, reconditionedDateTime='', TransformerInfo=None, PowerRatings=None, TransformerObservations=None, TransformerAssetModel=None, **kw_args):
        """Initializes a new 'TransformerAsset' instance.

        @param reconditionedDateTime: Date and time this asset was last reconditioned or had a major overhaul. 
        @param TransformerInfo:
        @param PowerRatings:
        @param TransformerObservations:
        @param TransformerAssetModel:
        """
        #: Date and time this asset was last reconditioned or had a major overhaul.
        self.reconditionedDateTime = reconditionedDateTime

        self._TransformerInfo = None
        self.TransformerInfo = TransformerInfo

        self._PowerRatings = []
        self.PowerRatings = [] if PowerRatings is None else PowerRatings

        self._TransformerObservations = []
        self.TransformerObservations = [] if TransformerObservations is None else TransformerObservations

        self._TransformerAssetModel = None
        self.TransformerAssetModel = TransformerAssetModel

        super(TransformerAsset, self).__init__(**kw_args)

    def getTransformerInfo(self):
        
        return self._TransformerInfo

    def setTransformerInfo(self, value):
        if self._TransformerInfo is not None:
            filtered = [x for x in self.TransformerInfo.TransformerAssets if x != self]
            self._TransformerInfo._TransformerAssets = filtered

        self._TransformerInfo = value
        if self._TransformerInfo is not None:
            self._TransformerInfo._TransformerAssets.append(self)

    TransformerInfo = property(getTransformerInfo, setTransformerInfo)

    def getPowerRatings(self):
        
        return self._PowerRatings

    def setPowerRatings(self, value):
        for p in self._PowerRatings:
            filtered = [q for q in p.TransformerAssets if q != self]
            self._PowerRatings._TransformerAssets = filtered
        for r in value:
            if self not in r._TransformerAssets:
                r._TransformerAssets.append(self)
        self._PowerRatings = value

    PowerRatings = property(getPowerRatings, setPowerRatings)

    def addPowerRatings(self, *PowerRatings):
        for obj in PowerRatings:
            if self not in obj._TransformerAssets:
                obj._TransformerAssets.append(self)
            self._PowerRatings.append(obj)

    def removePowerRatings(self, *PowerRatings):
        for obj in PowerRatings:
            if self in obj._TransformerAssets:
                obj._TransformerAssets.remove(self)
            self._PowerRatings.remove(obj)

    def getTransformerObservations(self):
        
        return self._TransformerObservations

    def setTransformerObservations(self, value):
        for x in self._TransformerObservations:
            x._TransformerAsset = None
        for y in value:
            y._TransformerAsset = self
        self._TransformerObservations = value

    TransformerObservations = property(getTransformerObservations, setTransformerObservations)

    def addTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            obj._TransformerAsset = self
            self._TransformerObservations.append(obj)

    def removeTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            obj._TransformerAsset = None
            self._TransformerObservations.remove(obj)

    def getTransformerAssetModel(self):
        
        return self._TransformerAssetModel

    def setTransformerAssetModel(self, value):
        if self._TransformerAssetModel is not None:
            filtered = [x for x in self.TransformerAssetModel.TransformerAssets if x != self]
            self._TransformerAssetModel._TransformerAssets = filtered

        self._TransformerAssetModel = value
        if self._TransformerAssetModel is not None:
            self._TransformerAssetModel._TransformerAssets.append(self)

    TransformerAssetModel = property(getTransformerAssetModel, setTransformerAssetModel)

