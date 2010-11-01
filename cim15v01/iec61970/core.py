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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from cim15v01 import Element

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
    def __init__(self, description='', m_rid='', name='', path_name='', local_name='', alias_name='', modeling_authority_set=None, *args, **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.

        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param m_rid: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param path_name: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        @param local_name: The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        @param alias_name: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        @param modeling_authority_set: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. 
        self.m_rid = m_rid

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.name = name

        # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        self.path_name = path_name

        # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        self.local_name = local_name

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        self.alias_name = alias_name


        self._modeling_authority_set = None
        self.modeling_authority_set = modeling_authority_set


        super(IdentifiedObject, self).__init__(*args, **kw_args)
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



class IrregularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points varies.
    """
    # <<< irregular_time_point
    # @generated
    def __init__(self, time=0.0, value1=0.0, value2=0.0, interval_schedule=None, *args, **kw_args):
        """ Initialises a new 'IrregularTimePoint' instance.

        @param time: The time is relative the BasicTimeSchedule.startTime. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param interval_schedule: An IrregularTimePoint belongs to an IrregularIntervalSchedule.
        """
        # The time is relative the BasicTimeSchedule.startTime. 
        self.time = time

        # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        self.value1 = value1

        # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        self.value2 = value2


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(IrregularTimePoint, self).__init__(*args, **kw_args)
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



class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.
    """
    # <<< regular_time_point
    # @generated
    def __init__(self, value2=0.0, sequence_number=0, value1=0.0, interval_schedule=None, *args, **kw_args):
        """ Initialises a new 'RegularTimePoint' instance.

        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param sequence_number: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param interval_schedule: A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value2 = value2

        # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        self.sequence_number = sequence_number

        # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value1 = value1


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(RegularTimePoint, self).__init__(*args, **kw_args)
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



class CurveData(Element):
    """ Multi-purpose data points for defining a curve.
    """
    # <<< curve_data
    # @generated
    def __init__(self, y1value=0.0, y2value=0.0, y3value=0.0, xvalue=0.0, curve=None, *args, **kw_args):
        """ Initialises a new 'CurveData' instance.

        @param y1value: The data value of the  first Y-axis variable, depending on the Y-axis units 
        @param y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        @param y3value: The data value of the third Y-axis variable (if present), depending on the Y-axis units 
        @param xvalue: The data value of the X-axis variable,  depending on the X-axis units 
        @param curve: The Curve defined by this CurveData.
        """
        # The data value of the  first Y-axis variable, depending on the Y-axis units 
        self.y1value = y1value

        # The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        self.y2value = y2value

        # The data value of the third Y-axis variable (if present), depending on the Y-axis units 
        self.y3value = y3value

        # The data value of the X-axis variable,  depending on the X-axis units 
        self.xvalue = xvalue


        self._curve = None
        self.curve = curve


        super(CurveData, self).__init__(*args, **kw_args)
    # >>> curve_data

    # <<< curve
    # @generated
    def get_curve(self):
        """ The Curve defined by this CurveData.
        """
        return self._curve

    def set_curve(self, value):
        if self._curve is not None:
            filtered = [x for x in self.curve.curve_datas if x != self]
            self._curve._curve_datas = filtered

        self._curve = value
        if self._curve is not None:
            self._curve._curve_datas.append(self)

    curve = property(get_curve, set_curve)
    # >>> curve



class OperatingShare(Element):
    """ Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """
    # <<< operating_share
    # @generated
    def __init__(self, percentage=0.0, operating_participant=None, power_system_resource=None, *args, **kw_args):
        """ Initialises a new 'OperatingShare' instance.

        @param percentage: Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%. 
        @param operating_participant: The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        @param power_system_resource: The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        """
        # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%. 
        self.percentage = percentage


        self._operating_participant = None
        self.operating_participant = operating_participant

        self._power_system_resource = None
        self.power_system_resource = power_system_resource


        super(OperatingShare, self).__init__(*args, **kw_args)
    # >>> operating_share

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



class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """
    # <<< geographical_region
    # @generated
    def __init__(self, regions=None, *args, **kw_args):
        """ Initialises a new 'GeographicalRegion' instance.

        @param regions: The association is used in the naming hierarchy.
        """

        self._regions = []
        if regions is not None:
            self.regions = regions
        else:
            self.regions = []


        super(GeographicalRegion, self).__init__(*args, **kw_args)
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



class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """
    # <<< power_system_resource
    # @generated
    def __init__(self, change_items=None, asset_roles=None, geo_location=None, safety_documents=None, outage_schedule=None, measurements=None, erp_organisation_roles=None, psrtype=None, psr_lists=None, psrevent=None, operating_share=None, schedule_steps=None, reporting_group=None, document_roles=None, circuit_sections=None, network_data_sets=None, *args, **kw_args):
        """ Initialises a new 'PowerSystemResource' instance.

        @param change_items:
        @param asset_roles:
        @param geo_location: Geographical location of this power system resource.
        @param safety_documents:
        @param outage_schedule: A power system resource may have an outage schedule
        @param measurements: The Measurements that are included in the naming hierarchy where the PSR is the containing object
        @param erp_organisation_roles:
        @param psrtype: PSRType (custom classification) for this PowerSystemResource.
        @param psr_lists:
        @param psrevent: All events associated with this power system resource.
        @param operating_share: The linkage to any number of operating share objects.
        @param schedule_steps:
        @param reporting_group: Reporting groups to which this PSR belongs.
        @param document_roles:
        @param circuit_sections:
        @param network_data_sets:
        """

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._asset_roles = []
        if asset_roles is not None:
            self.asset_roles = asset_roles
        else:
            self.asset_roles = []

        self._geo_location = None
        self.geo_location = geo_location

        self._safety_documents = []
        if safety_documents is not None:
            self.safety_documents = safety_documents
        else:
            self.safety_documents = []

        self._outage_schedule = None
        self.outage_schedule = outage_schedule

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._psrtype = None
        self.psrtype = psrtype

        self._psr_lists = []
        if psr_lists is not None:
            self.psr_lists = psr_lists
        else:
            self.psr_lists = []

        self._psrevent = []
        if psrevent is not None:
            self.psrevent = psrevent
        else:
            self.psrevent = []

        self._operating_share = []
        if operating_share is not None:
            self.operating_share = operating_share
        else:
            self.operating_share = []

        self._schedule_steps = []
        if schedule_steps is not None:
            self.schedule_steps = schedule_steps
        else:
            self.schedule_steps = []

        self._reporting_group = []
        if reporting_group is not None:
            self.reporting_group = reporting_group
        else:
            self.reporting_group = []

        self._document_roles = []
        if document_roles is not None:
            self.document_roles = document_roles
        else:
            self.document_roles = []

        self._circuit_sections = []
        if circuit_sections is not None:
            self.circuit_sections = circuit_sections
        else:
            self.circuit_sections = []

        self._network_data_sets = []
        if network_data_sets is not None:
            self.network_data_sets = network_data_sets
        else:
            self.network_data_sets = []


        super(PowerSystemResource, self).__init__(*args, **kw_args)
    # >>> power_system_resource

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._power_system_resource = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._power_system_resource = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< asset_roles
    # @generated
    def get_asset_roles(self):
        """ 
        """
        return self._asset_roles

    def set_asset_roles(self, value):
        for x in self._asset_roles:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._asset_roles = value

    asset_roles = property(get_asset_roles, set_asset_roles)

    def add_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._power_system_resource = self
            self._asset_roles.append(obj)

    def remove_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._power_system_resource = None
            self._asset_roles.remove(obj)
    # >>> asset_roles

    # <<< geo_location
    # @generated
    def get_geo_location(self):
        """ Geographical location of this power system resource.
        """
        return self._geo_location

    def set_geo_location(self, value):
        if self._geo_location is not None:
            filtered = [x for x in self.geo_location.power_system_resources if x != self]
            self._geo_location._power_system_resources = filtered

        self._geo_location = value
        if self._geo_location is not None:
            self._geo_location._power_system_resources.append(self)

    geo_location = property(get_geo_location, set_geo_location)
    # >>> geo_location

    # <<< safety_documents
    # @generated
    def get_safety_documents(self):
        """ 
        """
        return self._safety_documents

    def set_safety_documents(self, value):
        for x in self._safety_documents:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._safety_documents = value

    safety_documents = property(get_safety_documents, set_safety_documents)

    def add_safety_documents(self, *safety_documents):
        for obj in safety_documents:
            obj._power_system_resource = self
            self._safety_documents.append(obj)

    def remove_safety_documents(self, *safety_documents):
        for obj in safety_documents:
            obj._power_system_resource = None
            self._safety_documents.remove(obj)
    # >>> safety_documents

    # <<< outage_schedule
    # @generated
    def get_outage_schedule(self):
        """ A power system resource may have an outage schedule
        """
        return self._outage_schedule

    def set_outage_schedule(self, value):
        if self._outage_schedule is not None:
            self._outage_schedule._power_system_resource = None

        self._outage_schedule = value
        if self._outage_schedule is not None:
            self._outage_schedule._power_system_resource = self

    outage_schedule = property(get_outage_schedule, set_outage_schedule)
    # >>> outage_schedule

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._power_system_resource = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._power_system_resource = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for x in self._erp_organisation_roles:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._power_system_resource = self
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._power_system_resource = None
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< psrtype
    # @generated
    def get_psrtype(self):
        """ PSRType (custom classification) for this PowerSystemResource.
        """
        return self._psrtype

    def set_psrtype(self, value):
        if self._psrtype is not None:
            filtered = [x for x in self.psrtype.power_system_resources if x != self]
            self._psrtype._power_system_resources = filtered

        self._psrtype = value
        if self._psrtype is not None:
            self._psrtype._power_system_resources.append(self)

    psrtype = property(get_psrtype, set_psrtype)
    # >>> psrtype

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

    # <<< psrevent
    # @generated
    def get_psrevent(self):
        """ All events associated with this power system resource.
        """
        return self._psrevent

    def set_psrevent(self, value):
        for x in self._psrevent:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._psrevent = value

    psrevent = property(get_psrevent, set_psrevent)

    def add_psrevent(self, *psrevent):
        for obj in psrevent:
            obj._power_system_resource = self
            self._psrevent.append(obj)

    def remove_psrevent(self, *psrevent):
        for obj in psrevent:
            obj._power_system_resource = None
            self._psrevent.remove(obj)
    # >>> psrevent

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

    # <<< schedule_steps
    # @generated
    def get_schedule_steps(self):
        """ 
        """
        return self._schedule_steps

    def set_schedule_steps(self, value):
        for p in self._schedule_steps:
            filtered = [q for q in p.power_system_resources if q != self]
            self._schedule_steps._power_system_resources = filtered
        for r in value:
            if self not in r._power_system_resources:
                r._power_system_resources.append(self)
        self._schedule_steps = value

    schedule_steps = property(get_schedule_steps, set_schedule_steps)

    def add_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            if self not in obj._power_system_resources:
                obj._power_system_resources.append(self)
            self._schedule_steps.append(obj)

    def remove_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            if self in obj._power_system_resources:
                obj._power_system_resources.remove(self)
            self._schedule_steps.remove(obj)
    # >>> schedule_steps

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

    # <<< document_roles
    # @generated
    def get_document_roles(self):
        """ 
        """
        return self._document_roles

    def set_document_roles(self, value):
        for x in self._document_roles:
            x._power_system_resource = None
        for y in value:
            y._power_system_resource = self
        self._document_roles = value

    document_roles = property(get_document_roles, set_document_roles)

    def add_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._power_system_resource = self
            self._document_roles.append(obj)

    def remove_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._power_system_resource = None
            self._document_roles.remove(obj)
    # >>> document_roles

    # <<< circuit_sections
    # @generated
    def get_circuit_sections(self):
        """ 
        """
        return self._circuit_sections

    def set_circuit_sections(self, value):
        for p in self._circuit_sections:
            filtered = [q for q in p.power_system_resources if q != self]
            self._circuit_sections._power_system_resources = filtered
        for r in value:
            if self not in r._power_system_resources:
                r._power_system_resources.append(self)
        self._circuit_sections = value

    circuit_sections = property(get_circuit_sections, set_circuit_sections)

    def add_circuit_sections(self, *circuit_sections):
        for obj in circuit_sections:
            if self not in obj._power_system_resources:
                obj._power_system_resources.append(self)
            self._circuit_sections.append(obj)

    def remove_circuit_sections(self, *circuit_sections):
        for obj in circuit_sections:
            if self in obj._power_system_resources:
                obj._power_system_resources.remove(self)
            self._circuit_sections.remove(obj)
    # >>> circuit_sections

    # <<< network_data_sets
    # @generated
    def get_network_data_sets(self):
        """ 
        """
        return self._network_data_sets

    def set_network_data_sets(self, value):
        for p in self._network_data_sets:
            filtered = [q for q in p.power_system_resources if q != self]
            self._network_data_sets._power_system_resources = filtered
        for r in value:
            if self not in r._power_system_resources:
                r._power_system_resources.append(self)
        self._network_data_sets = value

    network_data_sets = property(get_network_data_sets, set_network_data_sets)

    def add_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self not in obj._power_system_resources:
                obj._power_system_resources.append(self)
            self._network_data_sets.append(obj)

    def remove_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self in obj._power_system_resources:
                obj._power_system_resources.remove(self)
            self._network_data_sets.remove(obj)
    # >>> network_data_sets



class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, normally_in_service=False, contingency_equipment=None, customer_agreements=None, operational_limit_set=None, equipment_container=None, *args, **kw_args):
        """ Initialises a new 'Equipment' instance.

        @param normally_in_service: The equipment is normally in service. 
        @param contingency_equipment: The contingency element associated with the equipment.
        @param customer_agreements:
        @param operational_limit_set: The equipment limit sets associated with the equipment.
        @param equipment_container: The association is used in the naming hierarchy.
        """
        # The equipment is normally in service. 
        self.normally_in_service = normally_in_service


        self._contingency_equipment = []
        if contingency_equipment is not None:
            self.contingency_equipment = contingency_equipment
        else:
            self.contingency_equipment = []

        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []

        self._equipment_container = None
        self.equipment_container = equipment_container


        super(Equipment, self).__init__(*args, **kw_args)
    # >>> equipment

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

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ 
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for p in self._customer_agreements:
            filtered = [q for q in p.equipments if q != self]
            self._customer_agreements._equipments = filtered
        for r in value:
            if self not in r._equipments:
                r._equipments.append(self)
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self not in obj._equipments:
                obj._equipments.append(self)
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self in obj._equipments:
                obj._equipments.remove(self)
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

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

    # <<< equipment_container
    # @generated
    def get_equipment_container(self):
        """ The association is used in the naming hierarchy.
        """
        return self._equipment_container

    def set_equipment_container(self, value):
        if self._equipment_container is not None:
            filtered = [x for x in self.equipment_container.equipments if x != self]
            self._equipment_container._equipments = filtered

        self._equipment_container = value
        if self._equipment_container is not None:
            self._equipment_container._equipments.append(self)

    equipment_container = property(get_equipment_container, set_equipment_container)
    # >>> equipment_container



class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment
    # @generated
    def __init__(self, phases='bc', terminals=None, clearance_tags=None, outage_step_roles=None, base_voltage=None, electrical_assets=None, sv_status=None, protection_equipments=None, *args, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.

        @param phases: Describes the phases carried by a conducting equipment. Values are: "bc", "ab", "b", "ac", "s2_n", "abc", "abn", "abcn", "cn", "an", "bcn", "acn", "a", "c", "n", "s12_n", "bn", "s1_n"
        @param terminals: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param clearance_tags: Conducting equipment may have multiple clearance tags for authorized field work
        @param outage_step_roles:
        @param base_voltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param electrical_assets:
        @param sv_status: The status state associated with the conducting equipment.
        @param protection_equipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        # Describes the phases carried by a conducting equipment. Values are: "bc", "ab", "b", "ac", "s2_n", "abc", "abn", "abcn", "cn", "an", "bcn", "acn", "a", "c", "n", "s12_n", "bn", "s1_n"
        self.phases = phases


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

        self._outage_step_roles = []
        if outage_step_roles is not None:
            self.outage_step_roles = outage_step_roles
        else:
            self.outage_step_roles = []

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._electrical_assets = []
        if electrical_assets is not None:
            self.electrical_assets = electrical_assets
        else:
            self.electrical_assets = []

        self._sv_status = None
        self.sv_status = sv_status

        self._protection_equipments = []
        if protection_equipments is not None:
            self.protection_equipments = protection_equipments
        else:
            self.protection_equipments = []


        super(ConductingEquipment, self).__init__(*args, **kw_args)
    # >>> conducting_equipment

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

    # <<< outage_step_roles
    # @generated
    def get_outage_step_roles(self):
        """ 
        """
        return self._outage_step_roles

    def set_outage_step_roles(self, value):
        for x in self._outage_step_roles:
            x._conducting_equipment = None
        for y in value:
            y._conducting_equipment = self
        self._outage_step_roles = value

    outage_step_roles = property(get_outage_step_roles, set_outage_step_roles)

    def add_outage_step_roles(self, *outage_step_roles):
        for obj in outage_step_roles:
            obj._conducting_equipment = self
            self._outage_step_roles.append(obj)

    def remove_outage_step_roles(self, *outage_step_roles):
        for obj in outage_step_roles:
            obj._conducting_equipment = None
            self._outage_step_roles.remove(obj)
    # >>> outage_step_roles

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

    # <<< electrical_assets
    # @generated
    def get_electrical_assets(self):
        """ 
        """
        return self._electrical_assets

    def set_electrical_assets(self, value):
        for x in self._electrical_assets:
            x._conducting_equipment = None
        for y in value:
            y._conducting_equipment = self
        self._electrical_assets = value

    electrical_assets = property(get_electrical_assets, set_electrical_assets)

    def add_electrical_assets(self, *electrical_assets):
        for obj in electrical_assets:
            obj._conducting_equipment = self
            self._electrical_assets.append(obj)

    def remove_electrical_assets(self, *electrical_assets):
        for obj in electrical_assets:
            obj._conducting_equipment = None
            self._electrical_assets.remove(obj)
    # >>> electrical_assets

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



class Curve(IdentifiedObject):
    """ A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.
    """
    # <<< curve
    # @generated
    def __init__(self, y3_multiplier='m', y2_multiplier='m', x_multiplier='m', y2_unit='m2', curve_style='constant_yvalue', y1_unit='m2', y1_multiplier='m', y3_unit='m2', x_unit='m2', curve_datas=None, *args, **kw_args):
        """ Initialises a new 'Curve' instance.

        @param y3_multiplier: Multiplier for Y3-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param y2_multiplier: Multiplier for Y2-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param x_multiplier: Multiplier for X-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param y2_unit: The Y2-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param curve_style: The style or shape of the curve. Values are: "constant_yvalue", "ramp_yvalue", "formula", "straight_line_yvalues"
        @param y1_unit: The Y1-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param y1_multiplier: Multiplier for Y1-axis Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param y3_unit: The Y3-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param x_unit: The X-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param curve_datas: The point data values that define a curve
        """
        # Multiplier for Y3-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.y3_multiplier = y3_multiplier

        # Multiplier for Y2-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.y2_multiplier = y2_multiplier

        # Multiplier for X-axis. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.x_multiplier = x_multiplier

        # The Y2-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.y2_unit = y2_unit

        # The style or shape of the curve. Values are: "constant_yvalue", "ramp_yvalue", "formula", "straight_line_yvalues"
        self.curve_style = curve_style

        # The Y1-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.y1_unit = y1_unit

        # Multiplier for Y1-axis Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.y1_multiplier = y1_multiplier

        # The Y3-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.y3_unit = y3_unit

        # The X-axis units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.x_unit = x_unit


        self._curve_datas = []
        if curve_datas is not None:
            self.curve_datas = curve_datas
        else:
            self.curve_datas = []


        super(Curve, self).__init__(*args, **kw_args)
    # >>> curve

    # <<< curve_datas
    # @generated
    def get_curve_datas(self):
        """ The point data values that define a curve
        """
        return self._curve_datas

    def set_curve_datas(self, value):
        for x in self._curve_datas:
            x._curve = None
        for y in value:
            y._curve = self
        self._curve_datas = value

    curve_datas = property(get_curve_datas, set_curve_datas)

    def add_curve_datas(self, *curve_datas):
        for obj in curve_datas:
            obj._curve = self
            self._curve_datas.append(obj)

    def remove_curve_datas(self, *curve_datas):
        for obj in curve_datas:
            obj._curve = None
            self._curve_datas.remove(obj)
    # >>> curve_datas



class ReportingSuperGroup(IdentifiedObject):
    """ A reporting super group, groups reporting groups for a higher level report.
    """
    # <<< reporting_super_group
    # @generated
    def __init__(self, reporting_group=None, *args, **kw_args):
        """ Initialises a new 'ReportingSuperGroup' instance.

        @param reporting_group: Reporting groups that are grouped under this group group.
        """

        self._reporting_group = []
        if reporting_group is not None:
            self.reporting_group = reporting_group
        else:
            self.reporting_group = []


        super(ReportingSuperGroup, self).__init__(*args, **kw_args)
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



class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """
    # <<< connectivity_node_container
    # @generated
    def __init__(self, topological_node=None, connectivity_nodes=None, *args, **kw_args):
        """ Initialises a new 'ConnectivityNodeContainer' instance.

        @param topological_node: The topological nodes which belong to this connectivity node container.
        @param connectivity_nodes: Connectivity nodes contained by this container.
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


        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)
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
            x._connectivity_node_container = None
        for y in value:
            y._connectivity_node_container = self
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._connectivity_node_container = self
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._connectivity_node_container = None
            self._connectivity_nodes.remove(obj)
    # >>> connectivity_nodes



class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for containing equipment.
    """
    # <<< equipment_container
    # @generated
    def __init__(self, equipments=None, *args, **kw_args):
        """ Initialises a new 'EquipmentContainer' instance.

        @param equipments: The association is used in the naming hierarchy.
        """

        self._equipments = []
        if equipments is not None:
            self.equipments = equipments
        else:
            self.equipments = []


        super(EquipmentContainer, self).__init__(*args, **kw_args)
    # >>> equipment_container

    # <<< equipments
    # @generated
    def get_equipments(self):
        """ The association is used in the naming hierarchy.
        """
        return self._equipments

    def set_equipments(self, value):
        for x in self._equipments:
            x._equipment_container = None
        for y in value:
            y._equipment_container = self
        self._equipments = value

    equipments = property(get_equipments, set_equipments)

    def add_equipments(self, *equipments):
        for obj in equipments:
            obj._equipment_container = self
            self._equipments.append(obj)

    def remove_equipments(self, *equipments):
        for obj in equipments:
            obj._equipment_container = None
            self._equipments.remove(obj)
    # >>> equipments



class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, voltage_levels=None, region=None, bays=None, substation_asset=None, *args, **kw_args):
        """ Initialises a new 'Substation' instance.

        @param voltage_levels: The association is used in the naming hierarchy.
        @param region: The association is used in the naming hierarchy.
        @param bays: The association is used in the naming hierarchy.
        @param substation_asset:
        """

        self._voltage_levels = []
        if voltage_levels is not None:
            self.voltage_levels = voltage_levels
        else:
            self.voltage_levels = []

        self._region = None
        self.region = region

        self._bays = []
        if bays is not None:
            self.bays = bays
        else:
            self.bays = []

        self._substation_asset = None
        self.substation_asset = substation_asset


        super(Substation, self).__init__(*args, **kw_args)
    # >>> substation

    # <<< voltage_levels
    # @generated
    def get_voltage_levels(self):
        """ The association is used in the naming hierarchy.
        """
        return self._voltage_levels

    def set_voltage_levels(self, value):
        for x in self._voltage_levels:
            x._substation = None
        for y in value:
            y._substation = self
        self._voltage_levels = value

    voltage_levels = property(get_voltage_levels, set_voltage_levels)

    def add_voltage_levels(self, *voltage_levels):
        for obj in voltage_levels:
            obj._substation = self
            self._voltage_levels.append(obj)

    def remove_voltage_levels(self, *voltage_levels):
        for obj in voltage_levels:
            obj._substation = None
            self._voltage_levels.remove(obj)
    # >>> voltage_levels

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

    # <<< bays
    # @generated
    def get_bays(self):
        """ The association is used in the naming hierarchy.
        """
        return self._bays

    def set_bays(self, value):
        for x in self._bays:
            x._substation = None
        for y in value:
            y._substation = self
        self._bays = value

    bays = property(get_bays, set_bays)

    def add_bays(self, *bays):
        for obj in bays:
            obj._substation = self
            self._bays.append(obj)

    def remove_bays(self, *bays):
        for obj in bays:
            obj._substation = None
            self._bays.remove(obj)
    # >>> bays

    # <<< substation_asset
    # @generated
    def get_substation_asset(self):
        """ 
        """
        return self._substation_asset

    def set_substation_asset(self, value):
        if self._substation_asset is not None:
            self._substation_asset._substation = None

        self._substation_asset = value
        if self._substation_asset is not None:
            self._substation_asset._substation = self

    substation_asset = property(get_substation_asset, set_substation_asset)
    # >>> substation_asset



