# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from cpsm.iec61970.wires import EnergyConsumer
from cpsm.iec61970.core import IdentifiedObject
from cpsm import Element
from cpsm.iec61970.core import RegularIntervalSchedule

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_LoadModel"

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """
    # <<< non_conform_load
    # @generated
    def __init__(self, load_group=None, *args, **kw_args):
        """ Initialises a new 'NonConformLoad' instance.

        @param load_group: Group of this ConformLoad.
        """

        self._load_group = None
        self.load_group = load_group


        super(NonConformLoad, self).__init__(*args, **kw_args)
    # >>> non_conform_load

    # <<< load_group
    # @generated
    def get_load_group(self):
        """ Group of this ConformLoad.
        """
        return self._load_group

    def set_load_group(self, value):
        if self._load_group is not None:
            filtered = [x for x in self.load_group.energy_consumers if x != self]
            self._load_group._energy_consumers = filtered

        self._load_group = value
        if self._load_group is not None:
            self._load_group._energy_consumers.append(self)

    load_group = property(get_load_group, set_load_group)
    # >>> load_group



class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """
    # <<< day_type
    # @generated
    def __init__(self, season_day_type_schedules=None, *args, **kw_args):
        """ Initialises a new 'DayType' instance.

        @param season_day_type_schedules: Schedules that use this DayType.
        """

        self._season_day_type_schedules = []
        if season_day_type_schedules is not None:
            self.season_day_type_schedules = season_day_type_schedules
        else:
            self.season_day_type_schedules = []


        super(DayType, self).__init__(*args, **kw_args)
    # >>> day_type

    # <<< season_day_type_schedules
    # @generated
    def get_season_day_type_schedules(self):
        """ Schedules that use this DayType.
        """
        return self._season_day_type_schedules

    def set_season_day_type_schedules(self, value):
        for x in self._season_day_type_schedules:
            x._day_type = None
        for y in value:
            y._day_type = self
        self._season_day_type_schedules = value

    season_day_type_schedules = property(get_season_day_type_schedules, set_season_day_type_schedules)

    def add_season_day_type_schedules(self, *season_day_type_schedules):
        for obj in season_day_type_schedules:
            obj._day_type = self
            self._season_day_type_schedules.append(obj)

    def remove_season_day_type_schedules(self, *season_day_type_schedules):
        for obj in season_day_type_schedules:
            obj._day_type = None
            self._season_day_type_schedules.remove(obj)
    # >>> season_day_type_schedules



class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """
    # <<< season
    # @generated
    def __init__(self, end_date='', start_date='', name='fall', season_day_type_schedules=None, *args, **kw_args):
        """ Initialises a new 'Season' instance.

        @param end_date: Date season ends 
        @param start_date: Date season starts 
        @param name: Name of the Season Values are: "fall", "winter", "spring", "summer"
        @param season_day_type_schedules: Schedules that use this Season.
        """
        # Date season ends 
        self.end_date = end_date

        # Date season starts 
        self.start_date = start_date

        # Name of the Season Values are: "fall", "winter", "spring", "summer"
        self.name = name


        self._season_day_type_schedules = []
        if season_day_type_schedules is not None:
            self.season_day_type_schedules = season_day_type_schedules
        else:
            self.season_day_type_schedules = []


        super(Season, self).__init__(*args, **kw_args)
    # >>> season

    # <<< season_day_type_schedules
    # @generated
    def get_season_day_type_schedules(self):
        """ Schedules that use this Season.
        """
        return self._season_day_type_schedules

    def set_season_day_type_schedules(self, value):
        for x in self._season_day_type_schedules:
            x._season = None
        for y in value:
            y._season = self
        self._season_day_type_schedules = value

    season_day_type_schedules = property(get_season_day_type_schedules, set_season_day_type_schedules)

    def add_season_day_type_schedules(self, *season_day_type_schedules):
        for obj in season_day_type_schedules:
            obj._season = self
            self._season_day_type_schedules.append(obj)

    def remove_season_day_type_schedules(self, *season_day_type_schedules):
        for obj in season_day_type_schedules:
            obj._season = None
            self._season_day_type_schedules.remove(obj)
    # >>> season_day_type_schedules



class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """
    pass
    # <<< station_supply
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'StationSupply' instance.

        """


        super(StationSupply, self).__init__(*args, **kw_args)
    # >>> station_supply



class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """
    # <<< season_day_type_schedule
    # @generated
    def __init__(self, day_type=None, season=None, *args, **kw_args):
        """ Initialises a new 'SeasonDayTypeSchedule' instance.

        @param day_type: DayType for the Schedule.
        @param season: Season for the Schedule.
        """

        self._day_type = None
        self.day_type = day_type

        self._season = None
        self.season = season


        super(SeasonDayTypeSchedule, self).__init__(*args, **kw_args)
    # >>> season_day_type_schedule

    # <<< day_type
    # @generated
    def get_day_type(self):
        """ DayType for the Schedule.
        """
        return self._day_type

    def set_day_type(self, value):
        if self._day_type is not None:
            filtered = [x for x in self.day_type.season_day_type_schedules if x != self]
            self._day_type._season_day_type_schedules = filtered

        self._day_type = value
        if self._day_type is not None:
            self._day_type._season_day_type_schedules.append(self)

    day_type = property(get_day_type, set_day_type)
    # >>> day_type

    # <<< season
    # @generated
    def get_season(self):
        """ Season for the Schedule.
        """
        return self._season

    def set_season(self, value):
        if self._season is not None:
            filtered = [x for x in self.season.season_day_type_schedules if x != self]
            self._season._season_day_type_schedules = filtered

        self._season = value
        if self._season is not None:
            self._season._season_day_type_schedules.append(self)

    season = property(get_season, set_season)
    # >>> season



