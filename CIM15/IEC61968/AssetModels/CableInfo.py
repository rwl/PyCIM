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

from CIM15.IEC61968.AssetModels.ConductorInfo import ConductorInfo

class CableInfo(ConductorInfo):
    """Cable data.Cable data.
    """

    def __init__(self, outerJacketKind="pvc", sheathAsNeutral=False, isStrandFill=False, nominalTemperature=0.0, constructionKind="sector", diameterOverJacket=0.0, diameterOverInsulation=0.0, diameterOverScreen=0.0, shieldMaterial="lead", diameterOverCore=0.0, DuctBankInfo=None, *args, **kw_args):
        """Initialises a new 'CableInfo' instance.

        @param outerJacketKind: Kind of outer jacket of this cable. Values are: "pvc", "linearLowDensityPolyethylene", "none", "insulating", "other", "polyethylene", "semiconducting"
        @param sheathAsNeutral: True if sheath / shield is used as a neutral (i.e., bonded). 
        @param isStrandFill: True if wire strands are extruded in a way to fill the voids in the cable. 
        @param nominalTemperature: Maximum nominal design operating temperature. 
        @param constructionKind: Kind of construction of this cable. Values are: "sector", "other", "solid", "compacted", "stranded", "segmental", "compressed"
        @param diameterOverJacket: Diameter over the outermost jacketing layer. 
        @param diameterOverInsulation: Diameter over the insulating layer, excluding outer screen. 
        @param diameterOverScreen: Diameter over the outer screen; should be the shield's inside diameter.. 
        @param shieldMaterial: Material of the shield. Values are: "lead", "aluminum", "other", "copper", "steel"
        @param diameterOverCore: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        @param DuctBankInfo:
        """
        #: Kind of outer jacket of this cable. Values are: "pvc", "linearLowDensityPolyethylene", "none", "insulating", "other", "polyethylene", "semiconducting"
        self.outerJacketKind = outerJacketKind

        #: True if sheath / shield is used as a neutral (i.e., bonded).
        self.sheathAsNeutral = sheathAsNeutral

        #: True if wire strands are extruded in a way to fill the voids in the cable.
        self.isStrandFill = isStrandFill

        #: Maximum nominal design operating temperature.
        self.nominalTemperature = nominalTemperature

        #: Kind of construction of this cable. Values are: "sector", "other", "solid", "compacted", "stranded", "segmental", "compressed"
        self.constructionKind = constructionKind

        #: Diameter over the outermost jacketing layer.
        self.diameterOverJacket = diameterOverJacket

        #: Diameter over the insulating layer, excluding outer screen.
        self.diameterOverInsulation = diameterOverInsulation

        #: Diameter over the outer screen; should be the shield's inside diameter..
        self.diameterOverScreen = diameterOverScreen

        #: Material of the shield. Values are: "lead", "aluminum", "other", "copper", "steel"
        self.shieldMaterial = shieldMaterial

        #: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
        self.diameterOverCore = diameterOverCore

        self._DuctBankInfo = None
        self.DuctBankInfo = DuctBankInfo

        super(CableInfo, self).__init__(*args, **kw_args)

    _attrs = ["outerJacketKind", "sheathAsNeutral", "isStrandFill", "nominalTemperature", "constructionKind", "diameterOverJacket", "diameterOverInsulation", "diameterOverScreen", "shieldMaterial", "diameterOverCore"]
    _attr_types = {"outerJacketKind": str, "sheathAsNeutral": bool, "isStrandFill": bool, "nominalTemperature": float, "constructionKind": str, "diameterOverJacket": float, "diameterOverInsulation": float, "diameterOverScreen": float, "shieldMaterial": str, "diameterOverCore": float}
    _defaults = {"outerJacketKind": "pvc", "sheathAsNeutral": False, "isStrandFill": False, "nominalTemperature": 0.0, "constructionKind": "sector", "diameterOverJacket": 0.0, "diameterOverInsulation": 0.0, "diameterOverScreen": 0.0, "shieldMaterial": "lead", "diameterOverCore": 0.0}
    _enums = {"outerJacketKind": "CableOuterJacketKind", "constructionKind": "CableConstructionKind", "shieldMaterial": "CableShieldMaterialKind"}
    _refs = ["DuctBankInfo"]
    _many_refs = []

    def getDuctBankInfo(self):
        
        return self._DuctBankInfo

    def setDuctBankInfo(self, value):
        if self._DuctBankInfo is not None:
            filtered = [x for x in self.DuctBankInfo.CableInfos if x != self]
            self._DuctBankInfo._CableInfos = filtered

        self._DuctBankInfo = value
        if self._DuctBankInfo is not None:
            if self not in self._DuctBankInfo._CableInfos:
                self._DuctBankInfo._CableInfos.append(self)

    DuctBankInfo = property(getDuctBankInfo, setDuctBankInfo)

