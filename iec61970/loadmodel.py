# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""
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


# Name of season
SeasonName = Enum("winter", "spring", "summer", "fall", desc="Name of season")

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """
    # Load demand models can be based on day type
    SeasonDayTypeSchedules = List(Instance("iec61970.loadmodel.SeasonDayTypeSchedule.SeasonDayTypeSchedule"))

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # The SubLoadArea where the Loadgroup belongs.
    SubLoadArea = Instance("iec61970.loadmodel.SubLoadArea.SubLoadArea", allow_none=False)

class Season(HasTraits):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """
    # Load demand models can be based on seasons
    SeasonDayTypeSchedules = List(Instance("iec61970.loadmodel.SeasonDayTypeSchedule.SeasonDayTypeSchedule"))
    # Name of the Season 
    name = SeasonName
    # Date season ends
    endDate = AbsoluteDateTime
    # Date season starts
    startDate = AbsoluteDateTime

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """
    pass

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """
    # An energy consumer is assigned to a power cut zone
    EnergyConsumers = List(Instance("iec61970.wires.EnergyConsumer.EnergyConsumer"))
    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = PerCent
    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = PerCent

class LoadModelVersion(HasTraits):
    version = String
    date = AbsoluteDateTime

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """
    pass

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """
    # Consumers may be assigned to a load area.
    LoadGroup = Instance("iec61970.loadmodel.ConformLoadGroup.ConformLoadGroup")

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """
    # Consumers may be assigned to a load area.
    LoadGroup = Instance("iec61970.loadmodel.NonConformLoadGroup.NonConformLoadGroup")

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """
    # Load demand models can be based on seasons
    Season = Instance("iec61970.loadmodel.Season.Season")
    # Load demand models can be based on day type
    DayType = Instance("iec61970.loadmodel.DayType.DayType")

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """
    pass

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """
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

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """
    pass

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """
    # The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup = Instance("iec61970.loadmodel.ConformLoadGroup.ConformLoadGroup", allow_none=False)

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """
    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup = Instance("iec61970.loadmodel.NonConformLoadGroup.NonConformLoadGroup", allow_none=False)

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # The LoadArea where the SubLoadArea belongs.
    LoadArea = Instance("iec61970.loadmodel.LoadArea.LoadArea", allow_none=False)
    # The Loadgroups in the SubLoadArea.
    LoadGroups = List(Instance("iec61970.loadmodel.LoadGroup.LoadGroup"))

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # The SubLoadAreas in the LoadArea.
    SubLoadAreas = List(Instance("iec61970.loadmodel.SubLoadArea.SubLoadArea"))

class ConformLoadGroup(LoadGroup):
    """ Loads that follows a daily and seasonal load variation pattern.
    """
    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("iec61970.loadmodel.ConformLoad.ConformLoad"))
    # The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedules = List(Instance("iec61970.loadmodel.ConformLoadSchedule.ConformLoadSchedule"))

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """
    # The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedules = List(Instance("iec61970.loadmodel.NonConformLoadSchedule.NonConformLoadSchedule"))
    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("iec61970.loadmodel.NonConformLoad.NonConformLoad"))