class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< load_group
    # @generated
    def __init__(self, sub_load_area=None, *args, **kw_args):
        """ Initialises a new 'LoadGroup' instance.

        @param sub_load_area: The SubLoadArea where the Loadgroup belongs.
        """

        self._sub_load_area = None
        self.sub_load_area = sub_load_area


        super(LoadGroup, self).__init__(*args, **kw_args)
    # >>> load_group

    # <<< sub_load_area
    # @generated
    def get_sub_load_area(self):
        """ The SubLoadArea where the Loadgroup belongs.
        """
        return self._sub_load_area

    def set_sub_load_area(self, value):
        if self._sub_load_area is not None:
            filtered = [x for x in self.sub_load_area.load_groups if x != self]
            self._sub_load_area._load_groups = filtered

        self._sub_load_area = value
        if self._sub_load_area is not None:
            self._sub_load_area._load_groups.append(self)

    sub_load_area = property(get_sub_load_area, set_sub_load_area)
    # >>> sub_load_area



class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """
    # <<< energy_area
    # @generated
    def __init__(self, control_area=None, *args, **kw_args):
        """ Initialises a new 'EnergyArea' instance.

        @param control_area: The control area specification that is used for the load forecast.
        """

        self._control_area = None
        self.control_area = control_area


        super(EnergyArea, self).__init__(*args, **kw_args)
    # >>> energy_area

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area specification that is used for the load forecast.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            self._control_area._energy_area = None

        self._control_area = value
        if self._control_area is not None:
            self._control_area._energy_area = self

    control_area = property(get_control_area, set_control_area)
    # >>> control_area



class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """
    # <<< load_response_characteristic
    # @generated
    def __init__(self, p_frequency_exponent=0.0, q_voltage_exponent=0.0, q_frequency_exponent=0.0, p_voltage_exponent=0.0, energy_consumer=None, *args, **kw_args):
        """ Initialises a new 'LoadResponseCharacteristic' instance.

        @param p_frequency_exponent: Exponent of per unit frequency effecting active power 
        @param q_voltage_exponent: Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        @param q_frequency_exponent: Exponent of per unit frequency effecting reactive power 
        @param p_voltage_exponent: Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        @param energy_consumer: The set of loads that have the response characteristics.
        """
        # Exponent of per unit frequency effecting active power 
        self.p_frequency_exponent = p_frequency_exponent

        # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        self.q_voltage_exponent = q_voltage_exponent

        # Exponent of per unit frequency effecting reactive power 
        self.q_frequency_exponent = q_frequency_exponent

        # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        self.p_voltage_exponent = p_voltage_exponent


        self._energy_consumer = []
        if energy_consumer is not None:
            self.energy_consumer = energy_consumer
        else:
            self.energy_consumer = []


        super(LoadResponseCharacteristic, self).__init__(*args, **kw_args)
    # >>> load_response_characteristic

    # <<< energy_consumer
    # @generated
    def get_energy_consumer(self):
        """ The set of loads that have the response characteristics.
        """
        return self._energy_consumer

    def set_energy_consumer(self, value):
        for x in self._energy_consumer:
            x._load_response = None
        for y in value:
            y._load_response = self
        self._energy_consumer = value

    energy_consumer = property(get_energy_consumer, set_energy_consumer)

    def add_energy_consumer(self, *energy_consumer):
        for obj in energy_consumer:
            obj._load_response = self
            self._energy_consumer.append(obj)

    def remove_energy_consumer(self, *energy_consumer):
        for obj in energy_consumer:
            obj._load_response = None
            self._energy_consumer.remove(obj)
    # >>> energy_consumer



