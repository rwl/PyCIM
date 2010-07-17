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

""" This package provides the capability to schedule and account for transactions for the exchange of electric power between companies. It includes transations for megawatts which are generated, consumed, lost, passed through, sold and purchased. These classes are used by Accounting and Billing for Energy, Generation Capacity, Transmission, and Ancillary Services.
"""

from cim.iec61968.common import Document
from cim.iec61970.core import Curve
from cim import Element
from cim.iec61970.core import IdentifiedObject
from cim.iec61970.control_area import ControlArea
from cim.iec61970.core import PowerSystemResource
from cim.iec61968.common import Agreement
from cim.iec61970.core import RegularIntervalSchedule

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.energyscheduling"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#EnergyScheduling"

class EnergyTransaction(Document):
    """ Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.
    """
    # <<< energy_transaction
    # @generated
    def __init__(self, receipt_point_p=0.0, energy_min=0.0, firm_interchange_flag=False, congest_charge_max=0.0, reason='', delivery_point_p=0.0, state=None, curtailment_profiles=None, export_sub_control_area=None, energy_trans_id=None, import_sub_control_area=None, energy_price_curves=None, loss_profiles=None, energy_profiles=None, energy_product=None, **kw_args):
        """ Initialises a new 'EnergyTransaction' instance.
        """
        # Receipt point active power 
        self.receipt_point_p = receipt_point_p

        # Transaction minimum active power if dispatchable 
        self.energy_min = energy_min

        # Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences. 
        self.firm_interchange_flag = firm_interchange_flag

        # Maximum congestion charges in monetary units 
        self.congest_charge_max = congest_charge_max

 
        self.reason = reason

        # Delivery point active power 
        self.delivery_point_p = delivery_point_p


        self.state = state

        self._curtailment_profiles = []
        if curtailment_profiles is not None:
            self.curtailment_profiles = curtailment_profiles
        else:
            self.curtailment_profiles = []

        self._export_sub_control_area = None
        self.export_sub_control_area = export_sub_control_area

        self._energy_trans_id = []
        if energy_trans_id is not None:
            self.energy_trans_id = energy_trans_id
        else:
            self.energy_trans_id = []

        self._import_sub_control_area = None
        self.import_sub_control_area = import_sub_control_area

        self._energy_price_curves = []
        if energy_price_curves is not None:
            self.energy_price_curves = energy_price_curves
        else:
            self.energy_price_curves = []

        self._loss_profiles = []
        if loss_profiles is not None:
            self.loss_profiles = loss_profiles
        else:
            self.loss_profiles = []

        self._energy_profiles = []
        if energy_profiles is not None:
            self.energy_profiles = energy_profiles
        else:
            self.energy_profiles = []

        self._energy_product = None
        self.energy_product = energy_product


        super(EnergyTransaction, self).__init__(**kw_args)
    # >>> energy_transaction

    # <<< state
    # @generated
    # { Approve | Deny | Study }
    state = None
    # >>> state

    # <<< curtailment_profiles
    # @generated
    def get_curtailment_profiles(self):
        """ An EnergyTransaction may be curtailed by any of the participating entities.
        """
        return self._curtailment_profiles

    def set_curtailment_profiles(self, value):
        for x in self._curtailment_profiles:
            x._energy_transaction = None
        for y in value:
            y._energy_transaction = self
        self._curtailment_profiles = value

    curtailment_profiles = property(get_curtailment_profiles, set_curtailment_profiles)

    def add_curtailment_profiles(self, *curtailment_profiles):
        for obj in curtailment_profiles:
            obj._energy_transaction = self
            self._curtailment_profiles.append(obj)

    def remove_curtailment_profiles(self, *curtailment_profiles):
        for obj in curtailment_profiles:
            obj._energy_transaction = None
            self._curtailment_profiles.remove(obj)
    # >>> curtailment_profiles

    # <<< export_sub_control_area
    # @generated
    def get_export_sub_control_area(self):
        """ Energy is transferred between interchange areas
        """
        return self._export_sub_control_area

    def set_export_sub_control_area(self, value):
        if self._export_sub_control_area is not None:
            filtered = [x for x in self.export_sub_control_area.export_energy_transactions if x != self]
            self._export_sub_control_area._export_energy_transactions = filtered

        self._export_sub_control_area = value
        if self._export_sub_control_area is not None:
            self._export_sub_control_area._export_energy_transactions.append(self)

    export_sub_control_area = property(get_export_sub_control_area, set_export_sub_control_area)
    # >>> export_sub_control_area

    # <<< energy_trans_id
    # @generated
    def get_energy_trans_id(self):
        """ 
        """
        return self._energy_trans_id

    def set_energy_trans_id(self, value):
        for x in self._energy_trans_id:
            x._energy_trans_id = None
        for y in value:
            y._energy_trans_id = self
        self._energy_trans_id = value

    energy_trans_id = property(get_energy_trans_id, set_energy_trans_id)

    def add_energy_trans_id(self, *energy_trans_id):
        for obj in energy_trans_id:
            obj._energy_trans_id = self
            self._energy_trans_id.append(obj)

    def remove_energy_trans_id(self, *energy_trans_id):
        for obj in energy_trans_id:
            obj._energy_trans_id = None
            self._energy_trans_id.remove(obj)
    # >>> energy_trans_id

    # <<< import_sub_control_area
    # @generated
    def get_import_sub_control_area(self):
        """ Energy is transferred between interchange areas
        """
        return self._import_sub_control_area

    def set_import_sub_control_area(self, value):
        if self._import_sub_control_area is not None:
            filtered = [x for x in self.import_sub_control_area.import_energy_transactions if x != self]
            self._import_sub_control_area._import_energy_transactions = filtered

        self._import_sub_control_area = value
        if self._import_sub_control_area is not None:
            self._import_sub_control_area._import_energy_transactions.append(self)

    import_sub_control_area = property(get_import_sub_control_area, set_import_sub_control_area)
    # >>> import_sub_control_area

    # <<< energy_price_curves
    # @generated
    def get_energy_price_curves(self):
        """ 
        """
        return self._energy_price_curves

    def set_energy_price_curves(self, value):
        for p in self._energy_price_curves:
            filtered = [q for q in p.energy_transactions if q != self]
            self._energy_price_curves._energy_transactions = filtered
        for r in value:
            if self not in r._energy_transactions:
                r._energy_transactions.append(self)
        self._energy_price_curves = value

    energy_price_curves = property(get_energy_price_curves, set_energy_price_curves)

    def add_energy_price_curves(self, *energy_price_curves):
        for obj in energy_price_curves:
            if self not in obj._energy_transactions:
                obj._energy_transactions.append(self)
            self._energy_price_curves.append(obj)

    def remove_energy_price_curves(self, *energy_price_curves):
        for obj in energy_price_curves:
            if self in obj._energy_transactions:
                obj._energy_transactions.remove(self)
            self._energy_price_curves.remove(obj)
    # >>> energy_price_curves

    # <<< loss_profiles
    # @generated
    def get_loss_profiles(self):
        """ An EnergyTransaction may have a LossProfile.
        """
        return self._loss_profiles

    def set_loss_profiles(self, value):
        for x in self._loss_profiles:
            x._energy_transaction = None
        for y in value:
            y._energy_transaction = self
        self._loss_profiles = value

    loss_profiles = property(get_loss_profiles, set_loss_profiles)

    def add_loss_profiles(self, *loss_profiles):
        for obj in loss_profiles:
            obj._energy_transaction = self
            self._loss_profiles.append(obj)

    def remove_loss_profiles(self, *loss_profiles):
        for obj in loss_profiles:
            obj._energy_transaction = None
            self._loss_profiles.remove(obj)
    # >>> loss_profiles

    # <<< energy_profiles
    # @generated
    def get_energy_profiles(self):
        """ An EnergyTransaction must have at least one EnergyProfile.
        """
        return self._energy_profiles

    def set_energy_profiles(self, value):
        for x in self._energy_profiles:
            x._energy_transaction = None
        for y in value:
            y._energy_transaction = self
        self._energy_profiles = value

    energy_profiles = property(get_energy_profiles, set_energy_profiles)

    def add_energy_profiles(self, *energy_profiles):
        for obj in energy_profiles:
            obj._energy_transaction = self
            self._energy_profiles.append(obj)

    def remove_energy_profiles(self, *energy_profiles):
        for obj in energy_profiles:
            obj._energy_transaction = None
            self._energy_profiles.remove(obj)
    # >>> energy_profiles

    # <<< energy_product
    # @generated
    def get_energy_product(self):
        """ The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        return self._energy_product

    def set_energy_product(self, value):
        if self._energy_product is not None:
            filtered = [x for x in self.energy_product.energy_transactions if x != self]
            self._energy_product._energy_transactions = filtered

        self._energy_product = value
        if self._energy_product is not None:
            self._energy_product._energy_transactions.append(self)

    energy_product = property(get_energy_product, set_energy_product)
    # >>> energy_product


    def __str__(self):
        """ Returns a string representation of the EnergyTransaction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_transaction.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyTransaction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyTransaction", self.uri)
        if format:
            indent += ' ' * depth

        if self.state is not None:
            s += '%s<%s:EnergyTransaction.state rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.state.uri)
        for obj in self.curtailment_profiles:
            s += '%s<%s:EnergyTransaction.curtailment_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.export_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.export_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.export_sub_control_area.uri)
        for obj in self.energy_trans_id:
            s += '%s<%s:EnergyTransaction.energy_trans_id rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.import_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.import_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.import_sub_control_area.uri)
        for obj in self.energy_price_curves:
            s += '%s<%s:EnergyTransaction.energy_price_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.loss_profiles:
            s += '%s<%s:EnergyTransaction.loss_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.energy_profiles:
            s += '%s<%s:EnergyTransaction.energy_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_product is not None:
            s += '%s<%s:EnergyTransaction.energy_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_product.uri)
        s += '%s<%s:EnergyTransaction.receipt_point_p>%s</%s:EnergyTransaction.receipt_point_p>' % \
            (indent, ns_prefix, self.receipt_point_p, ns_prefix)
        s += '%s<%s:EnergyTransaction.energy_min>%s</%s:EnergyTransaction.energy_min>' % \
            (indent, ns_prefix, self.energy_min, ns_prefix)
        s += '%s<%s:EnergyTransaction.firm_interchange_flag>%s</%s:EnergyTransaction.firm_interchange_flag>' % \
            (indent, ns_prefix, self.firm_interchange_flag, ns_prefix)
        s += '%s<%s:EnergyTransaction.congest_charge_max>%s</%s:EnergyTransaction.congest_charge_max>' % \
            (indent, ns_prefix, self.congest_charge_max, ns_prefix)
        s += '%s<%s:EnergyTransaction.reason>%s</%s:EnergyTransaction.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:EnergyTransaction.delivery_point_p>%s</%s:EnergyTransaction.delivery_point_p>' % \
            (indent, ns_prefix, self.delivery_point_p, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyTransaction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_transaction.serialize


class AvailableTransmissionCapacity(Curve):
    """ Amount of possible flow by direction.
    """
    # <<< available_transmission_capacity
    # @generated
    def __init__(self, schedule_for=None, **kw_args):
        """ Initialises a new 'AvailableTransmissionCapacity' instance.
        """

        self._schedule_for = []
        if schedule_for is not None:
            self.schedule_for = schedule_for
        else:
            self.schedule_for = []


        super(AvailableTransmissionCapacity, self).__init__(**kw_args)
    # >>> available_transmission_capacity

    # <<< schedule_for
    # @generated
    def get_schedule_for(self):
        """ A transmission schedule posts the available transmission capacity for a transmission line.
        """
        return self._schedule_for

    def set_schedule_for(self, value):
        for p in self._schedule_for:
            filtered = [q for q in p.scheduled_by if q != self]
            self._schedule_for._scheduled_by = filtered
        for r in value:
            if self not in r._scheduled_by:
                r._scheduled_by.append(self)
        self._schedule_for = value

    schedule_for = property(get_schedule_for, set_schedule_for)

    def add_schedule_for(self, *schedule_for):
        for obj in schedule_for:
            if self not in obj._scheduled_by:
                obj._scheduled_by.append(self)
            self._schedule_for.append(obj)

    def remove_schedule_for(self, *schedule_for):
        for obj in schedule_for:
            if self in obj._scheduled_by:
                obj._scheduled_by.remove(self)
            self._schedule_for.remove(obj)
    # >>> schedule_for


    def __str__(self):
        """ Returns a string representation of the AvailableTransmissionCapacity.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< available_transmission_capacity.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AvailableTransmissionCapacity.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AvailableTransmissionCapacity", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.schedule_for:
            s += '%s<%s:AvailableTransmissionCapacity.schedule_for rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AvailableTransmissionCapacity")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> available_transmission_capacity.serialize


class ProfileData(Element):
    """ Data for profile.
    """
    # <<< profile_data
    # @generated
    def __init__(self, stop_date_time='', energy_level=0.0, start_date_time='', capacity_level=0.0, sequence_number=0, profile=None, **kw_args):
        """ Initialises a new 'ProfileData' instance.
        """
        # Stop date/time for this profile. 
        self.stop_date_time = stop_date_time

        # Energy level for the profile 
        self.energy_level = energy_level

        # Start date/time for this profile. 
        self.start_date_time = start_date_time

        # Active power capacity level for the profile. 
        self.capacity_level = capacity_level

        # Sequence to provide item numbering for the profile. { greater than or equal to 1 } 
        self.sequence_number = sequence_number


        self._profile = []
        if profile is not None:
            self.profile = profile
        else:
            self.profile = []


        super(ProfileData, self).__init__(**kw_args)
    # >>> profile_data

    # <<< profile
    # @generated
    def get_profile(self):
        """ A profile has profile data associated with it.
        """
        return self._profile

    def set_profile(self, value):
        for p in self._profile:
            filtered = [q for q in p.profile_datas if q != self]
            self._profile._profile_datas = filtered
        for r in value:
            if self not in r._profile_datas:
                r._profile_datas.append(self)
        self._profile = value

    profile = property(get_profile, set_profile)

    def add_profile(self, *profile):
        for obj in profile:
            if self not in obj._profile_datas:
                obj._profile_datas.append(self)
            self._profile.append(obj)

    def remove_profile(self, *profile):
        for obj in profile:
            if self in obj._profile_datas:
                obj._profile_datas.remove(self)
            self._profile.remove(obj)
    # >>> profile


    def __str__(self):
        """ Returns a string representation of the ProfileData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< profile_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProfileData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProfileData", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.profile:
            s += '%s<%s:ProfileData.profile rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProfileData.stop_date_time>%s</%s:ProfileData.stop_date_time>' % \
            (indent, ns_prefix, self.stop_date_time, ns_prefix)
        s += '%s<%s:ProfileData.energy_level>%s</%s:ProfileData.energy_level>' % \
            (indent, ns_prefix, self.energy_level, ns_prefix)
        s += '%s<%s:ProfileData.start_date_time>%s</%s:ProfileData.start_date_time>' % \
            (indent, ns_prefix, self.start_date_time, ns_prefix)
        s += '%s<%s:ProfileData.capacity_level>%s</%s:ProfileData.capacity_level>' % \
            (indent, ns_prefix, self.capacity_level, ns_prefix)
        s += '%s<%s:ProfileData.sequence_number>%s</%s:ProfileData.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProfileData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> profile_data.serialize


class Profile(IdentifiedObject):
    """ A profile is a simpler curve type.
    """
    # <<< profile
    # @generated
    def __init__(self, profile_datas=None, **kw_args):
        """ Initialises a new 'Profile' instance.
        """

        self._profile_datas = []
        if profile_datas is not None:
            self.profile_datas = profile_datas
        else:
            self.profile_datas = []


        super(Profile, self).__init__(**kw_args)
    # >>> profile

    # <<< profile_datas
    # @generated
    def get_profile_datas(self):
        """ A profile has profile data associated with it.
        """
        return self._profile_datas

    def set_profile_datas(self, value):
        for p in self._profile_datas:
            filtered = [q for q in p.profile if q != self]
            self._profile_datas._profile = filtered
        for r in value:
            if self not in r._profile:
                r._profile.append(self)
        self._profile_datas = value

    profile_datas = property(get_profile_datas, set_profile_datas)

    def add_profile_datas(self, *profile_datas):
        for obj in profile_datas:
            if self not in obj._profile:
                obj._profile.append(self)
            self._profile_datas.append(obj)

    def remove_profile_datas(self, *profile_datas):
        for obj in profile_datas:
            if self in obj._profile:
                obj._profile.remove(self)
            self._profile_datas.remove(obj)
    # >>> profile_datas


    def __str__(self):
        """ Returns a string representation of the Profile.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< profile.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Profile.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Profile", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.profile_datas:
            s += '%s<%s:Profile.profile_datas rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Profile")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> profile.serialize


class SubControlArea(ControlArea):
    """ SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """
    # <<< sub_control_area
    # @generated
    def __init__(self, flowgate=None, export_energy_transactions=None, import_energy_transactions=None, host_control_area=None, part_of=None, side_a_tie_lines=None, generating_units=None, side_b_tie_lines=None, **kw_args):
        """ Initialises a new 'SubControlArea' instance.
        """

        self._flowgate = []
        if flowgate is not None:
            self.flowgate = flowgate
        else:
            self.flowgate = []

        self._export_energy_transactions = []
        if export_energy_transactions is not None:
            self.export_energy_transactions = export_energy_transactions
        else:
            self.export_energy_transactions = []

        self._import_energy_transactions = []
        if import_energy_transactions is not None:
            self.import_energy_transactions = import_energy_transactions
        else:
            self.import_energy_transactions = []

        self._host_control_area = None
        self.host_control_area = host_control_area

        self._part_of = []
        if part_of is not None:
            self.part_of = part_of
        else:
            self.part_of = []

        self._side_a_tie_lines = []
        if side_a_tie_lines is not None:
            self.side_a_tie_lines = side_a_tie_lines
        else:
            self.side_a_tie_lines = []

        self._generating_units = []
        if generating_units is not None:
            self.generating_units = generating_units
        else:
            self.generating_units = []

        self._side_b_tie_lines = []
        if side_b_tie_lines is not None:
            self.side_b_tie_lines = side_b_tie_lines
        else:
            self.side_b_tie_lines = []


        super(SubControlArea, self).__init__(**kw_args)
    # >>> sub_control_area

    # <<< flowgate
    # @generated
    def get_flowgate(self):
        """ A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        """
        return self._flowgate

    def set_flowgate(self, value):
        for x in self._flowgate:
            x._sub_control_area = None
        for y in value:
            y._sub_control_area = self
        self._flowgate = value

    flowgate = property(get_flowgate, set_flowgate)

    def add_flowgate(self, *flowgate):
        for obj in flowgate:
            obj._sub_control_area = self
            self._flowgate.append(obj)

    def remove_flowgate(self, *flowgate):
        for obj in flowgate:
            obj._sub_control_area = None
            self._flowgate.remove(obj)
    # >>> flowgate

    # <<< export_energy_transactions
    # @generated
    def get_export_energy_transactions(self):
        """ Energy is transferred between interchange areas
        """
        return self._export_energy_transactions

    def set_export_energy_transactions(self, value):
        for x in self._export_energy_transactions:
            x._export_sub_control_area = None
        for y in value:
            y._export_sub_control_area = self
        self._export_energy_transactions = value

    export_energy_transactions = property(get_export_energy_transactions, set_export_energy_transactions)

    def add_export_energy_transactions(self, *export_energy_transactions):
        for obj in export_energy_transactions:
            obj._export_sub_control_area = self
            self._export_energy_transactions.append(obj)

    def remove_export_energy_transactions(self, *export_energy_transactions):
        for obj in export_energy_transactions:
            obj._export_sub_control_area = None
            self._export_energy_transactions.remove(obj)
    # >>> export_energy_transactions

    # <<< import_energy_transactions
    # @generated
    def get_import_energy_transactions(self):
        """ Energy is transferred between interchange areas
        """
        return self._import_energy_transactions

    def set_import_energy_transactions(self, value):
        for x in self._import_energy_transactions:
            x._import_sub_control_area = None
        for y in value:
            y._import_sub_control_area = self
        self._import_energy_transactions = value

    import_energy_transactions = property(get_import_energy_transactions, set_import_energy_transactions)

    def add_import_energy_transactions(self, *import_energy_transactions):
        for obj in import_energy_transactions:
            obj._import_sub_control_area = self
            self._import_energy_transactions.append(obj)

    def remove_import_energy_transactions(self, *import_energy_transactions):
        for obj in import_energy_transactions:
            obj._import_sub_control_area = None
            self._import_energy_transactions.remove(obj)
    # >>> import_energy_transactions

    # <<< host_control_area
    # @generated
    def get_host_control_area(self):
        """ The interchange area  may operate as a control area
        """
        return self._host_control_area

    def set_host_control_area(self, value):
        if self._host_control_area is not None:
            filtered = [x for x in self.host_control_area.sub_control_areas if x != self]
            self._host_control_area._sub_control_areas = filtered

        self._host_control_area = value
        if self._host_control_area is not None:
            self._host_control_area._sub_control_areas.append(self)

    host_control_area = property(get_host_control_area, set_host_control_area)
    # >>> host_control_area

    # <<< part_of
    # @generated
    def get_part_of(self):
        """ A transmission path's service point is part of an interchange area
        """
        return self._part_of

    def set_part_of(self, value):
        for x in self._part_of:
            x._member_of = None
        for y in value:
            y._member_of = self
        self._part_of = value

    part_of = property(get_part_of, set_part_of)

    def add_part_of(self, *part_of):
        for obj in part_of:
            obj._member_of = self
            self._part_of.append(obj)

    def remove_part_of(self, *part_of):
        for obj in part_of:
            obj._member_of = None
            self._part_of.remove(obj)
    # >>> part_of

    # <<< side_a_tie_lines
    # @generated
    def get_side_a_tie_lines(self):
        """ The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._side_a_tie_lines

    def set_side_a_tie_lines(self, value):
        for x in self._side_a_tie_lines:
            x._side_a_sub_control_area = None
        for y in value:
            y._side_a_sub_control_area = self
        self._side_a_tie_lines = value

    side_a_tie_lines = property(get_side_a_tie_lines, set_side_a_tie_lines)

    def add_side_a_tie_lines(self, *side_a_tie_lines):
        for obj in side_a_tie_lines:
            obj._side_a_sub_control_area = self
            self._side_a_tie_lines.append(obj)

    def remove_side_a_tie_lines(self, *side_a_tie_lines):
        for obj in side_a_tie_lines:
            obj._side_a_sub_control_area = None
            self._side_a_tie_lines.remove(obj)
    # >>> side_a_tie_lines

    # <<< generating_units
    # @generated
    def get_generating_units(self):
        """ A GeneratingUnit injects energy into a SubControlArea.
        """
        return self._generating_units

    def set_generating_units(self, value):
        for x in self._generating_units:
            x._sub_control_area = None
        for y in value:
            y._sub_control_area = self
        self._generating_units = value

    generating_units = property(get_generating_units, set_generating_units)

    def add_generating_units(self, *generating_units):
        for obj in generating_units:
            obj._sub_control_area = self
            self._generating_units.append(obj)

    def remove_generating_units(self, *generating_units):
        for obj in generating_units:
            obj._sub_control_area = None
            self._generating_units.remove(obj)
    # >>> generating_units

    # <<< side_b_tie_lines
    # @generated
    def get_side_b_tie_lines(self):
        """ The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._side_b_tie_lines

    def set_side_b_tie_lines(self, value):
        for x in self._side_b_tie_lines:
            x._side_b_sub_control_area = None
        for y in value:
            y._side_b_sub_control_area = self
        self._side_b_tie_lines = value

    side_b_tie_lines = property(get_side_b_tie_lines, set_side_b_tie_lines)

    def add_side_b_tie_lines(self, *side_b_tie_lines):
        for obj in side_b_tie_lines:
            obj._side_b_sub_control_area = self
            self._side_b_tie_lines.append(obj)

    def remove_side_b_tie_lines(self, *side_b_tie_lines):
        for obj in side_b_tie_lines:
            obj._side_b_sub_control_area = None
            self._side_b_tie_lines.remove(obj)
    # >>> side_b_tie_lines


    def __str__(self):
        """ Returns a string representation of the SubControlArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sub_control_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubControlArea.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubControlArea", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.flowgate:
            s += '%s<%s:SubControlArea.flowgate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.export_energy_transactions:
            s += '%s<%s:SubControlArea.export_energy_transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.import_energy_transactions:
            s += '%s<%s:SubControlArea.import_energy_transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.host_control_area is not None:
            s += '%s<%s:SubControlArea.host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.host_control_area.uri)
        for obj in self.part_of:
            s += '%s<%s:SubControlArea.part_of rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.side_a_tie_lines:
            s += '%s<%s:SubControlArea.side_a_tie_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.generating_units:
            s += '%s<%s:SubControlArea.generating_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.side_b_tie_lines:
            s += '%s<%s:SubControlArea.side_b_tie_lines rdf:resource="#%s"/>' % \
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
        if self.energy_area is not None:
            s += '%s<%s:ControlArea.energy_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_area.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:ControlArea.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.tie_flow:
            s += '%s<%s:ControlArea.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ControlArea.type>%s</%s:ControlArea.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:ControlArea.p_tolerance>%s</%s:ControlArea.p_tolerance>' % \
            (indent, ns_prefix, self.p_tolerance, ns_prefix)
        s += '%s<%s:ControlArea.net_interchange>%s</%s:ControlArea.net_interchange>' % \
            (indent, ns_prefix, self.net_interchange, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubControlArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sub_control_area.serialize


class TransmissionRightOfWay(PowerSystemResource):
    """ A collection of transmission lines that are close proximity to each other.
    """
    # <<< transmission_right_of_way
    # @generated
    def __init__(self, transmission_corridor=None, lines=None, **kw_args):
        """ Initialises a new 'TransmissionRightOfWay' instance.
        """

        self._transmission_corridor = None
        self.transmission_corridor = transmission_corridor

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []


        super(TransmissionRightOfWay, self).__init__(**kw_args)
    # >>> transmission_right_of_way

    # <<< transmission_corridor
    # @generated
    def get_transmission_corridor(self):
        """ A transmission right-of-way is a member of a transmission corridor
        """
        return self._transmission_corridor

    def set_transmission_corridor(self, value):
        if self._transmission_corridor is not None:
            filtered = [x for x in self.transmission_corridor.transmission_right_of_ways if x != self]
            self._transmission_corridor._transmission_right_of_ways = filtered

        self._transmission_corridor = value
        if self._transmission_corridor is not None:
            self._transmission_corridor._transmission_right_of_ways.append(self)

    transmission_corridor = property(get_transmission_corridor, set_transmission_corridor)
    # >>> transmission_corridor

    # <<< lines
    # @generated
    def get_lines(self):
        """ A transmission line can be part of a transmission corridor
        """
        return self._lines

    def set_lines(self, value):
        for x in self._lines:
            x._transmission_right_of_way = None
        for y in value:
            y._transmission_right_of_way = self
        self._lines = value

    lines = property(get_lines, set_lines)

    def add_lines(self, *lines):
        for obj in lines:
            obj._transmission_right_of_way = self
            self._lines.append(obj)

    def remove_lines(self, *lines):
        for obj in lines:
            obj._transmission_right_of_way = None
            self._lines.remove(obj)
    # >>> lines


    def __str__(self):
        """ Returns a string representation of the TransmissionRightOfWay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transmission_right_of_way.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransmissionRightOfWay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransmissionRightOfWay", self.uri)
        if format:
            indent += ' ' * depth

        if self.transmission_corridor is not None:
            s += '%s<%s:TransmissionRightOfWay.transmission_corridor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transmission_corridor.uri)
        for obj in self.lines:
            s += '%s<%s:TransmissionRightOfWay.lines rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransmissionRightOfWay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transmission_right_of_way.serialize


class EnergySchedulingVersion(Element):
    # <<< energy_scheduling_version
    # @generated
    def __init__(self, date='', version='', **kw_args):
        """ Initialises a new 'EnergySchedulingVersion' instance.
        """
 
        self.date = date

        # v 4 moved SubControlArea 
        self.version = version



        super(EnergySchedulingVersion, self).__init__(**kw_args)
    # >>> energy_scheduling_version


    def __str__(self):
        """ Returns a string representation of the EnergySchedulingVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_scheduling_version.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergySchedulingVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergySchedulingVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:EnergySchedulingVersion.date>%s</%s:EnergySchedulingVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        s += '%s<%s:EnergySchedulingVersion.version>%s</%s:EnergySchedulingVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergySchedulingVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_scheduling_version.serialize


class HostControlArea(IdentifiedObject):
    """ A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.
    """
    # <<< host_control_area
    # @generated
    def __init__(self, area_control_mode='off', freq_set_point=0.0, inadvertent_accounts=None, area_reserve_spec=None, frequency_bias_factor=None, side_a_tie_lines=None, sub_control_areas=None, side_b_tie_lines=None, receive_dynamic_schedules=None, send_dynamic_schedules=None, controls=None, **kw_args):
        """ Initialises a new 'HostControlArea' instance.
        """
        # The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control) Values are: "off", "tlb", "cf", "ctl"
        self.area_control_mode = 'off'

        # The present power system frequency set point for automatic generation control 
        self.freq_set_point = freq_set_point


        self._inadvertent_accounts = []
        if inadvertent_accounts is not None:
            self.inadvertent_accounts = inadvertent_accounts
        else:
            self.inadvertent_accounts = []

        self._area_reserve_spec = None
        self.area_reserve_spec = area_reserve_spec

        self.frequency_bias_factor = frequency_bias_factor

        self._side_a_tie_lines = []
        if side_a_tie_lines is not None:
            self.side_a_tie_lines = side_a_tie_lines
        else:
            self.side_a_tie_lines = []

        self._sub_control_areas = []
        if sub_control_areas is not None:
            self.sub_control_areas = sub_control_areas
        else:
            self.sub_control_areas = []

        self._side_b_tie_lines = []
        if side_b_tie_lines is not None:
            self.side_b_tie_lines = side_b_tie_lines
        else:
            self.side_b_tie_lines = []

        self._receive_dynamic_schedules = []
        if receive_dynamic_schedules is not None:
            self.receive_dynamic_schedules = receive_dynamic_schedules
        else:
            self.receive_dynamic_schedules = []

        self._send_dynamic_schedules = []
        if send_dynamic_schedules is not None:
            self.send_dynamic_schedules = send_dynamic_schedules
        else:
            self.send_dynamic_schedules = []

        self._controls = None
        self.controls = controls


        super(HostControlArea, self).__init__(**kw_args)
    # >>> host_control_area

    # <<< inadvertent_accounts
    # @generated
    def get_inadvertent_accounts(self):
        """ A control area can have one or more net inadvertent interchange accounts
        """
        return self._inadvertent_accounts

    def set_inadvertent_accounts(self, value):
        for x in self._inadvertent_accounts:
            x._host_control_area = None
        for y in value:
            y._host_control_area = self
        self._inadvertent_accounts = value

    inadvertent_accounts = property(get_inadvertent_accounts, set_inadvertent_accounts)

    def add_inadvertent_accounts(self, *inadvertent_accounts):
        for obj in inadvertent_accounts:
            obj._host_control_area = self
            self._inadvertent_accounts.append(obj)

    def remove_inadvertent_accounts(self, *inadvertent_accounts):
        for obj in inadvertent_accounts:
            obj._host_control_area = None
            self._inadvertent_accounts.remove(obj)
    # >>> inadvertent_accounts

    # <<< area_reserve_spec
    # @generated
    def get_area_reserve_spec(self):
        """ A control area has one or more area reserve specifications
        """
        return self._area_reserve_spec

    def set_area_reserve_spec(self, value):
        if self._area_reserve_spec is not None:
            filtered = [x for x in self.area_reserve_spec.host_control_areas if x != self]
            self._area_reserve_spec._host_control_areas = filtered

        self._area_reserve_spec = value
        if self._area_reserve_spec is not None:
            self._area_reserve_spec._host_control_areas.append(self)

    area_reserve_spec = property(get_area_reserve_spec, set_area_reserve_spec)
    # >>> area_reserve_spec

    # <<< frequency_bias_factor
    # @generated
    # The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC)
    frequency_bias_factor = None
    # >>> frequency_bias_factor

    # <<< side_a_tie_lines
    # @generated
    def get_side_a_tie_lines(self):
        """ A HostControlArea can have zero or more tie lines.
        """
        return self._side_a_tie_lines

    def set_side_a_tie_lines(self, value):
        for x in self._side_a_tie_lines:
            x._side_a_host_control_area = None
        for y in value:
            y._side_a_host_control_area = self
        self._side_a_tie_lines = value

    side_a_tie_lines = property(get_side_a_tie_lines, set_side_a_tie_lines)

    def add_side_a_tie_lines(self, *side_a_tie_lines):
        for obj in side_a_tie_lines:
            obj._side_a_host_control_area = self
            self._side_a_tie_lines.append(obj)

    def remove_side_a_tie_lines(self, *side_a_tie_lines):
        for obj in side_a_tie_lines:
            obj._side_a_host_control_area = None
            self._side_a_tie_lines.remove(obj)
    # >>> side_a_tie_lines

    # <<< sub_control_areas
    # @generated
    def get_sub_control_areas(self):
        """ The interchange area  may operate as a control area
        """
        return self._sub_control_areas

    def set_sub_control_areas(self, value):
        for x in self._sub_control_areas:
            x._host_control_area = None
        for y in value:
            y._host_control_area = self
        self._sub_control_areas = value

    sub_control_areas = property(get_sub_control_areas, set_sub_control_areas)

    def add_sub_control_areas(self, *sub_control_areas):
        for obj in sub_control_areas:
            obj._host_control_area = self
            self._sub_control_areas.append(obj)

    def remove_sub_control_areas(self, *sub_control_areas):
        for obj in sub_control_areas:
            obj._host_control_area = None
            self._sub_control_areas.remove(obj)
    # >>> sub_control_areas

    # <<< side_b_tie_lines
    # @generated
    def get_side_b_tie_lines(self):
        """ A HostControlArea can have zero or more tie lines.
        """
        return self._side_b_tie_lines

    def set_side_b_tie_lines(self, value):
        for x in self._side_b_tie_lines:
            x._side_b_host_control_area = None
        for y in value:
            y._side_b_host_control_area = self
        self._side_b_tie_lines = value

    side_b_tie_lines = property(get_side_b_tie_lines, set_side_b_tie_lines)

    def add_side_b_tie_lines(self, *side_b_tie_lines):
        for obj in side_b_tie_lines:
            obj._side_b_host_control_area = self
            self._side_b_tie_lines.append(obj)

    def remove_side_b_tie_lines(self, *side_b_tie_lines):
        for obj in side_b_tie_lines:
            obj._side_b_host_control_area = None
            self._side_b_tie_lines.remove(obj)
    # >>> side_b_tie_lines

    # <<< receive_dynamic_schedules
    # @generated
    def get_receive_dynamic_schedules(self):
        """ A control area can receive dynamic schedules from other control areas
        """
        return self._receive_dynamic_schedules

    def set_receive_dynamic_schedules(self, value):
        for x in self._receive_dynamic_schedules:
            x._receive_host_control_area = None
        for y in value:
            y._receive_host_control_area = self
        self._receive_dynamic_schedules = value

    receive_dynamic_schedules = property(get_receive_dynamic_schedules, set_receive_dynamic_schedules)

    def add_receive_dynamic_schedules(self, *receive_dynamic_schedules):
        for obj in receive_dynamic_schedules:
            obj._receive_host_control_area = self
            self._receive_dynamic_schedules.append(obj)

    def remove_receive_dynamic_schedules(self, *receive_dynamic_schedules):
        for obj in receive_dynamic_schedules:
            obj._receive_host_control_area = None
            self._receive_dynamic_schedules.remove(obj)
    # >>> receive_dynamic_schedules

    # <<< send_dynamic_schedules
    # @generated
    def get_send_dynamic_schedules(self):
        """ A control area can send dynamic schedules to other control areas
        """
        return self._send_dynamic_schedules

    def set_send_dynamic_schedules(self, value):
        for x in self._send_dynamic_schedules:
            x._send_host_control_area = None
        for y in value:
            y._send_host_control_area = self
        self._send_dynamic_schedules = value

    send_dynamic_schedules = property(get_send_dynamic_schedules, set_send_dynamic_schedules)

    def add_send_dynamic_schedules(self, *send_dynamic_schedules):
        for obj in send_dynamic_schedules:
            obj._send_host_control_area = self
            self._send_dynamic_schedules.append(obj)

    def remove_send_dynamic_schedules(self, *send_dynamic_schedules):
        for obj in send_dynamic_schedules:
            obj._send_host_control_area = None
            self._send_dynamic_schedules.remove(obj)
    # >>> send_dynamic_schedules

    # <<< controls
    # @generated
    def get_controls(self):
        """ A ControlAreaCompany controls a ControlArea.
        """
        return self._controls

    def set_controls(self, value):
        if self._controls is not None:
            self._controls._controlled_by = None

        self._controls = value
        if self._controls is not None:
            self._controls._controlled_by = self

    controls = property(get_controls, set_controls)
    # >>> controls


    def __str__(self):
        """ Returns a string representation of the HostControlArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< host_control_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the HostControlArea.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "HostControlArea", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.inadvertent_accounts:
            s += '%s<%s:HostControlArea.inadvertent_accounts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.area_reserve_spec is not None:
            s += '%s<%s:HostControlArea.area_reserve_spec rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.area_reserve_spec.uri)
        if self.frequency_bias_factor is not None:
            s += '%s<%s:HostControlArea.frequency_bias_factor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.frequency_bias_factor.uri)
        for obj in self.side_a_tie_lines:
            s += '%s<%s:HostControlArea.side_a_tie_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.sub_control_areas:
            s += '%s<%s:HostControlArea.sub_control_areas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.side_b_tie_lines:
            s += '%s<%s:HostControlArea.side_b_tie_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.receive_dynamic_schedules:
            s += '%s<%s:HostControlArea.receive_dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.send_dynamic_schedules:
            s += '%s<%s:HostControlArea.send_dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.controls is not None:
            s += '%s<%s:HostControlArea.controls rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controls.uri)
        s += '%s<%s:HostControlArea.area_control_mode>%s</%s:HostControlArea.area_control_mode>' % \
            (indent, ns_prefix, self.area_control_mode, ns_prefix)
        s += '%s<%s:HostControlArea.freq_set_point>%s</%s:HostControlArea.freq_set_point>' % \
            (indent, ns_prefix, self.freq_set_point, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "HostControlArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> host_control_area.serialize


class InadvertentAccount(Curve):
    """ An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.
    """
    # <<< inadvertent_account
    # @generated
    def __init__(self, host_control_area=None, **kw_args):
        """ Initialises a new 'InadvertentAccount' instance.
        """

        self._host_control_area = None
        self.host_control_area = host_control_area


        super(InadvertentAccount, self).__init__(**kw_args)
    # >>> inadvertent_account

    # <<< host_control_area
    # @generated
    def get_host_control_area(self):
        """ A control area can have one or more net inadvertent interchange accounts
        """
        return self._host_control_area

    def set_host_control_area(self, value):
        if self._host_control_area is not None:
            filtered = [x for x in self.host_control_area.inadvertent_accounts if x != self]
            self._host_control_area._inadvertent_accounts = filtered

        self._host_control_area = value
        if self._host_control_area is not None:
            self._host_control_area._inadvertent_accounts.append(self)

    host_control_area = property(get_host_control_area, set_host_control_area)
    # >>> host_control_area


    def __str__(self):
        """ Returns a string representation of the InadvertentAccount.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< inadvertent_account.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the InadvertentAccount.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "InadvertentAccount", self.uri)
        if format:
            indent += ' ' * depth

        if self.host_control_area is not None:
            s += '%s<%s:InadvertentAccount.host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.host_control_area.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "InadvertentAccount")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> inadvertent_account.serialize


class TransmissionCorridor(PowerSystemResource):
    """ A corridor containing one or more rights of way
    """
    # <<< transmission_corridor
    # @generated
    def __init__(self, transmission_right_of_ways=None, contained_in=None, **kw_args):
        """ Initialises a new 'TransmissionCorridor' instance.
        """

        self._transmission_right_of_ways = []
        if transmission_right_of_ways is not None:
            self.transmission_right_of_ways = transmission_right_of_ways
        else:
            self.transmission_right_of_ways = []

        self._contained_in = []
        if contained_in is not None:
            self.contained_in = contained_in
        else:
            self.contained_in = []


        super(TransmissionCorridor, self).__init__(**kw_args)
    # >>> transmission_corridor

    # <<< transmission_right_of_ways
    # @generated
    def get_transmission_right_of_ways(self):
        """ A transmission right-of-way is a member of a transmission corridor
        """
        return self._transmission_right_of_ways

    def set_transmission_right_of_ways(self, value):
        for x in self._transmission_right_of_ways:
            x._transmission_corridor = None
        for y in value:
            y._transmission_corridor = self
        self._transmission_right_of_ways = value

    transmission_right_of_ways = property(get_transmission_right_of_ways, set_transmission_right_of_ways)

    def add_transmission_right_of_ways(self, *transmission_right_of_ways):
        for obj in transmission_right_of_ways:
            obj._transmission_corridor = self
            self._transmission_right_of_ways.append(obj)

    def remove_transmission_right_of_ways(self, *transmission_right_of_ways):
        for obj in transmission_right_of_ways:
            obj._transmission_corridor = None
            self._transmission_right_of_ways.remove(obj)
    # >>> transmission_right_of_ways

    # <<< contained_in
    # @generated
    def get_contained_in(self):
        """ A TransmissionPath is contained in a TransmissionCorridor.
        """
        return self._contained_in

    def set_contained_in(self, value):
        for x in self._contained_in:
            x._for = None
        for y in value:
            y._for = self
        self._contained_in = value

    contained_in = property(get_contained_in, set_contained_in)

    def add_contained_in(self, *contained_in):
        for obj in contained_in:
            obj._for = self
            self._contained_in.append(obj)

    def remove_contained_in(self, *contained_in):
        for obj in contained_in:
            obj._for = None
            self._contained_in.remove(obj)
    # >>> contained_in


    def __str__(self):
        """ Returns a string representation of the TransmissionCorridor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transmission_corridor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransmissionCorridor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransmissionCorridor", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.transmission_right_of_ways:
            s += '%s<%s:TransmissionCorridor.transmission_right_of_ways rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contained_in:
            s += '%s<%s:TransmissionCorridor.contained_in rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransmissionCorridor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transmission_corridor.serialize


class AreaReserveSpec(Element):
    """ The control area's reserve specification
    """
    # <<< area_reserve_spec
    # @generated
    def __init__(self, area_reserve_spec_name='', raise_reg_margin_reqt=0.0, lower_reg_margin_reqt=0.0, primary_reserve_reqt=0.0, op_reserve_reqt=0.0, spinning_reserve_reqt=0.0, host_control_areas=None, reserve_energy_transaction=None, **kw_args):
        """ Initialises a new 'AreaReserveSpec' instance.
        """
        # The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations. 
        self.area_reserve_spec_name = area_reserve_spec_name

        # Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes 
        self.raise_reg_margin_reqt = raise_reg_margin_reqt

        # Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes 
        self.lower_reg_margin_reqt = lower_reg_margin_reqt

        # Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve. 
        self.primary_reserve_reqt = primary_reserve_reqt

        # Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min). 
        self.op_reserve_reqt = op_reserve_reqt

        # Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes 
        self.spinning_reserve_reqt = spinning_reserve_reqt


        self._host_control_areas = []
        if host_control_areas is not None:
            self.host_control_areas = host_control_areas
        else:
            self.host_control_areas = []

        self._reserve_energy_transaction = None
        self.reserve_energy_transaction = reserve_energy_transaction


        super(AreaReserveSpec, self).__init__(**kw_args)
    # >>> area_reserve_spec

    # <<< host_control_areas
    # @generated
    def get_host_control_areas(self):
        """ A control area has one or more area reserve specifications
        """
        return self._host_control_areas

    def set_host_control_areas(self, value):
        for x in self._host_control_areas:
            x._area_reserve_spec = None
        for y in value:
            y._area_reserve_spec = self
        self._host_control_areas = value

    host_control_areas = property(get_host_control_areas, set_host_control_areas)

    def add_host_control_areas(self, *host_control_areas):
        for obj in host_control_areas:
            obj._area_reserve_spec = self
            self._host_control_areas.append(obj)

    def remove_host_control_areas(self, *host_control_areas):
        for obj in host_control_areas:
            obj._area_reserve_spec = None
            self._host_control_areas.remove(obj)
    # >>> host_control_areas

    # <<< reserve_energy_transaction
    # @generated
    def get_reserve_energy_transaction(self):
        """ A Reserve type of energy transaction can count towards an area reserve specification.
        """
        return self._reserve_energy_transaction

    def set_reserve_energy_transaction(self, value):
        if self._reserve_energy_transaction is not None:
            filtered = [x for x in self.reserve_energy_transaction.area_reserve_spec if x != self]
            self._reserve_energy_transaction._area_reserve_spec = filtered

        self._reserve_energy_transaction = value
        if self._reserve_energy_transaction is not None:
            self._reserve_energy_transaction._area_reserve_spec.append(self)

    reserve_energy_transaction = property(get_reserve_energy_transaction, set_reserve_energy_transaction)
    # >>> reserve_energy_transaction


    def __str__(self):
        """ Returns a string representation of the AreaReserveSpec.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< area_reserve_spec.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AreaReserveSpec.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AreaReserveSpec", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.host_control_areas:
            s += '%s<%s:AreaReserveSpec.host_control_areas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.reserve_energy_transaction is not None:
            s += '%s<%s:AreaReserveSpec.reserve_energy_transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reserve_energy_transaction.uri)
        s += '%s<%s:AreaReserveSpec.area_reserve_spec_name>%s</%s:AreaReserveSpec.area_reserve_spec_name>' % \
            (indent, ns_prefix, self.area_reserve_spec_name, ns_prefix)
        s += '%s<%s:AreaReserveSpec.raise_reg_margin_reqt>%s</%s:AreaReserveSpec.raise_reg_margin_reqt>' % \
            (indent, ns_prefix, self.raise_reg_margin_reqt, ns_prefix)
        s += '%s<%s:AreaReserveSpec.lower_reg_margin_reqt>%s</%s:AreaReserveSpec.lower_reg_margin_reqt>' % \
            (indent, ns_prefix, self.lower_reg_margin_reqt, ns_prefix)
        s += '%s<%s:AreaReserveSpec.primary_reserve_reqt>%s</%s:AreaReserveSpec.primary_reserve_reqt>' % \
            (indent, ns_prefix, self.primary_reserve_reqt, ns_prefix)
        s += '%s<%s:AreaReserveSpec.op_reserve_reqt>%s</%s:AreaReserveSpec.op_reserve_reqt>' % \
            (indent, ns_prefix, self.op_reserve_reqt, ns_prefix)
        s += '%s<%s:AreaReserveSpec.spinning_reserve_reqt>%s</%s:AreaReserveSpec.spinning_reserve_reqt>' % \
            (indent, ns_prefix, self.spinning_reserve_reqt, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AreaReserveSpec")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> area_reserve_spec.serialize


class EnergyProduct(Agreement):
    """ An EnergyProduct is offered commercially as a ContractOrTariff.
    """
    # <<< energy_product
    # @generated
    def __init__(self, service_point=None, generation_provider=None, energy_transactions=None, resold_by_marketers=None, title_held_by_marketer=None, **kw_args):
        """ Initialises a new 'EnergyProduct' instance.
        """

        self._service_point = []
        if service_point is not None:
            self.service_point = service_point
        else:
            self.service_point = []

        self._generation_provider = None
        self.generation_provider = generation_provider

        self._energy_transactions = []
        if energy_transactions is not None:
            self.energy_transactions = energy_transactions
        else:
            self.energy_transactions = []

        self._resold_by_marketers = []
        if resold_by_marketers is not None:
            self.resold_by_marketers = resold_by_marketers
        else:
            self.resold_by_marketers = []

        self._title_held_by_marketer = None
        self.title_held_by_marketer = title_held_by_marketer


        super(EnergyProduct, self).__init__(**kw_args)
    # >>> energy_product

    # <<< service_point
    # @generated
    def get_service_point(self):
        """ An EnergyProduct injects energy into a service point.
        """
        return self._service_point

    def set_service_point(self, value):
        for p in self._service_point:
            filtered = [q for q in p.energy_products if q != self]
            self._service_point._energy_products = filtered
        for r in value:
            if self not in r._energy_products:
                r._energy_products.append(self)
        self._service_point = value

    service_point = property(get_service_point, set_service_point)

    def add_service_point(self, *service_point):
        for obj in service_point:
            if self not in obj._energy_products:
                obj._energy_products.append(self)
            self._service_point.append(obj)

    def remove_service_point(self, *service_point):
        for obj in service_point:
            if self in obj._energy_products:
                obj._energy_products.remove(self)
            self._service_point.remove(obj)
    # >>> service_point

    # <<< generation_provider
    # @generated
    def get_generation_provider(self):
        """ 
        """
        return self._generation_provider

    def set_generation_provider(self, value):
        if self._generation_provider is not None:
            filtered = [x for x in self.generation_provider.energy_products if x != self]
            self._generation_provider._energy_products = filtered

        self._generation_provider = value
        if self._generation_provider is not None:
            self._generation_provider._energy_products.append(self)

    generation_provider = property(get_generation_provider, set_generation_provider)
    # >>> generation_provider

    # <<< energy_transactions
    # @generated
    def get_energy_transactions(self):
        """ The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        return self._energy_transactions

    def set_energy_transactions(self, value):
        for x in self._energy_transactions:
            x._energy_product = None
        for y in value:
            y._energy_product = self
        self._energy_transactions = value

    energy_transactions = property(get_energy_transactions, set_energy_transactions)

    def add_energy_transactions(self, *energy_transactions):
        for obj in energy_transactions:
            obj._energy_product = self
            self._energy_transactions.append(obj)

    def remove_energy_transactions(self, *energy_transactions):
        for obj in energy_transactions:
            obj._energy_product = None
            self._energy_transactions.remove(obj)
    # >>> energy_transactions

    # <<< resold_by_marketers
    # @generated
    def get_resold_by_marketers(self):
        """ A Marketer may resell an EnergyProduct.
        """
        return self._resold_by_marketers

    def set_resold_by_marketers(self, value):
        for p in self._resold_by_marketers:
            filtered = [q for q in p.resells_energy_product if q != self]
            self._resold_by_marketers._resells_energy_product = filtered
        for r in value:
            if self not in r._resells_energy_product:
                r._resells_energy_product.append(self)
        self._resold_by_marketers = value

    resold_by_marketers = property(get_resold_by_marketers, set_resold_by_marketers)

    def add_resold_by_marketers(self, *resold_by_marketers):
        for obj in resold_by_marketers:
            if self not in obj._resells_energy_product:
                obj._resells_energy_product.append(self)
            self._resold_by_marketers.append(obj)

    def remove_resold_by_marketers(self, *resold_by_marketers):
        for obj in resold_by_marketers:
            if self in obj._resells_energy_product:
                obj._resells_energy_product.remove(self)
            self._resold_by_marketers.remove(obj)
    # >>> resold_by_marketers

    # <<< title_held_by_marketer
    # @generated
    def get_title_held_by_marketer(self):
        """ A Marketer holds title to an EnergyProduct.
        """
        return self._title_held_by_marketer

    def set_title_held_by_marketer(self, value):
        if self._title_held_by_marketer is not None:
            filtered = [x for x in self.title_held_by_marketer.holds_title_to_energy_products if x != self]
            self._title_held_by_marketer._holds_title_to_energy_products = filtered

        self._title_held_by_marketer = value
        if self._title_held_by_marketer is not None:
            self._title_held_by_marketer._holds_title_to_energy_products.append(self)

    title_held_by_marketer = property(get_title_held_by_marketer, set_title_held_by_marketer)
    # >>> title_held_by_marketer


    def __str__(self):
        """ Returns a string representation of the EnergyProduct.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_product.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyProduct.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyProduct", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.service_point:
            s += '%s<%s:EnergyProduct.service_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.generation_provider is not None:
            s += '%s<%s:EnergyProduct.generation_provider rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generation_provider.uri)
        for obj in self.energy_transactions:
            s += '%s<%s:EnergyProduct.energy_transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resold_by_marketers:
            s += '%s<%s:EnergyProduct.resold_by_marketers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.title_held_by_marketer is not None:
            s += '%s<%s:EnergyProduct.title_held_by_marketer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.title_held_by_marketer.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyProduct")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_product.serialize


class TieLine(Element):
    # <<< tie_line
    # @generated
    def __init__(self, side_a_host_control_area=None, side_b_host_control_area=None, side_a_sub_control_area=None, customer_consumer=None, side_b_sub_control_area=None, dynamic_energy_transaction=None, control_area_operators=None, **kw_args):
        """ Initialises a new 'TieLine' instance.
        """

        self._side_a_host_control_area = None
        self.side_a_host_control_area = side_a_host_control_area

        self._side_b_host_control_area = None
        self.side_b_host_control_area = side_b_host_control_area

        self._side_a_sub_control_area = None
        self.side_a_sub_control_area = side_a_sub_control_area

        self._customer_consumer = None
        self.customer_consumer = customer_consumer

        self._side_b_sub_control_area = None
        self.side_b_sub_control_area = side_b_sub_control_area

        self._dynamic_energy_transaction = None
        self.dynamic_energy_transaction = dynamic_energy_transaction

        self._control_area_operators = []
        if control_area_operators is not None:
            self.control_area_operators = control_area_operators
        else:
            self.control_area_operators = []


        super(TieLine, self).__init__(**kw_args)
    # >>> tie_line

    # <<< side_a_host_control_area
    # @generated
    def get_side_a_host_control_area(self):
        """ A HostControlArea can have zero or more tie lines.
        """
        return self._side_a_host_control_area

    def set_side_a_host_control_area(self, value):
        if self._side_a_host_control_area is not None:
            filtered = [x for x in self.side_a_host_control_area.side_a_tie_lines if x != self]
            self._side_a_host_control_area._side_a_tie_lines = filtered

        self._side_a_host_control_area = value
        if self._side_a_host_control_area is not None:
            self._side_a_host_control_area._side_a_tie_lines.append(self)

    side_a_host_control_area = property(get_side_a_host_control_area, set_side_a_host_control_area)
    # >>> side_a_host_control_area

    # <<< side_b_host_control_area
    # @generated
    def get_side_b_host_control_area(self):
        """ A HostControlArea can have zero or more tie lines.
        """
        return self._side_b_host_control_area

    def set_side_b_host_control_area(self, value):
        if self._side_b_host_control_area is not None:
            filtered = [x for x in self.side_b_host_control_area.side_b_tie_lines if x != self]
            self._side_b_host_control_area._side_b_tie_lines = filtered

        self._side_b_host_control_area = value
        if self._side_b_host_control_area is not None:
            self._side_b_host_control_area._side_b_tie_lines.append(self)

    side_b_host_control_area = property(get_side_b_host_control_area, set_side_b_host_control_area)
    # >>> side_b_host_control_area

    # <<< side_a_sub_control_area
    # @generated
    def get_side_a_sub_control_area(self):
        """ The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._side_a_sub_control_area

    def set_side_a_sub_control_area(self, value):
        if self._side_a_sub_control_area is not None:
            filtered = [x for x in self.side_a_sub_control_area.side_a_tie_lines if x != self]
            self._side_a_sub_control_area._side_a_tie_lines = filtered

        self._side_a_sub_control_area = value
        if self._side_a_sub_control_area is not None:
            self._side_a_sub_control_area._side_a_tie_lines.append(self)

    side_a_sub_control_area = property(get_side_a_sub_control_area, set_side_a_sub_control_area)
    # >>> side_a_sub_control_area

    # <<< customer_consumer
    # @generated
    def get_customer_consumer(self):
        """ A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        """
        return self._customer_consumer

    def set_customer_consumer(self, value):
        if self._customer_consumer is not None:
            filtered = [x for x in self.customer_consumer.tie_lines if x != self]
            self._customer_consumer._tie_lines = filtered

        self._customer_consumer = value
        if self._customer_consumer is not None:
            self._customer_consumer._tie_lines.append(self)

    customer_consumer = property(get_customer_consumer, set_customer_consumer)
    # >>> customer_consumer

    # <<< side_b_sub_control_area
    # @generated
    def get_side_b_sub_control_area(self):
        """ The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        """
        return self._side_b_sub_control_area

    def set_side_b_sub_control_area(self, value):
        if self._side_b_sub_control_area is not None:
            filtered = [x for x in self.side_b_sub_control_area.side_b_tie_lines if x != self]
            self._side_b_sub_control_area._side_b_tie_lines = filtered

        self._side_b_sub_control_area = value
        if self._side_b_sub_control_area is not None:
            self._side_b_sub_control_area._side_b_tie_lines.append(self)

    side_b_sub_control_area = property(get_side_b_sub_control_area, set_side_b_sub_control_area)
    # >>> side_b_sub_control_area

    # <<< dynamic_energy_transaction
    # @generated
    def get_dynamic_energy_transaction(self):
        """ A dynamic energy transaction can act as a pseudo tie line.
        """
        return self._dynamic_energy_transaction

    def set_dynamic_energy_transaction(self, value):
        if self._dynamic_energy_transaction is not None:
            filtered = [x for x in self.dynamic_energy_transaction.tie_lines if x != self]
            self._dynamic_energy_transaction._tie_lines = filtered

        self._dynamic_energy_transaction = value
        if self._dynamic_energy_transaction is not None:
            self._dynamic_energy_transaction._tie_lines.append(self)

    dynamic_energy_transaction = property(get_dynamic_energy_transaction, set_dynamic_energy_transaction)
    # >>> dynamic_energy_transaction

    # <<< control_area_operators
    # @generated
    def get_control_area_operators(self):
        """ A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
        """
        return self._control_area_operators

    def set_control_area_operators(self, value):
        for p in self._control_area_operators:
            filtered = [q for q in p.tie_lines if q != self]
            self._control_area_operators._tie_lines = filtered
        for r in value:
            if self not in r._tie_lines:
                r._tie_lines.append(self)
        self._control_area_operators = value

    control_area_operators = property(get_control_area_operators, set_control_area_operators)

    def add_control_area_operators(self, *control_area_operators):
        for obj in control_area_operators:
            if self not in obj._tie_lines:
                obj._tie_lines.append(self)
            self._control_area_operators.append(obj)

    def remove_control_area_operators(self, *control_area_operators):
        for obj in control_area_operators:
            if self in obj._tie_lines:
                obj._tie_lines.remove(self)
            self._control_area_operators.remove(obj)
    # >>> control_area_operators


    def __str__(self):
        """ Returns a string representation of the TieLine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tie_line.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TieLine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TieLine", self.uri)
        if format:
            indent += ' ' * depth

        if self.side_a_host_control_area is not None:
            s += '%s<%s:TieLine.side_a_host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.side_a_host_control_area.uri)
        if self.side_b_host_control_area is not None:
            s += '%s<%s:TieLine.side_b_host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.side_b_host_control_area.uri)
        if self.side_a_sub_control_area is not None:
            s += '%s<%s:TieLine.side_a_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.side_a_sub_control_area.uri)
        if self.customer_consumer is not None:
            s += '%s<%s:TieLine.customer_consumer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_consumer.uri)
        if self.side_b_sub_control_area is not None:
            s += '%s<%s:TieLine.side_b_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.side_b_sub_control_area.uri)
        if self.dynamic_energy_transaction is not None:
            s += '%s<%s:TieLine.dynamic_energy_transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dynamic_energy_transaction.uri)
        for obj in self.control_area_operators:
            s += '%s<%s:TieLine.control_area_operators rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TieLine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_line.serialize


class DynamicSchedule(RegularIntervalSchedule):
    """ A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.
    """
    # <<< dynamic_schedule
    # @generated
    def __init__(self, dyn_sched_status='', dyn_sched_sign_rev=False, measurement=None, receive_host_control_area=None, send_host_control_area=None, **kw_args):
        """ Initialises a new 'DynamicSchedule' instance.
        """
        # The 'active' or 'inactive' status of the dynamic schedule 
        self.dyn_sched_status = dyn_sched_status

        # Dynamic schedule sign reversal required (yes/no) 
        self.dyn_sched_sign_rev = dyn_sched_sign_rev


        self._measurement = None
        self.measurement = measurement

        self._receive_host_control_area = None
        self.receive_host_control_area = receive_host_control_area

        self._send_host_control_area = None
        self.send_host_control_area = send_host_control_area


        super(DynamicSchedule, self).__init__(**kw_args)
    # >>> dynamic_schedule

    # <<< measurement
    # @generated
    def get_measurement(self):
        """ A measurement is a data source for dynamic interchange schedules
        """
        return self._measurement

    def set_measurement(self, value):
        if self._measurement is not None:
            filtered = [x for x in self.measurement.dynamic_schedules if x != self]
            self._measurement._dynamic_schedules = filtered

        self._measurement = value
        if self._measurement is not None:
            self._measurement._dynamic_schedules.append(self)

    measurement = property(get_measurement, set_measurement)
    # >>> measurement

    # <<< receive_host_control_area
    # @generated
    def get_receive_host_control_area(self):
        """ A control area can receive dynamic schedules from other control areas
        """
        return self._receive_host_control_area

    def set_receive_host_control_area(self, value):
        if self._receive_host_control_area is not None:
            filtered = [x for x in self.receive_host_control_area.receive_dynamic_schedules if x != self]
            self._receive_host_control_area._receive_dynamic_schedules = filtered

        self._receive_host_control_area = value
        if self._receive_host_control_area is not None:
            self._receive_host_control_area._receive_dynamic_schedules.append(self)

    receive_host_control_area = property(get_receive_host_control_area, set_receive_host_control_area)
    # >>> receive_host_control_area

    # <<< send_host_control_area
    # @generated
    def get_send_host_control_area(self):
        """ A control area can send dynamic schedules to other control areas
        """
        return self._send_host_control_area

    def set_send_host_control_area(self, value):
        if self._send_host_control_area is not None:
            filtered = [x for x in self.send_host_control_area.send_dynamic_schedules if x != self]
            self._send_host_control_area._send_dynamic_schedules = filtered

        self._send_host_control_area = value
        if self._send_host_control_area is not None:
            self._send_host_control_area._send_dynamic_schedules.append(self)

    send_host_control_area = property(get_send_host_control_area, set_send_host_control_area)
    # >>> send_host_control_area


    def __str__(self):
        """ Returns a string representation of the DynamicSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< dynamic_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DynamicSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DynamicSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement is not None:
            s += '%s<%s:DynamicSchedule.measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement.uri)
        if self.receive_host_control_area is not None:
            s += '%s<%s:DynamicSchedule.receive_host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.receive_host_control_area.uri)
        if self.send_host_control_area is not None:
            s += '%s<%s:DynamicSchedule.send_host_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.send_host_control_area.uri)
        s += '%s<%s:DynamicSchedule.dyn_sched_status>%s</%s:DynamicSchedule.dyn_sched_status>' % \
            (indent, ns_prefix, self.dyn_sched_status, ns_prefix)
        s += '%s<%s:DynamicSchedule.dyn_sched_sign_rev>%s</%s:DynamicSchedule.dyn_sched_sign_rev>' % \
            (indent, ns_prefix, self.dyn_sched_sign_rev, ns_prefix)
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
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DynamicSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> dynamic_schedule.serialize


class Reserve(EnergyTransaction):
    # <<< reserve
    # @generated
    def __init__(self, area_reserve_spec=None, **kw_args):
        """ Initialises a new 'Reserve' instance.
        """

        self._area_reserve_spec = []
        if area_reserve_spec is not None:
            self.area_reserve_spec = area_reserve_spec
        else:
            self.area_reserve_spec = []


        super(Reserve, self).__init__(**kw_args)
    # >>> reserve

    # <<< area_reserve_spec
    # @generated
    def get_area_reserve_spec(self):
        """ A Reserve type of energy transaction can count towards an area reserve specification.
        """
        return self._area_reserve_spec

    def set_area_reserve_spec(self, value):
        for x in self._area_reserve_spec:
            x._reserve_energy_transaction = None
        for y in value:
            y._reserve_energy_transaction = self
        self._area_reserve_spec = value

    area_reserve_spec = property(get_area_reserve_spec, set_area_reserve_spec)

    def add_area_reserve_spec(self, *area_reserve_spec):
        for obj in area_reserve_spec:
            obj._reserve_energy_transaction = self
            self._area_reserve_spec.append(obj)

    def remove_area_reserve_spec(self, *area_reserve_spec):
        for obj in area_reserve_spec:
            obj._reserve_energy_transaction = None
            self._area_reserve_spec.remove(obj)
    # >>> area_reserve_spec


    def __str__(self):
        """ Returns a string representation of the Reserve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reserve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Reserve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Reserve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.area_reserve_spec:
            s += '%s<%s:Reserve.area_reserve_spec rdf:resource="#%s"/>' % \
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
        if self.state is not None:
            s += '%s<%s:EnergyTransaction.state rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.state.uri)
        for obj in self.curtailment_profiles:
            s += '%s<%s:EnergyTransaction.curtailment_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.export_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.export_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.export_sub_control_area.uri)
        for obj in self.energy_trans_id:
            s += '%s<%s:EnergyTransaction.energy_trans_id rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.import_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.import_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.import_sub_control_area.uri)
        for obj in self.energy_price_curves:
            s += '%s<%s:EnergyTransaction.energy_price_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.loss_profiles:
            s += '%s<%s:EnergyTransaction.loss_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.energy_profiles:
            s += '%s<%s:EnergyTransaction.energy_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_product is not None:
            s += '%s<%s:EnergyTransaction.energy_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_product.uri)
        s += '%s<%s:EnergyTransaction.receipt_point_p>%s</%s:EnergyTransaction.receipt_point_p>' % \
            (indent, ns_prefix, self.receipt_point_p, ns_prefix)
        s += '%s<%s:EnergyTransaction.energy_min>%s</%s:EnergyTransaction.energy_min>' % \
            (indent, ns_prefix, self.energy_min, ns_prefix)
        s += '%s<%s:EnergyTransaction.firm_interchange_flag>%s</%s:EnergyTransaction.firm_interchange_flag>' % \
            (indent, ns_prefix, self.firm_interchange_flag, ns_prefix)
        s += '%s<%s:EnergyTransaction.congest_charge_max>%s</%s:EnergyTransaction.congest_charge_max>' % \
            (indent, ns_prefix, self.congest_charge_max, ns_prefix)
        s += '%s<%s:EnergyTransaction.reason>%s</%s:EnergyTransaction.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:EnergyTransaction.delivery_point_p>%s</%s:EnergyTransaction.delivery_point_p>' % \
            (indent, ns_prefix, self.delivery_point_p, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Reserve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reserve.serialize


class Block(EnergyTransaction):
    """ A block is a simple transaction type, with no additional relationships.
    """
    pass
    # <<< block
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Block' instance.
        """


        super(Block, self).__init__(**kw_args)
    # >>> block


    def __str__(self):
        """ Returns a string representation of the Block.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< block.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Block.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Block", self.uri)
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
        if self.state is not None:
            s += '%s<%s:EnergyTransaction.state rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.state.uri)
        for obj in self.curtailment_profiles:
            s += '%s<%s:EnergyTransaction.curtailment_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.export_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.export_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.export_sub_control_area.uri)
        for obj in self.energy_trans_id:
            s += '%s<%s:EnergyTransaction.energy_trans_id rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.import_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.import_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.import_sub_control_area.uri)
        for obj in self.energy_price_curves:
            s += '%s<%s:EnergyTransaction.energy_price_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.loss_profiles:
            s += '%s<%s:EnergyTransaction.loss_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.energy_profiles:
            s += '%s<%s:EnergyTransaction.energy_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_product is not None:
            s += '%s<%s:EnergyTransaction.energy_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_product.uri)
        s += '%s<%s:EnergyTransaction.receipt_point_p>%s</%s:EnergyTransaction.receipt_point_p>' % \
            (indent, ns_prefix, self.receipt_point_p, ns_prefix)
        s += '%s<%s:EnergyTransaction.energy_min>%s</%s:EnergyTransaction.energy_min>' % \
            (indent, ns_prefix, self.energy_min, ns_prefix)
        s += '%s<%s:EnergyTransaction.firm_interchange_flag>%s</%s:EnergyTransaction.firm_interchange_flag>' % \
            (indent, ns_prefix, self.firm_interchange_flag, ns_prefix)
        s += '%s<%s:EnergyTransaction.congest_charge_max>%s</%s:EnergyTransaction.congest_charge_max>' % \
            (indent, ns_prefix, self.congest_charge_max, ns_prefix)
        s += '%s<%s:EnergyTransaction.reason>%s</%s:EnergyTransaction.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:EnergyTransaction.delivery_point_p>%s</%s:EnergyTransaction.delivery_point_p>' % \
            (indent, ns_prefix, self.delivery_point_p, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Block")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> block.serialize


class LossProfile(Profile):
    """ LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.
    """
    # <<< loss_profile
    # @generated
    def __init__(self, energy_transaction=None, has_loss_=None, **kw_args):
        """ Initialises a new 'LossProfile' instance.
        """

        self._energy_transaction = None
        self.energy_transaction = energy_transaction

        self._has_loss_ = None
        self.has_loss_ = has_loss_


        super(LossProfile, self).__init__(**kw_args)
    # >>> loss_profile

    # <<< energy_transaction
    # @generated
    def get_energy_transaction(self):
        """ An EnergyTransaction may have a LossProfile.
        """
        return self._energy_transaction

    def set_energy_transaction(self, value):
        if self._energy_transaction is not None:
            filtered = [x for x in self.energy_transaction.loss_profiles if x != self]
            self._energy_transaction._loss_profiles = filtered

        self._energy_transaction = value
        if self._energy_transaction is not None:
            self._energy_transaction._loss_profiles.append(self)

    energy_transaction = property(get_energy_transaction, set_energy_transaction)
    # >>> energy_transaction

    # <<< has_loss_
    # @generated
    def get_has_loss_(self):
        """ Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        """
        return self._has_loss_

    def set_has_loss_(self, value):
        if self._has_loss_ is not None:
            filtered = [x for x in self.has_loss_.for if x != self]
            self._has_loss_._for = filtered

        self._has_loss_ = value
        if self._has_loss_ is not None:
            self._has_loss_._for.append(self)

    has_loss_ = property(get_has_loss_, set_has_loss_)
    # >>> has_loss_


    def __str__(self):
        """ Returns a string representation of the LossProfile.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< loss_profile.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LossProfile.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LossProfile", self.uri)
        if format:
            indent += ' ' * depth

        if self.energy_transaction is not None:
            s += '%s<%s:LossProfile.energy_transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_transaction.uri)
        if self.has_loss_ is not None:
            s += '%s<%s:LossProfile.has_loss_ rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.has_loss_.uri)
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
        for obj in self.profile_datas:
            s += '%s<%s:Profile.profile_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LossProfile")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> loss_profile.serialize


class CurtailmentProfile(Profile):
    """ Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.
    """
    # <<< curtailment_profile
    # @generated
    def __init__(self, energy_transaction=None, **kw_args):
        """ Initialises a new 'CurtailmentProfile' instance.
        """

        self._energy_transaction = None
        self.energy_transaction = energy_transaction


        super(CurtailmentProfile, self).__init__(**kw_args)
    # >>> curtailment_profile

    # <<< energy_transaction
    # @generated
    def get_energy_transaction(self):
        """ An EnergyTransaction may be curtailed by any of the participating entities.
        """
        return self._energy_transaction

    def set_energy_transaction(self, value):
        if self._energy_transaction is not None:
            filtered = [x for x in self.energy_transaction.curtailment_profiles if x != self]
            self._energy_transaction._curtailment_profiles = filtered

        self._energy_transaction = value
        if self._energy_transaction is not None:
            self._energy_transaction._curtailment_profiles.append(self)

    energy_transaction = property(get_energy_transaction, set_energy_transaction)
    # >>> energy_transaction


    def __str__(self):
        """ Returns a string representation of the CurtailmentProfile.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< curtailment_profile.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurtailmentProfile.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurtailmentProfile", self.uri)
        if format:
            indent += ' ' * depth

        if self.energy_transaction is not None:
            s += '%s<%s:CurtailmentProfile.energy_transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_transaction.uri)
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
        for obj in self.profile_datas:
            s += '%s<%s:Profile.profile_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurtailmentProfile")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> curtailment_profile.serialize


class Dynamic(EnergyTransaction):
    """ A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.
    """
    # <<< dynamic
    # @generated
    def __init__(self, tie_lines=None, **kw_args):
        """ Initialises a new 'Dynamic' instance.
        """

        self._tie_lines = []
        if tie_lines is not None:
            self.tie_lines = tie_lines
        else:
            self.tie_lines = []


        super(Dynamic, self).__init__(**kw_args)
    # >>> dynamic

    # <<< tie_lines
    # @generated
    def get_tie_lines(self):
        """ A dynamic energy transaction can act as a pseudo tie line.
        """
        return self._tie_lines

    def set_tie_lines(self, value):
        for x in self._tie_lines:
            x._dynamic_energy_transaction = None
        for y in value:
            y._dynamic_energy_transaction = self
        self._tie_lines = value

    tie_lines = property(get_tie_lines, set_tie_lines)

    def add_tie_lines(self, *tie_lines):
        for obj in tie_lines:
            obj._dynamic_energy_transaction = self
            self._tie_lines.append(obj)

    def remove_tie_lines(self, *tie_lines):
        for obj in tie_lines:
            obj._dynamic_energy_transaction = None
            self._tie_lines.remove(obj)
    # >>> tie_lines


    def __str__(self):
        """ Returns a string representation of the Dynamic.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< dynamic.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Dynamic.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Dynamic", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.tie_lines:
            s += '%s<%s:Dynamic.tie_lines rdf:resource="#%s"/>' % \
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
        if self.state is not None:
            s += '%s<%s:EnergyTransaction.state rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.state.uri)
        for obj in self.curtailment_profiles:
            s += '%s<%s:EnergyTransaction.curtailment_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.export_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.export_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.export_sub_control_area.uri)
        for obj in self.energy_trans_id:
            s += '%s<%s:EnergyTransaction.energy_trans_id rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.import_sub_control_area is not None:
            s += '%s<%s:EnergyTransaction.import_sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.import_sub_control_area.uri)
        for obj in self.energy_price_curves:
            s += '%s<%s:EnergyTransaction.energy_price_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.loss_profiles:
            s += '%s<%s:EnergyTransaction.loss_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.energy_profiles:
            s += '%s<%s:EnergyTransaction.energy_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_product is not None:
            s += '%s<%s:EnergyTransaction.energy_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_product.uri)
        s += '%s<%s:EnergyTransaction.receipt_point_p>%s</%s:EnergyTransaction.receipt_point_p>' % \
            (indent, ns_prefix, self.receipt_point_p, ns_prefix)
        s += '%s<%s:EnergyTransaction.energy_min>%s</%s:EnergyTransaction.energy_min>' % \
            (indent, ns_prefix, self.energy_min, ns_prefix)
        s += '%s<%s:EnergyTransaction.firm_interchange_flag>%s</%s:EnergyTransaction.firm_interchange_flag>' % \
            (indent, ns_prefix, self.firm_interchange_flag, ns_prefix)
        s += '%s<%s:EnergyTransaction.congest_charge_max>%s</%s:EnergyTransaction.congest_charge_max>' % \
            (indent, ns_prefix, self.congest_charge_max, ns_prefix)
        s += '%s<%s:EnergyTransaction.reason>%s</%s:EnergyTransaction.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:EnergyTransaction.delivery_point_p>%s</%s:EnergyTransaction.delivery_point_p>' % \
            (indent, ns_prefix, self.delivery_point_p, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Dynamic")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> dynamic.serialize


class EnergyProfile(Profile):
    """ Specifies the start time, stop time, level for an EnergyTransaction.
    """
    # <<< energy_profile
    # @generated
    def __init__(self, transaction_bid=None, energy_transaction=None, **kw_args):
        """ Initialises a new 'EnergyProfile' instance.
        """

        self._transaction_bid = None
        self.transaction_bid = transaction_bid

        self._energy_transaction = None
        self.energy_transaction = energy_transaction


        super(EnergyProfile, self).__init__(**kw_args)
    # >>> energy_profile

    # <<< transaction_bid
    # @generated
    def get_transaction_bid(self):
        """ 
        """
        return self._transaction_bid

    def set_transaction_bid(self, value):
        if self._transaction_bid is not None:
            filtered = [x for x in self.transaction_bid.energy_profiles if x != self]
            self._transaction_bid._energy_profiles = filtered

        self._transaction_bid = value
        if self._transaction_bid is not None:
            self._transaction_bid._energy_profiles.append(self)

    transaction_bid = property(get_transaction_bid, set_transaction_bid)
    # >>> transaction_bid

    # <<< energy_transaction
    # @generated
    def get_energy_transaction(self):
        """ An EnergyTransaction must have at least one EnergyProfile.
        """
        return self._energy_transaction

    def set_energy_transaction(self, value):
        if self._energy_transaction is not None:
            filtered = [x for x in self.energy_transaction.energy_profiles if x != self]
            self._energy_transaction._energy_profiles = filtered

        self._energy_transaction = value
        if self._energy_transaction is not None:
            self._energy_transaction._energy_profiles.append(self)

    energy_transaction = property(get_energy_transaction, set_energy_transaction)
    # >>> energy_transaction


    def __str__(self):
        """ Returns a string representation of the EnergyProfile.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_profile.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyProfile.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyProfile", self.uri)
        if format:
            indent += ' ' * depth

        if self.transaction_bid is not None:
            s += '%s<%s:EnergyProfile.transaction_bid rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transaction_bid.uri)
        if self.energy_transaction is not None:
            s += '%s<%s:EnergyProfile.energy_transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_transaction.uri)
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
        for obj in self.profile_datas:
            s += '%s<%s:Profile.profile_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyProfile")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_profile.serialize


# <<< energy_scheduling
# @generated
# >>> energy_scheduling
