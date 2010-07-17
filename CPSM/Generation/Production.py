#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.Core import Curve
from CPSM.Core import Equipment
from CPSM.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Enum, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


GeneratorControlSource = Enum("offAGC", "Unavailable", "onAGC", "PlantControl")

#------------------------------------------------------------------------------
#  "GrossToNetActivePowerCurve" class:
#------------------------------------------------------------------------------

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GeneratingUnit = Instance("CPSM.Generation.Production.GeneratingUnit", allow_none=False,
        desc="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit",
        transient=True,
        opposite="GrossToNetActivePowerCurves",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "GrossToNetActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "y2Unit", "xUnit", "curveStyle", "y1Unit",
                label="Attributes"),
            VGroup("Model", "CurveScheduleDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.Generation.Production.GrossToNetActivePowerCurve",
        title="GrossToNetActivePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GrossToNetActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratingUnit" class:
#------------------------------------------------------------------------------

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    Contains_SynchronousMachines = List(Instance("CPSM.Wires.SynchronousMachine"),
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit")

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GrossToNetActivePowerCurves = List(Instance("CPSM.Generation.Production.GrossToNetActivePowerCurve"),
        desc="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit")

    # ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.
    ControlAreaGeneratingUnit = List(Instance("CPSM.ControlArea.ControlAreaGeneratingUnit"),
        desc="ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.")

    # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = ActivePower(desc="This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit")

    # Generating unit economic participation factorGenerating unit economic participation factor
    normalPF = Float(desc="Generating unit economic participation factorGenerating unit economic participation factor")

    # The unit's gross rated maximum capacity (Book Value).The unit's gross rated maximum capacity (Book Value).
    ratedGrossMaxP = ActivePower(desc="The unit's gross rated maximum capacity (Book Value).The unit's gross rated maximum capacity (Book Value).")

    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission gridThe gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    ratedGrossMinP = ActivePower(desc="The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission gridThe gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid")

    # The source of controls for a generating unit.The source of controls for a generating unit.
    genControlSource = GeneratorControlSource(desc="The source of controls for a generating unit.The source of controls for a generating unit.")

    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacityThe net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    ratedNetMaxP = ActivePower(desc="The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacityThe net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity")

    # Generating unit economic participation factorGenerating unit economic participation factor
    longPF = Float(desc="Generating unit economic participation factorGenerating unit economic participation factor")

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configurationDefault Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initialP = ActivePower(desc="Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configurationDefault Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration")

    # Generating unit economic participation factorGenerating unit economic participation factor
    shortPF = Float(desc="Generating unit economic participation factorGenerating unit economic participation factor")

    # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = ActivePower(desc="This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.")

    #--------------------------------------------------------------------------
    #  Begin "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "maxOperatingP", "normalPF", "ratedGrossMaxP", "ratedGrossMinP", "genControlSource", "ratedNetMaxP", "longPF", "initialP", "shortPF", "minOperatingP",
                label="Attributes", columns=1),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "Contains_SynchronousMachines", "GrossToNetActivePowerCurves", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.Generation.Production.GeneratingUnit",
        title="GeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroGeneratingUnit" class:
#------------------------------------------------------------------------------

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "maxOperatingP", "normalPF", "ratedGrossMaxP", "ratedGrossMinP", "genControlSource", "ratedNetMaxP", "longPF", "initialP", "shortPF", "minOperatingP",
                label="Attributes", columns=1),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "Contains_SynchronousMachines", "GrossToNetActivePowerCurves", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.Generation.Production.HydroGeneratingUnit",
        title="HydroGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ThermalGeneratingUnit" class:
#------------------------------------------------------------------------------

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "maxOperatingP", "normalPF", "ratedGrossMaxP", "ratedGrossMinP", "genControlSource", "ratedNetMaxP", "longPF", "initialP", "shortPF", "minOperatingP",
                label="Attributes", columns=1),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "Contains_SynchronousMachines", "GrossToNetActivePowerCurves", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.Generation.Production.ThermalGeneratingUnit",
        title="ThermalGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