class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """
    # <<< conform_load
    # @generated
    def __init__(self, load_group=None, *args, **kw_args):
        """ Initialises a new 'ConformLoad' instance.

        @param load_group: Group of this ConformLoad.
        """

        self._load_group = None
        self.load_group = load_group


        super(ConformLoad, self).__init__(*args, **kw_args)
    # >>> conform_load

    # <<< load_group
    # @generated
    def get_load_group(self):
        """ Group of this ConformLoad.
        """
        return self._load_group

    def set_load_group(self, value):
        if self._load_group is not None:
            filtered = [x for x in self.load_group.energy_consumers if x != self]
            self._load_group._energy_consumers = filtered

        self._load_group = value
        if self._load_group is not None:
            self._load_group._energy_consumers.append(self)

    load_group = property(get_load_group, set_load_group)
    # >>> load_group



class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """
    # <<< non_conform_load_group
    # @generated
    def __init__(self, non_conform_load_schedules=None, energy_consumers=None, *args, **kw_args):
        """ Initialises a new 'NonConformLoadGroup' instance.

        @param non_conform_load_schedules: The NonConformLoadSchedules in the NonConformLoadGroup.
        @param energy_consumers: Conform loads assigned to this ConformLoadGroup.
        """

        self._non_conform_load_schedules = []
        if non_conform_load_schedules is not None:
            self.non_conform_load_schedules = non_conform_load_schedules
        else:
            self.non_conform_load_schedules = []

        self._energy_consumers = []
        if energy_consumers is not None:
            self.energy_consumers = energy_consumers
        else:
            self.energy_consumers = []


        super(NonConformLoadGroup, self).__init__(*args, **kw_args)
    # >>> non_conform_load_group

    # <<< non_conform_load_schedules
    # @generated
    def get_non_conform_load_schedules(self):
        """ The NonConformLoadSchedules in the NonConformLoadGroup.
        """
        return self._non_conform_load_schedules

    def set_non_conform_load_schedules(self, value):
        for x in self._non_conform_load_schedules:
            x._non_conform_load_group = None
        for y in value:
            y._non_conform_load_group = self
        self._non_conform_load_schedules = value

    non_conform_load_schedules = property(get_non_conform_load_schedules, set_non_conform_load_schedules)

    def add_non_conform_load_schedules(self, *non_conform_load_schedules):
        for obj in non_conform_load_schedules:
            obj._non_conform_load_group = self
            self._non_conform_load_schedules.append(obj)

    def remove_non_conform_load_schedules(self, *non_conform_load_schedules):
        for obj in non_conform_load_schedules:
            obj._non_conform_load_group = None
            self._non_conform_load_schedules.remove(obj)
    # >>> non_conform_load_schedules

    # <<< energy_consumers
    # @generated
    def get_energy_consumers(self):
        """ Conform loads assigned to this ConformLoadGroup.
        """
        return self._energy_consumers

    def set_energy_consumers(self, value):
        for x in self._energy_consumers:
            x._load_group = None
        for y in value:
            y._load_group = self
        self._energy_consumers = value

    energy_consumers = property(get_energy_consumers, set_energy_consumers)

    def add_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._load_group = self
            self._energy_consumers.append(obj)

    def remove_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._load_group = None
            self._energy_consumers.remove(obj)
    # >>> energy_consumers