class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """
    # <<< basic_interval_schedule
    # @generated
    def __init__(self, value2_multiplier='m', value1_unit='m2', value2_unit='m2', value1_multiplier='m', start_time='', *args, **kw_args):
        """ Initialises a new 'BasicIntervalSchedule' instance.

        @param value2_multiplier: Multiplier for value2. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param value1_unit: Value1 units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param value2_unit: Value2 units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param value1_multiplier: Multiplier for value1. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param start_time: The time for the first time point. 
        """
        # Multiplier for value2. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.value2_multiplier = value2_multiplier

        # Value1 units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.value1_unit = value1_unit

        # Value2 units of measure. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.value2_unit = value2_unit

        # Multiplier for value1. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.value1_multiplier = value1_multiplier

        # The time for the first time point. 
        self.start_time = start_time



        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)
    # >>> basic_interval_schedule



class IrregularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them varies.
    """
    # <<< irregular_interval_schedule
    # @generated
    def __init__(self, time_points=None, *args, **kw_args):
        """ Initialises a new 'IrregularIntervalSchedule' instance.

        @param time_points: The point data values that define a curve
        """

        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []


        super(IrregularIntervalSchedule, self).__init__(*args, **kw_args)
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



class PsrList(IdentifiedObject):
    """ Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """
    # <<< psr_list
    # @generated
    def __init__(self, type_psrlist='', power_system_resources=None, *args, **kw_args):
        """ Initialises a new 'PsrList' instance.

        @param type_psrlist: Type of power system resources in this list. 
        @param power_system_resources:
        """
        # Type of power system resources in this list. 
        self.type_psrlist = type_psrlist


        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(PsrList, self).__init__(*args, **kw_args)
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



