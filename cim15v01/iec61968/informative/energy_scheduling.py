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

""" This package provides the capability to schedule and account for transactions for the exchange of electric power between companies. It includes transations for megawatts which are generated, consumed, lost, passed through, sold and purchased. These classes are used by Accounting and Billing for Energy, Generation Capacity, Transmission, and Ancillary Services.
"""

from cim15v01.iec61968.common import Document
from cim15v01.iec61970.core import Curve
from cim15v01 import Element
from cim15v01.iec61970.core import IdentifiedObject
from cim15v01.iec61970.control_area import ControlArea
from cim15v01.iec61970.core import PowerSystemResource
from cim15v01.iec61968.common import Agreement
from cim15v01.iec61970.core import RegularIntervalSchedule

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimEnergyScheduling"

ns_uri = "http://iec.ch/TC57/CIM-generic#EnergyScheduling"

class EnergyTransaction(Document):
    """ Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.
    """
    # <<< energy_transaction
    # @generated
    def __init__(self, receipt_point_p=0.0, state=None, energy_min=0.0, firm_interchange_flag=False, congest_charge_max=0.0, reason='', delivery_point_p=0.0, curtailment_profiles=None, export_sub_control_area=None, energy_trans_id=None, import_sub_control_area=None, energy_price_curves=None, loss_profiles=None, energy_profiles=None, energy_product=None, *args, **kw_args):
        """ Initialises a new 'EnergyTransaction' instance.

        @param receipt_point_p: Receipt point active power
        @param state: { Approve | Deny | Study }
        @param energy_min: Transaction minimum active power if dispatchable
        @param firm_interchange_flag: Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences.
        @param congest_charge_max: Maximum congestion charges in monetary units
        @param reason:
        @param delivery_point_p: Delivery point active power
        @param curtailment_profiles: An EnergyTransaction may be curtailed by any of the participating entities.
        @param export_sub_control_area: Energy is transferred between interchange areas
        @param energy_trans_id:
        @param import_sub_control_area: Energy is transferred between interchange areas
        @param energy_price_curves:
        @param loss_profiles: An EnergyTransaction may have a LossProfile.
        @param energy_profiles: An EnergyTransaction must have at least one EnergyProfile.
        @param energy_product: The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        # Receipt point active power
        self.receipt_point_p = receipt_point_p

        # { Approve | Deny | Study }
        self.state = state

        # Transaction minimum active power if dispatchable
        self.energy_min = energy_min

        # Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences.
        self.firm_interchange_flag = firm_interchange_flag

        # Maximum congestion charges in monetary units
        self.congest_charge_max = congest_charge_max


        self.reason = reason

        # Delivery point active power
        self.delivery_point_p = delivery_point_p


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


        super(EnergyTransaction, self).__init__(*args, **kw_args)
    # >>> energy_transaction

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



class AvailableTransmissionCapacity(Curve):
    """ Amount of possible flow by direction.
    """
    # <<< available_transmission_capacity
    # @generated
    def __init__(self, schedule_for=None, *args, **kw_args):
        """ Initialises a new 'AvailableTransmissionCapacity' instance.

        @param schedule_for: A transmission schedule posts the available transmission capacity for a transmission line.
        """

        self._schedule_for = []
        if schedule_for is not None:
            self.schedule_for = schedule_for
        else:
            self.schedule_for = []


        super(AvailableTransmissionCapacity, self).__init__(*args, **kw_args)
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



class ProfileData(Element):
    """ Data for profile.
    """
    # <<< profile_data
    # @generated
    def __init__(self, stop_date_time='', energy_level=0.0, start_date_time='', capacity_level=0.0, sequence_number=0, profile=None, *args, **kw_args):
        """ Initialises a new 'ProfileData' instance.

        @param stop_date_time: Stop date/time for this profile.
        @param energy_level: Energy level for the profile
        @param start_date_time: Start date/time for this profile.
        @param capacity_level: Active power capacity level for the profile.
        @param sequence_number: Sequence to provide item numbering for the profile. { greater than or equal to 1 }
        @param profile: A profile has profile data associated with it.
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


        super(ProfileData, self).__init__(*args, **kw_args)
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



