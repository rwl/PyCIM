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


from cim.iec61968.informative.inf_common import Role
from cim.iec61968.common import Agreement
from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Location

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.inflocations"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfLocations"

class LocLocRole(Role):
    """ The relationship between one Location and another Location. One 'roleType' is 'Directions,' for which an additional attribute serves for providing a textual description for navigating from one location to another location.
    """
    # <<< loc_loc_role
    # @generated
    def __init__(self, direction_info='', to_location=None, from_location=None, **kw_args):
        """ Initialises a new 'LocLocRole' instance.
        """
        # Detailed directional information. 
        self.direction_info = direction_info


        self._to_location = None
        self.to_location = to_location

        self._from_location = None
        self.from_location = from_location


        super(LocLocRole, self).__init__(**kw_args)
    # >>> loc_loc_role

    # <<< to_location
    # @generated
    def get_to_location(self):
        """ 
        """
        return self._to_location

    def set_to_location(self, value):
        if self._to_location is not None:
            filtered = [x for x in self.to_location.from_location_roles if x != self]
            self._to_location._from_location_roles = filtered

        self._to_location = value
        if self._to_location is not None:
            self._to_location._from_location_roles.append(self)

    to_location = property(get_to_location, set_to_location)
    # >>> to_location

    # <<< from_location
    # @generated
    def get_from_location(self):
        """ 
        """
        return self._from_location

    def set_from_location(self, value):
        if self._from_location is not None:
            filtered = [x for x in self.from_location.to_location_roles if x != self]
            self._from_location._to_location_roles = filtered

        self._from_location = value
        if self._from_location is not None:
            self._from_location._to_location_roles.append(self)

    from_location = property(get_from_location, set_from_location)
    # >>> from_location


    def __str__(self):
        """ Returns a string representation of the LocLocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< loc_loc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LocLocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LocLocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.to_location is not None:
            s += '%s<%s:LocLocRole.to_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.to_location.uri)
        if self.from_location is not None:
            s += '%s<%s:LocLocRole.from_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_location.uri)
        s += '%s<%s:LocLocRole.direction_info>%s</%s:LocLocRole.direction_info>' % \
            (indent, ns_prefix, self.direction_info, ns_prefix)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LocLocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> loc_loc_role.serialize


class RightOfWay(Agreement):
    """ A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """
    # <<< right_of_way
    # @generated
    def __init__(self, property_data='', land_properties=None, **kw_args):
        """ Initialises a new 'RightOfWay' instance.
        """
        # Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        self.property_data = property_data


        self._land_properties = []
        if land_properties is not None:
            self.land_properties = land_properties
        else:
            self.land_properties = []


        super(RightOfWay, self).__init__(**kw_args)
    # >>> right_of_way

    # <<< land_properties
    # @generated
    def get_land_properties(self):
        """ All land properties this right of way applies to.
        """
        return self._land_properties

    def set_land_properties(self, value):
        for p in self._land_properties:
            filtered = [q for q in p.right_of_ways if q != self]
            self._land_properties._right_of_ways = filtered
        for r in value:
            if self not in r._right_of_ways:
                r._right_of_ways.append(self)
        self._land_properties = value

    land_properties = property(get_land_properties, set_land_properties)

    def add_land_properties(self, *land_properties):
        for obj in land_properties:
            if self not in obj._right_of_ways:
                obj._right_of_ways.append(self)
            self._land_properties.append(obj)

    def remove_land_properties(self, *land_properties):
        for obj in land_properties:
            if self in obj._right_of_ways:
                obj._right_of_ways.remove(self)
            self._land_properties.remove(obj)
    # >>> land_properties


    def __str__(self):
        """ Returns a string representation of the RightOfWay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< right_of_way.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RightOfWay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RightOfWay", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.land_properties:
            s += '%s<%s:RightOfWay.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RightOfWay.property_data>%s</%s:RightOfWay.property_data>' % \
            (indent, ns_prefix, self.property_data, ns_prefix)
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
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.validity_interval is not None:
            s += '%s<%s:Agreement.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        s += '%s<%s:Agreement.sign_date>%s</%s:Agreement.sign_date>' % \
            (indent, ns_prefix, self.sign_date, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RightOfWay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> right_of_way.serialize