class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """
    # <<< regular_interval_schedule
    # @generated
    def __init__(self, time_step=0.0, end_time='', time_points=None, *args, **kw_args):
        """ Initialises a new 'RegularIntervalSchedule' instance.

        @param time_step: The time between each pair of subsequent RegularTimePoints. 
        @param end_time: The time for the last time point. 
        @param time_points: The point data values that define a curve
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


        super(RegularIntervalSchedule, self).__init__(*args, **kw_args)
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



class OperatingParticipant(IdentifiedObject):
    """ An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """
    # <<< operating_participant
    # @generated
    def __init__(self, operating_share=None, *args, **kw_args):
        """ Initialises a new 'OperatingParticipant' instance.

        @param operating_share: The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """

        self._operating_share = []
        if operating_share is not None:
            self.operating_share = operating_share
        else:
            self.operating_share = []


        super(OperatingParticipant, self).__init__(*args, **kw_args)
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



class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """
    # <<< bay
    # @generated
    def __init__(self, breaker_configuration='no_breaker', bus_bar_configuration='ring_bus', bay_energy_meas_flag=False, bay_power_meas_flag=False, voltage_level=None, substation=None, *args, **kw_args):
        """ Initialises a new 'Bay' instance.

        @param breaker_configuration: Breaker configuration. Values are: "no_breaker", "double_breaker", "single_breaker", "breaker_and_ahalf"
        @param bus_bar_configuration: Bus bar configuration. Values are: "ring_bus", "double_bus", "main_with_transfer", "single_bus"
        @param bay_energy_meas_flag: Indicates the presence/absence of energy measurements. 
        @param bay_power_meas_flag: Indicates the presence/absence of active/reactive power measurements. 
        @param voltage_level: The association is used in the naming hierarchy.
        @param substation: The association is used in the naming hierarchy.
        """
        # Breaker configuration. Values are: "no_breaker", "double_breaker", "single_breaker", "breaker_and_ahalf"
        self.breaker_configuration = breaker_configuration

        # Bus bar configuration. Values are: "ring_bus", "double_bus", "main_with_transfer", "single_bus"
        self.bus_bar_configuration = bus_bar_configuration

        # Indicates the presence/absence of energy measurements. 
        self.bay_energy_meas_flag = bay_energy_meas_flag

        # Indicates the presence/absence of active/reactive power measurements. 
        self.bay_power_meas_flag = bay_power_meas_flag


        self._voltage_level = None
        self.voltage_level = voltage_level

        self._substation = None
        self.substation = substation


        super(Bay, self).__init__(*args, **kw_args)
    # >>> bay

    # <<< voltage_level
    # @generated
    def get_voltage_level(self):
        """ The association is used in the naming hierarchy.
        """
        return self._voltage_level

    def set_voltage_level(self, value):
        if self._voltage_level is not None:
            filtered = [x for x in self.voltage_level.bays if x != self]
            self._voltage_level._bays = filtered

        self._voltage_level = value
        if self._voltage_level is not None:
            self._voltage_level._bays.append(self)

    voltage_level = property(get_voltage_level, set_voltage_level)
    # >>> voltage_level

    # <<< substation
    # @generated
    def get_substation(self):
        """ The association is used in the naming hierarchy.
        """
        return self._substation

    def set_substation(self, value):
        if self._substation is not None:
            filtered = [x for x in self.substation.bays if x != self]
            self._substation._bays = filtered

        self._substation = value
        if self._substation is not None:
            self._substation._bays.append(self)

    substation = property(get_substation, set_substation)
    # >>> substation



class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, low_voltage_limit=0.0, high_voltage_limit=0.0, bays=None, substation=None, base_voltage=None, *args, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.

        @param low_voltage_limit: The bus bar's low voltage limit 
        @param high_voltage_limit: The bus bar's high voltage limit 
        @param bays: The association is used in the naming hierarchy.
        @param substation: The association is used in the naming hierarchy.
        @param base_voltage: The base voltage used for all equipment within the VoltageLevel.
        """
        # The bus bar's low voltage limit 
        self.low_voltage_limit = low_voltage_limit

        # The bus bar's high voltage limit 
        self.high_voltage_limit = high_voltage_limit


        self._bays = []
        if bays is not None:
            self.bays = bays
        else:
            self.bays = []

        self._substation = None
        self.substation = substation

        self._base_voltage = None
        self.base_voltage = base_voltage


        super(VoltageLevel, self).__init__(*args, **kw_args)
    # >>> voltage_level

    # <<< bays
    # @generated
    def get_bays(self):
        """ The association is used in the naming hierarchy.
        """
        return self._bays

    def set_bays(self, value):
        for x in self._bays:
            x._voltage_level = None
        for y in value:
            y._voltage_level = self
        self._bays = value

    bays = property(get_bays, set_bays)

    def add_bays(self, *bays):
        for obj in bays:
            obj._voltage_level = self
            self._bays.append(obj)

    def remove_bays(self, *bays):
        for obj in bays:
            obj._voltage_level = None
            self._bays.remove(obj)
    # >>> bays

    # <<< substation
    # @generated
    def get_substation(self):
        """ The association is used in the naming hierarchy.
        """
        return self._substation

    def set_substation(self, value):
        if self._substation is not None:
            filtered = [x for x in self.substation.voltage_levels if x != self]
            self._substation._voltage_levels = filtered

        self._substation = value
        if self._substation is not None:
            self._substation._voltage_levels.append(self)

    substation = property(get_substation, set_substation)
    # >>> substation

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



