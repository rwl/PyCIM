# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Assets.ProductAssetModel import ProductAssetModel

class TransformerAssetModel(ProductAssetModel):
    """Documentation for a type of a transformer of a particular product model made by a manufacturer.Documentation for a type of a transformer of a particular product model made by a manufacturer.
    """

    def __init__(self, neutralBIL=0.0, constructionKind="dryType", coreCoilsWeight=0.0, windingInsulationKind="thermallyUpgradedPaper", hourOverLoadRating=0.0, altPrimaryNomVoltage=0.0, altSecondaryNomVoltage=0.0, reconfigWinding=False, function="autotransformer", oilPreservationKind="other", dayOverLoadRating=0.0, coreKind="shell", autoTransformer=False, solidInsulationWeight=0.0, TransformerAssets=None, TransformerInfo=None, *args, **kw_args):
        """Initialises a new 'TransformerAssetModel' instance.

        @param neutralBIL: Basic Insulation Level of Neutral 
        @param constructionKind: Kind of construction for this transformer. Values are: "dryType", "vaultThreePhase", "network", "padmounted", "padmountLoopThrough", "vault", "onePhase", "padmountFeedThrough", "aerial", "threePhase", "unknown", "overhead", "padmountDeadFront", "underground", "padmountLiveFront", "subway"
        @param coreCoilsWeight: Weight of core and coils in transformer. 
        @param windingInsulationKind: Type of insultation used for transformer windings. Values are: "thermallyUpgradedPaper", "other", "nomex", "paper"
        @param hourOverLoadRating: 1-hour overload rating. 
        @param altPrimaryNomVoltage: Nominal voltage rating for alternate configuration for primary winding. 
        @param altSecondaryNomVoltage: Nominal voltage rating for alternate configuration for secondary winding. 
        @param reconfigWinding: True if windings can be re-configured to result in a different input or output voltage. 
        @param function: Function of this transformer. Values are: "autotransformer", "secondaryTransformer", "other", "powerTransformer", "voltageRegulator"
        @param oilPreservationKind: Kind of oil preservation system. Values are: "other", "conservator", "freeBreathing", "nitrogenBlanket"
        @param dayOverLoadRating: 24-hour overload rating. 
        @param coreKind: Core kind of this transformer product. Values are: "shell", "core"
        @param autoTransformer: True if this is an autotransformer, false otherwise. 
        @param solidInsulationWeight: Weight of solid insultation in transformer. 
        @param TransformerAssets:
        @param TransformerInfo:
        """
        #: Basic Insulation Level of Neutral
        self.neutralBIL = neutralBIL

        #: Kind of construction for this transformer. Values are: "dryType", "vaultThreePhase", "network", "padmounted", "padmountLoopThrough", "vault", "onePhase", "padmountFeedThrough", "aerial", "threePhase", "unknown", "overhead", "padmountDeadFront", "underground", "padmountLiveFront", "subway"
        self.constructionKind = constructionKind

        #: Weight of core and coils in transformer.
        self.coreCoilsWeight = coreCoilsWeight

        #: Type of insultation used for transformer windings. Values are: "thermallyUpgradedPaper", "other", "nomex", "paper"
        self.windingInsulationKind = windingInsulationKind

        #: 1-hour overload rating.
        self.hourOverLoadRating = hourOverLoadRating

        #: Nominal voltage rating for alternate configuration for primary winding.
        self.altPrimaryNomVoltage = altPrimaryNomVoltage

        #: Nominal voltage rating for alternate configuration for secondary winding.
        self.altSecondaryNomVoltage = altSecondaryNomVoltage

        #: True if windings can be re-configured to result in a different input or output voltage.
        self.reconfigWinding = reconfigWinding

        #: Function of this transformer. Values are: "autotransformer", "secondaryTransformer", "other", "powerTransformer", "voltageRegulator"
        self.function = function

        #: Kind of oil preservation system. Values are: "other", "conservator", "freeBreathing", "nitrogenBlanket"
        self.oilPreservationKind = oilPreservationKind

        #: 24-hour overload rating.
        self.dayOverLoadRating = dayOverLoadRating

        #: Core kind of this transformer product. Values are: "shell", "core"
        self.coreKind = coreKind

        #: True if this is an autotransformer, false otherwise.
        self.autoTransformer = autoTransformer

        #: Weight of solid insultation in transformer.
        self.solidInsulationWeight = solidInsulationWeight

        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        self._TransformerInfo = None
        self.TransformerInfo = TransformerInfo

        super(TransformerAssetModel, self).__init__(*args, **kw_args)

    _attrs = ["neutralBIL", "constructionKind", "coreCoilsWeight", "windingInsulationKind", "hourOverLoadRating", "altPrimaryNomVoltage", "altSecondaryNomVoltage", "reconfigWinding", "function", "oilPreservationKind", "dayOverLoadRating", "coreKind", "autoTransformer", "solidInsulationWeight"]
    _attr_types = {"neutralBIL": float, "constructionKind": str, "coreCoilsWeight": float, "windingInsulationKind": str, "hourOverLoadRating": float, "altPrimaryNomVoltage": float, "altSecondaryNomVoltage": float, "reconfigWinding": bool, "function": str, "oilPreservationKind": str, "dayOverLoadRating": float, "coreKind": str, "autoTransformer": bool, "solidInsulationWeight": float}
    _defaults = {"neutralBIL": 0.0, "constructionKind": "dryType", "coreCoilsWeight": 0.0, "windingInsulationKind": "thermallyUpgradedPaper", "hourOverLoadRating": 0.0, "altPrimaryNomVoltage": 0.0, "altSecondaryNomVoltage": 0.0, "reconfigWinding": False, "function": "autotransformer", "oilPreservationKind": "other", "dayOverLoadRating": 0.0, "coreKind": "shell", "autoTransformer": False, "solidInsulationWeight": 0.0}
    _enums = {"constructionKind": "TransformerConstructionKind", "windingInsulationKind": "WindingInsulationKind", "function": "TransformerFunctionKind", "oilPreservationKind": "OilPreservationKind", "coreKind": "TransformerCoreKind"}
    _refs = ["TransformerAssets", "TransformerInfo"]
    _many_refs = ["TransformerAssets"]

    def getTransformerAssets(self):
        
        return self._TransformerAssets

    def setTransformerAssets(self, value):
        for x in self._TransformerAssets:
            x.TransformerAssetModel = None
        for y in value:
            y._TransformerAssetModel = self
        self._TransformerAssets = value

    TransformerAssets = property(getTransformerAssets, setTransformerAssets)

    def addTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj.TransformerAssetModel = self

    def removeTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj.TransformerAssetModel = None

    def getTransformerInfo(self):
        
        return self._TransformerInfo

    def setTransformerInfo(self, value):
        if self._TransformerInfo is not None:
            filtered = [x for x in self.TransformerInfo.TransformerAssetModels if x != self]
            self._TransformerInfo._TransformerAssetModels = filtered

        self._TransformerInfo = value
        if self._TransformerInfo is not None:
            if self not in self._TransformerInfo._TransformerAssetModels:
                self._TransformerInfo._TransformerAssetModels.append(self)

    TransformerInfo = property(getTransformerInfo, setTransformerInfo)

