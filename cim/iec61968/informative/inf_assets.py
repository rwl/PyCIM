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

""" The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a PowerSystemResource in the Wires model.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful to operations which are constructed from one or more Assets, although PowerSystemResources are not required to specifiy their component Assets. The Asset package is comprosed of several packages. The key concepts of an Asset are as follows: <ul> 	<li>Assets can have names, through inheritance to the Naming package</li> 	<li>Assets are physical entities which have a lifecycle</li> 	<li>One or more assets can be associated to create a PowerSystemResource</li> 	<li>Assets can be grouped (aggregated) with other Assets</li> 	<li>Assets are typically either 'point' or 'linear' assets, which relate to physical geometry</li> 	<li>Assets have a close relationship to Work as a consequence of their lifecycle</li> </ul> The following sections describe the packages in the Assets package. The AssetBasics package defines the relationship between Asset and other classes, such as Organization, PowerSystemResource and Document. Point assets are those assets whose physical location can be described in terms of a single coordinate, such as a pole or a switch. Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon. Asset work triggers are used to determine when inspection and/or maintenance are required for assets.'
"""

from cim.iec61968.common import ActivityRecord
from cim.iec61968.assets import Asset
from cim.iec61968.assets import ElectricalInfo
from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Document
from cim.iec61968.assets import AssetContainer
from cim.iec61968.informative.inf_common import Role
from cim.iec61970.core import Curve

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infassets"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfAssets"

class FailureEvent(ActivityRecord):
    """ An event where an asset has failed to perform its functions within specified parameters.
    """
    # <<< failure_event
    # @generated
    def __init__(self, failure_isolation_method='manually_isolated', corporate_code='', fault_locating_method='', location='', **kw_args):
        """ Initialises a new 'FailureEvent' instance.
        """
        # How the asset failure was isolated from the system. Values are: "manually_isolated", "burned_in_the_clear", "fuse", "other", "breaker_operation"
        self.failure_isolation_method = 'manually_isolated'

        # Code for asset failure. 
        self.corporate_code = corporate_code

        # The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other. 
        self.fault_locating_method = fault_locating_method

        # Failure location on an object. 
        self.location = location



        super(FailureEvent, self).__init__(**kw_args)
    # >>> failure_event


    def __str__(self):
        """ Returns a string representation of the FailureEvent.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< failure_event.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FailureEvent.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FailureEvent", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:FailureEvent.failure_isolation_method>%s</%s:FailureEvent.failure_isolation_method>' % \
            (indent, ns_prefix, self.failure_isolation_method, ns_prefix)
        s += '%s<%s:FailureEvent.corporate_code>%s</%s:FailureEvent.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:FailureEvent.fault_locating_method>%s</%s:FailureEvent.fault_locating_method>' % \
            (indent, ns_prefix, self.fault_locating_method, ns_prefix)
        s += '%s<%s:FailureEvent.location>%s</%s:FailureEvent.location>' % \
            (indent, ns_prefix, self.location, ns_prefix)
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
        for obj in self.market_factors:
            s += '%s<%s:ActivityRecord.market_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.documents:
            s += '%s<%s:ActivityRecord.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.organisations:
            s += '%s<%s:ActivityRecord.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.scheduled_event is not None:
            s += '%s<%s:ActivityRecord.scheduled_event rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.scheduled_event.uri)
        for obj in self.assets:
            s += '%s<%s:ActivityRecord.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_persons:
            s += '%s<%s:ActivityRecord.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:ActivityRecord.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ActivityRecord.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ActivityRecord.reason>%s</%s:ActivityRecord.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:ActivityRecord.category>%s</%s:ActivityRecord.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:ActivityRecord.severity>%s</%s:ActivityRecord.severity>' % \
            (indent, ns_prefix, self.severity, ns_prefix)
        s += '%s<%s:ActivityRecord.created_date_time>%s</%s:ActivityRecord.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FailureEvent")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> failure_event.serialize


class ElectricalAsset(Asset):
    """ An asset that has (or can have) a role in the electrical network.
    """
    # <<< electrical_asset
    # @generated
    def __init__(self, phase_code='abc', is_connected=False, electrical_infos=None, conducting_equipment=None, **kw_args):
        """ Initialises a new 'ElectricalAsset' instance.
        """
        # If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with. Values are: "abc", "ab", "b", "bc", "ac", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.phase_code = 'abc'

        # True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used. 
        self.is_connected = is_connected


        self._electrical_infos = []
        if electrical_infos is not None:
            self.electrical_infos = electrical_infos
        else:
            self.electrical_infos = []

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment


        super(ElectricalAsset, self).__init__(**kw_args)
    # >>> electrical_asset

    # <<< electrical_infos
    # @generated
    def get_electrical_infos(self):
        """ 
        """
        return self._electrical_infos

    def set_electrical_infos(self, value):
        for p in self._electrical_infos:
            filtered = [q for q in p.electrical_assets if q != self]
            self._electrical_infos._electrical_assets = filtered
        for r in value:
            if self not in r._electrical_assets:
                r._electrical_assets.append(self)
        self._electrical_infos = value

    electrical_infos = property(get_electrical_infos, set_electrical_infos)

    def add_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self not in obj._electrical_assets:
                obj._electrical_assets.append(self)
            self._electrical_infos.append(obj)

    def remove_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self in obj._electrical_assets:
                obj._electrical_assets.remove(self)
            self._electrical_infos.remove(obj)
    # >>> electrical_infos

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ 
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            filtered = [x for x in self.conducting_equipment.electrical_assets if x != self]
            self._conducting_equipment._electrical_assets = filtered

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._electrical_assets.append(self)

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment


    def __str__(self):
        """ Returns a string representation of the ElectricalAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< electrical_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ElectricalAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ElectricalAsset", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ElectricalAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> electrical_asset.serialize


class SwitchInfo(ElectricalInfo):
    """ Properties of a switch.
    """
    # <<< switch_info
    # @generated
    def __init__(self, making_capacity=0.0, pole_count=0, interrupting_rating=0.0, withstand_current=0.0, minimum_current=0.0, load_break=False, gang=False, dielectric_strength=0.0, remote=False, switch_assets=None, switch_asset_model=None, switch_type_asset=None, **kw_args):
        """ Initialises a new 'SwitchInfo' instance.
        """
        # The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.making_capacity = making_capacity

        # Number of poles (i.e. of current carrying conductors that are switched). 
        self.pole_count = pole_count

        # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        self.interrupting_rating = interrupting_rating

        # The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.withstand_current = withstand_current

        # The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.minimum_current = minimum_current

        # True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers. 
        self.load_break = load_break

        # True if multi-phase switch controls all phases concurrently. 
        self.gang = gang

        # The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position. 
        self.dielectric_strength = dielectric_strength

        # True if device is capable of being operated by remote control. 
        self.remote = remote


        self._switch_assets = []
        if switch_assets is not None:
            self.switch_assets = switch_assets
        else:
            self.switch_assets = []

        self._switch_asset_model = None
        self.switch_asset_model = switch_asset_model

        self._switch_type_asset = None
        self.switch_type_asset = switch_type_asset


        super(SwitchInfo, self).__init__(**kw_args)
    # >>> switch_info

    # <<< switch_assets
    # @generated
    def get_switch_assets(self):
        """ 
        """
        return self._switch_assets

    def set_switch_assets(self, value):
        for x in self._switch_assets:
            x._switch_info = None
        for y in value:
            y._switch_info = self
        self._switch_assets = value

    switch_assets = property(get_switch_assets, set_switch_assets)

    def add_switch_assets(self, *switch_assets):
        for obj in switch_assets:
            obj._switch_info = self
            self._switch_assets.append(obj)

    def remove_switch_assets(self, *switch_assets):
        for obj in switch_assets:
            obj._switch_info = None
            self._switch_assets.remove(obj)
    # >>> switch_assets

    # <<< switch_asset_model
    # @generated
    def get_switch_asset_model(self):
        """ 
        """
        return self._switch_asset_model

    def set_switch_asset_model(self, value):
        if self._switch_asset_model is not None:
            self._switch_asset_model._switch_info = None

        self._switch_asset_model = value
        if self._switch_asset_model is not None:
            self._switch_asset_model._switch_info = self

    switch_asset_model = property(get_switch_asset_model, set_switch_asset_model)
    # >>> switch_asset_model

    # <<< switch_type_asset
    # @generated
    def get_switch_type_asset(self):
        """ 
        """
        return self._switch_type_asset

    def set_switch_type_asset(self, value):
        if self._switch_type_asset is not None:
            self._switch_type_asset._switch_info = None

        self._switch_type_asset = value
        if self._switch_type_asset is not None:
            self._switch_type_asset._switch_info = self

    switch_type_asset = property(get_switch_type_asset, set_switch_type_asset)
    # >>> switch_type_asset


    def __str__(self):
        """ Returns a string representation of the SwitchInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switch_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SwitchInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SwitchInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.switch_assets:
            s += '%s<%s:SwitchInfo.switch_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.switch_asset_model is not None:
            s += '%s<%s:SwitchInfo.switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_asset_model.uri)
        if self.switch_type_asset is not None:
            s += '%s<%s:SwitchInfo.switch_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_type_asset.uri)
        s += '%s<%s:SwitchInfo.making_capacity>%s</%s:SwitchInfo.making_capacity>' % \
            (indent, ns_prefix, self.making_capacity, ns_prefix)
        s += '%s<%s:SwitchInfo.pole_count>%s</%s:SwitchInfo.pole_count>' % \
            (indent, ns_prefix, self.pole_count, ns_prefix)
        s += '%s<%s:SwitchInfo.interrupting_rating>%s</%s:SwitchInfo.interrupting_rating>' % \
            (indent, ns_prefix, self.interrupting_rating, ns_prefix)
        s += '%s<%s:SwitchInfo.withstand_current>%s</%s:SwitchInfo.withstand_current>' % \
            (indent, ns_prefix, self.withstand_current, ns_prefix)
        s += '%s<%s:SwitchInfo.minimum_current>%s</%s:SwitchInfo.minimum_current>' % \
            (indent, ns_prefix, self.minimum_current, ns_prefix)
        s += '%s<%s:SwitchInfo.load_break>%s</%s:SwitchInfo.load_break>' % \
            (indent, ns_prefix, self.load_break, ns_prefix)
        s += '%s<%s:SwitchInfo.gang>%s</%s:SwitchInfo.gang>' % \
            (indent, ns_prefix, self.gang, ns_prefix)
        s += '%s<%s:SwitchInfo.dielectric_strength>%s</%s:SwitchInfo.dielectric_strength>' % \
            (indent, ns_prefix, self.dielectric_strength, ns_prefix)
        s += '%s<%s:SwitchInfo.remote>%s</%s:SwitchInfo.remote>' % \
            (indent, ns_prefix, self.remote, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SwitchInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switch_info.serialize


class PowerRating(IdentifiedObject):
    """ There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.
    """
    # <<< power_rating
    # @generated
    def __init__(self, cooling_kind='other', power_rating=0.0, stage=0, transformer_assets=None, **kw_args):
        """ Initialises a new 'PowerRating' instance.
        """
        # Kind of cooling system. Values are: "other", "forced_air", "forced_oil_and_air", "self_cooling"
        self.cooling_kind = 'other'

        # The power rating associated with type of cooling specified for this stage. 
        self.power_rating = power_rating

        # Stage of cooling and associated power rating. 
        self.stage = stage


        self._transformer_assets = []
        if transformer_assets is not None:
            self.transformer_assets = transformer_assets
        else:
            self.transformer_assets = []


        super(PowerRating, self).__init__(**kw_args)
    # >>> power_rating

    # <<< transformer_assets
    # @generated
    def get_transformer_assets(self):
        """ 
        """
        return self._transformer_assets

    def set_transformer_assets(self, value):
        for p in self._transformer_assets:
            filtered = [q for q in p.power_ratings if q != self]
            self._transformer_assets._power_ratings = filtered
        for r in value:
            if self not in r._power_ratings:
                r._power_ratings.append(self)
        self._transformer_assets = value

    transformer_assets = property(get_transformer_assets, set_transformer_assets)

    def add_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            if self not in obj._power_ratings:
                obj._power_ratings.append(self)
            self._transformer_assets.append(obj)

    def remove_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            if self in obj._power_ratings:
                obj._power_ratings.remove(self)
            self._transformer_assets.remove(obj)
    # >>> transformer_assets


    def __str__(self):
        """ Returns a string representation of the PowerRating.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_rating.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerRating.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerRating", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.transformer_assets:
            s += '%s<%s:PowerRating.transformer_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PowerRating.cooling_kind>%s</%s:PowerRating.cooling_kind>' % \
            (indent, ns_prefix, self.cooling_kind, ns_prefix)
        s += '%s<%s:PowerRating.power_rating>%s</%s:PowerRating.power_rating>' % \
            (indent, ns_prefix, self.power_rating, ns_prefix)
        s += '%s<%s:PowerRating.stage>%s</%s:PowerRating.stage>' % \
            (indent, ns_prefix, self.stage, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerRating")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_rating.serialize


class StructureSupport(Asset):
    """ Support for Structures.
    """
    # <<< structure_support
    # @generated
    def __init__(self, length=0.0, direction=0.0, size='', rod_length=0.0, rod_count=0, secured_structure=None, **kw_args):
        """ Initialises a new 'StructureSupport' instance.
        """
        # Length of anchor lead or guy. 
        self.length = length

        # Direction of supporting anchor or guy. 
        self.direction = direction

        # Size of anchor or guy. 
        self.size = size

        # Length of rod used for an anchor. 
        self.rod_length = rod_length

        # Number of rods used for an anchor. 
        self.rod_count = rod_count


        self._secured_structure = None
        self.secured_structure = secured_structure


        super(StructureSupport, self).__init__(**kw_args)
    # >>> structure_support

    # <<< secured_structure
    # @generated
    def get_secured_structure(self):
        """ 
        """
        return self._secured_structure

    def set_secured_structure(self, value):
        if self._secured_structure is not None:
            filtered = [x for x in self.secured_structure.structure_supports if x != self]
            self._secured_structure._structure_supports = filtered

        self._secured_structure = value
        if self._secured_structure is not None:
            self._secured_structure._structure_supports.append(self)

    secured_structure = property(get_secured_structure, set_secured_structure)
    # >>> secured_structure


    def __str__(self):
        """ Returns a string representation of the StructureSupport.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< structure_support.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StructureSupport.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StructureSupport", self.uri)
        if format:
            indent += ' ' * depth

        if self.secured_structure is not None:
            s += '%s<%s:StructureSupport.secured_structure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secured_structure.uri)
        s += '%s<%s:StructureSupport.length>%s</%s:StructureSupport.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:StructureSupport.direction>%s</%s:StructureSupport.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:StructureSupport.size>%s</%s:StructureSupport.size>' % \
            (indent, ns_prefix, self.size, ns_prefix)
        s += '%s<%s:StructureSupport.rod_length>%s</%s:StructureSupport.rod_length>' % \
            (indent, ns_prefix, self.rod_length, ns_prefix)
        s += '%s<%s:StructureSupport.rod_count>%s</%s:StructureSupport.rod_count>' % \
            (indent, ns_prefix, self.rod_count, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "StructureSupport")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> structure_support.serialize


class CurrentTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of Current Transformer (CT) or a CT Model.
    """
    # <<< current_transformer_info
    # @generated
    def __init__(self, tertiary_fls_rating=0.0, secondary_fls_rating=0.0, primary_fls_rating=0.0, current_transformer_type_asset=None, secondary_ratio=None, current_transformer_assets=None, current_transformer_assert_models=None, primary_ratio=None, tertiary_ratio=None, **kw_args):
        """ Initialises a new 'CurrentTransformerInfo' instance.
        """
        # Full load secondary (FLS) rating for tertiary winding. 
        self.tertiary_fls_rating = tertiary_fls_rating

        # Full load secondary (FLS) rating for secondary winding. 
        self.secondary_fls_rating = secondary_fls_rating

        # Full load secondary (FLS) rating for primary winding. 
        self.primary_fls_rating = primary_fls_rating


        self._current_transformer_type_asset = None
        self.current_transformer_type_asset = current_transformer_type_asset

        self.secondary_ratio = secondary_ratio

        self._current_transformer_assets = []
        if current_transformer_assets is not None:
            self.current_transformer_assets = current_transformer_assets
        else:
            self.current_transformer_assets = []

        self._current_transformer_assert_models = []
        if current_transformer_assert_models is not None:
            self.current_transformer_assert_models = current_transformer_assert_models
        else:
            self.current_transformer_assert_models = []

        self.primary_ratio = primary_ratio

        self.tertiary_ratio = tertiary_ratio


        super(CurrentTransformerInfo, self).__init__(**kw_args)
    # >>> current_transformer_info

    # <<< current_transformer_type_asset
    # @generated
    def get_current_transformer_type_asset(self):
        """ 
        """
        return self._current_transformer_type_asset

    def set_current_transformer_type_asset(self, value):
        if self._current_transformer_type_asset is not None:
            self._current_transformer_type_asset._current_transformer_info = None

        self._current_transformer_type_asset = value
        if self._current_transformer_type_asset is not None:
            self._current_transformer_type_asset._current_transformer_info = self

    current_transformer_type_asset = property(get_current_transformer_type_asset, set_current_transformer_type_asset)
    # >>> current_transformer_type_asset

    # <<< secondary_ratio
    # @generated
    # Ratio for the secondary winding tap changer.
    secondary_ratio = None
    # >>> secondary_ratio

    # <<< current_transformer_assets
    # @generated
    def get_current_transformer_assets(self):
        """ 
        """
        return self._current_transformer_assets

    def set_current_transformer_assets(self, value):
        for x in self._current_transformer_assets:
            x._current_transformer_info = None
        for y in value:
            y._current_transformer_info = self
        self._current_transformer_assets = value

    current_transformer_assets = property(get_current_transformer_assets, set_current_transformer_assets)

    def add_current_transformer_assets(self, *current_transformer_assets):
        for obj in current_transformer_assets:
            obj._current_transformer_info = self
            self._current_transformer_assets.append(obj)

    def remove_current_transformer_assets(self, *current_transformer_assets):
        for obj in current_transformer_assets:
            obj._current_transformer_info = None
            self._current_transformer_assets.remove(obj)
    # >>> current_transformer_assets

    # <<< current_transformer_assert_models
    # @generated
    def get_current_transformer_assert_models(self):
        """ 
        """
        return self._current_transformer_assert_models

    def set_current_transformer_assert_models(self, value):
        for x in self._current_transformer_assert_models:
            x._current_transformer_info = None
        for y in value:
            y._current_transformer_info = self
        self._current_transformer_assert_models = value

    current_transformer_assert_models = property(get_current_transformer_assert_models, set_current_transformer_assert_models)

    def add_current_transformer_assert_models(self, *current_transformer_assert_models):
        for obj in current_transformer_assert_models:
            obj._current_transformer_info = self
            self._current_transformer_assert_models.append(obj)

    def remove_current_transformer_assert_models(self, *current_transformer_assert_models):
        for obj in current_transformer_assert_models:
            obj._current_transformer_info = None
            self._current_transformer_assert_models.remove(obj)
    # >>> current_transformer_assert_models

    # <<< primary_ratio
    # @generated
    # Ratio for the primary winding tap changer.
    primary_ratio = None
    # >>> primary_ratio

    # <<< tertiary_ratio
    # @generated
    # Ratio for the tertiary winding tap changer.
    tertiary_ratio = None
    # >>> tertiary_ratio


    def __str__(self):
        """ Returns a string representation of the CurrentTransformerInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_transformer_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentTransformerInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentTransformerInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.current_transformer_type_asset is not None:
            s += '%s<%s:CurrentTransformerInfo.current_transformer_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer_type_asset.uri)
        if self.secondary_ratio is not None:
            s += '%s<%s:CurrentTransformerInfo.secondary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_ratio.uri)
        for obj in self.current_transformer_assets:
            s += '%s<%s:CurrentTransformerInfo.current_transformer_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.current_transformer_assert_models:
            s += '%s<%s:CurrentTransformerInfo.current_transformer_assert_models rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.primary_ratio is not None:
            s += '%s<%s:CurrentTransformerInfo.primary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.primary_ratio.uri)
        if self.tertiary_ratio is not None:
            s += '%s<%s:CurrentTransformerInfo.tertiary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tertiary_ratio.uri)
        s += '%s<%s:CurrentTransformerInfo.tertiary_fls_rating>%s</%s:CurrentTransformerInfo.tertiary_fls_rating>' % \
            (indent, ns_prefix, self.tertiary_fls_rating, ns_prefix)
        s += '%s<%s:CurrentTransformerInfo.secondary_fls_rating>%s</%s:CurrentTransformerInfo.secondary_fls_rating>' % \
            (indent, ns_prefix, self.secondary_fls_rating, ns_prefix)
        s += '%s<%s:CurrentTransformerInfo.primary_fls_rating>%s</%s:CurrentTransformerInfo.primary_fls_rating>' % \
            (indent, ns_prefix, self.primary_fls_rating, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentTransformerInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_transformer_info.serialize


class ConductorAsset(Asset):
    """ Physical asset used to perform the conductor's role.
    """
    # <<< conductor_asset
    # @generated
    def __init__(self, grounding_method='', is_horizontal=False, insulated=False, circuit_section=None, conductor_asset_model=None, conductor_segment=None, **kw_args):
        """ Initialises a new 'ConductorAsset' instance.
        """
        # Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other. 
        self.grounding_method = grounding_method

        # True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service). 
        self.is_horizontal = is_horizontal

        # True if conductor asset has an insulator around the core material. 
        self.insulated = insulated


        self._circuit_section = None
        self.circuit_section = circuit_section

        self._conductor_asset_model = None
        self.conductor_asset_model = conductor_asset_model

        self._conductor_segment = None
        self.conductor_segment = conductor_segment


        super(ConductorAsset, self).__init__(**kw_args)
    # >>> conductor_asset

    # <<< circuit_section
    # @generated
    def get_circuit_section(self):
        """ 
        """
        return self._circuit_section

    def set_circuit_section(self, value):
        if self._circuit_section is not None:
            filtered = [x for x in self.circuit_section.conductor_assets if x != self]
            self._circuit_section._conductor_assets = filtered

        self._circuit_section = value
        if self._circuit_section is not None:
            self._circuit_section._conductor_assets.append(self)

    circuit_section = property(get_circuit_section, set_circuit_section)
    # >>> circuit_section

    # <<< conductor_asset_model
    # @generated
    def get_conductor_asset_model(self):
        """ 
        """
        return self._conductor_asset_model

    def set_conductor_asset_model(self, value):
        if self._conductor_asset_model is not None:
            filtered = [x for x in self.conductor_asset_model.conductor_assets if x != self]
            self._conductor_asset_model._conductor_assets = filtered

        self._conductor_asset_model = value
        if self._conductor_asset_model is not None:
            self._conductor_asset_model._conductor_assets.append(self)

    conductor_asset_model = property(get_conductor_asset_model, set_conductor_asset_model)
    # >>> conductor_asset_model

    # <<< conductor_segment
    # @generated
    def get_conductor_segment(self):
        """ 
        """
        return self._conductor_segment

    def set_conductor_segment(self, value):
        if self._conductor_segment is not None:
            filtered = [x for x in self.conductor_segment.conductor_assets if x != self]
            self._conductor_segment._conductor_assets = filtered

        self._conductor_segment = value
        if self._conductor_segment is not None:
            self._conductor_segment._conductor_assets.append(self)

    conductor_segment = property(get_conductor_segment, set_conductor_segment)
    # >>> conductor_segment


    def __str__(self):
        """ Returns a string representation of the ConductorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conductor_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConductorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConductorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.circuit_section is not None:
            s += '%s<%s:ConductorAsset.circuit_section rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.circuit_section.uri)
        if self.conductor_asset_model is not None:
            s += '%s<%s:ConductorAsset.conductor_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_asset_model.uri)
        if self.conductor_segment is not None:
            s += '%s<%s:ConductorAsset.conductor_segment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_segment.uri)
        s += '%s<%s:ConductorAsset.grounding_method>%s</%s:ConductorAsset.grounding_method>' % \
            (indent, ns_prefix, self.grounding_method, ns_prefix)
        s += '%s<%s:ConductorAsset.is_horizontal>%s</%s:ConductorAsset.is_horizontal>' % \
            (indent, ns_prefix, self.is_horizontal, ns_prefix)
        s += '%s<%s:ConductorAsset.insulated>%s</%s:ConductorAsset.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConductorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conductor_asset.serialize


class Medium(IdentifiedObject):
    """ A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.
    """
    # <<< medium
    # @generated
    def __init__(self, kind='solid', volume_spec=0.0, assets=None, specification=None, **kw_args):
        """ Initialises a new 'Medium' instance.
        """
        # Kind of this medium. Values are: "solid", "gas", "liquid"
        self.kind = 'solid'

        # The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset. 
        self.volume_spec = volume_spec


        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._specification = None
        self.specification = specification


        super(Medium, self).__init__(**kw_args)
    # >>> medium

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.mediums if q != self]
            self._assets._mediums = filtered
        for r in value:
            if self not in r._mediums:
                r._mediums.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._mediums:
                obj._mediums.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._mediums:
                obj._mediums.remove(self)
            self._assets.remove(obj)
    # >>> assets

    # <<< specification
    # @generated
    def get_specification(self):
        """ 
        """
        return self._specification

    def set_specification(self, value):
        if self._specification is not None:
            filtered = [x for x in self.specification.mediums if x != self]
            self._specification._mediums = filtered

        self._specification = value
        if self._specification is not None:
            self._specification._mediums.append(self)

    specification = property(get_specification, set_specification)
    # >>> specification


    def __str__(self):
        """ Returns a string representation of the Medium.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< medium.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Medium.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Medium", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.assets:
            s += '%s<%s:Medium.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.specification is not None:
            s += '%s<%s:Medium.specification rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.specification.uri)
        s += '%s<%s:Medium.kind>%s</%s:Medium.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Medium.volume_spec>%s</%s:Medium.volume_spec>' % \
            (indent, ns_prefix, self.volume_spec, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Medium")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> medium.serialize


class ProcedureDataSet(Document):
    """ A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.
    """
    # <<< procedure_data_set
    # @generated
    def __init__(self, completed_date_time='', procedure=None, properties=None, measurement_values=None, transformer_observations=None, **kw_args):
        """ Initialises a new 'ProcedureDataSet' instance.
        """
        # Date and time procedure was completed. 
        self.completed_date_time = completed_date_time


        self._procedure = None
        self.procedure = procedure

        self._properties = []
        if properties is not None:
            self.properties = properties
        else:
            self.properties = []

        self._measurement_values = []
        if measurement_values is not None:
            self.measurement_values = measurement_values
        else:
            self.measurement_values = []

        self._transformer_observations = []
        if transformer_observations is not None:
            self.transformer_observations = transformer_observations
        else:
            self.transformer_observations = []


        super(ProcedureDataSet, self).__init__(**kw_args)
    # >>> procedure_data_set

    # <<< procedure
    # @generated
    def get_procedure(self):
        """ 
        """
        return self._procedure

    def set_procedure(self, value):
        if self._procedure is not None:
            filtered = [x for x in self.procedure.procedure_data_sets if x != self]
            self._procedure._procedure_data_sets = filtered

        self._procedure = value
        if self._procedure is not None:
            self._procedure._procedure_data_sets.append(self)

    procedure = property(get_procedure, set_procedure)
    # >>> procedure

    # <<< properties
    # @generated
    def get_properties(self):
        """ UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._properties

    def set_properties(self, value):
        for p in self._properties:
            filtered = [q for q in p.procedure_data_sets if q != self]
            self._properties._procedure_data_sets = filtered
        for r in value:
            if self not in r._procedure_data_sets:
                r._procedure_data_sets.append(self)
        self._properties = value

    properties = property(get_properties, set_properties)

    def add_properties(self, *properties):
        for obj in properties:
            if self not in obj._procedure_data_sets:
                obj._procedure_data_sets.append(self)
            self._properties.append(obj)

    def remove_properties(self, *properties):
        for obj in properties:
            if self in obj._procedure_data_sets:
                obj._procedure_data_sets.remove(self)
            self._properties.remove(obj)
    # >>> properties

    # <<< measurement_values
    # @generated
    def get_measurement_values(self):
        """ 
        """
        return self._measurement_values

    def set_measurement_values(self, value):
        for p in self._measurement_values:
            filtered = [q for q in p.procedure_data_sets if q != self]
            self._measurement_values._procedure_data_sets = filtered
        for r in value:
            if self not in r._procedure_data_sets:
                r._procedure_data_sets.append(self)
        self._measurement_values = value

    measurement_values = property(get_measurement_values, set_measurement_values)

    def add_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            if self not in obj._procedure_data_sets:
                obj._procedure_data_sets.append(self)
            self._measurement_values.append(obj)

    def remove_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            if self in obj._procedure_data_sets:
                obj._procedure_data_sets.remove(self)
            self._measurement_values.remove(obj)
    # >>> measurement_values

    # <<< transformer_observations
    # @generated
    def get_transformer_observations(self):
        """ 
        """
        return self._transformer_observations

    def set_transformer_observations(self, value):
        for p in self._transformer_observations:
            filtered = [q for q in p.procedure_data_sets if q != self]
            self._transformer_observations._procedure_data_sets = filtered
        for r in value:
            if self not in r._procedure_data_sets:
                r._procedure_data_sets.append(self)
        self._transformer_observations = value

    transformer_observations = property(get_transformer_observations, set_transformer_observations)

    def add_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            if self not in obj._procedure_data_sets:
                obj._procedure_data_sets.append(self)
            self._transformer_observations.append(obj)

    def remove_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            if self in obj._procedure_data_sets:
                obj._procedure_data_sets.remove(self)
            self._transformer_observations.remove(obj)
    # >>> transformer_observations


    def __str__(self):
        """ Returns a string representation of the ProcedureDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< procedure_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProcedureDataSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProcedureDataSet", self.uri)
        if format:
            indent += ' ' * depth

        if self.procedure is not None:
            s += '%s<%s:ProcedureDataSet.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.properties:
            s += '%s<%s:ProcedureDataSet.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ProcedureDataSet.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:ProcedureDataSet.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProcedureDataSet.completed_date_time>%s</%s:ProcedureDataSet.completed_date_time>' % \
            (indent, ns_prefix, self.completed_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProcedureDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> procedure_data_set.serialize


class Vehicle(Asset):
    """ A vehicle is a type of utility asset.
    """
    # <<< vehicle
    # @generated
    def __init__(self, usage_kind='contractor', odometer_reading=0.0, odometer_read_date_time='', crew=None, vehicle_asset_model=None, **kw_args):
        """ Initialises a new 'Vehicle' instance.
        """
        # The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations. Values are: "contractor", "other", "crew", "user"
        self.usage_kind = 'contractor'

        # Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings. 
        self.odometer_reading = odometer_reading

        # Date and time the last odometer reading was recorded. 
        self.odometer_read_date_time = odometer_read_date_time


        self._crew = None
        self.crew = crew

        self._vehicle_asset_model = None
        self.vehicle_asset_model = vehicle_asset_model


        super(Vehicle, self).__init__(**kw_args)
    # >>> vehicle

    # <<< crew
    # @generated
    def get_crew(self):
        """ 
        """
        return self._crew

    def set_crew(self, value):
        if self._crew is not None:
            filtered = [x for x in self.crew.vehicles if x != self]
            self._crew._vehicles = filtered

        self._crew = value
        if self._crew is not None:
            self._crew._vehicles.append(self)

    crew = property(get_crew, set_crew)
    # >>> crew

    # <<< vehicle_asset_model
    # @generated
    def get_vehicle_asset_model(self):
        """ 
        """
        return self._vehicle_asset_model

    def set_vehicle_asset_model(self, value):
        if self._vehicle_asset_model is not None:
            filtered = [x for x in self.vehicle_asset_model.vehicles if x != self]
            self._vehicle_asset_model._vehicles = filtered

        self._vehicle_asset_model = value
        if self._vehicle_asset_model is not None:
            self._vehicle_asset_model._vehicles.append(self)

    vehicle_asset_model = property(get_vehicle_asset_model, set_vehicle_asset_model)
    # >>> vehicle_asset_model


    def __str__(self):
        """ Returns a string representation of the Vehicle.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< vehicle.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Vehicle.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Vehicle", self.uri)
        if format:
            indent += ' ' * depth

        if self.crew is not None:
            s += '%s<%s:Vehicle.crew rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.crew.uri)
        if self.vehicle_asset_model is not None:
            s += '%s<%s:Vehicle.vehicle_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.vehicle_asset_model.uri)
        s += '%s<%s:Vehicle.usage_kind>%s</%s:Vehicle.usage_kind>' % \
            (indent, ns_prefix, self.usage_kind, ns_prefix)
        s += '%s<%s:Vehicle.odometer_reading>%s</%s:Vehicle.odometer_reading>' % \
            (indent, ns_prefix, self.odometer_reading, ns_prefix)
        s += '%s<%s:Vehicle.odometer_read_date_time>%s</%s:Vehicle.odometer_read_date_time>' % \
            (indent, ns_prefix, self.odometer_read_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Vehicle")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> vehicle.serialize


class WorkEquipmentAsset(Asset):
    """ Various equipment used to perform units of work by crews, office staff, etc.
    """
    # <<< work_equipment_asset
    # @generated
    def __init__(self, work_equipment_asset_model=None, crew=None, usages=None, **kw_args):
        """ Initialises a new 'WorkEquipmentAsset' instance.
        """

        self._work_equipment_asset_model = None
        self.work_equipment_asset_model = work_equipment_asset_model

        self._crew = None
        self.crew = crew

        self._usages = []
        if usages is not None:
            self.usages = usages
        else:
            self.usages = []


        super(WorkEquipmentAsset, self).__init__(**kw_args)
    # >>> work_equipment_asset

    # <<< work_equipment_asset_model
    # @generated
    def get_work_equipment_asset_model(self):
        """ 
        """
        return self._work_equipment_asset_model

    def set_work_equipment_asset_model(self, value):
        if self._work_equipment_asset_model is not None:
            filtered = [x for x in self.work_equipment_asset_model.work_equipment_assets if x != self]
            self._work_equipment_asset_model._work_equipment_assets = filtered

        self._work_equipment_asset_model = value
        if self._work_equipment_asset_model is not None:
            self._work_equipment_asset_model._work_equipment_assets.append(self)

    work_equipment_asset_model = property(get_work_equipment_asset_model, set_work_equipment_asset_model)
    # >>> work_equipment_asset_model

    # <<< crew
    # @generated
    def get_crew(self):
        """ 
        """
        return self._crew

    def set_crew(self, value):
        if self._crew is not None:
            filtered = [x for x in self.crew.work_equipment_assets if x != self]
            self._crew._work_equipment_assets = filtered

        self._crew = value
        if self._crew is not None:
            self._crew._work_equipment_assets.append(self)

    crew = property(get_crew, set_crew)
    # >>> crew

    # <<< usages
    # @generated
    def get_usages(self):
        """ 
        """
        return self._usages

    def set_usages(self, value):
        for x in self._usages:
            x._work_equipment_asset = None
        for y in value:
            y._work_equipment_asset = self
        self._usages = value

    usages = property(get_usages, set_usages)

    def add_usages(self, *usages):
        for obj in usages:
            obj._work_equipment_asset = self
            self._usages.append(obj)

    def remove_usages(self, *usages):
        for obj in usages:
            obj._work_equipment_asset = None
            self._usages.remove(obj)
    # >>> usages


    def __str__(self):
        """ Returns a string representation of the WorkEquipmentAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_equipment_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkEquipmentAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkEquipmentAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_equipment_asset_model is not None:
            s += '%s<%s:WorkEquipmentAsset.work_equipment_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_equipment_asset_model.uri)
        if self.crew is not None:
            s += '%s<%s:WorkEquipmentAsset.crew rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.crew.uri)
        for obj in self.usages:
            s += '%s<%s:WorkEquipmentAsset.usages rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkEquipmentAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_equipment_asset.serialize


class Tool(Asset):
    """ Utility asset typically used by utility resources like crews and persons. As is the case for other assets, tools must be maintained.
    """
    # <<< tool
    # @generated
    def __init__(self, last_calibration_date='', tool_asset_model=None, crew=None, **kw_args):
        """ Initialises a new 'Tool' instance.
        """
        # Date the tool was last caibrated, if applicable. 
        self.last_calibration_date = last_calibration_date


        self._tool_asset_model = None
        self.tool_asset_model = tool_asset_model

        self._crew = None
        self.crew = crew


        super(Tool, self).__init__(**kw_args)
    # >>> tool

    # <<< tool_asset_model
    # @generated
    def get_tool_asset_model(self):
        """ 
        """
        return self._tool_asset_model

    def set_tool_asset_model(self, value):
        if self._tool_asset_model is not None:
            filtered = [x for x in self.tool_asset_model.tools if x != self]
            self._tool_asset_model._tools = filtered

        self._tool_asset_model = value
        if self._tool_asset_model is not None:
            self._tool_asset_model._tools.append(self)

    tool_asset_model = property(get_tool_asset_model, set_tool_asset_model)
    # >>> tool_asset_model

    # <<< crew
    # @generated
    def get_crew(self):
        """ 
        """
        return self._crew

    def set_crew(self, value):
        if self._crew is not None:
            filtered = [x for x in self.crew.tools if x != self]
            self._crew._tools = filtered

        self._crew = value
        if self._crew is not None:
            self._crew._tools.append(self)

    crew = property(get_crew, set_crew)
    # >>> crew


    def __str__(self):
        """ Returns a string representation of the Tool.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tool.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Tool.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Tool", self.uri)
        if format:
            indent += ' ' * depth

        if self.tool_asset_model is not None:
            s += '%s<%s:Tool.tool_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tool_asset_model.uri)
        if self.crew is not None:
            s += '%s<%s:Tool.crew rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.crew.uri)
        s += '%s<%s:Tool.last_calibration_date>%s</%s:Tool.last_calibration_date>' % \
            (indent, ns_prefix, self.last_calibration_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Tool")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tool.serialize


class TransformerAsset(Asset):
    """ A specific physical (vs. logical) transformer.
    """
    # <<< transformer_asset
    # @generated
    def __init__(self, reconditioned_date_time='', transformer_info=None, power_ratings=None, transformer_observations=None, transformer_asset_model=None, **kw_args):
        """ Initialises a new 'TransformerAsset' instance.
        """
        # Date and time this asset was last reconditioned or had a major overhaul. 
        self.reconditioned_date_time = reconditioned_date_time


        self._transformer_info = None
        self.transformer_info = transformer_info

        self._power_ratings = []
        if power_ratings is not None:
            self.power_ratings = power_ratings
        else:
            self.power_ratings = []

        self._transformer_observations = []
        if transformer_observations is not None:
            self.transformer_observations = transformer_observations
        else:
            self.transformer_observations = []

        self._transformer_asset_model = None
        self.transformer_asset_model = transformer_asset_model


        super(TransformerAsset, self).__init__(**kw_args)
    # >>> transformer_asset

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ 
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.transformer_assets if x != self]
            self._transformer_info._transformer_assets = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._transformer_assets.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info

    # <<< power_ratings
    # @generated
    def get_power_ratings(self):
        """ 
        """
        return self._power_ratings

    def set_power_ratings(self, value):
        for p in self._power_ratings:
            filtered = [q for q in p.transformer_assets if q != self]
            self._power_ratings._transformer_assets = filtered
        for r in value:
            if self not in r._transformer_assets:
                r._transformer_assets.append(self)
        self._power_ratings = value

    power_ratings = property(get_power_ratings, set_power_ratings)

    def add_power_ratings(self, *power_ratings):
        for obj in power_ratings:
            if self not in obj._transformer_assets:
                obj._transformer_assets.append(self)
            self._power_ratings.append(obj)

    def remove_power_ratings(self, *power_ratings):
        for obj in power_ratings:
            if self in obj._transformer_assets:
                obj._transformer_assets.remove(self)
            self._power_ratings.remove(obj)
    # >>> power_ratings

    # <<< transformer_observations
    # @generated
    def get_transformer_observations(self):
        """ 
        """
        return self._transformer_observations

    def set_transformer_observations(self, value):
        for x in self._transformer_observations:
            x._transformer_asset = None
        for y in value:
            y._transformer_asset = self
        self._transformer_observations = value

    transformer_observations = property(get_transformer_observations, set_transformer_observations)

    def add_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            obj._transformer_asset = self
            self._transformer_observations.append(obj)

    def remove_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            obj._transformer_asset = None
            self._transformer_observations.remove(obj)
    # >>> transformer_observations

    # <<< transformer_asset_model
    # @generated
    def get_transformer_asset_model(self):
        """ 
        """
        return self._transformer_asset_model

    def set_transformer_asset_model(self, value):
        if self._transformer_asset_model is not None:
            filtered = [x for x in self.transformer_asset_model.transformer_assets if x != self]
            self._transformer_asset_model._transformer_assets = filtered

        self._transformer_asset_model = value
        if self._transformer_asset_model is not None:
            self._transformer_asset_model._transformer_assets.append(self)

    transformer_asset_model = property(get_transformer_asset_model, set_transformer_asset_model)
    # >>> transformer_asset_model


    def __str__(self):
        """ Returns a string representation of the TransformerAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.transformer_info is not None:
            s += '%s<%s:TransformerAsset.transformer_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_info.uri)
        for obj in self.power_ratings:
            s += '%s<%s:TransformerAsset.power_ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:TransformerAsset.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transformer_asset_model is not None:
            s += '%s<%s:TransformerAsset.transformer_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_asset_model.uri)
        s += '%s<%s:TransformerAsset.reconditioned_date_time>%s</%s:TransformerAsset.reconditioned_date_time>' % \
            (indent, ns_prefix, self.reconditioned_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_asset.serialize


class Facility(AssetContainer):
    """ A facility may contain buildings, storage facilities, switching facilities, power generation, manufacturing facilities, maintenance facilities, etc.
    """
    # <<< facility
    # @generated
    def __init__(self, kind='', **kw_args):
        """ Initialises a new 'Facility' instance.
        """
        # Kind of this facility. 
        self.kind = kind



        super(Facility, self).__init__(**kw_args)
    # >>> facility


    def __str__(self):
        """ Returns a string representation of the Facility.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< facility.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Facility.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Facility", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Facility.kind>%s</%s:Facility.kind>' % \
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Facility")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> facility.serialize