class OrgLocRole(Role):
    """ Roles played between Organisations and Locations, for example a service territory or school district. Note that roles dealing with use of a specific piece of property should be defined based on the relationship between OccupationsOfProperty and Location.
    """
    # <<< org_loc_role
    # @generated
    def __init__(self, erp_organisation=None, location=None, **kw_args):
        """ Initialises a new 'OrgLocRole' instance.
        """

        self._erp_organisation = None
        self.erp_organisation = erp_organisation

        self._location = None
        self.location = location


        super(OrgLocRole, self).__init__(**kw_args)
    # >>> org_loc_role

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.location_roles if x != self]
            self._erp_organisation._location_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._location_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.erp_organisation_roles if x != self]
            self._location._erp_organisation_roles = filtered

        self._location = value
        if self._location is not None:
            self._location._erp_organisation_roles.append(self)

    location = property(get_location, set_location)
    # >>> location


    def __str__(self):
        """ Returns a string representation of the OrgLocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_loc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgLocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgLocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_organisation is not None:
            s += '%s<%s:OrgLocRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
        if self.location is not None:
            s += '%s<%s:OrgLocRole.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgLocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_loc_role.serialize


class OrgPropertyRole(Role):
    """ Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """
    # <<< org_property_role
    # @generated
    def __init__(self, erp_organisation=None, land_property=None, **kw_args):
        """ Initialises a new 'OrgPropertyRole' instance.
        """

        self._erp_organisation = None
        self.erp_organisation = erp_organisation

        self._land_property = []
        if land_property is not None:
            self.land_property = land_property
        else:
            self.land_property = []


        super(OrgPropertyRole, self).__init__(**kw_args)
    # >>> org_property_role

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.land_property_roles if x != self]
            self._erp_organisation._land_property_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._land_property_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ 
        """
        return self._land_property

    def set_land_property(self, value):
        for p in self._land_property:
            filtered = [q for q in p.erp_organisation_roles if q != self]
            self._land_property._erp_organisation_roles = filtered
        for r in value:
            if self not in r._erp_organisation_roles:
                r._erp_organisation_roles.append(self)
        self._land_property = value

    land_property = property(get_land_property, set_land_property)

    def add_land_property(self, *land_property):
        for obj in land_property:
            if self not in obj._erp_organisation_roles:
                obj._erp_organisation_roles.append(self)
            self._land_property.append(obj)

    def remove_land_property(self, *land_property):
        for obj in land_property:
            if self in obj._erp_organisation_roles:
                obj._erp_organisation_roles.remove(self)
            self._land_property.remove(obj)
    # >>> land_property


    def __str__(self):
        """ Returns a string representation of the OrgPropertyRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_property_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgPropertyRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgPropertyRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_organisation is not None:
            s += '%s<%s:OrgPropertyRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
        for obj in self.land_property:
            s += '%s<%s:OrgPropertyRole.land_property rdf:resource="#%s"/>' % \
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgPropertyRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_property_role.serialize


class AssetLocRole(Role):
    """ Roles played between Assets and Locations.
    """
    # <<< asset_loc_role
    # @generated
    def __init__(self, asset=None, location=None, **kw_args):
        """ Initialises a new 'AssetLocRole' instance.
        """

        self._asset = None
        self.asset = asset

        self._location = None
        self.location = location


        super(AssetLocRole, self).__init__(**kw_args)
    # >>> asset_loc_role

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.location_roles if x != self]
            self._asset._location_roles = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._location_roles.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.asset_roles if x != self]
            self._location._asset_roles = filtered

        self._location = value
        if self._location is not None:
            self._location._asset_roles.append(self)

    location = property(get_location, set_location)
    # >>> location


    def __str__(self):
        """ Returns a string representation of the AssetLocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_loc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetLocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetLocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:AssetLocRole.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.location is not None:
            s += '%s<%s:AssetLocRole.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetLocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_loc_role.serialize