class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """
    # <<< terminal
    # @generated
    def __init__(self, sequence_number=0, connected=False, conducting_equipment=None, bushing_asset=None, has_second_mutual_coupling=None, operational_limit_set=None, has_first_mutual_coupling=None, tie_flow=None, measurements=None, topological_node=None, regulating_control=None, sv_power_flow=None, terminal_constraints=None, branch_group_terminal=None, connectivity_node=None, *args, **kw_args):
        """ Initialises a new 'Terminal' instance.

        @param sequence_number: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        @param connected: The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
        @param conducting_equipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param bushing_asset:
        @param has_second_mutual_coupling: Mutual couplings with the branch associated as the first branch.
        @param operational_limit_set: The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        @param has_first_mutual_coupling: Mutual couplings associated with the branch as the first branch.
        @param tie_flow: The control area tie flows to which this terminal associates.
        @param measurements: One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        @param topological_node: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param regulating_control: The terminal is regulated by a control.
        @param sv_power_flow: The power flow state associated with the terminal.
        @param terminal_constraints:
        @param branch_group_terminal: The directed branch group terminals for which the terminal is monitored.
        @param connectivity_node: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        self.sequence_number = sequence_number

        # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
        self.connected = connected


        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._bushing_asset = None
        self.bushing_asset = bushing_asset

        self._has_second_mutual_coupling = []
        if has_second_mutual_coupling is not None:
            self.has_second_mutual_coupling = has_second_mutual_coupling
        else:
            self.has_second_mutual_coupling = []

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []

        self._has_first_mutual_coupling = []
        if has_first_mutual_coupling is not None:
            self.has_first_mutual_coupling = has_first_mutual_coupling
        else:
            self.has_first_mutual_coupling = []

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._topological_node = None
        self.topological_node = topological_node

        self._regulating_control = []
        if regulating_control is not None:
            self.regulating_control = regulating_control
        else:
            self.regulating_control = []

        self._sv_power_flow = None
        self.sv_power_flow = sv_power_flow

        self._terminal_constraints = []
        if terminal_constraints is not None:
            self.terminal_constraints = terminal_constraints
        else:
            self.terminal_constraints = []

        self._branch_group_terminal = []
        if branch_group_terminal is not None:
            self.branch_group_terminal = branch_group_terminal
        else:
            self.branch_group_terminal = []

        self._connectivity_node = None
        self.connectivity_node = connectivity_node


        super(Terminal, self).__init__(*args, **kw_args)
    # >>> terminal

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

    # <<< bushing_asset
    # @generated
    def get_bushing_asset(self):
        """ 
        """
        return self._bushing_asset

    def set_bushing_asset(self, value):
        if self._bushing_asset is not None:
            self._bushing_asset._terminal = None

        self._bushing_asset = value
        if self._bushing_asset is not None:
            self._bushing_asset._terminal = self

    bushing_asset = property(get_bushing_asset, set_bushing_asset)
    # >>> bushing_asset

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

    # <<< terminal_constraints
    # @generated
    def get_terminal_constraints(self):
        """ 
        """
        return self._terminal_constraints

    def set_terminal_constraints(self, value):
        for x in self._terminal_constraints:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._terminal_constraints = value

    terminal_constraints = property(get_terminal_constraints, set_terminal_constraints)

    def add_terminal_constraints(self, *terminal_constraints):
        for obj in terminal_constraints:
            obj._terminal = self
            self._terminal_constraints.append(obj)

    def remove_terminal_constraints(self, *terminal_constraints):
        for obj in terminal_constraints:
            obj._terminal = None
            self._terminal_constraints.remove(obj)
    # >>> terminal_constraints

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