class Profile(IdentifiedObject):
    """ A profile is a simpler curve type.
    """
    # <<< profile
    # @generated
    def __init__(self, profile_datas=None, *args, **kw_args):
        """ Initialises a new 'Profile' instance.

        @param profile_datas: A profile has profile data associated with it.
        """

        self._profile_datas = []
        if profile_datas is not None:
            self.profile_datas = profile_datas
        else:
            self.profile_datas = []


        super(Profile, self).__init__(*args, **kw_args)
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



class SubControlArea(ControlArea):
    """ SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """
    # <<< sub_control_area
    # @generated
    def __init__(self, flowgate=None, export_energy_transactions=None, import_energy_transactions=None, host_control_area=None, part_of=None, side_a_tie_lines=None, generating_units=None, side_b_tie_lines=None, *args, **kw_args):
        """ Initialises a new 'SubControlArea' instance.

        @param flowgate: A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        @param export_energy_transactions: Energy is transferred between interchange areas
        @param import_energy_transactions: Energy is transferred between interchange areas
        @param host_control_area: The interchange area  may operate as a control area
        @param part_of: A transmission path's service point is part of an interchange area
        @param side_a_tie_lines: The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param generating_units: A GeneratingUnit injects energy into a SubControlArea.
        @param side_b_tie_lines: The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
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


        super(SubControlArea, self).__init__(*args, **kw_args)
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



class TransmissionRightOfWay(PowerSystemResource):
    """ A collection of transmission lines that are close proximity to each other.
    """
    # <<< transmission_right_of_way
    # @generated
    def __init__(self, transmission_corridor=None, lines=None, *args, **kw_args):
        """ Initialises a new 'TransmissionRightOfWay' instance.

        @param transmission_corridor: A transmission right-of-way is a member of a transmission corridor
        @param lines: A transmission line can be part of a transmission corridor
        """

        self._transmission_corridor = None
        self.transmission_corridor = transmission_corridor

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []


        super(TransmissionRightOfWay, self).__init__(*args, **kw_args)
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



class EnergySchedulingVersion(Element):
    # <<< energy_scheduling_version
    # @generated
    def __init__(self, date='', version='', *args, **kw_args):
        """ Initialises a new 'EnergySchedulingVersion' instance.

        @param date:
        @param version: v 4 moved SubControlArea
        """

        self.date = date

        # v 4 moved SubControlArea
        self.version = version



        super(EnergySchedulingVersion, self).__init__(*args, **kw_args)
    # >>> energy_scheduling_version



class HostControlArea(IdentifiedObject):
    """ A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.
    """
    # <<< host_control_area
    # @generated
    def __init__(self, area_control_mode='off', frequency_bias_factor=None, freq_set_point=0.0, inadvertent_accounts=None, area_reserve_spec=None, side_a_tie_lines=None, sub_control_areas=None, side_b_tie_lines=None, receive_dynamic_schedules=None, send_dynamic_schedules=None, controls=None, *args, **kw_args):
        """ Initialises a new 'HostControlArea' instance.

        @param area_control_mode: The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control) Values are: "off", "tlb", "cf", "ctl"
        @param frequency_bias_factor: The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC)
        @param freq_set_point: The present power system frequency set point for automatic generation control
        @param inadvertent_accounts: A control area can have one or more net inadvertent interchange accounts
        @param area_reserve_spec: A control area has one or more area reserve specifications
        @param side_a_tie_lines: A HostControlArea can have zero or more tie lines.
        @param sub_control_areas: The interchange area  may operate as a control area
        @param side_b_tie_lines: A HostControlArea can have zero or more tie lines.
        @param receive_dynamic_schedules: A control area can receive dynamic schedules from other control areas
        @param send_dynamic_schedules: A control area can send dynamic schedules to other control areas
        @param controls: A ControlAreaCompany controls a ControlArea.
        """
        # The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control) Values are: "off", "tlb", "cf", "ctl"
        self.area_control_mode = area_control_mode

        # The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC)
        self.frequency_bias_factor = frequency_bias_factor

        # The present power system frequency set point for automatic generation control
        self.freq_set_point = freq_set_point


        self._inadvertent_accounts = []
        if inadvertent_accounts is not None:
            self.inadvertent_accounts = inadvertent_accounts
        else:
            self.inadvertent_accounts = []

        self._area_reserve_spec = None
        self.area_reserve_spec = area_reserve_spec

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


        super(HostControlArea, self).__init__(*args, **kw_args)
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



class InadvertentAccount(Curve):
    """ An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.
    """
    # <<< inadvertent_account
    # @generated
    def __init__(self, host_control_area=None, *args, **kw_args):
        """ Initialises a new 'InadvertentAccount' instance.

        @param host_control_area: A control area can have one or more net inadvertent interchange accounts
        """

        self._host_control_area = None
        self.host_control_area = host_control_area


        super(InadvertentAccount, self).__init__(*args, **kw_args)
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



class TransmissionCorridor(PowerSystemResource):
    """ A corridor containing one or more rights of way
    """
    # <<< transmission_corridor
    # @generated
    def __init__(self, transmission_right_of_ways=None, contained_in=None, *args, **kw_args):
        """ Initialises a new 'TransmissionCorridor' instance.

        @param transmission_right_of_ways: A transmission right-of-way is a member of a transmission corridor
        @param contained_in: A TransmissionPath is contained in a TransmissionCorridor.
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


        super(TransmissionCorridor, self).__init__(*args, **kw_args)
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



