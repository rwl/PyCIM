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

""" This package includes information for Transaction Scheduling for Energy, Generation Capacity, Transmission, and Ancillary Services.
"""

from cim import Element
from cim.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.reservation"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Reservation"

class ReservationVersion(Element):
    # <<< reservation_version
    # @generated
    def __init__(self, version='', date='', **kw_args):
        """ Initialises a new 'ReservationVersion' instance.
        """
 
        self.version = version

 
        self.date = date



        super(ReservationVersion, self).__init__(**kw_args)
    # >>> reservation_version


    def __str__(self):
        """ Returns a string representation of the ReservationVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reservation_version.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReservationVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReservationVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ReservationVersion.version>%s</%s:ReservationVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:ReservationVersion.date>%s</%s:ReservationVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReservationVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reservation_version.serialize


class TiePoint(IdentifiedObject):
    """ Site of an interface between interchange areas. The tie point can be a network branch (e.g., transmission line or transformer) or a switching device. For transmission lines, the interchange area boundary is usually at a designated point such as the middle of the line. Line end metering is then corrected for line losses.
    """
    # <<< tie_point
    # @generated
    def __init__(self, tie_point_mwrating=0.0, declared_service_point=None, for_measurements=None, by_measurements=None, **kw_args):
        """ Initialises a new 'TiePoint' instance.
        """
        # The MW rating of the tie point 
        self.tie_point_mwrating = tie_point_mwrating


        self._declared_service_point = None
        self.declared_service_point = declared_service_point

        self._for_measurements = []
        if for_measurements is not None:
            self.for_measurements = for_measurements
        else:
            self.for_measurements = []

        self._by_measurements = []
        if by_measurements is not None:
            self.by_measurements = by_measurements
        else:
            self.by_measurements = []


        super(TiePoint, self).__init__(**kw_args)
    # >>> tie_point

    # <<< declared_service_point
    # @generated
    def get_declared_service_point(self):
        """ A tiepoint may be declared as a service point.
        """
        return self._declared_service_point

    def set_declared_service_point(self, value):
        if self._declared_service_point is not None:
            self._declared_service_point._declare_tie_point = None

        self._declared_service_point = value
        if self._declared_service_point is not None:
            self._declared_service_point._declare_tie_point = self

    declared_service_point = property(get_declared_service_point, set_declared_service_point)
    # >>> declared_service_point

    # <<< for_measurements
    # @generated
    def get_for_measurements(self):
        """ A measurement is made on the A side of a tie point
        """
        return self._for_measurements

    def set_for_measurements(self, value):
        for x in self._for_measurements:
            x._for_tie_point = None
        for y in value:
            y._for_tie_point = self
        self._for_measurements = value

    for_measurements = property(get_for_measurements, set_for_measurements)

    def add_for_measurements(self, *for_measurements):
        for obj in for_measurements:
            obj._for_tie_point = self
            self._for_measurements.append(obj)

    def remove_for_measurements(self, *for_measurements):
        for obj in for_measurements:
            obj._for_tie_point = None
            self._for_measurements.remove(obj)
    # >>> for_measurements

    # <<< by_measurements
    # @generated
    def get_by_measurements(self):
        """ A measurement is made on the B side of a tie point
        """
        return self._by_measurements

    def set_by_measurements(self, value):
        for x in self._by_measurements:
            x._by_tie_point = None
        for y in value:
            y._by_tie_point = self
        self._by_measurements = value

    by_measurements = property(get_by_measurements, set_by_measurements)

    def add_by_measurements(self, *by_measurements):
        for obj in by_measurements:
            obj._by_tie_point = self
            self._by_measurements.append(obj)

    def remove_by_measurements(self, *by_measurements):
        for obj in by_measurements:
            obj._by_tie_point = None
            self._by_measurements.remove(obj)
    # >>> by_measurements


    def __str__(self):
        """ Returns a string representation of the TiePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tie_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TiePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TiePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.declared_service_point is not None:
            s += '%s<%s:TiePoint.declared_service_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.declared_service_point.uri)
        for obj in self.for_measurements:
            s += '%s<%s:TiePoint.for_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.by_measurements:
            s += '%s<%s:TiePoint.by_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:TiePoint.tie_point_mwrating>%s</%s:TiePoint.tie_point_mwrating>' % \
            (indent, ns_prefix, self.tie_point_mwrating, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TiePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_point.serialize


class TransmissionService(IdentifiedObject):
    """ Transmission products along posted transmission path.
    """
    # <<< transmission_service
    # @generated
    def __init__(self, offered_as=None, offering=None, trans_contract_for=None, scheduled_by=None, offers=None, reserved_by_service_reservation=None, **kw_args):
        """ Initialises a new 'TransmissionService' instance.
        """

        self._offered_as = []
        if offered_as is not None:
            self.offered_as = offered_as
        else:
            self.offered_as = []

        self._offering = []
        if offering is not None:
            self.offering = offering
        else:
            self.offering = []

        self._trans_contract_for = None
        self.trans_contract_for = trans_contract_for

        self._scheduled_by = []
        if scheduled_by is not None:
            self.scheduled_by = scheduled_by
        else:
            self.scheduled_by = []

        self._offers = None
        self.offers = offers

        self._reserved_by_service_reservation = []
        if reserved_by_service_reservation is not None:
            self.reserved_by_service_reservation = reserved_by_service_reservation
        else:
            self.reserved_by_service_reservation = []


        super(TransmissionService, self).__init__(**kw_args)
    # >>> transmission_service

    # <<< offered_as
    # @generated
    def get_offered_as(self):
        """ A transmission product is offered as a transmission service along a transmission path.
        """
        return self._offered_as

    def set_offered_as(self, value):
        for p in self._offered_as:
            filtered = [q for q in p.offers if q != self]
            self._offered_as._offers = filtered
        for r in value:
            if self not in r._offers:
                r._offers.append(self)
        self._offered_as = value

    offered_as = property(get_offered_as, set_offered_as)

    def add_offered_as(self, *offered_as):
        for obj in offered_as:
            if self not in obj._offers:
                obj._offers.append(self)
            self._offered_as.append(obj)

    def remove_offered_as(self, *offered_as):
        for obj in offered_as:
            if self in obj._offers:
                obj._offers.remove(self)
            self._offered_as.remove(obj)
    # >>> offered_as

    # <<< offering
    # @generated
    def get_offering(self):
        """ A transmission service is offered on a transmission path.
        """
        return self._offering

    def set_offering(self, value):
        for p in self._offering:
            filtered = [q for q in p.offered_on if q != self]
            self._offering._offered_on = filtered
        for r in value:
            if self not in r._offered_on:
                r._offered_on.append(self)
        self._offering = value

    offering = property(get_offering, set_offering)

    def add_offering(self, *offering):
        for obj in offering:
            if self not in obj._offered_on:
                obj._offered_on.append(self)
            self._offering.append(obj)

    def remove_offering(self, *offering):
        for obj in offering:
            if self in obj._offered_on:
                obj._offered_on.remove(self)
            self._offering.remove(obj)
    # >>> offering

    # <<< trans_contract_for
    # @generated
    def get_trans_contract_for(self):
        """ A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
        """
        return self._trans_contract_for

    def set_trans_contract_for(self, value):
        if self._trans_contract_for is not None:
            filtered = [x for x in self.trans_contract_for.provided_by_transmission_service if x != self]
            self._trans_contract_for._provided_by_transmission_service = filtered

        self._trans_contract_for = value
        if self._trans_contract_for is not None:
            self._trans_contract_for._provided_by_transmission_service.append(self)

    trans_contract_for = property(get_trans_contract_for, set_trans_contract_for)
    # >>> trans_contract_for

    # <<< scheduled_by
    # @generated
    def get_scheduled_by(self):
        """ A transmission schedule posts the available transmission capacity for a transmission line.
        """
        return self._scheduled_by

    def set_scheduled_by(self, value):
        for p in self._scheduled_by:
            filtered = [q for q in p.schedule_for if q != self]
            self._scheduled_by._schedule_for = filtered
        for r in value:
            if self not in r._schedule_for:
                r._schedule_for.append(self)
        self._scheduled_by = value

    scheduled_by = property(get_scheduled_by, set_scheduled_by)

    def add_scheduled_by(self, *scheduled_by):
        for obj in scheduled_by:
            if self not in obj._schedule_for:
                obj._schedule_for.append(self)
            self._scheduled_by.append(obj)

    def remove_scheduled_by(self, *scheduled_by):
        for obj in scheduled_by:
            if self in obj._schedule_for:
                obj._schedule_for.remove(self)
            self._scheduled_by.remove(obj)
    # >>> scheduled_by

    # <<< offers
    # @generated
    def get_offers(self):
        """ The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
        """
        return self._offers

    def set_offers(self, value):
        if self._offers is not None:
            filtered = [x for x in self.offers.offered_by if x != self]
            self._offers._offered_by = filtered

        self._offers = value
        if self._offers is not None:
            self._offers._offered_by.append(self)

    offers = property(get_offers, set_offers)
    # >>> offers

    # <<< reserved_by_service_reservation
    # @generated
    def get_reserved_by_service_reservation(self):
        """ A service reservation reserves a particular transmission service.
        """
        return self._reserved_by_service_reservation

    def set_reserved_by_service_reservation(self, value):
        for p in self._reserved_by_service_reservation:
            filtered = [q for q in p.reserves_transmission_service if q != self]
            self._reserved_by_service_reservation._reserves_transmission_service = filtered
        for r in value:
            if self not in r._reserves_transmission_service:
                r._reserves_transmission_service.append(self)
        self._reserved_by_service_reservation = value

    reserved_by_service_reservation = property(get_reserved_by_service_reservation, set_reserved_by_service_reservation)

    def add_reserved_by_service_reservation(self, *reserved_by_service_reservation):
        for obj in reserved_by_service_reservation:
            if self not in obj._reserves_transmission_service:
                obj._reserves_transmission_service.append(self)
            self._reserved_by_service_reservation.append(obj)

    def remove_reserved_by_service_reservation(self, *reserved_by_service_reservation):
        for obj in reserved_by_service_reservation:
            if self in obj._reserves_transmission_service:
                obj._reserves_transmission_service.remove(self)
            self._reserved_by_service_reservation.remove(obj)
    # >>> reserved_by_service_reservation


    def __str__(self):
        """ Returns a string representation of the TransmissionService.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transmission_service.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransmissionService.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransmissionService", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.offered_as:
            s += '%s<%s:TransmissionService.offered_as rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.offering:
            s += '%s<%s:TransmissionService.offering rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.trans_contract_for is not None:
            s += '%s<%s:TransmissionService.trans_contract_for rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.trans_contract_for.uri)
        for obj in self.scheduled_by:
            s += '%s<%s:TransmissionService.scheduled_by rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.offers is not None:
            s += '%s<%s:TransmissionService.offers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.offers.uri)
        for obj in self.reserved_by_service_reservation:
            s += '%s<%s:TransmissionService.reserved_by_service_reservation rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransmissionService")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transmission_service.serialize


class ServicePoint(IdentifiedObject):
    """ Each ServicePoint is contained within (or on the boundary of) an ElectronicIinterchangeArea. ServicePoints are defined termination points of a transmission path (down to distribution level or to a customer - generation or consumption or both).
    """
    # <<< service_point
    # @generated
    def __init__(self, customer_consumer=None, declare_tie_point=None, energy_products=None, transmission_provider=None, has_apod_=None, has_apor_=None, member_of=None, generation_provider=None, **kw_args):
        """ Initialises a new 'ServicePoint' instance.
        """

        self._customer_consumer = None
        self.customer_consumer = customer_consumer

        self._declare_tie_point = None
        self.declare_tie_point = declare_tie_point

        self._energy_products = []
        if energy_products is not None:
            self.energy_products = energy_products
        else:
            self.energy_products = []

        self._transmission_provider = None
        self.transmission_provider = transmission_provider

        self._has_apod_ = []
        if has_apod_ is not None:
            self.has_apod_ = has_apod_
        else:
            self.has_apod_ = []

        self._has_apor_ = []
        if has_apor_ is not None:
            self.has_apor_ = has_apor_
        else:
            self.has_apor_ = []

        self._member_of = None
        self.member_of = member_of

        self._generation_provider = None
        self.generation_provider = generation_provider


        super(ServicePoint, self).__init__(**kw_args)
    # >>> service_point

    # <<< customer_consumer
    # @generated
    def get_customer_consumer(self):
        """ A CustomerConsumer may have one or more ServicePoints.
        """
        return self._customer_consumer

    def set_customer_consumer(self, value):
        if self._customer_consumer is not None:
            filtered = [x for x in self.customer_consumer.service_point if x != self]
            self._customer_consumer._service_point = filtered

        self._customer_consumer = value
        if self._customer_consumer is not None:
            self._customer_consumer._service_point.append(self)

    customer_consumer = property(get_customer_consumer, set_customer_consumer)
    # >>> customer_consumer

    # <<< declare_tie_point
    # @generated
    def get_declare_tie_point(self):
        """ A tiepoint may be declared as a service point.
        """
        return self._declare_tie_point

    def set_declare_tie_point(self, value):
        if self._declare_tie_point is not None:
            self._declare_tie_point._declared_service_point = None

        self._declare_tie_point = value
        if self._declare_tie_point is not None:
            self._declare_tie_point._declared_service_point = self

    declare_tie_point = property(get_declare_tie_point, set_declare_tie_point)
    # >>> declare_tie_point

    # <<< energy_products
    # @generated
    def get_energy_products(self):
        """ An EnergyProduct injects energy into a service point.
        """
        return self._energy_products

    def set_energy_products(self, value):
        for p in self._energy_products:
            filtered = [q for q in p.service_point if q != self]
            self._energy_products._service_point = filtered
        for r in value:
            if self not in r._service_point:
                r._service_point.append(self)
        self._energy_products = value

    energy_products = property(get_energy_products, set_energy_products)

    def add_energy_products(self, *energy_products):
        for obj in energy_products:
            if self not in obj._service_point:
                obj._service_point.append(self)
            self._energy_products.append(obj)

    def remove_energy_products(self, *energy_products):
        for obj in energy_products:
            if self in obj._service_point:
                obj._service_point.remove(self)
            self._energy_products.remove(obj)
    # >>> energy_products

    # <<< transmission_provider
    # @generated
    def get_transmission_provider(self):
        """ A TransmissionProvider registers one or more ServicePoints.
        """
        return self._transmission_provider

    def set_transmission_provider(self, value):
        if self._transmission_provider is not None:
            filtered = [x for x in self.transmission_provider.service_point if x != self]
            self._transmission_provider._service_point = filtered

        self._transmission_provider = value
        if self._transmission_provider is not None:
            self._transmission_provider._service_point.append(self)

    transmission_provider = property(get_transmission_provider, set_transmission_provider)
    # >>> transmission_provider

    # <<< has_apod_
    # @generated
    def get_has_apod_(self):
        """ A transmission path has a 'point-of-delivery' service point
        """
        return self._has_apod_

    def set_has_apod_(self, value):
        for x in self._has_apod_:
            x._delivery_point_for = None
        for y in value:
            y._delivery_point_for = self
        self._has_apod_ = value

    has_apod_ = property(get_has_apod_, set_has_apod_)

    def add_has_apod_(self, *has_apod_):
        for obj in has_apod_:
            obj._delivery_point_for = self
            self._has_apod_.append(obj)

    def remove_has_apod_(self, *has_apod_):
        for obj in has_apod_:
            obj._delivery_point_for = None
            self._has_apod_.remove(obj)
    # >>> has_apod_

    # <<< has_apor_
    # @generated
    def get_has_apor_(self):
        """ A transmission path has a 'point-of-receipt' service point
        """
        return self._has_apor_

    def set_has_apor_(self, value):
        for x in self._has_apor_:
            x._point_of_receipt_for = None
        for y in value:
            y._point_of_receipt_for = self
        self._has_apor_ = value

    has_apor_ = property(get_has_apor_, set_has_apor_)

    def add_has_apor_(self, *has_apor_):
        for obj in has_apor_:
            obj._point_of_receipt_for = self
            self._has_apor_.append(obj)

    def remove_has_apor_(self, *has_apor_):
        for obj in has_apor_:
            obj._point_of_receipt_for = None
            self._has_apor_.remove(obj)
    # >>> has_apor_

    # <<< member_of
    # @generated
    def get_member_of(self):
        """ A transmission path's service point is part of an interchange area
        """
        return self._member_of

    def set_member_of(self, value):
        if self._member_of is not None:
            filtered = [x for x in self.member_of.part_of if x != self]
            self._member_of._part_of = filtered

        self._member_of = value
        if self._member_of is not None:
            self._member_of._part_of.append(self)

    member_of = property(get_member_of, set_member_of)
    # >>> member_of

    # <<< generation_provider
    # @generated
    def get_generation_provider(self):
        """ A GenerationProvider has one or more ServicePoints where energy is injected into the network.
        """
        return self._generation_provider

    def set_generation_provider(self, value):
        if self._generation_provider is not None:
            filtered = [x for x in self.generation_provider.service_point if x != self]
            self._generation_provider._service_point = filtered

        self._generation_provider = value
        if self._generation_provider is not None:
            self._generation_provider._service_point.append(self)

    generation_provider = property(get_generation_provider, set_generation_provider)
    # >>> generation_provider


    def __str__(self):
        """ Returns a string representation of the ServicePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< service_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ServicePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ServicePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.customer_consumer is not None:
            s += '%s<%s:ServicePoint.customer_consumer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_consumer.uri)
        if self.declare_tie_point is not None:
            s += '%s<%s:ServicePoint.declare_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.declare_tie_point.uri)
        for obj in self.energy_products:
            s += '%s<%s:ServicePoint.energy_products rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transmission_provider is not None:
            s += '%s<%s:ServicePoint.transmission_provider rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transmission_provider.uri)
        for obj in self.has_apod_:
            s += '%s<%s:ServicePoint.has_apod_ rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.has_apor_:
            s += '%s<%s:ServicePoint.has_apor_ rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of is not None:
            s += '%s<%s:ServicePoint.member_of rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of.uri)
        if self.generation_provider is not None:
            s += '%s<%s:ServicePoint.generation_provider rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generation_provider.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ServicePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> service_point.serialize


class ServiceReservation(Element):
    """ A ServiceReservation is a reservation for either AncillaryServices or TransmissionServices. In the case of TransmissionServices, this is the right to some amount of AvailableTransmissionCapacity for a product on a path in a direction for some specific period of time
    """
    # <<< service_reservation
    # @generated
    def __init__(self, holds=None, resells=None, reserves_ancillary_services=None, sells=None, reserves_transmission_service=None, **kw_args):
        """ Initialises a new 'ServiceReservation' instance.
        """

        self._holds = None
        self.holds = holds

        self._resells = None
        self.resells = resells

        self._reserves_ancillary_services = []
        if reserves_ancillary_services is not None:
            self.reserves_ancillary_services = reserves_ancillary_services
        else:
            self.reserves_ancillary_services = []

        self._sells = None
        self.sells = sells

        self._reserves_transmission_service = []
        if reserves_transmission_service is not None:
            self.reserves_transmission_service = reserves_transmission_service
        else:
            self.reserves_transmission_service = []


        super(ServiceReservation, self).__init__(**kw_args)
    # >>> service_reservation

    # <<< holds
    # @generated
    def get_holds(self):
        """ A Marketer holds title to a ServiceReservation.
        """
        return self._holds

    def set_holds(self, value):
        if self._holds is not None:
            filtered = [x for x in self.holds.held_by if x != self]
            self._holds._held_by = filtered

        self._holds = value
        if self._holds is not None:
            self._holds._held_by.append(self)

    holds = property(get_holds, set_holds)
    # >>> holds

    # <<< resells
    # @generated
    def get_resells(self):
        """ A ServiceReservation may be resold by a Marketer.
        """
        return self._resells

    def set_resells(self, value):
        if self._resells is not None:
            self._resells._resold_by = None

        self._resells = value
        if self._resells is not None:
            self._resells._resold_by = self

    resells = property(get_resells, set_resells)
    # >>> resells

    # <<< reserves_ancillary_services
    # @generated
    def get_reserves_ancillary_services(self):
        """ A ServiceReservation guarantees a certain AncillaryService.
        """
        return self._reserves_ancillary_services

    def set_reserves_ancillary_services(self, value):
        for x in self._reserves_ancillary_services:
            x._reserved_by_service_reservation = None
        for y in value:
            y._reserved_by_service_reservation = self
        self._reserves_ancillary_services = value

    reserves_ancillary_services = property(get_reserves_ancillary_services, set_reserves_ancillary_services)

    def add_reserves_ancillary_services(self, *reserves_ancillary_services):
        for obj in reserves_ancillary_services:
            obj._reserved_by_service_reservation = self
            self._reserves_ancillary_services.append(obj)

    def remove_reserves_ancillary_services(self, *reserves_ancillary_services):
        for obj in reserves_ancillary_services:
            obj._reserved_by_service_reservation = None
            self._reserves_ancillary_services.remove(obj)
    # >>> reserves_ancillary_services

    # <<< sells
    # @generated
    def get_sells(self):
        """ A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
        """
        return self._sells

    def set_sells(self, value):
        if self._sells is not None:
            filtered = [x for x in self.sells.sold_by if x != self]
            self._sells._sold_by = filtered

        self._sells = value
        if self._sells is not None:
            self._sells._sold_by.append(self)

    sells = property(get_sells, set_sells)
    # >>> sells

    # <<< reserves_transmission_service
    # @generated
    def get_reserves_transmission_service(self):
        """ A service reservation reserves a particular transmission service.
        """
        return self._reserves_transmission_service

    def set_reserves_transmission_service(self, value):
        for p in self._reserves_transmission_service:
            filtered = [q for q in p.reserved_by_service_reservation if q != self]
            self._reserves_transmission_service._reserved_by_service_reservation = filtered
        for r in value:
            if self not in r._reserved_by_service_reservation:
                r._reserved_by_service_reservation.append(self)
        self._reserves_transmission_service = value

    reserves_transmission_service = property(get_reserves_transmission_service, set_reserves_transmission_service)

    def add_reserves_transmission_service(self, *reserves_transmission_service):
        for obj in reserves_transmission_service:
            if self not in obj._reserved_by_service_reservation:
                obj._reserved_by_service_reservation.append(self)
            self._reserves_transmission_service.append(obj)

    def remove_reserves_transmission_service(self, *reserves_transmission_service):
        for obj in reserves_transmission_service:
            if self in obj._reserved_by_service_reservation:
                obj._reserved_by_service_reservation.remove(self)
            self._reserves_transmission_service.remove(obj)
    # >>> reserves_transmission_service


    def __str__(self):
        """ Returns a string representation of the ServiceReservation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< service_reservation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ServiceReservation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ServiceReservation", self.uri)
        if format:
            indent += ' ' * depth

        if self.holds is not None:
            s += '%s<%s:ServiceReservation.holds rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.holds.uri)
        if self.resells is not None:
            s += '%s<%s:ServiceReservation.resells rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.resells.uri)
        for obj in self.reserves_ancillary_services:
            s += '%s<%s:ServiceReservation.reserves_ancillary_services rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.sells is not None:
            s += '%s<%s:ServiceReservation.sells rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sells.uri)
        for obj in self.reserves_transmission_service:
            s += '%s<%s:ServiceReservation.reserves_transmission_service rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ServiceReservation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> service_reservation.serialize


class TransmissionPath(Element):
    """ An electrical connection, link, or line consisting of one or more parallel transmission elements between two areas of the interconnected electric systems, or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints.
    """
    # <<< transmission_path
    # @generated
    def __init__(self, total_transfer_capability=0.0, parallel_path_flag=False, avail_transfer_capability=0.0, offered_on=None, delivery_point_for=None, point_of_receipt_for=None, located_on=None, for=None, **kw_args):
        """ Initialises a new 'TransmissionPath' instance.
        """
        # The total transmission capability of a transmission path in the reference direction 
        self.total_transfer_capability = total_transfer_capability

        # Flag which indicates if the transmission path is also a designated interconnection 'parallel path' 
        self.parallel_path_flag = parallel_path_flag

        # The available transmission capability of a transmission path for the reference direction 
        self.avail_transfer_capability = avail_transfer_capability


        self._offered_on = []
        if offered_on is not None:
            self.offered_on = offered_on
        else:
            self.offered_on = []

        self._delivery_point_for = None
        self.delivery_point_for = delivery_point_for

        self._point_of_receipt_for = None
        self.point_of_receipt_for = point_of_receipt_for

        self._located_on = []
        if located_on is not None:
            self.located_on = located_on
        else:
            self.located_on = []

        self._for = None
        self.for = for


        super(TransmissionPath, self).__init__(**kw_args)
    # >>> transmission_path

    # <<< offered_on
    # @generated
    def get_offered_on(self):
        """ A transmission service is offered on a transmission path.
        """
        return self._offered_on

    def set_offered_on(self, value):
        for p in self._offered_on:
            filtered = [q for q in p.offering if q != self]
            self._offered_on._offering = filtered
        for r in value:
            if self not in r._offering:
                r._offering.append(self)
        self._offered_on = value

    offered_on = property(get_offered_on, set_offered_on)

    def add_offered_on(self, *offered_on):
        for obj in offered_on:
            if self not in obj._offering:
                obj._offering.append(self)
            self._offered_on.append(obj)

    def remove_offered_on(self, *offered_on):
        for obj in offered_on:
            if self in obj._offering:
                obj._offering.remove(self)
            self._offered_on.remove(obj)
    # >>> offered_on

    # <<< delivery_point_for
    # @generated
    def get_delivery_point_for(self):
        """ A transmission path has a 'point-of-delivery' service point
        """
        return self._delivery_point_for

    def set_delivery_point_for(self, value):
        if self._delivery_point_for is not None:
            filtered = [x for x in self.delivery_point_for.has_apod_ if x != self]
            self._delivery_point_for._has_apod_ = filtered

        self._delivery_point_for = value
        if self._delivery_point_for is not None:
            self._delivery_point_for._has_apod_.append(self)

    delivery_point_for = property(get_delivery_point_for, set_delivery_point_for)
    # >>> delivery_point_for

    # <<< point_of_receipt_for
    # @generated
    def get_point_of_receipt_for(self):
        """ A transmission path has a 'point-of-receipt' service point
        """
        return self._point_of_receipt_for

    def set_point_of_receipt_for(self, value):
        if self._point_of_receipt_for is not None:
            filtered = [x for x in self.point_of_receipt_for.has_apor_ if x != self]
            self._point_of_receipt_for._has_apor_ = filtered

        self._point_of_receipt_for = value
        if self._point_of_receipt_for is not None:
            self._point_of_receipt_for._has_apor_.append(self)

    point_of_receipt_for = property(get_point_of_receipt_for, set_point_of_receipt_for)
    # >>> point_of_receipt_for

    # <<< located_on
    # @generated
    def get_located_on(self):
        """ A transmission product is located on a transmission path.
        """
        return self._located_on

    def set_located_on(self, value):
        for p in self._located_on:
            filtered = [q for q in p.location_for if q != self]
            self._located_on._location_for = filtered
        for r in value:
            if self not in r._location_for:
                r._location_for.append(self)
        self._located_on = value

    located_on = property(get_located_on, set_located_on)

    def add_located_on(self, *located_on):
        for obj in located_on:
            if self not in obj._location_for:
                obj._location_for.append(self)
            self._located_on.append(obj)

    def remove_located_on(self, *located_on):
        for obj in located_on:
            if self in obj._location_for:
                obj._location_for.remove(self)
            self._located_on.remove(obj)
    # >>> located_on

    # <<< for
    # @generated
    def get_for(self):
        """ A TransmissionPath is contained in a TransmissionCorridor.
        """
        return self._for

    def set_for(self, value):
        if self._for is not None:
            filtered = [x for x in self.for.contained_in if x != self]
            self._for._contained_in = filtered

        self._for = value
        if self._for is not None:
            self._for._contained_in.append(self)

    for = property(get_for, set_for)
    # >>> for


    def __str__(self):
        """ Returns a string representation of the TransmissionPath.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transmission_path.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransmissionPath.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransmissionPath", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.offered_on:
            s += '%s<%s:TransmissionPath.offered_on rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.delivery_point_for is not None:
            s += '%s<%s:TransmissionPath.delivery_point_for rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.delivery_point_for.uri)
        if self.point_of_receipt_for is not None:
            s += '%s<%s:TransmissionPath.point_of_receipt_for rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.point_of_receipt_for.uri)
        for obj in self.located_on:
            s += '%s<%s:TransmissionPath.located_on rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.for is not None:
            s += '%s<%s:TransmissionPath.for rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for.uri)
        s += '%s<%s:TransmissionPath.total_transfer_capability>%s</%s:TransmissionPath.total_transfer_capability>' % \
            (indent, ns_prefix, self.total_transfer_capability, ns_prefix)
        s += '%s<%s:TransmissionPath.parallel_path_flag>%s</%s:TransmissionPath.parallel_path_flag>' % \
            (indent, ns_prefix, self.parallel_path_flag, ns_prefix)
        s += '%s<%s:TransmissionPath.avail_transfer_capability>%s</%s:TransmissionPath.avail_transfer_capability>' % \
            (indent, ns_prefix, self.avail_transfer_capability, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransmissionPath")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transmission_path.serialize


class AncillaryService(IdentifiedObject):
    """ All of these services relate  to various aspects of insuring that the production of energy matches consumption of energy at any given time.  They are very critical to the security and reliability of the interconnected network. Some examples of AncillaryServices include Operating/Supplemental Reserve, Energy Imbalance Service, Operating/Spinning Reserve, Reactive Supply and Voltage Control, and Regulation and Frequency Response.
    """
    # <<< ancillary_service
    # @generated
    def __init__(self, transmission_providers=None, control_area_operator=None, reserved_by_service_reservation=None, open_access_product=None, **kw_args):
        """ Initialises a new 'AncillaryService' instance.
        """

        self._transmission_providers = []
        if transmission_providers is not None:
            self.transmission_providers = transmission_providers
        else:
            self.transmission_providers = []

        self._control_area_operator = None
        self.control_area_operator = control_area_operator

        self._reserved_by_service_reservation = None
        self.reserved_by_service_reservation = reserved_by_service_reservation

        self._open_access_product = None
        self.open_access_product = open_access_product


        super(AncillaryService, self).__init__(**kw_args)
    # >>> ancillary_service

    # <<< transmission_providers
    # @generated
    def get_transmission_providers(self):
        """ A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
        """
        return self._transmission_providers

    def set_transmission_providers(self, value):
        for p in self._transmission_providers:
            filtered = [q for q in p.ancillary_services if q != self]
            self._transmission_providers._ancillary_services = filtered
        for r in value:
            if self not in r._ancillary_services:
                r._ancillary_services.append(self)
        self._transmission_providers = value

    transmission_providers = property(get_transmission_providers, set_transmission_providers)

    def add_transmission_providers(self, *transmission_providers):
        for obj in transmission_providers:
            if self not in obj._ancillary_services:
                obj._ancillary_services.append(self)
            self._transmission_providers.append(obj)

    def remove_transmission_providers(self, *transmission_providers):
        for obj in transmission_providers:
            if self in obj._ancillary_services:
                obj._ancillary_services.remove(self)
            self._transmission_providers.remove(obj)
    # >>> transmission_providers

    # <<< control_area_operator
    # @generated
    def get_control_area_operator(self):
        """ Sale of ancillary services provided by ControlAreaOperators.
        """
        return self._control_area_operator

    def set_control_area_operator(self, value):
        if self._control_area_operator is not None:
            filtered = [x for x in self.control_area_operator.ancillary_service if x != self]
            self._control_area_operator._ancillary_service = filtered

        self._control_area_operator = value
        if self._control_area_operator is not None:
            self._control_area_operator._ancillary_service.append(self)

    control_area_operator = property(get_control_area_operator, set_control_area_operator)
    # >>> control_area_operator

    # <<< reserved_by_service_reservation
    # @generated
    def get_reserved_by_service_reservation(self):
        """ A ServiceReservation guarantees a certain AncillaryService.
        """
        return self._reserved_by_service_reservation

    def set_reserved_by_service_reservation(self, value):
        if self._reserved_by_service_reservation is not None:
            filtered = [x for x in self.reserved_by_service_reservation.reserves_ancillary_services if x != self]
            self._reserved_by_service_reservation._reserves_ancillary_services = filtered

        self._reserved_by_service_reservation = value
        if self._reserved_by_service_reservation is not None:
            self._reserved_by_service_reservation._reserves_ancillary_services.append(self)

    reserved_by_service_reservation = property(get_reserved_by_service_reservation, set_reserved_by_service_reservation)
    # >>> reserved_by_service_reservation

    # <<< open_access_product
    # @generated
    def get_open_access_product(self):
        """ AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
        """
        return self._open_access_product

    def set_open_access_product(self, value):
        if self._open_access_product is not None:
            filtered = [x for x in self.open_access_product.ancillary_services if x != self]
            self._open_access_product._ancillary_services = filtered

        self._open_access_product = value
        if self._open_access_product is not None:
            self._open_access_product._ancillary_services.append(self)

    open_access_product = property(get_open_access_product, set_open_access_product)
    # >>> open_access_product


    def __str__(self):
        """ Returns a string representation of the AncillaryService.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ancillary_service.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AncillaryService.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AncillaryService", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.transmission_providers:
            s += '%s<%s:AncillaryService.transmission_providers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.control_area_operator is not None:
            s += '%s<%s:AncillaryService.control_area_operator rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area_operator.uri)
        if self.reserved_by_service_reservation is not None:
            s += '%s<%s:AncillaryService.reserved_by_service_reservation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reserved_by_service_reservation.uri)
        if self.open_access_product is not None:
            s += '%s<%s:AncillaryService.open_access_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.open_access_product.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AncillaryService")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ancillary_service.serialize


# <<< reservation
# @generated
# >>> reservation
