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

from UCTE.Core import Equipment
from UCTE.Core import IdentifiedObject
from UCTE.Domain import ActivePower
from UCTE.Domain import Money
from UCTE.Domain import PerCent



from enthought.traits.api import Instance, List, Property, Enum, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


FuelType = Enum("oil", "coal", "lignite", "gas")

#------------------------------------------------------------------------------
#  "GeneratingUnit" class:
#------------------------------------------------------------------------------

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    Contains_SynchronousMachines = List(Instance("UCTE.Wires.SynchronousMachine"),
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit")

    # ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.
    ControlAreaGeneratingUnit = List(Instance("UCTE.ControlArea.ControlAreaGeneratingUnit"),
        desc="ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.")

    # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = ActivePower(desc="This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit")

    # The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.
    startupCost = Money(desc="The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.")

    # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
    nominalP = ActivePower(desc="The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).")

    # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.
    governorSCD = PerCent(desc="Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.")

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = ActivePower(desc="Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.")

    # The variable cost component of production per unit of ActivePower.This is for Short Circuit only.The variable cost component of production per unit of ActivePower.This is for Short Circuit only.
    variableCost = Money(desc="The variable cost component of production per unit of ActivePower.This is for Short Circuit only.The variable cost component of production per unit of ActivePower.This is for Short Circuit only.")

    # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = ActivePower(desc="This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.")

    # Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. 
    normalPF = Float(desc="Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. ")

    #--------------------------------------------------------------------------
    #  Begin "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "maxOperatingP", "startupCost", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "variableCost", "minOperatingP", "normalPF",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_SynchronousMachines", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.GeneratingUnit",
        title="GeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FossilFuel" class:
#------------------------------------------------------------------------------

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have one or more fossil fuelsA thermal generating unit may have one or more fossil fuels
    ThermalGeneratingUnit = Instance("UCTE.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have one or more fossil fuelsA thermal generating unit may have one or more fossil fuels",
        transient=True,
        opposite="FossilFuels",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The type of fossil fuel, such as coal, oil, or gas.The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType = FuelType(desc="The type of fossil fuel, such as coal, oil, or gas.The type of fossil fuel, such as coal, oil, or gas.")

    #--------------------------------------------------------------------------
    #  Begin "FossilFuel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "fossilFuelType",
                label="Attributes"),
            VGroup("Model", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.FossilFuel",
        title="FossilFuel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FossilFuel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroPump" class:
#------------------------------------------------------------------------------

class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    DrivenBy_SynchronousMachine = Instance("UCTE.Wires.SynchronousMachine", allow_none=False,
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="Drives_HydroPump",
        editor=InstanceEditor(name="_synchronousmachines"))

    def _get_synchronousmachines(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.SynchronousMachine" ]
        else:
            return []

    _synchronousmachines = Property(fget=_get_synchronousmachines)

    #--------------------------------------------------------------------------
    #  Begin "HydroPump" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "DrivenBy_SynchronousMachine",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.HydroPump",
        title="HydroPump",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPump" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindGeneratingUnit" class:
#------------------------------------------------------------------------------

class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.A wind driven generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "WindGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "maxOperatingP", "startupCost", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "variableCost", "minOperatingP", "normalPF",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_SynchronousMachines", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.WindGeneratingUnit",
        title="WindGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NuclearGeneratingUnit" class:
#------------------------------------------------------------------------------

class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.A nuclear generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "NuclearGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "maxOperatingP", "startupCost", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "variableCost", "minOperatingP", "normalPF",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_SynchronousMachines", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.NuclearGeneratingUnit",
        title="NuclearGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NuclearGeneratingUnit" user definitions:
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
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "maxOperatingP", "startupCost", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "variableCost", "minOperatingP", "normalPF",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_SynchronousMachines", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.HydroGeneratingUnit",
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

    # A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
    FossilFuels = Instance("UCTE.Generation.Production.FossilFuel", allow_none=False,
        desc="A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_fossilfuels"))

    def _get_fossilfuels(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Generation.Production.FossilFuel" ]
        else:
            return []

    _fossilfuels = Property(fget=_get_fossilfuels)

    #--------------------------------------------------------------------------
    #  Begin "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "maxOperatingP", "startupCost", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "variableCost", "minOperatingP", "normalPF",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_SynchronousMachines", "ControlAreaGeneratingUnit", "FossilFuels",
                label="References"),
            dock="tab"),
        id="UCTE.Generation.Production.ThermalGeneratingUnit",
        title="ThermalGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
