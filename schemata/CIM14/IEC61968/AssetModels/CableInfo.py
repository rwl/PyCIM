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

from CIM14.IEC61968.AssetModels.ConductorInfo import ConductorInfo

class CableInfo(ConductorInfo):
    """Cable data.
    """

    def __init__(self, constructionKind='sector', shieldMaterial='steel', outerJacketKind='polyethylene', isStrandFill=False, diameterOverScreen=0.0, diameterOverInsulation=0.0, diameterOverJacket=0.0, nominalTemperature=0.0, diameterOverCore=0.0, sheathAsNeutral=False, **kw_args):
        """Initializes a new 'CableInfo' instance.

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
        #: Kind of construction of this cable.Values are: "sector", "compressed", "segmental", "solid", "stranded", "compacted", "other"
        self.constructionKind = constructionKind

        #: Material of the shield.Values are: "steel", "lead", "aluminum", "other", "copper"
        self.shieldMaterial = shieldMaterial

        #: Kind of outer jacket of this cable.Values are: "polyethylene", "pvc", "none", "linearLowDensityPolyethylene", "other", "insulating", "semiconducting"
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

        super(CableInfo, self).__init__(**kw_args)