class Structure(AssetContainer):
    """ Construction holding assets such as conductors, transformers, switchgear, etc.
    """
    # <<< structure
    # @generated
    def __init__(self, material_kind='concrete', height=0.0, remove_weed=False, weed_removed_date='', fumigant_applied_date='', fumigant_name='', structure_supports=None, **kw_args):
        """ Initialises a new 'Structure' instance.
        """
        # Material this structure is made of. Values are: "concrete", "wood", "other", "steel"
        self.material_kind = 'concrete'

        # Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions. 
        self.height = height

        # True if weeds are to be removed around asset. 
        self.remove_weed = remove_weed

        # Date weed were last removed. 
        self.weed_removed_date = weed_removed_date

        # Date fumigant was last applied. 
        self.fumigant_applied_date = fumigant_applied_date

        # Name of fumigant. 
        self.fumigant_name = fumigant_name


        self._structure_supports = []
        if structure_supports is not None:
            self.structure_supports = structure_supports
        else:
            self.structure_supports = []


        super(Structure, self).__init__(**kw_args)
    # >>> structure

    # <<< structure_supports
    # @generated
    def get_structure_supports(self):
        """ 
        """
        return self._structure_supports

    def set_structure_supports(self, value):
        for x in self._structure_supports:
            x._secured_structure = None
        for y in value:
            y._secured_structure = self
        self._structure_supports = value

    structure_supports = property(get_structure_supports, set_structure_supports)

    def add_structure_supports(self, *structure_supports):
        for obj in structure_supports:
            obj._secured_structure = self
            self._structure_supports.append(obj)

    def remove_structure_supports(self, *structure_supports):
        for obj in structure_supports:
            obj._secured_structure = None
            self._structure_supports.remove(obj)
    # >>> structure_supports


    def __str__(self):
        """ Returns a string representation of the Structure.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< structure.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Structure.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Structure", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.structure_supports:
            s += '%s<%s:Structure.structure_supports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Structure.material_kind>%s</%s:Structure.material_kind>' % \
            (indent, ns_prefix, self.material_kind, ns_prefix)
        s += '%s<%s:Structure.height>%s</%s:Structure.height>' % \
            (indent, ns_prefix, self.height, ns_prefix)
        s += '%s<%s:Structure.remove_weed>%s</%s:Structure.remove_weed>' % \
            (indent, ns_prefix, self.remove_weed, ns_prefix)
        s += '%s<%s:Structure.weed_removed_date>%s</%s:Structure.weed_removed_date>' % \
            (indent, ns_prefix, self.weed_removed_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_applied_date>%s</%s:Structure.fumigant_applied_date>' % \
            (indent, ns_prefix, self.fumigant_applied_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_name>%s</%s:Structure.fumigant_name>' % \
            (indent, ns_prefix, self.fumigant_name, ns_prefix)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Structure")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> structure.serialize


class AssetAssetRole(Role):
    """ Roles played between Assets and other Assets.
    """
    # <<< asset_asset_role
    # @generated
    def __init__(self, to_asset=None, from_asset=None, **kw_args):
        """ Initialises a new 'AssetAssetRole' instance.
        """

        self._to_asset = None
        self.to_asset = to_asset

        self._from_asset = None
        self.from_asset = from_asset


        super(AssetAssetRole, self).__init__(**kw_args)
    # >>> asset_asset_role

    # <<< to_asset
    # @generated
    def get_to_asset(self):
        """ 
        """
        return self._to_asset

    def set_to_asset(self, value):
        if self._to_asset is not None:
            filtered = [x for x in self.to_asset.from_asset_roles if x != self]
            self._to_asset._from_asset_roles = filtered

        self._to_asset = value
        if self._to_asset is not None:
            self._to_asset._from_asset_roles.append(self)

    to_asset = property(get_to_asset, set_to_asset)
    # >>> to_asset

    # <<< from_asset
    # @generated
    def get_from_asset(self):
        """ 
        """
        return self._from_asset

    def set_from_asset(self, value):
        if self._from_asset is not None:
            filtered = [x for x in self.from_asset.to_asset_roles if x != self]
            self._from_asset._to_asset_roles = filtered

        self._from_asset = value
        if self._from_asset is not None:
            self._from_asset._to_asset_roles.append(self)

    from_asset = property(get_from_asset, set_from_asset)
    # >>> from_asset


    def __str__(self):
        """ Returns a string representation of the AssetAssetRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_asset_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetAssetRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetAssetRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.to_asset is not None:
            s += '%s<%s:AssetAssetRole.to_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.to_asset.uri)
        if self.from_asset is not None:
            s += '%s<%s:AssetAssetRole.from_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_asset.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetAssetRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_asset_role.serialize