class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """
    # <<< conform_load_schedule
    # @generated
    def __init__(self, conform_load_group=None, *args, **kw_args):
        """ Initialises a new 'ConformLoadSchedule' instance.

        @param conform_load_group: The ConformLoadGroup where the ConformLoadSchedule belongs.
        """

        self._conform_load_group = None
        self.conform_load_group = conform_load_group


        super(ConformLoadSchedule, self).__init__(*args, **kw_args)
    # >>> conform_load_schedule

    # <<< conform_load_group
    # @generated
    def get_conform_load_group(self):
        """ The ConformLoadGroup where the ConformLoadSchedule belongs.
        """
        return self._conform_load_group

    def set_conform_load_group(self, value):
        if self._conform_load_group is not None:
            filtered = [x for x in self.conform_load_group.conform_load_schedules if x != self]
            self._conform_load_group._conform_load_schedules = filtered

        self._conform_load_group = value
        if self._conform_load_group is not None:
            self._conform_load_group._conform_load_schedules.append(self)

    conform_load_group = property(get_conform_load_group, set_conform_load_group)
    # >>> conform_load_group



class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """
    pass
    # <<< customer_load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'CustomerLoad' instance.

        """


        super(CustomerLoad, self).__init__(*args, **kw_args)
    # >>> customer_load



class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """
    pass
    # <<< load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Load' instance.

        """


        super(Load, self).__init__(*args, **kw_args)
    # >>> load



class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """
    # <<< conform_load_group
    # @generated
    def __init__(self, energy_consumers=None, conform_load_schedules=None, *args, **kw_args):
        """ Initialises a new 'ConformLoadGroup' instance.

        @param energy_consumers: Conform loads assigned to this ConformLoadGroup.
        @param conform_load_schedules: The ConformLoadSchedules in the ConformLoadGroup.
        """

        self._energy_consumers = []
        if energy_consumers is not None:
            self.energy_consumers = energy_consumers
        else:
            self.energy_consumers = []

        self._conform_load_schedules = []
        if conform_load_schedules is not None:
            self.conform_load_schedules = conform_load_schedules
        else:
            self.conform_load_schedules = []


        super(ConformLoadGroup, self).__init__(*args, **kw_args)
    # >>> conform_load_group

    # <<< energy_consumers
    # @generated
    def get_energy_consumers(self):
        """ Conform loads assigned to this ConformLoadGroup.
        """
        return self._energy_consumers

    def set_energy_consumers(self, value):
        for x in self._energy_consumers:
            x._load_group = None
        for y in value:
            y._load_group = self
        self._energy_consumers = value

    energy_consumers = property(get_energy_consumers, set_energy_consumers)

    def add_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._load_group = self
            self._energy_consumers.append(obj)

    def remove_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._load_group = None
            self._energy_consumers.remove(obj)
    # >>> energy_consumers

    # <<< conform_load_schedules
    # @generated
    def get_conform_load_schedules(self):
        """ The ConformLoadSchedules in the ConformLoadGroup.
        """
        return self._conform_load_schedules

    def set_conform_load_schedules(self, value):
        for x in self._conform_load_schedules:
            x._conform_load_group = None
        for y in value:
            y._conform_load_group = self
        self._conform_load_schedules = value

    conform_load_schedules = property(get_conform_load_schedules, set_conform_load_schedules)

    def add_conform_load_schedules(self, *conform_load_schedules):
        for obj in conform_load_schedules:
            obj._conform_load_group = self
            self._conform_load_schedules.append(obj)

    def remove_conform_load_schedules(self, *conform_load_schedules):
        for obj in conform_load_schedules:
            obj._conform_load_group = None
            self._conform_load_schedules.remove(obj)
    # >>> conform_load_schedules