class ErpPersonLocRole(Role):
    """ Roles played between People and Locations. Some Locations are somewhat static, like the person's home address. Other may be dynamic, for example when the person is part of a crew driving around in truck.
    """
    # <<< erp_person_loc_role
    # @generated
    def __init__(self, location=None, erp_person=None, **kw_args):
        """ Initialises a new 'ErpPersonLocRole' instance.
        """

        self._location = None
        self.location = location

        self._erp_person = None
        self.erp_person = erp_person


        super(ErpPersonLocRole, self).__init__(**kw_args)
    # >>> erp_person_loc_role

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.erp_person_roles if x != self]
            self._location._erp_person_roles = filtered

        self._location = value
        if self._location is not None:
            self._location._erp_person_roles.append(self)

    location = property(get_location, set_location)
    # >>> location

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.location_roles if x != self]
            self._erp_person._location_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._location_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person


    def __str__(self):
        """ Returns a string representation of the ErpPersonLocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_person_loc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPersonLocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPersonLocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.location is not None:
            s += '%s<%s:ErpPersonLocRole.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        if self.erp_person is not None:
            s += '%s<%s:ErpPersonLocRole.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPersonLocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_person_loc_role.serialize


class Route(IdentifiedObject):
    """ Route that is followed, for example by service crews.
    """
    # <<< route
    # @generated
    def __init__(self, category='', locations=None, crews=None, status=None, **kw_args):
        """ Initialises a new 'Route' instance.
        """
        # Category by utility's work management standards and practices. 
        self.category = category


        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.status = status


        super(Route, self).__init__(**kw_args)
    # >>> route

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.routes if q != self]
            self._locations._routes = filtered
        for r in value:
            if self not in r._routes:
                r._routes.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._routes:
                obj._routes.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._routes:
                obj._routes.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for x in self._crews:
            x._route = None
        for y in value:
            y._route = self
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            obj._route = self
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            obj._route = None
            self._crews.remove(obj)
    # >>> crews

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Route.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< route.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Route.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Route", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.locations:
            s += '%s<%s:Route.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Route.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Route.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Route.category>%s</%s:Route.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Route")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> route.serialize


class Zone(Location):
    """ Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.
    """
    # <<< zone
    # @generated
    def __init__(self, kind='special_restriction_land', **kw_args):
        """ Initialises a new 'Zone' instance.
        """
        # Kind of this zone. Values are: "special_restriction_land", "electrical_network", "weather_zone", "other"
        self.kind = 'special_restriction_land'



        super(Zone, self).__init__(**kw_args)
    # >>> zone


    def __str__(self):
        """ Returns a string representation of the Zone.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< zone.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Zone.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Zone", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Zone.kind>%s</%s:Zone.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
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
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Zone")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> zone.serialize