class ReportingGroup(IdentifiedObject):
    """ A reporting group is used for various ad-hoc groupings used for reporting.
    """
    # <<< reporting_group
    # @generated
    def __init__(self, topological_node=None, bus_name_marker=None, power_system_resource=None, reporting_super_group=None, *args, **kw_args):
        """ Initialises a new 'ReportingGroup' instance.

        @param topological_node: The topological nodes that belong to the reporting group.
        @param bus_name_marker: The BusNameMarkers that belong to this reporting group.
        @param power_system_resource: PSR's which belong to this reporting group.
        @param reporting_super_group: Reporting super group to which this reporting group belongs.
        """

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []

        self._bus_name_marker = []
        if bus_name_marker is not None:
            self.bus_name_marker = bus_name_marker
        else:
            self.bus_name_marker = []

        self._power_system_resource = []
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        else:
            self.power_system_resource = []

        self._reporting_super_group = None
        self.reporting_super_group = reporting_super_group


        super(ReportingGroup, self).__init__(*args, **kw_args)
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



class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """
    # <<< psrtype
    # @generated
    def __init__(self, power_system_resources=None, *args, **kw_args):
        """ Initialises a new 'PSRType' instance.

        @param power_system_resources: Power system resources classified with this PSRType.
        """

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(PSRType, self).__init__(*args, **kw_args)
    # >>> psrtype

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ Power system resources classified with this PSRType.
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for x in self._power_system_resources:
            x._psrtype = None
        for y in value:
            y._psrtype = self
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._psrtype = self
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._psrtype = None
            self._power_system_resources.remove(obj)
    # >>> power_system_resources



class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region
    # @generated
    def __init__(self, region=None, substations=None, lines=None, *args, **kw_args):
        """ Initialises a new 'SubGeographicalRegion' instance.

        @param region: The association is used in the naming hierarchy.
        @param substations: The association is used in the naming hierarchy.
        @param lines: A Line can be contained by a SubGeographical Region.
        """

        self._region = None
        self.region = region

        self._substations = []
        if substations is not None:
            self.substations = substations
        else:
            self.substations = []

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []


        super(SubGeographicalRegion, self).__init__(*args, **kw_args)
    # >>> sub_geographical_region

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



class BaseVoltage(IdentifiedObject):
    """ Defines a nominal base voltage which is referenced in the system.
    """
    # <<< base_voltage
    # @generated
    def __init__(self, is_dc=False, nominal_voltage=0.0, voltage_level=None, conducting_equipment=None, topological_node=None, *args, **kw_args):
        """ Initialises a new 'BaseVoltage' instance.

        @param is_dc: If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
        @param nominal_voltage: The PowerSystemResource's base voltage. 
        @param voltage_level: The VoltageLevels having this BaseVoltage.
        @param conducting_equipment: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param topological_node: The topological nodes at the base voltage.
        """
        # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
        self.is_dc = is_dc

        # The PowerSystemResource's base voltage. 
        self.nominal_voltage = nominal_voltage


        self._voltage_level = []
        if voltage_level is not None:
            self.voltage_level = voltage_level
        else:
            self.voltage_level = []

        self._conducting_equipment = []
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
        else:
            self.conducting_equipment = []

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []


        super(BaseVoltage, self).__init__(*args, **kw_args)
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



class BasePower(IdentifiedObject):
    """ The BasePower class defines the base power used in the per unit calculations.
    """
    # <<< base_power
    # @generated
    def __init__(self, base_power=0.0, *args, **kw_args):
        """ Initialises a new 'BasePower' instance.

        @param base_power: Definition of base power. 
        """
        # Definition of base power. 
        self.base_power = base_power



        super(BasePower, self).__init__(*args, **kw_args)
    # >>> base_power



# <<< core
# @generated
# >>> core
