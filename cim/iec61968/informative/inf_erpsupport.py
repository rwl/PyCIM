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

""" The package contains portions of the model defined byEnterprise Resource Planning (ERP) standards like those proposed by the Open Applications Group (OAG). It is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (as defined by OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeld 'Erp...' should be associated with the appropriate classes of that standard. In fact, definitions of 'Erp...' classes are based on OAG Nouns to facilitate this process.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Enterprise Resource Planning (ERP) Support Package contains portions of the model defined by ERP standards like those proposed by the Open Applications Group (OAG). This package is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeled 'Erp...' should be associated with the appropriate classes of that standard.'
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Organisation
from cim.iec61968.informative.inf_common import Role
from cim.iec61968.common import Document
from cim.iec61968.informative.inf_common import BankAccount
from cim.iec61968.common import TelephoneNumber

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.inferpsupport"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfERPSupport"

class ErpIssueInventory(IdentifiedObject):
    """ Can be used to request an application to process an issue or request information about an issue.
    """
    # <<< erp_issue_inventory
    # @generated
    def __init__(self, status=None, type_material=None, type_asset=None, **kw_args):
        """ Initialises a new 'ErpIssueInventory' instance.
        """

        self.status = status

        self._type_material = None
        self.type_material = type_material

        self._type_asset = None
        self.type_asset = type_asset


        super(ErpIssueInventory, self).__init__(**kw_args)
    # >>> erp_issue_inventory

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.erp_issue_inventories if x != self]
            self._type_material._erp_issue_inventories = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._erp_issue_inventories.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            filtered = [x for x in self.type_asset.erp_inventory_issues if x != self]
            self._type_asset._erp_inventory_issues = filtered

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._erp_inventory_issues.append(self)

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset


    def __str__(self):
        """ Returns a string representation of the ErpIssueInventory.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_issue_inventory.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpIssueInventory.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpIssueInventory", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:ErpIssueInventory.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.type_material is not None:
            s += '%s<%s:ErpIssueInventory.type_material rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_material.uri)
        if self.type_asset is not None:
            s += '%s<%s:ErpIssueInventory.type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_asset.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpIssueInventory")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_issue_inventory.serialize


class ErpOrganisation(Organisation):
    """ Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.
    """
    # <<< erp_organisation
    # @generated
    def __init__(self, code='', category='', mode='', opt_out=False, industry_id='', is_profit_center=False, is_cost_center=False, government_id='', document_roles=None, activity_records=None, location_roles=None, erp_person_roles=None, violation_limits=None, requests=None, change_items=None, int_sched_agreement=None, registered_resources=None, power_system_resource_roles=None, asset_roles=None, land_property_roles=None, parent_organisation_roles=None, child_organisation_roles=None, crews=None, **kw_args):
        """ Initialises a new 'ErpOrganisation' instance.
        """
        # Designated code for organisation. 
        self.code = code

        # Category by utility's corporate standards and practices. 
        self.category = category

        # Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition). 
        self.mode = mode

        # True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation. 
        self.opt_out = opt_out

        # Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location. 
        self.industry_id = industry_id

        # True if organisation is profit center. 
        self.is_profit_center = is_profit_center

        # True if organisation is cost center. 
        self.is_cost_center = is_cost_center

        # Unique identifier for organisation relative to its governing authority, for example a federal tax identifier. 
        self.government_id = government_id


        self._document_roles = []
        if document_roles is not None:
            self.document_roles = document_roles
        else:
            self.document_roles = []

        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []

        self._location_roles = []
        if location_roles is not None:
            self.location_roles = location_roles
        else:
            self.location_roles = []

        self._erp_person_roles = []
        if erp_person_roles is not None:
            self.erp_person_roles = erp_person_roles
        else:
            self.erp_person_roles = []

        self._violation_limits = []
        if violation_limits is not None:
            self.violation_limits = violation_limits
        else:
            self.violation_limits = []

        self._requests = []
        if requests is not None:
            self.requests = requests
        else:
            self.requests = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._int_sched_agreement = []
        if int_sched_agreement is not None:
            self.int_sched_agreement = int_sched_agreement
        else:
            self.int_sched_agreement = []

        self._registered_resources = []
        if registered_resources is not None:
            self.registered_resources = registered_resources
        else:
            self.registered_resources = []

        self._power_system_resource_roles = []
        if power_system_resource_roles is not None:
            self.power_system_resource_roles = power_system_resource_roles
        else:
            self.power_system_resource_roles = []

        self._asset_roles = []
        if asset_roles is not None:
            self.asset_roles = asset_roles
        else:
            self.asset_roles = []

        self._land_property_roles = []
        if land_property_roles is not None:
            self.land_property_roles = land_property_roles
        else:
            self.land_property_roles = []

        self._parent_organisation_roles = []
        if parent_organisation_roles is not None:
            self.parent_organisation_roles = parent_organisation_roles
        else:
            self.parent_organisation_roles = []

        self._child_organisation_roles = []
        if child_organisation_roles is not None:
            self.child_organisation_roles = child_organisation_roles
        else:
            self.child_organisation_roles = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []


        super(ErpOrganisation, self).__init__(**kw_args)
    # >>> erp_organisation

    # <<< document_roles
    # @generated
    def get_document_roles(self):
        """ 
        """
        return self._document_roles

    def set_document_roles(self, value):
        for x in self._document_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._document_roles = value

    document_roles = property(get_document_roles, set_document_roles)

    def add_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._erp_organisation = self
            self._document_roles.append(obj)

    def remove_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._erp_organisation = None
            self._document_roles.remove(obj)
    # >>> document_roles

    # <<< activity_records
    # @generated
    def get_activity_records(self):
        """ 
        """
        return self._activity_records

    def set_activity_records(self, value):
        for p in self._activity_records:
            filtered = [q for q in p.organisations if q != self]
            self._activity_records._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._activity_records = value

    activity_records = property(get_activity_records, set_activity_records)

    def add_activity_records(self, *activity_records):
        for obj in activity_records:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._activity_records.append(obj)

    def remove_activity_records(self, *activity_records):
        for obj in activity_records:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._activity_records.remove(obj)
    # >>> activity_records

    # <<< location_roles
    # @generated
    def get_location_roles(self):
        """ 
        """
        return self._location_roles

    def set_location_roles(self, value):
        for x in self._location_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._location_roles = value

    location_roles = property(get_location_roles, set_location_roles)

    def add_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._erp_organisation = self
            self._location_roles.append(obj)

    def remove_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._erp_organisation = None
            self._location_roles.remove(obj)
    # >>> location_roles

    # <<< erp_person_roles
    # @generated
    def get_erp_person_roles(self):
        """ 
        """
        return self._erp_person_roles

    def set_erp_person_roles(self, value):
        for x in self._erp_person_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._erp_person_roles = value

    erp_person_roles = property(get_erp_person_roles, set_erp_person_roles)

    def add_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._erp_organisation = self
            self._erp_person_roles.append(obj)

    def remove_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._erp_organisation = None
            self._erp_person_roles.remove(obj)
    # >>> erp_person_roles

    # <<< violation_limits
    # @generated
    def get_violation_limits(self):
        """ 
        """
        return self._violation_limits

    def set_violation_limits(self, value):
        for p in self._violation_limits:
            filtered = [q for q in p.organisations if q != self]
            self._violation_limits._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._violation_limits = value

    violation_limits = property(get_violation_limits, set_violation_limits)

    def add_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._violation_limits.append(obj)

    def remove_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._violation_limits.remove(obj)
    # >>> violation_limits

    # <<< requests
    # @generated
    def get_requests(self):
        """ 
        """
        return self._requests

    def set_requests(self, value):
        for x in self._requests:
            x._organisation = None
        for y in value:
            y._organisation = self
        self._requests = value

    requests = property(get_requests, set_requests)

    def add_requests(self, *requests):
        for obj in requests:
            obj._organisation = self
            self._requests.append(obj)

    def remove_requests(self, *requests):
        for obj in requests:
            obj._organisation = None
            self._requests.remove(obj)
    # >>> requests

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._organisation = None
        for y in value:
            y._organisation = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._organisation = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._organisation = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< int_sched_agreement
    # @generated
    def get_int_sched_agreement(self):
        """ 
        """
        return self._int_sched_agreement

    def set_int_sched_agreement(self, value):
        for p in self._int_sched_agreement:
            filtered = [q for q in p.organisations if q != self]
            self._int_sched_agreement._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._int_sched_agreement = value

    int_sched_agreement = property(get_int_sched_agreement, set_int_sched_agreement)

    def add_int_sched_agreement(self, *int_sched_agreement):
        for obj in int_sched_agreement:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._int_sched_agreement.append(obj)

    def remove_int_sched_agreement(self, *int_sched_agreement):
        for obj in int_sched_agreement:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._int_sched_agreement.remove(obj)
    # >>> int_sched_agreement

    # <<< registered_resources
    # @generated
    def get_registered_resources(self):
        """ 
        """
        return self._registered_resources

    def set_registered_resources(self, value):
        for x in self._registered_resources:
            x._organisation = None
        for y in value:
            y._organisation = self
        self._registered_resources = value

    registered_resources = property(get_registered_resources, set_registered_resources)

    def add_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            obj._organisation = self
            self._registered_resources.append(obj)

    def remove_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            obj._organisation = None
            self._registered_resources.remove(obj)
    # >>> registered_resources

    # <<< power_system_resource_roles
    # @generated
    def get_power_system_resource_roles(self):
        """ 
        """
        return self._power_system_resource_roles

    def set_power_system_resource_roles(self, value):
        for x in self._power_system_resource_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._power_system_resource_roles = value

    power_system_resource_roles = property(get_power_system_resource_roles, set_power_system_resource_roles)

    def add_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._erp_organisation = self
            self._power_system_resource_roles.append(obj)

    def remove_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._erp_organisation = None
            self._power_system_resource_roles.remove(obj)
    # >>> power_system_resource_roles

    # <<< asset_roles
    # @generated
    def get_asset_roles(self):
        """ 
        """
        return self._asset_roles

    def set_asset_roles(self, value):
        for x in self._asset_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._asset_roles = value

    asset_roles = property(get_asset_roles, set_asset_roles)

    def add_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._erp_organisation = self
            self._asset_roles.append(obj)

    def remove_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._erp_organisation = None
            self._asset_roles.remove(obj)
    # >>> asset_roles

    # <<< land_property_roles
    # @generated
    def get_land_property_roles(self):
        """ 
        """
        return self._land_property_roles

    def set_land_property_roles(self, value):
        for x in self._land_property_roles:
            x._erp_organisation = None
        for y in value:
            y._erp_organisation = self
        self._land_property_roles = value

    land_property_roles = property(get_land_property_roles, set_land_property_roles)

    def add_land_property_roles(self, *land_property_roles):
        for obj in land_property_roles:
            obj._erp_organisation = self
            self._land_property_roles.append(obj)

    def remove_land_property_roles(self, *land_property_roles):
        for obj in land_property_roles:
            obj._erp_organisation = None
            self._land_property_roles.remove(obj)
    # >>> land_property_roles

    # <<< parent_organisation_roles
    # @generated
    def get_parent_organisation_roles(self):
        """ 
        """
        return self._parent_organisation_roles

    def set_parent_organisation_roles(self, value):
        for x in self._parent_organisation_roles:
            x._child_organisation = None
        for y in value:
            y._child_organisation = self
        self._parent_organisation_roles = value

    parent_organisation_roles = property(get_parent_organisation_roles, set_parent_organisation_roles)

    def add_parent_organisation_roles(self, *parent_organisation_roles):
        for obj in parent_organisation_roles:
            obj._child_organisation = self
            self._parent_organisation_roles.append(obj)

    def remove_parent_organisation_roles(self, *parent_organisation_roles):
        for obj in parent_organisation_roles:
            obj._child_organisation = None
            self._parent_organisation_roles.remove(obj)
    # >>> parent_organisation_roles

    # <<< child_organisation_roles
    # @generated
    def get_child_organisation_roles(self):
        """ 
        """
        return self._child_organisation_roles

    def set_child_organisation_roles(self, value):
        for x in self._child_organisation_roles:
            x._parent_organisation = None
        for y in value:
            y._parent_organisation = self
        self._child_organisation_roles = value

    child_organisation_roles = property(get_child_organisation_roles, set_child_organisation_roles)

    def add_child_organisation_roles(self, *child_organisation_roles):
        for obj in child_organisation_roles:
            obj._parent_organisation = self
            self._child_organisation_roles.append(obj)

    def remove_child_organisation_roles(self, *child_organisation_roles):
        for obj in child_organisation_roles:
            obj._parent_organisation = None
            self._child_organisation_roles.remove(obj)
    # >>> child_organisation_roles

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.organisations if q != self]
            self._crews._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._crews.remove(obj)
    # >>> crews


    def __str__(self):
        """ Returns a string representation of the ErpOrganisation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_organisation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpOrganisation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpOrganisation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.document_roles:
            s += '%s<%s:ErpOrganisation.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:ErpOrganisation.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:ErpOrganisation.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:ErpOrganisation.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:ErpOrganisation.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.requests:
            s += '%s<%s:ErpOrganisation.requests rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:ErpOrganisation.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.int_sched_agreement:
            s += '%s<%s:ErpOrganisation.int_sched_agreement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.registered_resources:
            s += '%s<%s:ErpOrganisation.registered_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:ErpOrganisation.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:ErpOrganisation.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.land_property_roles:
            s += '%s<%s:ErpOrganisation.land_property_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.parent_organisation_roles:
            s += '%s<%s:ErpOrganisation.parent_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.child_organisation_roles:
            s += '%s<%s:ErpOrganisation.child_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:ErpOrganisation.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ErpOrganisation.code>%s</%s:ErpOrganisation.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:ErpOrganisation.category>%s</%s:ErpOrganisation.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:ErpOrganisation.mode>%s</%s:ErpOrganisation.mode>' % \
            (indent, ns_prefix, self.mode, ns_prefix)
        s += '%s<%s:ErpOrganisation.opt_out>%s</%s:ErpOrganisation.opt_out>' % \
            (indent, ns_prefix, self.opt_out, ns_prefix)
        s += '%s<%s:ErpOrganisation.industry_id>%s</%s:ErpOrganisation.industry_id>' % \
            (indent, ns_prefix, self.industry_id, ns_prefix)
        s += '%s<%s:ErpOrganisation.is_profit_center>%s</%s:ErpOrganisation.is_profit_center>' % \
            (indent, ns_prefix, self.is_profit_center, ns_prefix)
        s += '%s<%s:ErpOrganisation.is_cost_center>%s</%s:ErpOrganisation.is_cost_center>' % \
            (indent, ns_prefix, self.is_cost_center, ns_prefix)
        s += '%s<%s:ErpOrganisation.government_id>%s</%s:ErpOrganisation.government_id>' % \
            (indent, ns_prefix, self.government_id, ns_prefix)
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
        for obj in self.business_roles:
            s += '%s<%s:Organisation.business_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Organisation.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.street_address is not None:
            s += '%s<%s:Organisation.street_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.street_address.uri)
        for obj in self.market_roles:
            s += '%s<%s:Organisation.market_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.postal_address is not None:
            s += '%s<%s:Organisation.postal_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.postal_address.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Organisation.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpOrganisation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_organisation.serialize


class DocErpPersonRole(Role):
    """ Roles played between Persons and Documents.
    """
    # <<< doc_erp_person_role
    # @generated
    def __init__(self, erp_person=None, document=None, **kw_args):
        """ Initialises a new 'DocErpPersonRole' instance.
        """

        self._erp_person = None
        self.erp_person = erp_person

        self._document = None
        self.document = document


        super(DocErpPersonRole, self).__init__(**kw_args)
    # >>> doc_erp_person_role

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.document_roles if x != self]
            self._erp_person._document_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._document_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.erp_person_roles if x != self]
            self._document._erp_person_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._erp_person_roles.append(self)

    document = property(get_document, set_document)
    # >>> document


    def __str__(self):
        """ Returns a string representation of the DocErpPersonRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_erp_person_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocErpPersonRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocErpPersonRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_person is not None:
            s += '%s<%s:DocErpPersonRole.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        if self.document is not None:
            s += '%s<%s:DocErpPersonRole.document rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocErpPersonRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_erp_person_role.serialize