class DocLocRole(Role):
    """ Roles played between Documents and Locations. For example, as ErpAddress is a type of Location and WorkBilling is a type of Document, a role is the address for which to mail the invoice. As a TroubleTicket is a type of Document, one instance of Location may be the address for which the trouble is reported.
    """
    # <<< doc_loc_role
    # @generated
    def __init__(self, location=None, document=None, **kw_args):
        """ Initialises a new 'DocLocRole' instance.
        """

        self._location = None
        self.location = location

        self._document = None
        self.document = document


        super(DocLocRole, self).__init__(**kw_args)
    # >>> doc_loc_role

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.document_roles if x != self]
            self._location._document_roles = filtered

        self._location = value
        if self._location is not None:
            self._location._document_roles.append(self)

    location = property(get_location, set_location)
    # >>> location

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.location_roles if x != self]
            self._document._location_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._location_roles.append(self)

    document = property(get_document, set_document)
    # >>> document


    def __str__(self):
        """ Returns a string representation of the DocLocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_loc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocLocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocLocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.location is not None:
            s += '%s<%s:DocLocRole.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        if self.document is not None:
            s += '%s<%s:DocLocRole.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocLocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_loc_role.serialize


class SchematicLocation(Location):
    """ Schematic location. Intended to be used in the context of diagrams (worked out by WG13 in 2008 and 2009).
    """
    pass
    # <<< schematic_location
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'SchematicLocation' instance.
        """


        super(SchematicLocation, self).__init__(**kw_args)
    # >>> schematic_location


    def __str__(self):
        """ Returns a string representation of the SchematicLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< schematic_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SchematicLocation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SchematicLocation", self.uri)
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
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SchematicLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> schematic_location.serialize


class RedLine(IdentifiedObject):
    """ This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.
    """
    # <<< red_line
    # @generated
    def __init__(self, status=None, locations=None, **kw_args):
        """ Initialises a new 'RedLine' instance.
        """

        self.status = status

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []


        super(RedLine, self).__init__(**kw_args)
    # >>> red_line

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.red_lines if q != self]
            self._locations._red_lines = filtered
        for r in value:
            if self not in r._red_lines:
                r._red_lines.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._red_lines:
                obj._red_lines.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._red_lines:
                obj._red_lines.remove(self)
            self._locations.remove(obj)
    # >>> locations


    def __str__(self):
        """ Returns a string representation of the RedLine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< red_line.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RedLine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RedLine", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:RedLine.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.locations:
            s += '%s<%s:RedLine.locations rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RedLine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> red_line.serialize


class LocationGrant(Agreement):
    """ A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """
    # <<< location_grant
    # @generated
    def __init__(self, property_data='', land_property=None, **kw_args):
        """ Initialises a new 'LocationGrant' instance.
        """
        # Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        self.property_data = property_data


        self._land_property = None
        self.land_property = land_property


        super(LocationGrant, self).__init__(**kw_args)
    # >>> location_grant

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ Land property this location grant applies to.
        """
        return self._land_property

    def set_land_property(self, value):
        if self._land_property is not None:
            filtered = [x for x in self.land_property.location_grants if x != self]
            self._land_property._location_grants = filtered

        self._land_property = value
        if self._land_property is not None:
            self._land_property._location_grants.append(self)

    land_property = property(get_land_property, set_land_property)
    # >>> land_property


    def __str__(self):
        """ Returns a string representation of the LocationGrant.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< location_grant.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LocationGrant.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LocationGrant", self.uri)
        if format:
            indent += ' ' * depth

        if self.land_property is not None:
            s += '%s<%s:LocationGrant.land_property rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.land_property.uri)
        s += '%s<%s:LocationGrant.property_data>%s</%s:LocationGrant.property_data>' % \
            (indent, ns_prefix, self.property_data, ns_prefix)
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
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.validity_interval is not None:
            s += '%s<%s:Agreement.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        s += '%s<%s:Agreement.sign_date>%s</%s:Agreement.sign_date>' % \
            (indent, ns_prefix, self.sign_date, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LocationGrant")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> location_grant.serialize


