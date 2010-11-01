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

from CIM14v13.IEC61968.AssetModels.ConductorInfo import ConductorInfo

class CableInfo(ConductorInfo):
    """Cable data.
    """

    def __init__(self, constructionKind='compacted', shieldMaterial='other', outerJacketKind='linearLowDensityPolyethylene', diameterOverCore=0.0, isStrandFill=False, diameterOverInsulation=0.0, diameterOverJacket=0.0, nominalTemperature=0.0, sheathAsNeutral=False, diameterOverScreen=0.0, *args, **kw_args):
        """Initializes a new 'CableInfo' instance.

        @param constructionKind: Kind of construction of this cable. Values are: "compacted", "sector", "segmental", "solid", "stranded", "other", "compressed"
        @param shieldMaterial: Material of the shield. Values are: "other", "aluminum", "steel", "lead", "copper"
        @param outerJacketKind: Kind of outer jacket of this cable. Values are: "linearLowDensityPolyethylene", "semiconducting", "none", "other", "pvc", "insulating", "polyethylene"
        @param diameterOverCore: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        @param isStrandFill: True if wire strands are extruded in a way to fill the voids in the cable. 
        @param diameterOverInsulation: Diameter over the insulating layer, excluding outer screen. 
        @param diameterOverJacket: Diameter over the outermost jacketing layer. 
        @param nominalTemperature: Maximum nominal design operating temperature. 
        @param sheathAsNeutral: True if sheath / shield is used as a neutral (i.e., bonded). 
        @param diameterOverScreen: Diameter over the outer screen; should be the shield's inside diameter.. 
        """
        #: Kind of construction of this cable. Values are: "compacted", "sector", "segmental", "solid", "stranded", "other", "compressed"
        self.constructionKind = constructionKind

        #: Material of the shield. Values are: "other", "aluminum", "steel", "lead", "copper"
        self.shieldMaterial = shieldMaterial

        #: Kind of outer jacket of this cable. Values are: "linearLowDensityPolyethylene", "semiconducting", "none", "other", "pvc", "insulating", "polyethylene"
        self.outerJacketKind = outerJacketKind

        #: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        self.diameterOverCore = diameterOverCore

        #: True if wire strands are extruded in a way to fill the voids in the cable. 
        self.isStrandFill = isStrandFill

        #: Diameter over the insulating layer, excluding outer screen. 
        self.diameterOverInsulation = diameterOverInsulation

        #: Diameter over the outermost jacketing layer. 
        self.diameterOverJacket = diameterOverJacket

        #: Maximum nominal design operating temperature. 
        self.nominalTemperature = nominalTemperature

        #: True if sheath / shield is used as a neutral (i.e., bonded). 
        self.sheathAsNeutral = sheathAsNeutral

        #: Diameter over the outer screen; should be the shield's inside diameter.. 
        self.diameterOverScreen = diameterOverScreen

        super(CableInfo, self).__init__(*args, **kw_args)

