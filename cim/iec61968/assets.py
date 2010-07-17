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

""" This package contains the core information classes that support asset management applications with specialized classes for asset-level models for objects (as opposed to power system resource models, mainly defined in IEC61970::Wires package).
"""

from cim.iec61970.core import IdentifiedObject
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.assets"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Assets"

class Seal(IdentifiedObject):
    """ Physically controls access to AssetContainers.
    """
    # <<< seal
    # @generated
    def __init__(self, condition='locked', kind='other', seal_number='', applied_date_time='', asset_container=None, **kw_args):
        """ Initialises a new 'Seal' instance.
        """
        # Condition of seal. Values are: "locked", "open", "missing", "broken", "other"
        self.condition = 'locked'

        # Kind of seal. Values are: "other", "steel", "lock", "lead"
        self.kind = 'other'

        # (reserved word) Seal number. 
        self.seal_number = seal_number

        # Date and time this seal has been applied. 
        self.applied_date_time = applied_date_time


        self._asset_container = None
        self.asset_container = asset_container


        super(Seal, self).__init__(**kw_args)
    # >>> seal

    # <<< asset_container
    # @generated
    def get_asset_container(self):
        """ Asset container to which this seal is applied.
        """
        return self._asset_container

    def set_asset_container(self, value):
        if self._asset_container is not None:
            filtered = [x for x in self.asset_container.seals if x != self]
            self._asset_container._seals = filtered

        self._asset_container = value
        if self._asset_container is not None:
            self._asset_container._seals.append(self)

    asset_container = property(get_asset_container, set_asset_container)
    # >>> asset_container


    def __str__(self):
        """ Returns a string representation of the Seal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< seal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Seal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Seal", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset_container is not None:
            s += '%s<%s:Seal.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        s += '%s<%s:Seal.condition>%s</%s:Seal.condition>' % \
            (indent, ns_prefix, self.condition, ns_prefix)
        s += '%s<%s:Seal.kind>%s</%s:Seal.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Seal.seal_number>%s</%s:Seal.seal_number>' % \
            (indent, ns_prefix, self.seal_number, ns_prefix)
        s += '%s<%s:Seal.applied_date_time>%s</%s:Seal.applied_date_time>' % \
            (indent, ns_prefix, self.applied_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Seal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> seal.serialize


class Asset(IdentifiedObject):
    """ Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """
    # <<< asset
    # @generated
    def __init__(self, initial_condition='', category='', lot_number='', application='', serial_number='', installation_date='', corporate_code='', purchase_price=0.0, manufactured_date='', initial_loss_of_life=0.0, utc_number='', critical=False, measurements=None, hazards=None, erp_organisation_roles=None, dimensions_info=None, scheduled_events=None, mediums=None, asset_functions=None, properties=None, asset_container=None, ratings=None, activity_records=None, from_asset_roles=None, location_roles=None, power_system_resource_roles=None, document_roles=None, change_items=None, erp_item_master=None, electronic_addresses=None, work_task=None, erp_rec_delivery_items=None, reliability_infos=None, to_asset_roles=None, asset_property_curves=None, financial_info=None, erp_inventory=None, acceptance_test=None, status=None, **kw_args):
        """ Initialises a new 'Asset' instance.
        """
        # Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset. 
        self.initial_condition = initial_condition

        # Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        self.category = category

        # Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots. 
        self.lot_number = lot_number

        # The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0. 
        self.application = application

        # Serial number of this asset. 
        self.serial_number = serial_number

        # (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool). 
        self.installation_date = installation_date

        # Code for this type of asset. 
        self.corporate_code = corporate_code

        # Purchase price of asset. 
        self.purchase_price = purchase_price

        # Date this asset was manufactured. 
        self.manufactured_date = manufactured_date

        # Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices. 
        self.initial_loss_of_life = initial_loss_of_life

        # Uniquely Tracked Commodity (UTC) number. 
        self.utc_number = utc_number

        # True if asset is considered critical for some reason (for example, a pole with critical attachments). 
        self.critical = critical


        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._hazards = []
        if hazards is not None:
            self.hazards = hazards
        else:
            self.hazards = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._dimensions_info = None
        self.dimensions_info = dimensions_info

        self._scheduled_events = []
        if scheduled_events is not None:
            self.scheduled_events = scheduled_events
        else:
            self.scheduled_events = []

        self._mediums = []
        if mediums is not None:
            self.mediums = mediums
        else:
            self.mediums = []

        self._asset_functions = []
        if asset_functions is not None:
            self.asset_functions = asset_functions
        else:
            self.asset_functions = []

        self._properties = []
        if properties is not None:
            self.properties = properties
        else:
            self.properties = []

        self._asset_container = None
        self.asset_container = asset_container

        self._ratings = []
        if ratings is not None:
            self.ratings = ratings
        else:
            self.ratings = []

        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []

        self._from_asset_roles = []
        if from_asset_roles is not None:
            self.from_asset_roles = from_asset_roles
        else:
            self.from_asset_roles = []

        self._location_roles = []
        if location_roles is not None:
            self.location_roles = location_roles
        else:
            self.location_roles = []

        self._power_system_resource_roles = []
        if power_system_resource_roles is not None:
            self.power_system_resource_roles = power_system_resource_roles
        else:
            self.power_system_resource_roles = []

        self._document_roles = []
        if document_roles is not None:
            self.document_roles = document_roles
        else:
            self.document_roles = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._erp_item_master = None
        self.erp_item_master = erp_item_master

        self._electronic_addresses = []
        if electronic_addresses is not None:
            self.electronic_addresses = electronic_addresses
        else:
            self.electronic_addresses = []

        self._work_task = None
        self.work_task = work_task

        self._erp_rec_delivery_items = []
        if erp_rec_delivery_items is not None:
            self.erp_rec_delivery_items = erp_rec_delivery_items
        else:
            self.erp_rec_delivery_items = []

        self._reliability_infos = []
        if reliability_infos is not None:
            self.reliability_infos = reliability_infos
        else:
            self.reliability_infos = []

        self._to_asset_roles = []
        if to_asset_roles is not None:
            self.to_asset_roles = to_asset_roles
        else:
            self.to_asset_roles = []

        self._asset_property_curves = []
        if asset_property_curves is not None:
            self.asset_property_curves = asset_property_curves
        else:
            self.asset_property_curves = []

        self._financial_info = None
        self.financial_info = financial_info

        self._erp_inventory = None
        self.erp_inventory = erp_inventory

        self.acceptance_test = acceptance_test

        self.status = status


        super(Asset, self).__init__(**kw_args)
    # >>> asset

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ 
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._asset = None
        for y in value:
            y._asset = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._asset = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._asset = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< hazards
    # @generated
    def get_hazards(self):
        """ 
        """
        return self._hazards

    def set_hazards(self, value):
        for p in self._hazards:
            filtered = [q for q in p.assets if q != self]
            self._hazards._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._hazards = value

    hazards = property(get_hazards, set_hazards)

    def add_hazards(self, *hazards):
        for obj in hazards:
            if self not in obj._assets:
                obj._assets.append(self)
            self._hazards.append(obj)

    def remove_hazards(self, *hazards):
        for obj in hazards:
            if self in obj._assets:
                obj._assets.remove(self)
            self._hazards.remove(obj)
    # >>> hazards

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for x in self._erp_organisation_roles:
            x._asset = None
        for y in value:
            y._asset = self
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._asset = self
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._asset = None
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< dimensions_info
    # @generated
    def get_dimensions_info(self):
        """ 
        """
        return self._dimensions_info

    def set_dimensions_info(self, value):
        if self._dimensions_info is not None:
            filtered = [x for x in self.dimensions_info.assets if x != self]
            self._dimensions_info._assets = filtered

        self._dimensions_info = value
        if self._dimensions_info is not None:
            self._dimensions_info._assets.append(self)

    dimensions_info = property(get_dimensions_info, set_dimensions_info)
    # >>> dimensions_info

    # <<< scheduled_events
    # @generated
    def get_scheduled_events(self):
        """ 
        """
        return self._scheduled_events

    def set_scheduled_events(self, value):
        for p in self._scheduled_events:
            filtered = [q for q in p.assets if q != self]
            self._scheduled_events._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._scheduled_events = value

    scheduled_events = property(get_scheduled_events, set_scheduled_events)

    def add_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            if self not in obj._assets:
                obj._assets.append(self)
            self._scheduled_events.append(obj)

    def remove_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            if self in obj._assets:
                obj._assets.remove(self)
            self._scheduled_events.remove(obj)
    # >>> scheduled_events

    # <<< mediums
    # @generated
    def get_mediums(self):
        """ 
        """
        return self._mediums

    def set_mediums(self, value):
        for p in self._mediums:
            filtered = [q for q in p.assets if q != self]
            self._mediums._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._mediums = value

    mediums = property(get_mediums, set_mediums)

    def add_mediums(self, *mediums):
        for obj in mediums:
            if self not in obj._assets:
                obj._assets.append(self)
            self._mediums.append(obj)

    def remove_mediums(self, *mediums):
        for obj in mediums:
            if self in obj._assets:
                obj._assets.remove(self)
            self._mediums.remove(obj)
    # >>> mediums

    # <<< asset_functions
    # @generated
    def get_asset_functions(self):
        """ 
        """
        return self._asset_functions

    def set_asset_functions(self, value):
        for x in self._asset_functions:
            x._asset = None
        for y in value:
            y._asset = self
        self._asset_functions = value

    asset_functions = property(get_asset_functions, set_asset_functions)

    def add_asset_functions(self, *asset_functions):
        for obj in asset_functions:
            obj._asset = self
            self._asset_functions.append(obj)

    def remove_asset_functions(self, *asset_functions):
        for obj in asset_functions:
            obj._asset = None
            self._asset_functions.remove(obj)
    # >>> asset_functions

    # <<< properties
    # @generated
    def get_properties(self):
        """ UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._properties

    def set_properties(self, value):
        for p in self._properties:
            filtered = [q for q in p.property_assets if q != self]
            self._properties._property_assets = filtered
        for r in value:
            if self not in r._property_assets:
                r._property_assets.append(self)
        self._properties = value

    properties = property(get_properties, set_properties)

    def add_properties(self, *properties):
        for obj in properties:
            if self not in obj._property_assets:
                obj._property_assets.append(self)
            self._properties.append(obj)

    def remove_properties(self, *properties):
        for obj in properties:
            if self in obj._property_assets:
                obj._property_assets.remove(self)
            self._properties.remove(obj)
    # >>> properties

    # <<< asset_container
    # @generated
    def get_asset_container(self):
        """ 
        """
        return self._asset_container

    def set_asset_container(self, value):
        if self._asset_container is not None:
            filtered = [x for x in self.asset_container.assets if x != self]
            self._asset_container._assets = filtered

        self._asset_container = value
        if self._asset_container is not None:
            self._asset_container._assets.append(self)

    asset_container = property(get_asset_container, set_asset_container)
    # >>> asset_container

    # <<< ratings
    # @generated
    def get_ratings(self):
        """ UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        """
        return self._ratings

    def set_ratings(self, value):
        for p in self._ratings:
            filtered = [q for q in p.rating_assets if q != self]
            self._ratings._rating_assets = filtered
        for r in value:
            if self not in r._rating_assets:
                r._rating_assets.append(self)
        self._ratings = value

    ratings = property(get_ratings, set_ratings)

    def add_ratings(self, *ratings):
        for obj in ratings:
            if self not in obj._rating_assets:
                obj._rating_assets.append(self)
            self._ratings.append(obj)

    def remove_ratings(self, *ratings):
        for obj in ratings:
            if self in obj._rating_assets:
                obj._rating_assets.remove(self)
            self._ratings.remove(obj)
    # >>> ratings

    # <<< activity_records
    # @generated
    def get_activity_records(self):
        """ All activity records created for this asset.
        """
        return self._activity_records

    def set_activity_records(self, value):
        for p in self._activity_records:
            filtered = [q for q in p.assets if q != self]
            self._activity_records._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._activity_records = value

    activity_records = property(get_activity_records, set_activity_records)

    def add_activity_records(self, *activity_records):
        for obj in activity_records:
            if self not in obj._assets:
                obj._assets.append(self)
            self._activity_records.append(obj)

    def remove_activity_records(self, *activity_records):
        for obj in activity_records:
            if self in obj._assets:
                obj._assets.remove(self)
            self._activity_records.remove(obj)
    # >>> activity_records

    # <<< from_asset_roles
    # @generated
    def get_from_asset_roles(self):
        """ 
        """
        return self._from_asset_roles

    def set_from_asset_roles(self, value):
        for x in self._from_asset_roles:
            x._to_asset = None
        for y in value:
            y._to_asset = self
        self._from_asset_roles = value

    from_asset_roles = property(get_from_asset_roles, set_from_asset_roles)

    def add_from_asset_roles(self, *from_asset_roles):
        for obj in from_asset_roles:
            obj._to_asset = self
            self._from_asset_roles.append(obj)

    def remove_from_asset_roles(self, *from_asset_roles):
        for obj in from_asset_roles:
            obj._to_asset = None
            self._from_asset_roles.remove(obj)
    # >>> from_asset_roles

    # <<< location_roles
    # @generated
    def get_location_roles(self):
        """ 
        """
        return self._location_roles

    def set_location_roles(self, value):
        for x in self._location_roles:
            x._asset = None
        for y in value:
            y._asset = self
        self._location_roles = value

    location_roles = property(get_location_roles, set_location_roles)

    def add_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._asset = self
            self._location_roles.append(obj)

    def remove_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._asset = None
            self._location_roles.remove(obj)
    # >>> location_roles

    # <<< power_system_resource_roles
    # @generated
    def get_power_system_resource_roles(self):
        """ 
        """
        return self._power_system_resource_roles

    def set_power_system_resource_roles(self, value):
        for x in self._power_system_resource_roles:
            x._asset = None
        for y in value:
            y._asset = self
        self._power_system_resource_roles = value

    power_system_resource_roles = property(get_power_system_resource_roles, set_power_system_resource_roles)

    def add_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._asset = self
            self._power_system_resource_roles.append(obj)

    def remove_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._asset = None
            self._power_system_resource_roles.remove(obj)
    # >>> power_system_resource_roles

    # <<< document_roles
    # @generated
    def get_document_roles(self):
        """ 
        """
        return self._document_roles

    def set_document_roles(self, value):
        for x in self._document_roles:
            x._asset = None
        for y in value:
            y._asset = self
        self._document_roles = value

    document_roles = property(get_document_roles, set_document_roles)

    def add_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._asset = self
            self._document_roles.append(obj)

    def remove_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._asset = None
            self._document_roles.remove(obj)
    # >>> document_roles

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._asset = None
        for y in value:
            y._asset = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._asset = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._asset = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< erp_item_master
    # @generated
    def get_erp_item_master(self):
        """ 
        """
        return self._erp_item_master

    def set_erp_item_master(self, value):
        if self._erp_item_master is not None:
            self._erp_item_master._asset = None

        self._erp_item_master = value
        if self._erp_item_master is not None:
            self._erp_item_master._asset = self

    erp_item_master = property(get_erp_item_master, set_erp_item_master)
    # >>> erp_item_master

    # <<< electronic_addresses
    # @generated
    def get_electronic_addresses(self):
        """ All electronic addresses of this asset.
        """
        return self._electronic_addresses

    def set_electronic_addresses(self, value):
        for x in self._electronic_addresses:
            x._asset = None
        for y in value:
            y._asset = self
        self._electronic_addresses = value

    electronic_addresses = property(get_electronic_addresses, set_electronic_addresses)

    def add_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._asset = self
            self._electronic_addresses.append(obj)

    def remove_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._asset = None
            self._electronic_addresses.remove(obj)
    # >>> electronic_addresses

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.assets if x != self]
            self._work_task._assets = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._assets.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< erp_rec_delivery_items
    # @generated
    def get_erp_rec_delivery_items(self):
        """ 
        """
        return self._erp_rec_delivery_items

    def set_erp_rec_delivery_items(self, value):
        for p in self._erp_rec_delivery_items:
            filtered = [q for q in p.assets if q != self]
            self._erp_rec_delivery_items._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._erp_rec_delivery_items = value

    erp_rec_delivery_items = property(get_erp_rec_delivery_items, set_erp_rec_delivery_items)

    def add_erp_rec_delivery_items(self, *erp_rec_delivery_items):
        for obj in erp_rec_delivery_items:
            if self not in obj._assets:
                obj._assets.append(self)
            self._erp_rec_delivery_items.append(obj)

    def remove_erp_rec_delivery_items(self, *erp_rec_delivery_items):
        for obj in erp_rec_delivery_items:
            if self in obj._assets:
                obj._assets.remove(self)
            self._erp_rec_delivery_items.remove(obj)
    # >>> erp_rec_delivery_items

    # <<< reliability_infos
    # @generated
    def get_reliability_infos(self):
        """ 
        """
        return self._reliability_infos

    def set_reliability_infos(self, value):
        for p in self._reliability_infos:
            filtered = [q for q in p.assets if q != self]
            self._reliability_infos._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._reliability_infos = value

    reliability_infos = property(get_reliability_infos, set_reliability_infos)

    def add_reliability_infos(self, *reliability_infos):
        for obj in reliability_infos:
            if self not in obj._assets:
                obj._assets.append(self)
            self._reliability_infos.append(obj)

    def remove_reliability_infos(self, *reliability_infos):
        for obj in reliability_infos:
            if self in obj._assets:
                obj._assets.remove(self)
            self._reliability_infos.remove(obj)
    # >>> reliability_infos

    # <<< to_asset_roles
    # @generated
    def get_to_asset_roles(self):
        """ 
        """
        return self._to_asset_roles

    def set_to_asset_roles(self, value):
        for x in self._to_asset_roles:
            x._from_asset = None
        for y in value:
            y._from_asset = self
        self._to_asset_roles = value

    to_asset_roles = property(get_to_asset_roles, set_to_asset_roles)

    def add_to_asset_roles(self, *to_asset_roles):
        for obj in to_asset_roles:
            obj._from_asset = self
            self._to_asset_roles.append(obj)

    def remove_to_asset_roles(self, *to_asset_roles):
        for obj in to_asset_roles:
            obj._from_asset = None
            self._to_asset_roles.remove(obj)
    # >>> to_asset_roles

    # <<< asset_property_curves
    # @generated
    def get_asset_property_curves(self):
        """ 
        """
        return self._asset_property_curves

    def set_asset_property_curves(self, value):
        for p in self._asset_property_curves:
            filtered = [q for q in p.assets if q != self]
            self._asset_property_curves._assets = filtered
        for r in value:
            if self not in r._assets:
                r._assets.append(self)
        self._asset_property_curves = value

    asset_property_curves = property(get_asset_property_curves, set_asset_property_curves)

    def add_asset_property_curves(self, *asset_property_curves):
        for obj in asset_property_curves:
            if self not in obj._assets:
                obj._assets.append(self)
            self._asset_property_curves.append(obj)

    def remove_asset_property_curves(self, *asset_property_curves):
        for obj in asset_property_curves:
            if self in obj._assets:
                obj._assets.remove(self)
            self._asset_property_curves.remove(obj)
    # >>> asset_property_curves

    # <<< financial_info
    # @generated
    def get_financial_info(self):
        """ 
        """
        return self._financial_info

    def set_financial_info(self, value):
        if self._financial_info is not None:
            self._financial_info._asset = None

        self._financial_info = value
        if self._financial_info is not None:
            self._financial_info._asset = self

    financial_info = property(get_financial_info, set_financial_info)
    # >>> financial_info

    # <<< erp_inventory
    # @generated
    def get_erp_inventory(self):
        """ 
        """
        return self._erp_inventory

    def set_erp_inventory(self, value):
        if self._erp_inventory is not None:
            self._erp_inventory._asset = None

        self._erp_inventory = value
        if self._erp_inventory is not None:
            self._erp_inventory._asset = self

    erp_inventory = property(get_erp_inventory, set_erp_inventory)
    # >>> erp_inventory

    # <<< acceptance_test
    # @generated
    # Information on acceptance test.
    acceptance_test = None
    # >>> acceptance_test

    # <<< status
    # @generated
    # Status of this asset.
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Asset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Asset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Asset", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:Asset.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Asset.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Asset.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Asset.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Asset.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Asset.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_functions:
            s += '%s<%s:Asset.asset_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.properties:
            s += '%s<%s:Asset.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.asset_container is not None:
            s += '%s<%s:Asset.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        for obj in self.ratings:
            s += '%s<%s:Asset.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Asset.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_asset_roles:
            s += '%s<%s:Asset.from_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Asset.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Asset.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:Asset.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Asset.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_item_master is not None:
            s += '%s<%s:Asset.erp_item_master rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_item_master.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Asset.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:Asset.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_rec_delivery_items:
            s += '%s<%s:Asset.erp_rec_delivery_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Asset.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_asset_roles:
            s += '%s<%s:Asset.to_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Asset.asset_property_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.financial_info is not None:
            s += '%s<%s:Asset.financial_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.financial_info.uri)
        if self.erp_inventory is not None:
            s += '%s<%s:Asset.erp_inventory rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_inventory.uri)
        if self.acceptance_test is not None:
            s += '%s<%s:Asset.acceptance_test rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.acceptance_test.uri)
        if self.status is not None:
            s += '%s<%s:Asset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Asset.initial_condition>%s</%s:Asset.initial_condition>' % \
            (indent, ns_prefix, self.initial_condition, ns_prefix)
        s += '%s<%s:Asset.category>%s</%s:Asset.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Asset.lot_number>%s</%s:Asset.lot_number>' % \
            (indent, ns_prefix, self.lot_number, ns_prefix)
        s += '%s<%s:Asset.application>%s</%s:Asset.application>' % \
            (indent, ns_prefix, self.application, ns_prefix)
        s += '%s<%s:Asset.serial_number>%s</%s:Asset.serial_number>' % \
            (indent, ns_prefix, self.serial_number, ns_prefix)
        s += '%s<%s:Asset.installation_date>%s</%s:Asset.installation_date>' % \
            (indent, ns_prefix, self.installation_date, ns_prefix)
        s += '%s<%s:Asset.corporate_code>%s</%s:Asset.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Asset.purchase_price>%s</%s:Asset.purchase_price>' % \
            (indent, ns_prefix, self.purchase_price, ns_prefix)
        s += '%s<%s:Asset.manufactured_date>%s</%s:Asset.manufactured_date>' % \
            (indent, ns_prefix, self.manufactured_date, ns_prefix)
        s += '%s<%s:Asset.initial_loss_of_life>%s</%s:Asset.initial_loss_of_life>' % \
            (indent, ns_prefix, self.initial_loss_of_life, ns_prefix)
        s += '%s<%s:Asset.utc_number>%s</%s:Asset.utc_number>' % \
            (indent, ns_prefix, self.utc_number, ns_prefix)
        s += '%s<%s:Asset.critical>%s</%s:Asset.critical>' % \
            (indent, ns_prefix, self.critical, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Asset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset.serialize


class ElectricalInfo(IdentifiedObject):
    """ Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.
    """
    # <<< electrical_info
    # @generated
    def __init__(self, b=0.0, wire_count=0, r0=0.0, frequency=0.0, g=0.0, rated_voltage=0.0, x=0.0, phase_count=0, rated_current=0.0, b0=0.0, r=0.0, g0=0.0, rated_apparent_power=0.0, x0=0.0, bil=0.0, end_device_assets=None, electrical_type_assets=None, electrical_assets=None, electrical_asset_models=None, **kw_args):
        """ Initialises a new 'ElectricalInfo' instance.
        """
        # Positive sequence susceptance. 
        self.b = b

        # For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y. 
        self.wire_count = wire_count

        # Zero sequence series resistance. 
        self.r0 = r0

        # Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz. 
        self.frequency = frequency

        # Positive sequence conductance. 
        self.g = g

        # Rated voltage. 
        self.rated_voltage = rated_voltage

        # Positive sequence series reactance. 
        self.x = x

        # Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        self.phase_count = phase_count

        # Rated current. 
        self.rated_current = rated_current

        # Zero sequence susceptance. 
        self.b0 = b0

        # Positive sequence series resistance. 
        self.r = r

        # Zero sequence conductance. 
        self.g0 = g0

        # Rated apparent power. 
        self.rated_apparent_power = rated_apparent_power

        # Zero sequence series reactance. 
        self.x0 = x0

        # Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        self.bil = bil


        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []

        self._electrical_type_assets = []
        if electrical_type_assets is not None:
            self.electrical_type_assets = electrical_type_assets
        else:
            self.electrical_type_assets = []

        self._electrical_assets = []
        if electrical_assets is not None:
            self.electrical_assets = electrical_assets
        else:
            self.electrical_assets = []

        self._electrical_asset_models = []
        if electrical_asset_models is not None:
            self.electrical_asset_models = electrical_asset_models
        else:
            self.electrical_asset_models = []


        super(ElectricalInfo, self).__init__(**kw_args)
    # >>> electrical_info

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets having this set of electrical properties.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for p in self._end_device_assets:
            filtered = [q for q in p.electrical_infos if q != self]
            self._end_device_assets._electrical_infos = filtered
        for r in value:
            if self not in r._electrical_infos:
                r._electrical_infos.append(self)
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            if self not in obj._electrical_infos:
                obj._electrical_infos.append(self)
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            if self in obj._electrical_infos:
                obj._electrical_infos.remove(self)
            self._end_device_assets.remove(obj)
    # >>> end_device_assets

    # <<< electrical_type_assets
    # @generated
    def get_electrical_type_assets(self):
        """ 
        """
        return self._electrical_type_assets

    def set_electrical_type_assets(self, value):
        for p in self._electrical_type_assets:
            filtered = [q for q in p.electrical_infos if q != self]
            self._electrical_type_assets._electrical_infos = filtered
        for r in value:
            if self not in r._electrical_infos:
                r._electrical_infos.append(self)
        self._electrical_type_assets = value

    electrical_type_assets = property(get_electrical_type_assets, set_electrical_type_assets)

    def add_electrical_type_assets(self, *electrical_type_assets):
        for obj in electrical_type_assets:
            if self not in obj._electrical_infos:
                obj._electrical_infos.append(self)
            self._electrical_type_assets.append(obj)

    def remove_electrical_type_assets(self, *electrical_type_assets):
        for obj in electrical_type_assets:
            if self in obj._electrical_infos:
                obj._electrical_infos.remove(self)
            self._electrical_type_assets.remove(obj)
    # >>> electrical_type_assets

    # <<< electrical_assets
    # @generated
    def get_electrical_assets(self):
        """ 
        """
        return self._electrical_assets

    def set_electrical_assets(self, value):
        for p in self._electrical_assets:
            filtered = [q for q in p.electrical_infos if q != self]
            self._electrical_assets._electrical_infos = filtered
        for r in value:
            if self not in r._electrical_infos:
                r._electrical_infos.append(self)
        self._electrical_assets = value

    electrical_assets = property(get_electrical_assets, set_electrical_assets)

    def add_electrical_assets(self, *electrical_assets):
        for obj in electrical_assets:
            if self not in obj._electrical_infos:
                obj._electrical_infos.append(self)
            self._electrical_assets.append(obj)

    def remove_electrical_assets(self, *electrical_assets):
        for obj in electrical_assets:
            if self in obj._electrical_infos:
                obj._electrical_infos.remove(self)
            self._electrical_assets.remove(obj)
    # >>> electrical_assets

    # <<< electrical_asset_models
    # @generated
    def get_electrical_asset_models(self):
        """ 
        """
        return self._electrical_asset_models

    def set_electrical_asset_models(self, value):
        for p in self._electrical_asset_models:
            filtered = [q for q in p.electrical_infos if q != self]
            self._electrical_asset_models._electrical_infos = filtered
        for r in value:
            if self not in r._electrical_infos:
                r._electrical_infos.append(self)
        self._electrical_asset_models = value

    electrical_asset_models = property(get_electrical_asset_models, set_electrical_asset_models)

    def add_electrical_asset_models(self, *electrical_asset_models):
        for obj in electrical_asset_models:
            if self not in obj._electrical_infos:
                obj._electrical_infos.append(self)
            self._electrical_asset_models.append(obj)

    def remove_electrical_asset_models(self, *electrical_asset_models):
        for obj in electrical_asset_models:
            if self in obj._electrical_infos:
                obj._electrical_infos.remove(self)
            self._electrical_asset_models.remove(obj)
    # >>> electrical_asset_models


    def __str__(self):
        """ Returns a string representation of the ElectricalInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< electrical_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ElectricalInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ElectricalInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.end_device_assets:
            s += '%s<%s:ElectricalInfo.end_device_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electrical_type_assets:
            s += '%s<%s:ElectricalInfo.electrical_type_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electrical_assets:
            s += '%s<%s:ElectricalInfo.electrical_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electrical_asset_models:
            s += '%s<%s:ElectricalInfo.electrical_asset_models rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ElectricalInfo.b>%s</%s:ElectricalInfo.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:ElectricalInfo.wire_count>%s</%s:ElectricalInfo.wire_count>' % \
            (indent, ns_prefix, self.wire_count, ns_prefix)
        s += '%s<%s:ElectricalInfo.r0>%s</%s:ElectricalInfo.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:ElectricalInfo.frequency>%s</%s:ElectricalInfo.frequency>' % \
            (indent, ns_prefix, self.frequency, ns_prefix)
        s += '%s<%s:ElectricalInfo.g>%s</%s:ElectricalInfo.g>' % \
            (indent, ns_prefix, self.g, ns_prefix)
        s += '%s<%s:ElectricalInfo.rated_voltage>%s</%s:ElectricalInfo.rated_voltage>' % \
            (indent, ns_prefix, self.rated_voltage, ns_prefix)
        s += '%s<%s:ElectricalInfo.x>%s</%s:ElectricalInfo.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:ElectricalInfo.phase_count>%s</%s:ElectricalInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ElectricalInfo.rated_current>%s</%s:ElectricalInfo.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
        s += '%s<%s:ElectricalInfo.b0>%s</%s:ElectricalInfo.b0>' % \
            (indent, ns_prefix, self.b0, ns_prefix)
        s += '%s<%s:ElectricalInfo.r>%s</%s:ElectricalInfo.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:ElectricalInfo.g0>%s</%s:ElectricalInfo.g0>' % \
            (indent, ns_prefix, self.g0, ns_prefix)
        s += '%s<%s:ElectricalInfo.rated_apparent_power>%s</%s:ElectricalInfo.rated_apparent_power>' % \
            (indent, ns_prefix, self.rated_apparent_power, ns_prefix)
        s += '%s<%s:ElectricalInfo.x0>%s</%s:ElectricalInfo.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:ElectricalInfo.bil>%s</%s:ElectricalInfo.bil>' % \
            (indent, ns_prefix, self.bil, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ElectricalInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> electrical_info.serialize


class AcceptanceTest(Element):
    """ Acceptance test for assets.
    """
    # <<< acceptance_test
    # @generated
    def __init__(self, date_time='', success=False, type='', **kw_args):
        """ Initialises a new 'AcceptanceTest' instance.
        """
        # Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute. 
        self.date_time = date_time

        # True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime. 
        self.success = success

        # Type of test or group of tests that was conducted on 'dateTime'. 
        self.type = type



        super(AcceptanceTest, self).__init__(**kw_args)
    # >>> acceptance_test


    def __str__(self):
        """ Returns a string representation of the AcceptanceTest.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< acceptance_test.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AcceptanceTest.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AcceptanceTest", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:AcceptanceTest.date_time>%s</%s:AcceptanceTest.date_time>' % \
            (indent, ns_prefix, self.date_time, ns_prefix)
        s += '%s<%s:AcceptanceTest.success>%s</%s:AcceptanceTest.success>' % \
            (indent, ns_prefix, self.success, ns_prefix)
        s += '%s<%s:AcceptanceTest.type>%s</%s:AcceptanceTest.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AcceptanceTest")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> acceptance_test.serialize


class AssetFunction(Asset):
    """ Function performed by an asset. Often, function is a module (or a board that plugs into a backplane) that can be replaced or updated without impacting the rest of the asset. Therefore functions are treated as assets because they have life-cycles that are independent of the asset containing the function.
    """
    # <<< asset_function
    # @generated
    def __init__(self, hardware_id='', config_id='', program_id='', password='', firmware_id='', asset=None, asset_function_asset_model=None, **kw_args):
        """ Initialises a new 'AssetFunction' instance.
        """
        # Hardware version. 
        self.hardware_id = hardware_id

        # Configuration specified for this function. 
        self.config_id = config_id

        # Name of program. 
        self.program_id = program_id

        # Password needed to access this function. 
        self.password = password

        # Firmware version. 
        self.firmware_id = firmware_id


        self._asset = None
        self.asset = asset

        self._asset_function_asset_model = None
        self.asset_function_asset_model = asset_function_asset_model


        super(AssetFunction, self).__init__(**kw_args)
    # >>> asset_function

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.asset_functions if x != self]
            self._asset._asset_functions = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._asset_functions.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< asset_function_asset_model
    # @generated
    def get_asset_function_asset_model(self):
        """ 
        """
        return self._asset_function_asset_model

    def set_asset_function_asset_model(self, value):
        if self._asset_function_asset_model is not None:
            filtered = [x for x in self.asset_function_asset_model.asset_functions if x != self]
            self._asset_function_asset_model._asset_functions = filtered

        self._asset_function_asset_model = value
        if self._asset_function_asset_model is not None:
            self._asset_function_asset_model._asset_functions.append(self)

    asset_function_asset_model = property(get_asset_function_asset_model, set_asset_function_asset_model)
    # >>> asset_function_asset_model


    def __str__(self):
        """ Returns a string representation of the AssetFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetFunction", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:AssetFunction.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.asset_function_asset_model is not None:
            s += '%s<%s:AssetFunction.asset_function_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_function_asset_model.uri)
        s += '%s<%s:AssetFunction.hardware_id>%s</%s:AssetFunction.hardware_id>' % \
            (indent, ns_prefix, self.hardware_id, ns_prefix)
        s += '%s<%s:AssetFunction.config_id>%s</%s:AssetFunction.config_id>' % \
            (indent, ns_prefix, self.config_id, ns_prefix)
        s += '%s<%s:AssetFunction.program_id>%s</%s:AssetFunction.program_id>' % \
            (indent, ns_prefix, self.program_id, ns_prefix)
        s += '%s<%s:AssetFunction.password>%s</%s:AssetFunction.password>' % \
            (indent, ns_prefix, self.password, ns_prefix)
        s += '%s<%s:AssetFunction.firmware_id>%s</%s:AssetFunction.firmware_id>' % \
            (indent, ns_prefix, self.firmware_id, ns_prefix)
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
        for obj in self.measurements:
            s += '%s<%s:Asset.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Asset.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Asset.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Asset.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Asset.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Asset.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_functions:
            s += '%s<%s:Asset.asset_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.properties:
            s += '%s<%s:Asset.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.asset_container is not None:
            s += '%s<%s:Asset.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        for obj in self.ratings:
            s += '%s<%s:Asset.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Asset.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_asset_roles:
            s += '%s<%s:Asset.from_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Asset.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Asset.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:Asset.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Asset.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_item_master is not None:
            s += '%s<%s:Asset.erp_item_master rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_item_master.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Asset.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:Asset.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_rec_delivery_items:
            s += '%s<%s:Asset.erp_rec_delivery_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Asset.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_asset_roles:
            s += '%s<%s:Asset.to_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Asset.asset_property_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.financial_info is not None:
            s += '%s<%s:Asset.financial_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.financial_info.uri)
        if self.erp_inventory is not None:
            s += '%s<%s:Asset.erp_inventory rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_inventory.uri)
        if self.acceptance_test is not None:
            s += '%s<%s:Asset.acceptance_test rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.acceptance_test.uri)
        if self.status is not None:
            s += '%s<%s:Asset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Asset.initial_condition>%s</%s:Asset.initial_condition>' % \
            (indent, ns_prefix, self.initial_condition, ns_prefix)
        s += '%s<%s:Asset.category>%s</%s:Asset.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Asset.lot_number>%s</%s:Asset.lot_number>' % \
            (indent, ns_prefix, self.lot_number, ns_prefix)
        s += '%s<%s:Asset.application>%s</%s:Asset.application>' % \
            (indent, ns_prefix, self.application, ns_prefix)
        s += '%s<%s:Asset.serial_number>%s</%s:Asset.serial_number>' % \
            (indent, ns_prefix, self.serial_number, ns_prefix)
        s += '%s<%s:Asset.installation_date>%s</%s:Asset.installation_date>' % \
            (indent, ns_prefix, self.installation_date, ns_prefix)
        s += '%s<%s:Asset.corporate_code>%s</%s:Asset.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Asset.purchase_price>%s</%s:Asset.purchase_price>' % \
            (indent, ns_prefix, self.purchase_price, ns_prefix)
        s += '%s<%s:Asset.manufactured_date>%s</%s:Asset.manufactured_date>' % \
            (indent, ns_prefix, self.manufactured_date, ns_prefix)
        s += '%s<%s:Asset.initial_loss_of_life>%s</%s:Asset.initial_loss_of_life>' % \
            (indent, ns_prefix, self.initial_loss_of_life, ns_prefix)
        s += '%s<%s:Asset.utc_number>%s</%s:Asset.utc_number>' % \
            (indent, ns_prefix, self.utc_number, ns_prefix)
        s += '%s<%s:Asset.critical>%s</%s:Asset.critical>' % \
            (indent, ns_prefix, self.critical, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_function.serialize


class ComMediaAsset(Asset):
    """ Communication media such as fibre optic cable, power-line, telephone, etc.
    """
    pass
    # <<< com_media_asset
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ComMediaAsset' instance.
        """


        super(ComMediaAsset, self).__init__(**kw_args)
    # >>> com_media_asset


    def __str__(self):
        """ Returns a string representation of the ComMediaAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< com_media_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ComMediaAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ComMediaAsset", self.uri)
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
        for obj in self.measurements:
            s += '%s<%s:Asset.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Asset.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Asset.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Asset.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Asset.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Asset.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_functions:
            s += '%s<%s:Asset.asset_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.properties:
            s += '%s<%s:Asset.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.asset_container is not None:
            s += '%s<%s:Asset.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        for obj in self.ratings:
            s += '%s<%s:Asset.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Asset.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_asset_roles:
            s += '%s<%s:Asset.from_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Asset.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Asset.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:Asset.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Asset.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_item_master is not None:
            s += '%s<%s:Asset.erp_item_master rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_item_master.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Asset.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:Asset.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_rec_delivery_items:
            s += '%s<%s:Asset.erp_rec_delivery_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Asset.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_asset_roles:
            s += '%s<%s:Asset.to_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Asset.asset_property_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.financial_info is not None:
            s += '%s<%s:Asset.financial_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.financial_info.uri)
        if self.erp_inventory is not None:
            s += '%s<%s:Asset.erp_inventory rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_inventory.uri)
        if self.acceptance_test is not None:
            s += '%s<%s:Asset.acceptance_test rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.acceptance_test.uri)
        if self.status is not None:
            s += '%s<%s:Asset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Asset.initial_condition>%s</%s:Asset.initial_condition>' % \
            (indent, ns_prefix, self.initial_condition, ns_prefix)
        s += '%s<%s:Asset.category>%s</%s:Asset.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Asset.lot_number>%s</%s:Asset.lot_number>' % \
            (indent, ns_prefix, self.lot_number, ns_prefix)
        s += '%s<%s:Asset.application>%s</%s:Asset.application>' % \
            (indent, ns_prefix, self.application, ns_prefix)
        s += '%s<%s:Asset.serial_number>%s</%s:Asset.serial_number>' % \
            (indent, ns_prefix, self.serial_number, ns_prefix)
        s += '%s<%s:Asset.installation_date>%s</%s:Asset.installation_date>' % \
            (indent, ns_prefix, self.installation_date, ns_prefix)
        s += '%s<%s:Asset.corporate_code>%s</%s:Asset.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Asset.purchase_price>%s</%s:Asset.purchase_price>' % \
            (indent, ns_prefix, self.purchase_price, ns_prefix)
        s += '%s<%s:Asset.manufactured_date>%s</%s:Asset.manufactured_date>' % \
            (indent, ns_prefix, self.manufactured_date, ns_prefix)
        s += '%s<%s:Asset.initial_loss_of_life>%s</%s:Asset.initial_loss_of_life>' % \
            (indent, ns_prefix, self.initial_loss_of_life, ns_prefix)
        s += '%s<%s:Asset.utc_number>%s</%s:Asset.utc_number>' % \
            (indent, ns_prefix, self.utc_number, ns_prefix)
        s += '%s<%s:Asset.critical>%s</%s:Asset.critical>' % \
            (indent, ns_prefix, self.critical, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ComMediaAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> com_media_asset.serialize


class AssetContainer(Asset):
    """ Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """
    # <<< asset_container
    # @generated
    def __init__(self, land_properties=None, assets=None, seals=None, **kw_args):
        """ Initialises a new 'AssetContainer' instance.
        """

        self._land_properties = []
        if land_properties is not None:
            self.land_properties = land_properties
        else:
            self.land_properties = []

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._seals = []
        if seals is not None:
            self.seals = seals
        else:
            self.seals = []


        super(AssetContainer, self).__init__(**kw_args)
    # >>> asset_container

    # <<< land_properties
    # @generated
    def get_land_properties(self):
        """ 
        """
        return self._land_properties

    def set_land_properties(self, value):
        for p in self._land_properties:
            filtered = [q for q in p.asset_containers if q != self]
            self._land_properties._asset_containers = filtered
        for r in value:
            if self not in r._asset_containers:
                r._asset_containers.append(self)
        self._land_properties = value

    land_properties = property(get_land_properties, set_land_properties)

    def add_land_properties(self, *land_properties):
        for obj in land_properties:
            if self not in obj._asset_containers:
                obj._asset_containers.append(self)
            self._land_properties.append(obj)

    def remove_land_properties(self, *land_properties):
        for obj in land_properties:
            if self in obj._asset_containers:
                obj._asset_containers.remove(self)
            self._land_properties.remove(obj)
    # >>> land_properties

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for x in self._assets:
            x._asset_container = None
        for y in value:
            y._asset_container = self
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            obj._asset_container = self
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            obj._asset_container = None
            self._assets.remove(obj)
    # >>> assets

    # <<< seals
    # @generated
    def get_seals(self):
        """ All seals applied to this asset container.
        """
        return self._seals

    def set_seals(self, value):
        for x in self._seals:
            x._asset_container = None
        for y in value:
            y._asset_container = self
        self._seals = value

    seals = property(get_seals, set_seals)

    def add_seals(self, *seals):
        for obj in seals:
            obj._asset_container = self
            self._seals.append(obj)

    def remove_seals(self, *seals):
        for obj in seals:
            obj._asset_container = None
            self._seals.remove(obj)
    # >>> seals


    def __str__(self):
        """ Returns a string representation of the AssetContainer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_container.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetContainer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetContainer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
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
        for obj in self.measurements:
            s += '%s<%s:Asset.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Asset.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Asset.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Asset.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Asset.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Asset.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_functions:
            s += '%s<%s:Asset.asset_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.properties:
            s += '%s<%s:Asset.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.asset_container is not None:
            s += '%s<%s:Asset.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        for obj in self.ratings:
            s += '%s<%s:Asset.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Asset.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_asset_roles:
            s += '%s<%s:Asset.from_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Asset.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Asset.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:Asset.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Asset.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_item_master is not None:
            s += '%s<%s:Asset.erp_item_master rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_item_master.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Asset.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:Asset.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_rec_delivery_items:
            s += '%s<%s:Asset.erp_rec_delivery_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Asset.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_asset_roles:
            s += '%s<%s:Asset.to_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Asset.asset_property_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.financial_info is not None:
            s += '%s<%s:Asset.financial_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.financial_info.uri)
        if self.erp_inventory is not None:
            s += '%s<%s:Asset.erp_inventory rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_inventory.uri)
        if self.acceptance_test is not None:
            s += '%s<%s:Asset.acceptance_test rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.acceptance_test.uri)
        if self.status is not None:
            s += '%s<%s:Asset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Asset.initial_condition>%s</%s:Asset.initial_condition>' % \
            (indent, ns_prefix, self.initial_condition, ns_prefix)
        s += '%s<%s:Asset.category>%s</%s:Asset.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Asset.lot_number>%s</%s:Asset.lot_number>' % \
            (indent, ns_prefix, self.lot_number, ns_prefix)
        s += '%s<%s:Asset.application>%s</%s:Asset.application>' % \
            (indent, ns_prefix, self.application, ns_prefix)
        s += '%s<%s:Asset.serial_number>%s</%s:Asset.serial_number>' % \
            (indent, ns_prefix, self.serial_number, ns_prefix)
        s += '%s<%s:Asset.installation_date>%s</%s:Asset.installation_date>' % \
            (indent, ns_prefix, self.installation_date, ns_prefix)
        s += '%s<%s:Asset.corporate_code>%s</%s:Asset.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Asset.purchase_price>%s</%s:Asset.purchase_price>' % \
            (indent, ns_prefix, self.purchase_price, ns_prefix)
        s += '%s<%s:Asset.manufactured_date>%s</%s:Asset.manufactured_date>' % \
            (indent, ns_prefix, self.manufactured_date, ns_prefix)
        s += '%s<%s:Asset.initial_loss_of_life>%s</%s:Asset.initial_loss_of_life>' % \
            (indent, ns_prefix, self.initial_loss_of_life, ns_prefix)
        s += '%s<%s:Asset.utc_number>%s</%s:Asset.utc_number>' % \
            (indent, ns_prefix, self.utc_number, ns_prefix)
        s += '%s<%s:Asset.critical>%s</%s:Asset.critical>' % \
            (indent, ns_prefix, self.critical, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_container.serialize


# <<< assets
# @generated
# >>> assets