class ErpPayableLineItem(IdentifiedObject):
    """ Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as credit memos.
    """
    # <<< erp_payable_line_item
    # @generated
    def __init__(self, erp_journal_entries=None, status=None, erp_payments=None, erp_invoice_line_item=None, erp_payable=None, **kw_args):
        """ Initialises a new 'ErpPayableLineItem' instance.
        """

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []

        self.status = status

        self._erp_payments = []
        if erp_payments is not None:
            self.erp_payments = erp_payments
        else:
            self.erp_payments = []

        self._erp_invoice_line_item = None
        self.erp_invoice_line_item = erp_invoice_line_item

        self._erp_payable = None
        self.erp_payable = erp_payable


        super(ErpPayableLineItem, self).__init__(**kw_args)
    # >>> erp_payable_line_item

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for p in self._erp_journal_entries:
            filtered = [q for q in p.erp_payable_line_items if q != self]
            self._erp_journal_entries._erp_payable_line_items = filtered
        for r in value:
            if self not in r._erp_payable_line_items:
                r._erp_payable_line_items.append(self)
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self not in obj._erp_payable_line_items:
                obj._erp_payable_line_items.append(self)
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self in obj._erp_payable_line_items:
                obj._erp_payable_line_items.remove(self)
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< erp_payments
    # @generated
    def get_erp_payments(self):
        """ 
        """
        return self._erp_payments

    def set_erp_payments(self, value):
        for p in self._erp_payments:
            filtered = [q for q in p.erp_payable_line_items if q != self]
            self._erp_payments._erp_payable_line_items = filtered
        for r in value:
            if self not in r._erp_payable_line_items:
                r._erp_payable_line_items.append(self)
        self._erp_payments = value

    erp_payments = property(get_erp_payments, set_erp_payments)

    def add_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self not in obj._erp_payable_line_items:
                obj._erp_payable_line_items.append(self)
            self._erp_payments.append(obj)

    def remove_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self in obj._erp_payable_line_items:
                obj._erp_payable_line_items.remove(self)
            self._erp_payments.remove(obj)
    # >>> erp_payments

    # <<< erp_invoice_line_item
    # @generated
    def get_erp_invoice_line_item(self):
        """ 
        """
        return self._erp_invoice_line_item

    def set_erp_invoice_line_item(self, value):
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_payable_line_item = None

        self._erp_invoice_line_item = value
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_payable_line_item = self

    erp_invoice_line_item = property(get_erp_invoice_line_item, set_erp_invoice_line_item)
    # >>> erp_invoice_line_item

    # <<< erp_payable
    # @generated
    def get_erp_payable(self):
        """ 
        """
        return self._erp_payable

    def set_erp_payable(self, value):
        if self._erp_payable is not None:
            filtered = [x for x in self.erp_payable.erp_payable_line_items if x != self]
            self._erp_payable._erp_payable_line_items = filtered

        self._erp_payable = value
        if self._erp_payable is not None:
            self._erp_payable._erp_payable_line_items.append(self)

    erp_payable = property(get_erp_payable, set_erp_payable)
    # >>> erp_payable


    def __str__(self):
        """ Returns a string representation of the ErpPayableLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_payable_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPayableLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPayableLineItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_journal_entries:
            s += '%s<%s:ErpPayableLineItem.erp_journal_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ErpPayableLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.erp_payments:
            s += '%s<%s:ErpPayableLineItem.erp_payments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_invoice_line_item is not None:
            s += '%s<%s:ErpPayableLineItem.erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice_line_item.uri)
        if self.erp_payable is not None:
            s += '%s<%s:ErpPayableLineItem.erp_payable rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_payable.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPayableLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_payable_line_item.serialize


class OrgOrgRole(Role):
    """ Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.
    """
    # <<< org_org_role
    # @generated
    def __init__(self, client_id='', child_organisation=None, parent_organisation=None, **kw_args):
        """ Initialises a new 'OrgOrgRole' instance.
        """
        # Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc. 
        self.client_id = client_id


        self._child_organisation = None
        self.child_organisation = child_organisation

        self._parent_organisation = None
        self.parent_organisation = parent_organisation


        super(OrgOrgRole, self).__init__(**kw_args)
    # >>> org_org_role

    # <<< child_organisation
    # @generated
    def get_child_organisation(self):
        """ 
        """
        return self._child_organisation

    def set_child_organisation(self, value):
        if self._child_organisation is not None:
            filtered = [x for x in self.child_organisation.parent_organisation_roles if x != self]
            self._child_organisation._parent_organisation_roles = filtered

        self._child_organisation = value
        if self._child_organisation is not None:
            self._child_organisation._parent_organisation_roles.append(self)

    child_organisation = property(get_child_organisation, set_child_organisation)
    # >>> child_organisation

    # <<< parent_organisation
    # @generated
    def get_parent_organisation(self):
        """ 
        """
        return self._parent_organisation

    def set_parent_organisation(self, value):
        if self._parent_organisation is not None:
            filtered = [x for x in self.parent_organisation.child_organisation_roles if x != self]
            self._parent_organisation._child_organisation_roles = filtered

        self._parent_organisation = value
        if self._parent_organisation is not None:
            self._parent_organisation._child_organisation_roles.append(self)

    parent_organisation = property(get_parent_organisation, set_parent_organisation)
    # >>> parent_organisation


    def __str__(self):
        """ Returns a string representation of the OrgOrgRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_org_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgOrgRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgOrgRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.child_organisation is not None:
            s += '%s<%s:OrgOrgRole.child_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.child_organisation.uri)
        if self.parent_organisation is not None:
            s += '%s<%s:OrgOrgRole.parent_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent_organisation.uri)
        s += '%s<%s:OrgOrgRole.client_id>%s</%s:OrgOrgRole.client_id>' % \
            (indent, ns_prefix, self.client_id, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgOrgRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_org_role.serialize


class ErpReqLineItem(IdentifiedObject):
    """ Information that describes a requested item and its attributes.
    """
    # <<< erp_req_line_item
    # @generated
    def __init__(self, delivery_date='', code='', quantity=0, cost=0.0, erp_requisition=None, type_material=None, erp_poline_item=None, status=None, erp_quote_line_item=None, type_asset=None, **kw_args):
        """ Initialises a new 'ErpReqLineItem' instance.
        """
 
        self.delivery_date = delivery_date

 
        self.code = code

        # Quantity of item requisitioned. 
        self.quantity = quantity

        # Cost of material 
        self.cost = cost


        self._erp_requisition = None
        self.erp_requisition = erp_requisition

        self._type_material = None
        self.type_material = type_material

        self._erp_poline_item = None
        self.erp_poline_item = erp_poline_item

        self.status = status

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._type_asset = None
        self.type_asset = type_asset


        super(ErpReqLineItem, self).__init__(**kw_args)
    # >>> erp_req_line_item

    # <<< erp_requisition
    # @generated
    def get_erp_requisition(self):
        """ 
        """
        return self._erp_requisition

    def set_erp_requisition(self, value):
        if self._erp_requisition is not None:
            filtered = [x for x in self.erp_requisition.erp_req_line_items if x != self]
            self._erp_requisition._erp_req_line_items = filtered

        self._erp_requisition = value
        if self._erp_requisition is not None:
            self._erp_requisition._erp_req_line_items.append(self)

    erp_requisition = property(get_erp_requisition, set_erp_requisition)
    # >>> erp_requisition

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.erp_req_line_items if x != self]
            self._type_material._erp_req_line_items = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._erp_req_line_items.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material

    # <<< erp_poline_item
    # @generated
    def get_erp_poline_item(self):
        """ 
        """
        return self._erp_poline_item

    def set_erp_poline_item(self, value):
        if self._erp_poline_item is not None:
            self._erp_poline_item._erp_req_line_item = None

        self._erp_poline_item = value
        if self._erp_poline_item is not None:
            self._erp_poline_item._erp_req_line_item = self

    erp_poline_item = property(get_erp_poline_item, set_erp_poline_item)
    # >>> erp_poline_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._erp_req_line_item = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._erp_req_line_item = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            filtered = [x for x in self.type_asset.erp_req_line_items if x != self]
            self._type_asset._erp_req_line_items = filtered

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._erp_req_line_items.append(self)

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset


    def __str__(self):
        """ Returns a string representation of the ErpReqLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_req_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpReqLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpReqLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_requisition is not None:
            s += '%s<%s:ErpReqLineItem.erp_requisition rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_requisition.uri)
        if self.type_material is not None:
            s += '%s<%s:ErpReqLineItem.type_material rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_material.uri)
        if self.erp_poline_item is not None:
            s += '%s<%s:ErpReqLineItem.erp_poline_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_poline_item.uri)
        if self.status is not None:
            s += '%s<%s:ErpReqLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.erp_quote_line_item is not None:
            s += '%s<%s:ErpReqLineItem.erp_quote_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_quote_line_item.uri)
        if self.type_asset is not None:
            s += '%s<%s:ErpReqLineItem.type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_asset.uri)
        s += '%s<%s:ErpReqLineItem.delivery_date>%s</%s:ErpReqLineItem.delivery_date>' % \
            (indent, ns_prefix, self.delivery_date, ns_prefix)
        s += '%s<%s:ErpReqLineItem.code>%s</%s:ErpReqLineItem.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:ErpReqLineItem.quantity>%s</%s:ErpReqLineItem.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:ErpReqLineItem.cost>%s</%s:ErpReqLineItem.cost>' % \
            (indent, ns_prefix, self.cost, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpReqLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_req_line_item.serialize


class ErpLedger(Document):
    """ In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.
    """
    # <<< erp_ledger
    # @generated
    def __init__(self, erp_ledger_entries=None, **kw_args):
        """ Initialises a new 'ErpLedger' instance.
        """

        self._erp_ledger_entries = []
        if erp_ledger_entries is not None:
            self.erp_ledger_entries = erp_ledger_entries
        else:
            self.erp_ledger_entries = []


        super(ErpLedger, self).__init__(**kw_args)
    # >>> erp_ledger

    # <<< erp_ledger_entries
    # @generated
    def get_erp_ledger_entries(self):
        """ 
        """
        return self._erp_ledger_entries

    def set_erp_ledger_entries(self, value):
        for x in self._erp_ledger_entries:
            x._erp_ledger = None
        for y in value:
            y._erp_ledger = self
        self._erp_ledger_entries = value

    erp_ledger_entries = property(get_erp_ledger_entries, set_erp_ledger_entries)

    def add_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            obj._erp_ledger = self
            self._erp_ledger_entries.append(obj)

    def remove_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            obj._erp_ledger = None
            self._erp_ledger_entries.remove(obj)
    # >>> erp_ledger_entries


    def __str__(self):
        """ Returns a string representation of the ErpLedger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_ledger.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpLedger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpLedger", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_ledger_entries:
            s += '%s<%s:ErpLedger.erp_ledger_entries rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpLedger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_ledger.serialize


class DocOrgRole(Role):
    """ Roles played between Organisations and Documents.
    """
    # <<< doc_org_role
    # @generated
    def __init__(self, erp_organisation=None, document=None, **kw_args):
        """ Initialises a new 'DocOrgRole' instance.
        """

        self._erp_organisation = None
        self.erp_organisation = erp_organisation

        self._document = None
        self.document = document


        super(DocOrgRole, self).__init__(**kw_args)
    # >>> doc_org_role

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.document_roles if x != self]
            self._erp_organisation._document_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._document_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.erp_organisation_roles if x != self]
            self._document._erp_organisation_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._erp_organisation_roles.append(self)

    document = property(get_document, set_document)
    # >>> document


    def __str__(self):
        """ Returns a string representation of the DocOrgRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_org_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocOrgRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocOrgRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_organisation is not None:
            s += '%s<%s:DocOrgRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
        if self.document is not None:
            s += '%s<%s:DocOrgRole.document rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocOrgRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_org_role.serialize


class ErpInventory(IdentifiedObject):
    """ Utility inventory-related information about an item or part (and not for description of the item and its attributes). It is used by ERP applications to enable the synchronization of Inventory data that exists on separate Item Master databases. This data is not the master data that describes the attributes of the item such as dimensions, weight, or unit of measure - it describes the item as it exists at a specific location.
    """
    # <<< erp_inventory
    # @generated
    def __init__(self, asset=None, status=None, **kw_args):
        """ Initialises a new 'ErpInventory' instance.
        """

        self._asset = None
        self.asset = asset

        self.status = status


        super(ErpInventory, self).__init__(**kw_args)
    # >>> erp_inventory

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            self._asset._erp_inventory = None

        self._asset = value
        if self._asset is not None:
            self._asset._erp_inventory = self

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpInventory.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_inventory.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpInventory.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpInventory", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:ErpInventory.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.status is not None:
            s += '%s<%s:ErpInventory.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpInventory")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_inventory.serialize


class ErpJournal(Document):
    """ Book for recording accounting transactions as they occur. Transactions and adjustments are first recorded in a journal, which is like a diary of instructions, advising which account to be charged and by how much. A journal represents a change in the balances of a business's financial accounts. Many tasks or transactions throughout an enterprise will result in the creation of a journal. Some examples are creating a customer invoice, paying a vendor, transferring inventory, or paying employees.
    """
    # <<< erp_journal
    # @generated
    def __init__(self, erp_journal_entries=None, **kw_args):
        """ Initialises a new 'ErpJournal' instance.
        """

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []


        super(ErpJournal, self).__init__(**kw_args)
    # >>> erp_journal

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for x in self._erp_journal_entries:
            x._erp_journal = None
        for y in value:
            y._erp_journal = self
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            obj._erp_journal = self
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            obj._erp_journal = None
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries


    def __str__(self):
        """ Returns a string representation of the ErpJournal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_journal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpJournal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpJournal", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_journal_entries:
            s += '%s<%s:ErpJournal.erp_journal_entries rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpJournal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_journal.serialize


class ErpProjectAccounting(Document):
    """ Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.
    """
    # <<< erp_project_accounting
    # @generated
    def __init__(self, projects=None, work_cost_details=None, works=None, erp_time_entries=None, **kw_args):
        """ Initialises a new 'ErpProjectAccounting' instance.
        """

        self._projects = []
        if projects is not None:
            self.projects = projects
        else:
            self.projects = []

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._erp_time_entries = []
        if erp_time_entries is not None:
            self.erp_time_entries = erp_time_entries
        else:
            self.erp_time_entries = []


        super(ErpProjectAccounting, self).__init__(**kw_args)
    # >>> erp_project_accounting

    # <<< projects
    # @generated
    def get_projects(self):
        """ 
        """
        return self._projects

    def set_projects(self, value):
        for x in self._projects:
            x._erp_project_accounting = None
        for y in value:
            y._erp_project_accounting = self
        self._projects = value

    projects = property(get_projects, set_projects)

    def add_projects(self, *projects):
        for obj in projects:
            obj._erp_project_accounting = self
            self._projects.append(obj)

    def remove_projects(self, *projects):
        for obj in projects:
            obj._erp_project_accounting = None
            self._projects.remove(obj)
    # >>> projects

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._erp_project_accounting = None
        for y in value:
            y._erp_project_accounting = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._erp_project_accounting = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._erp_project_accounting = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._erp_project_accounting = None
        for y in value:
            y._erp_project_accounting = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._erp_project_accounting = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._erp_project_accounting = None
            self._works.remove(obj)
    # >>> works

    # <<< erp_time_entries
    # @generated
    def get_erp_time_entries(self):
        """ 
        """
        return self._erp_time_entries

    def set_erp_time_entries(self, value):
        for x in self._erp_time_entries:
            x._erp_project_accounting = None
        for y in value:
            y._erp_project_accounting = self
        self._erp_time_entries = value

    erp_time_entries = property(get_erp_time_entries, set_erp_time_entries)

    def add_erp_time_entries(self, *erp_time_entries):
        for obj in erp_time_entries:
            obj._erp_project_accounting = self
            self._erp_time_entries.append(obj)

    def remove_erp_time_entries(self, *erp_time_entries):
        for obj in erp_time_entries:
            obj._erp_project_accounting = None
            self._erp_time_entries.remove(obj)
    # >>> erp_time_entries


    def __str__(self):
        """ Returns a string representation of the ErpProjectAccounting.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_project_accounting.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpProjectAccounting.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpProjectAccounting", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.projects:
            s += '%s<%s:ErpProjectAccounting.projects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_cost_details:
            s += '%s<%s:ErpProjectAccounting.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.works:
            s += '%s<%s:ErpProjectAccounting.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_time_entries:
            s += '%s<%s:ErpProjectAccounting.erp_time_entries rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpProjectAccounting")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_project_accounting.serialize


class ErpQuoteLineItem(IdentifiedObject):
    """ Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.
    """
    # <<< erp_quote_line_item
    # @generated
    def __init__(self, asset_model_catalogue_item=None, design=None, request=None, erp_req_line_item=None, erp_invoice_line_item=None, status=None, erp_quote=None, **kw_args):
        """ Initialises a new 'ErpQuoteLineItem' instance.
        """

        self._asset_model_catalogue_item = None
        self.asset_model_catalogue_item = asset_model_catalogue_item

        self._design = None
        self.design = design

        self._request = None
        self.request = request

        self._erp_req_line_item = None
        self.erp_req_line_item = erp_req_line_item

        self._erp_invoice_line_item = None
        self.erp_invoice_line_item = erp_invoice_line_item

        self.status = status

        self._erp_quote = None
        self.erp_quote = erp_quote


        super(ErpQuoteLineItem, self).__init__(**kw_args)
    # >>> erp_quote_line_item

    # <<< asset_model_catalogue_item
    # @generated
    def get_asset_model_catalogue_item(self):
        """ 
        """
        return self._asset_model_catalogue_item

    def set_asset_model_catalogue_item(self, value):
        if self._asset_model_catalogue_item is not None:
            filtered = [x for x in self.asset_model_catalogue_item.erp_quote_line_items if x != self]
            self._asset_model_catalogue_item._erp_quote_line_items = filtered

        self._asset_model_catalogue_item = value
        if self._asset_model_catalogue_item is not None:
            self._asset_model_catalogue_item._erp_quote_line_items.append(self)

    asset_model_catalogue_item = property(get_asset_model_catalogue_item, set_asset_model_catalogue_item)
    # >>> asset_model_catalogue_item

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            self._design._erp_quote_line_item = None

        self._design = value
        if self._design is not None:
            self._design._erp_quote_line_item = self

    design = property(get_design, set_design)
    # >>> design

    # <<< request
    # @generated
    def get_request(self):
        """ 
        """
        return self._request

    def set_request(self, value):
        if self._request is not None:
            self._request._erp_quote_line_item = None

        self._request = value
        if self._request is not None:
            self._request._erp_quote_line_item = self

    request = property(get_request, set_request)
    # >>> request

    # <<< erp_req_line_item
    # @generated
    def get_erp_req_line_item(self):
        """ 
        """
        return self._erp_req_line_item

    def set_erp_req_line_item(self, value):
        if self._erp_req_line_item is not None:
            self._erp_req_line_item._erp_quote_line_item = None

        self._erp_req_line_item = value
        if self._erp_req_line_item is not None:
            self._erp_req_line_item._erp_quote_line_item = self

    erp_req_line_item = property(get_erp_req_line_item, set_erp_req_line_item)
    # >>> erp_req_line_item

    # <<< erp_invoice_line_item
    # @generated
    def get_erp_invoice_line_item(self):
        """ Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
        """
        return self._erp_invoice_line_item

    def set_erp_invoice_line_item(self, value):
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_quote_line_item = None

        self._erp_invoice_line_item = value
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_quote_line_item = self

    erp_invoice_line_item = property(get_erp_invoice_line_item, set_erp_invoice_line_item)
    # >>> erp_invoice_line_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< erp_quote
    # @generated
    def get_erp_quote(self):
        """ 
        """
        return self._erp_quote

    def set_erp_quote(self, value):
        if self._erp_quote is not None:
            filtered = [x for x in self.erp_quote.erp_quote_line_items if x != self]
            self._erp_quote._erp_quote_line_items = filtered

        self._erp_quote = value
        if self._erp_quote is not None:
            self._erp_quote._erp_quote_line_items.append(self)

    erp_quote = property(get_erp_quote, set_erp_quote)
    # >>> erp_quote


    def __str__(self):
        """ Returns a string representation of the ErpQuoteLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_quote_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpQuoteLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpQuoteLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset_model_catalogue_item is not None:
            s += '%s<%s:ErpQuoteLineItem.asset_model_catalogue_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_model_catalogue_item.uri)
        if self.design is not None:
            s += '%s<%s:ErpQuoteLineItem.design rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design.uri)
        if self.request is not None:
            s += '%s<%s:ErpQuoteLineItem.request rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.request.uri)
        if self.erp_req_line_item is not None:
            s += '%s<%s:ErpQuoteLineItem.erp_req_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_req_line_item.uri)
        if self.erp_invoice_line_item is not None:
            s += '%s<%s:ErpQuoteLineItem.erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice_line_item.uri)
        if self.status is not None:
            s += '%s<%s:ErpQuoteLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.erp_quote is not None:
            s += '%s<%s:ErpQuoteLineItem.erp_quote rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_quote.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpQuoteLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_quote_line_item.serialize