class AreaReserveSpec(Element):
    """ The control area's reserve specification
    """
    # <<< area_reserve_spec
    # @generated
    def __init__(self, area_reserve_spec_name='', raise_reg_margin_reqt=0.0, lower_reg_margin_reqt=0.0, primary_reserve_reqt=0.0, op_reserve_reqt=0.0, spinning_reserve_reqt=0.0, host_control_areas=None, reserve_energy_transaction=None, *args, **kw_args):
        """ Initialises a new 'AreaReserveSpec' instance.

        @param area_reserve_spec_name: The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations.
        @param raise_reg_margin_reqt: Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes
        @param lower_reg_margin_reqt: Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes
        @param primary_reserve_reqt: Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve.
        @param op_reserve_reqt: Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min).
        @param spinning_reserve_reqt: Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes
        @param host_control_areas: A control area has one or more area reserve specifications
        @param reserve_energy_transaction: A Reserve type of energy transaction can count towards an area reserve specification.
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


        super(AreaReserveSpec, self).__init__(*args, **kw_args)
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



class EnergyProduct(Agreement):
    """ An EnergyProduct is offered commercially as a ContractOrTariff.
    """
    # <<< energy_product
    # @generated
    def __init__(self, service_point=None, generation_provider=None, energy_transactions=None, resold_by_marketers=None, title_held_by_marketer=None, *args, **kw_args):
        """ Initialises a new 'EnergyProduct' instance.

        @param service_point: An EnergyProduct injects energy into a service point.
        @param generation_provider:
        @param energy_transactions: The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        @param resold_by_marketers: A Marketer may resell an EnergyProduct.
        @param title_held_by_marketer: A Marketer holds title to an EnergyProduct.
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


        super(EnergyProduct, self).__init__(*args, **kw_args)
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



class TieLine(Element):
    # <<< tie_line
    # @generated
    def __init__(self, side_a_host_control_area=None, side_b_host_control_area=None, side_a_sub_control_area=None, customer_consumer=None, side_b_sub_control_area=None, dynamic_energy_transaction=None, control_area_operators=None, *args, **kw_args):
        """ Initialises a new 'TieLine' instance.

        @param side_a_host_control_area: A HostControlArea can have zero or more tie lines.
        @param side_b_host_control_area: A HostControlArea can have zero or more tie lines.
        @param side_a_sub_control_area: The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param customer_consumer: A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
        @param side_b_sub_control_area: The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
        @param dynamic_energy_transaction: A dynamic energy transaction can act as a pseudo tie line.
        @param control_area_operators: A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
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


        super(TieLine, self).__init__(*args, **kw_args)
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



class DynamicSchedule(RegularIntervalSchedule):
    """ A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.
    """
    # <<< dynamic_schedule
    # @generated
    def __init__(self, dyn_sched_status='', dyn_sched_sign_rev=False, measurement=None, receive_host_control_area=None, send_host_control_area=None, *args, **kw_args):
        """ Initialises a new 'DynamicSchedule' instance.

        @param dyn_sched_status: The 'active' or 'inactive' status of the dynamic schedule
        @param dyn_sched_sign_rev: Dynamic schedule sign reversal required (yes/no)
        @param measurement: A measurement is a data source for dynamic interchange schedules
        @param receive_host_control_area: A control area can receive dynamic schedules from other control areas
        @param send_host_control_area: A control area can send dynamic schedules to other control areas
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


        super(DynamicSchedule, self).__init__(*args, **kw_args)
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



