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

""" Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications.
"""

from cim.iec61970.core import PowerSystemResource
from cim.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.scada"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#SCADA"

class CommunicationLink(PowerSystemResource):
    """ The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """
    # <<< communication_link
    # @generated
    def __init__(self, remote_units=None, **kw_args):
        """ Initialises a new 'CommunicationLink' instance.
        """

        self._remote_units = []
        if remote_units is not None:
            self.remote_units = remote_units
        else:
            self.remote_units = []


        super(CommunicationLink, self).__init__(**kw_args)
    # >>> communication_link

    # <<< remote_units
    # @generated
    def get_remote_units(self):
        """ RTUs may be attached to communication links.
        """
        return self._remote_units

    def set_remote_units(self, value):
        for p in self._remote_units:
            filtered = [q for q in p.communication_links if q != self]
            self._remote_units._communication_links = filtered
        for r in value:
            if self not in r._communication_links:
                r._communication_links.append(self)
        self._remote_units = value

    remote_units = property(get_remote_units, set_remote_units)

    def add_remote_units(self, *remote_units):
        for obj in remote_units:
            if self not in obj._communication_links:
                obj._communication_links.append(self)
            self._remote_units.append(obj)

    def remove_remote_units(self, *remote_units):
        for obj in remote_units:
            if self in obj._communication_links:
                obj._communication_links.remove(self)
            self._remote_units.remove(obj)
    # >>> remote_units


    def __str__(self):
        """ Returns a string representation of the CommunicationLink.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< communication_link.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CommunicationLink.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CommunicationLink", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.remote_units:
            s += '%s<%s:CommunicationLink.remote_units rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CommunicationLink")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> communication_link.serialize


class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """
    # <<< remote_point
    # @generated
    def __init__(self, remote_unit=None, **kw_args):
        """ Initialises a new 'RemotePoint' instance.
        """

        self._remote_unit = None
        self.remote_unit = remote_unit


        super(RemotePoint, self).__init__(**kw_args)
    # >>> remote_point

    # <<< remote_unit
    # @generated
    def get_remote_unit(self):
        """ Remote unit this point belongs to.
        """
        return self._remote_unit

    def set_remote_unit(self, value):
        if self._remote_unit is not None:
            filtered = [x for x in self.remote_unit.remote_points if x != self]
            self._remote_unit._remote_points = filtered

        self._remote_unit = value
        if self._remote_unit is not None:
            self._remote_unit._remote_points.append(self)

    remote_unit = property(get_remote_unit, set_remote_unit)
    # >>> remote_unit


    def __str__(self):
        """ Returns a string representation of the RemotePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< remote_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RemotePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RemotePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.remote_unit is not None:
            s += '%s<%s:RemotePoint.remote_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_unit.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RemotePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> remote_point.serialize


class RemoteUnit(PowerSystemResource):
    """ A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """
    # <<< remote_unit
    # @generated
    def __init__(self, remote_unit_type='rtu', communication_links=None, remote_points=None, **kw_args):
        """ Initialises a new 'RemoteUnit' instance.
        """
        # Type of remote unit. Values are: "rtu", "substation_control_system", "control_center", "ied"
        self.remote_unit_type = 'rtu'


        self._communication_links = []
        if communication_links is not None:
            self.communication_links = communication_links
        else:
            self.communication_links = []

        self._remote_points = []
        if remote_points is not None:
            self.remote_points = remote_points
        else:
            self.remote_points = []


        super(RemoteUnit, self).__init__(**kw_args)
    # >>> remote_unit

    # <<< communication_links
    # @generated
    def get_communication_links(self):
        """ RTUs may be attached to communication links.
        """
        return self._communication_links

    def set_communication_links(self, value):
        for p in self._communication_links:
            filtered = [q for q in p.remote_units if q != self]
            self._communication_links._remote_units = filtered
        for r in value:
            if self not in r._remote_units:
                r._remote_units.append(self)
        self._communication_links = value

    communication_links = property(get_communication_links, set_communication_links)

    def add_communication_links(self, *communication_links):
        for obj in communication_links:
            if self not in obj._remote_units:
                obj._remote_units.append(self)
            self._communication_links.append(obj)

    def remove_communication_links(self, *communication_links):
        for obj in communication_links:
            if self in obj._remote_units:
                obj._remote_units.remove(self)
            self._communication_links.remove(obj)
    # >>> communication_links

    # <<< remote_points
    # @generated
    def get_remote_points(self):
        """ Remote points this Remote unit contains.
        """
        return self._remote_points

    def set_remote_points(self, value):
        for x in self._remote_points:
            x._remote_unit = None
        for y in value:
            y._remote_unit = self
        self._remote_points = value

    remote_points = property(get_remote_points, set_remote_points)

    def add_remote_points(self, *remote_points):
        for obj in remote_points:
            obj._remote_unit = self
            self._remote_points.append(obj)

    def remove_remote_points(self, *remote_points):
        for obj in remote_points:
            obj._remote_unit = None
            self._remote_points.remove(obj)
    # >>> remote_points


    def __str__(self):
        """ Returns a string representation of the RemoteUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< remote_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RemoteUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RemoteUnit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.communication_links:
            s += '%s<%s:RemoteUnit.communication_links rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.remote_points:
            s += '%s<%s:RemoteUnit.remote_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RemoteUnit.remote_unit_type>%s</%s:RemoteUnit.remote_unit_type>' % \
            (indent, ns_prefix, self.remote_unit_type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RemoteUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> remote_unit.serialize


class RemoteSource(RemotePoint):
    """ Remote sources are state variables that are telemetered or calculated within the remote unit.
    """
    # <<< remote_source
    # @generated
    def __init__(self, sensor_minimum=0.0, deadband=0.0, sensor_maximum=0.0, scan_interval=0.0, measurement_value=None, **kw_args):
        """ Initialises a new 'RemoteSource' instance.
        """
        # The minimum value the telemetry item can return. 
        self.sensor_minimum = sensor_minimum

        # The smallest change in value to be reported. 
        self.deadband = deadband

        # The maximum value the telemetry item can return. 
        self.sensor_maximum = sensor_maximum

        # The time interval between scans. 
        self.scan_interval = scan_interval


        self._measurement_value = None
        self.measurement_value = measurement_value


        super(RemoteSource, self).__init__(**kw_args)
    # >>> remote_source

    # <<< measurement_value
    # @generated
    def get_measurement_value(self):
        """ Link to the physical telemetered point associated with this measurement.
        """
        return self._measurement_value

    def set_measurement_value(self, value):
        if self._measurement_value is not None:
            self._measurement_value._remote_source = None

        self._measurement_value = value
        if self._measurement_value is not None:
            self._measurement_value._remote_source = self

    measurement_value = property(get_measurement_value, set_measurement_value)
    # >>> measurement_value


    def __str__(self):
        """ Returns a string representation of the RemoteSource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< remote_source.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RemoteSource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RemoteSource", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement_value is not None:
            s += '%s<%s:RemoteSource.measurement_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value.uri)
        s += '%s<%s:RemoteSource.sensor_minimum>%s</%s:RemoteSource.sensor_minimum>' % \
            (indent, ns_prefix, self.sensor_minimum, ns_prefix)
        s += '%s<%s:RemoteSource.deadband>%s</%s:RemoteSource.deadband>' % \
            (indent, ns_prefix, self.deadband, ns_prefix)
        s += '%s<%s:RemoteSource.sensor_maximum>%s</%s:RemoteSource.sensor_maximum>' % \
            (indent, ns_prefix, self.sensor_maximum, ns_prefix)
        s += '%s<%s:RemoteSource.scan_interval>%s</%s:RemoteSource.scan_interval>' % \
            (indent, ns_prefix, self.scan_interval, ns_prefix)
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
        if self.remote_unit is not None:
            s += '%s<%s:RemotePoint.remote_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_unit.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RemoteSource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> remote_source.serialize


class RemoteControl(RemotePoint):
    """ Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """
    # <<< remote_control
    # @generated
    def __init__(self, actuator_maximum=0.0, actuator_minimum=0.0, remote_controlled=False, control=None, **kw_args):
        """ Initialises a new 'RemoteControl' instance.
        """
        # The maximum set point value accepted by the remote control point. 
        self.actuator_maximum = actuator_maximum

        # The minimum set point value accepted by the remote control point. 
        self.actuator_minimum = actuator_minimum

        # Set to true if the actuator is remotely controlled. 
        self.remote_controlled = remote_controlled


        self._control = None
        self.control = control


        super(RemoteControl, self).__init__(**kw_args)
    # >>> remote_control

    # <<< control
    # @generated
    def get_control(self):
        """ The Control for the RemoteControl point.
        """
        return self._control

    def set_control(self, value):
        if self._control is not None:
            self._control._remote_control = None

        self._control = value
        if self._control is not None:
            self._control._remote_control = self

    control = property(get_control, set_control)
    # >>> control


    def __str__(self):
        """ Returns a string representation of the RemoteControl.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< remote_control.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RemoteControl.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RemoteControl", self.uri)
        if format:
            indent += ' ' * depth

        if self.control is not None:
            s += '%s<%s:RemoteControl.control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control.uri)
        s += '%s<%s:RemoteControl.actuator_maximum>%s</%s:RemoteControl.actuator_maximum>' % \
            (indent, ns_prefix, self.actuator_maximum, ns_prefix)
        s += '%s<%s:RemoteControl.actuator_minimum>%s</%s:RemoteControl.actuator_minimum>' % \
            (indent, ns_prefix, self.actuator_minimum, ns_prefix)
        s += '%s<%s:RemoteControl.remote_controlled>%s</%s:RemoteControl.remote_controlled>' % \
            (indent, ns_prefix, self.remote_controlled, ns_prefix)
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
        if self.remote_unit is not None:
            s += '%s<%s:RemotePoint.remote_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_unit.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RemoteControl")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> remote_control.serialize


# <<< scada
# @generated
# >>> scada