class LandProperty(IdentifiedObject):
    """ Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """
    # <<< land_property
    # @generated
    def __init__(self, kind='store', demographic_kind='other', external_record_reference='', location_grants=None, asset_containers=None, erp_site_level_datas=None, erp_person_roles=None, locations=None, right_of_ways=None, erp_organisation_roles=None, status=None, **kw_args):
        """ Initialises a new 'LandProperty' instance.
        """
        # Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "depot", "customer_premise", "external", "grid_supply_point", "substation", "building"
        self.kind = 'store'

        # Demographics around the site. Values are: "other", "urban", "rural"
        self.demographic_kind = 'other'

        # Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation. 
        self.external_record_reference = external_record_reference


        self._location_grants = []
        if location_grants is not None:
            self.location_grants = location_grants
        else:
            self.location_grants = []

        self._asset_containers = []
        if asset_containers is not None:
            self.asset_containers = asset_containers
        else:
            self.asset_containers = []

        self._erp_site_level_datas = []
        if erp_site_level_datas is not None:
            self.erp_site_level_datas = erp_site_level_datas
        else:
            self.erp_site_level_datas = []

        self._erp_person_roles = []
        if erp_person_roles is not None:
            self.erp_person_roles = erp_person_roles
        else:
            self.erp_person_roles = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._right_of_ways = []
        if right_of_ways is not None:
            self.right_of_ways = right_of_ways
        else:
            self.right_of_ways = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self.status = status


        super(LandProperty, self).__init__(**kw_args)
    # >>> land_property

    # <<< location_grants
    # @generated
    def get_location_grants(self):
        """ All location grants this land property has.
        """
        return self._location_grants

    def set_location_grants(self, value):
        for x in self._location_grants:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._location_grants = value

    location_grants = property(get_location_grants, set_location_grants)

    def add_location_grants(self, *location_grants):
        for obj in location_grants:
            obj._land_property = self
            self._location_grants.append(obj)

    def remove_location_grants(self, *location_grants):
        for obj in location_grants:
            obj._land_property = None
            self._location_grants.remove(obj)
    # >>> location_grants

    # <<< asset_containers
    # @generated
    def get_asset_containers(self):
        """ 
        """
        return self._asset_containers

    def set_asset_containers(self, value):
        for p in self._asset_containers:
            filtered = [q for q in p.land_properties if q != self]
            self._asset_containers._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._asset_containers = value

    asset_containers = property(get_asset_containers, set_asset_containers)

    def add_asset_containers(self, *asset_containers):
        for obj in asset_containers:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._asset_containers.append(obj)

    def remove_asset_containers(self, *asset_containers):
        for obj in asset_containers:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._asset_containers.remove(obj)
    # >>> asset_containers

    # <<< erp_site_level_datas
    # @generated
    def get_erp_site_level_datas(self):
        """ 
        """
        return self._erp_site_level_datas

    def set_erp_site_level_datas(self, value):
        for x in self._erp_site_level_datas:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._erp_site_level_datas = value

    erp_site_level_datas = property(get_erp_site_level_datas, set_erp_site_level_datas)

    def add_erp_site_level_datas(self, *erp_site_level_datas):
        for obj in erp_site_level_datas:
            obj._land_property = self
            self._erp_site_level_datas.append(obj)

    def remove_erp_site_level_datas(self, *erp_site_level_datas):
        for obj in erp_site_level_datas:
            obj._land_property = None
            self._erp_site_level_datas.remove(obj)
    # >>> erp_site_level_datas

    # <<< erp_person_roles
    # @generated
    def get_erp_person_roles(self):
        """ 
        """
        return self._erp_person_roles

    def set_erp_person_roles(self, value):
        for x in self._erp_person_roles:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._erp_person_roles = value

    erp_person_roles = property(get_erp_person_roles, set_erp_person_roles)

    def add_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._land_property = self
            self._erp_person_roles.append(obj)

    def remove_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._land_property = None
            self._erp_person_roles.remove(obj)
    # >>> erp_person_roles

    # <<< locations
    # @generated
    def get_locations(self):
        """ The spatail description of a piece of property.
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.land_properties if q != self]
            self._locations._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< right_of_ways
    # @generated
    def get_right_of_ways(self):
        """ All rights of way this land property has.
        """
        return self._right_of_ways

    def set_right_of_ways(self, value):
        for p in self._right_of_ways:
            filtered = [q for q in p.land_properties if q != self]
            self._right_of_ways._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._right_of_ways = value

    right_of_ways = property(get_right_of_ways, set_right_of_ways)

    def add_right_of_ways(self, *right_of_ways):
        for obj in right_of_ways:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._right_of_ways.append(obj)

    def remove_right_of_ways(self, *right_of_ways):
        for obj in right_of_ways:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._right_of_ways.remove(obj)
    # >>> right_of_ways

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for p in self._erp_organisation_roles:
            filtered = [q for q in p.land_property if q != self]
            self._erp_organisation_roles._land_property = filtered
        for r in value:
            if self not in r._land_property:
                r._land_property.append(self)
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            if self not in obj._land_property:
                obj._land_property.append(self)
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            if self in obj._land_property:
                obj._land_property.remove(self)
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the LandProperty.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< land_property.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LandProperty.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LandProperty", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.location_grants:
            s += '%s<%s:LandProperty.location_grants rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_containers:
            s += '%s<%s:LandProperty.asset_containers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_site_level_datas:
            s += '%s<%s:LandProperty.erp_site_level_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:LandProperty.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:LandProperty.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.right_of_ways:
            s += '%s<%s:LandProperty.right_of_ways rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:LandProperty.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:LandProperty.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:LandProperty.kind>%s</%s:LandProperty.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:LandProperty.demographic_kind>%s</%s:LandProperty.demographic_kind>' % \
            (indent, ns_prefix, self.demographic_kind, ns_prefix)
        s += '%s<%s:LandProperty.external_record_reference>%s</%s:LandProperty.external_record_reference>' % \
            (indent, ns_prefix, self.external_record_reference, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "LandProperty")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> land_property.serialize


class Hazard(IdentifiedObject):
    """ A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """
    # <<< hazard
    # @generated
    def __init__(self, category='', assets=None, locations=None, status=None, **kw_args):
        """ Initialises a new 'Hazard' instance.
        """
        # Category by utility's corporate standards and practices. 
        self.category = category


        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self.status = status


        super(Hazard, self).__init__(**kw_args)
    # >>> hazard

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.hazards if q != self]
            self._assets._hazards = filtered
        for r in value:
            if self not in r._hazards:
                r._hazards.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._hazards:
                obj._hazards.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._hazards:
                obj._hazards.remove(self)
            self._assets.remove(obj)
    # >>> assets

    # <<< locations
    # @generated
    def get_locations(self):
        """ The point or polygon location of a given hazard.
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.hazards if q != self]
            self._locations._hazards = filtered
        for r in value:
            if self not in r._hazards:
                r._hazards.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._hazards:
                obj._hazards.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._hazards:
                obj._hazards.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Hazard.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< hazard.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Hazard.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Hazard", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.assets:
            s += '%s<%s:Hazard.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Hazard.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Hazard.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Hazard.category>%s</%s:Hazard.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Hazard")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> hazard.serialize


