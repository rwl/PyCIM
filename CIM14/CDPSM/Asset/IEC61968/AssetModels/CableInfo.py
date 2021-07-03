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

from CIM15.CDPSM.Asset.IEC61968.AssetModels.ConductorInfo import ConductorInfo

class CableInfo(ConductorInfo):
    """Cable data.
    """

    def __init__(self, diameterOverJacket=0.0, constructionKind="sector", shieldMaterial="lead", outerJacketKind="pvc", isStrandFill=False, diameterOverInsulation=0.0, diameterOverScreen=0.0, sheathAsNeutral=False, nominalTemperature=0.0, diameterOverCore=0.0, *args, **kw_args):
        """Initialises a new 'CableInfo' instance.

        @param diameterOverJacket: Diameter over the outermost jacketing layer. 
        @param constructionKind: Kind of construction of this cable. Values are: "sector", "other", "solid", "compacted", "stranded", "segmental", "compressed"
        @param shieldMaterial: Material of the shield. Values are: "lead", "aluminum", "other", "copper", "steel"
        @param outerJacketKind: Kind of outer jacket of this cable. Values are: "pvc", "linearLowDensityPolyethylene", "none", "insulating", "other", "polyethylene", "semiconducting"
        @param isStrandFill: True if wire strands are extruded in a way to fill the voids in the cable. 
        @param diameterOverInsulation: Diameter over the insulating layer, excluding outer screen. 
        @param diameterOverScreen: Diameter over the outer screen; should be the shield's inside diameter.. 
        @param sheathAsNeutral: True if sheath / shield is used as a neutral (i.e., bonded). 
        @param nominalTemperature: Maximum nominal design operating temperature. 
        @param diameterOverCore: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        """
        #: Diameter over the outermost jacketing layer.
        self.diameterOverJacket = diameterOverJacket

        #: Kind of construction of this cable. Values are: "sector", "other", "solid", "compacted", "stranded", "segmental", "compressed"
        self.constructionKind = constructionKind

        #: Material of the shield. Values are: "lead", "aluminum", "other", "copper", "steel"
        self.shieldMaterial = shieldMaterial

        #: Kind of outer jacket of this cable. Values are: "pvc", "linearLowDensityPolyethylene", "none", "insulating", "other", "polyethylene", "semiconducting"
        self.outerJacketKind = outerJacketKind

        #: True if wire strands are extruded in a way to fill the voids in the cable.
        self.isStrandFill = isStrandFill

        #: Diameter over the insulating layer, excluding outer screen.
        self.diameterOverInsulation = diameterOverInsulation

        #: Diameter over the outer screen; should be the shield's inside diameter..
        self.diameterOverScreen = diameterOverScreen

        #: True if sheath / shield is used as a neutral (i.e., bonded).
        self.sheathAsNeutral = sheathAsNeutral

        #: Maximum nominal design operating temperature.
        self.nominalTemperature = nominalTemperature

        #: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
        self.diameterOverCore = diameterOverCore

        super(CableInfo, self).__init__(*args, **kw_args)

    _attrs = ["diameterOverJacket", "constructionKind", "shieldMaterial", "outerJacketKind", "isStrandFill", "diameterOverInsulation", "diameterOverScreen", "sheathAsNeutral", "nominalTemperature", "diameterOverCore"]
    _attr_types = {"diameterOverJacket": float, "constructionKind": str, "shieldMaterial": str, "outerJacketKind": str, "isStrandFill": bool, "diameterOverInsulation": float, "diameterOverScreen": float, "sheathAsNeutral": bool, "nominalTemperature": float, "diameterOverCore": float}
    _defaults = {"diameterOverJacket": 0.0, "constructionKind": "sector", "shieldMaterial": "lead", "outerJacketKind": "pvc", "isStrandFill": False, "diameterOverInsulation": 0.0, "diameterOverScreen": 0.0, "sheathAsNeutral": False, "nominalTemperature": 0.0, "diameterOverCore": 0.0}
    _enums = {"constructionKind": "CableConstructionKind", "shieldMaterial": "CableShieldMaterialKind", "outerJacketKind": "CableOuterJacketKind"}
    _refs = []
    _many_refs = []

