#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import IdentifiedObject
from CIM13 import Root
from CIM13.Wires import EnergyConsumer
from CIM13.Core import PowerSystemResource
from CIM13.Core import RegularIntervalSchedule



from enthought.traits.api import Instance, List, Enum, Float, Bool, Str
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SeasonName = Enum("summer", "fall", "winter", "spring")

#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EnergyConsumer = List(Instance("CIM13.Wires.EnergyConsumer"))

    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantPower = EFloat

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    pVoltageExponent = EFloat

    # Exponent of per unit frequency effecting active power
    pFrequencyExponent = EFloat

    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantImpedance = EFloat

    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantPower = EFloat

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantImpedance = EFloat

    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantCurrent = EFloat

    # Exponent of per unit frequency effecting reactive power
    qFrequencyExponent = EFloat

    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
    exponentModel = EBoolean

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    qVoltageExponent = EFloat

    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantCurrent = EFloat

    #--------------------------------------------------------------------------
    #  Begin loadResponseCharacteristic user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadResponseCharacteristic user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(Root):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Load demand models can be based on seasons
    SeasonDayTypeSchedules = List(Instance("CIM13.LoadModel.SeasonDayTypeSchedule"))

    # Date season ends
    endDate = EString

    # Name of the Season
    name = SeasonName

    # Date season starts
    startDate = EString

    #--------------------------------------------------------------------------
    #  Begin season user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End season user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoad" class:
#------------------------------------------------------------------------------

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Consumers may be assigned to a load area.
    LoadGroup = Instance("CIM13.LoadModel.ConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin conformLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conformLoad user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerCutZone" class:
#------------------------------------------------------------------------------

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    EnergyConsumers = List(Instance("CIM13.Wires.EnergyConsumer"))

    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = EFloat

    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = EFloat

    #--------------------------------------------------------------------------
    #  Begin powerCutZone user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerCutZone user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StationSupply" class:
#------------------------------------------------------------------------------

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin stationSupply user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stationSupply user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DayType" class:
#------------------------------------------------------------------------------

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Load demand models can be based on day type
    SeasonDayTypeSchedules = List(Instance("CIM13.LoadModel.SeasonDayTypeSchedule"))

    #--------------------------------------------------------------------------
    #  Begin dayType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End dayType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadGroup" class:
#------------------------------------------------------------------------------

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SubLoadArea = Instance("CIM13.LoadModel.SubLoadArea")

    #--------------------------------------------------------------------------
    #  Begin loadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadGroup user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyArea" class:
#------------------------------------------------------------------------------

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlArea = Instance("CIM13.ControlArea.ControlArea")

    #--------------------------------------------------------------------------
    #  Begin energyArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energyArea user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeasonDayTypeSchedule" class:
#------------------------------------------------------------------------------

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Load demand models can be based on day type
    DayType = Instance("CIM13.LoadModel.DayType")

    # Load demand models can be based on seasons
    Season = Instance("CIM13.LoadModel.Season")

    #--------------------------------------------------------------------------
    #  Begin seasonDayTypeSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End seasonDayTypeSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoad" class:
#------------------------------------------------------------------------------

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LoadGroup = Instance("CIM13.LoadModel.NonConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin nonConformLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoad user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubLoadArea" class:
#------------------------------------------------------------------------------

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadAreas in the LoadArea.
    LoadArea = Instance("CIM13.LoadModel.LoadArea")

    LoadGroups = List(Instance("CIM13.LoadModel.LoadGroup"))

    #--------------------------------------------------------------------------
    #  Begin subLoadArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subLoadArea user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The feeder's contribution to load management.
    feederLoadMgtFactor = EFloat

    # The rated individual phase current.
    phaseRatedCurrent = EFloat

    # The amount of nominal feeder active power that is picked up cold.
    coldPickUpFactorP = EFloat

    # The amount of nominal feeder reactive power that is picked up cold.
    coldPickUpFactorQ = EFloat

    # Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.
    loadAllocationFactor = EFloat

    #--------------------------------------------------------------------------
    #  Begin load user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End load user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("CIM13.LoadModel.ConformLoad"))

    ConformLoadSchedules = List(Instance("CIM13.LoadModel.ConformLoadSchedule"))

    #--------------------------------------------------------------------------
    #  Begin conformLoadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conformLoadGroup user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadArea" class:
#------------------------------------------------------------------------------

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadAreas in the LoadArea.
    SubLoadAreas = List(Instance("CIM13.LoadModel.SubLoadArea"))

    #--------------------------------------------------------------------------
    #  Begin loadArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadArea user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadSchedule" class:
#------------------------------------------------------------------------------

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConformLoadGroup = Instance("CIM13.LoadModel.ConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin conformLoadSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conformLoadSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadSchedule" class:
#------------------------------------------------------------------------------

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    NonConformLoadGroup = Instance("CIM13.LoadModel.NonConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin nonConformLoadSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoadSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerLoad" class:
#------------------------------------------------------------------------------

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin customerLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End customerLoad user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadGroup" class:
#------------------------------------------------------------------------------

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    NonConformLoadSchedules = List(Instance("CIM13.LoadModel.NonConformLoadSchedule"))

    EnergyConsumers = List(Instance("CIM13.LoadModel.NonConformLoad"))

    #--------------------------------------------------------------------------
    #  Begin nonConformLoadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoadGroup user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InductionMotorLoad" class:
#------------------------------------------------------------------------------

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin inductionMotorLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End inductionMotorLoad user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