class PersonPropertyRole(Role):
    """ The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.
    """
    # <<< person_property_role
    # @generated
    def __init__(self, land_property=None, erp_person=None, **kw_args):
        """ Initialises a new 'PersonPropertyRole' instance.
        """

        self._land_property = None
        self.land_property = land_property

        self._erp_person = None
        self.erp_person = erp_person


        super(PersonPropertyRole, self).__init__(**kw_args)
    # >>> person_property_role

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ 
        """
        return self._land_property

    def set_land_property(self, value):
        if self._land_property is not None:
            filtered = [x for x in self.land_property.erp_person_roles if x != self]
            self._land_property._erp_person_roles = filtered

        self._land_property = value
        if self._land_property is not None:
            self._land_property._erp_person_roles.append(self)

    land_property = property(get_land_property, set_land_property)
    # >>> land_property

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.land_property_roles if x != self]
            self._erp_person._land_property_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._land_property_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person


    def __str__(self):
        """ Returns a string representation of the PersonPropertyRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< person_property_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PersonPropertyRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PersonPropertyRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.land_property is not None:
            s += '%s<%s:PersonPropertyRole.land_property rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.land_property.uri)
        if self.erp_person is not None:
            s += '%s<%s:PersonPropertyRole.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PersonPropertyRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> person_property_role.serialize


# <<< inf_locations
# @generated
# >>> inf_locations
