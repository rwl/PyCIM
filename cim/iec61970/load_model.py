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

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from cim.iec61970.core import PowerSystemResource
from cim.iec61970.core import RegularIntervalSchedule
from cim.iec61970.core import IdentifiedObject
from cim.iec61970.wires import EnergyConsumer
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.loadmodel"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#LoadModel"

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """
    # <<< power_cut_zone
    # @generated
    def __init__(self, cut_level1=0.0, cut_level2=0.0, energy_consumers=None, **kw_args):
        """ Initialises a new 'PowerCutZone' instance.
        """
        # First level (amount) of load to cut as a percentage of total zone load 
        self.cut_level1 = cut_level1

        # Second level (amount) of load to cut as a percentage of total zone load 
        self.cut_level2 = cut_level2


        self._energy_consumers = []
        if energy_consumers is not None:
            self.energy_consumers = energy_consumers
        else:
            self.energy_consumers = []


        super(PowerCutZone, self).__init__(**kw_args)
    # >>> power_cut_zone

    # <<< energy_consumers
    # @generated
    def get_energy_consumers(self):
        """ An energy consumer is assigned to a power cut zone
        """
        return self._energy_consumers

    def set_energy_consumers(self, value):
        for x in self._energy_consumers:
            x._power_cut_zone = None
        for y in value:
            y._power_cut_zone = self
        self._energy_consumers = value

    energy_consumers = property(get_energy_consumers, set_energy_consumers)

    def add_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._power_cut_zone = self
            self._energy_consumers.append(obj)

    def remove_energy_consumers(self, *energy_consumers):
        for obj in energy_consumers:
            obj._power_cut_zone = None
            self._energy_consumers.remove(obj)
    # >>> energy_consumers


    def __str__(self):
        """ Returns a string representation of the PowerCutZone.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_cut_zone.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerCutZone.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerCutZone", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.energy_consumers:
            s += '%s<%s:PowerCutZone.energy_consumers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PowerCutZone.cut_level1>%s</%s:PowerCutZone.cut_level1>' % \
            (indent, ns_prefix, self.cut_level1, ns_prefix)
        s += '%s<%s:PowerCutZone.cut_level2>%s</%s:PowerCutZone.cut_level2>' % \
            (indent, ns_prefix, self.cut_level2, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerCutZone")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_cut_zone.serialize


class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """
    # <<< season_day_type_schedule
    # @generated
    def __init__(self, day_type=None, season=None, **kw_args):
        """ Initialises a new 'SeasonDayTypeSchedule' instance.
        """

        self._day_type = None
        self.day_type = day_type

        self._season = None
        self.season = season


        super(SeasonDayTypeSchedule, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the SeasonDayTypeSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< season_day_type_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SeasonDayTypeSchedule.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SeasonDayTypeSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.day_type is not None:
            s += '%s<%s:SeasonDayTypeSchedule.day_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.day_type.uri)
        if self.season is not None:
            s += '%s<%s:SeasonDayTypeSchedule.season rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.season.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SeasonDayTypeSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> season_day_type_schedule.serialize


class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """
    # <<< day_type
    # @generated
    def __init__(self, season_day_type_schedules=None, **kw_args):
        """ Initialises a new 'DayType' instance.
        """

        self._season_day_type_schedules = []
        if season_day_type_schedules is not None:
            self.season_day_type_schedules = season_day_type_schedules
        else:
            self.season_day_type_schedules = []


        super(DayType, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the DayType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< day_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DayType.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DayType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.season_day_type_schedules:
            s += '%s<%s:DayType.season_day_type_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DayType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> day_type.serialize


class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """
    # <<< energy_area
    # @generated
    def __init__(self, control_area=None, **kw_args):
        """ Initialises a new 'EnergyArea' instance.
        """

        self._control_area = None
        self.control_area = control_area


        super(EnergyArea, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the EnergyArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyArea.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyArea", self.uri)
        if format:
            indent += ' ' * depth

        if self.control_area is not None:
            s += '%s<%s:EnergyArea.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_area.serialize


class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """
    pass
    # <<< station_supply
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'StationSupply' instance.
        """


        super(StationSupply, self).__init__(**kw_args)
    # >>> station_supply


    def __str__(self):
        """ Returns a string representation of the StationSupply.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< station_supply.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StationSupply.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StationSupply", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.clearance_tags:
            s += '%s<%s:ConductingEquipment.clearance_tags rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_step_roles:
            s += '%s<%s:ConductingEquipment.outage_step_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.electrical_assets:
            s += '%s<%s:ConductingEquipment.electrical_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sv_status is not None:
            s += '%s<%s:ConductingEquipment.sv_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_status.uri)
        for obj in self.protection_equipments:
            s += '%s<%s:ConductingEquipment.protection_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        if self.power_cut_zone is not None:
            s += '%s<%s:EnergyConsumer.power_cut_zone rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_cut_zone.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:EnergyConsumer.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.load_response is not None:
            s += '%s<%s:EnergyConsumer.load_response rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_response.uri)
        s += '%s<%s:EnergyConsumer.qfixed_pct>%s</%s:EnergyConsumer.qfixed_pct>' % \
            (indent, ns_prefix, self.qfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed>%s</%s:EnergyConsumer.pfixed>' % \
            (indent, ns_prefix, self.pfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.customer_count>%s</%s:EnergyConsumer.customer_count>' % \
            (indent, ns_prefix, self.customer_count, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed>%s</%s:EnergyConsumer.qfixed>' % \
            (indent, ns_prefix, self.qfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed_pct>%s</%s:EnergyConsumer.pfixed_pct>' % \
            (indent, ns_prefix, self.pfixed_pct, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StationSupply")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> station_supply.serialize


class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """
    # <<< non_conform_load
    # @generated
    def __init__(self, load_group=None, **kw_args):
        """ Initialises a new 'NonConformLoad' instance.
        """

        self._load_group = None
        self.load_group = load_group


        super(NonConformLoad, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the NonConformLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< non_conform_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NonConformLoad.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NonConformLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_group is not None:
            s += '%s<%s:NonConformLoad.load_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_group.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.clearance_tags:
            s += '%s<%s:ConductingEquipment.clearance_tags rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_step_roles:
            s += '%s<%s:ConductingEquipment.outage_step_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.electrical_assets:
            s += '%s<%s:ConductingEquipment.electrical_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sv_status is not None:
            s += '%s<%s:ConductingEquipment.sv_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_status.uri)
        for obj in self.protection_equipments:
            s += '%s<%s:ConductingEquipment.protection_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        if self.power_cut_zone is not None:
            s += '%s<%s:EnergyConsumer.power_cut_zone rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_cut_zone.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:EnergyConsumer.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.load_response is not None:
            s += '%s<%s:EnergyConsumer.load_response rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_response.uri)
        s += '%s<%s:EnergyConsumer.qfixed_pct>%s</%s:EnergyConsumer.qfixed_pct>' % \
            (indent, ns_prefix, self.qfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed>%s</%s:EnergyConsumer.pfixed>' % \
            (indent, ns_prefix, self.pfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.customer_count>%s</%s:EnergyConsumer.customer_count>' % \
            (indent, ns_prefix, self.customer_count, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed>%s</%s:EnergyConsumer.qfixed>' % \
            (indent, ns_prefix, self.qfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed_pct>%s</%s:EnergyConsumer.pfixed_pct>' % \
            (indent, ns_prefix, self.pfixed_pct, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NonConformLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> non_conform_load.serialize


class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """
    # <<< conform_load
    # @generated
    def __init__(self, load_group=None, **kw_args):
        """ Initialises a new 'ConformLoad' instance.
        """

        self._load_group = None
        self.load_group = load_group


        super(ConformLoad, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the ConformLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conform_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConformLoad.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConformLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_group is not None:
            s += '%s<%s:ConformLoad.load_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_group.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.clearance_tags:
            s += '%s<%s:ConductingEquipment.clearance_tags rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_step_roles:
            s += '%s<%s:ConductingEquipment.outage_step_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.electrical_assets:
            s += '%s<%s:ConductingEquipment.electrical_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sv_status is not None:
            s += '%s<%s:ConductingEquipment.sv_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_status.uri)
        for obj in self.protection_equipments:
            s += '%s<%s:ConductingEquipment.protection_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        if self.power_cut_zone is not None:
            s += '%s<%s:EnergyConsumer.power_cut_zone rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_cut_zone.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:EnergyConsumer.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.load_response is not None:
            s += '%s<%s:EnergyConsumer.load_response rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_response.uri)
        s += '%s<%s:EnergyConsumer.qfixed_pct>%s</%s:EnergyConsumer.qfixed_pct>' % \
            (indent, ns_prefix, self.qfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed>%s</%s:EnergyConsumer.pfixed>' % \
            (indent, ns_prefix, self.pfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.customer_count>%s</%s:EnergyConsumer.customer_count>' % \
            (indent, ns_prefix, self.customer_count, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed>%s</%s:EnergyConsumer.qfixed>' % \
            (indent, ns_prefix, self.qfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed_pct>%s</%s:EnergyConsumer.pfixed_pct>' % \
            (indent, ns_prefix, self.pfixed_pct, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConformLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conform_load.serialize


class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """
    # <<< season
    # @generated
    def __init__(self, name='spring', start_date='', end_date='', capacity_benefit_margin=None, violation_limits=None, season_day_type_schedules=None, **kw_args):
        """ Initialises a new 'Season' instance.
        """
        # Name of the Season Values are: "spring", "fall", "winter", "summer"
        self.name = 'spring'

        # Date season starts 
        self.start_date = start_date

        # Date season ends 
        self.end_date = end_date


        self._capacity_benefit_margin = []
        if capacity_benefit_margin is not None:
            self.capacity_benefit_margin = capacity_benefit_margin
        else:
            self.capacity_benefit_margin = []

        self._violation_limits = []
        if violation_limits is not None:
            self.violation_limits = violation_limits
        else:
            self.violation_limits = []

        self._season_day_type_schedules = []
        if season_day_type_schedules is not None:
            self.season_day_type_schedules = season_day_type_schedules
        else:
            self.season_day_type_schedules = []


        super(Season, self).__init__(**kw_args)
    # >>> season

    # <<< capacity_benefit_margin
    # @generated
    def get_capacity_benefit_margin(self):
        """ Capacity Benefit Margin may differ based on the season
        """
        return self._capacity_benefit_margin

    def set_capacity_benefit_margin(self, value):
        for x in self._capacity_benefit_margin:
            x._season = None
        for y in value:
            y._season = self
        self._capacity_benefit_margin = value

    capacity_benefit_margin = property(get_capacity_benefit_margin, set_capacity_benefit_margin)

    def add_capacity_benefit_margin(self, *capacity_benefit_margin):
        for obj in capacity_benefit_margin:
            obj._season = self
            self._capacity_benefit_margin.append(obj)

    def remove_capacity_benefit_margin(self, *capacity_benefit_margin):
        for obj in capacity_benefit_margin:
            obj._season = None
            self._capacity_benefit_margin.remove(obj)
    # >>> capacity_benefit_margin

    # <<< violation_limits
    # @generated
    def get_violation_limits(self):
        """ Limits may differ based on the season
        """
        return self._violation_limits

    def set_violation_limits(self, value):
        for x in self._violation_limits:
            x._season = None
        for y in value:
            y._season = self
        self._violation_limits = value

    violation_limits = property(get_violation_limits, set_violation_limits)

    def add_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._season = self
            self._violation_limits.append(obj)

    def remove_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._season = None
            self._violation_limits.remove(obj)
    # >>> violation_limits

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


    def __str__(self):
        """ Returns a string representation of the Season.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< season.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Season.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Season", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.capacity_benefit_margin:
            s += '%s<%s:Season.capacity_benefit_margin rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Season.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.season_day_type_schedules:
            s += '%s<%s:Season.season_day_type_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Season.name>%s</%s:Season.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:Season.start_date>%s</%s:Season.start_date>' % \
            (indent, ns_prefix, self.start_date, ns_prefix)
        s += '%s<%s:Season.end_date>%s</%s:Season.end_date>' % \
            (indent, ns_prefix, self.end_date, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Season")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> season.serialize


class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< load_group
    # @generated
    def __init__(self, registered_loads=None, sub_load_area=None, **kw_args):
        """ Initialises a new 'LoadGroup' instance.
        """

        self._registered_loads = []
        if registered_loads is not None:
            self.registered_loads = registered_loads
        else:
            self.registered_loads = []

        self._sub_load_area = None
        self.sub_load_area = sub_load_area


        super(LoadGroup, self).__init__(**kw_args)
    # >>> load_group

    # <<< registered_loads
    # @generated
    def get_registered_loads(self):
        """ 
        """
        return self._registered_loads

    def set_registered_loads(self, value):
        for x in self._registered_loads:
            x._load_area = None
        for y in value:
            y._load_area = self
        self._registered_loads = value

    registered_loads = property(get_registered_loads, set_registered_loads)

    def add_registered_loads(self, *registered_loads):
        for obj in registered_loads:
            obj._load_area = self
            self._registered_loads.append(obj)

    def remove_registered_loads(self, *registered_loads):
        for obj in registered_loads:
            obj._load_area = None
            self._registered_loads.remove(obj)
    # >>> registered_loads

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


    def __str__(self):
        """ Returns a string representation of the LoadGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadGroup.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.registered_loads:
            s += '%s<%s:LoadGroup.registered_loads rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sub_load_area is not None:
            s += '%s<%s:LoadGroup.sub_load_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sub_load_area.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_group.serialize


class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
    """
    # <<< load_response_characteristic
    # @generated
    def __init__(self, p_frequency_exponent=0.0, p_constant_current=0.0, q_constant_power=0.0, q_constant_current=0.0, p_constant_impedance=0.0, exponent_model=False, q_voltage_exponent=0.0, q_frequency_exponent=0.0, q_constant_impedance=0.0, p_voltage_exponent=0.0, p_constant_power=0.0, energy_consumer=None, **kw_args):
        """ Initialises a new 'LoadResponseCharacteristic' instance.
        """
        # Exponent of per unit frequency effecting active power 
        self.p_frequency_exponent = p_frequency_exponent

        # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_current = p_constant_current

        # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_power = q_constant_power

        # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_current = q_constant_current

        # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_impedance = p_constant_impedance

        # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used. 
        self.exponent_model = exponent_model

        # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        self.q_voltage_exponent = q_voltage_exponent

        # Exponent of per unit frequency effecting reactive power 
        self.q_frequency_exponent = q_frequency_exponent

        # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_impedance = q_constant_impedance

        # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        self.p_voltage_exponent = p_voltage_exponent

        # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_power = p_constant_power


        self._energy_consumer = []
        if energy_consumer is not None:
            self.energy_consumer = energy_consumer
        else:
            self.energy_consumer = []


        super(LoadResponseCharacteristic, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the LoadResponseCharacteristic.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_response_characteristic.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadResponseCharacteristic.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadResponseCharacteristic", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.energy_consumer:
            s += '%s<%s:LoadResponseCharacteristic.energy_consumer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:LoadResponseCharacteristic.p_frequency_exponent>%s</%s:LoadResponseCharacteristic.p_frequency_exponent>' % \
            (indent, ns_prefix, self.p_frequency_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_current>%s</%s:LoadResponseCharacteristic.p_constant_current>' % \
            (indent, ns_prefix, self.p_constant_current, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_power>%s</%s:LoadResponseCharacteristic.q_constant_power>' % \
            (indent, ns_prefix, self.q_constant_power, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_current>%s</%s:LoadResponseCharacteristic.q_constant_current>' % \
            (indent, ns_prefix, self.q_constant_current, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_impedance>%s</%s:LoadResponseCharacteristic.p_constant_impedance>' % \
            (indent, ns_prefix, self.p_constant_impedance, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.exponent_model>%s</%s:LoadResponseCharacteristic.exponent_model>' % \
            (indent, ns_prefix, self.exponent_model, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_voltage_exponent>%s</%s:LoadResponseCharacteristic.q_voltage_exponent>' % \
            (indent, ns_prefix, self.q_voltage_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_frequency_exponent>%s</%s:LoadResponseCharacteristic.q_frequency_exponent>' % \
            (indent, ns_prefix, self.q_frequency_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_impedance>%s</%s:LoadResponseCharacteristic.q_constant_impedance>' % \
            (indent, ns_prefix, self.q_constant_impedance, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_voltage_exponent>%s</%s:LoadResponseCharacteristic.p_voltage_exponent>' % \
            (indent, ns_prefix, self.p_voltage_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_power>%s</%s:LoadResponseCharacteristic.p_constant_power>' % \
            (indent, ns_prefix, self.p_constant_power, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadResponseCharacteristic")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_response_characteristic.serialize


class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< sub_load_area
    # @generated
    def __init__(self, load_area=None, load_groups=None, **kw_args):
        """ Initialises a new 'SubLoadArea' instance.
        """

        self._load_area = None
        self.load_area = load_area

        self._load_groups = []
        if load_groups is not None:
            self.load_groups = load_groups
        else:
            self.load_groups = []


        super(SubLoadArea, self).__init__(**kw_args)
    # >>> sub_load_area

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


    def __str__(self):
        """ Returns a string representation of the SubLoadArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sub_load_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubLoadArea.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubLoadArea", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_area is not None:
            s += '%s<%s:SubLoadArea.load_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_area.uri)
        for obj in self.load_groups:
            s += '%s<%s:SubLoadArea.load_groups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.control_area is not None:
            s += '%s<%s:EnergyArea.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubLoadArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sub_load_area.serialize


class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """
    # <<< non_conform_load_schedule
    # @generated
    def __init__(self, non_conform_load_group=None, **kw_args):
        """ Initialises a new 'NonConformLoadSchedule' instance.
        """

        self._non_conform_load_group = None
        self.non_conform_load_group = non_conform_load_group


        super(NonConformLoadSchedule, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the NonConformLoadSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< non_conform_load_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NonConformLoadSchedule.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NonConformLoadSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.non_conform_load_group is not None:
            s += '%s<%s:NonConformLoadSchedule.non_conform_load_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.non_conform_load_group.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)
        if self.day_type is not None:
            s += '%s<%s:SeasonDayTypeSchedule.day_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.day_type.uri)
        if self.season is not None:
            s += '%s<%s:SeasonDayTypeSchedule.season rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.season.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NonConformLoadSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> non_conform_load_schedule.serialize


class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """
    # <<< conform_load_schedule
    # @generated
    def __init__(self, conform_load_group=None, **kw_args):
        """ Initialises a new 'ConformLoadSchedule' instance.
        """

        self._conform_load_group = None
        self.conform_load_group = conform_load_group


        super(ConformLoadSchedule, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the ConformLoadSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conform_load_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConformLoadSchedule.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConformLoadSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.conform_load_group is not None:
            s += '%s<%s:ConformLoadSchedule.conform_load_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conform_load_group.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)
        if self.day_type is not None:
            s += '%s<%s:SeasonDayTypeSchedule.day_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.day_type.uri)
        if self.season is not None:
            s += '%s<%s:SeasonDayTypeSchedule.season rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.season.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConformLoadSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conform_load_schedule.serialize


class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """
    # <<< non_conform_load_group
    # @generated
    def __init__(self, energy_consumers=None, non_conform_load_schedules=None, **kw_args):
        """ Initialises a new 'NonConformLoadGroup' instance.
        """

        self._energy_consumers = []
        if energy_consumers is not None:
            self.energy_consumers = energy_consumers
        else:
            self.energy_consumers = []

        self._non_conform_load_schedules = []
        if non_conform_load_schedules is not None:
            self.non_conform_load_schedules = non_conform_load_schedules
        else:
            self.non_conform_load_schedules = []


        super(NonConformLoadGroup, self).__init__(**kw_args)
    # >>> non_conform_load_group

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


    def __str__(self):
        """ Returns a string representation of the NonConformLoadGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< non_conform_load_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NonConformLoadGroup.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NonConformLoadGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.energy_consumers:
            s += '%s<%s:NonConformLoadGroup.energy_consumers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.non_conform_load_schedules:
            s += '%s<%s:NonConformLoadGroup.non_conform_load_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.registered_loads:
            s += '%s<%s:LoadGroup.registered_loads rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sub_load_area is not None:
            s += '%s<%s:LoadGroup.sub_load_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sub_load_area.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NonConformLoadGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> non_conform_load_group.serialize


class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """
    # <<< load_area
    # @generated
    def __init__(self, sub_load_areas=None, **kw_args):
        """ Initialises a new 'LoadArea' instance.
        """

        self._sub_load_areas = []
        if sub_load_areas is not None:
            self.sub_load_areas = sub_load_areas
        else:
            self.sub_load_areas = []


        super(LoadArea, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the LoadArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadArea.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadArea", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.sub_load_areas:
            s += '%s<%s:LoadArea.sub_load_areas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.control_area is not None:
            s += '%s<%s:EnergyArea.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_area.serialize


class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """
    # <<< conform_load_group
    # @generated
    def __init__(self, conform_load_schedules=None, energy_consumers=None, **kw_args):
        """ Initialises a new 'ConformLoadGroup' instance.
        """

        self._conform_load_schedules = []
        if conform_load_schedules is not None:
            self.conform_load_schedules = conform_load_schedules
        else:
            self.conform_load_schedules = []

        self._energy_consumers = []
        if energy_consumers is not None:
            self.energy_consumers = energy_consumers
        else:
            self.energy_consumers = []


        super(ConformLoadGroup, self).__init__(**kw_args)
    # >>> conform_load_group

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


    def __str__(self):
        """ Returns a string representation of the ConformLoadGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conform_load_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConformLoadGroup.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConformLoadGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.conform_load_schedules:
            s += '%s<%s:ConformLoadGroup.conform_load_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.energy_consumers:
            s += '%s<%s:ConformLoadGroup.energy_consumers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.registered_loads:
            s += '%s<%s:LoadGroup.registered_loads rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sub_load_area is not None:
            s += '%s<%s:LoadGroup.sub_load_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sub_load_area.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConformLoadGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conform_load_group.serialize


# <<< load_model
# @generated
# >>> load_model
