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

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.core import IdentifiedObject
from iec61970.wires import EnergyConsumer
from iec61970.core import PowerSystemResource
from iec61970.core import RegularIntervalSchedule
from iec61970.domain import PerCent
from iec61970.domain import CurrentFlow
from iec61970.domain import Float
from iec61970.domain import AbsoluteDateTime
from iec61970.domain import String



from enthought.traits.api import HasTraits, Instance, List, Enum, Float
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Name of season
SeasonName = Enum("winter", "spring", "summer", "fall", desc="Name of season")

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
    SeasonDayTypeSchedules = List(Instance("iec61970.loadmodel.SeasonDayTypeSchedule"))

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

    # The SubLoadArea where the Loadgroup belongs.
    SubLoadArea = Instance("iec61970.loadmodel.SubLoadArea", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin loadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadGroup user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(HasTraits):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Load demand models can be based on seasons
    SeasonDayTypeSchedules = List(Instance("iec61970.loadmodel.SeasonDayTypeSchedule"))

    # Name of the Season 
    name = SeasonName

    # Date season ends
    endDate = AbsoluteDateTime

    # Date season starts
    startDate = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin season user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End season user definitions:
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
#  "PowerCutZone" class:
#------------------------------------------------------------------------------

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    EnergyConsumers = List(Instance("iec61970.wires.EnergyConsumer"))

    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = PerCent

    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = PerCent

    #--------------------------------------------------------------------------
    #  Begin powerCutZone user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerCutZone user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadModelVersion" class:
#------------------------------------------------------------------------------

class LoadModelVersion(HasTraits):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin loadModelVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadModelVersion user definitions:
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

    pass
    #--------------------------------------------------------------------------
    #  Begin energyArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energyArea user definitions:
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
    LoadGroup = Instance("iec61970.loadmodel.ConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin conformLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conformLoad user definitions:
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

    # Consumers may be assigned to a load area.
    LoadGroup = Instance("iec61970.loadmodel.NonConformLoadGroup")

    #--------------------------------------------------------------------------
    #  Begin nonConformLoad user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoad user definitions:
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

    # Load demand models can be based on seasons
    Season = Instance("iec61970.loadmodel.Season")

    # Load demand models can be based on day type
    DayType = Instance("iec61970.loadmodel.DayType")

    #--------------------------------------------------------------------------
    #  Begin seasonDayTypeSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End seasonDayTypeSchedule user definitions:
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
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The feeder's contribution to load management, in percent
    feederLoadMgtFactor = PerCent

    # The amount of nominal feeder reactive power that is picked up cold, in percent
    coldPickUpFactorQ = PerCent

    # The amount of nominal feeder active power that is picked up cold, in percent
    coldPickUpFactorP = PerCent

    # The rated individual phase amperes
    phaseRatedCurrent = CurrentFlow

    # Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.
    loadAllocationFactor = Float

    #--------------------------------------------------------------------------
    #  Begin load user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End load user definitions:
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

#------------------------------------------------------------------------------
#  "ConformLoadSchedule" class:
#------------------------------------------------------------------------------

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup = Instance("iec61970.loadmodel.ConformLoadGroup", allow_none=False)

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

    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup = Instance("iec61970.loadmodel.NonConformLoadGroup", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin nonConformLoadSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoadSchedule user definitions:
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

    # The LoadArea where the SubLoadArea belongs.
    LoadArea = Instance("iec61970.loadmodel.LoadArea", allow_none=False)

    # The Loadgroups in the SubLoadArea.
    LoadGroups = List(Instance("iec61970.loadmodel.LoadGroup"))

    #--------------------------------------------------------------------------
    #  Begin subLoadArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subLoadArea user definitions:
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
    SubLoadAreas = List(Instance("iec61970.loadmodel.SubLoadArea"))

    #--------------------------------------------------------------------------
    #  Begin loadArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadArea user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Loads that follows a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("iec61970.loadmodel.ConformLoad"))

    # The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedules = List(Instance("iec61970.loadmodel.ConformLoadSchedule"))

    #--------------------------------------------------------------------------
    #  Begin conformLoadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conformLoadGroup user definitions:
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

    # The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedules = List(Instance("iec61970.loadmodel.NonConformLoadSchedule"))

    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("iec61970.loadmodel.NonConformLoad"))

    #--------------------------------------------------------------------------
    #  Begin nonConformLoadGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nonConformLoadGroup user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
