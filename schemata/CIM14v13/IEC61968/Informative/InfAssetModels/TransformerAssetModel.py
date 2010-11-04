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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class TransformerAssetModel(AssetModel):
    """Documentation for a type of a transformer of a particular product model made by a manufacturer.
    """

    def __init__(self, function='other', constructionKind='padmountDeadFront', windingInsulationKind='other', oilPreservationKind='nitrogenBlanket', coreKind='core', autoTransformer=False, reconfigWinding=False, dayOverLoadRating=0.0, altSecondaryNomVoltage=0.0, altPrimaryNomVoltage=0.0, coreCoilsWeight=0.0, solidInsulationWeight=0.0, hourOverLoadRating=0.0, neutralBIL=0.0, TransformerAssets=None, TransformerInfo=None, *args, **kw_args):
        """Initializes a new 'TransformerAssetModel' instance.

        @param function: Function of this transformer. Values are: "other", "voltageRegulator", "secondaryTransformer", "autotransformer", "powerTransformer"
        @param constructionKind: Kind of construction for this transformer. Values are: "padmountDeadFront", "onePhase", "unknown", "valut", "padmounted", "aerial", "underground", "padmountLiveFront", "network", "vaultThreePhase", "subway", "dryType", "padmountLoopThrough", "overhead", "threePhase", "padmountFeedThrough"
        @param windingInsulationKind: Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other Values are: "other", "nomex", "paper", "thermallyUpgradedPaper"
        @param oilPreservationKind: Kind of oil preservation system. Values are: "nitrogenBlanket", "freeBreathing", "conservator", "other"
        @param coreKind: Core kind of this transformer product. Values are: "core", "shell"
        @param autoTransformer: True if this is an autotransformer, false otherwise. 
        @param reconfigWinding: True if windings can be re-configured to result in a different input or output voltage. 
        @param dayOverLoadRating: 24-hour overload rating. 
        @param altSecondaryNomVoltage: Nominal voltage rating for alternate configuration for secondary winding. 
        @param altPrimaryNomVoltage: Nominal voltage rating for alternate configuration for primary winding. 
        @param coreCoilsWeight: Weight of core and coils in transformer. 
        @param solidInsulationWeight: Weight of solid insultation in transformer. 
        @param hourOverLoadRating: 1-hour overload rating. 
        @param neutralBIL: Basic Insulation Level of Neutral 
        @param TransformerAssets:
        @param TransformerInfo:
        """
        #: Function of this transformer.Values are: "other", "voltageRegulator", "secondaryTransformer", "autotransformer", "powerTransformer"
        self.function = function

        #: Kind of construction for this transformer.Values are: "padmountDeadFront", "onePhase", "unknown", "valut", "padmounted", "aerial", "underground", "padmountLiveFront", "network", "vaultThreePhase", "subway", "dryType", "padmountLoopThrough", "overhead", "threePhase", "padmountFeedThrough"
        self.constructionKind = constructionKind

        #: Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, otherValues are: "other", "nomex", "paper", "thermallyUpgradedPaper"
        self.windingInsulationKind = windingInsulationKind

        #: Kind of oil preservation system.Values are: "nitrogenBlanket", "freeBreathing", "conservator", "other"
        self.oilPreservationKind = oilPreservationKind

        #: Core kind of this transformer product.Values are: "core", "shell"
        self.coreKind = coreKind

        #: True if this is an autotransformer, false otherwise.
        self.autoTransformer = autoTransformer

        #: True if windings can be re-configured to result in a different input or output voltage.
        self.reconfigWinding = reconfigWinding

        #: 24-hour overload rating.
        self.dayOverLoadRating = dayOverLoadRating

        #: Nominal voltage rating for alternate configuration for secondary winding.
        self.altSecondaryNomVoltage = altSecondaryNomVoltage

        #: Nominal voltage rating for alternate configuration for primary winding.
        self.altPrimaryNomVoltage = altPrimaryNomVoltage

        #: Weight of core and coils in transformer.
        self.coreCoilsWeight = coreCoilsWeight

        #: Weight of solid insultation in transformer.
        self.solidInsulationWeight = solidInsulationWeight

        #: 1-hour overload rating.
        self.hourOverLoadRating = hourOverLoadRating

        #: Basic Insulation Level of Neutral
        self.neutralBIL = neutralBIL

        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        self._TransformerInfo = None
        self.TransformerInfo = TransformerInfo

        super(TransformerAssetModel, self).__init__(*args, **kw_args)

    def getTransformerAssets(self):
        
        return self._TransformerAssets

    def setTransformerAssets(self, value):
        for x in self._TransformerAssets:
            x._TransformerAssetModel = None
        for y in value:
            y._TransformerAssetModel = self
        self._TransformerAssets = value

    TransformerAssets = property(getTransformerAssets, setTransformerAssets)

    def addTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj._TransformerAssetModel = self
            self._TransformerAssets.append(obj)

    def removeTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj._TransformerAssetModel = None
            self._TransformerAssets.remove(obj)

    def getTransformerInfo(self):
        
        return self._TransformerInfo

    def setTransformerInfo(self, value):
        if self._TransformerInfo is not None:
            filtered = [x for x in self.TransformerInfo.TransformerAssetModels if x != self]
            self._TransformerInfo._TransformerAssetModels = filtered

        self._TransformerInfo = value
        if self._TransformerInfo is not None:
            self._TransformerInfo._TransformerAssetModels.append(self)

    TransformerInfo = property(getTransformerInfo, setTransformerInfo)