class Reserve(EnergyTransaction):
    # <<< reserve
    # @generated
    def __init__(self, area_reserve_spec=None, *args, **kw_args):
        """ Initialises a new 'Reserve' instance.

        @param area_reserve_spec: A Reserve type of energy transaction can count towards an area reserve specification.
        """

        self._area_reserve_spec = []
        if area_reserve_spec is not None:
            self.area_reserve_spec = area_reserve_spec
        else:
            self.area_reserve_spec = []


        super(Reserve, self).__init__(*args, **kw_args)
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



class Block(EnergyTransaction):
    """ A block is a simple transaction type, with no additional relationships.
    """
    pass
    # <<< block
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Block' instance.

        """


        super(Block, self).__init__(*args, **kw_args)
    # >>> block



class LossProfile(Profile):
    """ LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.
    """
    # <<< loss_profile
    # @generated
    def __init__(self, energy_transaction=None, has_loss_=None, *args, **kw_args):
        """ Initialises a new 'LossProfile' instance.

        @param energy_transaction: An EnergyTransaction may have a LossProfile.
        @param has_loss_: Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        """

        self._energy_transaction = None
        self.energy_transaction = energy_transaction

        self._has_loss_ = None
        self.has_loss_ = has_loss_


        super(LossProfile, self).__init__(*args, **kw_args)
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
            filtered = [x for x in self.has_loss_.ffor if x != self]
            self._has_loss_._for = filtered

        self._has_loss_ = value
        if self._has_loss_ is not None:
            self._has_loss_._for.append(self)

    has_loss_ = property(get_has_loss_, set_has_loss_)
    # >>> has_loss_



class CurtailmentProfile(Profile):
    """ Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.
    """
    # <<< curtailment_profile
    # @generated
    def __init__(self, energy_transaction=None, *args, **kw_args):
        """ Initialises a new 'CurtailmentProfile' instance.

        @param energy_transaction: An EnergyTransaction may be curtailed by any of the participating entities.
        """

        self._energy_transaction = None
        self.energy_transaction = energy_transaction


        super(CurtailmentProfile, self).__init__(*args, **kw_args)
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



class Dynamic(EnergyTransaction):
    """ A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.
    """
    # <<< dynamic
    # @generated
    def __init__(self, tie_lines=None, *args, **kw_args):
        """ Initialises a new 'Dynamic' instance.

        @param tie_lines: A dynamic energy transaction can act as a pseudo tie line.
        """

        self._tie_lines = []
        if tie_lines is not None:
            self.tie_lines = tie_lines
        else:
            self.tie_lines = []


        super(Dynamic, self).__init__(*args, **kw_args)
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



class EnergyProfile(Profile):
    """ Specifies the start time, stop time, level for an EnergyTransaction.
    """
    # <<< energy_profile
    # @generated
    def __init__(self, transaction_bid=None, energy_transaction=None, *args, **kw_args):
        """ Initialises a new 'EnergyProfile' instance.

        @param transaction_bid:
        @param energy_transaction: An EnergyTransaction must have at least one EnergyProfile.
        """

        self._transaction_bid = None
        self.transaction_bid = transaction_bid

        self._energy_transaction = None
        self.energy_transaction = energy_transaction


        super(EnergyProfile, self).__init__(*args, **kw_args)
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



# <<< energy_scheduling
# @generated
# >>> energy_scheduling
