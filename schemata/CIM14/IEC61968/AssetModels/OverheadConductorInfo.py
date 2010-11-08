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

class OverheadConductorInfo(ConductorInfo):
    """Overhead conductor data.
    """

    def __init__(self, neutralInsulationThickness=0.0, phaseConductorSpacing=0.0, phaseConductorCount=0, *args, **kw_args):
        """Initialises a new 'OverheadConductorInfo' instance.

        @param neutralInsulationThickness: (if applicable) Insulation thickness of the neutral conductor. 
        @param phaseConductorSpacing: Distance between conductor strands in a symmetrical bundle. 
        @param phaseConductorCount: Number of conductor strands in the symmetrical bundle (1-12). 
        """
        #: (if applicable) Insulation thickness of the neutral conductor.
        self.neutralInsulationThickness = neutralInsulationThickness

        #: Distance between conductor strands in a symmetrical bundle.
        self.phaseConductorSpacing = phaseConductorSpacing

        #: Number of conductor strands in the symmetrical bundle (1-12).
        self.phaseConductorCount = phaseConductorCount

        super(OverheadConductorInfo, self).__init__(*args, **kw_args)

    _attrs = ["neutralInsulationThickness", "phaseConductorSpacing", "phaseConductorCount"]
    _attr_types = {"neutralInsulationThickness": float, "phaseConductorSpacing": float, "phaseConductorCount": int}
    _defaults = {"neutralInsulationThickness": 0.0, "phaseConductorSpacing": 0.0, "phaseConductorCount": 0}
    _enums = {}
    _refs = []
    _many_refs = []

