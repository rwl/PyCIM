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

""" This package is an extension of the Metering package and contains the information classes that support specialized applications such as demand-side management using load control equipment. These classes are generally associated with the point where a service is delivered to the customer.
"""

from cim.iec61968.metering import DeviceFunction
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.loadcontrol"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#LoadControl"

class ConnectDisconnectFunction(DeviceFunction):
    """ A function that will disconnect or reconnect the customer's load under defined conditions.
    """
    # <<< connect_disconnect_function
    # @generated
    def __init__(self, is_delayed_discon=False, is_connected=False, event_count=0, is_local_auto_discon_op=False, is_remote_auto_discon_op=False, is_remote_auto_recon_op=False, is_local_auto_recon_op=False, rcd_info=None, switches=None, **kw_args):
        """ Initialises a new 'ConnectDisconnectFunction' instance.
        """
        # If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting. 
        self.is_delayed_discon = is_delayed_discon

        # True if this function is in the connected state. 
        self.is_connected = is_connected

        # Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared. 
        self.event_count = event_count

        # (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually. 
        self.is_local_auto_discon_op = is_local_auto_discon_op

        # If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually. 
        self.is_remote_auto_discon_op = is_remote_auto_discon_op

        # If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually. 
        self.is_remote_auto_recon_op = is_remote_auto_recon_op

        # If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually. 
        self.is_local_auto_recon_op = is_local_auto_recon_op


        self.rcd_info = rcd_info

        self._switches = []
        if switches is not None:
            self.switches = switches
        else:
            self.switches = []


        super(ConnectDisconnectFunction, self).__init__(**kw_args)
    # >>> connect_disconnect_function

    # <<< rcd_info
    # @generated
    # Information on remote connect disconnect switch.
    rcd_info = None
    # >>> rcd_info

    # <<< switches
    # @generated
    def get_switches(self):
        """ 
        """
        return self._switches

    def set_switches(self, value):
        for p in self._switches:
            filtered = [q for q in p.connect_disconnect_functions if q != self]
            self._switches._connect_disconnect_functions = filtered
        for r in value:
            if self not in r._connect_disconnect_functions:
                r._connect_disconnect_functions.append(self)
        self._switches = value

    switches = property(get_switches, set_switches)

    def add_switches(self, *switches):
        for obj in switches:
            if self not in obj._connect_disconnect_functions:
                obj._connect_disconnect_functions.append(self)
            self._switches.append(obj)

    def remove_switches(self, *switches):
        for obj in switches:
            if self in obj._connect_disconnect_functions:
                obj._connect_disconnect_functions.remove(self)
            self._switches.remove(obj)
    # >>> switches


    def __str__(self):
        """ Returns a string representation of the ConnectDisconnectFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< connect_disconnect_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConnectDisconnectFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConnectDisconnectFunction", self.uri)
        if format:
            indent += ' ' * depth

        if self.rcd_info is not None:
            s += '%s<%s:ConnectDisconnectFunction.rcd_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rcd_info.uri)
        for obj in self.switches:
            s += '%s<%s:ConnectDisconnectFunction.switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConnectDisconnectFunction.is_delayed_discon>%s</%s:ConnectDisconnectFunction.is_delayed_discon>' % \
            (indent, ns_prefix, self.is_delayed_discon, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.is_connected>%s</%s:ConnectDisconnectFunction.is_connected>' % \
            (indent, ns_prefix, self.is_connected, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.event_count>%s</%s:ConnectDisconnectFunction.event_count>' % \
            (indent, ns_prefix, self.event_count, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.is_local_auto_discon_op>%s</%s:ConnectDisconnectFunction.is_local_auto_discon_op>' % \
            (indent, ns_prefix, self.is_local_auto_discon_op, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.is_remote_auto_discon_op>%s</%s:ConnectDisconnectFunction.is_remote_auto_discon_op>' % \
            (indent, ns_prefix, self.is_remote_auto_discon_op, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.is_remote_auto_recon_op>%s</%s:ConnectDisconnectFunction.is_remote_auto_recon_op>' % \
            (indent, ns_prefix, self.is_remote_auto_recon_op, ns_prefix)
        s += '%s<%s:ConnectDisconnectFunction.is_local_auto_recon_op>%s</%s:ConnectDisconnectFunction.is_local_auto_recon_op>' % \
            (indent, ns_prefix, self.is_local_auto_recon_op, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectDisconnectFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connect_disconnect_function.serialize


class RemoteConnectDisconnectInfo(Element):
    """ Details of remote connect disconnect function.
    """
    # <<< remote_connect_disconnect_info
    # @generated
    def __init__(self, is_arm_connect=False, customer_voltage_limit=0.0, power_limit=0.0, is_energy_limiting=False, energy_usage_warning=0.0, is_arm_disconnect=False, energy_usage_start_date_time='', needs_voltage_limit_check=False, energy_limit=0.0, armed_timeout=0.0, needs_power_limit_check=False, use_pushbutton=False, **kw_args):
        """ Initialises a new 'RemoteConnectDisconnectInfo' instance.
        """
        # True if the RCD switch must be armed before a connect action can be initiated. 
        self.is_arm_connect = is_arm_connect

        # Voltage limit on customer side of RCD switch above which the connect should not be made. 
        self.customer_voltage_limit = customer_voltage_limit

        # Load limit above which the connect should either not take place or should cause an immediate disconnect. 
        self.power_limit = power_limit

        # True if the energy usage is limited and the customer will be disconnected if they go over the limit. 
        self.is_energy_limiting = is_energy_limiting

        # Warning energy limit, used to trigger event code that energy usage is nearing limit. 
        self.energy_usage_warning = energy_usage_warning

        # True if the RCD switch must be armed before a disconnect action can be initiated. 
        self.is_arm_disconnect = is_arm_disconnect

        # Start date and time to accumulate energy for energy usage limiting. 
        self.energy_usage_start_date_time = energy_usage_start_date_time

        # True if voltage limit must be checked to prevent connect if voltage is over the limit. 
        self.needs_voltage_limit_check = needs_voltage_limit_check

        # Limit of energy before disconnect. 
        self.energy_limit = energy_limit

        # Setting of the timeout elapsed time. 
        self.armed_timeout = armed_timeout

        # True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit. 
        self.needs_power_limit_check = needs_power_limit_check

        # True if pushbutton must be used for connect. 
        self.use_pushbutton = use_pushbutton



        super(RemoteConnectDisconnectInfo, self).__init__(**kw_args)
    # >>> remote_connect_disconnect_info


    def __str__(self):
        """ Returns a string representation of the RemoteConnectDisconnectInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< remote_connect_disconnect_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RemoteConnectDisconnectInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RemoteConnectDisconnectInfo", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:RemoteConnectDisconnectInfo.is_arm_connect>%s</%s:RemoteConnectDisconnectInfo.is_arm_connect>' % \
            (indent, ns_prefix, self.is_arm_connect, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.customer_voltage_limit>%s</%s:RemoteConnectDisconnectInfo.customer_voltage_limit>' % \
            (indent, ns_prefix, self.customer_voltage_limit, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.power_limit>%s</%s:RemoteConnectDisconnectInfo.power_limit>' % \
            (indent, ns_prefix, self.power_limit, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.is_energy_limiting>%s</%s:RemoteConnectDisconnectInfo.is_energy_limiting>' % \
            (indent, ns_prefix, self.is_energy_limiting, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.energy_usage_warning>%s</%s:RemoteConnectDisconnectInfo.energy_usage_warning>' % \
            (indent, ns_prefix, self.energy_usage_warning, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.is_arm_disconnect>%s</%s:RemoteConnectDisconnectInfo.is_arm_disconnect>' % \
            (indent, ns_prefix, self.is_arm_disconnect, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.energy_usage_start_date_time>%s</%s:RemoteConnectDisconnectInfo.energy_usage_start_date_time>' % \
            (indent, ns_prefix, self.energy_usage_start_date_time, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.needs_voltage_limit_check>%s</%s:RemoteConnectDisconnectInfo.needs_voltage_limit_check>' % \
            (indent, ns_prefix, self.needs_voltage_limit_check, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.energy_limit>%s</%s:RemoteConnectDisconnectInfo.energy_limit>' % \
            (indent, ns_prefix, self.energy_limit, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.armed_timeout>%s</%s:RemoteConnectDisconnectInfo.armed_timeout>' % \
            (indent, ns_prefix, self.armed_timeout, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.needs_power_limit_check>%s</%s:RemoteConnectDisconnectInfo.needs_power_limit_check>' % \
            (indent, ns_prefix, self.needs_power_limit_check, ns_prefix)
        s += '%s<%s:RemoteConnectDisconnectInfo.use_pushbutton>%s</%s:RemoteConnectDisconnectInfo.use_pushbutton>' % \
            (indent, ns_prefix, self.use_pushbutton, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RemoteConnectDisconnectInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> remote_connect_disconnect_info.serialize


# <<< load_control
# @generated
# >>> load_control
