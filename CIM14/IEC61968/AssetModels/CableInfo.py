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

from CIM14.IEC61968.AssetModels.ConductorInfo import ConductorInfo

class CableInfo(ConductorInfo):
    """Cable data.
    """

    def __init__(self, constructionKind="sector", shieldMaterial="steel", outerJacketKind="polyethylene", isStrandFill=False, diameterOverScreen=0.0, diameterOverInsulation=0.0, diameterOverJacket=0.0, nominalTemperature=0.0, diameterOverCore=0.0, sheathAsNeutral=False, *args, **kw_args):
        """Initialises a new 'CableInfo' instance.

        @param constructionKind: Kind of construction of this cable. Values are: "sector", "compressed", "segmental", "solid", "stranded", "compacted", "other"
        @param shieldMaterial: Material of the shield. Values are: "steel", "lead", "aluminum", "other", "copper"
        @param outerJacketKind: Kind of outer jacket of this cable. Values are: "polyethylene", "pvc", "none", "linearLowDensityPolyethylene", "other", "insulating", "semiconducting"
        @param isStrandFill: True if wire strands are extruded in a way to fill the voids in the cable. 
        @param diameterOverScreen: Diameter over the outer screen; should be the shield's inside diameter.. 
        @param diameterOverInsulation: Diameter over the insulating layer, excluding outer screen. 
        @param diameterOverJacket: Diameter over the outermost jacketing layer. 
        @param nominalTemperature: Maximum nominal design operating temperature. 
        @param diameterOverCore: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        @param sheathAsNeutral: True if sheath / shield is used as a neutral (i.e., bonded). 
        """
        #: Kind of construction of this cable. Values are: "sector", "compressed", "segmental", "solid", "stranded", "compacted", "other"
        self.constructionKind = constructionKind

        #: Material of the shield. Values are: "steel", "lead", "aluminum", "other", "copper"
        self.shieldMaterial = shieldMaterial

        #: Kind of outer jacket of this cable. Values are: "polyethylene", "pvc", "none", "linearLowDensityPolyethylene", "other", "insulating", "semiconducting"
        self.outerJacketKind = outerJacketKind

        #: True if wire strands are extruded in a way to fill the voids in the cable.
        self.isStrandFill = isStrandFill

        #: Diameter over the outer screen; should be the shield's inside diameter..
        self.diameterOverScreen = diameterOverScreen

        #: Diameter over the insulating layer, excluding outer screen.
        self.diameterOverInsulation = diameterOverInsulation

        #: Diameter over the outermost jacketing layer.
        self.diameterOverJacket = diameterOverJacket

        #: Maximum nominal design operating temperature.
        self.nominalTemperature = nominalTemperature

        #: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
        self.diameterOverCore = diameterOverCore

        #: True if sheath / shield is used as a neutral (i.e., bonded).
        self.sheathAsNeutral = sheathAsNeutral

        super(CableInfo, self).__init__(*args, **kw_args)

    _attrs = ["constructionKind", "shieldMaterial", "outerJacketKind", "isStrandFill", "diameterOverScreen", "diameterOverInsulation", "diameterOverJacket", "nominalTemperature", "diameterOverCore", "sheathAsNeutral"]
    _attr_types = {"constructionKind": str, "shieldMaterial": str, "outerJacketKind": str, "isStrandFill": bool, "diameterOverScreen": float, "diameterOverInsulation": float, "diameterOverJacket": float, "nominalTemperature": float, "diameterOverCore": float, "sheathAsNeutral": bool}
    _defaults = {"constructionKind": "sector", "shieldMaterial": "steel", "outerJacketKind": "polyethylene", "isStrandFill": False, "diameterOverScreen": 0.0, "diameterOverInsulation": 0.0, "diameterOverJacket": 0.0, "nominalTemperature": 0.0, "diameterOverCore": 0.0, "sheathAsNeutral": False}
    _enums = {"constructionKind": "CableConstructionKind", "shieldMaterial": "CableShieldMaterialKind", "outerJacketKind": "CableOuterJacketKind"}
    _refs = []
    _many_refs = []