class ErpPerson(IdentifiedObject):
    """ General purpose information for name and other information to contact people.
    """
    # <<< erp_person
    # @generated
    def __init__(self, prefix='', government_id='', last_name='', category='', first_name='', suffix='', special_need='', m_name='', erp_telephone_numbers=None, document_roles=None, electronic_addresses=None, crews=None, appointments=None, labor_items=None, measurement_values=None, call_backs=None, activity_records=None, erp_organisation_roles=None, crafts=None, location_roles=None, skills=None, customer_data=None, change_items=None, switching_step_roles=None, erp_personnel=None, erp_competency=None, land_property_roles=None, status=None, **kw_args):
        """ Initialises a new 'ErpPerson' instance.
        """
        # A prefix or title for the person's name, such as Miss, Mister, Doctor, etc. 
        self.prefix = prefix

        # Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States). 
        self.government_id = government_id

        # Person's last (family, sir) name. 
        self.last_name = last_name

        # Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations. 
        self.category = category

        # Person's first name. 
        self.first_name = first_name

        # A suffix for the person's name, such as II, III, etc. 
        self.suffix = suffix

        # Special service needs for the person (contact) are described; examples include life support, etc. 
        self.special_need = special_need

        # Middle name(s) or initial(s). 
        self.m_name = m_name


        self._erp_telephone_numbers = []
        if erp_telephone_numbers is not None:
            self.erp_telephone_numbers = erp_telephone_numbers
        else:
            self.erp_telephone_numbers = []

        self._document_roles = []
        if document_roles is not None:
            self.document_roles = document_roles
        else:
            self.document_roles = []

        self._electronic_addresses = []
        if electronic_addresses is not None:
            self.electronic_addresses = electronic_addresses
        else:
            self.electronic_addresses = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._appointments = []
        if appointments is not None:
            self.appointments = appointments
        else:
            self.appointments = []

        self._labor_items = []
        if labor_items is not None:
            self.labor_items = labor_items
        else:
            self.labor_items = []

        self._measurement_values = []
        if measurement_values is not None:
            self.measurement_values = measurement_values
        else:
            self.measurement_values = []

        self._call_backs = []
        if call_backs is not None:
            self.call_backs = call_backs
        else:
            self.call_backs = []

        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._crafts = []
        if crafts is not None:
            self.crafts = crafts
        else:
            self.crafts = []

        self._location_roles = []
        if location_roles is not None:
            self.location_roles = location_roles
        else:
            self.location_roles = []

        self._skills = []
        if skills is not None:
            self.skills = skills
        else:
            self.skills = []

        self._customer_data = None
        self.customer_data = customer_data

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._switching_step_roles = []
        if switching_step_roles is not None:
            self.switching_step_roles = switching_step_roles
        else:
            self.switching_step_roles = []

        self._erp_personnel = None
        self.erp_personnel = erp_personnel

        self._erp_competency = None
        self.erp_competency = erp_competency

        self._land_property_roles = []
        if land_property_roles is not None:
            self.land_property_roles = land_property_roles
        else:
            self.land_property_roles = []

        self.status = status


        super(ErpPerson, self).__init__(**kw_args)
    # >>> erp_person

    # <<< erp_telephone_numbers
    # @generated
    def get_erp_telephone_numbers(self):
        """ 
        """
        return self._erp_telephone_numbers

    def set_erp_telephone_numbers(self, value):
        for p in self._erp_telephone_numbers:
            filtered = [q for q in p.erp_persons if q != self]
            self._erp_telephone_numbers._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._erp_telephone_numbers = value

    erp_telephone_numbers = property(get_erp_telephone_numbers, set_erp_telephone_numbers)

    def add_erp_telephone_numbers(self, *erp_telephone_numbers):
        for obj in erp_telephone_numbers:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._erp_telephone_numbers.append(obj)

    def remove_erp_telephone_numbers(self, *erp_telephone_numbers):
        for obj in erp_telephone_numbers:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._erp_telephone_numbers.remove(obj)
    # >>> erp_telephone_numbers

    # <<< document_roles
    # @generated
    def get_document_roles(self):
        """ 
        """
        return self._document_roles

    def set_document_roles(self, value):
        for x in self._document_roles:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._document_roles = value

    document_roles = property(get_document_roles, set_document_roles)

    def add_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._erp_person = self
            self._document_roles.append(obj)

    def remove_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._erp_person = None
            self._document_roles.remove(obj)
    # >>> document_roles

    # <<< electronic_addresses
    # @generated
    def get_electronic_addresses(self):
        """ 
        """
        return self._electronic_addresses

    def set_electronic_addresses(self, value):
        for x in self._electronic_addresses:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._electronic_addresses = value

    electronic_addresses = property(get_electronic_addresses, set_electronic_addresses)

    def add_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._erp_person = self
            self._electronic_addresses.append(obj)

    def remove_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._erp_person = None
            self._electronic_addresses.remove(obj)
    # >>> electronic_addresses

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews to which this ErpPerson belongs.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.crew_members if q != self]
            self._crews._crew_members = filtered
        for r in value:
            if self not in r._crew_members:
                r._crew_members.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._crew_members:
                obj._crew_members.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._crew_members:
                obj._crew_members.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< appointments
    # @generated
    def get_appointments(self):
        """ 
        """
        return self._appointments

    def set_appointments(self, value):
        for p in self._appointments:
            filtered = [q for q in p.erp_persons if q != self]
            self._appointments._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._appointments = value

    appointments = property(get_appointments, set_appointments)

    def add_appointments(self, *appointments):
        for obj in appointments:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._appointments.append(obj)

    def remove_appointments(self, *appointments):
        for obj in appointments:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._appointments.remove(obj)
    # >>> appointments

    # <<< labor_items
    # @generated
    def get_labor_items(self):
        """ 
        """
        return self._labor_items

    def set_labor_items(self, value):
        for p in self._labor_items:
            filtered = [q for q in p.erp_persons if q != self]
            self._labor_items._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._labor_items = value

    labor_items = property(get_labor_items, set_labor_items)

    def add_labor_items(self, *labor_items):
        for obj in labor_items:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._labor_items.append(obj)

    def remove_labor_items(self, *labor_items):
        for obj in labor_items:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._labor_items.remove(obj)
    # >>> labor_items

    # <<< measurement_values
    # @generated
    def get_measurement_values(self):
        """ 
        """
        return self._measurement_values

    def set_measurement_values(self, value):
        for x in self._measurement_values:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._measurement_values = value

    measurement_values = property(get_measurement_values, set_measurement_values)

    def add_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._erp_person = self
            self._measurement_values.append(obj)

    def remove_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._erp_person = None
            self._measurement_values.remove(obj)
    # >>> measurement_values

    # <<< call_backs
    # @generated
    def get_call_backs(self):
        """ 
        """
        return self._call_backs

    def set_call_backs(self, value):
        for p in self._call_backs:
            filtered = [q for q in p.erp_persons if q != self]
            self._call_backs._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._call_backs = value

    call_backs = property(get_call_backs, set_call_backs)

    def add_call_backs(self, *call_backs):
        for obj in call_backs:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._call_backs.append(obj)

    def remove_call_backs(self, *call_backs):
        for obj in call_backs:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._call_backs.remove(obj)
    # >>> call_backs

    # <<< activity_records
    # @generated
    def get_activity_records(self):
        """ 
        """
        return self._activity_records

    def set_activity_records(self, value):
        for p in self._activity_records:
            filtered = [q for q in p.erp_persons if q != self]
            self._activity_records._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._activity_records = value

    activity_records = property(get_activity_records, set_activity_records)

    def add_activity_records(self, *activity_records):
        for obj in activity_records:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._activity_records.append(obj)

    def remove_activity_records(self, *activity_records):
        for obj in activity_records:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._activity_records.remove(obj)
    # >>> activity_records

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for x in self._erp_organisation_roles:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._erp_person = self
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._erp_person = None
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< crafts
    # @generated
    def get_crafts(self):
        """ 
        """
        return self._crafts

    def set_crafts(self, value):
        for p in self._crafts:
            filtered = [q for q in p.erp_persons if q != self]
            self._crafts._erp_persons = filtered
        for r in value:
            if self not in r._erp_persons:
                r._erp_persons.append(self)
        self._crafts = value

    crafts = property(get_crafts, set_crafts)

    def add_crafts(self, *crafts):
        for obj in crafts:
            if self not in obj._erp_persons:
                obj._erp_persons.append(self)
            self._crafts.append(obj)

    def remove_crafts(self, *crafts):
        for obj in crafts:
            if self in obj._erp_persons:
                obj._erp_persons.remove(self)
            self._crafts.remove(obj)
    # >>> crafts

    # <<< location_roles
    # @generated
    def get_location_roles(self):
        """ 
        """
        return self._location_roles

    def set_location_roles(self, value):
        for x in self._location_roles:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._location_roles = value

    location_roles = property(get_location_roles, set_location_roles)

    def add_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._erp_person = self
            self._location_roles.append(obj)

    def remove_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._erp_person = None
            self._location_roles.remove(obj)
    # >>> location_roles

    # <<< skills
    # @generated
    def get_skills(self):
        """ 
        """
        return self._skills

    def set_skills(self, value):
        for x in self._skills:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._skills = value

    skills = property(get_skills, set_skills)

    def add_skills(self, *skills):
        for obj in skills:
            obj._erp_person = self
            self._skills.append(obj)

    def remove_skills(self, *skills):
        for obj in skills:
            obj._erp_person = None
            self._skills.remove(obj)
    # >>> skills

    # <<< customer_data
    # @generated
    def get_customer_data(self):
        """ 
        """
        return self._customer_data

    def set_customer_data(self, value):
        if self._customer_data is not None:
            filtered = [x for x in self.customer_data.erp_persons if x != self]
            self._customer_data._erp_persons = filtered

        self._customer_data = value
        if self._customer_data is not None:
            self._customer_data._erp_persons.append(self)

    customer_data = property(get_customer_data, set_customer_data)
    # >>> customer_data

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._erp_person = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._erp_person = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< switching_step_roles
    # @generated
    def get_switching_step_roles(self):
        """ 
        """
        return self._switching_step_roles

    def set_switching_step_roles(self, value):
        for x in self._switching_step_roles:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._switching_step_roles = value

    switching_step_roles = property(get_switching_step_roles, set_switching_step_roles)

    def add_switching_step_roles(self, *switching_step_roles):
        for obj in switching_step_roles:
            obj._erp_person = self
            self._switching_step_roles.append(obj)

    def remove_switching_step_roles(self, *switching_step_roles):
        for obj in switching_step_roles:
            obj._erp_person = None
            self._switching_step_roles.remove(obj)
    # >>> switching_step_roles

    # <<< erp_personnel
    # @generated
    def get_erp_personnel(self):
        """ 
        """
        return self._erp_personnel

    def set_erp_personnel(self, value):
        if self._erp_personnel is not None:
            filtered = [x for x in self.erp_personnel.erp_persons if x != self]
            self._erp_personnel._erp_persons = filtered

        self._erp_personnel = value
        if self._erp_personnel is not None:
            self._erp_personnel._erp_persons.append(self)

    erp_personnel = property(get_erp_personnel, set_erp_personnel)
    # >>> erp_personnel

    # <<< erp_competency
    # @generated
    def get_erp_competency(self):
        """ 
        """
        return self._erp_competency

    def set_erp_competency(self, value):
        if self._erp_competency is not None:
            filtered = [x for x in self.erp_competency.erp_persons if x != self]
            self._erp_competency._erp_persons = filtered

        self._erp_competency = value
        if self._erp_competency is not None:
            self._erp_competency._erp_persons.append(self)

    erp_competency = property(get_erp_competency, set_erp_competency)
    # >>> erp_competency

    # <<< land_property_roles
    # @generated
    def get_land_property_roles(self):
        """ 
        """
        return self._land_property_roles

    def set_land_property_roles(self, value):
        for x in self._land_property_roles:
            x._erp_person = None
        for y in value:
            y._erp_person = self
        self._land_property_roles = value

    land_property_roles = property(get_land_property_roles, set_land_property_roles)

    def add_land_property_roles(self, *land_property_roles):
        for obj in land_property_roles:
            obj._erp_person = self
            self._land_property_roles.append(obj)

    def remove_land_property_roles(self, *land_property_roles):
        for obj in land_property_roles:
            obj._erp_person = None
            self._land_property_roles.remove(obj)
    # >>> land_property_roles

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpPerson.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_person.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPerson.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPerson", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_telephone_numbers:
            s += '%s<%s:ErpPerson.erp_telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:ErpPerson.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:ErpPerson.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:ErpPerson.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.appointments:
            s += '%s<%s:ErpPerson.appointments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.labor_items:
            s += '%s<%s:ErpPerson.labor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ErpPerson.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.call_backs:
            s += '%s<%s:ErpPerson.call_backs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:ErpPerson.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:ErpPerson.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crafts:
            s += '%s<%s:ErpPerson.crafts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:ErpPerson.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.skills:
            s += '%s<%s:ErpPerson.skills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.customer_data is not None:
            s += '%s<%s:ErpPerson.customer_data rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_data.uri)
        for obj in self.change_items:
            s += '%s<%s:ErpPerson.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.switching_step_roles:
            s += '%s<%s:ErpPerson.switching_step_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_personnel is not None:
            s += '%s<%s:ErpPerson.erp_personnel rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_personnel.uri)
        if self.erp_competency is not None:
            s += '%s<%s:ErpPerson.erp_competency rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_competency.uri)
        for obj in self.land_property_roles:
            s += '%s<%s:ErpPerson.land_property_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ErpPerson.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ErpPerson.prefix>%s</%s:ErpPerson.prefix>' % \
            (indent, ns_prefix, self.prefix, ns_prefix)
        s += '%s<%s:ErpPerson.government_id>%s</%s:ErpPerson.government_id>' % \
            (indent, ns_prefix, self.government_id, ns_prefix)
        s += '%s<%s:ErpPerson.last_name>%s</%s:ErpPerson.last_name>' % \
            (indent, ns_prefix, self.last_name, ns_prefix)
        s += '%s<%s:ErpPerson.category>%s</%s:ErpPerson.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:ErpPerson.first_name>%s</%s:ErpPerson.first_name>' % \
            (indent, ns_prefix, self.first_name, ns_prefix)
        s += '%s<%s:ErpPerson.suffix>%s</%s:ErpPerson.suffix>' % \
            (indent, ns_prefix, self.suffix, ns_prefix)
        s += '%s<%s:ErpPerson.special_need>%s</%s:ErpPerson.special_need>' % \
            (indent, ns_prefix, self.special_need, ns_prefix)
        s += '%s<%s:ErpPerson.m_name>%s</%s:ErpPerson.m_name>' % \
            (indent, ns_prefix, self.m_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPerson")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_person.serialize


class ErpRecDelvLineItem(IdentifiedObject):
    """ Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.
    """
    # <<< erp_rec_delv_line_item
    # @generated
    def __init__(self, status=None, erp_poline_item=None, erp_receive_delivery=None, material_items=None, erp_invoice_line_item=None, assets=None, **kw_args):
        """ Initialises a new 'ErpRecDelvLineItem' instance.
        """

        self.status = status

        self._erp_poline_item = None
        self.erp_poline_item = erp_poline_item

        self._erp_receive_delivery = None
        self.erp_receive_delivery = erp_receive_delivery

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._erp_invoice_line_item = None
        self.erp_invoice_line_item = erp_invoice_line_item

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []


        super(ErpRecDelvLineItem, self).__init__(**kw_args)
    # >>> erp_rec_delv_line_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< erp_poline_item
    # @generated
    def get_erp_poline_item(self):
        """ 
        """
        return self._erp_poline_item

    def set_erp_poline_item(self, value):
        if self._erp_poline_item is not None:
            self._erp_poline_item._erp_rec_del_line_item = None

        self._erp_poline_item = value
        if self._erp_poline_item is not None:
            self._erp_poline_item._erp_rec_del_line_item = self

    erp_poline_item = property(get_erp_poline_item, set_erp_poline_item)
    # >>> erp_poline_item

    # <<< erp_receive_delivery
    # @generated
    def get_erp_receive_delivery(self):
        """ 
        """
        return self._erp_receive_delivery

    def set_erp_receive_delivery(self, value):
        if self._erp_receive_delivery is not None:
            filtered = [x for x in self.erp_receive_delivery.erp_rec_delv_line_items if x != self]
            self._erp_receive_delivery._erp_rec_delv_line_items = filtered

        self._erp_receive_delivery = value
        if self._erp_receive_delivery is not None:
            self._erp_receive_delivery._erp_rec_delv_line_items.append(self)

    erp_receive_delivery = property(get_erp_receive_delivery, set_erp_receive_delivery)
    # >>> erp_receive_delivery

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for p in self._material_items:
            filtered = [q for q in p.erp_rec_delv_line_items if q != self]
            self._material_items._erp_rec_delv_line_items = filtered
        for r in value:
            if self not in r._erp_rec_delv_line_items:
                r._erp_rec_delv_line_items.append(self)
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            if self not in obj._erp_rec_delv_line_items:
                obj._erp_rec_delv_line_items.append(self)
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            if self in obj._erp_rec_delv_line_items:
                obj._erp_rec_delv_line_items.remove(self)
            self._material_items.remove(obj)
    # >>> material_items

    # <<< erp_invoice_line_item
    # @generated
    def get_erp_invoice_line_item(self):
        """ 
        """
        return self._erp_invoice_line_item

    def set_erp_invoice_line_item(self, value):
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_rec_delv_line_item = None

        self._erp_invoice_line_item = value
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_rec_delv_line_item = self

    erp_invoice_line_item = property(get_erp_invoice_line_item, set_erp_invoice_line_item)
    # >>> erp_invoice_line_item

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.erp_rec_delivery_items if q != self]
            self._assets._erp_rec_delivery_items = filtered
        for r in value:
            if self not in r._erp_rec_delivery_items:
                r._erp_rec_delivery_items.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._erp_rec_delivery_items:
                obj._erp_rec_delivery_items.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._erp_rec_delivery_items:
                obj._erp_rec_delivery_items.remove(self)
            self._assets.remove(obj)
    # >>> assets


    def __str__(self):
        """ Returns a string representation of the ErpRecDelvLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_rec_delv_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpRecDelvLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpRecDelvLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:ErpRecDelvLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.erp_poline_item is not None:
            s += '%s<%s:ErpRecDelvLineItem.erp_poline_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_poline_item.uri)
        if self.erp_receive_delivery is not None:
            s += '%s<%s:ErpRecDelvLineItem.erp_receive_delivery rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_receive_delivery.uri)
        for obj in self.material_items:
            s += '%s<%s:ErpRecDelvLineItem.material_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_invoice_line_item is not None:
            s += '%s<%s:ErpRecDelvLineItem.erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice_line_item.uri)
        for obj in self.assets:
            s += '%s<%s:ErpRecDelvLineItem.assets rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpRecDelvLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_rec_delv_line_item.serialize


class ErpBankAccount(BankAccount):
    """ Relationship under a particular name, usually evidenced by a deposit against which withdrawals can be made. Types of bank accounts include: demand, time, custodial, joint, trustee, corporate, special, and regular accounts. A statement of transactions during a fiscal period and the resulting balance is maintained on each account. For Payment metering, the account is associated with Bank and Supplier, reflecting details of the bank account used for depositing revenue collected by TokenVendor. The name of the account holder should be specified in 'name' attribute.
    """
    # <<< erp_bank_account
    # @generated
    def __init__(self, bank_aba='', **kw_args):
        """ Initialises a new 'ErpBankAccount' instance.
        """
        # Bank ABA. 
        self.bank_aba = bank_aba



        super(ErpBankAccount, self).__init__(**kw_args)
    # >>> erp_bank_account


    def __str__(self):
        """ Returns a string representation of the ErpBankAccount.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_bank_account.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpBankAccount.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpBankAccount", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ErpBankAccount.bank_aba>%s</%s:ErpBankAccount.bank_aba>' % \
            (indent, ns_prefix, self.bank_aba, ns_prefix)
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
        if self.service_supplier is not None:
            s += '%s<%s:BankAccount.service_supplier rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_supplier.uri)
        if self.bank is not None:
            s += '%s<%s:BankAccount.bank rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bank.uri)
        for obj in self.bank_statements:
            s += '%s<%s:BankAccount.bank_statements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BankAccount.account_number>%s</%s:BankAccount.account_number>' % \
            (indent, ns_prefix, self.account_number, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpBankAccount")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_bank_account.serialize


class ErpPurchaseOrder(Document):
    """ A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.
    """
    # <<< erp_purchase_order
    # @generated
    def __init__(self, erp_poline_items=None, **kw_args):
        """ Initialises a new 'ErpPurchaseOrder' instance.
        """

        self._erp_poline_items = []
        if erp_poline_items is not None:
            self.erp_poline_items = erp_poline_items
        else:
            self.erp_poline_items = []


        super(ErpPurchaseOrder, self).__init__(**kw_args)
    # >>> erp_purchase_order

    # <<< erp_poline_items
    # @generated
    def get_erp_poline_items(self):
        """ 
        """
        return self._erp_poline_items

    def set_erp_poline_items(self, value):
        for x in self._erp_poline_items:
            x._erp_purchase_order = None
        for y in value:
            y._erp_purchase_order = self
        self._erp_poline_items = value

    erp_poline_items = property(get_erp_poline_items, set_erp_poline_items)

    def add_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._erp_purchase_order = self
            self._erp_poline_items.append(obj)

    def remove_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._erp_purchase_order = None
            self._erp_poline_items.remove(obj)
    # >>> erp_poline_items


    def __str__(self):
        """ Returns a string representation of the ErpPurchaseOrder.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_purchase_order.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPurchaseOrder.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPurchaseOrder", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_poline_items:
            s += '%s<%s:ErpPurchaseOrder.erp_poline_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPurchaseOrder")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_purchase_order.serialize


class ErpInvoice(Document):
    """ A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.
    """
    # <<< erp_invoice
    # @generated
    def __init__(self, bill_media_kind='other', kind='sales', amount=0.0, pro_forma=False, transaction_date_time='', mailed_date='', due_date='', transfer_type='', reference_number='', customer_account=None, erp_invoice_line_items=None, **kw_args):
        """ Initialises a new 'ErpInvoice' instance.
        """
        # Kind of media by which the CustomerBillingInfo was delivered. Values are: "other", "paper", "electronic"
        self.bill_media_kind = 'other'

        # Kind of invoice (default is 'sales'). Values are: "sales", "purchase"
        self.kind = 'sales'

        # Total amount due on this invoice based on line items and applicable adjustments. 
        self.amount = amount

        # True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote. 
        self.pro_forma = pro_forma

        # Date and time when the invoice is issued. 
        self.transaction_date_time = transaction_date_time

        # Date on which the customer billing statement/invoice was printed/mailed. 
        self.mailed_date = mailed_date

        # Calculated date upon which the Invoice amount is due. 
        self.due_date = due_date

        # Type of invoice transfer. 
        self.transfer_type = transfer_type

        # Number of an invoice to be reference by this invoice. 
        self.reference_number = reference_number


        self._customer_account = None
        self.customer_account = customer_account

        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []


        super(ErpInvoice, self).__init__(**kw_args)
    # >>> erp_invoice

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ 
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.erp_invoicees if x != self]
            self._customer_account._erp_invoicees = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._erp_invoicees.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for x in self._erp_invoice_line_items:
            x._erp_invoice = None
        for y in value:
            y._erp_invoice = self
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            obj._erp_invoice = self
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            obj._erp_invoice = None
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items


    def __str__(self):
        """ Returns a string representation of the ErpInvoice.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_invoice.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpInvoice.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpInvoice", self.uri)
        if format:
            indent += ' ' * depth

        if self.customer_account is not None:
            s += '%s<%s:ErpInvoice.customer_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_account.uri)
        for obj in self.erp_invoice_line_items:
            s += '%s<%s:ErpInvoice.erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ErpInvoice.bill_media_kind>%s</%s:ErpInvoice.bill_media_kind>' % \
            (indent, ns_prefix, self.bill_media_kind, ns_prefix)
        s += '%s<%s:ErpInvoice.kind>%s</%s:ErpInvoice.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:ErpInvoice.amount>%s</%s:ErpInvoice.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:ErpInvoice.pro_forma>%s</%s:ErpInvoice.pro_forma>' % \
            (indent, ns_prefix, self.pro_forma, ns_prefix)
        s += '%s<%s:ErpInvoice.transaction_date_time>%s</%s:ErpInvoice.transaction_date_time>' % \
            (indent, ns_prefix, self.transaction_date_time, ns_prefix)
        s += '%s<%s:ErpInvoice.mailed_date>%s</%s:ErpInvoice.mailed_date>' % \
            (indent, ns_prefix, self.mailed_date, ns_prefix)
        s += '%s<%s:ErpInvoice.due_date>%s</%s:ErpInvoice.due_date>' % \
            (indent, ns_prefix, self.due_date, ns_prefix)
        s += '%s<%s:ErpInvoice.transfer_type>%s</%s:ErpInvoice.transfer_type>' % \
            (indent, ns_prefix, self.transfer_type, ns_prefix)
        s += '%s<%s:ErpInvoice.reference_number>%s</%s:ErpInvoice.reference_number>' % \
            (indent, ns_prefix, self.reference_number, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpInvoice")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_invoice.serialize


class ErpBomItemData(IdentifiedObject):
    """ An individual item on a bill of materials.
    """
    # <<< erp_bom_item_data
    # @generated
    def __init__(self, design_location=None, erp_bom=None, type_asset=None, **kw_args):
        """ Initialises a new 'ErpBomItemData' instance.
        """

        self._design_location = None
        self.design_location = design_location

        self._erp_bom = None
        self.erp_bom = erp_bom

        self._type_asset = None
        self.type_asset = type_asset


        super(ErpBomItemData, self).__init__(**kw_args)
    # >>> erp_bom_item_data

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.erp_bom_item_datas if x != self]
            self._design_location._erp_bom_item_datas = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._erp_bom_item_datas.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< erp_bom
    # @generated
    def get_erp_bom(self):
        """ 
        """
        return self._erp_bom

    def set_erp_bom(self, value):
        if self._erp_bom is not None:
            filtered = [x for x in self.erp_bom.erp_bom_item_datas if x != self]
            self._erp_bom._erp_bom_item_datas = filtered

        self._erp_bom = value
        if self._erp_bom is not None:
            self._erp_bom._erp_bom_item_datas.append(self)

    erp_bom = property(get_erp_bom, set_erp_bom)
    # >>> erp_bom

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            filtered = [x for x in self.type_asset.erp_bom_item_datas if x != self]
            self._type_asset._erp_bom_item_datas = filtered

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._erp_bom_item_datas.append(self)

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset


    def __str__(self):
        """ Returns a string representation of the ErpBomItemData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_bom_item_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpBomItemData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpBomItemData", self.uri)
        if format:
            indent += ' ' * depth

        if self.design_location is not None:
            s += '%s<%s:ErpBomItemData.design_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design_location.uri)
        if self.erp_bom is not None:
            s += '%s<%s:ErpBomItemData.erp_bom rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_bom.uri)
        if self.type_asset is not None:
            s += '%s<%s:ErpBomItemData.type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_asset.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpBomItemData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_bom_item_data.serialize


class ErpItemMaster(IdentifiedObject):
    """ Any unique purchased part for manufactured product tracked by ERP systems for a utility. Item, as used by the OAG, refers to the basic information about an item, including its attributes, cost, and locations. It does not include item quantities. Compare to the Inventory, which includes all quantities and other location-specific information.
    """
    # <<< erp_item_master
    # @generated
    def __init__(self, asset=None, status=None, **kw_args):
        """ Initialises a new 'ErpItemMaster' instance.
        """

        self._asset = None
        self.asset = asset

        self.status = status


        super(ErpItemMaster, self).__init__(**kw_args)
    # >>> erp_item_master

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            self._asset._erp_item_master = None

        self._asset = value
        if self._asset is not None:
            self._asset._erp_item_master = self

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpItemMaster.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_item_master.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpItemMaster.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpItemMaster", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:ErpItemMaster.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.status is not None:
            s += '%s<%s:ErpItemMaster.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpItemMaster")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_item_master.serialize


class ErpInventoryCount(IdentifiedObject):
    """ This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.
    """
    # <<< erp_inventory_count
    # @generated
    def __init__(self, asset_model=None, material_item=None, status=None, **kw_args):
        """ Initialises a new 'ErpInventoryCount' instance.
        """

        self._asset_model = None
        self.asset_model = asset_model

        self._material_item = None
        self.material_item = material_item

        self.status = status


        super(ErpInventoryCount, self).__init__(**kw_args)
    # >>> erp_inventory_count

    # <<< asset_model
    # @generated
    def get_asset_model(self):
        """ 
        """
        return self._asset_model

    def set_asset_model(self, value):
        if self._asset_model is not None:
            filtered = [x for x in self.asset_model.erp_inventory_counts if x != self]
            self._asset_model._erp_inventory_counts = filtered

        self._asset_model = value
        if self._asset_model is not None:
            self._asset_model._erp_inventory_counts.append(self)

    asset_model = property(get_asset_model, set_asset_model)
    # >>> asset_model

    # <<< material_item
    # @generated
    def get_material_item(self):
        """ 
        """
        return self._material_item

    def set_material_item(self, value):
        if self._material_item is not None:
            filtered = [x for x in self.material_item.erp_inventory_counts if x != self]
            self._material_item._erp_inventory_counts = filtered

        self._material_item = value
        if self._material_item is not None:
            self._material_item._erp_inventory_counts.append(self)

    material_item = property(get_material_item, set_material_item)
    # >>> material_item

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpInventoryCount.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_inventory_count.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpInventoryCount.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpInventoryCount", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset_model is not None:
            s += '%s<%s:ErpInventoryCount.asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_model.uri)
        if self.material_item is not None:
            s += '%s<%s:ErpInventoryCount.material_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.material_item.uri)
        if self.status is not None:
            s += '%s<%s:ErpInventoryCount.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpInventoryCount")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_inventory_count.serialize


class ErpEngChangeOrder(Document):
    """ General Utility Engineering Change Order information.
    """
    pass
    # <<< erp_eng_change_order
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ErpEngChangeOrder' instance.
        """


        super(ErpEngChangeOrder, self).__init__(**kw_args)
    # >>> erp_eng_change_order


    def __str__(self):
        """ Returns a string representation of the ErpEngChangeOrder.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_eng_change_order.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpEngChangeOrder.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpEngChangeOrder", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpEngChangeOrder")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_eng_change_order.serialize


class ErpInvoiceLineItem(Document):
    """ An individual line item on an invoice.
    """
    # <<< erp_invoice_line_item
    # @generated
    def __init__(self, kind='recalculation', line_number='', net_amount=0.0, gl_account='', gl_date_time='', line_amount=0.0, previous_amount=0.0, line_version='', work_billing_infos=None, erp_rec_line_item=None, market_factors=None, erp_journal_entries=None, bill_period=None, erp_rec_delv_line_item=None, customer_billing_infos=None, user_attributes=None, container_erp_invoice_line_item=None, component_erp_invoice_line_items=None, erp_payments=None, settlements=None, erp_invoice=None, erp_quote_line_item=None, erp_payable_line_item=None, **kw_args):
        """ Initialises a new 'ErpInvoiceLineItem' instance.
        """
        # Kind of line item. Values are: "recalculation", "initial", "other"
        self.kind = 'recalculation'

        # Line item number on invoice statement. 
        self.line_number = line_number

        # Net line item charge amount. 
        self.net_amount = net_amount

        # General Ledger account code, must be a valid combination. 
        self.gl_account = gl_account

        # Date and time line item will be posted to the General Ledger. 
        self.gl_date_time = gl_date_time

        # Amount due for this line item. 
        self.line_amount = line_amount

        # Previous line item charge amount. 
        self.previous_amount = previous_amount

        # Version number of the bill run. 
        self.line_version = line_version


        self._work_billing_infos = []
        if work_billing_infos is not None:
            self.work_billing_infos = work_billing_infos
        else:
            self.work_billing_infos = []

        self._erp_rec_line_item = None
        self.erp_rec_line_item = erp_rec_line_item

        self._market_factors = []
        if market_factors is not None:
            self.market_factors = market_factors
        else:
            self.market_factors = []

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []

        self.bill_period = bill_period

        self._erp_rec_delv_line_item = None
        self.erp_rec_delv_line_item = erp_rec_delv_line_item

        self._customer_billing_infos = []
        if customer_billing_infos is not None:
            self.customer_billing_infos = customer_billing_infos
        else:
            self.customer_billing_infos = []

        self._user_attributes = []
        if user_attributes is not None:
            self.user_attributes = user_attributes
        else:
            self.user_attributes = []

        self._container_erp_invoice_line_item = None
        self.container_erp_invoice_line_item = container_erp_invoice_line_item

        self._component_erp_invoice_line_items = []
        if component_erp_invoice_line_items is not None:
            self.component_erp_invoice_line_items = component_erp_invoice_line_items
        else:
            self.component_erp_invoice_line_items = []

        self._erp_payments = []
        if erp_payments is not None:
            self.erp_payments = erp_payments
        else:
            self.erp_payments = []

        self._settlements = []
        if settlements is not None:
            self.settlements = settlements
        else:
            self.settlements = []

        self._erp_invoice = None
        self.erp_invoice = erp_invoice

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._erp_payable_line_item = None
        self.erp_payable_line_item = erp_payable_line_item


        super(ErpInvoiceLineItem, self).__init__(**kw_args)
    # >>> erp_invoice_line_item

    # <<< work_billing_infos
    # @generated
    def get_work_billing_infos(self):
        """ 
        """
        return self._work_billing_infos

    def set_work_billing_infos(self, value):
        for p in self._work_billing_infos:
            filtered = [q for q in p.erp_line_items if q != self]
            self._work_billing_infos._erp_line_items = filtered
        for r in value:
            if self not in r._erp_line_items:
                r._erp_line_items.append(self)
        self._work_billing_infos = value

    work_billing_infos = property(get_work_billing_infos, set_work_billing_infos)

    def add_work_billing_infos(self, *work_billing_infos):
        for obj in work_billing_infos:
            if self not in obj._erp_line_items:
                obj._erp_line_items.append(self)
            self._work_billing_infos.append(obj)

    def remove_work_billing_infos(self, *work_billing_infos):
        for obj in work_billing_infos:
            if self in obj._erp_line_items:
                obj._erp_line_items.remove(self)
            self._work_billing_infos.remove(obj)
    # >>> work_billing_infos

    # <<< erp_rec_line_item
    # @generated
    def get_erp_rec_line_item(self):
        """ 
        """
        return self._erp_rec_line_item

    def set_erp_rec_line_item(self, value):
        if self._erp_rec_line_item is not None:
            self._erp_rec_line_item._erp_invoice_line_item = None

        self._erp_rec_line_item = value
        if self._erp_rec_line_item is not None:
            self._erp_rec_line_item._erp_invoice_line_item = self

    erp_rec_line_item = property(get_erp_rec_line_item, set_erp_rec_line_item)
    # >>> erp_rec_line_item

    # <<< market_factors
    # @generated
    def get_market_factors(self):
        """ 
        """
        return self._market_factors

    def set_market_factors(self, value):
        for p in self._market_factors:
            filtered = [q for q in p.erp_invoices if q != self]
            self._market_factors._erp_invoices = filtered
        for r in value:
            if self not in r._erp_invoices:
                r._erp_invoices.append(self)
        self._market_factors = value

    market_factors = property(get_market_factors, set_market_factors)

    def add_market_factors(self, *market_factors):
        for obj in market_factors:
            if self not in obj._erp_invoices:
                obj._erp_invoices.append(self)
            self._market_factors.append(obj)

    def remove_market_factors(self, *market_factors):
        for obj in market_factors:
            if self in obj._erp_invoices:
                obj._erp_invoices.remove(self)
            self._market_factors.remove(obj)
    # >>> market_factors

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for x in self._erp_journal_entries:
            x._erp_invoice_line_item = None
        for y in value:
            y._erp_invoice_line_item = self
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            obj._erp_invoice_line_item = self
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            obj._erp_invoice_line_item = None
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries

    # <<< bill_period
    # @generated
    # Bill period for the line item.
    bill_period = None
    # >>> bill_period

    # <<< erp_rec_delv_line_item
    # @generated
    def get_erp_rec_delv_line_item(self):
        """ 
        """
        return self._erp_rec_delv_line_item

    def set_erp_rec_delv_line_item(self, value):
        if self._erp_rec_delv_line_item is not None:
            self._erp_rec_delv_line_item._erp_invoice_line_item = None

        self._erp_rec_delv_line_item = value
        if self._erp_rec_delv_line_item is not None:
            self._erp_rec_delv_line_item._erp_invoice_line_item = self

    erp_rec_delv_line_item = property(get_erp_rec_delv_line_item, set_erp_rec_delv_line_item)
    # >>> erp_rec_delv_line_item

    # <<< customer_billing_infos
    # @generated
    def get_customer_billing_infos(self):
        """ Customer billing for services rendered.
        """
        return self._customer_billing_infos

    def set_customer_billing_infos(self, value):
        for p in self._customer_billing_infos:
            filtered = [q for q in p.erp_invoice_line_items if q != self]
            self._customer_billing_infos._erp_invoice_line_items = filtered
        for r in value:
            if self not in r._erp_invoice_line_items:
                r._erp_invoice_line_items.append(self)
        self._customer_billing_infos = value

    customer_billing_infos = property(get_customer_billing_infos, set_customer_billing_infos)

    def add_customer_billing_infos(self, *customer_billing_infos):
        for obj in customer_billing_infos:
            if self not in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.append(self)
            self._customer_billing_infos.append(obj)

    def remove_customer_billing_infos(self, *customer_billing_infos):
        for obj in customer_billing_infos:
            if self in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.remove(self)
            self._customer_billing_infos.remove(obj)
    # >>> customer_billing_infos

    # <<< user_attributes
    # @generated
    def get_user_attributes(self):
        """ 
        """
        return self._user_attributes

    def set_user_attributes(self, value):
        for p in self._user_attributes:
            filtered = [q for q in p.erp_invoice_line_items if q != self]
            self._user_attributes._erp_invoice_line_items = filtered
        for r in value:
            if self not in r._erp_invoice_line_items:
                r._erp_invoice_line_items.append(self)
        self._user_attributes = value

    user_attributes = property(get_user_attributes, set_user_attributes)

    def add_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self not in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.append(self)
            self._user_attributes.append(obj)

    def remove_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.remove(self)
            self._user_attributes.remove(obj)
    # >>> user_attributes

    # <<< container_erp_invoice_line_item
    # @generated
    def get_container_erp_invoice_line_item(self):
        """ 
        """
        return self._container_erp_invoice_line_item

    def set_container_erp_invoice_line_item(self, value):
        if self._container_erp_invoice_line_item is not None:
            filtered = [x for x in self.container_erp_invoice_line_item.component_erp_invoice_line_items if x != self]
            self._container_erp_invoice_line_item._component_erp_invoice_line_items = filtered

        self._container_erp_invoice_line_item = value
        if self._container_erp_invoice_line_item is not None:
            self._container_erp_invoice_line_item._component_erp_invoice_line_items.append(self)

    container_erp_invoice_line_item = property(get_container_erp_invoice_line_item, set_container_erp_invoice_line_item)
    # >>> container_erp_invoice_line_item

    # <<< component_erp_invoice_line_items
    # @generated
    def get_component_erp_invoice_line_items(self):
        """ 
        """
        return self._component_erp_invoice_line_items

    def set_component_erp_invoice_line_items(self, value):
        for x in self._component_erp_invoice_line_items:
            x._container_erp_invoice_line_item = None
        for y in value:
            y._container_erp_invoice_line_item = self
        self._component_erp_invoice_line_items = value

    component_erp_invoice_line_items = property(get_component_erp_invoice_line_items, set_component_erp_invoice_line_items)

    def add_component_erp_invoice_line_items(self, *component_erp_invoice_line_items):
        for obj in component_erp_invoice_line_items:
            obj._container_erp_invoice_line_item = self
            self._component_erp_invoice_line_items.append(obj)

    def remove_component_erp_invoice_line_items(self, *component_erp_invoice_line_items):
        for obj in component_erp_invoice_line_items:
            obj._container_erp_invoice_line_item = None
            self._component_erp_invoice_line_items.remove(obj)
    # >>> component_erp_invoice_line_items

    # <<< erp_payments
    # @generated
    def get_erp_payments(self):
        """ 
        """
        return self._erp_payments

    def set_erp_payments(self, value):
        for p in self._erp_payments:
            filtered = [q for q in p.erp_invoice_line_items if q != self]
            self._erp_payments._erp_invoice_line_items = filtered
        for r in value:
            if self not in r._erp_invoice_line_items:
                r._erp_invoice_line_items.append(self)
        self._erp_payments = value

    erp_payments = property(get_erp_payments, set_erp_payments)

    def add_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self not in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.append(self)
            self._erp_payments.append(obj)

    def remove_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.remove(self)
            self._erp_payments.remove(obj)
    # >>> erp_payments

    # <<< settlements
    # @generated
    def get_settlements(self):
        """ 
        """
        return self._settlements

    def set_settlements(self, value):
        for p in self._settlements:
            filtered = [q for q in p.erp_invoice_line_items if q != self]
            self._settlements._erp_invoice_line_items = filtered
        for r in value:
            if self not in r._erp_invoice_line_items:
                r._erp_invoice_line_items.append(self)
        self._settlements = value

    settlements = property(get_settlements, set_settlements)

    def add_settlements(self, *settlements):
        for obj in settlements:
            if self not in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.append(self)
            self._settlements.append(obj)

    def remove_settlements(self, *settlements):
        for obj in settlements:
            if self in obj._erp_invoice_line_items:
                obj._erp_invoice_line_items.remove(self)
            self._settlements.remove(obj)
    # >>> settlements

    # <<< erp_invoice
    # @generated
    def get_erp_invoice(self):
        """ 
        """
        return self._erp_invoice

    def set_erp_invoice(self, value):
        if self._erp_invoice is not None:
            filtered = [x for x in self.erp_invoice.erp_invoice_line_items if x != self]
            self._erp_invoice._erp_invoice_line_items = filtered

        self._erp_invoice = value
        if self._erp_invoice is not None:
            self._erp_invoice._erp_invoice_line_items.append(self)

    erp_invoice = property(get_erp_invoice, set_erp_invoice)
    # >>> erp_invoice

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._erp_invoice_line_item = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._erp_invoice_line_item = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< erp_payable_line_item
    # @generated
    def get_erp_payable_line_item(self):
        """ 
        """
        return self._erp_payable_line_item

    def set_erp_payable_line_item(self, value):
        if self._erp_payable_line_item is not None:
            self._erp_payable_line_item._erp_invoice_line_item = None

        self._erp_payable_line_item = value
        if self._erp_payable_line_item is not None:
            self._erp_payable_line_item._erp_invoice_line_item = self

    erp_payable_line_item = property(get_erp_payable_line_item, set_erp_payable_line_item)
    # >>> erp_payable_line_item


    def __str__(self):
        """ Returns a string representation of the ErpInvoiceLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_invoice_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpInvoiceLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpInvoiceLineItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_billing_infos:
            s += '%s<%s:ErpInvoiceLineItem.work_billing_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_rec_line_item is not None:
            s += '%s<%s:ErpInvoiceLineItem.erp_rec_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_rec_line_item.uri)
        for obj in self.market_factors:
            s += '%s<%s:ErpInvoiceLineItem.market_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_journal_entries:
            s += '%s<%s:ErpInvoiceLineItem.erp_journal_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bill_period is not None:
            s += '%s<%s:ErpInvoiceLineItem.bill_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bill_period.uri)
        if self.erp_rec_delv_line_item is not None:
            s += '%s<%s:ErpInvoiceLineItem.erp_rec_delv_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_rec_delv_line_item.uri)
        for obj in self.customer_billing_infos:
            s += '%s<%s:ErpInvoiceLineItem.customer_billing_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.user_attributes:
            s += '%s<%s:ErpInvoiceLineItem.user_attributes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.container_erp_invoice_line_item is not None:
            s += '%s<%s:ErpInvoiceLineItem.container_erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.container_erp_invoice_line_item.uri)
        for obj in self.component_erp_invoice_line_items:
            s += '%s<%s:ErpInvoiceLineItem.component_erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_payments:
            s += '%s<%s:ErpInvoiceLineItem.erp_payments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.settlements:
            s += '%s<%s:ErpInvoiceLineItem.settlements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_invoice is not None:
            s += '%s<%s:ErpInvoiceLineItem.erp_invoice rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice.uri)
        if self.erp_quote_line_item is not None:
            s += '%s<%s:ErpInvoiceLineItem.erp_quote_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_quote_line_item.uri)
        if self.erp_payable_line_item is not None:
            s += '%s<%s:ErpInvoiceLineItem.erp_payable_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_payable_line_item.uri)
        s += '%s<%s:ErpInvoiceLineItem.kind>%s</%s:ErpInvoiceLineItem.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.line_number>%s</%s:ErpInvoiceLineItem.line_number>' % \
            (indent, ns_prefix, self.line_number, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.net_amount>%s</%s:ErpInvoiceLineItem.net_amount>' % \
            (indent, ns_prefix, self.net_amount, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.gl_account>%s</%s:ErpInvoiceLineItem.gl_account>' % \
            (indent, ns_prefix, self.gl_account, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.gl_date_time>%s</%s:ErpInvoiceLineItem.gl_date_time>' % \
            (indent, ns_prefix, self.gl_date_time, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.line_amount>%s</%s:ErpInvoiceLineItem.line_amount>' % \
            (indent, ns_prefix, self.line_amount, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.previous_amount>%s</%s:ErpInvoiceLineItem.previous_amount>' % \
            (indent, ns_prefix, self.previous_amount, ns_prefix)
        s += '%s<%s:ErpInvoiceLineItem.line_version>%s</%s:ErpInvoiceLineItem.line_version>' % \
            (indent, ns_prefix, self.line_version, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpInvoiceLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_invoice_line_item.serialize


class ErpPayable(Document):
    """ A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.
    """
    # <<< erp_payable
    # @generated
    def __init__(self, contractor_items=None, erp_payable_line_items=None, **kw_args):
        """ Initialises a new 'ErpPayable' instance.
        """

        self._contractor_items = []
        if contractor_items is not None:
            self.contractor_items = contractor_items
        else:
            self.contractor_items = []

        self._erp_payable_line_items = []
        if erp_payable_line_items is not None:
            self.erp_payable_line_items = erp_payable_line_items
        else:
            self.erp_payable_line_items = []


        super(ErpPayable, self).__init__(**kw_args)
    # >>> erp_payable

    # <<< contractor_items
    # @generated
    def get_contractor_items(self):
        """ 
        """
        return self._contractor_items

    def set_contractor_items(self, value):
        for p in self._contractor_items:
            filtered = [q for q in p.erp_payables if q != self]
            self._contractor_items._erp_payables = filtered
        for r in value:
            if self not in r._erp_payables:
                r._erp_payables.append(self)
        self._contractor_items = value

    contractor_items = property(get_contractor_items, set_contractor_items)

    def add_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            if self not in obj._erp_payables:
                obj._erp_payables.append(self)
            self._contractor_items.append(obj)

    def remove_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            if self in obj._erp_payables:
                obj._erp_payables.remove(self)
            self._contractor_items.remove(obj)
    # >>> contractor_items

    # <<< erp_payable_line_items
    # @generated
    def get_erp_payable_line_items(self):
        """ 
        """
        return self._erp_payable_line_items

    def set_erp_payable_line_items(self, value):
        for x in self._erp_payable_line_items:
            x._erp_payable = None
        for y in value:
            y._erp_payable = self
        self._erp_payable_line_items = value

    erp_payable_line_items = property(get_erp_payable_line_items, set_erp_payable_line_items)

    def add_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            obj._erp_payable = self
            self._erp_payable_line_items.append(obj)

    def remove_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            obj._erp_payable = None
            self._erp_payable_line_items.remove(obj)
    # >>> erp_payable_line_items


    def __str__(self):
        """ Returns a string representation of the ErpPayable.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_payable.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPayable.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPayable", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contractor_items:
            s += '%s<%s:ErpPayable.contractor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_payable_line_items:
            s += '%s<%s:ErpPayable.erp_payable_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPayable")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_payable.serialize


class ErpPayment(Document):
    """ Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.
    """
    # <<< erp_payment
    # @generated
    def __init__(self, terms_payment='', erp_rec_line_items=None, erp_invoice_line_items=None, erp_payable_line_items=None, **kw_args):
        """ Initialises a new 'ErpPayment' instance.
        """
        # Payment terms (e.g., net 30). 
        self.terms_payment = terms_payment


        self._erp_rec_line_items = []
        if erp_rec_line_items is not None:
            self.erp_rec_line_items = erp_rec_line_items
        else:
            self.erp_rec_line_items = []

        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []

        self._erp_payable_line_items = []
        if erp_payable_line_items is not None:
            self.erp_payable_line_items = erp_payable_line_items
        else:
            self.erp_payable_line_items = []


        super(ErpPayment, self).__init__(**kw_args)
    # >>> erp_payment

    # <<< erp_rec_line_items
    # @generated
    def get_erp_rec_line_items(self):
        """ 
        """
        return self._erp_rec_line_items

    def set_erp_rec_line_items(self, value):
        for p in self._erp_rec_line_items:
            filtered = [q for q in p.erp_payments if q != self]
            self._erp_rec_line_items._erp_payments = filtered
        for r in value:
            if self not in r._erp_payments:
                r._erp_payments.append(self)
        self._erp_rec_line_items = value

    erp_rec_line_items = property(get_erp_rec_line_items, set_erp_rec_line_items)

    def add_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            if self not in obj._erp_payments:
                obj._erp_payments.append(self)
            self._erp_rec_line_items.append(obj)

    def remove_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            if self in obj._erp_payments:
                obj._erp_payments.remove(self)
            self._erp_rec_line_items.remove(obj)
    # >>> erp_rec_line_items

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for p in self._erp_invoice_line_items:
            filtered = [q for q in p.erp_payments if q != self]
            self._erp_invoice_line_items._erp_payments = filtered
        for r in value:
            if self not in r._erp_payments:
                r._erp_payments.append(self)
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self not in obj._erp_payments:
                obj._erp_payments.append(self)
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self in obj._erp_payments:
                obj._erp_payments.remove(self)
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items

    # <<< erp_payable_line_items
    # @generated
    def get_erp_payable_line_items(self):
        """ 
        """
        return self._erp_payable_line_items

    def set_erp_payable_line_items(self, value):
        for p in self._erp_payable_line_items:
            filtered = [q for q in p.erp_payments if q != self]
            self._erp_payable_line_items._erp_payments = filtered
        for r in value:
            if self not in r._erp_payments:
                r._erp_payments.append(self)
        self._erp_payable_line_items = value

    erp_payable_line_items = property(get_erp_payable_line_items, set_erp_payable_line_items)

    def add_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            if self not in obj._erp_payments:
                obj._erp_payments.append(self)
            self._erp_payable_line_items.append(obj)

    def remove_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            if self in obj._erp_payments:
                obj._erp_payments.remove(self)
            self._erp_payable_line_items.remove(obj)
    # >>> erp_payable_line_items


    def __str__(self):
        """ Returns a string representation of the ErpPayment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_payment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPayment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPayment", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_rec_line_items:
            s += '%s<%s:ErpPayment.erp_rec_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_invoice_line_items:
            s += '%s<%s:ErpPayment.erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_payable_line_items:
            s += '%s<%s:ErpPayment.erp_payable_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ErpPayment.terms_payment>%s</%s:ErpPayment.terms_payment>' % \
            (indent, ns_prefix, self.terms_payment, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPayment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_payment.serialize


class ErpQuote(Document):
    """ Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.
    """
    # <<< erp_quote
    # @generated
    def __init__(self, erp_quote_line_items=None, **kw_args):
        """ Initialises a new 'ErpQuote' instance.
        """

        self._erp_quote_line_items = []
        if erp_quote_line_items is not None:
            self.erp_quote_line_items = erp_quote_line_items
        else:
            self.erp_quote_line_items = []


        super(ErpQuote, self).__init__(**kw_args)
    # >>> erp_quote

    # <<< erp_quote_line_items
    # @generated
    def get_erp_quote_line_items(self):
        """ 
        """
        return self._erp_quote_line_items

    def set_erp_quote_line_items(self, value):
        for x in self._erp_quote_line_items:
            x._erp_quote = None
        for y in value:
            y._erp_quote = self
        self._erp_quote_line_items = value

    erp_quote_line_items = property(get_erp_quote_line_items, set_erp_quote_line_items)

    def add_erp_quote_line_items(self, *erp_quote_line_items):
        for obj in erp_quote_line_items:
            obj._erp_quote = self
            self._erp_quote_line_items.append(obj)

    def remove_erp_quote_line_items(self, *erp_quote_line_items):
        for obj in erp_quote_line_items:
            obj._erp_quote = None
            self._erp_quote_line_items.remove(obj)
    # >>> erp_quote_line_items


    def __str__(self):
        """ Returns a string representation of the ErpQuote.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_quote.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpQuote.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpQuote", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_quote_line_items:
            s += '%s<%s:ErpQuote.erp_quote_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpQuote")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_quote.serialize


class ErpJournalEntry(IdentifiedObject):
    """ Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.
    """
    # <<< erp_journal_entry
    # @generated
    def __init__(self, transaction_date_time='', account_id='', posting_date_time='', amount=0.0, source_id='', erp_payable_line_items=None, erp_invoice_line_item=None, status=None, erp_journal=None, cost_types=None, erp_ledger_entry=None, erp_rec_line_items=None, **kw_args):
        """ Initialises a new 'ErpJournalEntry' instance.
        """
        # Date and time journal entry was recorded. 
        self.transaction_date_time = transaction_date_time

        # Account identifier for this entry. 
        self.account_id = account_id

        # Date and time this entry is to be posted to the ledger. 
        self.posting_date_time = posting_date_time

        # The amount of the debit or credit for this account. 
        self.amount = amount

        # The identifer of the source for this entry. 
        self.source_id = source_id


        self._erp_payable_line_items = []
        if erp_payable_line_items is not None:
            self.erp_payable_line_items = erp_payable_line_items
        else:
            self.erp_payable_line_items = []

        self._erp_invoice_line_item = None
        self.erp_invoice_line_item = erp_invoice_line_item

        self.status = status

        self._erp_journal = None
        self.erp_journal = erp_journal

        self._cost_types = []
        if cost_types is not None:
            self.cost_types = cost_types
        else:
            self.cost_types = []

        self._erp_ledger_entry = None
        self.erp_ledger_entry = erp_ledger_entry

        self._erp_rec_line_items = []
        if erp_rec_line_items is not None:
            self.erp_rec_line_items = erp_rec_line_items
        else:
            self.erp_rec_line_items = []


        super(ErpJournalEntry, self).__init__(**kw_args)
    # >>> erp_journal_entry

    # <<< erp_payable_line_items
    # @generated
    def get_erp_payable_line_items(self):
        """ 
        """
        return self._erp_payable_line_items

    def set_erp_payable_line_items(self, value):
        for p in self._erp_payable_line_items:
            filtered = [q for q in p.erp_journal_entries if q != self]
            self._erp_payable_line_items._erp_journal_entries = filtered
        for r in value:
            if self not in r._erp_journal_entries:
                r._erp_journal_entries.append(self)
        self._erp_payable_line_items = value

    erp_payable_line_items = property(get_erp_payable_line_items, set_erp_payable_line_items)

    def add_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            if self not in obj._erp_journal_entries:
                obj._erp_journal_entries.append(self)
            self._erp_payable_line_items.append(obj)

    def remove_erp_payable_line_items(self, *erp_payable_line_items):
        for obj in erp_payable_line_items:
            if self in obj._erp_journal_entries:
                obj._erp_journal_entries.remove(self)
            self._erp_payable_line_items.remove(obj)
    # >>> erp_payable_line_items

    # <<< erp_invoice_line_item
    # @generated
    def get_erp_invoice_line_item(self):
        """ 
        """
        return self._erp_invoice_line_item

    def set_erp_invoice_line_item(self, value):
        if self._erp_invoice_line_item is not None:
            filtered = [x for x in self.erp_invoice_line_item.erp_journal_entries if x != self]
            self._erp_invoice_line_item._erp_journal_entries = filtered

        self._erp_invoice_line_item = value
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_journal_entries.append(self)

    erp_invoice_line_item = property(get_erp_invoice_line_item, set_erp_invoice_line_item)
    # >>> erp_invoice_line_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< erp_journal
    # @generated
    def get_erp_journal(self):
        """ 
        """
        return self._erp_journal

    def set_erp_journal(self, value):
        if self._erp_journal is not None:
            filtered = [x for x in self.erp_journal.erp_journal_entries if x != self]
            self._erp_journal._erp_journal_entries = filtered

        self._erp_journal = value
        if self._erp_journal is not None:
            self._erp_journal._erp_journal_entries.append(self)

    erp_journal = property(get_erp_journal, set_erp_journal)
    # >>> erp_journal

    # <<< cost_types
    # @generated
    def get_cost_types(self):
        """ 
        """
        return self._cost_types

    def set_cost_types(self, value):
        for p in self._cost_types:
            filtered = [q for q in p.erp_journal_entries if q != self]
            self._cost_types._erp_journal_entries = filtered
        for r in value:
            if self not in r._erp_journal_entries:
                r._erp_journal_entries.append(self)
        self._cost_types = value

    cost_types = property(get_cost_types, set_cost_types)

    def add_cost_types(self, *cost_types):
        for obj in cost_types:
            if self not in obj._erp_journal_entries:
                obj._erp_journal_entries.append(self)
            self._cost_types.append(obj)

    def remove_cost_types(self, *cost_types):
        for obj in cost_types:
            if self in obj._erp_journal_entries:
                obj._erp_journal_entries.remove(self)
            self._cost_types.remove(obj)
    # >>> cost_types

    # <<< erp_ledger_entry
    # @generated
    def get_erp_ledger_entry(self):
        """ 
        """
        return self._erp_ledger_entry

    def set_erp_ledger_entry(self, value):
        if self._erp_ledger_entry is not None:
            self._erp_ledger_entry._erp_jounal_entry = None

        self._erp_ledger_entry = value
        if self._erp_ledger_entry is not None:
            self._erp_ledger_entry._erp_jounal_entry = self

    erp_ledger_entry = property(get_erp_ledger_entry, set_erp_ledger_entry)
    # >>> erp_ledger_entry

    # <<< erp_rec_line_items
    # @generated
    def get_erp_rec_line_items(self):
        """ 
        """
        return self._erp_rec_line_items

    def set_erp_rec_line_items(self, value):
        for p in self._erp_rec_line_items:
            filtered = [q for q in p.erp_journal_entries if q != self]
            self._erp_rec_line_items._erp_journal_entries = filtered
        for r in value:
            if self not in r._erp_journal_entries:
                r._erp_journal_entries.append(self)
        self._erp_rec_line_items = value

    erp_rec_line_items = property(get_erp_rec_line_items, set_erp_rec_line_items)

    def add_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            if self not in obj._erp_journal_entries:
                obj._erp_journal_entries.append(self)
            self._erp_rec_line_items.append(obj)

    def remove_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            if self in obj._erp_journal_entries:
                obj._erp_journal_entries.remove(self)
            self._erp_rec_line_items.remove(obj)
    # >>> erp_rec_line_items


    def __str__(self):
        """ Returns a string representation of the ErpJournalEntry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_journal_entry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpJournalEntry.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpJournalEntry", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_payable_line_items:
            s += '%s<%s:ErpJournalEntry.erp_payable_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_invoice_line_item is not None:
            s += '%s<%s:ErpJournalEntry.erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice_line_item.uri)
        if self.status is not None:
            s += '%s<%s:ErpJournalEntry.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.erp_journal is not None:
            s += '%s<%s:ErpJournalEntry.erp_journal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_journal.uri)
        for obj in self.cost_types:
            s += '%s<%s:ErpJournalEntry.cost_types rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_ledger_entry is not None:
            s += '%s<%s:ErpJournalEntry.erp_ledger_entry rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_ledger_entry.uri)
        for obj in self.erp_rec_line_items:
            s += '%s<%s:ErpJournalEntry.erp_rec_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ErpJournalEntry.transaction_date_time>%s</%s:ErpJournalEntry.transaction_date_time>' % \
            (indent, ns_prefix, self.transaction_date_time, ns_prefix)
        s += '%s<%s:ErpJournalEntry.account_id>%s</%s:ErpJournalEntry.account_id>' % \
            (indent, ns_prefix, self.account_id, ns_prefix)
        s += '%s<%s:ErpJournalEntry.posting_date_time>%s</%s:ErpJournalEntry.posting_date_time>' % \
            (indent, ns_prefix, self.posting_date_time, ns_prefix)
        s += '%s<%s:ErpJournalEntry.amount>%s</%s:ErpJournalEntry.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:ErpJournalEntry.source_id>%s</%s:ErpJournalEntry.source_id>' % \
            (indent, ns_prefix, self.source_id, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpJournalEntry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_journal_entry.serialize


class ErpPOLineItem(Document):
    """ Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.
    """
    # <<< erp_poline_item
    # @generated
    def __init__(self, erp_req_line_item=None, erp_rec_del_line_item=None, asset_model_catalogue_item=None, erp_purchase_order=None, material_item=None, **kw_args):
        """ Initialises a new 'ErpPOLineItem' instance.
        """

        self._erp_req_line_item = None
        self.erp_req_line_item = erp_req_line_item

        self._erp_rec_del_line_item = None
        self.erp_rec_del_line_item = erp_rec_del_line_item

        self._asset_model_catalogue_item = None
        self.asset_model_catalogue_item = asset_model_catalogue_item

        self._erp_purchase_order = None
        self.erp_purchase_order = erp_purchase_order

        self._material_item = None
        self.material_item = material_item


        super(ErpPOLineItem, self).__init__(**kw_args)
    # >>> erp_poline_item

    # <<< erp_req_line_item
    # @generated
    def get_erp_req_line_item(self):
        """ 
        """
        return self._erp_req_line_item

    def set_erp_req_line_item(self, value):
        if self._erp_req_line_item is not None:
            self._erp_req_line_item._erp_poline_item = None

        self._erp_req_line_item = value
        if self._erp_req_line_item is not None:
            self._erp_req_line_item._erp_poline_item = self

    erp_req_line_item = property(get_erp_req_line_item, set_erp_req_line_item)
    # >>> erp_req_line_item

    # <<< erp_rec_del_line_item
    # @generated
    def get_erp_rec_del_line_item(self):
        """ 
        """
        return self._erp_rec_del_line_item

    def set_erp_rec_del_line_item(self, value):
        if self._erp_rec_del_line_item is not None:
            self._erp_rec_del_line_item._erp_poline_item = None

        self._erp_rec_del_line_item = value
        if self._erp_rec_del_line_item is not None:
            self._erp_rec_del_line_item._erp_poline_item = self

    erp_rec_del_line_item = property(get_erp_rec_del_line_item, set_erp_rec_del_line_item)
    # >>> erp_rec_del_line_item

    # <<< asset_model_catalogue_item
    # @generated
    def get_asset_model_catalogue_item(self):
        """ 
        """
        return self._asset_model_catalogue_item

    def set_asset_model_catalogue_item(self, value):
        if self._asset_model_catalogue_item is not None:
            filtered = [x for x in self.asset_model_catalogue_item.erp_poline_items if x != self]
            self._asset_model_catalogue_item._erp_poline_items = filtered

        self._asset_model_catalogue_item = value
        if self._asset_model_catalogue_item is not None:
            self._asset_model_catalogue_item._erp_poline_items.append(self)

    asset_model_catalogue_item = property(get_asset_model_catalogue_item, set_asset_model_catalogue_item)
    # >>> asset_model_catalogue_item

    # <<< erp_purchase_order
    # @generated
    def get_erp_purchase_order(self):
        """ 
        """
        return self._erp_purchase_order

    def set_erp_purchase_order(self, value):
        if self._erp_purchase_order is not None:
            filtered = [x for x in self.erp_purchase_order.erp_poline_items if x != self]
            self._erp_purchase_order._erp_poline_items = filtered

        self._erp_purchase_order = value
        if self._erp_purchase_order is not None:
            self._erp_purchase_order._erp_poline_items.append(self)

    erp_purchase_order = property(get_erp_purchase_order, set_erp_purchase_order)
    # >>> erp_purchase_order

    # <<< material_item
    # @generated
    def get_material_item(self):
        """ 
        """
        return self._material_item

    def set_material_item(self, value):
        if self._material_item is not None:
            filtered = [x for x in self.material_item.erp_poline_items if x != self]
            self._material_item._erp_poline_items = filtered

        self._material_item = value
        if self._material_item is not None:
            self._material_item._erp_poline_items.append(self)

    material_item = property(get_material_item, set_material_item)
    # >>> material_item


    def __str__(self):
        """ Returns a string representation of the ErpPOLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_poline_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPOLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPOLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_req_line_item is not None:
            s += '%s<%s:ErpPOLineItem.erp_req_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_req_line_item.uri)
        if self.erp_rec_del_line_item is not None:
            s += '%s<%s:ErpPOLineItem.erp_rec_del_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_rec_del_line_item.uri)
        if self.asset_model_catalogue_item is not None:
            s += '%s<%s:ErpPOLineItem.asset_model_catalogue_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_model_catalogue_item.uri)
        if self.erp_purchase_order is not None:
            s += '%s<%s:ErpPOLineItem.erp_purchase_order rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_purchase_order.uri)
        if self.material_item is not None:
            s += '%s<%s:ErpPOLineItem.material_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.material_item.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPOLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_poline_item.serialize


class ErpReceiveDelivery(Document):
    """ Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.
    """
    # <<< erp_receive_delivery
    # @generated
    def __init__(self, erp_rec_delv_line_items=None, **kw_args):
        """ Initialises a new 'ErpReceiveDelivery' instance.
        """

        self._erp_rec_delv_line_items = []
        if erp_rec_delv_line_items is not None:
            self.erp_rec_delv_line_items = erp_rec_delv_line_items
        else:
            self.erp_rec_delv_line_items = []


        super(ErpReceiveDelivery, self).__init__(**kw_args)
    # >>> erp_receive_delivery

    # <<< erp_rec_delv_line_items
    # @generated
    def get_erp_rec_delv_line_items(self):
        """ 
        """
        return self._erp_rec_delv_line_items

    def set_erp_rec_delv_line_items(self, value):
        for x in self._erp_rec_delv_line_items:
            x._erp_receive_delivery = None
        for y in value:
            y._erp_receive_delivery = self
        self._erp_rec_delv_line_items = value

    erp_rec_delv_line_items = property(get_erp_rec_delv_line_items, set_erp_rec_delv_line_items)

    def add_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            obj._erp_receive_delivery = self
            self._erp_rec_delv_line_items.append(obj)

    def remove_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            obj._erp_receive_delivery = None
            self._erp_rec_delv_line_items.remove(obj)
    # >>> erp_rec_delv_line_items


    def __str__(self):
        """ Returns a string representation of the ErpReceiveDelivery.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_receive_delivery.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpReceiveDelivery.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpReceiveDelivery", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_rec_delv_line_items:
            s += '%s<%s:ErpReceiveDelivery.erp_rec_delv_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpReceiveDelivery")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_receive_delivery.serialize


class ErpTimeEntry(IdentifiedObject):
    """ An individual entry on an ErpTimeSheet.
    """
    # <<< erp_time_entry
    # @generated
    def __init__(self, erp_project_accounting=None, erp_time_sheet=None, status=None, **kw_args):
        """ Initialises a new 'ErpTimeEntry' instance.
        """

        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._erp_time_sheet = None
        self.erp_time_sheet = erp_time_sheet

        self.status = status


        super(ErpTimeEntry, self).__init__(**kw_args)
    # >>> erp_time_entry

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.erp_time_entries if x != self]
            self._erp_project_accounting._erp_time_entries = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._erp_time_entries.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< erp_time_sheet
    # @generated
    def get_erp_time_sheet(self):
        """ 
        """
        return self._erp_time_sheet

    def set_erp_time_sheet(self, value):
        if self._erp_time_sheet is not None:
            filtered = [x for x in self.erp_time_sheet.erp_time_entries if x != self]
            self._erp_time_sheet._erp_time_entries = filtered

        self._erp_time_sheet = value
        if self._erp_time_sheet is not None:
            self._erp_time_sheet._erp_time_entries.append(self)

    erp_time_sheet = property(get_erp_time_sheet, set_erp_time_sheet)
    # >>> erp_time_sheet

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpTimeEntry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_time_entry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpTimeEntry.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpTimeEntry", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_project_accounting is not None:
            s += '%s<%s:ErpTimeEntry.erp_project_accounting rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_project_accounting.uri)
        if self.erp_time_sheet is not None:
            s += '%s<%s:ErpTimeEntry.erp_time_sheet rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_time_sheet.uri)
        if self.status is not None:
            s += '%s<%s:ErpTimeEntry.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpTimeEntry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_time_entry.serialize


class ErpChartOfAccounts(Document):
    """ Accounting structure of a business. Each account represents a financial aspect of a business, such as its Accounts Payable, or the value of its inventory, or its office supply expenses.
    """
    pass
    # <<< erp_chart_of_accounts
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ErpChartOfAccounts' instance.
        """


        super(ErpChartOfAccounts, self).__init__(**kw_args)
    # >>> erp_chart_of_accounts


    def __str__(self):
        """ Returns a string representation of the ErpChartOfAccounts.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_chart_of_accounts.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpChartOfAccounts.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpChartOfAccounts", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpChartOfAccounts")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_chart_of_accounts.serialize


class ErpLedgerBudget(Document):
    """ Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.
    """
    # <<< erp_ledger_budget
    # @generated
    def __init__(self, erp_led_bud_line_items=None, **kw_args):
        """ Initialises a new 'ErpLedgerBudget' instance.
        """

        self._erp_led_bud_line_items = []
        if erp_led_bud_line_items is not None:
            self.erp_led_bud_line_items = erp_led_bud_line_items
        else:
            self.erp_led_bud_line_items = []


        super(ErpLedgerBudget, self).__init__(**kw_args)
    # >>> erp_ledger_budget

    # <<< erp_led_bud_line_items
    # @generated
    def get_erp_led_bud_line_items(self):
        """ 
        """
        return self._erp_led_bud_line_items

    def set_erp_led_bud_line_items(self, value):
        for x in self._erp_led_bud_line_items:
            x._erp_ledger_budget = None
        for y in value:
            y._erp_ledger_budget = self
        self._erp_led_bud_line_items = value

    erp_led_bud_line_items = property(get_erp_led_bud_line_items, set_erp_led_bud_line_items)

    def add_erp_led_bud_line_items(self, *erp_led_bud_line_items):
        for obj in erp_led_bud_line_items:
            obj._erp_ledger_budget = self
            self._erp_led_bud_line_items.append(obj)

    def remove_erp_led_bud_line_items(self, *erp_led_bud_line_items):
        for obj in erp_led_bud_line_items:
            obj._erp_ledger_budget = None
            self._erp_led_bud_line_items.remove(obj)
    # >>> erp_led_bud_line_items


    def __str__(self):
        """ Returns a string representation of the ErpLedgerBudget.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_ledger_budget.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpLedgerBudget.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpLedgerBudget", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_led_bud_line_items:
            s += '%s<%s:ErpLedgerBudget.erp_led_bud_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpLedgerBudget")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_ledger_budget.serialize


class ErpRequisition(Document):
    """ General information that applies to a utility requisition that is a request for the purchase of goods or services. Typically, a requisition leads to the creation of a purchase order to a specific supplier.
    """
    # <<< erp_requisition
    # @generated
    def __init__(self, erp_req_line_items=None, **kw_args):
        """ Initialises a new 'ErpRequisition' instance.
        """

        self._erp_req_line_items = []
        if erp_req_line_items is not None:
            self.erp_req_line_items = erp_req_line_items
        else:
            self.erp_req_line_items = []


        super(ErpRequisition, self).__init__(**kw_args)
    # >>> erp_requisition

    # <<< erp_req_line_items
    # @generated
    def get_erp_req_line_items(self):
        """ 
        """
        return self._erp_req_line_items

    def set_erp_req_line_items(self, value):
        for x in self._erp_req_line_items:
            x._erp_requisition = None
        for y in value:
            y._erp_requisition = self
        self._erp_req_line_items = value

    erp_req_line_items = property(get_erp_req_line_items, set_erp_req_line_items)

    def add_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._erp_requisition = self
            self._erp_req_line_items.append(obj)

    def remove_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._erp_requisition = None
            self._erp_req_line_items.remove(obj)
    # >>> erp_req_line_items


    def __str__(self):
        """ Returns a string representation of the ErpRequisition.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_requisition.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpRequisition.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpRequisition", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_req_line_items:
            s += '%s<%s:ErpRequisition.erp_req_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpRequisition")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_requisition.serialize


class OrgErpPersonRole(Role):
    """ Roles played between Persons and Organisations.
    """
    # <<< org_erp_person_role
    # @generated
    def __init__(self, client_id='', erp_organisation=None, erp_person=None, **kw_args):
        """ Initialises a new 'OrgErpPersonRole' instance.
        """
        # Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc. 
        self.client_id = client_id


        self._erp_organisation = None
        self.erp_organisation = erp_organisation

        self._erp_person = None
        self.erp_person = erp_person


        super(OrgErpPersonRole, self).__init__(**kw_args)
    # >>> org_erp_person_role

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.erp_person_roles if x != self]
            self._erp_organisation._erp_person_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._erp_person_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.erp_organisation_roles if x != self]
            self._erp_person._erp_organisation_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._erp_organisation_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person


    def __str__(self):
        """ Returns a string representation of the OrgErpPersonRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_erp_person_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgErpPersonRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgErpPersonRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_organisation is not None:
            s += '%s<%s:OrgErpPersonRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
        if self.erp_person is not None:
            s += '%s<%s:OrgErpPersonRole.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        s += '%s<%s:OrgErpPersonRole.client_id>%s</%s:OrgErpPersonRole.client_id>' % \
            (indent, ns_prefix, self.client_id, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgErpPersonRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_erp_person_role.serialize


class ErpBOM(Document):
    """ Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.
    """
    # <<< erp_bom
    # @generated
    def __init__(self, design=None, erp_bom_item_datas=None, **kw_args):
        """ Initialises a new 'ErpBOM' instance.
        """

        self._design = None
        self.design = design

        self._erp_bom_item_datas = []
        if erp_bom_item_datas is not None:
            self.erp_bom_item_datas = erp_bom_item_datas
        else:
            self.erp_bom_item_datas = []


        super(ErpBOM, self).__init__(**kw_args)
    # >>> erp_bom

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            filtered = [x for x in self.design.erp_boms if x != self]
            self._design._erp_boms = filtered

        self._design = value
        if self._design is not None:
            self._design._erp_boms.append(self)

    design = property(get_design, set_design)
    # >>> design

    # <<< erp_bom_item_datas
    # @generated
    def get_erp_bom_item_datas(self):
        """ 
        """
        return self._erp_bom_item_datas

    def set_erp_bom_item_datas(self, value):
        for x in self._erp_bom_item_datas:
            x._erp_bom = None
        for y in value:
            y._erp_bom = self
        self._erp_bom_item_datas = value

    erp_bom_item_datas = property(get_erp_bom_item_datas, set_erp_bom_item_datas)

    def add_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._erp_bom = self
            self._erp_bom_item_datas.append(obj)

    def remove_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._erp_bom = None
            self._erp_bom_item_datas.remove(obj)
    # >>> erp_bom_item_datas


    def __str__(self):
        """ Returns a string representation of the ErpBOM.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_bom.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpBOM.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpBOM", self.uri)
        if format:
            indent += ' ' * depth

        if self.design is not None:
            s += '%s<%s:ErpBOM.design rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design.uri)
        for obj in self.erp_bom_item_datas:
            s += '%s<%s:ErpBOM.erp_bom_item_datas rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpBOM")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_bom.serialize


class ErpTimeSheet(Document):
    """ Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.
    """
    # <<< erp_time_sheet
    # @generated
    def __init__(self, erp_time_entries=None, **kw_args):
        """ Initialises a new 'ErpTimeSheet' instance.
        """

        self._erp_time_entries = []
        if erp_time_entries is not None:
            self.erp_time_entries = erp_time_entries
        else:
            self.erp_time_entries = []


        super(ErpTimeSheet, self).__init__(**kw_args)
    # >>> erp_time_sheet

    # <<< erp_time_entries
    # @generated
    def get_erp_time_entries(self):
        """ 
        """
        return self._erp_time_entries

    def set_erp_time_entries(self, value):
        for x in self._erp_time_entries:
            x._erp_time_sheet = None
        for y in value:
            y._erp_time_sheet = self
        self._erp_time_entries = value

    erp_time_entries = property(get_erp_time_entries, set_erp_time_entries)

    def add_erp_time_entries(self, *erp_time_entries):
        for obj in erp_time_entries:
            obj._erp_time_sheet = self
            self._erp_time_entries.append(obj)

    def remove_erp_time_entries(self, *erp_time_entries):
        for obj in erp_time_entries:
            obj._erp_time_sheet = None
            self._erp_time_entries.remove(obj)
    # >>> erp_time_entries


    def __str__(self):
        """ Returns a string representation of the ErpTimeSheet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_time_sheet.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpTimeSheet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpTimeSheet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_time_entries:
            s += '%s<%s:ErpTimeSheet.erp_time_entries rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpTimeSheet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_time_sheet.serialize


class ErpSalesOrder(Document):
    """ General purpose Sales Order is used for utility service orders, etc. As used by the OAG, the SalesOrder is a step beyond a PurchaseOrder in that the receiving entity of the order also communicates SalesInformoration about the Order along with the Order itself.
    """
    pass
    # <<< erp_sales_order
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ErpSalesOrder' instance.
        """


        super(ErpSalesOrder, self).__init__(**kw_args)
    # >>> erp_sales_order


    def __str__(self):
        """ Returns a string representation of the ErpSalesOrder.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_sales_order.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpSalesOrder.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpSalesOrder", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpSalesOrder")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_sales_order.serialize


class ErpRecLineItem(IdentifiedObject):
    """ Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.
    """
    # <<< erp_rec_line_item
    # @generated
    def __init__(self, erp_invoice_line_item=None, erp_payments=None, erp_journal_entries=None, erp_receivable=None, status=None, **kw_args):
        """ Initialises a new 'ErpRecLineItem' instance.
        """

        self._erp_invoice_line_item = None
        self.erp_invoice_line_item = erp_invoice_line_item

        self._erp_payments = []
        if erp_payments is not None:
            self.erp_payments = erp_payments
        else:
            self.erp_payments = []

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []

        self._erp_receivable = None
        self.erp_receivable = erp_receivable

        self.status = status


        super(ErpRecLineItem, self).__init__(**kw_args)
    # >>> erp_rec_line_item

    # <<< erp_invoice_line_item
    # @generated
    def get_erp_invoice_line_item(self):
        """ 
        """
        return self._erp_invoice_line_item

    def set_erp_invoice_line_item(self, value):
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_rec_line_item = None

        self._erp_invoice_line_item = value
        if self._erp_invoice_line_item is not None:
            self._erp_invoice_line_item._erp_rec_line_item = self

    erp_invoice_line_item = property(get_erp_invoice_line_item, set_erp_invoice_line_item)
    # >>> erp_invoice_line_item

    # <<< erp_payments
    # @generated
    def get_erp_payments(self):
        """ 
        """
        return self._erp_payments

    def set_erp_payments(self, value):
        for p in self._erp_payments:
            filtered = [q for q in p.erp_rec_line_items if q != self]
            self._erp_payments._erp_rec_line_items = filtered
        for r in value:
            if self not in r._erp_rec_line_items:
                r._erp_rec_line_items.append(self)
        self._erp_payments = value

    erp_payments = property(get_erp_payments, set_erp_payments)

    def add_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self not in obj._erp_rec_line_items:
                obj._erp_rec_line_items.append(self)
            self._erp_payments.append(obj)

    def remove_erp_payments(self, *erp_payments):
        for obj in erp_payments:
            if self in obj._erp_rec_line_items:
                obj._erp_rec_line_items.remove(self)
            self._erp_payments.remove(obj)
    # >>> erp_payments

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for p in self._erp_journal_entries:
            filtered = [q for q in p.erp_rec_line_items if q != self]
            self._erp_journal_entries._erp_rec_line_items = filtered
        for r in value:
            if self not in r._erp_rec_line_items:
                r._erp_rec_line_items.append(self)
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self not in obj._erp_rec_line_items:
                obj._erp_rec_line_items.append(self)
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self in obj._erp_rec_line_items:
                obj._erp_rec_line_items.remove(self)
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries

    # <<< erp_receivable
    # @generated
    def get_erp_receivable(self):
        """ 
        """
        return self._erp_receivable

    def set_erp_receivable(self, value):
        if self._erp_receivable is not None:
            filtered = [x for x in self.erp_receivable.erp_rec_line_items if x != self]
            self._erp_receivable._erp_rec_line_items = filtered

        self._erp_receivable = value
        if self._erp_receivable is not None:
            self._erp_receivable._erp_rec_line_items.append(self)

    erp_receivable = property(get_erp_receivable, set_erp_receivable)
    # >>> erp_receivable

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpRecLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_rec_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpRecLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpRecLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_invoice_line_item is not None:
            s += '%s<%s:ErpRecLineItem.erp_invoice_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_invoice_line_item.uri)
        for obj in self.erp_payments:
            s += '%s<%s:ErpRecLineItem.erp_payments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_journal_entries:
            s += '%s<%s:ErpRecLineItem.erp_journal_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_receivable is not None:
            s += '%s<%s:ErpRecLineItem.erp_receivable rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_receivable.uri)
        if self.status is not None:
            s += '%s<%s:ErpRecLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpRecLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_rec_line_item.serialize


class ErpSiteLevelData(IdentifiedObject):
    """ For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.
    """
    # <<< erp_site_level_data
    # @generated
    def __init__(self, status=None, land_property=None, **kw_args):
        """ Initialises a new 'ErpSiteLevelData' instance.
        """

        self.status = status

        self._land_property = None
        self.land_property = land_property


        super(ErpSiteLevelData, self).__init__(**kw_args)
    # >>> erp_site_level_data

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ 
        """
        return self._land_property

    def set_land_property(self, value):
        if self._land_property is not None:
            filtered = [x for x in self.land_property.erp_site_level_datas if x != self]
            self._land_property._erp_site_level_datas = filtered

        self._land_property = value
        if self._land_property is not None:
            self._land_property._erp_site_level_datas.append(self)

    land_property = property(get_land_property, set_land_property)
    # >>> land_property


    def __str__(self):
        """ Returns a string representation of the ErpSiteLevelData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_site_level_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpSiteLevelData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpSiteLevelData", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:ErpSiteLevelData.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.land_property is not None:
            s += '%s<%s:ErpSiteLevelData.land_property rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.land_property.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpSiteLevelData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_site_level_data.serialize


class ErpPersonnel(IdentifiedObject):
    """ Information that applies to the basic data about a utility person, used by ERP applications to transfer Personnel data for a worker.
    """
    # <<< erp_personnel
    # @generated
    def __init__(self, erp_persons=None, status=None, **kw_args):
        """ Initialises a new 'ErpPersonnel' instance.
        """

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status


        super(ErpPersonnel, self).__init__(**kw_args)
    # >>> erp_personnel

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for x in self._erp_persons:
            x._erp_personnel = None
        for y in value:
            y._erp_personnel = self
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._erp_personnel = self
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._erp_personnel = None
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpPersonnel.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_personnel.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPersonnel.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPersonnel", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_persons:
            s += '%s<%s:ErpPersonnel.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ErpPersonnel.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPersonnel")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_personnel.serialize


class ErpReceivable(Document):
    """ Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.
    """
    # <<< erp_receivable
    # @generated
    def __init__(self, erp_rec_line_items=None, **kw_args):
        """ Initialises a new 'ErpReceivable' instance.
        """

        self._erp_rec_line_items = []
        if erp_rec_line_items is not None:
            self.erp_rec_line_items = erp_rec_line_items
        else:
            self.erp_rec_line_items = []


        super(ErpReceivable, self).__init__(**kw_args)
    # >>> erp_receivable

    # <<< erp_rec_line_items
    # @generated
    def get_erp_rec_line_items(self):
        """ 
        """
        return self._erp_rec_line_items

    def set_erp_rec_line_items(self, value):
        for x in self._erp_rec_line_items:
            x._erp_receivable = None
        for y in value:
            y._erp_receivable = self
        self._erp_rec_line_items = value

    erp_rec_line_items = property(get_erp_rec_line_items, set_erp_rec_line_items)

    def add_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            obj._erp_receivable = self
            self._erp_rec_line_items.append(obj)

    def remove_erp_rec_line_items(self, *erp_rec_line_items):
        for obj in erp_rec_line_items:
            obj._erp_receivable = None
            self._erp_rec_line_items.remove(obj)
    # >>> erp_rec_line_items


    def __str__(self):
        """ Returns a string representation of the ErpReceivable.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_receivable.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpReceivable.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpReceivable", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_rec_line_items:
            s += '%s<%s:ErpReceivable.erp_rec_line_items rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpReceivable")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_receivable.serialize


class ErpLedgerEntry(IdentifiedObject):
    """ Details of an individual entry in a ledger, which was posted from a journal on the posted date.
    """
    # <<< erp_ledger_entry
    # @generated
    def __init__(self, account_kind='estimate', amount=0.0, account_id='', transaction_date_time='', posted_date_time='', erp_ledger=None, user_attributes=None, erp_ledger_entry=None, settlements=None, erp_jounal_entry=None, status=None, **kw_args):
        """ Initialises a new 'ErpLedgerEntry' instance.
        """
        # Kind of account for this entry. Values are: "estimate", "reversal", "statistical", "normal"
        self.account_kind = 'estimate'

        # The amount of the debit or credit for this account. 
        self.amount = amount

        # Account identifier for this entry. 
        self.account_id = account_id

        # Date and time journal entry was recorded. 
        self.transaction_date_time = transaction_date_time

        # Date and time this entry was posted to the ledger. 
        self.posted_date_time = posted_date_time


        self._erp_ledger = None
        self.erp_ledger = erp_ledger

        self._user_attributes = []
        if user_attributes is not None:
            self.user_attributes = user_attributes
        else:
            self.user_attributes = []

        self._erp_ledger_entry = None
        self.erp_ledger_entry = erp_ledger_entry

        self._settlements = []
        if settlements is not None:
            self.settlements = settlements
        else:
            self.settlements = []

        self._erp_jounal_entry = None
        self.erp_jounal_entry = erp_jounal_entry

        self.status = status


        super(ErpLedgerEntry, self).__init__(**kw_args)
    # >>> erp_ledger_entry

    # <<< erp_ledger
    # @generated
    def get_erp_ledger(self):
        """ 
        """
        return self._erp_ledger

    def set_erp_ledger(self, value):
        if self._erp_ledger is not None:
            filtered = [x for x in self.erp_ledger.erp_ledger_entries if x != self]
            self._erp_ledger._erp_ledger_entries = filtered

        self._erp_ledger = value
        if self._erp_ledger is not None:
            self._erp_ledger._erp_ledger_entries.append(self)

    erp_ledger = property(get_erp_ledger, set_erp_ledger)
    # >>> erp_ledger

    # <<< user_attributes
    # @generated
    def get_user_attributes(self):
        """ 
        """
        return self._user_attributes

    def set_user_attributes(self, value):
        for p in self._user_attributes:
            filtered = [q for q in p.erp_ledger_entries if q != self]
            self._user_attributes._erp_ledger_entries = filtered
        for r in value:
            if self not in r._erp_ledger_entries:
                r._erp_ledger_entries.append(self)
        self._user_attributes = value

    user_attributes = property(get_user_attributes, set_user_attributes)

    def add_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self not in obj._erp_ledger_entries:
                obj._erp_ledger_entries.append(self)
            self._user_attributes.append(obj)

    def remove_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self in obj._erp_ledger_entries:
                obj._erp_ledger_entries.remove(self)
            self._user_attributes.remove(obj)
    # >>> user_attributes

    # <<< erp_ledger_entry
    # @generated
    def get_erp_ledger_entry(self):
        """ 
        """
        return self._erp_ledger_entry

    def set_erp_ledger_entry(self, value):
        if self._erp_ledger_entry is not None:
            self._erp_ledger_entry._erp_led_bud_line_item = None

        self._erp_ledger_entry = value
        if self._erp_ledger_entry is not None:
            self._erp_ledger_entry._erp_led_bud_line_item = self

    erp_ledger_entry = property(get_erp_ledger_entry, set_erp_ledger_entry)
    # >>> erp_ledger_entry

    # <<< settlements
    # @generated
    def get_settlements(self):
        """ 
        """
        return self._settlements

    def set_settlements(self, value):
        for p in self._settlements:
            filtered = [q for q in p.erp_ledger_entries if q != self]
            self._settlements._erp_ledger_entries = filtered
        for r in value:
            if self not in r._erp_ledger_entries:
                r._erp_ledger_entries.append(self)
        self._settlements = value

    settlements = property(get_settlements, set_settlements)

    def add_settlements(self, *settlements):
        for obj in settlements:
            if self not in obj._erp_ledger_entries:
                obj._erp_ledger_entries.append(self)
            self._settlements.append(obj)

    def remove_settlements(self, *settlements):
        for obj in settlements:
            if self in obj._erp_ledger_entries:
                obj._erp_ledger_entries.remove(self)
            self._settlements.remove(obj)
    # >>> settlements

    # <<< erp_jounal_entry
    # @generated
    def get_erp_jounal_entry(self):
        """ 
        """
        return self._erp_jounal_entry

    def set_erp_jounal_entry(self, value):
        if self._erp_jounal_entry is not None:
            self._erp_jounal_entry._erp_ledger_entry = None

        self._erp_jounal_entry = value
        if self._erp_jounal_entry is not None:
            self._erp_jounal_entry._erp_ledger_entry = self

    erp_jounal_entry = property(get_erp_jounal_entry, set_erp_jounal_entry)
    # >>> erp_jounal_entry

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpLedgerEntry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_ledger_entry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpLedgerEntry.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpLedgerEntry", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_ledger is not None:
            s += '%s<%s:ErpLedgerEntry.erp_ledger rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_ledger.uri)
        for obj in self.user_attributes:
            s += '%s<%s:ErpLedgerEntry.user_attributes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_ledger_entry is not None:
            s += '%s<%s:ErpLedgerEntry.erp_ledger_entry rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_ledger_entry.uri)
        for obj in self.settlements:
            s += '%s<%s:ErpLedgerEntry.settlements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_jounal_entry is not None:
            s += '%s<%s:ErpLedgerEntry.erp_jounal_entry rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_jounal_entry.uri)
        if self.status is not None:
            s += '%s<%s:ErpLedgerEntry.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ErpLedgerEntry.account_kind>%s</%s:ErpLedgerEntry.account_kind>' % \
            (indent, ns_prefix, self.account_kind, ns_prefix)
        s += '%s<%s:ErpLedgerEntry.amount>%s</%s:ErpLedgerEntry.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:ErpLedgerEntry.account_id>%s</%s:ErpLedgerEntry.account_id>' % \
            (indent, ns_prefix, self.account_id, ns_prefix)
        s += '%s<%s:ErpLedgerEntry.transaction_date_time>%s</%s:ErpLedgerEntry.transaction_date_time>' % \
            (indent, ns_prefix, self.transaction_date_time, ns_prefix)
        s += '%s<%s:ErpLedgerEntry.posted_date_time>%s</%s:ErpLedgerEntry.posted_date_time>' % \
            (indent, ns_prefix, self.posted_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpLedgerEntry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_ledger_entry.serialize


class ErpLedBudLineItem(IdentifiedObject):
    """ Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.
    """
    # <<< erp_led_bud_line_item
    # @generated
    def __init__(self, erp_ledger_budget=None, erp_led_bud_line_item=None, status=None, **kw_args):
        """ Initialises a new 'ErpLedBudLineItem' instance.
        """

        self._erp_ledger_budget = None
        self.erp_ledger_budget = erp_ledger_budget

        self._erp_led_bud_line_item = None
        self.erp_led_bud_line_item = erp_led_bud_line_item

        self.status = status


        super(ErpLedBudLineItem, self).__init__(**kw_args)
    # >>> erp_led_bud_line_item

    # <<< erp_ledger_budget
    # @generated
    def get_erp_ledger_budget(self):
        """ 
        """
        return self._erp_ledger_budget

    def set_erp_ledger_budget(self, value):
        if self._erp_ledger_budget is not None:
            filtered = [x for x in self.erp_ledger_budget.erp_led_bud_line_items if x != self]
            self._erp_ledger_budget._erp_led_bud_line_items = filtered

        self._erp_ledger_budget = value
        if self._erp_ledger_budget is not None:
            self._erp_ledger_budget._erp_led_bud_line_items.append(self)

    erp_ledger_budget = property(get_erp_ledger_budget, set_erp_ledger_budget)
    # >>> erp_ledger_budget

    # <<< erp_led_bud_line_item
    # @generated
    def get_erp_led_bud_line_item(self):
        """ 
        """
        return self._erp_led_bud_line_item

    def set_erp_led_bud_line_item(self, value):
        if self._erp_led_bud_line_item is not None:
            self._erp_led_bud_line_item._erp_ledger_entry = None

        self._erp_led_bud_line_item = value
        if self._erp_led_bud_line_item is not None:
            self._erp_led_bud_line_item._erp_ledger_entry = self

    erp_led_bud_line_item = property(get_erp_led_bud_line_item, set_erp_led_bud_line_item)
    # >>> erp_led_bud_line_item

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpLedBudLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_led_bud_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpLedBudLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpLedBudLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_ledger_budget is not None:
            s += '%s<%s:ErpLedBudLineItem.erp_ledger_budget rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_ledger_budget.uri)
        if self.erp_led_bud_line_item is not None:
            s += '%s<%s:ErpLedBudLineItem.erp_led_bud_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_led_bud_line_item.uri)
        if self.status is not None:
            s += '%s<%s:ErpLedBudLineItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpLedBudLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_led_bud_line_item.serialize


class ErpTelephoneNumber(TelephoneNumber):
    """ The telephone number for a person or organisation.
    """
    # <<< erp_telephone_number
    # @generated
    def __init__(self, usage='', electronic_address=None, erp_persons=None, status=None, **kw_args):
        """ Initialises a new 'ErpTelephoneNumber' instance.
        """
        # The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other. 
        self.usage = usage


        self._electronic_address = None
        self.electronic_address = electronic_address

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status


        super(ErpTelephoneNumber, self).__init__(**kw_args)
    # >>> erp_telephone_number

    # <<< electronic_address
    # @generated
    def get_electronic_address(self):
        """ 
        """
        return self._electronic_address

    def set_electronic_address(self, value):
        if self._electronic_address is not None:
            filtered = [x for x in self.electronic_address.erp_telephone_numbers if x != self]
            self._electronic_address._erp_telephone_numbers = filtered

        self._electronic_address = value
        if self._electronic_address is not None:
            self._electronic_address._erp_telephone_numbers.append(self)

    electronic_address = property(get_electronic_address, set_electronic_address)
    # >>> electronic_address

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.erp_telephone_numbers if q != self]
            self._erp_persons._erp_telephone_numbers = filtered
        for r in value:
            if self not in r._erp_telephone_numbers:
                r._erp_telephone_numbers.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._erp_telephone_numbers:
                obj._erp_telephone_numbers.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._erp_telephone_numbers:
                obj._erp_telephone_numbers.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ErpTelephoneNumber.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_telephone_number.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpTelephoneNumber.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpTelephoneNumber", self.uri)
        if format:
            indent += ' ' * depth

        if self.electronic_address is not None:
            s += '%s<%s:ErpTelephoneNumber.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.erp_persons:
            s += '%s<%s:ErpTelephoneNumber.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ErpTelephoneNumber.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ErpTelephoneNumber.usage>%s</%s:ErpTelephoneNumber.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
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
        if self.organisation is not None:
            s += '%s<%s:TelephoneNumber.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        if self.location is not None:
            s += '%s<%s:TelephoneNumber.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        s += '%s<%s:TelephoneNumber.city_code>%s</%s:TelephoneNumber.city_code>' % \
            (indent, ns_prefix, self.city_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.country_code>%s</%s:TelephoneNumber.country_code>' % \
            (indent, ns_prefix, self.country_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.extension>%s</%s:TelephoneNumber.extension>' % \
            (indent, ns_prefix, self.extension, ns_prefix)
        s += '%s<%s:TelephoneNumber.area_code>%s</%s:TelephoneNumber.area_code>' % \
            (indent, ns_prefix, self.area_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.local_number>%s</%s:TelephoneNumber.local_number>' % \
            (indent, ns_prefix, self.local_number, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpTelephoneNumber")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_telephone_number.serialize


class ErpCompetency(IdentifiedObject):
    """ Information that describes aptitudes of a utility employee. Unlike Skills that an ErpPerson must be certified to perform before undertaking certain type of assignments (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human Resource (HR) matters such as schooling, training, etc.
    """
    # <<< erp_competency
    # @generated
    def __init__(self, erp_persons=None, **kw_args):
        """ Initialises a new 'ErpCompetency' instance.
        """

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []


        super(ErpCompetency, self).__init__(**kw_args)
    # >>> erp_competency

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for x in self._erp_persons:
            x._erp_competency = None
        for y in value:
            y._erp_competency = self
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._erp_competency = self
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._erp_competency = None
            self._erp_persons.remove(obj)
    # >>> erp_persons


    def __str__(self):
        """ Returns a string representation of the ErpCompetency.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_competency.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpCompetency.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpCompetency", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_persons:
            s += '%s<%s:ErpCompetency.erp_persons rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpCompetency")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_competency.serialize


# <<< inf_erpsupport
# @generated
# >>> inf_erpsupport
