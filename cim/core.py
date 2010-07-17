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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimCore"

ns_uri = "http://iec.ch/TC57/CIM-generic#Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object
    # @generated
    def __init__(self, m_rid='', local_name='', path_name='', description='', alias_name='', name='', modeling_authority_set=None, **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.
        """
        # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
        self.m_rid = m_rid

        # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
        self.local_name = local_name

        # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
        self.path_name = path_name

        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
        self.description = description

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
        self.alias_name = alias_name

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
        self.name = name


        self._modeling_authority_set = None
        self.modeling_authority_set = modeling_authority_set


        super(IdentifiedObject, self).__init__(**kw_args)
    # >>> identified_object

    # <<< modeling_authority_set
    # @generated
    def get_modeling_authority_set(self):
        """ An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._modeling_authority_set

    def set_modeling_authority_set(self, value):
        if self._modeling_authority_set is not None:
            filtered = [x for x in self.modeling_authority_set.identified_objects if x != self]
            self._modeling_authority_set._identified_objects = filtered

        self._modeling_authority_set = value
        if self._modeling_authority_set is not None:
            self._modeling_authority_set._identified_objects.append(self)

    modeling_authority_set = property(get_modeling_authority_set, set_modeling_authority_set)
    # >>> modeling_authority_set


    def __str__(self):
        """ Returns a string representation of the IdentifiedObject.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< identified_object.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IdentifiedObject.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IdentifiedObject", self.uri)
        if format:
            indent += ' ' * depth

        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IdentifiedObject")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> identified_object.serialize


class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """
    # <<< curve_data
    # @generated
    def __init__(self, y2value=0.0, y1value=0.0, xvalue=0.0, curve_schedule=None, **kw_args):
        """ Initialises a new 'CurveData' instance.
        """
        # The data value of the second Y-axis variable (if present), depending on the Y-axis units
        self.y2value = y2value

        # The data value of the  first Y-axis variable, depending on the Y-axis units
        self.y1value = y1value

        # The data value of the X-axis variable,  depending on the X-axis units
        self.xvalue = xvalue


        self._curve_schedule = None
        self.curve_schedule = curve_schedule


        super(CurveData, self).__init__(**kw_args)
    # >>> curve_data

    # <<< curve_schedule
    # @generated
    def get_curve_schedule(self):
        """ The Curve defined by this CurveData.
        """
        return self._curve_schedule

    def set_curve_schedule(self, value):
        if self._curve_schedule is not None:
            filtered = [x for x in self.curve_schedule.curve_schedule_datas if x != self]
            self._curve_schedule._curve_schedule_datas = filtered

        self._curve_schedule = value
        if self._curve_schedule is not None:
            self._curve_schedule._curve_schedule_datas.append(self)

    curve_schedule = property(get_curve_schedule, set_curve_schedule)
    # >>> curve_schedule


    def __str__(self):
        """ Returns a string representation of the CurveData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< curve_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurveData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurveData", self.uri)
        if format:
            indent += ' ' * depth

        if self.curve_schedule is not None:
            s += '%s<%s:CurveData.curve_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.curve_schedule.uri)
        s += '%s<%s:CurveData.y2value>%s</%s:CurveData.y2value>' % \
            (indent, ns_prefix, self.y2value, ns_prefix)
        s += '%s<%s:CurveData.y1value>%s</%s:CurveData.y1value>' % \
            (indent, ns_prefix, self.y1value, ns_prefix)
        s += '%s<%s:CurveData.xvalue>%s</%s:CurveData.xvalue>' % \
            (indent, ns_prefix, self.xvalue, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurveData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> curve_data.serialize


class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.
    """
    # <<< regular_time_point
    # @generated
    def __init__(self, sequence_number=0, value2=0.0, value1=0.0, interval_schedule=None, **kw_args):
        """ Initialises a new 'RegularTimePoint' instance.
        """
        # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
        self.sequence_number = sequence_number

        # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value2 = value2

        # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value1 = value1


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(RegularTimePoint, self).__init__(**kw_args)
    # >>> regular_time_point

    # <<< interval_schedule
    # @generated
    def get_interval_schedule(self):
        """ A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        return self._interval_schedule

    def set_interval_schedule(self, value):
        if self._interval_schedule is not None:
            filtered = [x for x in self.interval_schedule.time_points if x != self]
            self._interval_schedule._time_points = filtered

        self._interval_schedule = value
        if self._interval_schedule is not None:
            self._interval_schedule._time_points.append(self)

    interval_schedule = property(get_interval_schedule, set_interval_schedule)
    # >>> interval_schedule


    def __str__(self):
        """ Returns a string representation of the RegularTimePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regular_time_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegularTimePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegularTimePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.interval_schedule is not None:
            s += '%s<%s:RegularTimePoint.interval_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.interval_schedule.uri)
        s += '%s<%s:RegularTimePoint.sequence_number>%s</%s:RegularTimePoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:RegularTimePoint.value2>%s</%s:RegularTimePoint.value2>' % \
            (indent, ns_prefix, self.value2, ns_prefix)
        s += '%s<%s:RegularTimePoint.value1>%s</%s:RegularTimePoint.value1>' % \
            (indent, ns_prefix, self.value1, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegularTimePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regular_time_point.serialize


class IrregularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points varies.
    """
    # <<< irregular_time_point
    # @generated
    def __init__(self, value2=0.0, value1=0.0, time=0.0, interval_schedule=None, **kw_args):
        """ Initialises a new 'IrregularTimePoint' instance.
        """
        # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value2 = value2

        # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value1 = value1

        # The time is relative the BasicTimeSchedule.startTime.
        self.time = time


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(IrregularTimePoint, self).__init__(**kw_args)
    # >>> irregular_time_point

    # <<< interval_schedule
    # @generated
    def get_interval_schedule(self):
        """ An IrregularTimePoint belongs to an IrregularIntervalSchedule.
        """
        return self._interval_schedule

    def set_interval_schedule(self, value):
        if self._interval_schedule is not None:
            filtered = [x for x in self.interval_schedule.time_points if x != self]
            self._interval_schedule._time_points = filtered

        self._interval_schedule = value
        if self._interval_schedule is not None:
            self._interval_schedule._time_points.append(self)

    interval_schedule = property(get_interval_schedule, set_interval_schedule)
    # >>> interval_schedule


    def __str__(self):
        """ Returns a string representation of the IrregularTimePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< irregular_time_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IrregularTimePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IrregularTimePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.interval_schedule is not None:
            s += '%s<%s:IrregularTimePoint.interval_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.interval_schedule.uri)
        s += '%s<%s:IrregularTimePoint.value2>%s</%s:IrregularTimePoint.value2>' % \
            (indent, ns_prefix, self.value2, ns_prefix)
        s += '%s<%s:IrregularTimePoint.value1>%s</%s:IrregularTimePoint.value1>' % \
            (indent, ns_prefix, self.value1, ns_prefix)
        s += '%s<%s:IrregularTimePoint.time>%s</%s:IrregularTimePoint.time>' % \
            (indent, ns_prefix, self.time, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IrregularTimePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> irregular_time_point.serialize


class OperatingShare(Element):
    """ Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """
    # <<< operating_share
    # @generated
    def __init__(self, percentage=0.0, power_system_resource=None, operating_participant=None, **kw_args):
        """ Initialises a new 'OperatingShare' instance.
        """
        # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
        self.percentage = percentage


        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._operating_participant = None
        self.operating_participant = operating_participant


        super(OperatingShare, self).__init__(**kw_args)
    # >>> operating_share

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.operating_share if x != self]
            self._power_system_resource._operating_share = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._operating_share.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< operating_participant
    # @generated
    def get_operating_participant(self):
        """ The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        """
        return self._operating_participant

    def set_operating_participant(self, value):
        if self._operating_participant is not None:
            filtered = [x for x in self.operating_participant.operating_share if x != self]
            self._operating_participant._operating_share = filtered

        self._operating_participant = value
        if self._operating_participant is not None:
            self._operating_participant._operating_share.append(self)

    operating_participant = property(get_operating_participant, set_operating_participant)
    # >>> operating_participant


    def __str__(self):
        """ Returns a string representation of the OperatingShare.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operating_share.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperatingShare.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperatingShare", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:OperatingShare.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        if self.operating_participant is not None:
            s += '%s<%s:OperatingShare.operating_participant rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operating_participant.uri)
        s += '%s<%s:OperatingShare.percentage>%s</%s:OperatingShare.percentage>' % \
            (indent, ns_prefix, self.percentage, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperatingShare")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operating_share.serialize


class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """
    # <<< power_system_resource
    # @generated
    def __init__(self, operated_by_companies=None, psr_lists=None, contains_measurements=None, operating_share=None, outage_schedule=None, reporting_group=None, psrtype=None, **kw_args):
        """ Initialises a new 'PowerSystemResource' instance.
        """

        self._operated_by_companies = []
        if operated_by_companies is not None:
            self.operated_by_companies = operated_by_companies
        else:
            self.operated_by_companies = []

        self._psr_lists = []
        if psr_lists is not None:
            self.psr_lists = psr_lists
        else:
            self.psr_lists = []

        self._contains_measurements = []
        if contains_measurements is not None:
            self.contains_measurements = contains_measurements
        else:
            self.contains_measurements = []

        self._operating_share = []
        if operating_share is not None:
            self.operating_share = operating_share
        else:
            self.operating_share = []

        self._outage_schedule = None
        self.outage_schedule = outage_schedule

        self._reporting_group = []
        if reporting_group is not None:
            self.reporting_group = reporting_group
        else:
            self.reporting_group = []

        self._psrtype = None
        self.psrtype = psrtype


        super(PowerSystemResource, self).__init__(**kw_args)
    # >>> power_system_resource

    # <<< operated_by_companies
    # @generated
    def get_operated_by_companies(self):
        """ A power system resource may be part of one or more companies
        """
        return self._operated_by_companies

    def set_operated_by_companies(self, value):
        for p in self._operated_by_companies:
            filtered = [q for q in p.operates_psrs if q != self]
            self._operated_by_companies._operates_psrs = filtered
        for r in value:
            if self not in r._operates_psrs:
                r._operates_psrs.append(self)
        self._operated_by_companies = value

    operated_by_companies = property(get_operated_by_companies, set_operated_by_companies)

    def add_operated_by_companies(self, *operated_by_companies):
        for obj in operated_by_companies:
            if self not in obj._operates_psrs:
                obj._operates_psrs.append(self)
            self._operated_by_companies.append(obj)

    def remove_operated_by_companies(self, *operated_by_companies):
        for obj in operated_by_companies:
            if self in obj._operates_psrs:
                obj._operates_psrs.remove(self)
            self._operated_by_companies.remove(obj)
    # >>> operated_by_companies

    # <<< psr_lists
    # @generated
    def get_psr_lists(self):
        """
        """
        return self._psr_lists

    def set_psr_lists(self, value):
        for p in self._psr_lists:
            filtered = [q for q in p.power_system_resources if q != self]
            self._psr_lists._power_system_resources = filtered
        for r in value:
            if self not in r._power_system_resources:
                r._power_system_resources.append(self)
        self._psr_lists = value

    psr_lists = property(get_psr_lists, set_psr_lists)

    def add_psr_lists(self, *psr_lists):
        for obj in psr_lists:
            if self not in obj._power_system_resources:
                obj._power_system_resources.append(self)
            self._psr_lists.append(obj)

    def remove_psr_lists(self, *psr_lists):
        for obj in psr_lists:
            if self in obj._power_system_resources:
                obj._power_system_resources.remove(self)
            self._psr_lists.remove(obj)
    # >>> psr_lists

    # <<< contains_measurements
    # @generated
    def get_contains_measurements(self):
        """ The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._contains_measurements

    def set_contains_measurements(self, value):
        for x in self._contains_measurements:
            x._member_of_psr = None
        for y in value:
            y._member_of_psr = self
        self._contains_measurements = value

    contains_measurements = property(get_contains_measurements, set_contains_measurements)

    def add_contains_measurements(self, *contains_measurements):
        for obj in contains_measurements:
            obj._member_of_psr = self
            self._contains_measurements.append(obj)

    def remove_contains_measurements(self, *contains_measurements):
        for obj in contains_measurements:
            obj._member_of_psr = None
            self._contains_measurements.remove(obj)
    # >>> contains_measurements

    # <<< operating_share
    # @generated
    def get_operating_share(self):
        """ The linkage to any number of operating share objects.
        """
        return self._operating_share

    def set_operating_share(self, value):
        for x in self._operating_share:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._operating_share = value

    operating_share = property(get_operating_share, set_operating_share)

    def add_operating_share(self, *operating_share):
        for obj in operating_share:
            obj._power_system_resource = self
            self._operating_share.append(obj)

    def remove_operating_share(self, *operating_share):
        for obj in operating_share:
            obj._power_system_resource = None
            self._operating_share.remove(obj)
    # >>> operating_share

    # <<< outage_schedule
    # @generated
    def get_outage_schedule(self):
        """ A power system resource may have an outage schedule
        """
        return self._outage_schedule

    def set_outage_schedule(self, value):
        if self._outage_schedule is not None:
            self._outage_schedule._psr = None

        self._outage_schedule = value
        if self._outage_schedule is not None:
            self._outage_schedule._psr = self

    outage_schedule = property(get_outage_schedule, set_outage_schedule)
    # >>> outage_schedule

    # <<< reporting_group
    # @generated
    def get_reporting_group(self):
        """ Reporting groups to which this PSR belongs.
        """
        return self._reporting_group

    def set_reporting_group(self, value):
        for p in self._reporting_group:
            filtered = [q for q in p.power_system_resource if q != self]
            self._reporting_group._power_system_resource = filtered
        for r in value:
            if self not in r._power_system_resource:
                r._power_system_resource.append(self)
        self._reporting_group = value

    reporting_group = property(get_reporting_group, set_reporting_group)

    def add_reporting_group(self, *reporting_group):
        for obj in reporting_group:
            if self not in obj._power_system_resource:
                obj._power_system_resource.append(self)
            self._reporting_group.append(obj)

    def remove_reporting_group(self, *reporting_group):
        for obj in reporting_group:
            if self in obj._power_system_resource:
                obj._power_system_resource.remove(self)
            self._reporting_group.remove(obj)
    # >>> reporting_group

    # <<< psrtype
    # @generated
    def get_psrtype(self):
        """ PSRType (custom classification) for this PowerSystemResource.
        """
        return self._psrtype

    def set_psrtype(self, value):
        if self._psrtype is not None:
            filtered = [x for x in self.psrtype.power_system_resource if x != self]
            self._psrtype._power_system_resource = filtered

        self._psrtype = value
        if self._psrtype is not None:
            self._psrtype._power_system_resource.append(self)

    psrtype = property(get_psrtype, set_psrtype)
    # >>> psrtype


    def __str__(self):
        """ Returns a string representation of the PowerSystemResource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_system_resource.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerSystemResource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerSystemResource", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerSystemResource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_system_resource.serialize


class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, equivalent=False, normal_ily_in_service=False, operational_limit_set=None, member_of_equipment_container=None, contingency_equipment=None, **kw_args):
        """ Initialises a new 'Equipment' instance.
        """
        # Indicates if the equipment is real equipment (false) or an equivalent.
        self.equivalent = equivalent

        # The equipment is normally in service.
        self.normal_ily_in_service = normal_ily_in_service


        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []

        self._member_of_equipment_container = None
        self.member_of_equipment_container = member_of_equipment_container

        self._contingency_equipment = []
        if contingency_equipment is not None:
            self.contingency_equipment = contingency_equipment
        else:
            self.contingency_equipment = []


        super(Equipment, self).__init__(**kw_args)
    # >>> equipment

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The equipment limit sets associated with the equipment.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        for x in self._operational_limit_set:
            x._equipment = None
        for y in value:
            y._equipment = self
        self._operational_limit_set = value

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)

    def add_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._equipment = self
            self._operational_limit_set.append(obj)

    def remove_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._equipment = None
            self._operational_limit_set.remove(obj)
    # >>> operational_limit_set

    # <<< member_of_equipment_container
    # @generated
    def get_member_of_equipment_container(self):
        """ The association is used in the naming hierarchy.
        """
        return self._member_of_equipment_container

    def set_member_of_equipment_container(self, value):
        if self._member_of_equipment_container is not None:
            filtered = [x for x in self.member_of_equipment_container.contains_equipments if x != self]
            self._member_of_equipment_container._contains_equipments = filtered

        self._member_of_equipment_container = value
        if self._member_of_equipment_container is not None:
            self._member_of_equipment_container._contains_equipments.append(self)

    member_of_equipment_container = property(get_member_of_equipment_container, set_member_of_equipment_container)
    # >>> member_of_equipment_container

    # <<< contingency_equipment
    # @generated
    def get_contingency_equipment(self):
        """ The contingency element associated with the equipment.
        """
        return self._contingency_equipment

    def set_contingency_equipment(self, value):
        for x in self._contingency_equipment:
            x._equipment = None
        for y in value:
            y._equipment = self
        self._contingency_equipment = value

    contingency_equipment = property(get_contingency_equipment, set_contingency_equipment)

    def add_contingency_equipment(self, *contingency_equipment):
        for obj in contingency_equipment:
            obj._equipment = self
            self._contingency_equipment.append(obj)

    def remove_contingency_equipment(self, *contingency_equipment):
        for obj in contingency_equipment:
            obj._equipment = None
            self._contingency_equipment.remove(obj)
    # >>> contingency_equipment


    def __str__(self):
        """ Returns a string representation of the Equipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Equipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Equipment", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:Equipment.normal_ily_in_service>%s</%s:Equipment.normal_ily_in_service>' % \
            (indent, ns_prefix, self.normal_ily_in_service, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Equipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment.serialize


class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment
    # @generated
    def __init__(self, phases='a', sv_status=None, base_voltage=None, protection_equipments=None, terminals=None, clearance_tags=None, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.
        """
        # Describes the phases carried by a conducting equipment. Values are: "a", "ac", "an", "abcn", "b", "c", "bn", "cn", "abc", "n", "abn", "bc", "bcn", "ab", "acn"
        self.phases = 'a'


        self._sv_status = None
        self.sv_status = sv_status

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._protection_equipments = []
        if protection_equipments is not None:
            self.protection_equipments = protection_equipments
        else:
            self.protection_equipments = []

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []

        self._clearance_tags = []
        if clearance_tags is not None:
            self.clearance_tags = clearance_tags
        else:
            self.clearance_tags = []


        super(ConductingEquipment, self).__init__(**kw_args)
    # >>> conducting_equipment

    # <<< sv_status
    # @generated
    def get_sv_status(self):
        """ The status state associated with the conducting equipment.
        """
        return self._sv_status

    def set_sv_status(self, value):
        if self._sv_status is not None:
            self._sv_status._conducting_equipment = None

        self._sv_status = value
        if self._sv_status is not None:
            self._sv_status._conducting_equipment = self

    sv_status = property(get_sv_status, set_sv_status)
    # >>> sv_status

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._base_voltage

    def set_base_voltage(self, value):
        if self._base_voltage is not None:
            filtered = [x for x in self.base_voltage.conducting_equipment if x != self]
            self._base_voltage._conducting_equipment = filtered

        self._base_voltage = value
        if self._base_voltage is not None:
            self._base_voltage._conducting_equipment.append(self)

    base_voltage = property(get_base_voltage, set_base_voltage)
    # >>> base_voltage

    # <<< protection_equipments
    # @generated
    def get_protection_equipments(self):
        """ Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        return self._protection_equipments

    def set_protection_equipments(self, value):
        for p in self._protection_equipments:
            filtered = [q for q in p.conducting_equipments if q != self]
            self._protection_equipments._conducting_equipments = filtered
        for r in value:
            if self not in r._conducting_equipments:
                r._conducting_equipments.append(self)
        self._protection_equipments = value

    protection_equipments = property(get_protection_equipments, set_protection_equipments)

    def add_protection_equipments(self, *protection_equipments):
        for obj in protection_equipments:
            if self not in obj._conducting_equipments:
                obj._conducting_equipments.append(self)
            self._protection_equipments.append(obj)

    def remove_protection_equipments(self, *protection_equipments):
        for obj in protection_equipments:
            if self in obj._conducting_equipments:
                obj._conducting_equipments.remove(self)
            self._protection_equipments.remove(obj)
    # >>> protection_equipments

    # <<< terminals
    # @generated
    def get_terminals(self):
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._terminals

    def set_terminals(self, value):
        for x in self._terminals:
            x._conducting_equipment = None
        for y in value:
            y._conducting_equipment = self
        self._terminals = value

    terminals = property(get_terminals, set_terminals)

    def add_terminals(self, *terminals):
        for obj in terminals:
            obj._conducting_equipment = self
            self._terminals.append(obj)

    def remove_terminals(self, *terminals):
        for obj in terminals:
            obj._conducting_equipment = None
            self._terminals.remove(obj)
    # >>> terminals

    # <<< clearance_tags
    # @generated
    def get_clearance_tags(self):
        """ Conducting equipment may have multiple clearance tags for authorized field work
        """
        return self._clearance_tags

    def set_clearance_tags(self, value):
        for x in self._clearance_tags:
            x._conducting_equipment = None
        for y in value:
            y._conducting_equipment = self
        self._clearance_tags = value

    clearance_tags = property(get_clearance_tags, set_clearance_tags)

    def add_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._conducting_equipment = self
            self._clearance_tags.append(obj)

    def remove_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._conducting_equipment = None
            self._clearance_tags.remove(obj)
    # >>> clearance_tags


    def __str__(self):
        """ Returns a string representation of the ConductingEquipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conducting_equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConductingEquipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConductingEquipment", self.uri)
        if format:
            indent += ' ' * depth

        if self.sv_status is not None:
            s += '%s<%s:ConductingEquipment.sv_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_status.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.protection_equipments:
            s += '%s<%s:ConductingEquipment.protection_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.clearance_tags:
            s += '%s<%s:ConductingEquipment.clearance_tags rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:Equipment.normal_ily_in_service>%s</%s:Equipment.normal_ily_in_service>' % \
            (indent, ns_prefix, self.normal_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConductingEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conducting_equipment.serialize


class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """
    # <<< curve
    # @generated
    def __init__(self, y2_unit='n', y1_multiplier='k', curve_style='ramp_yvalue', y2_multiplier='k', x_unit='n', y1_unit='n', x_multiplier='k', curve_schedule_datas=None, **kw_args):
        """ Initialises a new 'Curve' instance.
        """
        # The Y2-axis units of measure. Values are: "n", "varh", "va", "none", "m3", "kg/j", "deg", "w/hz", "g", "wh", "w/s", "pa", "v/var", "ohm", "h", "f", "h", "m2", "var", "a", "rad", "s", "s", "vah", "hz", "deg_c", "s-1", "min", "j", "hz-1", "j/s", "m", "w", "v"
        self.y2_unit = 'n'

        # Multiplier for Y1-axis Values are: "k", "d", "n", "m", "none", "g", "micro", "t", "c", "m", "p"
        self.y1_multiplier = 'k'

        # The style or shape of the curve. Values are: "ramp_yvalue", "constant_yvalue", "formula", "straight_line_yvalues"
        self.curve_style = 'ramp_yvalue'

        # Multiplier for Y2-axis. Values are: "k", "d", "n", "m", "none", "g", "micro", "t", "c", "m", "p"
        self.y2_multiplier = 'k'

        # The X-axis units of measure. Values are: "n", "varh", "va", "none", "m3", "kg/j", "deg", "w/hz", "g", "wh", "w/s", "pa", "v/var", "ohm", "h", "f", "h", "m2", "var", "a", "rad", "s", "s", "vah", "hz", "deg_c", "s-1", "min", "j", "hz-1", "j/s", "m", "w", "v"
        self.x_unit = 'n'

        # The Y1-axis units of measure. Values are: "n", "varh", "va", "none", "m3", "kg/j", "deg", "w/hz", "g", "wh", "w/s", "pa", "v/var", "ohm", "h", "f", "h", "m2", "var", "a", "rad", "s", "s", "vah", "hz", "deg_c", "s-1", "min", "j", "hz-1", "j/s", "m", "w", "v"
        self.y1_unit = 'n'

        # Multiplier for X-axis. Values are: "k", "d", "n", "m", "none", "g", "micro", "t", "c", "m", "p"
        self.x_multiplier = 'k'


        self._curve_schedule_datas = []
        if curve_schedule_datas is not None:
            self.curve_schedule_datas = curve_schedule_datas
        else:
            self.curve_schedule_datas = []


        super(Curve, self).__init__(**kw_args)
    # >>> curve

    # <<< curve_schedule_datas
    # @generated
    def get_curve_schedule_datas(self):
        """ The point data values that define a curve
        """
        return self._curve_schedule_datas

    def set_curve_schedule_datas(self, value):
        for x in self._curve_schedule_datas:
            x._curve_schedule = None
        for y in value:
            y._curve_schedule = self
        self._curve_schedule_datas = value

    curve_schedule_datas = property(get_curve_schedule_datas, set_curve_schedule_datas)

    def add_curve_schedule_datas(self, *curve_schedule_datas):
        for obj in curve_schedule_datas:
            obj._curve_schedule = self
            self._curve_schedule_datas.append(obj)

    def remove_curve_schedule_datas(self, *curve_schedule_datas):
        for obj in curve_schedule_datas:
            obj._curve_schedule = None
            self._curve_schedule_datas.remove(obj)
    # >>> curve_schedule_datas


    def __str__(self):
        """ Returns a string representation of the Curve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Curve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Curve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.curve_schedule_datas:
            s += '%s<%s:Curve.curve_schedule_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Curve.y2_unit>%s</%s:Curve.y2_unit>' % \
            (indent, ns_prefix, self.y2_unit, ns_prefix)
        s += '%s<%s:Curve.y1_multiplier>%s</%s:Curve.y1_multiplier>' % \
            (indent, ns_prefix, self.y1_multiplier, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y2_multiplier>%s</%s:Curve.y2_multiplier>' % \
            (indent, ns_prefix, self.y2_multiplier, ns_prefix)
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)
        s += '%s<%s:Curve.x_multiplier>%s</%s:Curve.x_multiplier>' % \
            (indent, ns_prefix, self.x_multiplier, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Curve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> curve.serialize


class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """
    # <<< basic_interval_schedule
    # @generated
    def __init__(self, value1_unit='n', value2_multiplier='k', value1_multiplier='k', value2_unit='n', start_time='', **kw_args):
        """ Initialises a new 'BasicIntervalSchedule' instance.
        """
        # Value1 units of measure. Values are: "n", "varh", "va", "none", "m3", "kg/j", "deg", "w/hz", "g", "wh", "w/s", "pa", "v/var", "ohm", "h", "f", "h", "m2", "var", "a", "rad", "s", "s", "vah", "hz", "deg_c", "s-1", "min", "j", "hz-1", "j/s", "m", "w", "v"
        self.value1_unit = 'n'

        # Multiplier for value2. Values are: "k", "d", "n", "m", "none", "g", "micro", "t", "c", "m", "p"
        self.value2_multiplier = 'k'

        # Multiplier for value1. Values are: "k", "d", "n", "m", "none", "g", "micro", "t", "c", "m", "p"
        self.value1_multiplier = 'k'

        # Value2 units of measure. Values are: "n", "varh", "va", "none", "m3", "kg/j", "deg", "w/hz", "g", "wh", "w/s", "pa", "v/var", "ohm", "h", "f", "h", "m2", "var", "a", "rad", "s", "s", "vah", "hz", "deg_c", "s-1", "min", "j", "hz-1", "j/s", "m", "w", "v"
        self.value2_unit = 'n'

        # The time for the first time point.
        self.start_time = start_time



        super(BasicIntervalSchedule, self).__init__(**kw_args)
    # >>> basic_interval_schedule


    def __str__(self):
        """ Returns a string representation of the BasicIntervalSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< basic_interval_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BasicIntervalSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BasicIntervalSchedule", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BasicIntervalSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> basic_interval_schedule.serialize


class IrregularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them varies.
    """
    # <<< irregular_interval_schedule
    # @generated
    def __init__(self, time_points=None, **kw_args):
        """ Initialises a new 'IrregularIntervalSchedule' instance.
        """

        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []


        super(IrregularIntervalSchedule, self).__init__(**kw_args)
    # >>> irregular_interval_schedule

    # <<< time_points
    # @generated
    def get_time_points(self):
        """ The point data values that define a curve
        """
        return self._time_points

    def set_time_points(self, value):
        for x in self._time_points:
            x._interval_schedule = None
        for y in value:
            y._interval_schedule = self
        self._time_points = value

    time_points = property(get_time_points, set_time_points)

    def add_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = self
            self._time_points.append(obj)

    def remove_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = None
            self._time_points.remove(obj)
    # >>> time_points


    def __str__(self):
        """ Returns a string representation of the IrregularIntervalSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< irregular_interval_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IrregularIntervalSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IrregularIntervalSchedule", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.time_points:
            s += '%s<%s:IrregularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IrregularIntervalSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> irregular_interval_schedule.serialize


class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """
    # <<< regular_interval_schedule
    # @generated
    def __init__(self, time_step=0.0, end_time='', time_points=None, **kw_args):
        """ Initialises a new 'RegularIntervalSchedule' instance.
        """
        # The time between each pair of subsequent RegularTimePoints.
        self.time_step = time_step

        # The time for the last time point.
        self.end_time = end_time


        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []


        super(RegularIntervalSchedule, self).__init__(**kw_args)
    # >>> regular_interval_schedule

    # <<< time_points
    # @generated
    def get_time_points(self):
        """ The point data values that define a curve
        """
        return self._time_points

    def set_time_points(self, value):
        for x in self._time_points:
            x._interval_schedule = None
        for y in value:
            y._interval_schedule = self
        self._time_points = value

    time_points = property(get_time_points, set_time_points)

    def add_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = self
            self._time_points.append(obj)

    def remove_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = None
            self._time_points.remove(obj)
    # >>> time_points


    def __str__(self):
        """ Returns a string representation of the RegularIntervalSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regular_interval_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegularIntervalSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegularIntervalSchedule", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegularIntervalSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regular_interval_schedule.serialize


class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """
    # <<< connectivity_node_container
    # @generated
    def __init__(self, topological_node=None, connectivity_nodes=None, **kw_args):
        """ Initialises a new 'ConnectivityNodeContainer' instance.
        """

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []

        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []


        super(ConnectivityNodeContainer, self).__init__(**kw_args)
    # >>> connectivity_node_container

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes which belong to this connectivity node container.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._connectivity_node_container = None
        for y in value:
            y._connectivity_node_container = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._connectivity_node_container = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._connectivity_node_container = None
            self._topological_node.remove(obj)
    # >>> topological_node

    # <<< connectivity_nodes
    # @generated
    def get_connectivity_nodes(self):
        """ Connectivity nodes contained by this container.
        """
        return self._connectivity_nodes

    def set_connectivity_nodes(self, value):
        for x in self._connectivity_nodes:
            x._member_of_equipment_container = None
        for y in value:
            y._member_of_equipment_container = self
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._member_of_equipment_container = self
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._member_of_equipment_container = None
            self._connectivity_nodes.remove(obj)
    # >>> connectivity_nodes


    def __str__(self):
        """ Returns a string representation of the ConnectivityNodeContainer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< connectivity_node_container.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConnectivityNodeContainer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConnectivityNodeContainer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectivityNodeContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connectivity_node_container.serialize


class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes
    """
    # <<< equipment_container
    # @generated
    def __init__(self, contains_equipments=None, **kw_args):
        """ Initialises a new 'EquipmentContainer' instance.
        """

        self._contains_equipments = []
        if contains_equipments is not None:
            self.contains_equipments = contains_equipments
        else:
            self.contains_equipments = []


        super(EquipmentContainer, self).__init__(**kw_args)
    # >>> equipment_container

    # <<< contains_equipments
    # @generated
    def get_contains_equipments(self):
        """ The association is used in the naming hierarchy.
        """
        return self._contains_equipments

    def set_contains_equipments(self, value):
        for x in self._contains_equipments:
            x._member_of_equipment_container = None
        for y in value:
            y._member_of_equipment_container = self
        self._contains_equipments = value

    contains_equipments = property(get_contains_equipments, set_contains_equipments)

    def add_contains_equipments(self, *contains_equipments):
        for obj in contains_equipments:
            obj._member_of_equipment_container = self
            self._contains_equipments.append(obj)

    def remove_contains_equipments(self, *contains_equipments):
        for obj in contains_equipments:
            obj._member_of_equipment_container = None
            self._contains_equipments.remove(obj)
    # >>> contains_equipments


    def __str__(self):
        """ Returns a string representation of the EquipmentContainer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equipment_container.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquipmentContainer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquipmentContainer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquipmentContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment_container.serialize


class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """
    # <<< bay
    # @generated
    def __init__(self, breaker_configuration='double_breaker', bus_bar_configuration='ring_bus', bay_energy_meas_flag=False, bay_power_meas_flag=False, member_of_substation=None, member_of_voltage_level=None, **kw_args):
        """ Initialises a new 'Bay' instance.
        """
        # Breaker configuration. Values are: "double_breaker", "breaker_and_ahalf", "no_breaker", "single_breaker"
        self.breaker_configuration = 'double_breaker'

        # Bus bar configuration. Values are: "ring_bus", "main_with_transfer", "double_bus", "single_bus"
        self.bus_bar_configuration = 'ring_bus'

        # Indicates the presence/absence of energy measurements.
        self.bay_energy_meas_flag = bay_energy_meas_flag

        # Indicates the presence/absence of active/reactive power measurements.
        self.bay_power_meas_flag = bay_power_meas_flag


        self._member_of_substation = None
        self.member_of_substation = member_of_substation

        self._member_of_voltage_level = None
        self.member_of_voltage_level = member_of_voltage_level


        super(Bay, self).__init__(**kw_args)
    # >>> bay

    # <<< member_of_substation
    # @generated
    def get_member_of_substation(self):
        """ The association is used in the naming hierarchy.
        """
        return self._member_of_substation

    def set_member_of_substation(self, value):
        if self._member_of_substation is not None:
            filtered = [x for x in self.member_of_substation.contains_bays if x != self]
            self._member_of_substation._contains_bays = filtered

        self._member_of_substation = value
        if self._member_of_substation is not None:
            self._member_of_substation._contains_bays.append(self)

    member_of_substation = property(get_member_of_substation, set_member_of_substation)
    # >>> member_of_substation

    # <<< member_of_voltage_level
    # @generated
    def get_member_of_voltage_level(self):
        """ The association is used in the naming hierarchy.
        """
        return self._member_of_voltage_level

    def set_member_of_voltage_level(self, value):
        if self._member_of_voltage_level is not None:
            filtered = [x for x in self.member_of_voltage_level.contains_bays if x != self]
            self._member_of_voltage_level._contains_bays = filtered

        self._member_of_voltage_level = value
        if self._member_of_voltage_level is not None:
            self._member_of_voltage_level._contains_bays.append(self)

    member_of_voltage_level = property(get_member_of_voltage_level, set_member_of_voltage_level)
    # >>> member_of_voltage_level


    def __str__(self):
        """ Returns a string representation of the Bay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bay.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Bay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Bay", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_substation is not None:
            s += '%s<%s:Bay.member_of_substation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_substation.uri)
        if self.member_of_voltage_level is not None:
            s += '%s<%s:Bay.member_of_voltage_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_voltage_level.uri)
        s += '%s<%s:Bay.breaker_configuration>%s</%s:Bay.breaker_configuration>' % \
            (indent, ns_prefix, self.breaker_configuration, ns_prefix)
        s += '%s<%s:Bay.bus_bar_configuration>%s</%s:Bay.bus_bar_configuration>' % \
            (indent, ns_prefix, self.bus_bar_configuration, ns_prefix)
        s += '%s<%s:Bay.bay_energy_meas_flag>%s</%s:Bay.bay_energy_meas_flag>' % \
            (indent, ns_prefix, self.bay_energy_meas_flag, ns_prefix)
        s += '%s<%s:Bay.bay_power_meas_flag>%s</%s:Bay.bay_power_meas_flag>' % \
            (indent, ns_prefix, self.bay_power_meas_flag, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Bay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bay.serialize


class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """
    # <<< psrtype
    # @generated
    def __init__(self, power_system_resource=None, **kw_args):
        """ Initialises a new 'PSRType' instance.
        """

        self._power_system_resource = []
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        else:
            self.power_system_resource = []


        super(PSRType, self).__init__(**kw_args)
    # >>> psrtype

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ Power system resources classified with this PSRType.
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        for x in self._power_system_resource:
            x._psrtype = None
        for y in value:
            y._psrtype = self
        self._power_system_resource = value

    power_system_resource = property(get_power_system_resource, set_power_system_resource)

    def add_power_system_resource(self, *power_system_resource):
        for obj in power_system_resource:
            obj._psrtype = self
            self._power_system_resource.append(obj)

    def remove_power_system_resource(self, *power_system_resource):
        for obj in power_system_resource:
            obj._psrtype = None
            self._power_system_resource.remove(obj)
    # >>> power_system_resource


    def __str__(self):
        """ Returns a string representation of the PSRType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< psrtype.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PSRType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PSRType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.power_system_resource:
            s += '%s<%s:PSRType.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PSRType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> psrtype.serialize


class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """
    # <<< geographical_region
    # @generated
    def __init__(self, regions=None, **kw_args):
        """ Initialises a new 'GeographicalRegion' instance.
        """

        self._regions = []
        if regions is not None:
            self.regions = regions
        else:
            self.regions = []


        super(GeographicalRegion, self).__init__(**kw_args)
    # >>> geographical_region

    # <<< regions
    # @generated
    def get_regions(self):
        """ The association is used in the naming hierarchy.
        """
        return self._regions

    def set_regions(self, value):
        for x in self._regions:
            x._region = None
        for y in value:
            y._region = self
        self._regions = value

    regions = property(get_regions, set_regions)

    def add_regions(self, *regions):
        for obj in regions:
            obj._region = self
            self._regions.append(obj)

    def remove_regions(self, *regions):
        for obj in regions:
            obj._region = None
            self._regions.remove(obj)
    # >>> regions


    def __str__(self):
        """ Returns a string representation of the GeographicalRegion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< geographical_region.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeographicalRegion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeographicalRegion", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.regions:
            s += '%s<%s:GeographicalRegion.regions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> geographical_region.serialize


class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """
    # <<< terminal
    # @generated
    def __init__(self, connected=False, sequence_number=0, branch_group_terminal=None, regulating_control=None, has_first_mutual_coupling=None, sv_power_flow=None, tie_flow=None, operational_limit_set=None, topological_node=None, conducting_equipment=None, has_second_mutual_coupling=None, connectivity_node=None, measurements=None, **kw_args):
        """ Initialises a new 'Terminal' instance.
        """
        # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.
        self.connected = connected

        # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
        self.sequence_number = sequence_number


        self._branch_group_terminal = []
        if branch_group_terminal is not None:
            self.branch_group_terminal = branch_group_terminal
        else:
            self.branch_group_terminal = []

        self._regulating_control = []
        if regulating_control is not None:
            self.regulating_control = regulating_control
        else:
            self.regulating_control = []

        self._has_first_mutual_coupling = []
        if has_first_mutual_coupling is not None:
            self.has_first_mutual_coupling = has_first_mutual_coupling
        else:
            self.has_first_mutual_coupling = []

        self._sv_power_flow = None
        self.sv_power_flow = sv_power_flow

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []

        self._topological_node = None
        self.topological_node = topological_node

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._has_second_mutual_coupling = []
        if has_second_mutual_coupling is not None:
            self.has_second_mutual_coupling = has_second_mutual_coupling
        else:
            self.has_second_mutual_coupling = []

        self._connectivity_node = None
        self.connectivity_node = connectivity_node

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(Terminal, self).__init__(**kw_args)
    # >>> terminal

    # <<< branch_group_terminal
    # @generated
    def get_branch_group_terminal(self):
        """ The directed branch group terminals for which the terminal is monitored.
        """
        return self._branch_group_terminal

    def set_branch_group_terminal(self, value):
        for x in self._branch_group_terminal:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._branch_group_terminal = value

    branch_group_terminal = property(get_branch_group_terminal, set_branch_group_terminal)

    def add_branch_group_terminal(self, *branch_group_terminal):
        for obj in branch_group_terminal:
            obj._terminal = self
            self._branch_group_terminal.append(obj)

    def remove_branch_group_terminal(self, *branch_group_terminal):
        for obj in branch_group_terminal:
            obj._terminal = None
            self._branch_group_terminal.remove(obj)
    # >>> branch_group_terminal

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ The terminal is regulated by a control.
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        for x in self._regulating_control:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._regulating_control = value

    regulating_control = property(get_regulating_control, set_regulating_control)

    def add_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._terminal = self
            self._regulating_control.append(obj)

    def remove_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._terminal = None
            self._regulating_control.remove(obj)
    # >>> regulating_control

    # <<< has_first_mutual_coupling
    # @generated
    def get_has_first_mutual_coupling(self):
        """ Mutual couplings associated with the branch as the first branch.
        """
        return self._has_first_mutual_coupling

    def set_has_first_mutual_coupling(self, value):
        for x in self._has_first_mutual_coupling:
            x._first_terminal = None
        for y in value:
            y._first_terminal = self
        self._has_first_mutual_coupling = value

    has_first_mutual_coupling = property(get_has_first_mutual_coupling, set_has_first_mutual_coupling)

    def add_has_first_mutual_coupling(self, *has_first_mutual_coupling):
        for obj in has_first_mutual_coupling:
            obj._first_terminal = self
            self._has_first_mutual_coupling.append(obj)

    def remove_has_first_mutual_coupling(self, *has_first_mutual_coupling):
        for obj in has_first_mutual_coupling:
            obj._first_terminal = None
            self._has_first_mutual_coupling.remove(obj)
    # >>> has_first_mutual_coupling

    # <<< sv_power_flow
    # @generated
    def get_sv_power_flow(self):
        """ The power flow state associated with the terminal.
        """
        return self._sv_power_flow

    def set_sv_power_flow(self, value):
        if self._sv_power_flow is not None:
            self._sv_power_flow._terminal = None

        self._sv_power_flow = value
        if self._sv_power_flow is not None:
            self._sv_power_flow._terminal = self

    sv_power_flow = property(get_sv_power_flow, set_sv_power_flow)
    # >>> sv_power_flow

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The control area tie flows to which this terminal associates.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        for x in self._tie_flow:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._tie_flow = value

    tie_flow = property(get_tie_flow, set_tie_flow)

    def add_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._terminal = self
            self._tie_flow.append(obj)

    def remove_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._terminal = None
            self._tie_flow.remove(obj)
    # >>> tie_flow

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        for x in self._operational_limit_set:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._operational_limit_set = value

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)

    def add_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._terminal = self
            self._operational_limit_set.append(obj)

    def remove_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._terminal = None
            self._operational_limit_set.remove(obj)
    # >>> operational_limit_set

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            filtered = [x for x in self.topological_node.terminal if x != self]
            self._topological_node._terminal = filtered

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._terminal.append(self)

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            filtered = [x for x in self.conducting_equipment.terminals if x != self]
            self._conducting_equipment._terminals = filtered

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._terminals.append(self)

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment

    # <<< has_second_mutual_coupling
    # @generated
    def get_has_second_mutual_coupling(self):
        """ Mutual couplings with the branch associated as the first branch.
        """
        return self._has_second_mutual_coupling

    def set_has_second_mutual_coupling(self, value):
        for x in self._has_second_mutual_coupling:
            x._second_terminal = None
        for y in value:
            y._second_terminal = self
        self._has_second_mutual_coupling = value

    has_second_mutual_coupling = property(get_has_second_mutual_coupling, set_has_second_mutual_coupling)

    def add_has_second_mutual_coupling(self, *has_second_mutual_coupling):
        for obj in has_second_mutual_coupling:
            obj._second_terminal = self
            self._has_second_mutual_coupling.append(obj)

    def remove_has_second_mutual_coupling(self, *has_second_mutual_coupling):
        for obj in has_second_mutual_coupling:
            obj._second_terminal = None
            self._has_second_mutual_coupling.remove(obj)
    # >>> has_second_mutual_coupling

    # <<< connectivity_node
    # @generated
    def get_connectivity_node(self):
        """ Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._connectivity_node

    def set_connectivity_node(self, value):
        if self._connectivity_node is not None:
            filtered = [x for x in self.connectivity_node.terminals if x != self]
            self._connectivity_node._terminals = filtered

        self._connectivity_node = value
        if self._connectivity_node is not None:
            self._connectivity_node._terminals.append(self)

    connectivity_node = property(get_connectivity_node, set_connectivity_node)
    # >>> connectivity_node

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._terminal = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._terminal = None
            self._measurements.remove(obj)
    # >>> measurements


    def __str__(self):
        """ Returns a string representation of the Terminal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< terminal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Terminal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Terminal", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.branch_group_terminal:
            s += '%s<%s:Terminal.branch_group_terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.regulating_control:
            s += '%s<%s:Terminal.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.has_first_mutual_coupling:
            s += '%s<%s:Terminal.has_first_mutual_coupling rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sv_power_flow is not None:
            s += '%s<%s:Terminal.sv_power_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_power_flow.uri)
        for obj in self.tie_flow:
            s += '%s<%s:Terminal.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Terminal.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.topological_node is not None:
            s += '%s<%s:Terminal.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_node.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:Terminal.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        for obj in self.has_second_mutual_coupling:
            s += '%s<%s:Terminal.has_second_mutual_coupling rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.connectivity_node is not None:
            s += '%s<%s:Terminal.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node.uri)
        for obj in self.measurements:
            s += '%s<%s:Terminal.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Terminal.connected>%s</%s:Terminal.connected>' % \
            (indent, ns_prefix, self.connected, ns_prefix)
        s += '%s<%s:Terminal.sequence_number>%s</%s:Terminal.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Terminal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> terminal.serialize


class OperatingParticipant(IdentifiedObject):
    """ An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """
    # <<< operating_participant
    # @generated
    def __init__(self, operating_share=None, **kw_args):
        """ Initialises a new 'OperatingParticipant' instance.
        """

        self._operating_share = []
        if operating_share is not None:
            self.operating_share = operating_share
        else:
            self.operating_share = []


        super(OperatingParticipant, self).__init__(**kw_args)
    # >>> operating_participant

    # <<< operating_share
    # @generated
    def get_operating_share(self):
        """ The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """
        return self._operating_share

    def set_operating_share(self, value):
        for x in self._operating_share:
            x._operating_participant = None
        for y in value:
            y._operating_participant = self
        self._operating_share = value

    operating_share = property(get_operating_share, set_operating_share)

    def add_operating_share(self, *operating_share):
        for obj in operating_share:
            obj._operating_participant = self
            self._operating_share.append(obj)

    def remove_operating_share(self, *operating_share):
        for obj in operating_share:
            obj._operating_participant = None
            self._operating_share.remove(obj)
    # >>> operating_share


    def __str__(self):
        """ Returns a string representation of the OperatingParticipant.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operating_participant.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperatingParticipant.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperatingParticipant", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operating_share:
            s += '%s<%s:OperatingParticipant.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperatingParticipant")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operating_participant.serialize


class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, high_voltage_limit=0.0, low_voltage_limit=0.0, base_voltage=None, member_of_substation=None, contains_bays=None, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.
        """
        # The bus bar's high voltage limit
        self.high_voltage_limit = high_voltage_limit

        # The bus bar's low voltage limit
        self.low_voltage_limit = low_voltage_limit


        self._base_voltage = None
        self.base_voltage = base_voltage

        self._member_of_substation = None
        self.member_of_substation = member_of_substation

        self._contains_bays = []
        if contains_bays is not None:
            self.contains_bays = contains_bays
        else:
            self.contains_bays = []


        super(VoltageLevel, self).__init__(**kw_args)
    # >>> voltage_level

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ The base voltage used for all equipment within the VoltageLevel.
        """
        return self._base_voltage

    def set_base_voltage(self, value):
        if self._base_voltage is not None:
            filtered = [x for x in self.base_voltage.voltage_level if x != self]
            self._base_voltage._voltage_level = filtered

        self._base_voltage = value
        if self._base_voltage is not None:
            self._base_voltage._voltage_level.append(self)

    base_voltage = property(get_base_voltage, set_base_voltage)
    # >>> base_voltage

    # <<< member_of_substation
    # @generated
    def get_member_of_substation(self):
        """ The association is used in the naming hierarchy.
        """
        return self._member_of_substation

    def set_member_of_substation(self, value):
        if self._member_of_substation is not None:
            filtered = [x for x in self.member_of_substation.contains_voltage_levels if x != self]
            self._member_of_substation._contains_voltage_levels = filtered

        self._member_of_substation = value
        if self._member_of_substation is not None:
            self._member_of_substation._contains_voltage_levels.append(self)

    member_of_substation = property(get_member_of_substation, set_member_of_substation)
    # >>> member_of_substation

    # <<< contains_bays
    # @generated
    def get_contains_bays(self):
        """ The association is used in the naming hierarchy.
        """
        return self._contains_bays

    def set_contains_bays(self, value):
        for x in self._contains_bays:
            x._member_of_voltage_level = None
        for y in value:
            y._member_of_voltage_level = self
        self._contains_bays = value

    contains_bays = property(get_contains_bays, set_contains_bays)

    def add_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_voltage_level = self
            self._contains_bays.append(obj)

    def remove_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_voltage_level = None
            self._contains_bays.remove(obj)
    # >>> contains_bays


    def __str__(self):
        """ Returns a string representation of the VoltageLevel.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_level.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageLevel.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageLevel", self.uri)
        if format:
            indent += ' ' * depth

        if self.base_voltage is not None:
            s += '%s<%s:VoltageLevel.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        if self.member_of_substation is not None:
            s += '%s<%s:VoltageLevel.member_of_substation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_substation.uri)
        for obj in self.contains_bays:
            s += '%s<%s:VoltageLevel.contains_bays rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:VoltageLevel.high_voltage_limit>%s</%s:VoltageLevel.high_voltage_limit>' % \
            (indent, ns_prefix, self.high_voltage_limit, ns_prefix)
        s += '%s<%s:VoltageLevel.low_voltage_limit>%s</%s:VoltageLevel.low_voltage_limit>' % \
            (indent, ns_prefix, self.low_voltage_limit, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageLevel")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_level.serialize


class BasePower(IdentifiedObject):
    """ The BasePower class defines the base power used in the per unit calculations.
    """
    # <<< base_power
    # @generated
    def __init__(self, base_power=0.0, **kw_args):
        """ Initialises a new 'BasePower' instance.
        """
        # Definition of base power.
        self.base_power = base_power



        super(BasePower, self).__init__(**kw_args)
    # >>> base_power


    def __str__(self):
        """ Returns a string representation of the BasePower.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< base_power.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BasePower.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BasePower", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BasePower.base_power>%s</%s:BasePower.base_power>' % \
            (indent, ns_prefix, self.base_power, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BasePower")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> base_power.serialize


class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """
    # <<< unit
    # @generated
    def __init__(self, measurements=None, controls=None, protection_equipments=None, **kw_args):
        """ Initialises a new 'Unit' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._controls = []
        if controls is not None:
            self.controls = controls
        else:
            self.controls = []

        self._protection_equipments = []
        if protection_equipments is not None:
            self.protection_equipments = protection_equipments
        else:
            self.protection_equipments = []


        super(Unit, self).__init__(**kw_args)
    # >>> unit

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements having the Unit
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._unit = None
        for y in value:
            y._unit = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._unit = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._unit = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< controls
    # @generated
    def get_controls(self):
        """ The Controls having the Unit.
        """
        return self._controls

    def set_controls(self, value):
        for x in self._controls:
            x._unit = None
        for y in value:
            y._unit = self
        self._controls = value

    controls = property(get_controls, set_controls)

    def add_controls(self, *controls):
        for obj in controls:
            obj._unit = self
            self._controls.append(obj)

    def remove_controls(self, *controls):
        for obj in controls:
            obj._unit = None
            self._controls.remove(obj)
    # >>> controls

    # <<< protection_equipments
    # @generated
    def get_protection_equipments(self):
        """ The Protection Equipments having the Unit.
        """
        return self._protection_equipments

    def set_protection_equipments(self, value):
        for x in self._protection_equipments:
            x._unit = None
        for y in value:
            y._unit = self
        self._protection_equipments = value

    protection_equipments = property(get_protection_equipments, set_protection_equipments)

    def add_protection_equipments(self, *protection_equipments):
        for obj in protection_equipments:
            obj._unit = self
            self._protection_equipments.append(obj)

    def remove_protection_equipments(self, *protection_equipments):
        for obj in protection_equipments:
            obj._unit = None
            self._protection_equipments.remove(obj)
    # >>> protection_equipments


    def __str__(self):
        """ Returns a string representation of the Unit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Unit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Unit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:Unit.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.controls:
            s += '%s<%s:Unit.controls rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.protection_equipments:
            s += '%s<%s:Unit.protection_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Unit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> unit.serialize


class ModelingAuthority(IdentifiedObject):
    """ A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """
    # <<< modeling_authority
    # @generated
    def __init__(self, modeling_authority_sets=None, **kw_args):
        """ Initialises a new 'ModelingAuthority' instance.
        """

        self._modeling_authority_sets = []
        if modeling_authority_sets is not None:
            self.modeling_authority_sets = modeling_authority_sets
        else:
            self.modeling_authority_sets = []


        super(ModelingAuthority, self).__init__(**kw_args)
    # >>> modeling_authority

    # <<< modeling_authority_sets
    # @generated
    def get_modeling_authority_sets(self):
        """ A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._modeling_authority_sets

    def set_modeling_authority_sets(self, value):
        for x in self._modeling_authority_sets:
            x._modeling_authority = None
        for y in value:
            y._modeling_authority = self
        self._modeling_authority_sets = value

    modeling_authority_sets = property(get_modeling_authority_sets, set_modeling_authority_sets)

    def add_modeling_authority_sets(self, *modeling_authority_sets):
        for obj in modeling_authority_sets:
            obj._modeling_authority = self
            self._modeling_authority_sets.append(obj)

    def remove_modeling_authority_sets(self, *modeling_authority_sets):
        for obj in modeling_authority_sets:
            obj._modeling_authority = None
            self._modeling_authority_sets.remove(obj)
    # >>> modeling_authority_sets


    def __str__(self):
        """ Returns a string representation of the ModelingAuthority.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< modeling_authority.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ModelingAuthority.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ModelingAuthority", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.modeling_authority_sets:
            s += '%s<%s:ModelingAuthority.modeling_authority_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ModelingAuthority")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> modeling_authority.serialize


class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """
    # <<< base_voltage
    # @generated
    def __init__(self, nominal_voltage=0.0, is_dc=False, voltage_level=None, topological_node=None, conducting_equipment=None, **kw_args):
        """ Initialises a new 'BaseVoltage' instance.
        """
        # The PowerSystemResource's base voltage.
        self.nominal_voltage = nominal_voltage

        # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
        self.is_dc = is_dc


        self._voltage_level = []
        if voltage_level is not None:
            self.voltage_level = voltage_level
        else:
            self.voltage_level = []

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []

        self._conducting_equipment = []
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
        else:
            self.conducting_equipment = []


        super(BaseVoltage, self).__init__(**kw_args)
    # >>> base_voltage

    # <<< voltage_level
    # @generated
    def get_voltage_level(self):
        """ The VoltageLevels having this BaseVoltage.
        """
        return self._voltage_level

    def set_voltage_level(self, value):
        for x in self._voltage_level:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._voltage_level = value

    voltage_level = property(get_voltage_level, set_voltage_level)

    def add_voltage_level(self, *voltage_level):
        for obj in voltage_level:
            obj._base_voltage = self
            self._voltage_level.append(obj)

    def remove_voltage_level(self, *voltage_level):
        for obj in voltage_level:
            obj._base_voltage = None
            self._voltage_level.remove(obj)
    # >>> voltage_level

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes at the base voltage.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._base_voltage = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._base_voltage = None
            self._topological_node.remove(obj)
    # >>> topological_node

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        for x in self._conducting_equipment:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._conducting_equipment = value

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)

    def add_conducting_equipment(self, *conducting_equipment):
        for obj in conducting_equipment:
            obj._base_voltage = self
            self._conducting_equipment.append(obj)

    def remove_conducting_equipment(self, *conducting_equipment):
        for obj in conducting_equipment:
            obj._base_voltage = None
            self._conducting_equipment.remove(obj)
    # >>> conducting_equipment


    def __str__(self):
        """ Returns a string representation of the BaseVoltage.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< base_voltage.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BaseVoltage.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BaseVoltage", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.voltage_level:
            s += '%s<%s:BaseVoltage.voltage_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.topological_node:
            s += '%s<%s:BaseVoltage.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conducting_equipment:
            s += '%s<%s:BaseVoltage.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BaseVoltage.nominal_voltage>%s</%s:BaseVoltage.nominal_voltage>' % \
            (indent, ns_prefix, self.nominal_voltage, ns_prefix)
        s += '%s<%s:BaseVoltage.is_dc>%s</%s:BaseVoltage.is_dc>' % \
            (indent, ns_prefix, self.is_dc, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BaseVoltage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> base_voltage.serialize


class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region
    # @generated
    def __init__(self, lines=None, substations=None, region=None, **kw_args):
        """ Initialises a new 'SubGeographicalRegion' instance.
        """

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []

        self._substations = []
        if substations is not None:
            self.substations = substations
        else:
            self.substations = []

        self._region = None
        self.region = region


        super(SubGeographicalRegion, self).__init__(**kw_args)
    # >>> sub_geographical_region

    # <<< lines
    # @generated
    def get_lines(self):
        """ A Line can be contained by a SubGeographical Region.
        """
        return self._lines

    def set_lines(self, value):
        for x in self._lines:
            x._region = None
        for y in value:
            y._region = self
        self._lines = value

    lines = property(get_lines, set_lines)

    def add_lines(self, *lines):
        for obj in lines:
            obj._region = self
            self._lines.append(obj)

    def remove_lines(self, *lines):
        for obj in lines:
            obj._region = None
            self._lines.remove(obj)
    # >>> lines

    # <<< substations
    # @generated
    def get_substations(self):
        """ The association is used in the naming hierarchy.
        """
        return self._substations

    def set_substations(self, value):
        for x in self._substations:
            x._region = None
        for y in value:
            y._region = self
        self._substations = value

    substations = property(get_substations, set_substations)

    def add_substations(self, *substations):
        for obj in substations:
            obj._region = self
            self._substations.append(obj)

    def remove_substations(self, *substations):
        for obj in substations:
            obj._region = None
            self._substations.remove(obj)
    # >>> substations

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.regions if x != self]
            self._region._regions = filtered

        self._region = value
        if self._region is not None:
            self._region._regions.append(self)

    region = property(get_region, set_region)
    # >>> region


    def __str__(self):
        """ Returns a string representation of the SubGeographicalRegion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sub_geographical_region.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubGeographicalRegion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubGeographicalRegion", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.lines:
            s += '%s<%s:SubGeographicalRegion.lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.substations:
            s += '%s<%s:SubGeographicalRegion.substations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.region is not None:
            s += '%s<%s:SubGeographicalRegion.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubGeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sub_geographical_region.serialize


class PsrList(IdentifiedObject):
    """ Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """
    # <<< psr_list
    # @generated
    def __init__(self, type_psrlist='', power_system_resources=None, **kw_args):
        """ Initialises a new 'PsrList' instance.
        """
        # Type of power system resources in this list.
        self.type_psrlist = type_psrlist


        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(PsrList, self).__init__(**kw_args)
    # >>> psr_list

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for p in self._power_system_resources:
            filtered = [q for q in p.psr_lists if q != self]
            self._power_system_resources._psr_lists = filtered
        for r in value:
            if self not in r._psr_lists:
                r._psr_lists.append(self)
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self not in obj._psr_lists:
                obj._psr_lists.append(self)
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self in obj._psr_lists:
                obj._psr_lists.remove(self)
            self._power_system_resources.remove(obj)
    # >>> power_system_resources


    def __str__(self):
        """ Returns a string representation of the PsrList.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< psr_list.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PsrList.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PsrList", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.power_system_resources:
            s += '%s<%s:PsrList.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PsrList.type_psrlist>%s</%s:PsrList.type_psrlist>' % \
            (indent, ns_prefix, self.type_psrlist, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PsrList")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> psr_list.serialize


class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, contains_bays=None, contains_voltage_levels=None, region=None, **kw_args):
        """ Initialises a new 'Substation' instance.
        """

        self._contains_bays = []
        if contains_bays is not None:
            self.contains_bays = contains_bays
        else:
            self.contains_bays = []

        self._contains_voltage_levels = []
        if contains_voltage_levels is not None:
            self.contains_voltage_levels = contains_voltage_levels
        else:
            self.contains_voltage_levels = []

        self._region = None
        self.region = region


        super(Substation, self).__init__(**kw_args)
    # >>> substation

    # <<< contains_bays
    # @generated
    def get_contains_bays(self):
        """ The association is used in the naming hierarchy.
        """
        return self._contains_bays

    def set_contains_bays(self, value):
        for x in self._contains_bays:
            x._member_of_substation = None
        for y in value:
            y._member_of_substation = self
        self._contains_bays = value

    contains_bays = property(get_contains_bays, set_contains_bays)

    def add_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_substation = self
            self._contains_bays.append(obj)

    def remove_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_substation = None
            self._contains_bays.remove(obj)
    # >>> contains_bays

    # <<< contains_voltage_levels
    # @generated
    def get_contains_voltage_levels(self):
        """ The association is used in the naming hierarchy.
        """
        return self._contains_voltage_levels

    def set_contains_voltage_levels(self, value):
        for x in self._contains_voltage_levels:
            x._member_of_substation = None
        for y in value:
            y._member_of_substation = self
        self._contains_voltage_levels = value

    contains_voltage_levels = property(get_contains_voltage_levels, set_contains_voltage_levels)

    def add_contains_voltage_levels(self, *contains_voltage_levels):
        for obj in contains_voltage_levels:
            obj._member_of_substation = self
            self._contains_voltage_levels.append(obj)

    def remove_contains_voltage_levels(self, *contains_voltage_levels):
        for obj in contains_voltage_levels:
            obj._member_of_substation = None
            self._contains_voltage_levels.remove(obj)
    # >>> contains_voltage_levels

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.substations if x != self]
            self._region._substations = filtered

        self._region = value
        if self._region is not None:
            self._region._substations.append(self)

    region = property(get_region, set_region)
    # >>> region


    def __str__(self):
        """ Returns a string representation of the Substation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< substation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Substation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Substation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_bays:
            s += '%s<%s:Substation.contains_bays rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_voltage_levels:
            s += '%s<%s:Substation.contains_voltage_levels rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.region is not None:
            s += '%s<%s:Substation.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Substation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> substation.serialize


class ReportingGroup(IdentifiedObject):
    """ A reporting group is used for various ad-hoc groupings used for reporting.
    """
    # <<< reporting_group
    # @generated
    def __init__(self, topological_node=None, reporting_super_group=None, power_system_resource=None, bus_name_marker=None, **kw_args):
        """ Initialises a new 'ReportingGroup' instance.
        """

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []

        self._reporting_super_group = None
        self.reporting_super_group = reporting_super_group

        self._power_system_resource = []
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        else:
            self.power_system_resource = []

        self._bus_name_marker = []
        if bus_name_marker is not None:
            self.bus_name_marker = bus_name_marker
        else:
            self.bus_name_marker = []


        super(ReportingGroup, self).__init__(**kw_args)
    # >>> reporting_group

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes that belong to the reporting group.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._reporting_group = None
        for y in value:
            y._reporting_group = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._reporting_group = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._reporting_group = None
            self._topological_node.remove(obj)
    # >>> topological_node

    # <<< reporting_super_group
    # @generated
    def get_reporting_super_group(self):
        """ Reporting super group to which this reporting group belongs.
        """
        return self._reporting_super_group

    def set_reporting_super_group(self, value):
        if self._reporting_super_group is not None:
            filtered = [x for x in self.reporting_super_group.reporting_group if x != self]
            self._reporting_super_group._reporting_group = filtered

        self._reporting_super_group = value
        if self._reporting_super_group is not None:
            self._reporting_super_group._reporting_group.append(self)

    reporting_super_group = property(get_reporting_super_group, set_reporting_super_group)
    # >>> reporting_super_group

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ PSR's which belong to this reporting group.
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        for p in self._power_system_resource:
            filtered = [q for q in p.reporting_group if q != self]
            self._power_system_resource._reporting_group = filtered
        for r in value:
            if self not in r._reporting_group:
                r._reporting_group.append(self)
        self._power_system_resource = value

    power_system_resource = property(get_power_system_resource, set_power_system_resource)

    def add_power_system_resource(self, *power_system_resource):
        for obj in power_system_resource:
            if self not in obj._reporting_group:
                obj._reporting_group.append(self)
            self._power_system_resource.append(obj)

    def remove_power_system_resource(self, *power_system_resource):
        for obj in power_system_resource:
            if self in obj._reporting_group:
                obj._reporting_group.remove(self)
            self._power_system_resource.remove(obj)
    # >>> power_system_resource

    # <<< bus_name_marker
    # @generated
    def get_bus_name_marker(self):
        """ The BusNameMarkers that belong to this reporting group.
        """
        return self._bus_name_marker

    def set_bus_name_marker(self, value):
        for x in self._bus_name_marker:
            x._reporting_group = None
        for y in value:
            y._reporting_group = self
        self._bus_name_marker = value

    bus_name_marker = property(get_bus_name_marker, set_bus_name_marker)

    def add_bus_name_marker(self, *bus_name_marker):
        for obj in bus_name_marker:
            obj._reporting_group = self
            self._bus_name_marker.append(obj)

    def remove_bus_name_marker(self, *bus_name_marker):
        for obj in bus_name_marker:
            obj._reporting_group = None
            self._bus_name_marker.remove(obj)
    # >>> bus_name_marker


    def __str__(self):
        """ Returns a string representation of the ReportingGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reporting_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReportingGroup.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReportingGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.topological_node:
            s += '%s<%s:ReportingGroup.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.reporting_super_group is not None:
            s += '%s<%s:ReportingGroup.reporting_super_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reporting_super_group.uri)
        for obj in self.power_system_resource:
            s += '%s<%s:ReportingGroup.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.bus_name_marker:
            s += '%s<%s:ReportingGroup.bus_name_marker rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReportingGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reporting_group.serialize


class Company(IdentifiedObject):
    """ A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts.
    """
    # <<< company
    # @generated
    def __init__(self, company_type='pool', operates_psrs=None, **kw_args):
        """ Initialises a new 'Company' instance.
        """
        # The type of company. Values are: "pool", "municipal", "is_private"
        self.company_type = 'pool'


        self._operates_psrs = []
        if operates_psrs is not None:
            self.operates_psrs = operates_psrs
        else:
            self.operates_psrs = []


        super(Company, self).__init__(**kw_args)
    # >>> company

    # <<< operates_psrs
    # @generated
    def get_operates_psrs(self):
        """ PowerSystemResources the Company operates.
        """
        return self._operates_psrs

    def set_operates_psrs(self, value):
        for p in self._operates_psrs:
            filtered = [q for q in p.operated_by_companies if q != self]
            self._operates_psrs._operated_by_companies = filtered
        for r in value:
            if self not in r._operated_by_companies:
                r._operated_by_companies.append(self)
        self._operates_psrs = value

    operates_psrs = property(get_operates_psrs, set_operates_psrs)

    def add_operates_psrs(self, *operates_psrs):
        for obj in operates_psrs:
            if self not in obj._operated_by_companies:
                obj._operated_by_companies.append(self)
            self._operates_psrs.append(obj)

    def remove_operates_psrs(self, *operates_psrs):
        for obj in operates_psrs:
            if self in obj._operated_by_companies:
                obj._operated_by_companies.remove(self)
            self._operates_psrs.remove(obj)
    # >>> operates_psrs


    def __str__(self):
        """ Returns a string representation of the Company.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< company.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Company.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Company", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operates_psrs:
            s += '%s<%s:Company.operates_psrs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Company.company_type>%s</%s:Company.company_type>' % \
            (indent, ns_prefix, self.company_type, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Company")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> company.serialize


class ReportingSuperGroup(IdentifiedObject):
    """ A reporting super group, groups reporting groups for a higher level report.
    """
    # <<< reporting_super_group
    # @generated
    def __init__(self, reporting_group=None, **kw_args):
        """ Initialises a new 'ReportingSuperGroup' instance.
        """

        self._reporting_group = []
        if reporting_group is not None:
            self.reporting_group = reporting_group
        else:
            self.reporting_group = []


        super(ReportingSuperGroup, self).__init__(**kw_args)
    # >>> reporting_super_group

    # <<< reporting_group
    # @generated
    def get_reporting_group(self):
        """ Reporting groups that are grouped under this group group.
        """
        return self._reporting_group

    def set_reporting_group(self, value):
        for x in self._reporting_group:
            x._reporting_super_group = None
        for y in value:
            y._reporting_super_group = self
        self._reporting_group = value

    reporting_group = property(get_reporting_group, set_reporting_group)

    def add_reporting_group(self, *reporting_group):
        for obj in reporting_group:
            obj._reporting_super_group = self
            self._reporting_group.append(obj)

    def remove_reporting_group(self, *reporting_group):
        for obj in reporting_group:
            obj._reporting_super_group = None
            self._reporting_group.remove(obj)
    # >>> reporting_group


    def __str__(self):
        """ Returns a string representation of the ReportingSuperGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reporting_super_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReportingSuperGroup.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReportingSuperGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.reporting_group:
            s += '%s<%s:ReportingSuperGroup.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReportingSuperGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reporting_super_group.serialize


class ModelingAuthoritySet(IdentifiedObject):
    """ A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """
    # <<< modeling_authority_set
    # @generated
    def __init__(self, identified_objects=None, modeling_authority=None, **kw_args):
        """ Initialises a new 'ModelingAuthoritySet' instance.
        """

        self._identified_objects = []
        if identified_objects is not None:
            self.identified_objects = identified_objects
        else:
            self.identified_objects = []

        self._modeling_authority = None
        self.modeling_authority = modeling_authority


        super(ModelingAuthoritySet, self).__init__(**kw_args)
    # >>> modeling_authority_set

    # <<< identified_objects
    # @generated
    def get_identified_objects(self):
        """ An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._identified_objects

    def set_identified_objects(self, value):
        for x in self._identified_objects:
            x._modeling_authority_set = None
        for y in value:
            y._modeling_authority_set = self
        self._identified_objects = value

    identified_objects = property(get_identified_objects, set_identified_objects)

    def add_identified_objects(self, *identified_objects):
        for obj in identified_objects:
            obj._modeling_authority_set = self
            self._identified_objects.append(obj)

    def remove_identified_objects(self, *identified_objects):
        for obj in identified_objects:
            obj._modeling_authority_set = None
            self._identified_objects.remove(obj)
    # >>> identified_objects

    # <<< modeling_authority
    # @generated
    def get_modeling_authority(self):
        """ A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._modeling_authority

    def set_modeling_authority(self, value):
        if self._modeling_authority is not None:
            filtered = [x for x in self.modeling_authority.modeling_authority_sets if x != self]
            self._modeling_authority._modeling_authority_sets = filtered

        self._modeling_authority = value
        if self._modeling_authority is not None:
            self._modeling_authority._modeling_authority_sets.append(self)

    modeling_authority = property(get_modeling_authority, set_modeling_authority)
    # >>> modeling_authority


    def __str__(self):
        """ Returns a string representation of the ModelingAuthoritySet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< modeling_authority_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ModelingAuthoritySet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ModelingAuthoritySet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.identified_objects:
            s += '%s<%s:ModelingAuthoritySet.identified_objects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.modeling_authority is not None:
            s += '%s<%s:ModelingAuthoritySet.modeling_authority rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ModelingAuthoritySet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> modeling_authority_set.serialize


# <<< core
# @generated
# >>> core
