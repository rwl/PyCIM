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


from cim.iec61970.core import IdentifiedObject
from cim.iec61968.metering import DeviceFunction

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infmetering"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfMetering"

class ComPort(IdentifiedObject):
    """ Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.
    """
    pass
    # <<< com_port
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ComPort' instance.
        """


        super(ComPort, self).__init__(**kw_args)
    # >>> com_port


    def __str__(self):
        """ Returns a string representation of the ComPort.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< com_port.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ComPort.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ComPort", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ComPort")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> com_port.serialize


class WaterMeteringFunction(DeviceFunction):
    """ Functionality performed by a water meter. It's entirely possible that the metering system would carry information to/from water meters even though it was built primarily to carry the higher-value electric meter data.
    """
    pass
    # <<< water_metering_function
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'WaterMeteringFunction' instance.
        """


        super(WaterMeteringFunction, self).__init__(**kw_args)
    # >>> water_metering_function


    def __str__(self):
        """ Returns a string representation of the WaterMeteringFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< water_metering_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WaterMeteringFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WaterMeteringFunction", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WaterMeteringFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> water_metering_function.serialize


class GasMeteringFunction(DeviceFunction):
    """ Functionality performed by a gas meter. It's entirely possible that the metering system would carry information to/from gas meters even though it was built primarily to carry the higher-value electric meter data.
    """
    pass
    # <<< gas_metering_function
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GasMeteringFunction' instance.
        """


        super(GasMeteringFunction, self).__init__(**kw_args)
    # >>> gas_metering_function


    def __str__(self):
        """ Returns a string representation of the GasMeteringFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gas_metering_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GasMeteringFunction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GasMeteringFunction", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "GasMeteringFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gas_metering_function.serialize


class MeteringFunctionConfiguration(IdentifiedObject):
    """ The configuration of data for a given meter function.
    """
    # <<< metering_function_configuration
    # @generated
    def __init__(self, electric_metering_functions=None, **kw_args):
        """ Initialises a new 'MeteringFunctionConfiguration' instance.
        """

        self._electric_metering_functions = []
        if electric_metering_functions is not None:
            self.electric_metering_functions = electric_metering_functions
        else:
            self.electric_metering_functions = []


        super(MeteringFunctionConfiguration, self).__init__(**kw_args)
    # >>> metering_function_configuration

    # <<< electric_metering_functions
    # @generated
    def get_electric_metering_functions(self):
        """ All electric metering functions with this configuration.
        """
        return self._electric_metering_functions

    def set_electric_metering_functions(self, value):
        for x in self._electric_metering_functions:
            x._metering_function_configuration = None
        for y in value:
            y._metering_function_configuration = self
        self._electric_metering_functions = value

    electric_metering_functions = property(get_electric_metering_functions, set_electric_metering_functions)

    def add_electric_metering_functions(self, *electric_metering_functions):
        for obj in electric_metering_functions:
            obj._metering_function_configuration = self
            self._electric_metering_functions.append(obj)

    def remove_electric_metering_functions(self, *electric_metering_functions):
        for obj in electric_metering_functions:
            obj._metering_function_configuration = None
            self._electric_metering_functions.remove(obj)
    # >>> electric_metering_functions


    def __str__(self):
        """ Returns a string representation of the MeteringFunctionConfiguration.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< metering_function_configuration.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeteringFunctionConfiguration.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeteringFunctionConfiguration", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.electric_metering_functions:
            s += '%s<%s:MeteringFunctionConfiguration.electric_metering_functions rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeteringFunctionConfiguration")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> metering_function_configuration.serialize


# <<< inf_metering
# @generated
# >>> inf_metering