class WindingInsulation(IdentifiedObject):
    """ Winding insulation condition as a result of a test.
    """
    # <<< winding_insulation
    # @generated
    def __init__(self, insulation_pfstatus='', leakage_reactance=0.0, insulation_resistance='', from_winding=None, ground=None, transformer_observation=None, status=None, to_winding=None, **kw_args):
        """ Initialises a new 'WindingInsulation' instance.
        """
        # Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed. 
        self.insulation_pfstatus = insulation_pfstatus

        # As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited. 
        self.leakage_reactance = leakage_reactance

        # For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed. 
        self.insulation_resistance = insulation_resistance


        self._from_winding = None
        self.from_winding = from_winding

        self._ground = None
        self.ground = ground

        self._transformer_observation = None
        self.transformer_observation = transformer_observation

        self.status = status

        self._to_winding = None
        self.to_winding = to_winding


        super(WindingInsulation, self).__init__(**kw_args)
    # >>> winding_insulation

    # <<< from_winding
    # @generated
    def get_from_winding(self):
        """ 
        """
        return self._from_winding

    def set_from_winding(self, value):
        if self._from_winding is not None:
            filtered = [x for x in self.from_winding.from_winding_insulations if x != self]
            self._from_winding._from_winding_insulations = filtered

        self._from_winding = value
        if self._from_winding is not None:
            self._from_winding._from_winding_insulations.append(self)

    from_winding = property(get_from_winding, set_from_winding)
    # >>> from_winding

    # <<< ground
    # @generated
    def get_ground(self):
        """ 
        """
        return self._ground

    def set_ground(self, value):
        if self._ground is not None:
            filtered = [x for x in self.ground.winding_insulations if x != self]
            self._ground._winding_insulations = filtered

        self._ground = value
        if self._ground is not None:
            self._ground._winding_insulations.append(self)

    ground = property(get_ground, set_ground)
    # >>> ground

    # <<< transformer_observation
    # @generated
    def get_transformer_observation(self):
        """ 
        """
        return self._transformer_observation

    def set_transformer_observation(self, value):
        if self._transformer_observation is not None:
            filtered = [x for x in self.transformer_observation.winding_insulation_pfs if x != self]
            self._transformer_observation._winding_insulation_pfs = filtered

        self._transformer_observation = value
        if self._transformer_observation is not None:
            self._transformer_observation._winding_insulation_pfs.append(self)

    transformer_observation = property(get_transformer_observation, set_transformer_observation)
    # >>> transformer_observation

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< to_winding
    # @generated
    def get_to_winding(self):
        """ 
        """
        return self._to_winding

    def set_to_winding(self, value):
        if self._to_winding is not None:
            filtered = [x for x in self.to_winding.to_winding_insulations if x != self]
            self._to_winding._to_winding_insulations = filtered

        self._to_winding = value
        if self._to_winding is not None:
            self._to_winding._to_winding_insulations.append(self)

    to_winding = property(get_to_winding, set_to_winding)
    # >>> to_winding


    def __str__(self):
        """ Returns a string representation of the WindingInsulation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< winding_insulation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WindingInsulation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WindingInsulation", self.uri)
        if format:
            indent += ' ' * depth

        if self.from_winding is not None:
            s += '%s<%s:WindingInsulation.from_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_winding.uri)
        if self.ground is not None:
            s += '%s<%s:WindingInsulation.ground rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.ground.uri)
        if self.transformer_observation is not None:
            s += '%s<%s:WindingInsulation.transformer_observation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_observation.uri)
        if self.status is not None:
            s += '%s<%s:WindingInsulation.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.to_winding is not None:
            s += '%s<%s:WindingInsulation.to_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.to_winding.uri)
        s += '%s<%s:WindingInsulation.insulation_pfstatus>%s</%s:WindingInsulation.insulation_pfstatus>' % \
            (indent, ns_prefix, self.insulation_pfstatus, ns_prefix)
        s += '%s<%s:WindingInsulation.leakage_reactance>%s</%s:WindingInsulation.leakage_reactance>' % \
            (indent, ns_prefix, self.leakage_reactance, ns_prefix)
        s += '%s<%s:WindingInsulation.insulation_resistance>%s</%s:WindingInsulation.insulation_resistance>' % \
            (indent, ns_prefix, self.insulation_resistance, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WindingInsulation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> winding_insulation.serialize


class TransformerObservation(IdentifiedObject):
    """ Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.
    """
    # <<< transformer_observation
    # @generated
    def __init__(self, oil_neutralization_number='', top_oil_temp=0.0, dga='', pump_vibration='', oil_color='', oil_ift='', oil_dielectric_strength=0.0, hot_spot_temp=0.0, oil_level='', water_content='', bushing_temp=0.0, furfural_dp='', freq_resp='', status=None, winding_insulation_pfs=None, transformer_asset=None, transformer=None, bushing_insultation_pfs=None, procedure_data_sets=None, **kw_args):
        """ Initialises a new 'TransformerObservation' instance.
        """
        # Oil Quality Analysis-Neutralization Number - Number - Mg KOH. 
        self.oil_neutralization_number = oil_neutralization_number

        # Top oil temperature. 
        self.top_oil_temp = top_oil_temp

        # Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing. 
        self.dga = dga

        # Pump vibration, with typical values being: nominal, high. 
        self.pump_vibration = pump_vibration

        # Oil Quality Analysis-Color. 
        self.oil_color = oil_color

        # Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM. 
        self.oil_ift = oil_ift

        # Oil Quality Analysis-Dielectric Strength. 
        self.oil_dielectric_strength = oil_dielectric_strength

        # Hotspot oil temperature. 
        self.hot_spot_temp = hot_spot_temp

        # The level of oil in the transformer. 
        self.oil_level = oil_level

        # Water Content expressed in parts per million. 
        self.water_content = water_content

        # Bushing temperature. 
        self.bushing_temp = bushing_temp

        # Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million. 
        self.furfural_dp = furfural_dp

        # Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet. 
        self.freq_resp = freq_resp


        self.status = status

        self._winding_insulation_pfs = []
        if winding_insulation_pfs is not None:
            self.winding_insulation_pfs = winding_insulation_pfs
        else:
            self.winding_insulation_pfs = []

        self._transformer_asset = None
        self.transformer_asset = transformer_asset

        self._transformer = None
        self.transformer = transformer

        self._bushing_insultation_pfs = []
        if bushing_insultation_pfs is not None:
            self.bushing_insultation_pfs = bushing_insultation_pfs
        else:
            self.bushing_insultation_pfs = []

        self._procedure_data_sets = []
        if procedure_data_sets is not None:
            self.procedure_data_sets = procedure_data_sets
        else:
            self.procedure_data_sets = []


        super(TransformerObservation, self).__init__(**kw_args)
    # >>> transformer_observation

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< winding_insulation_pfs
    # @generated
    def get_winding_insulation_pfs(self):
        """ 
        """
        return self._winding_insulation_pfs

    def set_winding_insulation_pfs(self, value):
        for x in self._winding_insulation_pfs:
            x._transformer_observation = None
        for y in value:
            y._transformer_observation = self
        self._winding_insulation_pfs = value

    winding_insulation_pfs = property(get_winding_insulation_pfs, set_winding_insulation_pfs)

    def add_winding_insulation_pfs(self, *winding_insulation_pfs):
        for obj in winding_insulation_pfs:
            obj._transformer_observation = self
            self._winding_insulation_pfs.append(obj)

    def remove_winding_insulation_pfs(self, *winding_insulation_pfs):
        for obj in winding_insulation_pfs:
            obj._transformer_observation = None
            self._winding_insulation_pfs.remove(obj)
    # >>> winding_insulation_pfs

    # <<< transformer_asset
    # @generated
    def get_transformer_asset(self):
        """ 
        """
        return self._transformer_asset

    def set_transformer_asset(self, value):
        if self._transformer_asset is not None:
            filtered = [x for x in self.transformer_asset.transformer_observations if x != self]
            self._transformer_asset._transformer_observations = filtered

        self._transformer_asset = value
        if self._transformer_asset is not None:
            self._transformer_asset._transformer_observations.append(self)

    transformer_asset = property(get_transformer_asset, set_transformer_asset)
    # >>> transformer_asset

    # <<< transformer
    # @generated
    def get_transformer(self):
        """ 
        """
        return self._transformer

    def set_transformer(self, value):
        if self._transformer is not None:
            filtered = [x for x in self.transformer.transformer_observations if x != self]
            self._transformer._transformer_observations = filtered

        self._transformer = value
        if self._transformer is not None:
            self._transformer._transformer_observations.append(self)

    transformer = property(get_transformer, set_transformer)
    # >>> transformer

    # <<< bushing_insultation_pfs
    # @generated
    def get_bushing_insultation_pfs(self):
        """ 
        """
        return self._bushing_insultation_pfs

    def set_bushing_insultation_pfs(self, value):
        for x in self._bushing_insultation_pfs:
            x._transformer_observation = None
        for y in value:
            y._transformer_observation = self
        self._bushing_insultation_pfs = value

    bushing_insultation_pfs = property(get_bushing_insultation_pfs, set_bushing_insultation_pfs)

    def add_bushing_insultation_pfs(self, *bushing_insultation_pfs):
        for obj in bushing_insultation_pfs:
            obj._transformer_observation = self
            self._bushing_insultation_pfs.append(obj)

    def remove_bushing_insultation_pfs(self, *bushing_insultation_pfs):
        for obj in bushing_insultation_pfs:
            obj._transformer_observation = None
            self._bushing_insultation_pfs.remove(obj)
    # >>> bushing_insultation_pfs

    # <<< procedure_data_sets
    # @generated
    def get_procedure_data_sets(self):
        """ 
        """
        return self._procedure_data_sets

    def set_procedure_data_sets(self, value):
        for p in self._procedure_data_sets:
            filtered = [q for q in p.transformer_observations if q != self]
            self._procedure_data_sets._transformer_observations = filtered
        for r in value:
            if self not in r._transformer_observations:
                r._transformer_observations.append(self)
        self._procedure_data_sets = value

    procedure_data_sets = property(get_procedure_data_sets, set_procedure_data_sets)

    def add_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self not in obj._transformer_observations:
                obj._transformer_observations.append(self)
            self._procedure_data_sets.append(obj)

    def remove_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self in obj._transformer_observations:
                obj._transformer_observations.remove(self)
            self._procedure_data_sets.remove(obj)
    # >>> procedure_data_sets


    def __str__(self):
        """ Returns a string representation of the TransformerObservation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_observation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerObservation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerObservation", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:TransformerObservation.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.winding_insulation_pfs:
            s += '%s<%s:TransformerObservation.winding_insulation_pfs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transformer_asset is not None:
            s += '%s<%s:TransformerObservation.transformer_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_asset.uri)
        if self.transformer is not None:
            s += '%s<%s:TransformerObservation.transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer.uri)
        for obj in self.bushing_insultation_pfs:
            s += '%s<%s:TransformerObservation.bushing_insultation_pfs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:TransformerObservation.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:TransformerObservation.oil_neutralization_number>%s</%s:TransformerObservation.oil_neutralization_number>' % \
            (indent, ns_prefix, self.oil_neutralization_number, ns_prefix)
        s += '%s<%s:TransformerObservation.top_oil_temp>%s</%s:TransformerObservation.top_oil_temp>' % \
            (indent, ns_prefix, self.top_oil_temp, ns_prefix)
        s += '%s<%s:TransformerObservation.dga>%s</%s:TransformerObservation.dga>' % \
            (indent, ns_prefix, self.dga, ns_prefix)
        s += '%s<%s:TransformerObservation.pump_vibration>%s</%s:TransformerObservation.pump_vibration>' % \
            (indent, ns_prefix, self.pump_vibration, ns_prefix)
        s += '%s<%s:TransformerObservation.oil_color>%s</%s:TransformerObservation.oil_color>' % \
            (indent, ns_prefix, self.oil_color, ns_prefix)
        s += '%s<%s:TransformerObservation.oil_ift>%s</%s:TransformerObservation.oil_ift>' % \
            (indent, ns_prefix, self.oil_ift, ns_prefix)
        s += '%s<%s:TransformerObservation.oil_dielectric_strength>%s</%s:TransformerObservation.oil_dielectric_strength>' % \
            (indent, ns_prefix, self.oil_dielectric_strength, ns_prefix)
        s += '%s<%s:TransformerObservation.hot_spot_temp>%s</%s:TransformerObservation.hot_spot_temp>' % \
            (indent, ns_prefix, self.hot_spot_temp, ns_prefix)
        s += '%s<%s:TransformerObservation.oil_level>%s</%s:TransformerObservation.oil_level>' % \
            (indent, ns_prefix, self.oil_level, ns_prefix)
        s += '%s<%s:TransformerObservation.water_content>%s</%s:TransformerObservation.water_content>' % \
            (indent, ns_prefix, self.water_content, ns_prefix)
        s += '%s<%s:TransformerObservation.bushing_temp>%s</%s:TransformerObservation.bushing_temp>' % \
            (indent, ns_prefix, self.bushing_temp, ns_prefix)
        s += '%s<%s:TransformerObservation.furfural_dp>%s</%s:TransformerObservation.furfural_dp>' % \
            (indent, ns_prefix, self.furfural_dp, ns_prefix)
        s += '%s<%s:TransformerObservation.freq_resp>%s</%s:TransformerObservation.freq_resp>' % \
            (indent, ns_prefix, self.freq_resp, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerObservation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_observation.serialize


class CompositeSwitchInfo(IdentifiedObject):
    """ Properties of a composite switch.
    """
    # <<< composite_switch_info
    # @generated
    def __init__(self, phase_code='abc', rated_voltage=0.0, phase_count=0, remote=False, init_op_mode='', gang=False, switch_state_count=0, interrupting_rating=0.0, composite_switch_asset_model=None, composite_switch_assets=None, composite_switch_type_asset=None, **kw_args):
        """ Initialises a new 'CompositeSwitchInfo' instance.
        """
        # Phases carried, if applicable. Values are: "abc", "ab", "b", "bc", "ac", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.phase_code = 'abc'

        # Rated voltage. 
        self.rated_voltage = rated_voltage

        # Supported number of phases, typically 0, 1 or 3. 
        self.phase_count = phase_count

        # True if device is capable of being operated by remote control. 
        self.remote = remote

        # Initial operating mode, with the following values: Automatic, Manual. 
        self.init_op_mode = init_op_mode

        # True if multi-phase switch controls all phases concurrently. 
        self.gang = gang

        # Number of switch states represented by the composite switch. 
        self.switch_state_count = switch_state_count

        # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        self.interrupting_rating = interrupting_rating


        self._composite_switch_asset_model = None
        self.composite_switch_asset_model = composite_switch_asset_model

        self._composite_switch_assets = []
        if composite_switch_assets is not None:
            self.composite_switch_assets = composite_switch_assets
        else:
            self.composite_switch_assets = []

        self._composite_switch_type_asset = None
        self.composite_switch_type_asset = composite_switch_type_asset


        super(CompositeSwitchInfo, self).__init__(**kw_args)
    # >>> composite_switch_info

    # <<< composite_switch_asset_model
    # @generated
    def get_composite_switch_asset_model(self):
        """ 
        """
        return self._composite_switch_asset_model

    def set_composite_switch_asset_model(self, value):
        if self._composite_switch_asset_model is not None:
            self._composite_switch_asset_model._composite_switch_info = None

        self._composite_switch_asset_model = value
        if self._composite_switch_asset_model is not None:
            self._composite_switch_asset_model._composite_switch_info = self

    composite_switch_asset_model = property(get_composite_switch_asset_model, set_composite_switch_asset_model)
    # >>> composite_switch_asset_model

    # <<< composite_switch_assets
    # @generated
    def get_composite_switch_assets(self):
        """ 
        """
        return self._composite_switch_assets

    def set_composite_switch_assets(self, value):
        for x in self._composite_switch_assets:
            x._composite_switch_info = None
        for y in value:
            y._composite_switch_info = self
        self._composite_switch_assets = value

    composite_switch_assets = property(get_composite_switch_assets, set_composite_switch_assets)

    def add_composite_switch_assets(self, *composite_switch_assets):
        for obj in composite_switch_assets:
            obj._composite_switch_info = self
            self._composite_switch_assets.append(obj)

    def remove_composite_switch_assets(self, *composite_switch_assets):
        for obj in composite_switch_assets:
            obj._composite_switch_info = None
            self._composite_switch_assets.remove(obj)
    # >>> composite_switch_assets

    # <<< composite_switch_type_asset
    # @generated
    def get_composite_switch_type_asset(self):
        """ 
        """
        return self._composite_switch_type_asset

    def set_composite_switch_type_asset(self, value):
        if self._composite_switch_type_asset is not None:
            self._composite_switch_type_asset._composite_switch_info = None

        self._composite_switch_type_asset = value
        if self._composite_switch_type_asset is not None:
            self._composite_switch_type_asset._composite_switch_info = self

    composite_switch_type_asset = property(get_composite_switch_type_asset, set_composite_switch_type_asset)
    # >>> composite_switch_type_asset


    def __str__(self):
        """ Returns a string representation of the CompositeSwitchInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< composite_switch_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CompositeSwitchInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CompositeSwitchInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.composite_switch_asset_model is not None:
            s += '%s<%s:CompositeSwitchInfo.composite_switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.composite_switch_asset_model.uri)
        for obj in self.composite_switch_assets:
            s += '%s<%s:CompositeSwitchInfo.composite_switch_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.composite_switch_type_asset is not None:
            s += '%s<%s:CompositeSwitchInfo.composite_switch_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.composite_switch_type_asset.uri)
        s += '%s<%s:CompositeSwitchInfo.phase_code>%s</%s:CompositeSwitchInfo.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.rated_voltage>%s</%s:CompositeSwitchInfo.rated_voltage>' % \
            (indent, ns_prefix, self.rated_voltage, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.phase_count>%s</%s:CompositeSwitchInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.remote>%s</%s:CompositeSwitchInfo.remote>' % \
            (indent, ns_prefix, self.remote, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.init_op_mode>%s</%s:CompositeSwitchInfo.init_op_mode>' % \
            (indent, ns_prefix, self.init_op_mode, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.gang>%s</%s:CompositeSwitchInfo.gang>' % \
            (indent, ns_prefix, self.gang, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.switch_state_count>%s</%s:CompositeSwitchInfo.switch_state_count>' % \
            (indent, ns_prefix, self.switch_state_count, ns_prefix)
        s += '%s<%s:CompositeSwitchInfo.interrupting_rating>%s</%s:CompositeSwitchInfo.interrupting_rating>' % \
            (indent, ns_prefix, self.interrupting_rating, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CompositeSwitchInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> composite_switch_info.serialize


class ShuntImpedanceInfo(ElectricalInfo):
    """ Properties of a shunt impedance.
    """
    # <<< shunt_impedance_info
    # @generated
    def __init__(self, control_kind='fixed', sensing_phase_code='abc', reg_branch_kind='transformer', local_control_kind='none', reg_branch='', low_voltage_override=0.0, switch_operation_cycle=0.0, high_voltage_override=0.0, local_override=False, reg_branch_end=0, local_off_level='', branch_direct=0, normal_open=False, cell_size=0.0, local_on_level='', max_switch_operation_count=0, v_reg_line_line=False, shunt_compensator_type_asset=None, shunt_compensator_asset_model=None, shunt_compensator_assets=None, **kw_args):
        """ Initialises a new 'ShuntImpedanceInfo' instance.
        """
        # Kind of control (if any). Values are: "fixed", "remote_with_local_override", "remote_only", "local_only"
        self.control_kind = 'fixed'

        # Phases that are measured for controlling the device. Values are: "abc", "ab", "b", "bc", "ac", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.sensing_phase_code = 'abc'

        # (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch. Values are: "transformer", "line", "fuse", "sectionner", "other", "breaker", "switch", "recloser"
        self.reg_branch_kind = 'transformer'

        # Kind of local controller. Values are: "none", "current", "reactive_power", "time", "temperature", "voltage", "power_factor"
        self.local_control_kind = 'none'

        # For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch. 
        self.reg_branch = reg_branch

        # For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings. 
        self.low_voltage_override = low_voltage_override

        # Time interval between consecutive switching operations. 
        self.switch_operation_cycle = switch_operation_cycle

        # For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings. 
        self.high_voltage_override = high_voltage_override

        # True if the locally controlled capacitor has voltage override capability. 
        self.local_override = local_override

        # For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer). 
        self.reg_branch_end = reg_branch_end

        # Upper control setting. 
        self.local_off_level = local_off_level

        # For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out. 
        self.branch_direct = branch_direct

        # True if open is normal status for a fixed capacitor bank, otherwise normal status is closed. 
        self.normal_open = normal_open

        # The size of the individual units that make up the bank. 
        self.cell_size = cell_size

        # Lower control setting. 
        self.local_on_level = local_on_level

        # IdmsShuntImpedanceData.maxNumSwitchOps 
        self.max_switch_operation_count = max_switch_operation_count

        # True if regulated voltages are measured line to line, otherwise they are measured line to ground. 
        self.v_reg_line_line = v_reg_line_line


        self._shunt_compensator_type_asset = None
        self.shunt_compensator_type_asset = shunt_compensator_type_asset

        self._shunt_compensator_asset_model = None
        self.shunt_compensator_asset_model = shunt_compensator_asset_model

        self._shunt_compensator_assets = []
        if shunt_compensator_assets is not None:
            self.shunt_compensator_assets = shunt_compensator_assets
        else:
            self.shunt_compensator_assets = []


        super(ShuntImpedanceInfo, self).__init__(**kw_args)
    # >>> shunt_impedance_info

    # <<< shunt_compensator_type_asset
    # @generated
    def get_shunt_compensator_type_asset(self):
        """ 
        """
        return self._shunt_compensator_type_asset

    def set_shunt_compensator_type_asset(self, value):
        if self._shunt_compensator_type_asset is not None:
            self._shunt_compensator_type_asset._shunt_impedance_info = None

        self._shunt_compensator_type_asset = value
        if self._shunt_compensator_type_asset is not None:
            self._shunt_compensator_type_asset._shunt_impedance_info = self

    shunt_compensator_type_asset = property(get_shunt_compensator_type_asset, set_shunt_compensator_type_asset)
    # >>> shunt_compensator_type_asset

    # <<< shunt_compensator_asset_model
    # @generated
    def get_shunt_compensator_asset_model(self):
        """ 
        """
        return self._shunt_compensator_asset_model

    def set_shunt_compensator_asset_model(self, value):
        if self._shunt_compensator_asset_model is not None:
            self._shunt_compensator_asset_model._shunt_impedance_info = None

        self._shunt_compensator_asset_model = value
        if self._shunt_compensator_asset_model is not None:
            self._shunt_compensator_asset_model._shunt_impedance_info = self

    shunt_compensator_asset_model = property(get_shunt_compensator_asset_model, set_shunt_compensator_asset_model)
    # >>> shunt_compensator_asset_model

    # <<< shunt_compensator_assets
    # @generated
    def get_shunt_compensator_assets(self):
        """ 
        """
        return self._shunt_compensator_assets

    def set_shunt_compensator_assets(self, value):
        for x in self._shunt_compensator_assets:
            x._shunt_impedance_info = None
        for y in value:
            y._shunt_impedance_info = self
        self._shunt_compensator_assets = value

    shunt_compensator_assets = property(get_shunt_compensator_assets, set_shunt_compensator_assets)

    def add_shunt_compensator_assets(self, *shunt_compensator_assets):
        for obj in shunt_compensator_assets:
            obj._shunt_impedance_info = self
            self._shunt_compensator_assets.append(obj)

    def remove_shunt_compensator_assets(self, *shunt_compensator_assets):
        for obj in shunt_compensator_assets:
            obj._shunt_impedance_info = None
            self._shunt_compensator_assets.remove(obj)
    # >>> shunt_compensator_assets


    def __str__(self):
        """ Returns a string representation of the ShuntImpedanceInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< shunt_impedance_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShuntImpedanceInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShuntImpedanceInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.shunt_compensator_type_asset is not None:
            s += '%s<%s:ShuntImpedanceInfo.shunt_compensator_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shunt_compensator_type_asset.uri)
        if self.shunt_compensator_asset_model is not None:
            s += '%s<%s:ShuntImpedanceInfo.shunt_compensator_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shunt_compensator_asset_model.uri)
        for obj in self.shunt_compensator_assets:
            s += '%s<%s:ShuntImpedanceInfo.shunt_compensator_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ShuntImpedanceInfo.control_kind>%s</%s:ShuntImpedanceInfo.control_kind>' % \
            (indent, ns_prefix, self.control_kind, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.sensing_phase_code>%s</%s:ShuntImpedanceInfo.sensing_phase_code>' % \
            (indent, ns_prefix, self.sensing_phase_code, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.reg_branch_kind>%s</%s:ShuntImpedanceInfo.reg_branch_kind>' % \
            (indent, ns_prefix, self.reg_branch_kind, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.local_control_kind>%s</%s:ShuntImpedanceInfo.local_control_kind>' % \
            (indent, ns_prefix, self.local_control_kind, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.reg_branch>%s</%s:ShuntImpedanceInfo.reg_branch>' % \
            (indent, ns_prefix, self.reg_branch, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.low_voltage_override>%s</%s:ShuntImpedanceInfo.low_voltage_override>' % \
            (indent, ns_prefix, self.low_voltage_override, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.switch_operation_cycle>%s</%s:ShuntImpedanceInfo.switch_operation_cycle>' % \
            (indent, ns_prefix, self.switch_operation_cycle, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.high_voltage_override>%s</%s:ShuntImpedanceInfo.high_voltage_override>' % \
            (indent, ns_prefix, self.high_voltage_override, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.local_override>%s</%s:ShuntImpedanceInfo.local_override>' % \
            (indent, ns_prefix, self.local_override, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.reg_branch_end>%s</%s:ShuntImpedanceInfo.reg_branch_end>' % \
            (indent, ns_prefix, self.reg_branch_end, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.local_off_level>%s</%s:ShuntImpedanceInfo.local_off_level>' % \
            (indent, ns_prefix, self.local_off_level, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.branch_direct>%s</%s:ShuntImpedanceInfo.branch_direct>' % \
            (indent, ns_prefix, self.branch_direct, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.normal_open>%s</%s:ShuntImpedanceInfo.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.cell_size>%s</%s:ShuntImpedanceInfo.cell_size>' % \
            (indent, ns_prefix, self.cell_size, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.local_on_level>%s</%s:ShuntImpedanceInfo.local_on_level>' % \
            (indent, ns_prefix, self.local_on_level, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.max_switch_operation_count>%s</%s:ShuntImpedanceInfo.max_switch_operation_count>' % \
            (indent, ns_prefix, self.max_switch_operation_count, ns_prefix)
        s += '%s<%s:ShuntImpedanceInfo.v_reg_line_line>%s</%s:ShuntImpedanceInfo.v_reg_line_line>' % \
            (indent, ns_prefix, self.v_reg_line_line, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShuntImpedanceInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shunt_impedance_info.serialize


class DuctBank(Asset):
    """ A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.
    """
    # <<< duct_bank
    # @generated
    def __init__(self, circuit_count=0, duct_count=0, cable_assets=None, duct_bank_type_asset=None, **kw_args):
        """ Initialises a new 'DuctBank' instance.
        """
        # Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts. 
        self.circuit_count = circuit_count

        # Number of ducts in duct bank. 
        self.duct_count = duct_count


        self._cable_assets = []
        if cable_assets is not None:
            self.cable_assets = cable_assets
        else:
            self.cable_assets = []

        self._duct_bank_type_asset = None
        self.duct_bank_type_asset = duct_bank_type_asset


        super(DuctBank, self).__init__(**kw_args)
    # >>> duct_bank

    # <<< cable_assets
    # @generated
    def get_cable_assets(self):
        """ 
        """
        return self._cable_assets

    def set_cable_assets(self, value):
        for p in self._cable_assets:
            filtered = [q for q in p.duct_banks if q != self]
            self._cable_assets._duct_banks = filtered
        for r in value:
            if self not in r._duct_banks:
                r._duct_banks.append(self)
        self._cable_assets = value

    cable_assets = property(get_cable_assets, set_cable_assets)

    def add_cable_assets(self, *cable_assets):
        for obj in cable_assets:
            if self not in obj._duct_banks:
                obj._duct_banks.append(self)
            self._cable_assets.append(obj)

    def remove_cable_assets(self, *cable_assets):
        for obj in cable_assets:
            if self in obj._duct_banks:
                obj._duct_banks.remove(self)
            self._cable_assets.remove(obj)
    # >>> cable_assets

    # <<< duct_bank_type_asset
    # @generated
    def get_duct_bank_type_asset(self):
        """ 
        """
        return self._duct_bank_type_asset

    def set_duct_bank_type_asset(self, value):
        if self._duct_bank_type_asset is not None:
            filtered = [x for x in self.duct_bank_type_asset.duct_banks if x != self]
            self._duct_bank_type_asset._duct_banks = filtered

        self._duct_bank_type_asset = value
        if self._duct_bank_type_asset is not None:
            self._duct_bank_type_asset._duct_banks.append(self)

    duct_bank_type_asset = property(get_duct_bank_type_asset, set_duct_bank_type_asset)
    # >>> duct_bank_type_asset


    def __str__(self):
        """ Returns a string representation of the DuctBank.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< duct_bank.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DuctBank.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DuctBank", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.cable_assets:
            s += '%s<%s:DuctBank.cable_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.duct_bank_type_asset is not None:
            s += '%s<%s:DuctBank.duct_bank_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.duct_bank_type_asset.uri)
        s += '%s<%s:DuctBank.circuit_count>%s</%s:DuctBank.circuit_count>' % \
            (indent, ns_prefix, self.circuit_count, ns_prefix)
        s += '%s<%s:DuctBank.duct_count>%s</%s:DuctBank.duct_count>' % \
            (indent, ns_prefix, self.duct_count, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DuctBank")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> duct_bank.serialize


class Procedure(Document):
    """ A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.
    """
    # <<< procedure
    # @generated
    def __init__(self, kind='test', instruction='', sequence_number='', corporate_code='', compatible_units=None, procedure_data_sets=None, procedure_values=None, limits=None, **kw_args):
        """ Initialises a new 'Procedure' instance.
        """
        # Kind of this procedure. Values are: "test", "diagnosis", "inspection", "other", "maintenance"
        self.kind = 'test'

        # The textual description of the procedure, which references instances of ProcedureValue as appropriate. 
        self.instruction = instruction

        # Sequence number in a sequence of procedures being performed. 
        self.sequence_number = sequence_number

        # Code for this kind of procedure. 
        self.corporate_code = corporate_code


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._procedure_data_sets = []
        if procedure_data_sets is not None:
            self.procedure_data_sets = procedure_data_sets
        else:
            self.procedure_data_sets = []

        self._procedure_values = []
        if procedure_values is not None:
            self.procedure_values = procedure_values
        else:
            self.procedure_values = []

        self._limits = []
        if limits is not None:
            self.limits = limits
        else:
            self.limits = []


        super(Procedure, self).__init__(**kw_args)
    # >>> procedure

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.procedures if q != self]
            self._compatible_units._procedures = filtered
        for r in value:
            if self not in r._procedures:
                r._procedures.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._procedures:
                obj._procedures.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._procedures:
                obj._procedures.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< procedure_data_sets
    # @generated
    def get_procedure_data_sets(self):
        """ 
        """
        return self._procedure_data_sets

    def set_procedure_data_sets(self, value):
        for x in self._procedure_data_sets:
            x._procedure = None
        for y in value:
            y._procedure = self
        self._procedure_data_sets = value

    procedure_data_sets = property(get_procedure_data_sets, set_procedure_data_sets)

    def add_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            obj._procedure = self
            self._procedure_data_sets.append(obj)

    def remove_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            obj._procedure = None
            self._procedure_data_sets.remove(obj)
    # >>> procedure_data_sets

    # <<< procedure_values
    # @generated
    def get_procedure_values(self):
        """ UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
        """
        return self._procedure_values

    def set_procedure_values(self, value):
        for x in self._procedure_values:
            x._procedure = None
        for y in value:
            y._procedure = self
        self._procedure_values = value

    procedure_values = property(get_procedure_values, set_procedure_values)

    def add_procedure_values(self, *procedure_values):
        for obj in procedure_values:
            obj._procedure = self
            self._procedure_values.append(obj)

    def remove_procedure_values(self, *procedure_values):
        for obj in procedure_values:
            obj._procedure = None
            self._procedure_values.remove(obj)
    # >>> procedure_values

    # <<< limits
    # @generated
    def get_limits(self):
        """ 
        """
        return self._limits

    def set_limits(self, value):
        for p in self._limits:
            filtered = [q for q in p.procedures if q != self]
            self._limits._procedures = filtered
        for r in value:
            if self not in r._procedures:
                r._procedures.append(self)
        self._limits = value

    limits = property(get_limits, set_limits)

    def add_limits(self, *limits):
        for obj in limits:
            if self not in obj._procedures:
                obj._procedures.append(self)
            self._limits.append(obj)

    def remove_limits(self, *limits):
        for obj in limits:
            if self in obj._procedures:
                obj._procedures.remove(self)
            self._limits.remove(obj)
    # >>> limits


    def __str__(self):
        """ Returns a string representation of the Procedure.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< procedure.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Procedure.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Procedure", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.compatible_units:
            s += '%s<%s:Procedure.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:Procedure.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.procedure_values:
            s += '%s<%s:Procedure.procedure_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.limits:
            s += '%s<%s:Procedure.limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Procedure.kind>%s</%s:Procedure.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Procedure.instruction>%s</%s:Procedure.instruction>' % \
            (indent, ns_prefix, self.instruction, ns_prefix)
        s += '%s<%s:Procedure.sequence_number>%s</%s:Procedure.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:Procedure.corporate_code>%s</%s:Procedure.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Procedure")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> procedure.serialize


class TapChangerAsset(Asset):
    """ Physical asset performing TapChanger function.
    """
    # <<< tap_changer_asset
    # @generated
    def __init__(self, tap_changer_asset_model=None, **kw_args):
        """ Initialises a new 'TapChangerAsset' instance.
        """

        self._tap_changer_asset_model = None
        self.tap_changer_asset_model = tap_changer_asset_model


        super(TapChangerAsset, self).__init__(**kw_args)
    # >>> tap_changer_asset

    # <<< tap_changer_asset_model
    # @generated
    def get_tap_changer_asset_model(self):
        """ 
        """
        return self._tap_changer_asset_model

    def set_tap_changer_asset_model(self, value):
        if self._tap_changer_asset_model is not None:
            filtered = [x for x in self.tap_changer_asset_model.tap_changer_assets if x != self]
            self._tap_changer_asset_model._tap_changer_assets = filtered

        self._tap_changer_asset_model = value
        if self._tap_changer_asset_model is not None:
            self._tap_changer_asset_model._tap_changer_assets.append(self)

    tap_changer_asset_model = property(get_tap_changer_asset_model, set_tap_changer_asset_model)
    # >>> tap_changer_asset_model


    def __str__(self):
        """ Returns a string representation of the TapChangerAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tap_changer_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TapChangerAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TapChangerAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.tap_changer_asset_model is not None:
            s += '%s<%s:TapChangerAsset.tap_changer_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tap_changer_asset_model.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TapChangerAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tap_changer_asset.serialize


class PotentialTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of a Potential Transformer (PT), or a PT Model.
    """
    # <<< potential_transformer_info
    # @generated
    def __init__(self, primary_ratio=None, tertiary_ratio=None, secondary_ratio=None, potential_transformer_assets=None, potential_transformer_asset_models=None, potential_transformer_type_asset=None, **kw_args):
        """ Initialises a new 'PotentialTransformerInfo' instance.
        """

        self.primary_ratio = primary_ratio

        self.tertiary_ratio = tertiary_ratio

        self.secondary_ratio = secondary_ratio

        self._potential_transformer_assets = []
        if potential_transformer_assets is not None:
            self.potential_transformer_assets = potential_transformer_assets
        else:
            self.potential_transformer_assets = []

        self._potential_transformer_asset_models = []
        if potential_transformer_asset_models is not None:
            self.potential_transformer_asset_models = potential_transformer_asset_models
        else:
            self.potential_transformer_asset_models = []

        self._potential_transformer_type_asset = None
        self.potential_transformer_type_asset = potential_transformer_type_asset


        super(PotentialTransformerInfo, self).__init__(**kw_args)
    # >>> potential_transformer_info

    # <<< primary_ratio
    # @generated
    # Ratio for the primary winding tap changer.
    primary_ratio = None
    # >>> primary_ratio

    # <<< tertiary_ratio
    # @generated
    # Ratio for the tertiary winding tap changer.
    tertiary_ratio = None
    # >>> tertiary_ratio

    # <<< secondary_ratio
    # @generated
    # Ratio for the secondary winding tap changer.
    secondary_ratio = None
    # >>> secondary_ratio

    # <<< potential_transformer_assets
    # @generated
    def get_potential_transformer_assets(self):
        """ 
        """
        return self._potential_transformer_assets

    def set_potential_transformer_assets(self, value):
        for x in self._potential_transformer_assets:
            x._potential_transformer_info = None
        for y in value:
            y._potential_transformer_info = self
        self._potential_transformer_assets = value

    potential_transformer_assets = property(get_potential_transformer_assets, set_potential_transformer_assets)

    def add_potential_transformer_assets(self, *potential_transformer_assets):
        for obj in potential_transformer_assets:
            obj._potential_transformer_info = self
            self._potential_transformer_assets.append(obj)

    def remove_potential_transformer_assets(self, *potential_transformer_assets):
        for obj in potential_transformer_assets:
            obj._potential_transformer_info = None
            self._potential_transformer_assets.remove(obj)
    # >>> potential_transformer_assets

    # <<< potential_transformer_asset_models
    # @generated
    def get_potential_transformer_asset_models(self):
        """ 
        """
        return self._potential_transformer_asset_models

    def set_potential_transformer_asset_models(self, value):
        for x in self._potential_transformer_asset_models:
            x._potential_transformer_info = None
        for y in value:
            y._potential_transformer_info = self
        self._potential_transformer_asset_models = value

    potential_transformer_asset_models = property(get_potential_transformer_asset_models, set_potential_transformer_asset_models)

    def add_potential_transformer_asset_models(self, *potential_transformer_asset_models):
        for obj in potential_transformer_asset_models:
            obj._potential_transformer_info = self
            self._potential_transformer_asset_models.append(obj)

    def remove_potential_transformer_asset_models(self, *potential_transformer_asset_models):
        for obj in potential_transformer_asset_models:
            obj._potential_transformer_info = None
            self._potential_transformer_asset_models.remove(obj)
    # >>> potential_transformer_asset_models

    # <<< potential_transformer_type_asset
    # @generated
    def get_potential_transformer_type_asset(self):
        """ 
        """
        return self._potential_transformer_type_asset

    def set_potential_transformer_type_asset(self, value):
        if self._potential_transformer_type_asset is not None:
            self._potential_transformer_type_asset._potential_transformer_info = None

        self._potential_transformer_type_asset = value
        if self._potential_transformer_type_asset is not None:
            self._potential_transformer_type_asset._potential_transformer_info = self

    potential_transformer_type_asset = property(get_potential_transformer_type_asset, set_potential_transformer_type_asset)
    # >>> potential_transformer_type_asset


    def __str__(self):
        """ Returns a string representation of the PotentialTransformerInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< potential_transformer_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PotentialTransformerInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PotentialTransformerInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.primary_ratio is not None:
            s += '%s<%s:PotentialTransformerInfo.primary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.primary_ratio.uri)
        if self.tertiary_ratio is not None:
            s += '%s<%s:PotentialTransformerInfo.tertiary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tertiary_ratio.uri)
        if self.secondary_ratio is not None:
            s += '%s<%s:PotentialTransformerInfo.secondary_ratio rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_ratio.uri)
        for obj in self.potential_transformer_assets:
            s += '%s<%s:PotentialTransformerInfo.potential_transformer_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.potential_transformer_asset_models:
            s += '%s<%s:PotentialTransformerInfo.potential_transformer_asset_models rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.potential_transformer_type_asset is not None:
            s += '%s<%s:PotentialTransformerInfo.potential_transformer_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer_type_asset.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PotentialTransformerInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> potential_transformer_info.serialize


class AssetPsrRole(Role):
    """ Roles played between Assets and Power System Resources.
    """
    # <<< asset_psr_role
    # @generated
    def __init__(self, power_system_resource=None, asset=None, **kw_args):
        """ Initialises a new 'AssetPsrRole' instance.
        """

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._asset = None
        self.asset = asset


        super(AssetPsrRole, self).__init__(**kw_args)
    # >>> asset_psr_role

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.asset_roles if x != self]
            self._power_system_resource._asset_roles = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._asset_roles.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.power_system_resource_roles if x != self]
            self._asset._power_system_resource_roles = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._power_system_resource_roles.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset


    def __str__(self):
        """ Returns a string representation of the AssetPsrRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_psr_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetPsrRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetPsrRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:AssetPsrRole.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        if self.asset is not None:
            s += '%s<%s:AssetPsrRole.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetPsrRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_psr_role.serialize


class DocAssetRole(Role):
    """ Roles played between Documents and Assets.
    """
    # <<< doc_asset_role
    # @generated
    def __init__(self, asset=None, document=None, **kw_args):
        """ Initialises a new 'DocAssetRole' instance.
        """

        self._asset = None
        self.asset = asset

        self._document = None
        self.document = document


        super(DocAssetRole, self).__init__(**kw_args)
    # >>> doc_asset_role

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.document_roles if x != self]
            self._asset._document_roles = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._document_roles.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.asset_roles if x != self]
            self._document._asset_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._asset_roles.append(self)

    document = property(get_document, set_document)
    # >>> document


    def __str__(self):
        """ Returns a string representation of the DocAssetRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_asset_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocAssetRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocAssetRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:DocAssetRole.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.document is not None:
            s += '%s<%s:DocAssetRole.document rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocAssetRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_asset_role.serialize


class SubstationAsset(AssetContainer):
    """ A grouping of assets such as conductors, transformers, switchgear, etc. When located on the ground surface, it is usually surrounded by some kind of fence with a locked gate. It may also be located inside buildings, in underground vaults, and on structures. Use 'category' for utility-specific categorisation (such as Air Cooled, Gas Insultated, etc.).
    """
    # <<< substation_asset
    # @generated
    def __init__(self, function='industrial', substation=None, **kw_args):
        """ Initialises a new 'SubstationAsset' instance.
        """
        # Function of this substation asset. Values are: "industrial", "sub_transmission", "generation", "distribution", "transmission", "other"
        self.function = 'industrial'


        self._substation = None
        self.substation = substation


        super(SubstationAsset, self).__init__(**kw_args)
    # >>> substation_asset

    # <<< substation
    # @generated
    def get_substation(self):
        """ 
        """
        return self._substation

    def set_substation(self, value):
        if self._substation is not None:
            self._substation._substation_asset = None

        self._substation = value
        if self._substation is not None:
            self._substation._substation_asset = self

    substation = property(get_substation, set_substation)
    # >>> substation


    def __str__(self):
        """ Returns a string representation of the SubstationAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< substation_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubstationAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubstationAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.substation is not None:
            s += '%s<%s:SubstationAsset.substation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.substation.uri)
        s += '%s<%s:SubstationAsset.function>%s</%s:SubstationAsset.function>' % \
            (indent, ns_prefix, self.function, ns_prefix)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubstationAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> substation_asset.serialize


class SVCInfo(ElectricalInfo):
    """ Properties for an SVC, allowing the capacitive and inductive ratings for each phase to be specified individually if required.
    """
    # <<< svcinfo
    # @generated
    def __init__(self, capacitive_rating=0.0, inductive_rating=0.0, svctype_assets=None, svcasset=None, svcasset_model=None, **kw_args):
        """ Initialises a new 'SVCInfo' instance.
        """
        # Maximum capacitive reactive power 
        self.capacitive_rating = capacitive_rating

        # Maximum inductive reactive power 
        self.inductive_rating = inductive_rating


        self._svctype_assets = []
        if svctype_assets is not None:
            self.svctype_assets = svctype_assets
        else:
            self.svctype_assets = []

        self._svcasset = None
        self.svcasset = svcasset

        self._svcasset_model = None
        self.svcasset_model = svcasset_model


        super(SVCInfo, self).__init__(**kw_args)
    # >>> svcinfo

    # <<< svctype_assets
    # @generated
    def get_svctype_assets(self):
        """ 
        """
        return self._svctype_assets

    def set_svctype_assets(self, value):
        for p in self._svctype_assets:
            filtered = [q for q in p.svc_infos if q != self]
            self._svctype_assets._svc_infos = filtered
        for r in value:
            if self not in r._svc_infos:
                r._svc_infos.append(self)
        self._svctype_assets = value

    svctype_assets = property(get_svctype_assets, set_svctype_assets)

    def add_svctype_assets(self, *svctype_assets):
        for obj in svctype_assets:
            if self not in obj._svc_infos:
                obj._svc_infos.append(self)
            self._svctype_assets.append(obj)

    def remove_svctype_assets(self, *svctype_assets):
        for obj in svctype_assets:
            if self in obj._svc_infos:
                obj._svc_infos.remove(self)
            self._svctype_assets.remove(obj)
    # >>> svctype_assets

    # <<< svcasset
    # @generated
    def get_svcasset(self):
        """ 
        """
        return self._svcasset

    def set_svcasset(self, value):
        if self._svcasset is not None:
            self._svcasset._svc_info = None

        self._svcasset = value
        if self._svcasset is not None:
            self._svcasset._svc_info = self

    svcasset = property(get_svcasset, set_svcasset)
    # >>> svcasset

    # <<< svcasset_model
    # @generated
    def get_svcasset_model(self):
        """ 
        """
        return self._svcasset_model

    def set_svcasset_model(self, value):
        if self._svcasset_model is not None:
            self._svcasset_model._svc_info = None

        self._svcasset_model = value
        if self._svcasset_model is not None:
            self._svcasset_model._svc_info = self

    svcasset_model = property(get_svcasset_model, set_svcasset_model)
    # >>> svcasset_model


    def __str__(self):
        """ Returns a string representation of the SVCInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< svcinfo.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SVCInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SVCInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.svctype_assets:
            s += '%s<%s:SVCInfo.svctype_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.svcasset is not None:
            s += '%s<%s:SVCInfo.svcasset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.svcasset.uri)
        if self.svcasset_model is not None:
            s += '%s<%s:SVCInfo.svcasset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.svcasset_model.uri)
        s += '%s<%s:SVCInfo.capacitive_rating>%s</%s:SVCInfo.capacitive_rating>' % \
            (indent, ns_prefix, self.capacitive_rating, ns_prefix)
        s += '%s<%s:SVCInfo.inductive_rating>%s</%s:SVCInfo.inductive_rating>' % \
            (indent, ns_prefix, self.inductive_rating, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SVCInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> svcinfo.serialize


class CompositeSwitchAsset(Asset):
    """ Physical asset that performs a given CompositeSwitch's role.
    """
    # <<< composite_switch_asset
    # @generated
    def __init__(self, kind='ug_multi_switch', composite_switch_info=None, composite_switch_asset_model=None, **kw_args):
        """ Initialises a new 'CompositeSwitchAsset' instance.
        """
        # Kind of composite switch. Values are: "ug_multi_switch", "throw_over", "esco_throw_over", "gral", "ral", "other", "regulator_bypass"
        self.kind = 'ug_multi_switch'


        self._composite_switch_info = None
        self.composite_switch_info = composite_switch_info

        self._composite_switch_asset_model = None
        self.composite_switch_asset_model = composite_switch_asset_model


        super(CompositeSwitchAsset, self).__init__(**kw_args)
    # >>> composite_switch_asset

    # <<< composite_switch_info
    # @generated
    def get_composite_switch_info(self):
        """ 
        """
        return self._composite_switch_info

    def set_composite_switch_info(self, value):
        if self._composite_switch_info is not None:
            filtered = [x for x in self.composite_switch_info.composite_switch_assets if x != self]
            self._composite_switch_info._composite_switch_assets = filtered

        self._composite_switch_info = value
        if self._composite_switch_info is not None:
            self._composite_switch_info._composite_switch_assets.append(self)

    composite_switch_info = property(get_composite_switch_info, set_composite_switch_info)
    # >>> composite_switch_info

    # <<< composite_switch_asset_model
    # @generated
    def get_composite_switch_asset_model(self):
        """ 
        """
        return self._composite_switch_asset_model

    def set_composite_switch_asset_model(self, value):
        if self._composite_switch_asset_model is not None:
            filtered = [x for x in self.composite_switch_asset_model.composite_switch_assets if x != self]
            self._composite_switch_asset_model._composite_switch_assets = filtered

        self._composite_switch_asset_model = value
        if self._composite_switch_asset_model is not None:
            self._composite_switch_asset_model._composite_switch_assets.append(self)

    composite_switch_asset_model = property(get_composite_switch_asset_model, set_composite_switch_asset_model)
    # >>> composite_switch_asset_model


    def __str__(self):
        """ Returns a string representation of the CompositeSwitchAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< composite_switch_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CompositeSwitchAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CompositeSwitchAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.composite_switch_info is not None:
            s += '%s<%s:CompositeSwitchAsset.composite_switch_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.composite_switch_info.uri)
        if self.composite_switch_asset_model is not None:
            s += '%s<%s:CompositeSwitchAsset.composite_switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.composite_switch_asset_model.uri)
        s += '%s<%s:CompositeSwitchAsset.kind>%s</%s:CompositeSwitchAsset.kind>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CompositeSwitchAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> composite_switch_asset.serialize


class AssetPropertyCurve(Curve):
    """ An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).
    """
    # <<< asset_property_curve
    # @generated
    def __init__(self, specification=None, assets=None, **kw_args):
        """ Initialises a new 'AssetPropertyCurve' instance.
        """

        self._specification = None
        self.specification = specification

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []


        super(AssetPropertyCurve, self).__init__(**kw_args)
    # >>> asset_property_curve

    # <<< specification
    # @generated
    def get_specification(self):
        """ 
        """
        return self._specification

    def set_specification(self, value):
        if self._specification is not None:
            filtered = [x for x in self.specification.asset_property_curves if x != self]
            self._specification._asset_property_curves = filtered

        self._specification = value
        if self._specification is not None:
            self._specification._asset_property_curves.append(self)

    specification = property(get_specification, set_specification)
    # >>> specification

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.asset_property_curves if q != self]
            self._assets._asset_property_curves = filtered
        for r in value:
            if self not in r._asset_property_curves:
                r._asset_property_curves.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._asset_property_curves:
                obj._asset_property_curves.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._asset_property_curves:
                obj._asset_property_curves.remove(self)
            self._assets.remove(obj)
    # >>> assets


    def __str__(self):
        """ Returns a string representation of the AssetPropertyCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asset_property_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AssetPropertyCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AssetPropertyCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.specification is not None:
            s += '%s<%s:AssetPropertyCurve.specification rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.specification.uri)
        for obj in self.assets:
            s += '%s<%s:AssetPropertyCurve.assets rdf:resource="#%s"/>' % \
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
        for obj in self.curve_datas:
            s += '%s<%s:Curve.curve_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Curve.y3_multiplier>%s</%s:Curve.y3_multiplier>' % \
            (indent, ns_prefix, self.y3_multiplier, ns_prefix)
        s += '%s<%s:Curve.y2_multiplier>%s</%s:Curve.y2_multiplier>' % \
            (indent, ns_prefix, self.y2_multiplier, ns_prefix)
        s += '%s<%s:Curve.x_multiplier>%s</%s:Curve.x_multiplier>' % \
            (indent, ns_prefix, self.x_multiplier, ns_prefix)
        s += '%s<%s:Curve.y2_unit>%s</%s:Curve.y2_unit>' % \
            (indent, ns_prefix, self.y2_unit, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)
        s += '%s<%s:Curve.y1_multiplier>%s</%s:Curve.y1_multiplier>' % \
            (indent, ns_prefix, self.y1_multiplier, ns_prefix)
        s += '%s<%s:Curve.y3_unit>%s</%s:Curve.y3_unit>' % \
            (indent, ns_prefix, self.y3_unit, ns_prefix)
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AssetPropertyCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asset_property_curve.serialize


class Specification(Document):
    """ Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.
    """
    # <<< specification
    # @generated
    def __init__(self, asset_properites=None, qualification_requirements=None, ratings=None, dimensions_infos=None, reliability_infos=None, mediums=None, asset_property_curves=None, **kw_args):
        """ Initialises a new 'Specification' instance.
        """

        self._asset_properites = []
        if asset_properites is not None:
            self.asset_properites = asset_properites
        else:
            self.asset_properites = []

        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._ratings = []
        if ratings is not None:
            self.ratings = ratings
        else:
            self.ratings = []

        self._dimensions_infos = []
        if dimensions_infos is not None:
            self.dimensions_infos = dimensions_infos
        else:
            self.dimensions_infos = []

        self._reliability_infos = []
        if reliability_infos is not None:
            self.reliability_infos = reliability_infos
        else:
            self.reliability_infos = []

        self._mediums = []
        if mediums is not None:
            self.mediums = mediums
        else:
            self.mediums = []

        self._asset_property_curves = []
        if asset_property_curves is not None:
            self.asset_property_curves = asset_property_curves
        else:
            self.asset_property_curves = []


        super(Specification, self).__init__(**kw_args)
    # >>> specification

    # <<< asset_properites
    # @generated
    def get_asset_properites(self):
        """ UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._asset_properites

    def set_asset_properites(self, value):
        for x in self._asset_properites:
            x._property_specification = None
        for y in value:
            y._property_specification = self
        self._asset_properites = value

    asset_properites = property(get_asset_properites, set_asset_properites)

    def add_asset_properites(self, *asset_properites):
        for obj in asset_properites:
            obj._property_specification = self
            self._asset_properites.append(obj)

    def remove_asset_properites(self, *asset_properites):
        for obj in asset_properites:
            obj._property_specification = None
            self._asset_properites.remove(obj)
    # >>> asset_properites

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.specifications if q != self]
            self._qualification_requirements._specifications = filtered
        for r in value:
            if self not in r._specifications:
                r._specifications.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._specifications:
                obj._specifications.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._specifications:
                obj._specifications.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< ratings
    # @generated
    def get_ratings(self):
        """ UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        """
        return self._ratings

    def set_ratings(self, value):
        for x in self._ratings:
            x._rating_specification = None
        for y in value:
            y._rating_specification = self
        self._ratings = value

    ratings = property(get_ratings, set_ratings)

    def add_ratings(self, *ratings):
        for obj in ratings:
            obj._rating_specification = self
            self._ratings.append(obj)

    def remove_ratings(self, *ratings):
        for obj in ratings:
            obj._rating_specification = None
            self._ratings.remove(obj)
    # >>> ratings

    # <<< dimensions_infos
    # @generated
    def get_dimensions_infos(self):
        """ 
        """
        return self._dimensions_infos

    def set_dimensions_infos(self, value):
        for p in self._dimensions_infos:
            filtered = [q for q in p.specifications if q != self]
            self._dimensions_infos._specifications = filtered
        for r in value:
            if self not in r._specifications:
                r._specifications.append(self)
        self._dimensions_infos = value

    dimensions_infos = property(get_dimensions_infos, set_dimensions_infos)

    def add_dimensions_infos(self, *dimensions_infos):
        for obj in dimensions_infos:
            if self not in obj._specifications:
                obj._specifications.append(self)
            self._dimensions_infos.append(obj)

    def remove_dimensions_infos(self, *dimensions_infos):
        for obj in dimensions_infos:
            if self in obj._specifications:
                obj._specifications.remove(self)
            self._dimensions_infos.remove(obj)
    # >>> dimensions_infos

    # <<< reliability_infos
    # @generated
    def get_reliability_infos(self):
        """ 
        """
        return self._reliability_infos

    def set_reliability_infos(self, value):
        for x in self._reliability_infos:
            x._specification = None
        for y in value:
            y._specification = self
        self._reliability_infos = value

    reliability_infos = property(get_reliability_infos, set_reliability_infos)

    def add_reliability_infos(self, *reliability_infos):
        for obj in reliability_infos:
            obj._specification = self
            self._reliability_infos.append(obj)

    def remove_reliability_infos(self, *reliability_infos):
        for obj in reliability_infos:
            obj._specification = None
            self._reliability_infos.remove(obj)
    # >>> reliability_infos

    # <<< mediums
    # @generated
    def get_mediums(self):
        """ 
        """
        return self._mediums

    def set_mediums(self, value):
        for x in self._mediums:
            x._specification = None
        for y in value:
            y._specification = self
        self._mediums = value

    mediums = property(get_mediums, set_mediums)

    def add_mediums(self, *mediums):
        for obj in mediums:
            obj._specification = self
            self._mediums.append(obj)

    def remove_mediums(self, *mediums):
        for obj in mediums:
            obj._specification = None
            self._mediums.remove(obj)
    # >>> mediums

    # <<< asset_property_curves
    # @generated
    def get_asset_property_curves(self):
        """ 
        """
        return self._asset_property_curves

    def set_asset_property_curves(self, value):
        for x in self._asset_property_curves:
            x._specification = None
        for y in value:
            y._specification = self
        self._asset_property_curves = value

    asset_property_curves = property(get_asset_property_curves, set_asset_property_curves)

    def add_asset_property_curves(self, *asset_property_curves):
        for obj in asset_property_curves:
            obj._specification = self
            self._asset_property_curves.append(obj)

    def remove_asset_property_curves(self, *asset_property_curves):
        for obj in asset_property_curves:
            obj._specification = None
            self._asset_property_curves.remove(obj)
    # >>> asset_property_curves


    def __str__(self):
        """ Returns a string representation of the Specification.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< specification.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Specification.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Specification", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.asset_properites:
            s += '%s<%s:Specification.asset_properites rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.qualification_requirements:
            s += '%s<%s:Specification.qualification_requirements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.ratings:
            s += '%s<%s:Specification.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.dimensions_infos:
            s += '%s<%s:Specification.dimensions_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Specification.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Specification.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Specification.asset_property_curves rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Specification")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> specification.serialize


class BushingInsulationPF(IdentifiedObject):
    """ Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    """
    # <<< bushing_insulation_pf
    # @generated
    def __init__(self, test_kind='c1', bushing_asset=None, transformer_observation=None, status=None, **kw_args):
        """ Initialises a new 'BushingInsulationPF' instance.
        """
        # Kind of test for this bushing. Values are: "c1", "c2"
        self.test_kind = 'c1'


        self._bushing_asset = None
        self.bushing_asset = bushing_asset

        self._transformer_observation = None
        self.transformer_observation = transformer_observation

        self.status = status


        super(BushingInsulationPF, self).__init__(**kw_args)
    # >>> bushing_insulation_pf

    # <<< bushing_asset
    # @generated
    def get_bushing_asset(self):
        """ 
        """
        return self._bushing_asset

    def set_bushing_asset(self, value):
        if self._bushing_asset is not None:
            filtered = [x for x in self.bushing_asset.bushing_insulation_pfs if x != self]
            self._bushing_asset._bushing_insulation_pfs = filtered

        self._bushing_asset = value
        if self._bushing_asset is not None:
            self._bushing_asset._bushing_insulation_pfs.append(self)

    bushing_asset = property(get_bushing_asset, set_bushing_asset)
    # >>> bushing_asset

    # <<< transformer_observation
    # @generated
    def get_transformer_observation(self):
        """ 
        """
        return self._transformer_observation

    def set_transformer_observation(self, value):
        if self._transformer_observation is not None:
            filtered = [x for x in self.transformer_observation.bushing_insultation_pfs if x != self]
            self._transformer_observation._bushing_insultation_pfs = filtered

        self._transformer_observation = value
        if self._transformer_observation is not None:
            self._transformer_observation._bushing_insultation_pfs.append(self)

    transformer_observation = property(get_transformer_observation, set_transformer_observation)
    # >>> transformer_observation

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the BushingInsulationPF.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bushing_insulation_pf.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BushingInsulationPF.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BushingInsulationPF", self.uri)
        if format:
            indent += ' ' * depth

        if self.bushing_asset is not None:
            s += '%s<%s:BushingInsulationPF.bushing_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bushing_asset.uri)
        if self.transformer_observation is not None:
            s += '%s<%s:BushingInsulationPF.transformer_observation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_observation.uri)
        if self.status is not None:
            s += '%s<%s:BushingInsulationPF.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:BushingInsulationPF.test_kind>%s</%s:BushingInsulationPF.test_kind>' % \
            (indent, ns_prefix, self.test_kind, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BushingInsulationPF")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bushing_insulation_pf.serialize


class DimensionsInfo(IdentifiedObject):
    """ As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.
    """
    # <<< dimensions_info
    # @generated
    def __init__(self, size_length=0.0, size_depth=0.0, size_diameter=0.0, orientation='', size_width=0.0, assets=None, specifications=None, locations=None, **kw_args):
        """ Initialises a new 'DimensionsInfo' instance.
        """
        # Length measurement. 
        self.size_length = size_length

        # Depth measurement. 
        self.size_depth = size_depth

        # Diameter measurement. 
        self.size_diameter = size_diameter

        # A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault. 
        self.orientation = orientation

        # Width measurement. 
        self.size_width = size_width


        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._specifications = []
        if specifications is not None:
            self.specifications = specifications
        else:
            self.specifications = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []


        super(DimensionsInfo, self).__init__(**kw_args)
    # >>> dimensions_info

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for x in self._assets:
            x._dimensions_info = None
        for y in value:
            y._dimensions_info = self
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            obj._dimensions_info = self
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            obj._dimensions_info = None
            self._assets.remove(obj)
    # >>> assets

    # <<< specifications
    # @generated
    def get_specifications(self):
        """ 
        """
        return self._specifications

    def set_specifications(self, value):
        for p in self._specifications:
            filtered = [q for q in p.dimensions_infos if q != self]
            self._specifications._dimensions_infos = filtered
        for r in value:
            if self not in r._dimensions_infos:
                r._dimensions_infos.append(self)
        self._specifications = value

    specifications = property(get_specifications, set_specifications)

    def add_specifications(self, *specifications):
        for obj in specifications:
            if self not in obj._dimensions_infos:
                obj._dimensions_infos.append(self)
            self._specifications.append(obj)

    def remove_specifications(self, *specifications):
        for obj in specifications:
            if self in obj._dimensions_infos:
                obj._dimensions_infos.remove(self)
            self._specifications.remove(obj)
    # >>> specifications

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for x in self._locations:
            x._dimensions_info = None
        for y in value:
            y._dimensions_info = self
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            obj._dimensions_info = self
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            obj._dimensions_info = None
            self._locations.remove(obj)
    # >>> locations


    def __str__(self):
        """ Returns a string representation of the DimensionsInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< dimensions_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DimensionsInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DimensionsInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.assets:
            s += '%s<%s:DimensionsInfo.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.specifications:
            s += '%s<%s:DimensionsInfo.specifications rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:DimensionsInfo.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DimensionsInfo.size_length>%s</%s:DimensionsInfo.size_length>' % \
            (indent, ns_prefix, self.size_length, ns_prefix)
        s += '%s<%s:DimensionsInfo.size_depth>%s</%s:DimensionsInfo.size_depth>' % \
            (indent, ns_prefix, self.size_depth, ns_prefix)
        s += '%s<%s:DimensionsInfo.size_diameter>%s</%s:DimensionsInfo.size_diameter>' % \
            (indent, ns_prefix, self.size_diameter, ns_prefix)
        s += '%s<%s:DimensionsInfo.orientation>%s</%s:DimensionsInfo.orientation>' % \
            (indent, ns_prefix, self.orientation, ns_prefix)
        s += '%s<%s:DimensionsInfo.size_width>%s</%s:DimensionsInfo.size_width>' % \
            (indent, ns_prefix, self.size_width, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DimensionsInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> dimensions_info.serialize


class ComEquipmentAsset(AssetContainer):
    """ Communicaiton equipment, other than media, such as gateways, routers, controllers, etc.
    """
    # <<< com_equipment_asset
    # @generated
    def __init__(self, device_functions=None, **kw_args):
        """ Initialises a new 'ComEquipmentAsset' instance.
        """

        self._device_functions = []
        if device_functions is not None:
            self.device_functions = device_functions
        else:
            self.device_functions = []


        super(ComEquipmentAsset, self).__init__(**kw_args)
    # >>> com_equipment_asset

    # <<< device_functions
    # @generated
    def get_device_functions(self):
        """ All device functions of this communication equipment asset.
        """
        return self._device_functions

    def set_device_functions(self, value):
        for x in self._device_functions:
            x._com_equipment_asset = None
        for y in value:
            y._com_equipment_asset = self
        self._device_functions = value

    device_functions = property(get_device_functions, set_device_functions)

    def add_device_functions(self, *device_functions):
        for obj in device_functions:
            obj._com_equipment_asset = self
            self._device_functions.append(obj)

    def remove_device_functions(self, *device_functions):
        for obj in device_functions:
            obj._com_equipment_asset = None
            self._device_functions.remove(obj)
    # >>> device_functions


    def __str__(self):
        """ Returns a string representation of the ComEquipmentAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< com_equipment_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ComEquipmentAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ComEquipmentAsset", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.device_functions:
            s += '%s<%s:ComEquipmentAsset.device_functions rdf:resource="#%s"/>' % \
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ComEquipmentAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> com_equipment_asset.serialize


class BushingAsset(Asset):
    """ Physical bushing that insulates and protects from abrasion a conductor that passes through it. It is associated with a specific Terminal, which is in turn associated with a ConductingEquipment.
    """
    # <<< bushing_asset
    # @generated
    def __init__(self, c2_capacitance=0.0, c1_power_factor=0.0, c2_power_factor=0.0, c1_capacitance=0.0, terminal=None, bushing_insulation_pfs=None, bushing_model=None, **kw_args):
        """ Initialises a new 'BushingAsset' instance.
        """
        # Factory measured capacitance measured between the power factor tap and ground. 
        self.c2_capacitance = c2_capacitance

        # Factory measured insulation power factor, measured between the power factor tap and the bushing conductor. 
        self.c1_power_factor = c1_power_factor

        # Factory measured insulation power factor, measured between the power factor tap and ground. 
        self.c2_power_factor = c2_power_factor

        # Factory measured capacitance, measured between the power factor tap and the bushing conductor. 
        self.c1_capacitance = c1_capacitance


        self._terminal = None
        self.terminal = terminal

        self._bushing_insulation_pfs = []
        if bushing_insulation_pfs is not None:
            self.bushing_insulation_pfs = bushing_insulation_pfs
        else:
            self.bushing_insulation_pfs = []

        self._bushing_model = None
        self.bushing_model = bushing_model


        super(BushingAsset, self).__init__(**kw_args)
    # >>> bushing_asset

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ 
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            self._terminal._bushing_asset = None

        self._terminal = value
        if self._terminal is not None:
            self._terminal._bushing_asset = self

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< bushing_insulation_pfs
    # @generated
    def get_bushing_insulation_pfs(self):
        """ 
        """
        return self._bushing_insulation_pfs

    def set_bushing_insulation_pfs(self, value):
        for x in self._bushing_insulation_pfs:
            x._bushing_asset = None
        for y in value:
            y._bushing_asset = self
        self._bushing_insulation_pfs = value

    bushing_insulation_pfs = property(get_bushing_insulation_pfs, set_bushing_insulation_pfs)

    def add_bushing_insulation_pfs(self, *bushing_insulation_pfs):
        for obj in bushing_insulation_pfs:
            obj._bushing_asset = self
            self._bushing_insulation_pfs.append(obj)

    def remove_bushing_insulation_pfs(self, *bushing_insulation_pfs):
        for obj in bushing_insulation_pfs:
            obj._bushing_asset = None
            self._bushing_insulation_pfs.remove(obj)
    # >>> bushing_insulation_pfs

    # <<< bushing_model
    # @generated
    def get_bushing_model(self):
        """ 
        """
        return self._bushing_model

    def set_bushing_model(self, value):
        if self._bushing_model is not None:
            self._bushing_model._bushing_asset = None

        self._bushing_model = value
        if self._bushing_model is not None:
            self._bushing_model._bushing_asset = self

    bushing_model = property(get_bushing_model, set_bushing_model)
    # >>> bushing_model


    def __str__(self):
        """ Returns a string representation of the BushingAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bushing_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BushingAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BushingAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:BushingAsset.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.bushing_insulation_pfs:
            s += '%s<%s:BushingAsset.bushing_insulation_pfs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bushing_model is not None:
            s += '%s<%s:BushingAsset.bushing_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bushing_model.uri)
        s += '%s<%s:BushingAsset.c2_capacitance>%s</%s:BushingAsset.c2_capacitance>' % \
            (indent, ns_prefix, self.c2_capacitance, ns_prefix)
        s += '%s<%s:BushingAsset.c1_power_factor>%s</%s:BushingAsset.c1_power_factor>' % \
            (indent, ns_prefix, self.c1_power_factor, ns_prefix)
        s += '%s<%s:BushingAsset.c2_power_factor>%s</%s:BushingAsset.c2_power_factor>' % \
            (indent, ns_prefix, self.c2_power_factor, ns_prefix)
        s += '%s<%s:BushingAsset.c1_capacitance>%s</%s:BushingAsset.c1_capacitance>' % \
            (indent, ns_prefix, self.c1_capacitance, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BushingAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bushing_asset.serialize


class Cabinet(AssetContainer):
    """ Enclosure that offers protection to the equipment it contains and/or safety to people/animals outside it.
    """
    # <<< cabinet
    # @generated
    def __init__(self, cabinet_model=None, **kw_args):
        """ Initialises a new 'Cabinet' instance.
        """

        self._cabinet_model = None
        self.cabinet_model = cabinet_model


        super(Cabinet, self).__init__(**kw_args)
    # >>> cabinet

    # <<< cabinet_model
    # @generated
    def get_cabinet_model(self):
        """ 
        """
        return self._cabinet_model

    def set_cabinet_model(self, value):
        if self._cabinet_model is not None:
            filtered = [x for x in self.cabinet_model.cabinets if x != self]
            self._cabinet_model._cabinets = filtered

        self._cabinet_model = value
        if self._cabinet_model is not None:
            self._cabinet_model._cabinets.append(self)

    cabinet_model = property(get_cabinet_model, set_cabinet_model)
    # >>> cabinet_model


    def __str__(self):
        """ Returns a string representation of the Cabinet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cabinet.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Cabinet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Cabinet", self.uri)
        if format:
            indent += ' ' * depth

        if self.cabinet_model is not None:
            s += '%s<%s:Cabinet.cabinet_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cabinet_model.uri)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Cabinet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cabinet.serialize


class ReliabilityInfo(IdentifiedObject):
    """ Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.
    """
    # <<< reliability_info
    # @generated
    def __init__(self, mom_failure_rate=0.0, m_ttr=0.0, specification=None, assets=None, **kw_args):
        """ Initialises a new 'ReliabilityInfo' instance.
        """
        # Momentary failure rate (temporary failures/kft-year). 
        self.mom_failure_rate = mom_failure_rate

        # Mean time to repair (MTTR - hours). 
        self.m_ttr = m_ttr


        self._specification = None
        self.specification = specification

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []


        super(ReliabilityInfo, self).__init__(**kw_args)
    # >>> reliability_info

    # <<< specification
    # @generated
    def get_specification(self):
        """ 
        """
        return self._specification

    def set_specification(self, value):
        if self._specification is not None:
            filtered = [x for x in self.specification.reliability_infos if x != self]
            self._specification._reliability_infos = filtered

        self._specification = value
        if self._specification is not None:
            self._specification._reliability_infos.append(self)

    specification = property(get_specification, set_specification)
    # >>> specification

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.reliability_infos if q != self]
            self._assets._reliability_infos = filtered
        for r in value:
            if self not in r._reliability_infos:
                r._reliability_infos.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._reliability_infos:
                obj._reliability_infos.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._reliability_infos:
                obj._reliability_infos.remove(self)
            self._assets.remove(obj)
    # >>> assets


    def __str__(self):
        """ Returns a string representation of the ReliabilityInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reliability_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReliabilityInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReliabilityInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.specification is not None:
            s += '%s<%s:ReliabilityInfo.specification rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.specification.uri)
        for obj in self.assets:
            s += '%s<%s:ReliabilityInfo.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ReliabilityInfo.mom_failure_rate>%s</%s:ReliabilityInfo.mom_failure_rate>' % \
            (indent, ns_prefix, self.mom_failure_rate, ns_prefix)
        s += '%s<%s:ReliabilityInfo.m_ttr>%s</%s:ReliabilityInfo.m_ttr>' % \
            (indent, ns_prefix, self.m_ttr, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReliabilityInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reliability_info.serialize


class OrgAssetRole(Role):
    """ The roles played between an Organisations and an Asset.
    """
    # <<< org_asset_role
    # @generated
    def __init__(self, percent_ownership=0.0, asset=None, erp_organisation=None, **kw_args):
        """ Initialises a new 'OrgAssetRole' instance.
        """
        # If the role type is 'owner,' this indicate the percentage of ownership. 
        self.percent_ownership = percent_ownership


        self._asset = None
        self.asset = asset

        self._erp_organisation = None
        self.erp_organisation = erp_organisation


        super(OrgAssetRole, self).__init__(**kw_args)
    # >>> org_asset_role

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.erp_organisation_roles if x != self]
            self._asset._erp_organisation_roles = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._erp_organisation_roles.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.asset_roles if x != self]
            self._erp_organisation._asset_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._asset_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation


    def __str__(self):
        """ Returns a string representation of the OrgAssetRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_asset_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgAssetRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgAssetRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:OrgAssetRole.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.erp_organisation is not None:
            s += '%s<%s:OrgAssetRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
        s += '%s<%s:OrgAssetRole.percent_ownership>%s</%s:OrgAssetRole.percent_ownership>' % \
            (indent, ns_prefix, self.percent_ownership, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgAssetRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_asset_role.serialize


class FinancialInfo(IdentifiedObject):
    """ Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.
    """
    # <<< financial_info
    # @generated
    def __init__(self, cost_type='', plant_transfer_date_time='', actual_purchase_cost=0.0, purchase_date_time='', purchase_order_number='', warranty_end_date_time='', value_date_time='', account='', financial_value=0.0, quantity=0, cost_description='', asset=None, **kw_args):
        """ Initialises a new 'FinancialInfo' instance.
        """
        # Category of cost to which this Material Item belongs. 
        self.cost_type = cost_type

        # Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.' 
        self.plant_transfer_date_time = plant_transfer_date_time

        # The actual purchase cost of this particular asset. 
        self.actual_purchase_cost = actual_purchase_cost

        # Date and time asset was purchased. 
        self.purchase_date_time = purchase_date_time

        # Purchase order identifier. 
        self.purchase_order_number = purchase_order_number

        # Date and time warranty on asset expires. 
        self.warranty_end_date_time = warranty_end_date_time

        # Date and time at which the financial value was last established. 
        self.value_date_time = value_date_time

        # The account to which this actual material item is charged. 
        self.account = account

        # Value of asset as of 'valueDateTime'. 
        self.financial_value = financial_value

        # The quantity of the asset if per unit length, for example conductor. 
        self.quantity = quantity

        # Description of the cost. 
        self.cost_description = cost_description


        self._asset = None
        self.asset = asset


        super(FinancialInfo, self).__init__(**kw_args)
    # >>> financial_info

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            self._asset._financial_info = None

        self._asset = value
        if self._asset is not None:
            self._asset._financial_info = self

    asset = property(get_asset, set_asset)
    # >>> asset


    def __str__(self):
        """ Returns a string representation of the FinancialInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< financial_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FinancialInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FinancialInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:FinancialInfo.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        s += '%s<%s:FinancialInfo.cost_type>%s</%s:FinancialInfo.cost_type>' % \
            (indent, ns_prefix, self.cost_type, ns_prefix)
        s += '%s<%s:FinancialInfo.plant_transfer_date_time>%s</%s:FinancialInfo.plant_transfer_date_time>' % \
            (indent, ns_prefix, self.plant_transfer_date_time, ns_prefix)
        s += '%s<%s:FinancialInfo.actual_purchase_cost>%s</%s:FinancialInfo.actual_purchase_cost>' % \
            (indent, ns_prefix, self.actual_purchase_cost, ns_prefix)
        s += '%s<%s:FinancialInfo.purchase_date_time>%s</%s:FinancialInfo.purchase_date_time>' % \
            (indent, ns_prefix, self.purchase_date_time, ns_prefix)
        s += '%s<%s:FinancialInfo.purchase_order_number>%s</%s:FinancialInfo.purchase_order_number>' % \
            (indent, ns_prefix, self.purchase_order_number, ns_prefix)
        s += '%s<%s:FinancialInfo.warranty_end_date_time>%s</%s:FinancialInfo.warranty_end_date_time>' % \
            (indent, ns_prefix, self.warranty_end_date_time, ns_prefix)
        s += '%s<%s:FinancialInfo.value_date_time>%s</%s:FinancialInfo.value_date_time>' % \
            (indent, ns_prefix, self.value_date_time, ns_prefix)
        s += '%s<%s:FinancialInfo.account>%s</%s:FinancialInfo.account>' % \
            (indent, ns_prefix, self.account, ns_prefix)
        s += '%s<%s:FinancialInfo.financial_value>%s</%s:FinancialInfo.financial_value>' % \
            (indent, ns_prefix, self.financial_value, ns_prefix)
        s += '%s<%s:FinancialInfo.quantity>%s</%s:FinancialInfo.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:FinancialInfo.cost_description>%s</%s:FinancialInfo.cost_description>' % \
            (indent, ns_prefix, self.cost_description, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "FinancialInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> financial_info.serialize


class SwitchAsset(ElectricalAsset):
    """ Physical asset performing Switch function.
    """
    # <<< switch_asset
    # @generated
    def __init__(self, switch_info=None, switch_asset_model=None, **kw_args):
        """ Initialises a new 'SwitchAsset' instance.
        """

        self._switch_info = None
        self.switch_info = switch_info

        self._switch_asset_model = None
        self.switch_asset_model = switch_asset_model


        super(SwitchAsset, self).__init__(**kw_args)
    # >>> switch_asset

    # <<< switch_info
    # @generated
    def get_switch_info(self):
        """ 
        """
        return self._switch_info

    def set_switch_info(self, value):
        if self._switch_info is not None:
            filtered = [x for x in self.switch_info.switch_assets if x != self]
            self._switch_info._switch_assets = filtered

        self._switch_info = value
        if self._switch_info is not None:
            self._switch_info._switch_assets.append(self)

    switch_info = property(get_switch_info, set_switch_info)
    # >>> switch_info

    # <<< switch_asset_model
    # @generated
    def get_switch_asset_model(self):
        """ 
        """
        return self._switch_asset_model

    def set_switch_asset_model(self, value):
        if self._switch_asset_model is not None:
            filtered = [x for x in self.switch_asset_model.switch_assets if x != self]
            self._switch_asset_model._switch_assets = filtered

        self._switch_asset_model = value
        if self._switch_asset_model is not None:
            self._switch_asset_model._switch_assets.append(self)

    switch_asset_model = property(get_switch_asset_model, set_switch_asset_model)
    # >>> switch_asset_model


    def __str__(self):
        """ Returns a string representation of the SwitchAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switch_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SwitchAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SwitchAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.switch_info is not None:
            s += '%s<%s:SwitchAsset.switch_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_info.uri)
        if self.switch_asset_model is not None:
            s += '%s<%s:SwitchAsset.switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SwitchAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switch_asset.serialize


class RecloserInfo(SwitchInfo):
    """ Properties of reclosers.
    """
    # <<< recloser_info
    # @generated
    def __init__(self, ground_trip_normal_enabled=False, ground_trip_capable=False, ground_trip_rating=0.0, phase_trip_rating=0.0, reclose_lockout_count=0, recloser_asset_models=None, recloser_type_asset=None, recloser_assets=None, **kw_args):
        """ Initialises a new 'RecloserInfo' instance.
        """
        # True if normal status of ground trip is enabled. 
        self.ground_trip_normal_enabled = ground_trip_normal_enabled

        # True if device has ground trip capability. 
        self.ground_trip_capable = ground_trip_capable

        # Ground trip rating. 
        self.ground_trip_rating = ground_trip_rating

        # Phase trip rating. 
        self.phase_trip_rating = phase_trip_rating

        # Total number of phase reclose operations. 
        self.reclose_lockout_count = reclose_lockout_count


        self._recloser_asset_models = []
        if recloser_asset_models is not None:
            self.recloser_asset_models = recloser_asset_models
        else:
            self.recloser_asset_models = []

        self._recloser_type_asset = None
        self.recloser_type_asset = recloser_type_asset

        self._recloser_assets = []
        if recloser_assets is not None:
            self.recloser_assets = recloser_assets
        else:
            self.recloser_assets = []


        super(RecloserInfo, self).__init__(**kw_args)
    # >>> recloser_info

    # <<< recloser_asset_models
    # @generated
    def get_recloser_asset_models(self):
        """ 
        """
        return self._recloser_asset_models

    def set_recloser_asset_models(self, value):
        for x in self._recloser_asset_models:
            x._recloser_info = None
        for y in value:
            y._recloser_info = self
        self._recloser_asset_models = value

    recloser_asset_models = property(get_recloser_asset_models, set_recloser_asset_models)

    def add_recloser_asset_models(self, *recloser_asset_models):
        for obj in recloser_asset_models:
            obj._recloser_info = self
            self._recloser_asset_models.append(obj)

    def remove_recloser_asset_models(self, *recloser_asset_models):
        for obj in recloser_asset_models:
            obj._recloser_info = None
            self._recloser_asset_models.remove(obj)
    # >>> recloser_asset_models

    # <<< recloser_type_asset
    # @generated
    def get_recloser_type_asset(self):
        """ 
        """
        return self._recloser_type_asset

    def set_recloser_type_asset(self, value):
        if self._recloser_type_asset is not None:
            self._recloser_type_asset._recloser_info = None

        self._recloser_type_asset = value
        if self._recloser_type_asset is not None:
            self._recloser_type_asset._recloser_info = self

    recloser_type_asset = property(get_recloser_type_asset, set_recloser_type_asset)
    # >>> recloser_type_asset

    # <<< recloser_assets
    # @generated
    def get_recloser_assets(self):
        """ 
        """
        return self._recloser_assets

    def set_recloser_assets(self, value):
        for x in self._recloser_assets:
            x._recloser_info = None
        for y in value:
            y._recloser_info = self
        self._recloser_assets = value

    recloser_assets = property(get_recloser_assets, set_recloser_assets)

    def add_recloser_assets(self, *recloser_assets):
        for obj in recloser_assets:
            obj._recloser_info = self
            self._recloser_assets.append(obj)

    def remove_recloser_assets(self, *recloser_assets):
        for obj in recloser_assets:
            obj._recloser_info = None
            self._recloser_assets.remove(obj)
    # >>> recloser_assets


    def __str__(self):
        """ Returns a string representation of the RecloserInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< recloser_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RecloserInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RecloserInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.recloser_asset_models:
            s += '%s<%s:RecloserInfo.recloser_asset_models rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.recloser_type_asset is not None:
            s += '%s<%s:RecloserInfo.recloser_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.recloser_type_asset.uri)
        for obj in self.recloser_assets:
            s += '%s<%s:RecloserInfo.recloser_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RecloserInfo.ground_trip_normal_enabled>%s</%s:RecloserInfo.ground_trip_normal_enabled>' % \
            (indent, ns_prefix, self.ground_trip_normal_enabled, ns_prefix)
        s += '%s<%s:RecloserInfo.ground_trip_capable>%s</%s:RecloserInfo.ground_trip_capable>' % \
            (indent, ns_prefix, self.ground_trip_capable, ns_prefix)
        s += '%s<%s:RecloserInfo.ground_trip_rating>%s</%s:RecloserInfo.ground_trip_rating>' % \
            (indent, ns_prefix, self.ground_trip_rating, ns_prefix)
        s += '%s<%s:RecloserInfo.phase_trip_rating>%s</%s:RecloserInfo.phase_trip_rating>' % \
            (indent, ns_prefix, self.phase_trip_rating, ns_prefix)
        s += '%s<%s:RecloserInfo.reclose_lockout_count>%s</%s:RecloserInfo.reclose_lockout_count>' % \
            (indent, ns_prefix, self.reclose_lockout_count, ns_prefix)
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
        for obj in self.switch_assets:
            s += '%s<%s:SwitchInfo.switch_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.switch_asset_model is not None:
            s += '%s<%s:SwitchInfo.switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_asset_model.uri)
        if self.switch_type_asset is not None:
            s += '%s<%s:SwitchInfo.switch_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_type_asset.uri)
        s += '%s<%s:SwitchInfo.making_capacity>%s</%s:SwitchInfo.making_capacity>' % \
            (indent, ns_prefix, self.making_capacity, ns_prefix)
        s += '%s<%s:SwitchInfo.pole_count>%s</%s:SwitchInfo.pole_count>' % \
            (indent, ns_prefix, self.pole_count, ns_prefix)
        s += '%s<%s:SwitchInfo.interrupting_rating>%s</%s:SwitchInfo.interrupting_rating>' % \
            (indent, ns_prefix, self.interrupting_rating, ns_prefix)
        s += '%s<%s:SwitchInfo.withstand_current>%s</%s:SwitchInfo.withstand_current>' % \
            (indent, ns_prefix, self.withstand_current, ns_prefix)
        s += '%s<%s:SwitchInfo.minimum_current>%s</%s:SwitchInfo.minimum_current>' % \
            (indent, ns_prefix, self.minimum_current, ns_prefix)
        s += '%s<%s:SwitchInfo.load_break>%s</%s:SwitchInfo.load_break>' % \
            (indent, ns_prefix, self.load_break, ns_prefix)
        s += '%s<%s:SwitchInfo.gang>%s</%s:SwitchInfo.gang>' % \
            (indent, ns_prefix, self.gang, ns_prefix)
        s += '%s<%s:SwitchInfo.dielectric_strength>%s</%s:SwitchInfo.dielectric_strength>' % \
            (indent, ns_prefix, self.dielectric_strength, ns_prefix)
        s += '%s<%s:SwitchInfo.remote>%s</%s:SwitchInfo.remote>' % \
            (indent, ns_prefix, self.remote, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RecloserInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> recloser_info.serialize


class BusbarAsset(ElectricalAsset):
    """ Physical asset used to perform the BusbarSection's role.
    """
    # <<< busbar_asset
    # @generated
    def __init__(self, busbar_asset_model=None, **kw_args):
        """ Initialises a new 'BusbarAsset' instance.
        """

        self._busbar_asset_model = None
        self.busbar_asset_model = busbar_asset_model


        super(BusbarAsset, self).__init__(**kw_args)
    # >>> busbar_asset

    # <<< busbar_asset_model
    # @generated
    def get_busbar_asset_model(self):
        """ 
        """
        return self._busbar_asset_model

    def set_busbar_asset_model(self, value):
        if self._busbar_asset_model is not None:
            filtered = [x for x in self.busbar_asset_model.busbar_assets if x != self]
            self._busbar_asset_model._busbar_assets = filtered

        self._busbar_asset_model = value
        if self._busbar_asset_model is not None:
            self._busbar_asset_model._busbar_assets.append(self)

    busbar_asset_model = property(get_busbar_asset_model, set_busbar_asset_model)
    # >>> busbar_asset_model


    def __str__(self):
        """ Returns a string representation of the BusbarAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< busbar_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusbarAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusbarAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.busbar_asset_model is not None:
            s += '%s<%s:BusbarAsset.busbar_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.busbar_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusbarAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> busbar_asset.serialize


class Guy(StructureSupport):
    """ A type of support for structures.
    """
    pass
    # <<< guy
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Guy' instance.
        """


        super(Guy, self).__init__(**kw_args)
    # >>> guy


    def __str__(self):
        """ Returns a string representation of the Guy.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< guy.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Guy.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Guy", self.uri)
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
        if self.secured_structure is not None:
            s += '%s<%s:StructureSupport.secured_structure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secured_structure.uri)
        s += '%s<%s:StructureSupport.length>%s</%s:StructureSupport.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:StructureSupport.direction>%s</%s:StructureSupport.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:StructureSupport.size>%s</%s:StructureSupport.size>' % \
            (indent, ns_prefix, self.size, ns_prefix)
        s += '%s<%s:StructureSupport.rod_length>%s</%s:StructureSupport.rod_length>' % \
            (indent, ns_prefix, self.rod_length, ns_prefix)
        s += '%s<%s:StructureSupport.rod_count>%s</%s:StructureSupport.rod_count>' % \
            (indent, ns_prefix, self.rod_count, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Guy")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> guy.serialize


class CableAsset(ConductorAsset):
    """ Insultated physical cable for performing the Conductor role used in undergrond and other applications..
    """
    # <<< cable_asset
    # @generated
    def __init__(self, duct_banks=None, duct_bank_type_asset=None, **kw_args):
        """ Initialises a new 'CableAsset' instance.
        """

        self._duct_banks = []
        if duct_banks is not None:
            self.duct_banks = duct_banks
        else:
            self.duct_banks = []

        self._duct_bank_type_asset = None
        self.duct_bank_type_asset = duct_bank_type_asset


        super(CableAsset, self).__init__(**kw_args)
    # >>> cable_asset

    # <<< duct_banks
    # @generated
    def get_duct_banks(self):
        """ 
        """
        return self._duct_banks

    def set_duct_banks(self, value):
        for p in self._duct_banks:
            filtered = [q for q in p.cable_assets if q != self]
            self._duct_banks._cable_assets = filtered
        for r in value:
            if self not in r._cable_assets:
                r._cable_assets.append(self)
        self._duct_banks = value

    duct_banks = property(get_duct_banks, set_duct_banks)

    def add_duct_banks(self, *duct_banks):
        for obj in duct_banks:
            if self not in obj._cable_assets:
                obj._cable_assets.append(self)
            self._duct_banks.append(obj)

    def remove_duct_banks(self, *duct_banks):
        for obj in duct_banks:
            if self in obj._cable_assets:
                obj._cable_assets.remove(self)
            self._duct_banks.remove(obj)
    # >>> duct_banks

    # <<< duct_bank_type_asset
    # @generated
    def get_duct_bank_type_asset(self):
        """ 
        """
        return self._duct_bank_type_asset

    def set_duct_bank_type_asset(self, value):
        if self._duct_bank_type_asset is not None:
            filtered = [x for x in self.duct_bank_type_asset.cable_assets if x != self]
            self._duct_bank_type_asset._cable_assets = filtered

        self._duct_bank_type_asset = value
        if self._duct_bank_type_asset is not None:
            self._duct_bank_type_asset._cable_assets.append(self)

    duct_bank_type_asset = property(get_duct_bank_type_asset, set_duct_bank_type_asset)
    # >>> duct_bank_type_asset


    def __str__(self):
        """ Returns a string representation of the CableAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cable_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CableAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CableAsset", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.duct_banks:
            s += '%s<%s:CableAsset.duct_banks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.duct_bank_type_asset is not None:
            s += '%s<%s:CableAsset.duct_bank_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.duct_bank_type_asset.uri)
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
        if self.circuit_section is not None:
            s += '%s<%s:ConductorAsset.circuit_section rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.circuit_section.uri)
        if self.conductor_asset_model is not None:
            s += '%s<%s:ConductorAsset.conductor_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_asset_model.uri)
        if self.conductor_segment is not None:
            s += '%s<%s:ConductorAsset.conductor_segment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_segment.uri)
        s += '%s<%s:ConductorAsset.grounding_method>%s</%s:ConductorAsset.grounding_method>' % \
            (indent, ns_prefix, self.grounding_method, ns_prefix)
        s += '%s<%s:ConductorAsset.is_horizontal>%s</%s:ConductorAsset.is_horizontal>' % \
            (indent, ns_prefix, self.is_horizontal, ns_prefix)
        s += '%s<%s:ConductorAsset.insulated>%s</%s:ConductorAsset.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CableAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cable_asset.serialize


class GeneratorAsset(ElectricalAsset):
    """ Physical asset performing the Generator role.
    """
    # <<< generator_asset
    # @generated
    def __init__(self, generator_asset_model=None, **kw_args):
        """ Initialises a new 'GeneratorAsset' instance.
        """

        self._generator_asset_model = None
        self.generator_asset_model = generator_asset_model


        super(GeneratorAsset, self).__init__(**kw_args)
    # >>> generator_asset

    # <<< generator_asset_model
    # @generated
    def get_generator_asset_model(self):
        """ 
        """
        return self._generator_asset_model

    def set_generator_asset_model(self, value):
        if self._generator_asset_model is not None:
            filtered = [x for x in self.generator_asset_model.generator_assets if x != self]
            self._generator_asset_model._generator_assets = filtered

        self._generator_asset_model = value
        if self._generator_asset_model is not None:
            self._generator_asset_model._generator_assets.append(self)

    generator_asset_model = property(get_generator_asset_model, set_generator_asset_model)
    # >>> generator_asset_model


    def __str__(self):
        """ Returns a string representation of the GeneratorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< generator_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeneratorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeneratorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.generator_asset_model is not None:
            s += '%s<%s:GeneratorAsset.generator_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generator_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeneratorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> generator_asset.serialize


class UndergroundStructure(Structure):
    """ Abstract class for underground structures. Typical structure types are: BURD, Enclosure, Hand Hole, Manhole, Pad/Slab, Subsurface Enclosure, Trench, Tunnel, Vault, Pull/Splice Box.
    """
    # <<< underground_structure
    # @generated
    def __init__(self, sealing_warranty_expires_date='', ventilation=False, material='', **kw_args):
        """ Initialises a new 'UndergroundStructure' instance.
        """
        # Date sealing warranty expires. 
        self.sealing_warranty_expires_date = sealing_warranty_expires_date

        # True if vault is ventilating. 
        self.ventilation = ventilation

        # Primary material of underground structure. 
        self.material = material



        super(UndergroundStructure, self).__init__(**kw_args)
    # >>> underground_structure


    def __str__(self):
        """ Returns a string representation of the UndergroundStructure.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< underground_structure.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the UndergroundStructure.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "UndergroundStructure", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:UndergroundStructure.sealing_warranty_expires_date>%s</%s:UndergroundStructure.sealing_warranty_expires_date>' % \
            (indent, ns_prefix, self.sealing_warranty_expires_date, ns_prefix)
        s += '%s<%s:UndergroundStructure.ventilation>%s</%s:UndergroundStructure.ventilation>' % \
            (indent, ns_prefix, self.ventilation, ns_prefix)
        s += '%s<%s:UndergroundStructure.material>%s</%s:UndergroundStructure.material>' % \
            (indent, ns_prefix, self.material, ns_prefix)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.structure_supports:
            s += '%s<%s:Structure.structure_supports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Structure.material_kind>%s</%s:Structure.material_kind>' % \
            (indent, ns_prefix, self.material_kind, ns_prefix)
        s += '%s<%s:Structure.height>%s</%s:Structure.height>' % \
            (indent, ns_prefix, self.height, ns_prefix)
        s += '%s<%s:Structure.remove_weed>%s</%s:Structure.remove_weed>' % \
            (indent, ns_prefix, self.remove_weed, ns_prefix)
        s += '%s<%s:Structure.weed_removed_date>%s</%s:Structure.weed_removed_date>' % \
            (indent, ns_prefix, self.weed_removed_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_applied_date>%s</%s:Structure.fumigant_applied_date>' % \
            (indent, ns_prefix, self.fumigant_applied_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_name>%s</%s:Structure.fumigant_name>' % \
            (indent, ns_prefix, self.fumigant_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "UndergroundStructure")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> underground_structure.serialize


class ShuntCompensatorAsset(ElectricalAsset):
    """ For a shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is the physical asset performing the ShuntCompensator role (PSR).
    """
    # <<< shunt_compensator_asset
    # @generated
    def __init__(self, shunt_compensator_asset_model=None, shunt_impedance_info=None, **kw_args):
        """ Initialises a new 'ShuntCompensatorAsset' instance.
        """

        self._shunt_compensator_asset_model = None
        self.shunt_compensator_asset_model = shunt_compensator_asset_model

        self._shunt_impedance_info = None
        self.shunt_impedance_info = shunt_impedance_info


        super(ShuntCompensatorAsset, self).__init__(**kw_args)
    # >>> shunt_compensator_asset

    # <<< shunt_compensator_asset_model
    # @generated
    def get_shunt_compensator_asset_model(self):
        """ 
        """
        return self._shunt_compensator_asset_model

    def set_shunt_compensator_asset_model(self, value):
        if self._shunt_compensator_asset_model is not None:
            filtered = [x for x in self.shunt_compensator_asset_model.shunt_compensator_assets if x != self]
            self._shunt_compensator_asset_model._shunt_compensator_assets = filtered

        self._shunt_compensator_asset_model = value
        if self._shunt_compensator_asset_model is not None:
            self._shunt_compensator_asset_model._shunt_compensator_assets.append(self)

    shunt_compensator_asset_model = property(get_shunt_compensator_asset_model, set_shunt_compensator_asset_model)
    # >>> shunt_compensator_asset_model

    # <<< shunt_impedance_info
    # @generated
    def get_shunt_impedance_info(self):
        """ 
        """
        return self._shunt_impedance_info

    def set_shunt_impedance_info(self, value):
        if self._shunt_impedance_info is not None:
            filtered = [x for x in self.shunt_impedance_info.shunt_compensator_assets if x != self]
            self._shunt_impedance_info._shunt_compensator_assets = filtered

        self._shunt_impedance_info = value
        if self._shunt_impedance_info is not None:
            self._shunt_impedance_info._shunt_compensator_assets.append(self)

    shunt_impedance_info = property(get_shunt_impedance_info, set_shunt_impedance_info)
    # >>> shunt_impedance_info


    def __str__(self):
        """ Returns a string representation of the ShuntCompensatorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< shunt_compensator_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShuntCompensatorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShuntCompensatorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.shunt_compensator_asset_model is not None:
            s += '%s<%s:ShuntCompensatorAsset.shunt_compensator_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shunt_compensator_asset_model.uri)
        if self.shunt_impedance_info is not None:
            s += '%s<%s:ShuntCompensatorAsset.shunt_impedance_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shunt_impedance_info.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShuntCompensatorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shunt_compensator_asset.serialize


class SurgeProtectorAsset(ElectricalAsset):
    """ Physical asset performing SurgeProtector function.
    """
    # <<< surge_protector_asset
    # @generated
    def __init__(self, surge_protector=None, surge_protector_asset_model=None, **kw_args):
        """ Initialises a new 'SurgeProtectorAsset' instance.
        """

        self._surge_protector = None
        self.surge_protector = surge_protector

        self._surge_protector_asset_model = None
        self.surge_protector_asset_model = surge_protector_asset_model


        super(SurgeProtectorAsset, self).__init__(**kw_args)
    # >>> surge_protector_asset

    # <<< surge_protector
    # @generated
    def get_surge_protector(self):
        """ 
        """
        return self._surge_protector

    def set_surge_protector(self, value):
        if self._surge_protector is not None:
            self._surge_protector._surge_protector_asset = None

        self._surge_protector = value
        if self._surge_protector is not None:
            self._surge_protector._surge_protector_asset = self

    surge_protector = property(get_surge_protector, set_surge_protector)
    # >>> surge_protector

    # <<< surge_protector_asset_model
    # @generated
    def get_surge_protector_asset_model(self):
        """ 
        """
        return self._surge_protector_asset_model

    def set_surge_protector_asset_model(self, value):
        if self._surge_protector_asset_model is not None:
            filtered = [x for x in self.surge_protector_asset_model.surge_protector_assets if x != self]
            self._surge_protector_asset_model._surge_protector_assets = filtered

        self._surge_protector_asset_model = value
        if self._surge_protector_asset_model is not None:
            self._surge_protector_asset_model._surge_protector_assets.append(self)

    surge_protector_asset_model = property(get_surge_protector_asset_model, set_surge_protector_asset_model)
    # >>> surge_protector_asset_model


    def __str__(self):
        """ Returns a string representation of the SurgeProtectorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< surge_protector_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SurgeProtectorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SurgeProtectorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.surge_protector is not None:
            s += '%s<%s:SurgeProtectorAsset.surge_protector rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.surge_protector.uri)
        if self.surge_protector_asset_model is not None:
            s += '%s<%s:SurgeProtectorAsset.surge_protector_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.surge_protector_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SurgeProtectorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> surge_protector_asset.serialize


class PotentialTransformerAsset(ElectricalAsset):
    """ Physical asset performing Potential Transformer (PT) function.
    """
    # <<< potential_transformer_asset
    # @generated
    def __init__(self, potential_transformer=None, potential_transformer_info=None, potential_transformer_asset_model=None, **kw_args):
        """ Initialises a new 'PotentialTransformerAsset' instance.
        """

        self._potential_transformer = None
        self.potential_transformer = potential_transformer

        self._potential_transformer_info = None
        self.potential_transformer_info = potential_transformer_info

        self._potential_transformer_asset_model = None
        self.potential_transformer_asset_model = potential_transformer_asset_model


        super(PotentialTransformerAsset, self).__init__(**kw_args)
    # >>> potential_transformer_asset

    # <<< potential_transformer
    # @generated
    def get_potential_transformer(self):
        """ 
        """
        return self._potential_transformer

    def set_potential_transformer(self, value):
        if self._potential_transformer is not None:
            self._potential_transformer._potential_transformer_asset = None

        self._potential_transformer = value
        if self._potential_transformer is not None:
            self._potential_transformer._potential_transformer_asset = self

    potential_transformer = property(get_potential_transformer, set_potential_transformer)
    # >>> potential_transformer

    # <<< potential_transformer_info
    # @generated
    def get_potential_transformer_info(self):
        """ 
        """
        return self._potential_transformer_info

    def set_potential_transformer_info(self, value):
        if self._potential_transformer_info is not None:
            filtered = [x for x in self.potential_transformer_info.potential_transformer_assets if x != self]
            self._potential_transformer_info._potential_transformer_assets = filtered

        self._potential_transformer_info = value
        if self._potential_transformer_info is not None:
            self._potential_transformer_info._potential_transformer_assets.append(self)

    potential_transformer_info = property(get_potential_transformer_info, set_potential_transformer_info)
    # >>> potential_transformer_info

    # <<< potential_transformer_asset_model
    # @generated
    def get_potential_transformer_asset_model(self):
        """ 
        """
        return self._potential_transformer_asset_model

    def set_potential_transformer_asset_model(self, value):
        if self._potential_transformer_asset_model is not None:
            filtered = [x for x in self.potential_transformer_asset_model.potential_transformer_assets if x != self]
            self._potential_transformer_asset_model._potential_transformer_assets = filtered

        self._potential_transformer_asset_model = value
        if self._potential_transformer_asset_model is not None:
            self._potential_transformer_asset_model._potential_transformer_assets.append(self)

    potential_transformer_asset_model = property(get_potential_transformer_asset_model, set_potential_transformer_asset_model)
    # >>> potential_transformer_asset_model


    def __str__(self):
        """ Returns a string representation of the PotentialTransformerAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< potential_transformer_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PotentialTransformerAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PotentialTransformerAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.potential_transformer is not None:
            s += '%s<%s:PotentialTransformerAsset.potential_transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer.uri)
        if self.potential_transformer_info is not None:
            s += '%s<%s:PotentialTransformerAsset.potential_transformer_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer_info.uri)
        if self.potential_transformer_asset_model is not None:
            s += '%s<%s:PotentialTransformerAsset.potential_transformer_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PotentialTransformerAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> potential_transformer_asset.serialize


class TestDataSet(ProcedureDataSet):
    """ Test results, usually obtained by a lab or other independent organisation.
    """
    # <<< test_data_set
    # @generated
    def __init__(self, specimen_id='', conclusion='', specimen_to_lab_date_time='', **kw_args):
        """ Initialises a new 'TestDataSet' instance.
        """
        # Identifier of specimen used in inspection or test. 
        self.specimen_id = specimen_id

        # Conclusion drawn from test results. 
        self.conclusion = conclusion

        # Date and time the specimen was received by the lab. 
        self.specimen_to_lab_date_time = specimen_to_lab_date_time



        super(TestDataSet, self).__init__(**kw_args)
    # >>> test_data_set


    def __str__(self):
        """ Returns a string representation of the TestDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< test_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TestDataSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TestDataSet", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:TestDataSet.specimen_id>%s</%s:TestDataSet.specimen_id>' % \
            (indent, ns_prefix, self.specimen_id, ns_prefix)
        s += '%s<%s:TestDataSet.conclusion>%s</%s:TestDataSet.conclusion>' % \
            (indent, ns_prefix, self.conclusion, ns_prefix)
        s += '%s<%s:TestDataSet.specimen_to_lab_date_time>%s</%s:TestDataSet.specimen_to_lab_date_time>' % \
            (indent, ns_prefix, self.specimen_to_lab_date_time, ns_prefix)
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
        if self.procedure is not None:
            s += '%s<%s:ProcedureDataSet.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.properties:
            s += '%s<%s:ProcedureDataSet.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ProcedureDataSet.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:ProcedureDataSet.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProcedureDataSet.completed_date_time>%s</%s:ProcedureDataSet.completed_date_time>' % \
            (indent, ns_prefix, self.completed_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TestDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> test_data_set.serialize


class FACTSDeviceAsset(ElectricalAsset):
    """ Physical asset used to perform the FACTSDevice's role.
    """
    # <<< factsdevice_asset
    # @generated
    def __init__(self, kind='tsbr', factsdevice_asset_model=None, **kw_args):
        """ Initialises a new 'FACTSDeviceAsset' instance.
        """
        # Kind of FACTS device. Values are: "tsbr", "statcom", "tcvl", "tssc", "tcpar", "svc", "upfc", "tcsc"
        self.kind = 'tsbr'


        self._factsdevice_asset_model = None
        self.factsdevice_asset_model = factsdevice_asset_model


        super(FACTSDeviceAsset, self).__init__(**kw_args)
    # >>> factsdevice_asset

    # <<< factsdevice_asset_model
    # @generated
    def get_factsdevice_asset_model(self):
        """ 
        """
        return self._factsdevice_asset_model

    def set_factsdevice_asset_model(self, value):
        if self._factsdevice_asset_model is not None:
            filtered = [x for x in self.factsdevice_asset_model.factsdevice_assets if x != self]
            self._factsdevice_asset_model._factsdevice_assets = filtered

        self._factsdevice_asset_model = value
        if self._factsdevice_asset_model is not None:
            self._factsdevice_asset_model._factsdevice_assets.append(self)

    factsdevice_asset_model = property(get_factsdevice_asset_model, set_factsdevice_asset_model)
    # >>> factsdevice_asset_model


    def __str__(self):
        """ Returns a string representation of the FACTSDeviceAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< factsdevice_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FACTSDeviceAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FACTSDeviceAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.factsdevice_asset_model is not None:
            s += '%s<%s:FACTSDeviceAsset.factsdevice_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.factsdevice_asset_model.uri)
        s += '%s<%s:FACTSDeviceAsset.kind>%s</%s:FACTSDeviceAsset.kind>' % \
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FACTSDeviceAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> factsdevice_asset.serialize


class OverheadConductorAsset(ConductorAsset):
    """ Physical conductor performing the Conductor role that is used in overhead applications.
    """
    # <<< overhead_conductor_asset
    # @generated
    def __init__(self, mounting_point=None, **kw_args):
        """ Initialises a new 'OverheadConductorAsset' instance.
        """

        self._mounting_point = None
        self.mounting_point = mounting_point


        super(OverheadConductorAsset, self).__init__(**kw_args)
    # >>> overhead_conductor_asset

    # <<< mounting_point
    # @generated
    def get_mounting_point(self):
        """ 
        """
        return self._mounting_point

    def set_mounting_point(self, value):
        if self._mounting_point is not None:
            filtered = [x for x in self.mounting_point.overhead_conductors if x != self]
            self._mounting_point._overhead_conductors = filtered

        self._mounting_point = value
        if self._mounting_point is not None:
            self._mounting_point._overhead_conductors.append(self)

    mounting_point = property(get_mounting_point, set_mounting_point)
    # >>> mounting_point


    def __str__(self):
        """ Returns a string representation of the OverheadConductorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< overhead_conductor_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OverheadConductorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OverheadConductorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.mounting_point is not None:
            s += '%s<%s:OverheadConductorAsset.mounting_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.mounting_point.uri)
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
        if self.circuit_section is not None:
            s += '%s<%s:ConductorAsset.circuit_section rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.circuit_section.uri)
        if self.conductor_asset_model is not None:
            s += '%s<%s:ConductorAsset.conductor_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_asset_model.uri)
        if self.conductor_segment is not None:
            s += '%s<%s:ConductorAsset.conductor_segment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_segment.uri)
        s += '%s<%s:ConductorAsset.grounding_method>%s</%s:ConductorAsset.grounding_method>' % \
            (indent, ns_prefix, self.grounding_method, ns_prefix)
        s += '%s<%s:ConductorAsset.is_horizontal>%s</%s:ConductorAsset.is_horizontal>' % \
            (indent, ns_prefix, self.is_horizontal, ns_prefix)
        s += '%s<%s:ConductorAsset.insulated>%s</%s:ConductorAsset.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OverheadConductorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> overhead_conductor_asset.serialize


class SVCAsset(FACTSDeviceAsset):
    """ Physical asset performing StaticVarCompensator function.
    """
    # <<< svcasset
    # @generated
    def __init__(self, svc_info=None, svcasset_model=None, **kw_args):
        """ Initialises a new 'SVCAsset' instance.
        """

        self._svc_info = None
        self.svc_info = svc_info

        self._svcasset_model = None
        self.svcasset_model = svcasset_model


        super(SVCAsset, self).__init__(**kw_args)
    # >>> svcasset

    # <<< svc_info
    # @generated
    def get_svc_info(self):
        """ 
        """
        return self._svc_info

    def set_svc_info(self, value):
        if self._svc_info is not None:
            self._svc_info._svcasset = None

        self._svc_info = value
        if self._svc_info is not None:
            self._svc_info._svcasset = self

    svc_info = property(get_svc_info, set_svc_info)
    # >>> svc_info

    # <<< svcasset_model
    # @generated
    def get_svcasset_model(self):
        """ 
        """
        return self._svcasset_model

    def set_svcasset_model(self, value):
        if self._svcasset_model is not None:
            filtered = [x for x in self.svcasset_model.svcassets if x != self]
            self._svcasset_model._svcassets = filtered

        self._svcasset_model = value
        if self._svcasset_model is not None:
            self._svcasset_model._svcassets.append(self)

    svcasset_model = property(get_svcasset_model, set_svcasset_model)
    # >>> svcasset_model


    def __str__(self):
        """ Returns a string representation of the SVCAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< svcasset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SVCAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SVCAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.svc_info is not None:
            s += '%s<%s:SVCAsset.svc_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.svc_info.uri)
        if self.svcasset_model is not None:
            s += '%s<%s:SVCAsset.svcasset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.svcasset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)
        if self.factsdevice_asset_model is not None:
            s += '%s<%s:FACTSDeviceAsset.factsdevice_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.factsdevice_asset_model.uri)
        s += '%s<%s:FACTSDeviceAsset.kind>%s</%s:FACTSDeviceAsset.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SVCAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> svcasset.serialize


class ProtectionEquipmentAsset(ElectricalAsset):
    """ Physical asset performing ProtectionEquipment function.
    """
    # <<< protection_equipment_asset
    # @generated
    def __init__(self, phase_trip=0.0, ground_trip=0.0, protection_equipment_asset_model=None, **kw_args):
        """ Initialises a new 'ProtectionEquipmentAsset' instance.
        """
        # Actual phase trip for this type of relay, if applicable. 
        self.phase_trip = phase_trip

        # Actual ground trip for this type of relay, if applicable. 
        self.ground_trip = ground_trip


        self._protection_equipment_asset_model = None
        self.protection_equipment_asset_model = protection_equipment_asset_model


        super(ProtectionEquipmentAsset, self).__init__(**kw_args)
    # >>> protection_equipment_asset

    # <<< protection_equipment_asset_model
    # @generated
    def get_protection_equipment_asset_model(self):
        """ 
        """
        return self._protection_equipment_asset_model

    def set_protection_equipment_asset_model(self, value):
        if self._protection_equipment_asset_model is not None:
            filtered = [x for x in self.protection_equipment_asset_model.protection_equipment_assets if x != self]
            self._protection_equipment_asset_model._protection_equipment_assets = filtered

        self._protection_equipment_asset_model = value
        if self._protection_equipment_asset_model is not None:
            self._protection_equipment_asset_model._protection_equipment_assets.append(self)

    protection_equipment_asset_model = property(get_protection_equipment_asset_model, set_protection_equipment_asset_model)
    # >>> protection_equipment_asset_model


    def __str__(self):
        """ Returns a string representation of the ProtectionEquipmentAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< protection_equipment_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProtectionEquipmentAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProtectionEquipmentAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.protection_equipment_asset_model is not None:
            s += '%s<%s:ProtectionEquipmentAsset.protection_equipment_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.protection_equipment_asset_model.uri)
        s += '%s<%s:ProtectionEquipmentAsset.phase_trip>%s</%s:ProtectionEquipmentAsset.phase_trip>' % \
            (indent, ns_prefix, self.phase_trip, ns_prefix)
        s += '%s<%s:ProtectionEquipmentAsset.ground_trip>%s</%s:ProtectionEquipmentAsset.ground_trip>' % \
            (indent, ns_prefix, self.ground_trip, ns_prefix)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProtectionEquipmentAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> protection_equipment_asset.serialize


class Manhole(UndergroundStructure):
    """ Provides access at key locations to underground cables, equipment, etc. housed inside a protective vault.
    """
    pass
    # <<< manhole
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Manhole' instance.
        """


        super(Manhole, self).__init__(**kw_args)
    # >>> manhole


    def __str__(self):
        """ Returns a string representation of the Manhole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< manhole.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Manhole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Manhole", self.uri)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.structure_supports:
            s += '%s<%s:Structure.structure_supports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Structure.material_kind>%s</%s:Structure.material_kind>' % \
            (indent, ns_prefix, self.material_kind, ns_prefix)
        s += '%s<%s:Structure.height>%s</%s:Structure.height>' % \
            (indent, ns_prefix, self.height, ns_prefix)
        s += '%s<%s:Structure.remove_weed>%s</%s:Structure.remove_weed>' % \
            (indent, ns_prefix, self.remove_weed, ns_prefix)
        s += '%s<%s:Structure.weed_removed_date>%s</%s:Structure.weed_removed_date>' % \
            (indent, ns_prefix, self.weed_removed_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_applied_date>%s</%s:Structure.fumigant_applied_date>' % \
            (indent, ns_prefix, self.fumigant_applied_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_name>%s</%s:Structure.fumigant_name>' % \
            (indent, ns_prefix, self.fumigant_name, ns_prefix)
        s += '%s<%s:UndergroundStructure.sealing_warranty_expires_date>%s</%s:UndergroundStructure.sealing_warranty_expires_date>' % \
            (indent, ns_prefix, self.sealing_warranty_expires_date, ns_prefix)
        s += '%s<%s:UndergroundStructure.ventilation>%s</%s:UndergroundStructure.ventilation>' % \
            (indent, ns_prefix, self.ventilation, ns_prefix)
        s += '%s<%s:UndergroundStructure.material>%s</%s:UndergroundStructure.material>' % \
            (indent, ns_prefix, self.material, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Manhole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> manhole.serialize


class BreakerAsset(ElectricalAsset):
    """ Physical asset performing Breaker role.
    """
    # <<< breaker_asset
    # @generated
    def __init__(self, breaker_info=None, breaker_asset_model=None, **kw_args):
        """ Initialises a new 'BreakerAsset' instance.
        """

        self._breaker_info = None
        self.breaker_info = breaker_info

        self._breaker_asset_model = None
        self.breaker_asset_model = breaker_asset_model


        super(BreakerAsset, self).__init__(**kw_args)
    # >>> breaker_asset

    # <<< breaker_info
    # @generated
    def get_breaker_info(self):
        """ 
        """
        return self._breaker_info

    def set_breaker_info(self, value):
        if self._breaker_info is not None:
            filtered = [x for x in self.breaker_info.breaker_assets if x != self]
            self._breaker_info._breaker_assets = filtered

        self._breaker_info = value
        if self._breaker_info is not None:
            self._breaker_info._breaker_assets.append(self)

    breaker_info = property(get_breaker_info, set_breaker_info)
    # >>> breaker_info

    # <<< breaker_asset_model
    # @generated
    def get_breaker_asset_model(self):
        """ 
        """
        return self._breaker_asset_model

    def set_breaker_asset_model(self, value):
        if self._breaker_asset_model is not None:
            filtered = [x for x in self.breaker_asset_model.breaker_assets if x != self]
            self._breaker_asset_model._breaker_assets = filtered

        self._breaker_asset_model = value
        if self._breaker_asset_model is not None:
            self._breaker_asset_model._breaker_assets.append(self)

    breaker_asset_model = property(get_breaker_asset_model, set_breaker_asset_model)
    # >>> breaker_asset_model


    def __str__(self):
        """ Returns a string representation of the BreakerAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< breaker_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BreakerAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BreakerAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.breaker_info is not None:
            s += '%s<%s:BreakerAsset.breaker_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.breaker_info.uri)
        if self.breaker_asset_model is not None:
            s += '%s<%s:BreakerAsset.breaker_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.breaker_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BreakerAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> breaker_asset.serialize


class SeriesCompensatorAsset(ElectricalAsset):
    """ For a a series capacitor or reactor, this is the physical asset performing the SeriesCompensator role (PSR).
    """
    # <<< series_compensator_asset
    # @generated
    def __init__(self, series_compensator_asset_model=None, **kw_args):
        """ Initialises a new 'SeriesCompensatorAsset' instance.
        """

        self._series_compensator_asset_model = None
        self.series_compensator_asset_model = series_compensator_asset_model


        super(SeriesCompensatorAsset, self).__init__(**kw_args)
    # >>> series_compensator_asset

    # <<< series_compensator_asset_model
    # @generated
    def get_series_compensator_asset_model(self):
        """ 
        """
        return self._series_compensator_asset_model

    def set_series_compensator_asset_model(self, value):
        if self._series_compensator_asset_model is not None:
            self._series_compensator_asset_model._series_compensator_asset = None

        self._series_compensator_asset_model = value
        if self._series_compensator_asset_model is not None:
            self._series_compensator_asset_model._series_compensator_asset = self

    series_compensator_asset_model = property(get_series_compensator_asset_model, set_series_compensator_asset_model)
    # >>> series_compensator_asset_model


    def __str__(self):
        """ Returns a string representation of the SeriesCompensatorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< series_compensator_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SeriesCompensatorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SeriesCompensatorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.series_compensator_asset_model is not None:
            s += '%s<%s:SeriesCompensatorAsset.series_compensator_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.series_compensator_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SeriesCompensatorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> series_compensator_asset.serialize


class Pole(Structure):
    """ A long, slender piece of wood, metal, etc. usually rounded that stands vertically from the ground and is used for mounting various types of overhead equipment. Dimensions of Pole are specified in associated DimensionsInfo.
    """
    # <<< pole
    # @generated
    def __init__(self, base_kind='cement', preservative_kind='naphthena', treatment_kind='gray_stain', treated_date_time='', construction='', breast_block=False, jpa_reference='', support_streetlights=None, pole_model=None, **kw_args):
        """ Initialises a new 'Pole' instance.
        """
        # Kind of base for this pole. Values are: "cement", "dirt", "unknown", "other", "asphalt"
        self.base_kind = 'cement'

        # Kind of preservative for this pole. Values are: "naphthena", "unknown", "other", "chemonite", "penta", "cellon", "creosote"
        self.preservative_kind = 'naphthena'

        # Kind of treatment for this pole. Values are: "gray_stain", "other", "natural", "green_stain", "full", "unknown", "butt", "penta"
        self.treatment_kind = 'gray_stain'

        # Date and time pole was last treated with preservative. 
        self.treated_date_time = treated_date_time

        # The framing structure mounted on the pole. 
        self.construction = construction

        # True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used. 
        self.breast_block = breast_block

        # Joint pole agreement reference number. 
        self.jpa_reference = jpa_reference


        self._support_streetlights = []
        if support_streetlights is not None:
            self.support_streetlights = support_streetlights
        else:
            self.support_streetlights = []

        self._pole_model = None
        self.pole_model = pole_model


        super(Pole, self).__init__(**kw_args)
    # >>> pole

    # <<< support_streetlights
    # @generated
    def get_support_streetlights(self):
        """ Streetlight(s) may be attached to a pole.
        """
        return self._support_streetlights

    def set_support_streetlights(self, value):
        for x in self._support_streetlights:
            x._attached_to_pole = None
        for y in value:
            y._attached_to_pole = self
        self._support_streetlights = value

    support_streetlights = property(get_support_streetlights, set_support_streetlights)

    def add_support_streetlights(self, *support_streetlights):
        for obj in support_streetlights:
            obj._attached_to_pole = self
            self._support_streetlights.append(obj)

    def remove_support_streetlights(self, *support_streetlights):
        for obj in support_streetlights:
            obj._attached_to_pole = None
            self._support_streetlights.remove(obj)
    # >>> support_streetlights

    # <<< pole_model
    # @generated
    def get_pole_model(self):
        """ 
        """
        return self._pole_model

    def set_pole_model(self, value):
        if self._pole_model is not None:
            filtered = [x for x in self.pole_model.poles if x != self]
            self._pole_model._poles = filtered

        self._pole_model = value
        if self._pole_model is not None:
            self._pole_model._poles.append(self)

    pole_model = property(get_pole_model, set_pole_model)
    # >>> pole_model


    def __str__(self):
        """ Returns a string representation of the Pole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pole.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Pole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Pole", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.support_streetlights:
            s += '%s<%s:Pole.support_streetlights rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pole_model is not None:
            s += '%s<%s:Pole.pole_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pole_model.uri)
        s += '%s<%s:Pole.base_kind>%s</%s:Pole.base_kind>' % \
            (indent, ns_prefix, self.base_kind, ns_prefix)
        s += '%s<%s:Pole.preservative_kind>%s</%s:Pole.preservative_kind>' % \
            (indent, ns_prefix, self.preservative_kind, ns_prefix)
        s += '%s<%s:Pole.treatment_kind>%s</%s:Pole.treatment_kind>' % \
            (indent, ns_prefix, self.treatment_kind, ns_prefix)
        s += '%s<%s:Pole.treated_date_time>%s</%s:Pole.treated_date_time>' % \
            (indent, ns_prefix, self.treated_date_time, ns_prefix)
        s += '%s<%s:Pole.construction>%s</%s:Pole.construction>' % \
            (indent, ns_prefix, self.construction, ns_prefix)
        s += '%s<%s:Pole.breast_block>%s</%s:Pole.breast_block>' % \
            (indent, ns_prefix, self.breast_block, ns_prefix)
        s += '%s<%s:Pole.jpa_reference>%s</%s:Pole.jpa_reference>' % \
            (indent, ns_prefix, self.jpa_reference, ns_prefix)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.structure_supports:
            s += '%s<%s:Structure.structure_supports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Structure.material_kind>%s</%s:Structure.material_kind>' % \
            (indent, ns_prefix, self.material_kind, ns_prefix)
        s += '%s<%s:Structure.height>%s</%s:Structure.height>' % \
            (indent, ns_prefix, self.height, ns_prefix)
        s += '%s<%s:Structure.remove_weed>%s</%s:Structure.remove_weed>' % \
            (indent, ns_prefix, self.remove_weed, ns_prefix)
        s += '%s<%s:Structure.weed_removed_date>%s</%s:Structure.weed_removed_date>' % \
            (indent, ns_prefix, self.weed_removed_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_applied_date>%s</%s:Structure.fumigant_applied_date>' % \
            (indent, ns_prefix, self.fumigant_applied_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_name>%s</%s:Structure.fumigant_name>' % \
            (indent, ns_prefix, self.fumigant_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Pole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pole.serialize


class Anchor(StructureSupport):
    """ A type of support for structures, used to hold poles secure.
    """
    # <<< anchor
    # @generated
    def __init__(self, kind='other', **kw_args):
        """ Initialises a new 'Anchor' instance.
        """
        # Kind of this anchor. Values are: "other", "concrete", "rod", "screw", "multi_helix", "helix", "unknown"
        self.kind = 'other'



        super(Anchor, self).__init__(**kw_args)
    # >>> anchor


    def __str__(self):
        """ Returns a string representation of the Anchor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< anchor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Anchor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Anchor", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Anchor.kind>%s</%s:Anchor.kind>' % \
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
        if self.secured_structure is not None:
            s += '%s<%s:StructureSupport.secured_structure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secured_structure.uri)
        s += '%s<%s:StructureSupport.length>%s</%s:StructureSupport.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:StructureSupport.direction>%s</%s:StructureSupport.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:StructureSupport.size>%s</%s:StructureSupport.size>' % \
            (indent, ns_prefix, self.size, ns_prefix)
        s += '%s<%s:StructureSupport.rod_length>%s</%s:StructureSupport.rod_length>' % \
            (indent, ns_prefix, self.rod_length, ns_prefix)
        s += '%s<%s:StructureSupport.rod_count>%s</%s:StructureSupport.rod_count>' % \
            (indent, ns_prefix, self.rod_count, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Anchor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> anchor.serialize


class CurrentTransformerAsset(ElectricalAsset):
    """ Physical asset performing Current Transformer (CT) function.
    """
    # <<< current_transformer_asset
    # @generated
    def __init__(self, type_ct='', current_transformer_info=None, current_transformer_asset_model=None, current_transformer=None, **kw_args):
        """ Initialises a new 'CurrentTransformerAsset' instance.
        """
        # Type of CT as categorized by the utility's asset management standards and practices. 
        self.type_ct = type_ct


        self._current_transformer_info = None
        self.current_transformer_info = current_transformer_info

        self._current_transformer_asset_model = None
        self.current_transformer_asset_model = current_transformer_asset_model

        self._current_transformer = None
        self.current_transformer = current_transformer


        super(CurrentTransformerAsset, self).__init__(**kw_args)
    # >>> current_transformer_asset

    # <<< current_transformer_info
    # @generated
    def get_current_transformer_info(self):
        """ 
        """
        return self._current_transformer_info

    def set_current_transformer_info(self, value):
        if self._current_transformer_info is not None:
            filtered = [x for x in self.current_transformer_info.current_transformer_assets if x != self]
            self._current_transformer_info._current_transformer_assets = filtered

        self._current_transformer_info = value
        if self._current_transformer_info is not None:
            self._current_transformer_info._current_transformer_assets.append(self)

    current_transformer_info = property(get_current_transformer_info, set_current_transformer_info)
    # >>> current_transformer_info

    # <<< current_transformer_asset_model
    # @generated
    def get_current_transformer_asset_model(self):
        """ 
        """
        return self._current_transformer_asset_model

    def set_current_transformer_asset_model(self, value):
        if self._current_transformer_asset_model is not None:
            filtered = [x for x in self.current_transformer_asset_model.current_transformer_assets if x != self]
            self._current_transformer_asset_model._current_transformer_assets = filtered

        self._current_transformer_asset_model = value
        if self._current_transformer_asset_model is not None:
            self._current_transformer_asset_model._current_transformer_assets.append(self)

    current_transformer_asset_model = property(get_current_transformer_asset_model, set_current_transformer_asset_model)
    # >>> current_transformer_asset_model

    # <<< current_transformer
    # @generated
    def get_current_transformer(self):
        """ 
        """
        return self._current_transformer

    def set_current_transformer(self, value):
        if self._current_transformer is not None:
            self._current_transformer._current_transformer_asset = None

        self._current_transformer = value
        if self._current_transformer is not None:
            self._current_transformer._current_transformer_asset = self

    current_transformer = property(get_current_transformer, set_current_transformer)
    # >>> current_transformer


    def __str__(self):
        """ Returns a string representation of the CurrentTransformerAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_transformer_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentTransformerAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentTransformerAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.current_transformer_info is not None:
            s += '%s<%s:CurrentTransformerAsset.current_transformer_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer_info.uri)
        if self.current_transformer_asset_model is not None:
            s += '%s<%s:CurrentTransformerAsset.current_transformer_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer_asset_model.uri)
        if self.current_transformer is not None:
            s += '%s<%s:CurrentTransformerAsset.current_transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer.uri)
        s += '%s<%s:CurrentTransformerAsset.type_ct>%s</%s:CurrentTransformerAsset.type_ct>' % \
            (indent, ns_prefix, self.type_ct, ns_prefix)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentTransformerAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_transformer_asset.serialize


class ResistorAsset(ElectricalAsset):
    """ Physical asset performing Resistor function.
    """
    # <<< resistor_asset
    # @generated
    def __init__(self, resistor=None, resistor_asset_model=None, **kw_args):
        """ Initialises a new 'ResistorAsset' instance.
        """

        self._resistor = None
        self.resistor = resistor

        self._resistor_asset_model = None
        self.resistor_asset_model = resistor_asset_model


        super(ResistorAsset, self).__init__(**kw_args)
    # >>> resistor_asset

    # <<< resistor
    # @generated
    def get_resistor(self):
        """ 
        """
        return self._resistor

    def set_resistor(self, value):
        if self._resistor is not None:
            self._resistor._resistor_asset = None

        self._resistor = value
        if self._resistor is not None:
            self._resistor._resistor_asset = self

    resistor = property(get_resistor, set_resistor)
    # >>> resistor

    # <<< resistor_asset_model
    # @generated
    def get_resistor_asset_model(self):
        """ 
        """
        return self._resistor_asset_model

    def set_resistor_asset_model(self, value):
        if self._resistor_asset_model is not None:
            filtered = [x for x in self.resistor_asset_model.resistor_assets if x != self]
            self._resistor_asset_model._resistor_assets = filtered

        self._resistor_asset_model = value
        if self._resistor_asset_model is not None:
            self._resistor_asset_model._resistor_assets.append(self)

    resistor_asset_model = property(get_resistor_asset_model, set_resistor_asset_model)
    # >>> resistor_asset_model


    def __str__(self):
        """ Returns a string representation of the ResistorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< resistor_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ResistorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ResistorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.resistor is not None:
            s += '%s<%s:ResistorAsset.resistor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.resistor.uri)
        if self.resistor_asset_model is not None:
            s += '%s<%s:ResistorAsset.resistor_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.resistor_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ResistorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> resistor_asset.serialize


class Streetlight(ElectricalAsset):
    """ Streetlight asset.
    """
    # <<< streetlight
    # @generated
    def __init__(self, lamp_kind='high_pressure_sodium', light_rating=0.0, arm_length=0.0, attached_to_pole=None, streetlight_asset_model=None, **kw_args):
        """ Initialises a new 'Streetlight' instance.
        """
        # Lamp kind currently installed. Values are: "high_pressure_sodium", "other", "metal_halide", "mercury_vapor"
        self.lamp_kind = 'high_pressure_sodium'

        # Actual power rating of light. 
        self.light_rating = light_rating

        # Length of arm of this specific asset. Note that a new light may be placed on an existing arm. 
        self.arm_length = arm_length


        self._attached_to_pole = None
        self.attached_to_pole = attached_to_pole

        self._streetlight_asset_model = None
        self.streetlight_asset_model = streetlight_asset_model


        super(Streetlight, self).__init__(**kw_args)
    # >>> streetlight

    # <<< attached_to_pole
    # @generated
    def get_attached_to_pole(self):
        """ Streetlight(s) may be attached to a pole.
        """
        return self._attached_to_pole

    def set_attached_to_pole(self, value):
        if self._attached_to_pole is not None:
            filtered = [x for x in self.attached_to_pole.support_streetlights if x != self]
            self._attached_to_pole._support_streetlights = filtered

        self._attached_to_pole = value
        if self._attached_to_pole is not None:
            self._attached_to_pole._support_streetlights.append(self)

    attached_to_pole = property(get_attached_to_pole, set_attached_to_pole)
    # >>> attached_to_pole

    # <<< streetlight_asset_model
    # @generated
    def get_streetlight_asset_model(self):
        """ 
        """
        return self._streetlight_asset_model

    def set_streetlight_asset_model(self, value):
        if self._streetlight_asset_model is not None:
            filtered = [x for x in self.streetlight_asset_model.streetlights if x != self]
            self._streetlight_asset_model._streetlights = filtered

        self._streetlight_asset_model = value
        if self._streetlight_asset_model is not None:
            self._streetlight_asset_model._streetlights.append(self)

    streetlight_asset_model = property(get_streetlight_asset_model, set_streetlight_asset_model)
    # >>> streetlight_asset_model


    def __str__(self):
        """ Returns a string representation of the Streetlight.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< streetlight.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Streetlight.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Streetlight", self.uri)
        if format:
            indent += ' ' * depth

        if self.attached_to_pole is not None:
            s += '%s<%s:Streetlight.attached_to_pole rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.attached_to_pole.uri)
        if self.streetlight_asset_model is not None:
            s += '%s<%s:Streetlight.streetlight_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.streetlight_asset_model.uri)
        s += '%s<%s:Streetlight.lamp_kind>%s</%s:Streetlight.lamp_kind>' % \
            (indent, ns_prefix, self.lamp_kind, ns_prefix)
        s += '%s<%s:Streetlight.light_rating>%s</%s:Streetlight.light_rating>' % \
            (indent, ns_prefix, self.light_rating, ns_prefix)
        s += '%s<%s:Streetlight.arm_length>%s</%s:Streetlight.arm_length>' % \
            (indent, ns_prefix, self.arm_length, ns_prefix)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Streetlight")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> streetlight.serialize


class JointAsset(ElectricalAsset):
    """ Physical asset connecting two or more cable assets. It includes the portion of cable under wipes, welds, or other seals.
    """
    # <<< joint_asset
    # @generated
    def __init__(self, configuration_kind='wires2to1', fill_kind='bluefill254', insulation='', **kw_args):
        """ Initialises a new 'JointAsset' instance.
        """
        # Configuration of joint. Values are: "wires2to1", "wires1to1", "other", "wires3to1"
        self.configuration_kind = 'wires2to1'

        # Material used to fill the joint. Values are: "bluefill254", "air_no_filling", "epoxy", "insoluseal", "no_void", "no_fill_prefab", "asphaltic", "other", "oil", "petrolatum"
        self.fill_kind = 'bluefill254'

        # The type of insulation around the joint, classified according to the utility's asset management standards and practices. 
        self.insulation = insulation



        super(JointAsset, self).__init__(**kw_args)
    # >>> joint_asset


    def __str__(self):
        """ Returns a string representation of the JointAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< joint_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the JointAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "JointAsset", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:JointAsset.configuration_kind>%s</%s:JointAsset.configuration_kind>' % \
            (indent, ns_prefix, self.configuration_kind, ns_prefix)
        s += '%s<%s:JointAsset.fill_kind>%s</%s:JointAsset.fill_kind>' % \
            (indent, ns_prefix, self.fill_kind, ns_prefix)
        s += '%s<%s:JointAsset.insulation>%s</%s:JointAsset.insulation>' % \
            (indent, ns_prefix, self.insulation, ns_prefix)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "JointAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> joint_asset.serialize


class RecloserAsset(ElectricalAsset):
    """ Physical recloser performing a reclosing function, which is modeled through Breaker.
    """
    # <<< recloser_asset
    # @generated
    def __init__(self, recloser_asset_model=None, recloser_info=None, **kw_args):
        """ Initialises a new 'RecloserAsset' instance.
        """

        self._recloser_asset_model = None
        self.recloser_asset_model = recloser_asset_model

        self._recloser_info = None
        self.recloser_info = recloser_info


        super(RecloserAsset, self).__init__(**kw_args)
    # >>> recloser_asset

    # <<< recloser_asset_model
    # @generated
    def get_recloser_asset_model(self):
        """ 
        """
        return self._recloser_asset_model

    def set_recloser_asset_model(self, value):
        if self._recloser_asset_model is not None:
            filtered = [x for x in self.recloser_asset_model.recloser_assets if x != self]
            self._recloser_asset_model._recloser_assets = filtered

        self._recloser_asset_model = value
        if self._recloser_asset_model is not None:
            self._recloser_asset_model._recloser_assets.append(self)

    recloser_asset_model = property(get_recloser_asset_model, set_recloser_asset_model)
    # >>> recloser_asset_model

    # <<< recloser_info
    # @generated
    def get_recloser_info(self):
        """ 
        """
        return self._recloser_info

    def set_recloser_info(self, value):
        if self._recloser_info is not None:
            filtered = [x for x in self.recloser_info.recloser_assets if x != self]
            self._recloser_info._recloser_assets = filtered

        self._recloser_info = value
        if self._recloser_info is not None:
            self._recloser_info._recloser_assets.append(self)

    recloser_info = property(get_recloser_info, set_recloser_info)
    # >>> recloser_info


    def __str__(self):
        """ Returns a string representation of the RecloserAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< recloser_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RecloserAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RecloserAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.recloser_asset_model is not None:
            s += '%s<%s:RecloserAsset.recloser_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.recloser_asset_model.uri)
        if self.recloser_info is not None:
            s += '%s<%s:RecloserAsset.recloser_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.recloser_info.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RecloserAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> recloser_asset.serialize


class Tower(Structure):
    """ Large structure used to carry transmission lines, subtransmission lines, and/or other equipment/lines (e.g., communication). Dimensions of the Tower are specified in associated DimensionsInfo class.
    """
    # <<< tower
    # @generated
    def __init__(self, construction_kind='suspension', tower_asset_model=None, **kw_args):
        """ Initialises a new 'Tower' instance.
        """
        # Construction structure on the tower. Values are: "suspension", "tension"
        self.construction_kind = 'suspension'


        self._tower_asset_model = None
        self.tower_asset_model = tower_asset_model


        super(Tower, self).__init__(**kw_args)
    # >>> tower

    # <<< tower_asset_model
    # @generated
    def get_tower_asset_model(self):
        """ 
        """
        return self._tower_asset_model

    def set_tower_asset_model(self, value):
        if self._tower_asset_model is not None:
            filtered = [x for x in self.tower_asset_model.towers if x != self]
            self._tower_asset_model._towers = filtered

        self._tower_asset_model = value
        if self._tower_asset_model is not None:
            self._tower_asset_model._towers.append(self)

    tower_asset_model = property(get_tower_asset_model, set_tower_asset_model)
    # >>> tower_asset_model


    def __str__(self):
        """ Returns a string representation of the Tower.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tower.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Tower.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Tower", self.uri)
        if format:
            indent += ' ' * depth

        if self.tower_asset_model is not None:
            s += '%s<%s:Tower.tower_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tower_asset_model.uri)
        s += '%s<%s:Tower.construction_kind>%s</%s:Tower.construction_kind>' % \
            (indent, ns_prefix, self.construction_kind, ns_prefix)
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
        for obj in self.land_properties:
            s += '%s<%s:AssetContainer.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assets:
            s += '%s<%s:AssetContainer.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.seals:
            s += '%s<%s:AssetContainer.seals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.structure_supports:
            s += '%s<%s:Structure.structure_supports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Structure.material_kind>%s</%s:Structure.material_kind>' % \
            (indent, ns_prefix, self.material_kind, ns_prefix)
        s += '%s<%s:Structure.height>%s</%s:Structure.height>' % \
            (indent, ns_prefix, self.height, ns_prefix)
        s += '%s<%s:Structure.remove_weed>%s</%s:Structure.remove_weed>' % \
            (indent, ns_prefix, self.remove_weed, ns_prefix)
        s += '%s<%s:Structure.weed_removed_date>%s</%s:Structure.weed_removed_date>' % \
            (indent, ns_prefix, self.weed_removed_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_applied_date>%s</%s:Structure.fumigant_applied_date>' % \
            (indent, ns_prefix, self.fumigant_applied_date, ns_prefix)
        s += '%s<%s:Structure.fumigant_name>%s</%s:Structure.fumigant_name>' % \
            (indent, ns_prefix, self.fumigant_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Tower")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tower.serialize


class FaultIndicatorAsset(ElectricalAsset):
    """ Physical asset performing FaultIndicator function.
    """
    # <<< fault_indicator_asset
    # @generated
    def __init__(self, fault_indicator=None, fault_indicator_asset_model=None, **kw_args):
        """ Initialises a new 'FaultIndicatorAsset' instance.
        """

        self._fault_indicator = None
        self.fault_indicator = fault_indicator

        self._fault_indicator_asset_model = None
        self.fault_indicator_asset_model = fault_indicator_asset_model


        super(FaultIndicatorAsset, self).__init__(**kw_args)
    # >>> fault_indicator_asset

    # <<< fault_indicator
    # @generated
    def get_fault_indicator(self):
        """ 
        """
        return self._fault_indicator

    def set_fault_indicator(self, value):
        if self._fault_indicator is not None:
            filtered = [x for x in self.fault_indicator.fault_indicator_assets if x != self]
            self._fault_indicator._fault_indicator_assets = filtered

        self._fault_indicator = value
        if self._fault_indicator is not None:
            self._fault_indicator._fault_indicator_assets.append(self)

    fault_indicator = property(get_fault_indicator, set_fault_indicator)
    # >>> fault_indicator

    # <<< fault_indicator_asset_model
    # @generated
    def get_fault_indicator_asset_model(self):
        """ 
        """
        return self._fault_indicator_asset_model

    def set_fault_indicator_asset_model(self, value):
        if self._fault_indicator_asset_model is not None:
            filtered = [x for x in self.fault_indicator_asset_model.fault_indicator_assets if x != self]
            self._fault_indicator_asset_model._fault_indicator_assets = filtered

        self._fault_indicator_asset_model = value
        if self._fault_indicator_asset_model is not None:
            self._fault_indicator_asset_model._fault_indicator_assets.append(self)

    fault_indicator_asset_model = property(get_fault_indicator_asset_model, set_fault_indicator_asset_model)
    # >>> fault_indicator_asset_model


    def __str__(self):
        """ Returns a string representation of the FaultIndicatorAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< fault_indicator_asset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FaultIndicatorAsset.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FaultIndicatorAsset", self.uri)
        if format:
            indent += ' ' * depth

        if self.fault_indicator is not None:
            s += '%s<%s:FaultIndicatorAsset.fault_indicator rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.fault_indicator.uri)
        if self.fault_indicator_asset_model is not None:
            s += '%s<%s:FaultIndicatorAsset.fault_indicator_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.fault_indicator_asset_model.uri)
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
        for obj in self.electrical_infos:
            s += '%s<%s:ElectricalAsset.electrical_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:ElectricalAsset.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:ElectricalAsset.phase_code>%s</%s:ElectricalAsset.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:ElectricalAsset.is_connected>%s</%s:ElectricalAsset.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FaultIndicatorAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> fault_indicator_asset.serialize


class BreakerInfo(SwitchInfo):
    """ Properties of breakers.
    """
    # <<< breaker_info
    # @generated
    def __init__(self, phase_trip=0.0, breaker_assets=None, breaker_asset_models=None, breaker_type_asset=None, **kw_args):
        """ Initialises a new 'BreakerInfo' instance.
        """
        # Phase trip rating. 
        self.phase_trip = phase_trip


        self._breaker_assets = []
        if breaker_assets is not None:
            self.breaker_assets = breaker_assets
        else:
            self.breaker_assets = []

        self._breaker_asset_models = []
        if breaker_asset_models is not None:
            self.breaker_asset_models = breaker_asset_models
        else:
            self.breaker_asset_models = []

        self._breaker_type_asset = None
        self.breaker_type_asset = breaker_type_asset


        super(BreakerInfo, self).__init__(**kw_args)
    # >>> breaker_info

    # <<< breaker_assets
    # @generated
    def get_breaker_assets(self):
        """ 
        """
        return self._breaker_assets

    def set_breaker_assets(self, value):
        for x in self._breaker_assets:
            x._breaker_info = None
        for y in value:
            y._breaker_info = self
        self._breaker_assets = value

    breaker_assets = property(get_breaker_assets, set_breaker_assets)

    def add_breaker_assets(self, *breaker_assets):
        for obj in breaker_assets:
            obj._breaker_info = self
            self._breaker_assets.append(obj)

    def remove_breaker_assets(self, *breaker_assets):
        for obj in breaker_assets:
            obj._breaker_info = None
            self._breaker_assets.remove(obj)
    # >>> breaker_assets

    # <<< breaker_asset_models
    # @generated
    def get_breaker_asset_models(self):
        """ 
        """
        return self._breaker_asset_models

    def set_breaker_asset_models(self, value):
        for x in self._breaker_asset_models:
            x._breaker_info = None
        for y in value:
            y._breaker_info = self
        self._breaker_asset_models = value

    breaker_asset_models = property(get_breaker_asset_models, set_breaker_asset_models)

    def add_breaker_asset_models(self, *breaker_asset_models):
        for obj in breaker_asset_models:
            obj._breaker_info = self
            self._breaker_asset_models.append(obj)

    def remove_breaker_asset_models(self, *breaker_asset_models):
        for obj in breaker_asset_models:
            obj._breaker_info = None
            self._breaker_asset_models.remove(obj)
    # >>> breaker_asset_models

    # <<< breaker_type_asset
    # @generated
    def get_breaker_type_asset(self):
        """ 
        """
        return self._breaker_type_asset

    def set_breaker_type_asset(self, value):
        if self._breaker_type_asset is not None:
            self._breaker_type_asset._breaker_info = None

        self._breaker_type_asset = value
        if self._breaker_type_asset is not None:
            self._breaker_type_asset._breaker_info = self

    breaker_type_asset = property(get_breaker_type_asset, set_breaker_type_asset)
    # >>> breaker_type_asset


    def __str__(self):
        """ Returns a string representation of the BreakerInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< breaker_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BreakerInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BreakerInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.breaker_assets:
            s += '%s<%s:BreakerInfo.breaker_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.breaker_asset_models:
            s += '%s<%s:BreakerInfo.breaker_asset_models rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.breaker_type_asset is not None:
            s += '%s<%s:BreakerInfo.breaker_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.breaker_type_asset.uri)
        s += '%s<%s:BreakerInfo.phase_trip>%s</%s:BreakerInfo.phase_trip>' % \
            (indent, ns_prefix, self.phase_trip, ns_prefix)
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
        for obj in self.switch_assets:
            s += '%s<%s:SwitchInfo.switch_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.switch_asset_model is not None:
            s += '%s<%s:SwitchInfo.switch_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_asset_model.uri)
        if self.switch_type_asset is not None:
            s += '%s<%s:SwitchInfo.switch_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switch_type_asset.uri)
        s += '%s<%s:SwitchInfo.making_capacity>%s</%s:SwitchInfo.making_capacity>' % \
            (indent, ns_prefix, self.making_capacity, ns_prefix)
        s += '%s<%s:SwitchInfo.pole_count>%s</%s:SwitchInfo.pole_count>' % \
            (indent, ns_prefix, self.pole_count, ns_prefix)
        s += '%s<%s:SwitchInfo.interrupting_rating>%s</%s:SwitchInfo.interrupting_rating>' % \
            (indent, ns_prefix, self.interrupting_rating, ns_prefix)
        s += '%s<%s:SwitchInfo.withstand_current>%s</%s:SwitchInfo.withstand_current>' % \
            (indent, ns_prefix, self.withstand_current, ns_prefix)
        s += '%s<%s:SwitchInfo.minimum_current>%s</%s:SwitchInfo.minimum_current>' % \
            (indent, ns_prefix, self.minimum_current, ns_prefix)
        s += '%s<%s:SwitchInfo.load_break>%s</%s:SwitchInfo.load_break>' % \
            (indent, ns_prefix, self.load_break, ns_prefix)
        s += '%s<%s:SwitchInfo.gang>%s</%s:SwitchInfo.gang>' % \
            (indent, ns_prefix, self.gang, ns_prefix)
        s += '%s<%s:SwitchInfo.dielectric_strength>%s</%s:SwitchInfo.dielectric_strength>' % \
            (indent, ns_prefix, self.dielectric_strength, ns_prefix)
        s += '%s<%s:SwitchInfo.remote>%s</%s:SwitchInfo.remote>' % \
            (indent, ns_prefix, self.remote, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BreakerInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> breaker_info.serialize


# <<< inf_assets
# @generated
# >>> inf_assets