class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< load_area
    # @generated
    def __init__(self, sub_load_areas=None, *args, **kw_args):
        """ Initialises a new 'LoadArea' instance.

        @param sub_load_areas: The SubLoadAreas in the LoadArea.
        """

        self._sub_load_areas = []
        if sub_load_areas is not None:
            self.sub_load_areas = sub_load_areas
        else:
            self.sub_load_areas = []


        super(LoadArea, self).__init__(*args, **kw_args)
    # >>> load_area

    # <<< sub_load_areas
    # @generated
    def get_sub_load_areas(self):
        """ The SubLoadAreas in the LoadArea.
        """
        return self._sub_load_areas

    def set_sub_load_areas(self, value):
        for x in self._sub_load_areas:
            x._load_area = None
        for y in value:
            y._load_area = self
        self._sub_load_areas = value

    sub_load_areas = property(get_sub_load_areas, set_sub_load_areas)

    def add_sub_load_areas(self, *sub_load_areas):
        for obj in sub_load_areas:
            obj._load_area = self
            self._sub_load_areas.append(obj)

    def remove_sub_load_areas(self, *sub_load_areas):
        for obj in sub_load_areas:
            obj._load_area = None
            self._sub_load_areas.remove(obj)
    # >>> sub_load_areas



class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< sub_load_area
    # @generated
    def __init__(self, load_groups=None, load_area=None, *args, **kw_args):
        """ Initialises a new 'SubLoadArea' instance.

        @param load_groups: The Loadgroups in the SubLoadArea.
        @param load_area: The LoadArea where the SubLoadArea belongs.
        """

        self._load_groups = []
        if load_groups is not None:
            self.load_groups = load_groups
        else:
            self.load_groups = []

        self._load_area = None
        self.load_area = load_area


        super(SubLoadArea, self).__init__(*args, **kw_args)
    # >>> sub_load_area

    # <<< load_groups
    # @generated
    def get_load_groups(self):
        """ The Loadgroups in the SubLoadArea.
        """
        return self._load_groups

    def set_load_groups(self, value):
        for x in self._load_groups:
            x._sub_load_area = None
        for y in value:
            y._sub_load_area = self
        self._load_groups = value

    load_groups = property(get_load_groups, set_load_groups)

    def add_load_groups(self, *load_groups):
        for obj in load_groups:
            obj._sub_load_area = self
            self._load_groups.append(obj)

    def remove_load_groups(self, *load_groups):
        for obj in load_groups:
            obj._sub_load_area = None
            self._load_groups.remove(obj)
    # >>> load_groups

    # <<< load_area
    # @generated
    def get_load_area(self):
        """ The LoadArea where the SubLoadArea belongs.
        """
        return self._load_area

    def set_load_area(self, value):
        if self._load_area is not None:
            filtered = [x for x in self.load_area.sub_load_areas if x != self]
            self._load_area._sub_load_areas = filtered

        self._load_area = value
        if self._load_area is not None:
            self._load_area._sub_load_areas.append(self)

    load_area = property(get_load_area, set_load_area)
    # >>> load_area



class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """
    # <<< non_conform_load_schedule
    # @generated
    def __init__(self, non_conform_load_group=None, *args, **kw_args):
        """ Initialises a new 'NonConformLoadSchedule' instance.

        @param non_conform_load_group: The NonConformLoadGroup where the NonConformLoadSchedule belongs.
        """

        self._non_conform_load_group = None
        self.non_conform_load_group = non_conform_load_group


        super(NonConformLoadSchedule, self).__init__(*args, **kw_args)
    # >>> non_conform_load_schedule

    # <<< non_conform_load_group
    # @generated
    def get_non_conform_load_group(self):
        """ The NonConformLoadGroup where the NonConformLoadSchedule belongs.
        """
        return self._non_conform_load_group

    def set_non_conform_load_group(self, value):
        if self._non_conform_load_group is not None:
            filtered = [x for x in self.non_conform_load_group.non_conform_load_schedules if x != self]
            self._non_conform_load_group._non_conform_load_schedules = filtered

        self._non_conform_load_group = value
        if self._non_conform_load_group is not None:
            self._non_conform_load_group._non_conform_load_schedules.append(self)

    non_conform_load_group = property(get_non_conform_load_group, set_non_conform_load_group)
    # >>> non_conform_load_group



class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """
    pass
    # <<< induction_motor_load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'InductionMotorLoad' instance.

        """


        super(InductionMotorLoad, self).__init__(*args, **kw_args)
    # >>> induction_motor_load



# <<< load_model
# @generated
# >>> load_model
