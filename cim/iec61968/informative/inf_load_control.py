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


from cim.iec61968.metering import DeviceFunction
from cim.iec61968.common import ActivityRecord

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infloadcontrol"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfLoadControl"

class LoadMgmtFunction(DeviceFunction):
    """ A collective function at an end device that manages the customer load.
    """
    # <<< load_mgmt_function
    # @generated
    def __init__(self, scheduling_basis='tariff_based', load_status='no_load', manual_over_ride=False, over_ride_time_out=0.0, remote_over_ride=False, is_auto_op=False, switches=None, load_mgmt_records=None, **kw_args):
        """ Initialises a new 'LoadMgmtFunction' instance.
        """
        # The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "tariff_based", "remote_control", "manual_control", "time_based"
        self.scheduling_basis = 'tariff_based'

        # The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "no_load", "full_load", "limited_load"
        self.load_status = 'no_load'

        # True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        self.manual_over_ride = manual_over_ride

        # After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        self.over_ride_time_out = over_ride_time_out

        # True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        self.remote_over_ride = remote_over_ride

        # True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        self.is_auto_op = is_auto_op


        self._switches = []
        if switches is not None:
            self.switches = switches
        else:
            self.switches = []

        self._load_mgmt_records = []
        if load_mgmt_records is not None:
            self.load_mgmt_records = load_mgmt_records
        else:
            self.load_mgmt_records = []


        super(LoadMgmtFunction, self).__init__(**kw_args)
    # >>> load_mgmt_function

    # <<< switches
    # @generated
    def get_switches(self):
        """ 
        """
        return self._switches

    def set_switches(self, value):
        for p in self._switches:
            filtered = [q for q in p.load_mgmt_functions if q != self]
            self._switches._load_mgmt_functions = filtered
        for r in value:
            if self not in r._load_mgmt_functions:
                r._load_mgmt_functions.append(self)
        self._switches = value

    switches = property(get_switches, set_switches)

    def add_switches(self, *switches):
        for obj in switches:
            if self not in obj._load_mgmt_functions:
                obj._load_mgmt_functions.append(self)
            self._switches.append(obj)

    def remove_switches(self, *switches):
        for obj in switches:
            if self in obj._load_mgmt_functions:
                obj._load_mgmt_functions.remove(self)
            self._switches.remove(obj)
    # >>> switches

    # <<< load_mgmt_records
    # @generated
    def get_load_mgmt_records(self):
        """ 
        """
        return self._load_mgmt_records

    def set_load_mgmt_records(self, value):
        for x in self._load_mgmt_records:
            x._load_mgmt_function = None
        for y in value:
            y._load_mgmt_function = self
        self._load_mgmt_records = value

    load_mgmt_records = property(get_load_mgmt_records, set_load_mgmt_records)

    def add_load_mgmt_records(self, *load_mgmt_records):
        for obj in load_mgmt_records:
            obj._load_mgmt_function = self
            self._load_mgmt_records.append(obj)

    def remove_load_mgmt_records(self, *load_mgmt_records):
        for obj in load_mgmt_records:
            obj._load_mgmt_function = None
            self._load_mgmt_records.remove(obj)
    # >>> load_mgmt_records


    def __str__(self):
        """ Returns a string representation of the LoadMgmtFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_mgmt_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadMgmtFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadMgmtFunction", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.switches:
            s += '%s<%s:LoadMgmtFunction.switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.load_mgmt_records:
            s += '%s<%s:LoadMgmtFunction.load_mgmt_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:LoadMgmtFunction.scheduling_basis>%s</%s:LoadMgmtFunction.scheduling_basis>' % \
            (indent, ns_prefix, self.scheduling_basis, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.load_status>%s</%s:LoadMgmtFunction.load_status>' % \
            (indent, ns_prefix, self.load_status, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.manual_over_ride>%s</%s:LoadMgmtFunction.manual_over_ride>' % \
            (indent, ns_prefix, self.manual_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.over_ride_time_out>%s</%s:LoadMgmtFunction.over_ride_time_out>' % \
            (indent, ns_prefix, self.over_ride_time_out, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.remote_over_ride>%s</%s:LoadMgmtFunction.remote_over_ride>' % \
            (indent, ns_prefix, self.remote_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.is_auto_op>%s</%s:LoadMgmtFunction.is_auto_op>' % \
            (indent, ns_prefix, self.is_auto_op, ns_prefix)
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
        if self.com_equipment_asset is not None:
            s += '%s<%s:DeviceFunction.com_equipment_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.com_equipment_asset.uri)
        if self.end_device_asset is not None:
            s += '%s<%s:DeviceFunction.end_device_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.end_device_asset.uri)
        for obj in self.registers:
            s += '%s<%s:DeviceFunction.registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_events:
            s += '%s<%s:DeviceFunction.end_device_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DeviceFunction.disabled>%s</%s:DeviceFunction.disabled>' % \
            (indent, ns_prefix, self.disabled, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadMgmtFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_mgmt_function.serialize


class LoadMgmtRecord(ActivityRecord):
    """ A log of actual measured load reductions as a result of load shed operations.
    """
    # <<< load_mgmt_record
    # @generated
    def __init__(self, load_reduction=0.0, load_mgmt_function=None, **kw_args):
        """ Initialises a new 'LoadMgmtRecord' instance.
        """
        # The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        self.load_reduction = load_reduction


        self._load_mgmt_function = None
        self.load_mgmt_function = load_mgmt_function


        super(LoadMgmtRecord, self).__init__(**kw_args)
    # >>> load_mgmt_record

    # <<< load_mgmt_function
    # @generated
    def get_load_mgmt_function(self):
        """ 
        """
        return self._load_mgmt_function

    def set_load_mgmt_function(self, value):
        if self._load_mgmt_function is not None:
            filtered = [x for x in self.load_mgmt_function.load_mgmt_records if x != self]
            self._load_mgmt_function._load_mgmt_records = filtered

        self._load_mgmt_function = value
        if self._load_mgmt_function is not None:
            self._load_mgmt_function._load_mgmt_records.append(self)

    load_mgmt_function = property(get_load_mgmt_function, set_load_mgmt_function)
    # >>> load_mgmt_function


    def __str__(self):
        """ Returns a string representation of the LoadMgmtRecord.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_mgmt_record.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadMgmtRecord.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadMgmtRecord", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_mgmt_function is not None:
            s += '%s<%s:LoadMgmtRecord.load_mgmt_function rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_mgmt_function.uri)
        s += '%s<%s:LoadMgmtRecord.load_reduction>%s</%s:LoadMgmtRecord.load_reduction>' % \
            (indent, ns_prefix, self.load_reduction, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadMgmtRecord")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_mgmt_record.serialize


class LoadLimitFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that limits the customer load to a given value.
    """
    # <<< load_limit_function
    # @generated
    def __init__(self, is_auto_recon_op=False, disconnect_time_delay=0.0, reconnect_time_delay=0.0, maximum_load=0.0, **kw_args):
        """ Initialises a new 'LoadLimitFunction' instance.
        """
        # True if the switch will reconnect automatically, otherwise it will reconnect under manual control. 
        self.is_auto_recon_op = is_auto_recon_op

        # From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations. 
        self.disconnect_time_delay = disconnect_time_delay

        # From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity. 
        self.reconnect_time_delay = reconnect_time_delay

        # The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load. 
        self.maximum_load = maximum_load



        super(LoadLimitFunction, self).__init__(**kw_args)
    # >>> load_limit_function


    def __str__(self):
        """ Returns a string representation of the LoadLimitFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_limit_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadLimitFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadLimitFunction", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadLimitFunction.is_auto_recon_op>%s</%s:LoadLimitFunction.is_auto_recon_op>' % \
            (indent, ns_prefix, self.is_auto_recon_op, ns_prefix)
        s += '%s<%s:LoadLimitFunction.disconnect_time_delay>%s</%s:LoadLimitFunction.disconnect_time_delay>' % \
            (indent, ns_prefix, self.disconnect_time_delay, ns_prefix)
        s += '%s<%s:LoadLimitFunction.reconnect_time_delay>%s</%s:LoadLimitFunction.reconnect_time_delay>' % \
            (indent, ns_prefix, self.reconnect_time_delay, ns_prefix)
        s += '%s<%s:LoadLimitFunction.maximum_load>%s</%s:LoadLimitFunction.maximum_load>' % \
            (indent, ns_prefix, self.maximum_load, ns_prefix)
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
        if self.com_equipment_asset is not None:
            s += '%s<%s:DeviceFunction.com_equipment_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.com_equipment_asset.uri)
        if self.end_device_asset is not None:
            s += '%s<%s:DeviceFunction.end_device_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.end_device_asset.uri)
        for obj in self.registers:
            s += '%s<%s:DeviceFunction.registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_events:
            s += '%s<%s:DeviceFunction.end_device_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DeviceFunction.disabled>%s</%s:DeviceFunction.disabled>' % \
            (indent, ns_prefix, self.disabled, ns_prefix)
        for obj in self.switches:
            s += '%s<%s:LoadMgmtFunction.switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.load_mgmt_records:
            s += '%s<%s:LoadMgmtFunction.load_mgmt_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:LoadMgmtFunction.scheduling_basis>%s</%s:LoadMgmtFunction.scheduling_basis>' % \
            (indent, ns_prefix, self.scheduling_basis, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.load_status>%s</%s:LoadMgmtFunction.load_status>' % \
            (indent, ns_prefix, self.load_status, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.manual_over_ride>%s</%s:LoadMgmtFunction.manual_over_ride>' % \
            (indent, ns_prefix, self.manual_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.over_ride_time_out>%s</%s:LoadMgmtFunction.over_ride_time_out>' % \
            (indent, ns_prefix, self.over_ride_time_out, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.remote_over_ride>%s</%s:LoadMgmtFunction.remote_over_ride>' % \
            (indent, ns_prefix, self.remote_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.is_auto_op>%s</%s:LoadMgmtFunction.is_auto_op>' % \
            (indent, ns_prefix, self.is_auto_op, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadLimitFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_limit_function.serialize


class LoadShedFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that sheds a part of the customer load.
    """
    # <<< load_shed_function
    # @generated
    def __init__(self, switched_load=0.0, **kw_args):
        """ Initialises a new 'LoadShedFunction' instance.
        """
        # The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value. 
        self.switched_load = switched_load



        super(LoadShedFunction, self).__init__(**kw_args)
    # >>> load_shed_function


    def __str__(self):
        """ Returns a string representation of the LoadShedFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_shed_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadShedFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadShedFunction", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadShedFunction.switched_load>%s</%s:LoadShedFunction.switched_load>' % \
            (indent, ns_prefix, self.switched_load, ns_prefix)
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
        if self.com_equipment_asset is not None:
            s += '%s<%s:DeviceFunction.com_equipment_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.com_equipment_asset.uri)
        if self.end_device_asset is not None:
            s += '%s<%s:DeviceFunction.end_device_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.end_device_asset.uri)
        for obj in self.registers:
            s += '%s<%s:DeviceFunction.registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_events:
            s += '%s<%s:DeviceFunction.end_device_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DeviceFunction.disabled>%s</%s:DeviceFunction.disabled>' % \
            (indent, ns_prefix, self.disabled, ns_prefix)
        for obj in self.switches:
            s += '%s<%s:LoadMgmtFunction.switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.load_mgmt_records:
            s += '%s<%s:LoadMgmtFunction.load_mgmt_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:LoadMgmtFunction.scheduling_basis>%s</%s:LoadMgmtFunction.scheduling_basis>' % \
            (indent, ns_prefix, self.scheduling_basis, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.load_status>%s</%s:LoadMgmtFunction.load_status>' % \
            (indent, ns_prefix, self.load_status, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.manual_over_ride>%s</%s:LoadMgmtFunction.manual_over_ride>' % \
            (indent, ns_prefix, self.manual_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.over_ride_time_out>%s</%s:LoadMgmtFunction.over_ride_time_out>' % \
            (indent, ns_prefix, self.over_ride_time_out, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.remote_over_ride>%s</%s:LoadMgmtFunction.remote_over_ride>' % \
            (indent, ns_prefix, self.remote_over_ride, ns_prefix)
        s += '%s<%s:LoadMgmtFunction.is_auto_op>%s</%s:LoadMgmtFunction.is_auto_op>' % \
            (indent, ns_prefix, self.is_auto_op, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadShedFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_shed_function.serialize


# <<< inf_load_control
# @generated
# >>> inf_load_control
