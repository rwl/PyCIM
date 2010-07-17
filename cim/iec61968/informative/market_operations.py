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


from cim.iec61970.core import Curve
from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Document
from cim import Element
from cim.iec61968.informative.inf_erpsupport import ErpOrganisation
from cim.iec61968.informative.energy_scheduling import Profile
from cim.iec61968.common import Agreement
from cim.iec61970.core import RegularIntervalSchedule
from cim.iec61970.core import PowerSystemResource
from cim.iec61970.meas import Limit

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.marketoperations"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#MarketOperations"

class ContingencyConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a constraint for a specific contingency. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """
    # <<< contingency_constraint_limit
    # @generated
    def __init__(self, mwlimit_schedules=None, contingency=None, security_constraint_sum=None, **kw_args):
        """ Initialises a new 'ContingencyConstraintLimit' instance.
        """

        self._mwlimit_schedules = None
        self.mwlimit_schedules = mwlimit_schedules

        self._contingency = None
        self.contingency = contingency

        self._security_constraint_sum = None
        self.security_constraint_sum = security_constraint_sum


        super(ContingencyConstraintLimit, self).__init__(**kw_args)
    # >>> contingency_constraint_limit

    # <<< mwlimit_schedules
    # @generated
    def get_mwlimit_schedules(self):
        """ 
        """
        return self._mwlimit_schedules

    def set_mwlimit_schedules(self, value):
        if self._mwlimit_schedules is not None:
            self._mwlimit_schedules._security_constraint_limit = None

        self._mwlimit_schedules = value
        if self._mwlimit_schedules is not None:
            self._mwlimit_schedules._security_constraint_limit = self

    mwlimit_schedules = property(get_mwlimit_schedules, set_mwlimit_schedules)
    # >>> mwlimit_schedules

    # <<< contingency
    # @generated
    def get_contingency(self):
        """ 
        """
        return self._contingency

    def set_contingency(self, value):
        if self._contingency is not None:
            filtered = [x for x in self.contingency.contingency_constraint_limit if x != self]
            self._contingency._contingency_constraint_limit = filtered

        self._contingency = value
        if self._contingency is not None:
            self._contingency._contingency_constraint_limit.append(self)

    contingency = property(get_contingency, set_contingency)
    # >>> contingency

    # <<< security_constraint_sum
    # @generated
    def get_security_constraint_sum(self):
        """ 
        """
        return self._security_constraint_sum

    def set_security_constraint_sum(self, value):
        if self._security_constraint_sum is not None:
            filtered = [x for x in self.security_constraint_sum.contingency_constraint_limits if x != self]
            self._security_constraint_sum._contingency_constraint_limits = filtered

        self._security_constraint_sum = value
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._contingency_constraint_limits.append(self)

    security_constraint_sum = property(get_security_constraint_sum, set_security_constraint_sum)
    # >>> security_constraint_sum


    def __str__(self):
        """ Returns a string representation of the ContingencyConstraintLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< contingency_constraint_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ContingencyConstraintLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ContingencyConstraintLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.mwlimit_schedules is not None:
            s += '%s<%s:ContingencyConstraintLimit.mwlimit_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.mwlimit_schedules.uri)
        if self.contingency is not None:
            s += '%s<%s:ContingencyConstraintLimit.contingency rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.contingency.uri)
        if self.security_constraint_sum is not None:
            s += '%s<%s:ContingencyConstraintLimit.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ContingencyConstraintLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> contingency_constraint_limit.serialize


class ResourceGroupReq(IdentifiedObject):
    """ Ancillary service requirements for a market.
    """
    # <<< resource_group_req
    # @generated
    def __init__(self, resource_group=None, rtos=None, **kw_args):
        """ Initialises a new 'ResourceGroupReq' instance.
        """

        self._resource_group = None
        self.resource_group = resource_group

        self._rtos = []
        if rtos is not None:
            self.rtos = rtos
        else:
            self.rtos = []


        super(ResourceGroupReq, self).__init__(**kw_args)
    # >>> resource_group_req

    # <<< resource_group
    # @generated
    def get_resource_group(self):
        """ 
        """
        return self._resource_group

    def set_resource_group(self, value):
        if self._resource_group is not None:
            filtered = [x for x in self.resource_group.resource_group_reqs if x != self]
            self._resource_group._resource_group_reqs = filtered

        self._resource_group = value
        if self._resource_group is not None:
            self._resource_group._resource_group_reqs.append(self)

    resource_group = property(get_resource_group, set_resource_group)
    # >>> resource_group

    # <<< rtos
    # @generated
    def get_rtos(self):
        """ 
        """
        return self._rtos

    def set_rtos(self, value):
        for p in self._rtos:
            filtered = [q for q in p.resource_group_reqs if q != self]
            self._rtos._resource_group_reqs = filtered
        for r in value:
            if self not in r._resource_group_reqs:
                r._resource_group_reqs.append(self)
        self._rtos = value

    rtos = property(get_rtos, set_rtos)

    def add_rtos(self, *rtos):
        for obj in rtos:
            if self not in obj._resource_group_reqs:
                obj._resource_group_reqs.append(self)
            self._rtos.append(obj)

    def remove_rtos(self, *rtos):
        for obj in rtos:
            if self in obj._resource_group_reqs:
                obj._resource_group_reqs.remove(self)
            self._rtos.remove(obj)
    # >>> rtos


    def __str__(self):
        """ Returns a string representation of the ResourceGroupReq.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< resource_group_req.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ResourceGroupReq.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ResourceGroupReq", self.uri)
        if format:
            indent += ' ' * depth

        if self.resource_group is not None:
            s += '%s<%s:ResourceGroupReq.resource_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.resource_group.uri)
        for obj in self.rtos:
            s += '%s<%s:ResourceGroupReq.rtos rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ResourceGroupReq")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> resource_group_req.serialize


class MarketFactors(Document):
    """ Aggregation of market information relative for a specific time interval.
    """
    # <<< market_factors
    # @generated
    def __init__(self, interval_start_time='', erp_invoices=None, market=None, **kw_args):
        """ Initialises a new 'MarketFactors' instance.
        """
        # The start of the time interval for which requirement is defined. 
        self.interval_start_time = interval_start_time


        self._erp_invoices = []
        if erp_invoices is not None:
            self.erp_invoices = erp_invoices
        else:
            self.erp_invoices = []

        self._market = None
        self.market = market


        super(MarketFactors, self).__init__(**kw_args)
    # >>> market_factors

    # <<< erp_invoices
    # @generated
    def get_erp_invoices(self):
        """ 
        """
        return self._erp_invoices

    def set_erp_invoices(self, value):
        for p in self._erp_invoices:
            filtered = [q for q in p.market_factors if q != self]
            self._erp_invoices._market_factors = filtered
        for r in value:
            if self not in r._market_factors:
                r._market_factors.append(self)
        self._erp_invoices = value

    erp_invoices = property(get_erp_invoices, set_erp_invoices)

    def add_erp_invoices(self, *erp_invoices):
        for obj in erp_invoices:
            if self not in obj._market_factors:
                obj._market_factors.append(self)
            self._erp_invoices.append(obj)

    def remove_erp_invoices(self, *erp_invoices):
        for obj in erp_invoices:
            if self in obj._market_factors:
                obj._market_factors.remove(self)
            self._erp_invoices.remove(obj)
    # >>> erp_invoices

    # <<< market
    # @generated
    def get_market(self):
        """ 
        """
        return self._market

    def set_market(self, value):
        if self._market is not None:
            filtered = [x for x in self.market.market_factors if x != self]
            self._market._market_factors = filtered

        self._market = value
        if self._market is not None:
            self._market._market_factors.append(self)

    market = property(get_market, set_market)
    # >>> market


    def __str__(self):
        """ Returns a string representation of the MarketFactors.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_factors.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketFactors.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketFactors", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketFactors")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_factors.serialize


class Settlement(Document):
    """ Specifies a settlement run.
    """
    # <<< settlement
    # @generated
    def __init__(self, trade_date='', market=None, erp_ledger_entries=None, erp_invoice_line_items=None, **kw_args):
        """ Initialises a new 'Settlement' instance.
        """
        # The trade date on which the settlement is run. 
        self.trade_date = trade_date


        self._market = None
        self.market = market

        self._erp_ledger_entries = []
        if erp_ledger_entries is not None:
            self.erp_ledger_entries = erp_ledger_entries
        else:
            self.erp_ledger_entries = []

        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []


        super(Settlement, self).__init__(**kw_args)
    # >>> settlement

    # <<< market
    # @generated
    def get_market(self):
        """ 
        """
        return self._market

    def set_market(self, value):
        if self._market is not None:
            filtered = [x for x in self.market.settlements if x != self]
            self._market._settlements = filtered

        self._market = value
        if self._market is not None:
            self._market._settlements.append(self)

    market = property(get_market, set_market)
    # >>> market

    # <<< erp_ledger_entries
    # @generated
    def get_erp_ledger_entries(self):
        """ 
        """
        return self._erp_ledger_entries

    def set_erp_ledger_entries(self, value):
        for p in self._erp_ledger_entries:
            filtered = [q for q in p.settlements if q != self]
            self._erp_ledger_entries._settlements = filtered
        for r in value:
            if self not in r._settlements:
                r._settlements.append(self)
        self._erp_ledger_entries = value

    erp_ledger_entries = property(get_erp_ledger_entries, set_erp_ledger_entries)

    def add_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            if self not in obj._settlements:
                obj._settlements.append(self)
            self._erp_ledger_entries.append(obj)

    def remove_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            if self in obj._settlements:
                obj._settlements.remove(self)
            self._erp_ledger_entries.remove(obj)
    # >>> erp_ledger_entries

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for p in self._erp_invoice_line_items:
            filtered = [q for q in p.settlements if q != self]
            self._erp_invoice_line_items._settlements = filtered
        for r in value:
            if self not in r._settlements:
                r._settlements.append(self)
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self not in obj._settlements:
                obj._settlements.append(self)
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self in obj._settlements:
                obj._settlements.remove(self)
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items


    def __str__(self):
        """ Returns a string representation of the Settlement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< settlement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Settlement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Settlement", self.uri)
        if format:
            indent += ' ' * depth

        if self.market is not None:
            s += '%s<%s:Settlement.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.erp_ledger_entries:
            s += '%s<%s:Settlement.erp_ledger_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_invoice_line_items:
            s += '%s<%s:Settlement.erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Settlement.trade_date>%s</%s:Settlement.trade_date>' % \
            (indent, ns_prefix, self.trade_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Settlement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> settlement.serialize


class ConstraintTerm(IdentifiedObject):
    """ A constraint term is one element of a linear constraint.
    """
    # <<< constraint_term
    # @generated
    def __init__(self, factor='', function='', security_constraint_sum=None, **kw_args):
        """ Initialises a new 'ConstraintTerm' instance.
        """
 
        self.factor = factor

        # The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow. 
        self.function = function


        self._security_constraint_sum = None
        self.security_constraint_sum = security_constraint_sum


        super(ConstraintTerm, self).__init__(**kw_args)
    # >>> constraint_term

    # <<< security_constraint_sum
    # @generated
    def get_security_constraint_sum(self):
        """ 
        """
        return self._security_constraint_sum

    def set_security_constraint_sum(self, value):
        if self._security_constraint_sum is not None:
            filtered = [x for x in self.security_constraint_sum.constraint_terms if x != self]
            self._security_constraint_sum._constraint_terms = filtered

        self._security_constraint_sum = value
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._constraint_terms.append(self)

    security_constraint_sum = property(get_security_constraint_sum, set_security_constraint_sum)
    # >>> security_constraint_sum


    def __str__(self):
        """ Returns a string representation of the ConstraintTerm.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< constraint_term.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConstraintTerm.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConstraintTerm", self.uri)
        if format:
            indent += ' ' * depth

        if self.security_constraint_sum is not None:
            s += '%s<%s:ConstraintTerm.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
        s += '%s<%s:ConstraintTerm.factor>%s</%s:ConstraintTerm.factor>' % \
            (indent, ns_prefix, self.factor, ns_prefix)
        s += '%s<%s:ConstraintTerm.function>%s</%s:ConstraintTerm.function>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConstraintTerm")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> constraint_term.serialize


class Meter(IdentifiedObject):
    """ This is generic logical meter object.
    """
    # <<< meter
    # @generated
    def __init__(self, registered_resource=None, **kw_args):
        """ Initialises a new 'Meter' instance.
        """

        self._registered_resource = None
        self.registered_resource = registered_resource


        super(Meter, self).__init__(**kw_args)
    # >>> meter

    # <<< registered_resource
    # @generated
    def get_registered_resource(self):
        """ 
        """
        return self._registered_resource

    def set_registered_resource(self, value):
        if self._registered_resource is not None:
            filtered = [x for x in self.registered_resource.meters if x != self]
            self._registered_resource._meters = filtered

        self._registered_resource = value
        if self._registered_resource is not None:
            self._registered_resource._meters.append(self)

    registered_resource = property(get_registered_resource, set_registered_resource)
    # >>> registered_resource


    def __str__(self):
        """ Returns a string representation of the Meter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Meter.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Meter", self.uri)
        if format:
            indent += ' ' * depth

        if self.registered_resource is not None:
            s += '%s<%s:Meter.registered_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.registered_resource.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Meter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meter.serialize


class EnergyPriceCurve(Curve):
    """ Relationship between a price in $/hour (Y-axis) and a MW value (X-axis).
    """
    # <<< energy_price_curve
    # @generated
    def __init__(self, energy_transactions=None, ftrs=None, **kw_args):
        """ Initialises a new 'EnergyPriceCurve' instance.
        """

        self._energy_transactions = []
        if energy_transactions is not None:
            self.energy_transactions = energy_transactions
        else:
            self.energy_transactions = []

        self._ftrs = []
        if ftrs is not None:
            self.ftrs = ftrs
        else:
            self.ftrs = []


        super(EnergyPriceCurve, self).__init__(**kw_args)
    # >>> energy_price_curve

    # <<< energy_transactions
    # @generated
    def get_energy_transactions(self):
        """ 
        """
        return self._energy_transactions

    def set_energy_transactions(self, value):
        for p in self._energy_transactions:
            filtered = [q for q in p.energy_price_curves if q != self]
            self._energy_transactions._energy_price_curves = filtered
        for r in value:
            if self not in r._energy_price_curves:
                r._energy_price_curves.append(self)
        self._energy_transactions = value

    energy_transactions = property(get_energy_transactions, set_energy_transactions)

    def add_energy_transactions(self, *energy_transactions):
        for obj in energy_transactions:
            if self not in obj._energy_price_curves:
                obj._energy_price_curves.append(self)
            self._energy_transactions.append(obj)

    def remove_energy_transactions(self, *energy_transactions):
        for obj in energy_transactions:
            if self in obj._energy_price_curves:
                obj._energy_price_curves.remove(self)
            self._energy_transactions.remove(obj)
    # >>> energy_transactions

    # <<< ftrs
    # @generated
    def get_ftrs(self):
        """ 
        """
        return self._ftrs

    def set_ftrs(self, value):
        for x in self._ftrs:
            x._energy_price_curve = None
        for y in value:
            y._energy_price_curve = self
        self._ftrs = value

    ftrs = property(get_ftrs, set_ftrs)

    def add_ftrs(self, *ftrs):
        for obj in ftrs:
            obj._energy_price_curve = self
            self._ftrs.append(obj)

    def remove_ftrs(self, *ftrs):
        for obj in ftrs:
            obj._energy_price_curve = None
            self._ftrs.remove(obj)
    # >>> ftrs


    def __str__(self):
        """ Returns a string representation of the EnergyPriceCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_price_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyPriceCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyPriceCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.energy_transactions:
            s += '%s<%s:EnergyPriceCurve.energy_transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.ftrs:
            s += '%s<%s:EnergyPriceCurve.ftrs rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyPriceCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_price_curve.serialize


class MarketStatement(Document):
    """ A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time.
    """
    # <<< market_statement
    # @generated
    def __init__(self, trade_date='', reference_number='', start='', end='', transaction_date='', market_statement_line_item=None, **kw_args):
        """ Initialises a new 'MarketStatement' instance.
        """
        # The date of which Settlement is run. 
        self.trade_date = trade_date

        # The version number of previous statement (in the case of true up). 
        self.reference_number = reference_number

        # The start of a bill period. 
        self.start = start

        # The end of a bill period. 
        self.end = end

        # The date of which this statement is issued. 
        self.transaction_date = transaction_date


        self._market_statement_line_item = []
        if market_statement_line_item is not None:
            self.market_statement_line_item = market_statement_line_item
        else:
            self.market_statement_line_item = []


        super(MarketStatement, self).__init__(**kw_args)
    # >>> market_statement

    # <<< market_statement_line_item
    # @generated
    def get_market_statement_line_item(self):
        """ 
        """
        return self._market_statement_line_item

    def set_market_statement_line_item(self, value):
        for x in self._market_statement_line_item:
            x._market_statement = None
        for y in value:
            y._market_statement = self
        self._market_statement_line_item = value

    market_statement_line_item = property(get_market_statement_line_item, set_market_statement_line_item)

    def add_market_statement_line_item(self, *market_statement_line_item):
        for obj in market_statement_line_item:
            obj._market_statement = self
            self._market_statement_line_item.append(obj)

    def remove_market_statement_line_item(self, *market_statement_line_item):
        for obj in market_statement_line_item:
            obj._market_statement = None
            self._market_statement_line_item.remove(obj)
    # >>> market_statement_line_item


    def __str__(self):
        """ Returns a string representation of the MarketStatement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_statement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketStatement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketStatement", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.market_statement_line_item:
            s += '%s<%s:MarketStatement.market_statement_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:MarketStatement.trade_date>%s</%s:MarketStatement.trade_date>' % \
            (indent, ns_prefix, self.trade_date, ns_prefix)
        s += '%s<%s:MarketStatement.reference_number>%s</%s:MarketStatement.reference_number>' % \
            (indent, ns_prefix, self.reference_number, ns_prefix)
        s += '%s<%s:MarketStatement.start>%s</%s:MarketStatement.start>' % \
            (indent, ns_prefix, self.start, ns_prefix)
        s += '%s<%s:MarketStatement.end>%s</%s:MarketStatement.end>' % \
            (indent, ns_prefix, self.end, ns_prefix)
        s += '%s<%s:MarketStatement.transaction_date>%s</%s:MarketStatement.transaction_date>' % \
            (indent, ns_prefix, self.transaction_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketStatement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_statement.serialize


class StartUpTimeCurve(Curve):
    """ Startup time curve as a function of down time, where time is specified in seconds.  Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis).
    """
    # <<< start_up_time_curve
    # @generated
    def __init__(self, generating_bids=None, **kw_args):
        """ Initialises a new 'StartUpTimeCurve' instance.
        """

        self._generating_bids = []
        if generating_bids is not None:
            self.generating_bids = generating_bids
        else:
            self.generating_bids = []


        super(StartUpTimeCurve, self).__init__(**kw_args)
    # >>> start_up_time_curve

    # <<< generating_bids
    # @generated
    def get_generating_bids(self):
        """ 
        """
        return self._generating_bids

    def set_generating_bids(self, value):
        for x in self._generating_bids:
            x._start_up_time_curve = None
        for y in value:
            y._start_up_time_curve = self
        self._generating_bids = value

    generating_bids = property(get_generating_bids, set_generating_bids)

    def add_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._start_up_time_curve = self
            self._generating_bids.append(obj)

    def remove_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._start_up_time_curve = None
            self._generating_bids.remove(obj)
    # >>> generating_bids


    def __str__(self):
        """ Returns a string representation of the StartUpTimeCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< start_up_time_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StartUpTimeCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StartUpTimeCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.generating_bids:
            s += '%s<%s:StartUpTimeCurve.generating_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "StartUpTimeCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> start_up_time_curve.serialize


class Bid(Document):
    """ Represents both bids to purchase and offers to sell energy or ancillary services in an RTO-sponsored market.
    """
    # <<< bid
    # @generated
    def __init__(self, stop_time='', start_time='', market_type='', market=None, product_bids=None, bid_clearing=None, **kw_args):
        """ Initialises a new 'Bid' instance.
        """
        # Stop time and date for which bid is applicable. 
        self.stop_time = stop_time

        # Start time and date for which bid applies. 
        self.start_time = start_time

 
        self.market_type = market_type


        self._market = None
        self.market = market

        self._product_bids = []
        if product_bids is not None:
            self.product_bids = product_bids
        else:
            self.product_bids = []

        self._bid_clearing = None
        self.bid_clearing = bid_clearing


        super(Bid, self).__init__(**kw_args)
    # >>> bid

    # <<< market
    # @generated
    def get_market(self):
        """ 
        """
        return self._market

    def set_market(self, value):
        if self._market is not None:
            filtered = [x for x in self.market.bids if x != self]
            self._market._bids = filtered

        self._market = value
        if self._market is not None:
            self._market._bids.append(self)

    market = property(get_market, set_market)
    # >>> market

    # <<< product_bids
    # @generated
    def get_product_bids(self):
        """ A bid comprises one or more product bids of market products
        """
        return self._product_bids

    def set_product_bids(self, value):
        for x in self._product_bids:
            x._bid = None
        for y in value:
            y._bid = self
        self._product_bids = value

    product_bids = property(get_product_bids, set_product_bids)

    def add_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._bid = self
            self._product_bids.append(obj)

    def remove_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._bid = None
            self._product_bids.remove(obj)
    # >>> product_bids

    # <<< bid_clearing
    # @generated
    def get_bid_clearing(self):
        """ 
        """
        return self._bid_clearing

    def set_bid_clearing(self, value):
        if self._bid_clearing is not None:
            self._bid_clearing._bid = None

        self._bid_clearing = value
        if self._bid_clearing is not None:
            self._bid_clearing._bid = self

    bid_clearing = property(get_bid_clearing, set_bid_clearing)
    # >>> bid_clearing


    def __str__(self):
        """ Returns a string representation of the Bid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Bid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Bid", self.uri)
        if format:
            indent += ' ' * depth

        if self.market is not None:
            s += '%s<%s:Bid.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.product_bids:
            s += '%s<%s:Bid.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bid_clearing is not None:
            s += '%s<%s:Bid.bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_clearing.uri)
        s += '%s<%s:Bid.stop_time>%s</%s:Bid.stop_time>' % \
            (indent, ns_prefix, self.stop_time, ns_prefix)
        s += '%s<%s:Bid.start_time>%s</%s:Bid.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Bid.market_type>%s</%s:Bid.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Bid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bid.serialize


class BidClearing(Element):
    """ Bid clearing results posted for a given settlement period.
    """
    # <<< bid_clearing
    # @generated
    def __init__(self, no_load_cost=0.0, start_up_cost=0.0, lost_op_cost=0.0, bid=None, **kw_args):
        """ Initialises a new 'BidClearing' instance.
        """
        # No-load cost in monetary units. 
        self.no_load_cost = no_load_cost

        # Start up cost in case of energy commodity in monetary units. 
        self.start_up_cost = start_up_cost

        # Energy lost opportunity cost in monetary units. 
        self.lost_op_cost = lost_op_cost


        self._bid = None
        self.bid = bid


        super(BidClearing, self).__init__(**kw_args)
    # >>> bid_clearing

    # <<< bid
    # @generated
    def get_bid(self):
        """ 
        """
        return self._bid

    def set_bid(self, value):
        if self._bid is not None:
            self._bid._bid_clearing = None

        self._bid = value
        if self._bid is not None:
            self._bid._bid_clearing = self

    bid = property(get_bid, set_bid)
    # >>> bid


    def __str__(self):
        """ Returns a string representation of the BidClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bid_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BidClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BidClearing", self.uri)
        if format:
            indent += ' ' * depth

        if self.bid is not None:
            s += '%s<%s:BidClearing.bid rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid.uri)
        s += '%s<%s:BidClearing.no_load_cost>%s</%s:BidClearing.no_load_cost>' % \
            (indent, ns_prefix, self.no_load_cost, ns_prefix)
        s += '%s<%s:BidClearing.start_up_cost>%s</%s:BidClearing.start_up_cost>' % \
            (indent, ns_prefix, self.start_up_cost, ns_prefix)
        s += '%s<%s:BidClearing.lost_op_cost>%s</%s:BidClearing.lost_op_cost>' % \
            (indent, ns_prefix, self.lost_op_cost, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BidClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bid_clearing.serialize


class ResourceGroup(IdentifiedObject):
    """ A logical grouping of resources that are used to model location of types of requirements for ancillary services such as spinning reserve zones, regulation zones, etc.
    """
    # <<< resource_group
    # @generated
    def __init__(self, registered_resources=None, resource_group_reqs=None, **kw_args):
        """ Initialises a new 'ResourceGroup' instance.
        """

        self._registered_resources = []
        if registered_resources is not None:
            self.registered_resources = registered_resources
        else:
            self.registered_resources = []

        self._resource_group_reqs = []
        if resource_group_reqs is not None:
            self.resource_group_reqs = resource_group_reqs
        else:
            self.resource_group_reqs = []


        super(ResourceGroup, self).__init__(**kw_args)
    # >>> resource_group

    # <<< registered_resources
    # @generated
    def get_registered_resources(self):
        """ 
        """
        return self._registered_resources

    def set_registered_resources(self, value):
        for p in self._registered_resources:
            filtered = [q for q in p.resource_groups if q != self]
            self._registered_resources._resource_groups = filtered
        for r in value:
            if self not in r._resource_groups:
                r._resource_groups.append(self)
        self._registered_resources = value

    registered_resources = property(get_registered_resources, set_registered_resources)

    def add_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self not in obj._resource_groups:
                obj._resource_groups.append(self)
            self._registered_resources.append(obj)

    def remove_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self in obj._resource_groups:
                obj._resource_groups.remove(self)
            self._registered_resources.remove(obj)
    # >>> registered_resources

    # <<< resource_group_reqs
    # @generated
    def get_resource_group_reqs(self):
        """ 
        """
        return self._resource_group_reqs

    def set_resource_group_reqs(self, value):
        for x in self._resource_group_reqs:
            x._resource_group = None
        for y in value:
            y._resource_group = self
        self._resource_group_reqs = value

    resource_group_reqs = property(get_resource_group_reqs, set_resource_group_reqs)

    def add_resource_group_reqs(self, *resource_group_reqs):
        for obj in resource_group_reqs:
            obj._resource_group = self
            self._resource_group_reqs.append(obj)

    def remove_resource_group_reqs(self, *resource_group_reqs):
        for obj in resource_group_reqs:
            obj._resource_group = None
            self._resource_group_reqs.remove(obj)
    # >>> resource_group_reqs


    def __str__(self):
        """ Returns a string representation of the ResourceGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< resource_group.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ResourceGroup.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ResourceGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.registered_resources:
            s += '%s<%s:ResourceGroup.registered_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resource_group_reqs:
            s += '%s<%s:ResourceGroup.resource_group_reqs rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ResourceGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> resource_group.serialize


class PassThroughBill(Document):
    """ Pass Through Bill is used for: 1)Two sided charge transactions with or without ISO involvement (hence the ?pass thru?) 2) Specific direct charges or payments that are calculated outside or provided directly to settlements 3) Specific charge bill determinants that are externally supplied and used in charge calculations
    """
    # <<< pass_through_bill
    # @generated
    def __init__(self, transaction_date='', transaction_type='', bill_run_type='', time_zone='', tax_amount=0.0, effective_date='', trade_date='', bill_start='', price=0.0, sold_to='', previous_start='', provided_by='', product_code='', is_profiled=False, previous_end='', service_start='', paid_to='', bill_end='', amount=0.0, service_end='', billed_to='', is_disputed=False, market_statement_line_item=None, user_attributes=None, charge_profiles=None, quantity=None, **kw_args):
        """ Initialises a new 'PassThroughBill' instance.
        """
        # The date the transaction occurs. 
        self.transaction_date = transaction_date

        # The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant 
        self.transaction_type = transaction_type

        # The settlement run type, for example: prelim, final, and rerun. 
        self.bill_run_type = bill_run_type

        # The time zone code 
        self.time_zone = time_zone

        # The tax on services taken. 
        self.tax_amount = tax_amount

        # The effective date of the transaction 
        self.effective_date = effective_date

        # The trade date 
        self.trade_date = trade_date

        # Bill period start date 
        self.bill_start = bill_start

        # The price of product/service. 
        self.price = price

        # The company to which the PTB transaction is sold. 
        self.sold_to = sold_to

        # The previous bill period start date 
        self.previous_start = previous_start

        # The company by which the PTB transaction service is provided. 
        self.provided_by = provided_by

        # The product identifier for determining the charge type of the transaction. 
        self.product_code = product_code

        # A flag indicating whether there is a profile data associated with the PTB. 
        self.is_profiled = is_profiled

        # The previous bill period end date 
        self.previous_end = previous_end

        # The start date of service provided, if periodic. 
        self.service_start = service_start

        # The company to which the PTB transaction is paid. 
        self.paid_to = paid_to

        # Bill period end date 
        self.bill_end = bill_end

        # The charge amount of the product/service. 
        self.amount = amount

        # The end date of service provided, if periodic. 
        self.service_end = service_end

        # The company to which the PTB transaction is billed. 
        self.billed_to = billed_to

        # Disputed transaction indicator 
        self.is_disputed = is_disputed


        self._market_statement_line_item = None
        self.market_statement_line_item = market_statement_line_item

        self._user_attributes = []
        if user_attributes is not None:
            self.user_attributes = user_attributes
        else:
            self.user_attributes = []

        self._charge_profiles = []
        if charge_profiles is not None:
            self.charge_profiles = charge_profiles
        else:
            self.charge_profiles = []

        self.quantity = quantity


        super(PassThroughBill, self).__init__(**kw_args)
    # >>> pass_through_bill

    # <<< market_statement_line_item
    # @generated
    def get_market_statement_line_item(self):
        """ 
        """
        return self._market_statement_line_item

    def set_market_statement_line_item(self, value):
        if self._market_statement_line_item is not None:
            self._market_statement_line_item._pass_through_bill = None

        self._market_statement_line_item = value
        if self._market_statement_line_item is not None:
            self._market_statement_line_item._pass_through_bill = self

    market_statement_line_item = property(get_market_statement_line_item, set_market_statement_line_item)
    # >>> market_statement_line_item

    # <<< user_attributes
    # @generated
    def get_user_attributes(self):
        """ 
        """
        return self._user_attributes

    def set_user_attributes(self, value):
        for p in self._user_attributes:
            filtered = [q for q in p.pass_through_bills if q != self]
            self._user_attributes._pass_through_bills = filtered
        for r in value:
            if self not in r._pass_through_bills:
                r._pass_through_bills.append(self)
        self._user_attributes = value

    user_attributes = property(get_user_attributes, set_user_attributes)

    def add_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self not in obj._pass_through_bills:
                obj._pass_through_bills.append(self)
            self._user_attributes.append(obj)

    def remove_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self in obj._pass_through_bills:
                obj._pass_through_bills.remove(self)
            self._user_attributes.remove(obj)
    # >>> user_attributes

    # <<< charge_profiles
    # @generated
    def get_charge_profiles(self):
        """ 
        """
        return self._charge_profiles

    def set_charge_profiles(self, value):
        for x in self._charge_profiles:
            x._pass_trough_bill = None
        for y in value:
            y._pass_trough_bill = self
        self._charge_profiles = value

    charge_profiles = property(get_charge_profiles, set_charge_profiles)

    def add_charge_profiles(self, *charge_profiles):
        for obj in charge_profiles:
            obj._pass_trough_bill = self
            self._charge_profiles.append(obj)

    def remove_charge_profiles(self, *charge_profiles):
        for obj in charge_profiles:
            obj._pass_trough_bill = None
            self._charge_profiles.remove(obj)
    # >>> charge_profiles

    # <<< quantity
    # @generated
    # The product quantity.
    quantity = None
    # >>> quantity


    def __str__(self):
        """ Returns a string representation of the PassThroughBill.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pass_through_bill.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PassThroughBill.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PassThroughBill", self.uri)
        if format:
            indent += ' ' * depth

        if self.market_statement_line_item is not None:
            s += '%s<%s:PassThroughBill.market_statement_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market_statement_line_item.uri)
        for obj in self.user_attributes:
            s += '%s<%s:PassThroughBill.user_attributes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.charge_profiles:
            s += '%s<%s:PassThroughBill.charge_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.quantity is not None:
            s += '%s<%s:PassThroughBill.quantity rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.quantity.uri)
        s += '%s<%s:PassThroughBill.transaction_date>%s</%s:PassThroughBill.transaction_date>' % \
            (indent, ns_prefix, self.transaction_date, ns_prefix)
        s += '%s<%s:PassThroughBill.transaction_type>%s</%s:PassThroughBill.transaction_type>' % \
            (indent, ns_prefix, self.transaction_type, ns_prefix)
        s += '%s<%s:PassThroughBill.bill_run_type>%s</%s:PassThroughBill.bill_run_type>' % \
            (indent, ns_prefix, self.bill_run_type, ns_prefix)
        s += '%s<%s:PassThroughBill.time_zone>%s</%s:PassThroughBill.time_zone>' % \
            (indent, ns_prefix, self.time_zone, ns_prefix)
        s += '%s<%s:PassThroughBill.tax_amount>%s</%s:PassThroughBill.tax_amount>' % \
            (indent, ns_prefix, self.tax_amount, ns_prefix)
        s += '%s<%s:PassThroughBill.effective_date>%s</%s:PassThroughBill.effective_date>' % \
            (indent, ns_prefix, self.effective_date, ns_prefix)
        s += '%s<%s:PassThroughBill.trade_date>%s</%s:PassThroughBill.trade_date>' % \
            (indent, ns_prefix, self.trade_date, ns_prefix)
        s += '%s<%s:PassThroughBill.bill_start>%s</%s:PassThroughBill.bill_start>' % \
            (indent, ns_prefix, self.bill_start, ns_prefix)
        s += '%s<%s:PassThroughBill.price>%s</%s:PassThroughBill.price>' % \
            (indent, ns_prefix, self.price, ns_prefix)
        s += '%s<%s:PassThroughBill.sold_to>%s</%s:PassThroughBill.sold_to>' % \
            (indent, ns_prefix, self.sold_to, ns_prefix)
        s += '%s<%s:PassThroughBill.previous_start>%s</%s:PassThroughBill.previous_start>' % \
            (indent, ns_prefix, self.previous_start, ns_prefix)
        s += '%s<%s:PassThroughBill.provided_by>%s</%s:PassThroughBill.provided_by>' % \
            (indent, ns_prefix, self.provided_by, ns_prefix)
        s += '%s<%s:PassThroughBill.product_code>%s</%s:PassThroughBill.product_code>' % \
            (indent, ns_prefix, self.product_code, ns_prefix)
        s += '%s<%s:PassThroughBill.is_profiled>%s</%s:PassThroughBill.is_profiled>' % \
            (indent, ns_prefix, self.is_profiled, ns_prefix)
        s += '%s<%s:PassThroughBill.previous_end>%s</%s:PassThroughBill.previous_end>' % \
            (indent, ns_prefix, self.previous_end, ns_prefix)
        s += '%s<%s:PassThroughBill.service_start>%s</%s:PassThroughBill.service_start>' % \
            (indent, ns_prefix, self.service_start, ns_prefix)
        s += '%s<%s:PassThroughBill.paid_to>%s</%s:PassThroughBill.paid_to>' % \
            (indent, ns_prefix, self.paid_to, ns_prefix)
        s += '%s<%s:PassThroughBill.bill_end>%s</%s:PassThroughBill.bill_end>' % \
            (indent, ns_prefix, self.bill_end, ns_prefix)
        s += '%s<%s:PassThroughBill.amount>%s</%s:PassThroughBill.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:PassThroughBill.service_end>%s</%s:PassThroughBill.service_end>' % \
            (indent, ns_prefix, self.service_end, ns_prefix)
        s += '%s<%s:PassThroughBill.billed_to>%s</%s:PassThroughBill.billed_to>' % \
            (indent, ns_prefix, self.billed_to, ns_prefix)
        s += '%s<%s:PassThroughBill.is_disputed>%s</%s:PassThroughBill.is_disputed>' % \
            (indent, ns_prefix, self.is_disputed, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PassThroughBill")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pass_through_bill.serialize


class SchedulingCoordinator(ErpOrganisation):
    """ In certain ISO/RTO operations, market participants are represented by Scheduling Coordinators (SCs) that are registered with the ISO/RTO. One participant can register multiple SCs with the ISO/RTO.  Many participants can do business with the ISO/RTO using a single SC. Each generator resource can only be scheduled by one SC. One SC can schedule multiple generators. A load scheduling point can be used by multiple SCs. Each SC can schedule load at multiple scheduling points. Each SC can have more than one load schedule at any load scheduling point as long as each load schedule at the same load scheduling point has a separate resource ID and settlement-quality meter. An inter-tie scheduling point can be used by multiple SCs. Each SC can schedule interchange at multiple inter-tie scheduling points. An SC can have multiple interchange schedules at the same inter-tie scheduling point by assigning a unique interchange identifier to each interchange schedule.
    """
    pass
    # <<< scheduling_coordinator
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'SchedulingCoordinator' instance.
        """


        super(SchedulingCoordinator, self).__init__(**kw_args)
    # >>> scheduling_coordinator


    def __str__(self):
        """ Returns a string representation of the SchedulingCoordinator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< scheduling_coordinator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SchedulingCoordinator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SchedulingCoordinator", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SchedulingCoordinator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> scheduling_coordinator.serialize


class RampRateCurve(Curve):
    """ Ramp rate as a function of resource MW output
    """
    # <<< ramp_rate_curve
    # @generated
    def __init__(self, ramp_rate_type='', generating_unit=None, **kw_args):
        """ Initialises a new 'RampRateCurve' instance.
        """
        # How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource) 
        self.ramp_rate_type = ramp_rate_type


        self._generating_unit = []
        if generating_unit is not None:
            self.generating_unit = generating_unit
        else:
            self.generating_unit = []


        super(RampRateCurve, self).__init__(**kw_args)
    # >>> ramp_rate_curve

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ 
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        for p in self._generating_unit:
            filtered = [q for q in p.ramp_rate_curves if q != self]
            self._generating_unit._ramp_rate_curves = filtered
        for r in value:
            if self not in r._ramp_rate_curves:
                r._ramp_rate_curves.append(self)
        self._generating_unit = value

    generating_unit = property(get_generating_unit, set_generating_unit)

    def add_generating_unit(self, *generating_unit):
        for obj in generating_unit:
            if self not in obj._ramp_rate_curves:
                obj._ramp_rate_curves.append(self)
            self._generating_unit.append(obj)

    def remove_generating_unit(self, *generating_unit):
        for obj in generating_unit:
            if self in obj._ramp_rate_curves:
                obj._ramp_rate_curves.remove(self)
            self._generating_unit.remove(obj)
    # >>> generating_unit


    def __str__(self):
        """ Returns a string representation of the RampRateCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ramp_rate_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RampRateCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RampRateCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.generating_unit:
            s += '%s<%s:RampRateCurve.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RampRateCurve.ramp_rate_type>%s</%s:RampRateCurve.ramp_rate_type>' % \
            (indent, ns_prefix, self.ramp_rate_type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RampRateCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ramp_rate_curve.serialize


class ProductBid(IdentifiedObject):
    """ Component of a bid that pertains to one market product.
    """
    # <<< product_bid
    # @generated
    def __init__(self, bid=None, market_product=None, bid_price_curve=None, product_bid_clearing=None, **kw_args):
        """ Initialises a new 'ProductBid' instance.
        """

        self._bid = None
        self.bid = bid

        self._market_product = None
        self.market_product = market_product

        self._bid_price_curve = None
        self.bid_price_curve = bid_price_curve

        self._product_bid_clearing = None
        self.product_bid_clearing = product_bid_clearing


        super(ProductBid, self).__init__(**kw_args)
    # >>> product_bid

    # <<< bid
    # @generated
    def get_bid(self):
        """ A bid comprises one or more product bids of market products
        """
        return self._bid

    def set_bid(self, value):
        if self._bid is not None:
            filtered = [x for x in self.bid.product_bids if x != self]
            self._bid._product_bids = filtered

        self._bid = value
        if self._bid is not None:
            self._bid._product_bids.append(self)

    bid = property(get_bid, set_bid)
    # >>> bid

    # <<< market_product
    # @generated
    def get_market_product(self):
        """ 
        """
        return self._market_product

    def set_market_product(self, value):
        if self._market_product is not None:
            filtered = [x for x in self.market_product.product_bids if x != self]
            self._market_product._product_bids = filtered

        self._market_product = value
        if self._market_product is not None:
            self._market_product._product_bids.append(self)

    market_product = property(get_market_product, set_market_product)
    # >>> market_product

    # <<< bid_price_curve
    # @generated
    def get_bid_price_curve(self):
        """ 
        """
        return self._bid_price_curve

    def set_bid_price_curve(self, value):
        if self._bid_price_curve is not None:
            filtered = [x for x in self.bid_price_curve.product_bids if x != self]
            self._bid_price_curve._product_bids = filtered

        self._bid_price_curve = value
        if self._bid_price_curve is not None:
            self._bid_price_curve._product_bids.append(self)

    bid_price_curve = property(get_bid_price_curve, set_bid_price_curve)
    # >>> bid_price_curve

    # <<< product_bid_clearing
    # @generated
    def get_product_bid_clearing(self):
        """ 
        """
        return self._product_bid_clearing

    def set_product_bid_clearing(self, value):
        if self._product_bid_clearing is not None:
            filtered = [x for x in self.product_bid_clearing.product_bids if x != self]
            self._product_bid_clearing._product_bids = filtered

        self._product_bid_clearing = value
        if self._product_bid_clearing is not None:
            self._product_bid_clearing._product_bids.append(self)

    product_bid_clearing = property(get_product_bid_clearing, set_product_bid_clearing)
    # >>> product_bid_clearing


    def __str__(self):
        """ Returns a string representation of the ProductBid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< product_bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProductBid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProductBid", self.uri)
        if format:
            indent += ' ' * depth

        if self.bid is not None:
            s += '%s<%s:ProductBid.bid rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid.uri)
        if self.market_product is not None:
            s += '%s<%s:ProductBid.market_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market_product.uri)
        if self.bid_price_curve is not None:
            s += '%s<%s:ProductBid.bid_price_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_price_curve.uri)
        if self.product_bid_clearing is not None:
            s += '%s<%s:ProductBid.product_bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.product_bid_clearing.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProductBid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> product_bid.serialize


class DefaultConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) applied as a default value if no specific constraint limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """
    # <<< default_constraint_limit
    # @generated
    def __init__(self, security_constraint_sum=None, **kw_args):
        """ Initialises a new 'DefaultConstraintLimit' instance.
        """

        self._security_constraint_sum = None
        self.security_constraint_sum = security_constraint_sum


        super(DefaultConstraintLimit, self).__init__(**kw_args)
    # >>> default_constraint_limit

    # <<< security_constraint_sum
    # @generated
    def get_security_constraint_sum(self):
        """ 
        """
        return self._security_constraint_sum

    def set_security_constraint_sum(self, value):
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._default_constraint_limit = None

        self._security_constraint_sum = value
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._default_constraint_limit = self

    security_constraint_sum = property(get_security_constraint_sum, set_security_constraint_sum)
    # >>> security_constraint_sum


    def __str__(self):
        """ Returns a string representation of the DefaultConstraintLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< default_constraint_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DefaultConstraintLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DefaultConstraintLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.security_constraint_sum is not None:
            s += '%s<%s:DefaultConstraintLimit.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DefaultConstraintLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> default_constraint_limit.serialize


class ChargeProfile(Profile):
    """ A type of profile for financial charges
    """
    # <<< charge_profile
    # @generated
    def __init__(self, unit_of_measure='', frequency='', number_interval=0, type='', bill_determinant=None, pass_trough_bill=None, charge_profile_data=None, **kw_args):
        """ Initialises a new 'ChargeProfile' instance.
        """
        # The unit of measure applied to the value attribute of the profile data. 
        self.unit_of_measure = unit_of_measure

        # The calculation frequency, daily or monthly. 
        self.frequency = frequency

        # The number of intervals in the profile data. 
        self.number_interval = number_interval

        # The type of profile.  It could be amount, price, or quantity. 
        self.type = type


        self._bill_determinant = None
        self.bill_determinant = bill_determinant

        self._pass_trough_bill = None
        self.pass_trough_bill = pass_trough_bill

        self._charge_profile_data = []
        if charge_profile_data is not None:
            self.charge_profile_data = charge_profile_data
        else:
            self.charge_profile_data = []


        super(ChargeProfile, self).__init__(**kw_args)
    # >>> charge_profile

    # <<< bill_determinant
    # @generated
    def get_bill_determinant(self):
        """ 
        """
        return self._bill_determinant

    def set_bill_determinant(self, value):
        if self._bill_determinant is not None:
            self._bill_determinant._charge_profile = None

        self._bill_determinant = value
        if self._bill_determinant is not None:
            self._bill_determinant._charge_profile = self

    bill_determinant = property(get_bill_determinant, set_bill_determinant)
    # >>> bill_determinant

    # <<< pass_trough_bill
    # @generated
    def get_pass_trough_bill(self):
        """ 
        """
        return self._pass_trough_bill

    def set_pass_trough_bill(self, value):
        if self._pass_trough_bill is not None:
            filtered = [x for x in self.pass_trough_bill.charge_profiles if x != self]
            self._pass_trough_bill._charge_profiles = filtered

        self._pass_trough_bill = value
        if self._pass_trough_bill is not None:
            self._pass_trough_bill._charge_profiles.append(self)

    pass_trough_bill = property(get_pass_trough_bill, set_pass_trough_bill)
    # >>> pass_trough_bill

    # <<< charge_profile_data
    # @generated
    def get_charge_profile_data(self):
        """ 
        """
        return self._charge_profile_data

    def set_charge_profile_data(self, value):
        for x in self._charge_profile_data:
            x._charge_profile = None
        for y in value:
            y._charge_profile = self
        self._charge_profile_data = value

    charge_profile_data = property(get_charge_profile_data, set_charge_profile_data)

    def add_charge_profile_data(self, *charge_profile_data):
        for obj in charge_profile_data:
            obj._charge_profile = self
            self._charge_profile_data.append(obj)

    def remove_charge_profile_data(self, *charge_profile_data):
        for obj in charge_profile_data:
            obj._charge_profile = None
            self._charge_profile_data.remove(obj)
    # >>> charge_profile_data


    def __str__(self):
        """ Returns a string representation of the ChargeProfile.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< charge_profile.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ChargeProfile.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ChargeProfile", self.uri)
        if format:
            indent += ' ' * depth

        if self.bill_determinant is not None:
            s += '%s<%s:ChargeProfile.bill_determinant rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bill_determinant.uri)
        if self.pass_trough_bill is not None:
            s += '%s<%s:ChargeProfile.pass_trough_bill rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pass_trough_bill.uri)
        for obj in self.charge_profile_data:
            s += '%s<%s:ChargeProfile.charge_profile_data rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ChargeProfile.unit_of_measure>%s</%s:ChargeProfile.unit_of_measure>' % \
            (indent, ns_prefix, self.unit_of_measure, ns_prefix)
        s += '%s<%s:ChargeProfile.frequency>%s</%s:ChargeProfile.frequency>' % \
            (indent, ns_prefix, self.frequency, ns_prefix)
        s += '%s<%s:ChargeProfile.number_interval>%s</%s:ChargeProfile.number_interval>' % \
            (indent, ns_prefix, self.number_interval, ns_prefix)
        s += '%s<%s:ChargeProfile.type>%s</%s:ChargeProfile.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ChargeProfile")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> charge_profile.serialize


class MarketStatementLineItem(IdentifiedObject):
    """ An individual line item on a statement.
    """
    # <<< market_statement_line_item
    # @generated
    def __init__(self, previous_isoamount=0.0, interval_number='', net_quantity=0.0, interval_date='', previous_amount=0.0, net_isoamount=0.0, net_price=0.0, current_amount=0.0, net_isoquantity=0.0, previous_quantity=0.0, quantity_uom='', previsou_price=0.0, previous_isoquantity=0.0, current_isoamount=0.0, current_quantity=0.0, current_price=0.0, net_amount=0.0, current_isoquantity=0.0, market_statement=None, pass_through_bill=None, container_market_statement_line_item=None, component_market_statement_line_item=None, user_attributes=None, **kw_args):
        """ Initialises a new 'MarketStatementLineItem' instance.
        """
        # Previous ISO settlement amount. 
        self.previous_isoamount = previous_isoamount

        # The number of intervals. 
        self.interval_number = interval_number

        # Net settlement quantity, subject to the UOM. 
        self.net_quantity = net_quantity

        # The date of which the settlement is run. 
        self.interval_date = interval_date

        # Previous settlement amount. 
        self.previous_amount = previous_amount

        # Net ISO settlement amount. 
        self.net_isoamount = net_isoamount

        # Net settlement price. 
        self.net_price = net_price

        # Current settlement amount. 
        self.current_amount = current_amount

        # Net ISO settlement quantity. 
        self.net_isoquantity = net_isoquantity

        # Previous settlement quantity, subject to the UOM. 
        self.previous_quantity = previous_quantity

        # The unit of measure for the quantity element of the line item. 
        self.quantity_uom = quantity_uom

        # Previous settlement price. 
        self.previsou_price = previsou_price

        # Previous ISO settlement quantity. 
        self.previous_isoquantity = previous_isoquantity

        # Current ISO settlement amount. 
        self.current_isoamount = current_isoamount

        # Current settlement quantity, subject to the UOM. 
        self.current_quantity = current_quantity

        # Current settlement price. 
        self.current_price = current_price

        # Net settlement amount. 
        self.net_amount = net_amount

        # Current ISO settlement quantity. 
        self.current_isoquantity = current_isoquantity


        self._market_statement = None
        self.market_statement = market_statement

        self._pass_through_bill = None
        self.pass_through_bill = pass_through_bill

        self._container_market_statement_line_item = None
        self.container_market_statement_line_item = container_market_statement_line_item

        self._component_market_statement_line_item = []
        if component_market_statement_line_item is not None:
            self.component_market_statement_line_item = component_market_statement_line_item
        else:
            self.component_market_statement_line_item = []

        self._user_attributes = []
        if user_attributes is not None:
            self.user_attributes = user_attributes
        else:
            self.user_attributes = []


        super(MarketStatementLineItem, self).__init__(**kw_args)
    # >>> market_statement_line_item

    # <<< market_statement
    # @generated
    def get_market_statement(self):
        """ 
        """
        return self._market_statement

    def set_market_statement(self, value):
        if self._market_statement is not None:
            filtered = [x for x in self.market_statement.market_statement_line_item if x != self]
            self._market_statement._market_statement_line_item = filtered

        self._market_statement = value
        if self._market_statement is not None:
            self._market_statement._market_statement_line_item.append(self)

    market_statement = property(get_market_statement, set_market_statement)
    # >>> market_statement

    # <<< pass_through_bill
    # @generated
    def get_pass_through_bill(self):
        """ 
        """
        return self._pass_through_bill

    def set_pass_through_bill(self, value):
        if self._pass_through_bill is not None:
            self._pass_through_bill._market_statement_line_item = None

        self._pass_through_bill = value
        if self._pass_through_bill is not None:
            self._pass_through_bill._market_statement_line_item = self

    pass_through_bill = property(get_pass_through_bill, set_pass_through_bill)
    # >>> pass_through_bill

    # <<< container_market_statement_line_item
    # @generated
    def get_container_market_statement_line_item(self):
        """ 
        """
        return self._container_market_statement_line_item

    def set_container_market_statement_line_item(self, value):
        if self._container_market_statement_line_item is not None:
            filtered = [x for x in self.container_market_statement_line_item.component_market_statement_line_item if x != self]
            self._container_market_statement_line_item._component_market_statement_line_item = filtered

        self._container_market_statement_line_item = value
        if self._container_market_statement_line_item is not None:
            self._container_market_statement_line_item._component_market_statement_line_item.append(self)

    container_market_statement_line_item = property(get_container_market_statement_line_item, set_container_market_statement_line_item)
    # >>> container_market_statement_line_item

    # <<< component_market_statement_line_item
    # @generated
    def get_component_market_statement_line_item(self):
        """ 
        """
        return self._component_market_statement_line_item

    def set_component_market_statement_line_item(self, value):
        for x in self._component_market_statement_line_item:
            x._container_market_statement_line_item = None
        for y in value:
            y._container_market_statement_line_item = self
        self._component_market_statement_line_item = value

    component_market_statement_line_item = property(get_component_market_statement_line_item, set_component_market_statement_line_item)

    def add_component_market_statement_line_item(self, *component_market_statement_line_item):
        for obj in component_market_statement_line_item:
            obj._container_market_statement_line_item = self
            self._component_market_statement_line_item.append(obj)

    def remove_component_market_statement_line_item(self, *component_market_statement_line_item):
        for obj in component_market_statement_line_item:
            obj._container_market_statement_line_item = None
            self._component_market_statement_line_item.remove(obj)
    # >>> component_market_statement_line_item

    # <<< user_attributes
    # @generated
    def get_user_attributes(self):
        """ 
        """
        return self._user_attributes

    def set_user_attributes(self, value):
        for p in self._user_attributes:
            filtered = [q for q in p.erp_statement_line_items if q != self]
            self._user_attributes._erp_statement_line_items = filtered
        for r in value:
            if self not in r._erp_statement_line_items:
                r._erp_statement_line_items.append(self)
        self._user_attributes = value

    user_attributes = property(get_user_attributes, set_user_attributes)

    def add_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self not in obj._erp_statement_line_items:
                obj._erp_statement_line_items.append(self)
            self._user_attributes.append(obj)

    def remove_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self in obj._erp_statement_line_items:
                obj._erp_statement_line_items.remove(self)
            self._user_attributes.remove(obj)
    # >>> user_attributes


    def __str__(self):
        """ Returns a string representation of the MarketStatementLineItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_statement_line_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketStatementLineItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketStatementLineItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.market_statement is not None:
            s += '%s<%s:MarketStatementLineItem.market_statement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market_statement.uri)
        if self.pass_through_bill is not None:
            s += '%s<%s:MarketStatementLineItem.pass_through_bill rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pass_through_bill.uri)
        if self.container_market_statement_line_item is not None:
            s += '%s<%s:MarketStatementLineItem.container_market_statement_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.container_market_statement_line_item.uri)
        for obj in self.component_market_statement_line_item:
            s += '%s<%s:MarketStatementLineItem.component_market_statement_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.user_attributes:
            s += '%s<%s:MarketStatementLineItem.user_attributes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:MarketStatementLineItem.previous_isoamount>%s</%s:MarketStatementLineItem.previous_isoamount>' % \
            (indent, ns_prefix, self.previous_isoamount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.interval_number>%s</%s:MarketStatementLineItem.interval_number>' % \
            (indent, ns_prefix, self.interval_number, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.net_quantity>%s</%s:MarketStatementLineItem.net_quantity>' % \
            (indent, ns_prefix, self.net_quantity, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.interval_date>%s</%s:MarketStatementLineItem.interval_date>' % \
            (indent, ns_prefix, self.interval_date, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.previous_amount>%s</%s:MarketStatementLineItem.previous_amount>' % \
            (indent, ns_prefix, self.previous_amount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.net_isoamount>%s</%s:MarketStatementLineItem.net_isoamount>' % \
            (indent, ns_prefix, self.net_isoamount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.net_price>%s</%s:MarketStatementLineItem.net_price>' % \
            (indent, ns_prefix, self.net_price, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.current_amount>%s</%s:MarketStatementLineItem.current_amount>' % \
            (indent, ns_prefix, self.current_amount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.net_isoquantity>%s</%s:MarketStatementLineItem.net_isoquantity>' % \
            (indent, ns_prefix, self.net_isoquantity, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.previous_quantity>%s</%s:MarketStatementLineItem.previous_quantity>' % \
            (indent, ns_prefix, self.previous_quantity, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.quantity_uom>%s</%s:MarketStatementLineItem.quantity_uom>' % \
            (indent, ns_prefix, self.quantity_uom, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.previsou_price>%s</%s:MarketStatementLineItem.previsou_price>' % \
            (indent, ns_prefix, self.previsou_price, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.previous_isoquantity>%s</%s:MarketStatementLineItem.previous_isoquantity>' % \
            (indent, ns_prefix, self.previous_isoquantity, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.current_isoamount>%s</%s:MarketStatementLineItem.current_isoamount>' % \
            (indent, ns_prefix, self.current_isoamount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.current_quantity>%s</%s:MarketStatementLineItem.current_quantity>' % \
            (indent, ns_prefix, self.current_quantity, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.current_price>%s</%s:MarketStatementLineItem.current_price>' % \
            (indent, ns_prefix, self.current_price, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.net_amount>%s</%s:MarketStatementLineItem.net_amount>' % \
            (indent, ns_prefix, self.net_amount, ns_prefix)
        s += '%s<%s:MarketStatementLineItem.current_isoquantity>%s</%s:MarketStatementLineItem.current_isoquantity>' % \
            (indent, ns_prefix, self.current_isoquantity, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketStatementLineItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_statement_line_item.serialize


class RegisteredResource(IdentifiedObject):
    """ A resource that is registered through the RTO participant registration system. Examples include generating unit, customer meter, and a non-physical generator or load.
    """
    # <<< registered_resource
    # @generated
    def __init__(self, rto_id='', meters=None, markets=None, resource_groups=None, market_products=None, pnode=None, organisation=None, **kw_args):
        """ Initialises a new 'RegisteredResource' instance.
        """
        # Unique name obtained via RTO registration 
        self.rto_id = rto_id


        self._meters = []
        if meters is not None:
            self.meters = meters
        else:
            self.meters = []

        self._markets = []
        if markets is not None:
            self.markets = markets
        else:
            self.markets = []

        self._resource_groups = []
        if resource_groups is not None:
            self.resource_groups = resource_groups
        else:
            self.resource_groups = []

        self._market_products = []
        if market_products is not None:
            self.market_products = market_products
        else:
            self.market_products = []

        self._pnode = None
        self.pnode = pnode

        self._organisation = None
        self.organisation = organisation


        super(RegisteredResource, self).__init__(**kw_args)
    # >>> registered_resource

    # <<< meters
    # @generated
    def get_meters(self):
        """ 
        """
        return self._meters

    def set_meters(self, value):
        for x in self._meters:
            x._registered_resource = None
        for y in value:
            y._registered_resource = self
        self._meters = value

    meters = property(get_meters, set_meters)

    def add_meters(self, *meters):
        for obj in meters:
            obj._registered_resource = self
            self._meters.append(obj)

    def remove_meters(self, *meters):
        for obj in meters:
            obj._registered_resource = None
            self._meters.remove(obj)
    # >>> meters

    # <<< markets
    # @generated
    def get_markets(self):
        """ 
        """
        return self._markets

    def set_markets(self, value):
        for p in self._markets:
            filtered = [q for q in p.registered_resources if q != self]
            self._markets._registered_resources = filtered
        for r in value:
            if self not in r._registered_resources:
                r._registered_resources.append(self)
        self._markets = value

    markets = property(get_markets, set_markets)

    def add_markets(self, *markets):
        for obj in markets:
            if self not in obj._registered_resources:
                obj._registered_resources.append(self)
            self._markets.append(obj)

    def remove_markets(self, *markets):
        for obj in markets:
            if self in obj._registered_resources:
                obj._registered_resources.remove(self)
            self._markets.remove(obj)
    # >>> markets

    # <<< resource_groups
    # @generated
    def get_resource_groups(self):
        """ 
        """
        return self._resource_groups

    def set_resource_groups(self, value):
        for p in self._resource_groups:
            filtered = [q for q in p.registered_resources if q != self]
            self._resource_groups._registered_resources = filtered
        for r in value:
            if self not in r._registered_resources:
                r._registered_resources.append(self)
        self._resource_groups = value

    resource_groups = property(get_resource_groups, set_resource_groups)

    def add_resource_groups(self, *resource_groups):
        for obj in resource_groups:
            if self not in obj._registered_resources:
                obj._registered_resources.append(self)
            self._resource_groups.append(obj)

    def remove_resource_groups(self, *resource_groups):
        for obj in resource_groups:
            if self in obj._registered_resources:
                obj._registered_resources.remove(self)
            self._resource_groups.remove(obj)
    # >>> resource_groups

    # <<< market_products
    # @generated
    def get_market_products(self):
        """ A registered resource is eligible to bid market products
        """
        return self._market_products

    def set_market_products(self, value):
        for p in self._market_products:
            filtered = [q for q in p.registered_resources if q != self]
            self._market_products._registered_resources = filtered
        for r in value:
            if self not in r._registered_resources:
                r._registered_resources.append(self)
        self._market_products = value

    market_products = property(get_market_products, set_market_products)

    def add_market_products(self, *market_products):
        for obj in market_products:
            if self not in obj._registered_resources:
                obj._registered_resources.append(self)
            self._market_products.append(obj)

    def remove_market_products(self, *market_products):
        for obj in market_products:
            if self in obj._registered_resources:
                obj._registered_resources.remove(self)
            self._market_products.remove(obj)
    # >>> market_products

    # <<< pnode
    # @generated
    def get_pnode(self):
        """ A registered resource injects power at one or more connectivity nodes related to a pnode
        """
        return self._pnode

    def set_pnode(self, value):
        if self._pnode is not None:
            filtered = [x for x in self.pnode.registered_resources if x != self]
            self._pnode._registered_resources = filtered

        self._pnode = value
        if self._pnode is not None:
            self._pnode._registered_resources.append(self)

    pnode = property(get_pnode, set_pnode)
    # >>> pnode

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ 
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.registered_resources if x != self]
            self._organisation._registered_resources = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._registered_resources.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation


    def __str__(self):
        """ Returns a string representation of the RegisteredResource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< registered_resource.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegisteredResource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegisteredResource", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.meters:
            s += '%s<%s:RegisteredResource.meters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.markets:
            s += '%s<%s:RegisteredResource.markets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resource_groups:
            s += '%s<%s:RegisteredResource.resource_groups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.market_products:
            s += '%s<%s:RegisteredResource.market_products rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:RegisteredResource.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.organisation is not None:
            s += '%s<%s:RegisteredResource.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        s += '%s<%s:RegisteredResource.rto_id>%s</%s:RegisteredResource.rto_id>' % \
            (indent, ns_prefix, self.rto_id, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegisteredResource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> registered_resource.serialize


class Market(IdentifiedObject):
    """ Market (e.g., DAM, HAM)  zzMarket operation control parameters.
    """
    # <<< market
    # @generated
    def __init__(self, ramp_interval_non_spin_res=0.0, local_time_zone='', ramp_interval_energy=0.0, type='', time_interval_length=0.0, ramp_interval_spin_res=0.0, dst=False, ramp_interval_reg=0.0, end='', start='', bids=None, market_products=None, registered_resources=None, settlements=None, market_factors=None, rto=None, **kw_args):
        """ Initialises a new 'Market' instance.
        """
        # Ramping time interval for non-spinning reserve. 
        self.ramp_interval_non_spin_res = ramp_interval_non_spin_res

        # Local time zone. 
        self.local_time_zone = local_time_zone

        # Ramping time interval for energy. 
        self.ramp_interval_energy = ramp_interval_energy

        # The type of a market. 
        self.type = type

        # Trading time interval length. 
        self.time_interval_length = time_interval_length

        # Ramping time interval for spinning reserve. 
        self.ramp_interval_spin_res = ramp_interval_spin_res

        # True if daylight savings time (DST) is in effect. 
        self.dst = dst

        # Ramping time interval for regulation. 
        self.ramp_interval_reg = ramp_interval_reg

        # Market end time. 
        self.end = end

        # Market start time. 
        self.start = start


        self._bids = []
        if bids is not None:
            self.bids = bids
        else:
            self.bids = []

        self._market_products = []
        if market_products is not None:
            self.market_products = market_products
        else:
            self.market_products = []

        self._registered_resources = []
        if registered_resources is not None:
            self.registered_resources = registered_resources
        else:
            self.registered_resources = []

        self._settlements = []
        if settlements is not None:
            self.settlements = settlements
        else:
            self.settlements = []

        self._market_factors = []
        if market_factors is not None:
            self.market_factors = market_factors
        else:
            self.market_factors = []

        self._rto = None
        self.rto = rto


        super(Market, self).__init__(**kw_args)
    # >>> market

    # <<< bids
    # @generated
    def get_bids(self):
        """ 
        """
        return self._bids

    def set_bids(self, value):
        for x in self._bids:
            x._market = None
        for y in value:
            y._market = self
        self._bids = value

    bids = property(get_bids, set_bids)

    def add_bids(self, *bids):
        for obj in bids:
            obj._market = self
            self._bids.append(obj)

    def remove_bids(self, *bids):
        for obj in bids:
            obj._market = None
            self._bids.remove(obj)
    # >>> bids

    # <<< market_products
    # @generated
    def get_market_products(self):
        """ 
        """
        return self._market_products

    def set_market_products(self, value):
        for x in self._market_products:
            x._market = None
        for y in value:
            y._market = self
        self._market_products = value

    market_products = property(get_market_products, set_market_products)

    def add_market_products(self, *market_products):
        for obj in market_products:
            obj._market = self
            self._market_products.append(obj)

    def remove_market_products(self, *market_products):
        for obj in market_products:
            obj._market = None
            self._market_products.remove(obj)
    # >>> market_products

    # <<< registered_resources
    # @generated
    def get_registered_resources(self):
        """ 
        """
        return self._registered_resources

    def set_registered_resources(self, value):
        for p in self._registered_resources:
            filtered = [q for q in p.markets if q != self]
            self._registered_resources._markets = filtered
        for r in value:
            if self not in r._markets:
                r._markets.append(self)
        self._registered_resources = value

    registered_resources = property(get_registered_resources, set_registered_resources)

    def add_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self not in obj._markets:
                obj._markets.append(self)
            self._registered_resources.append(obj)

    def remove_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self in obj._markets:
                obj._markets.remove(self)
            self._registered_resources.remove(obj)
    # >>> registered_resources

    # <<< settlements
    # @generated
    def get_settlements(self):
        """ 
        """
        return self._settlements

    def set_settlements(self, value):
        for x in self._settlements:
            x._market = None
        for y in value:
            y._market = self
        self._settlements = value

    settlements = property(get_settlements, set_settlements)

    def add_settlements(self, *settlements):
        for obj in settlements:
            obj._market = self
            self._settlements.append(obj)

    def remove_settlements(self, *settlements):
        for obj in settlements:
            obj._market = None
            self._settlements.remove(obj)
    # >>> settlements

    # <<< market_factors
    # @generated
    def get_market_factors(self):
        """ 
        """
        return self._market_factors

    def set_market_factors(self, value):
        for x in self._market_factors:
            x._market = None
        for y in value:
            y._market = self
        self._market_factors = value

    market_factors = property(get_market_factors, set_market_factors)

    def add_market_factors(self, *market_factors):
        for obj in market_factors:
            obj._market = self
            self._market_factors.append(obj)

    def remove_market_factors(self, *market_factors):
        for obj in market_factors:
            obj._market = None
            self._market_factors.remove(obj)
    # >>> market_factors

    # <<< rto
    # @generated
    def get_rto(self):
        """ 
        """
        return self._rto

    def set_rto(self, value):
        if self._rto is not None:
            filtered = [x for x in self.rto.markets if x != self]
            self._rto._markets = filtered

        self._rto = value
        if self._rto is not None:
            self._rto._markets.append(self)

    rto = property(get_rto, set_rto)
    # >>> rto


    def __str__(self):
        """ Returns a string representation of the Market.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Market.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Market", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.bids:
            s += '%s<%s:Market.bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.market_products:
            s += '%s<%s:Market.market_products rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.registered_resources:
            s += '%s<%s:Market.registered_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.settlements:
            s += '%s<%s:Market.settlements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.market_factors:
            s += '%s<%s:Market.market_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.rto is not None:
            s += '%s<%s:Market.rto rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rto.uri)
        s += '%s<%s:Market.ramp_interval_non_spin_res>%s</%s:Market.ramp_interval_non_spin_res>' % \
            (indent, ns_prefix, self.ramp_interval_non_spin_res, ns_prefix)
        s += '%s<%s:Market.local_time_zone>%s</%s:Market.local_time_zone>' % \
            (indent, ns_prefix, self.local_time_zone, ns_prefix)
        s += '%s<%s:Market.ramp_interval_energy>%s</%s:Market.ramp_interval_energy>' % \
            (indent, ns_prefix, self.ramp_interval_energy, ns_prefix)
        s += '%s<%s:Market.type>%s</%s:Market.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:Market.time_interval_length>%s</%s:Market.time_interval_length>' % \
            (indent, ns_prefix, self.time_interval_length, ns_prefix)
        s += '%s<%s:Market.ramp_interval_spin_res>%s</%s:Market.ramp_interval_spin_res>' % \
            (indent, ns_prefix, self.ramp_interval_spin_res, ns_prefix)
        s += '%s<%s:Market.dst>%s</%s:Market.dst>' % \
            (indent, ns_prefix, self.dst, ns_prefix)
        s += '%s<%s:Market.ramp_interval_reg>%s</%s:Market.ramp_interval_reg>' % \
            (indent, ns_prefix, self.ramp_interval_reg, ns_prefix)
        s += '%s<%s:Market.end>%s</%s:Market.end>' % \
            (indent, ns_prefix, self.end, ns_prefix)
        s += '%s<%s:Market.start>%s</%s:Market.start>' % \
            (indent, ns_prefix, self.start, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Market")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market.serialize


class Pnode(IdentifiedObject):
    """ A pricing node is directly associated with a connectivity node.  It is a pricing location for which market participants submit their bids, offers, buy/sell CRRs, and settle.
    """
    # <<< pnode
    # @generated
    def __init__(self, usage='', is_public=False, begin_period='', end_period='', type='', connectivity_node=None, rto=None, delivery_transaction_bids=None, measurements=None, receipt_transaction_bids=None, ftrs=None, registered_resources=None, pnode_clearing=None, **kw_args):
        """ Initialises a new 'Pnode' instance.
        """
        # Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub' 
        self.usage = usage

        # True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions 
        self.is_public = is_public

        # Start date-time of the period in which the price node definition is valid. 
        self.begin_period = begin_period

        # End date-time of the period in which the price node definition is valid 
        self.end_period = end_period

        # Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B) 
        self.type = type


        self._connectivity_node = None
        self.connectivity_node = connectivity_node

        self._rto = None
        self.rto = rto

        self._delivery_transaction_bids = []
        if delivery_transaction_bids is not None:
            self.delivery_transaction_bids = delivery_transaction_bids
        else:
            self.delivery_transaction_bids = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._receipt_transaction_bids = []
        if receipt_transaction_bids is not None:
            self.receipt_transaction_bids = receipt_transaction_bids
        else:
            self.receipt_transaction_bids = []

        self._ftrs = []
        if ftrs is not None:
            self.ftrs = ftrs
        else:
            self.ftrs = []

        self._registered_resources = []
        if registered_resources is not None:
            self.registered_resources = registered_resources
        else:
            self.registered_resources = []

        self._pnode_clearing = None
        self.pnode_clearing = pnode_clearing


        super(Pnode, self).__init__(**kw_args)
    # >>> pnode

    # <<< connectivity_node
    # @generated
    def get_connectivity_node(self):
        """ 
        """
        return self._connectivity_node

    def set_connectivity_node(self, value):
        if self._connectivity_node is not None:
            self._connectivity_node._pnode = None

        self._connectivity_node = value
        if self._connectivity_node is not None:
            self._connectivity_node._pnode = self

    connectivity_node = property(get_connectivity_node, set_connectivity_node)
    # >>> connectivity_node

    # <<< rto
    # @generated
    def get_rto(self):
        """ 
        """
        return self._rto

    def set_rto(self, value):
        if self._rto is not None:
            filtered = [x for x in self.rto.pnodes if x != self]
            self._rto._pnodes = filtered

        self._rto = value
        if self._rto is not None:
            self._rto._pnodes.append(self)

    rto = property(get_rto, set_rto)
    # >>> rto

    # <<< delivery_transaction_bids
    # @generated
    def get_delivery_transaction_bids(self):
        """ 
        """
        return self._delivery_transaction_bids

    def set_delivery_transaction_bids(self, value):
        for x in self._delivery_transaction_bids:
            x._delivery_pnode = None
        for y in value:
            y._delivery_pnode = self
        self._delivery_transaction_bids = value

    delivery_transaction_bids = property(get_delivery_transaction_bids, set_delivery_transaction_bids)

    def add_delivery_transaction_bids(self, *delivery_transaction_bids):
        for obj in delivery_transaction_bids:
            obj._delivery_pnode = self
            self._delivery_transaction_bids.append(obj)

    def remove_delivery_transaction_bids(self, *delivery_transaction_bids):
        for obj in delivery_transaction_bids:
            obj._delivery_pnode = None
            self._delivery_transaction_bids.remove(obj)
    # >>> delivery_transaction_bids

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ 
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._pnode = None
        for y in value:
            y._pnode = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._pnode = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._pnode = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< receipt_transaction_bids
    # @generated
    def get_receipt_transaction_bids(self):
        """ 
        """
        return self._receipt_transaction_bids

    def set_receipt_transaction_bids(self, value):
        for x in self._receipt_transaction_bids:
            x._receipt_pnode = None
        for y in value:
            y._receipt_pnode = self
        self._receipt_transaction_bids = value

    receipt_transaction_bids = property(get_receipt_transaction_bids, set_receipt_transaction_bids)

    def add_receipt_transaction_bids(self, *receipt_transaction_bids):
        for obj in receipt_transaction_bids:
            obj._receipt_pnode = self
            self._receipt_transaction_bids.append(obj)

    def remove_receipt_transaction_bids(self, *receipt_transaction_bids):
        for obj in receipt_transaction_bids:
            obj._receipt_pnode = None
            self._receipt_transaction_bids.remove(obj)
    # >>> receipt_transaction_bids

    # <<< ftrs
    # @generated
    def get_ftrs(self):
        """ 
        """
        return self._ftrs

    def set_ftrs(self, value):
        for p in self._ftrs:
            filtered = [q for q in p.pnodes if q != self]
            self._ftrs._pnodes = filtered
        for r in value:
            if self not in r._pnodes:
                r._pnodes.append(self)
        self._ftrs = value

    ftrs = property(get_ftrs, set_ftrs)

    def add_ftrs(self, *ftrs):
        for obj in ftrs:
            if self not in obj._pnodes:
                obj._pnodes.append(self)
            self._ftrs.append(obj)

    def remove_ftrs(self, *ftrs):
        for obj in ftrs:
            if self in obj._pnodes:
                obj._pnodes.remove(self)
            self._ftrs.remove(obj)
    # >>> ftrs

    # <<< registered_resources
    # @generated
    def get_registered_resources(self):
        """ A registered resource injects power at one or more connectivity nodes related to a pnode
        """
        return self._registered_resources

    def set_registered_resources(self, value):
        for x in self._registered_resources:
            x._pnode = None
        for y in value:
            y._pnode = self
        self._registered_resources = value

    registered_resources = property(get_registered_resources, set_registered_resources)

    def add_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            obj._pnode = self
            self._registered_resources.append(obj)

    def remove_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            obj._pnode = None
            self._registered_resources.remove(obj)
    # >>> registered_resources

    # <<< pnode_clearing
    # @generated
    def get_pnode_clearing(self):
        """ 
        """
        return self._pnode_clearing

    def set_pnode_clearing(self, value):
        if self._pnode_clearing is not None:
            self._pnode_clearing._pnode = None

        self._pnode_clearing = value
        if self._pnode_clearing is not None:
            self._pnode_clearing._pnode = self

    pnode_clearing = property(get_pnode_clearing, set_pnode_clearing)
    # >>> pnode_clearing


    def __str__(self):
        """ Returns a string representation of the Pnode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pnode.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Pnode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Pnode", self.uri)
        if format:
            indent += ' ' * depth

        if self.connectivity_node is not None:
            s += '%s<%s:Pnode.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node.uri)
        if self.rto is not None:
            s += '%s<%s:Pnode.rto rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rto.uri)
        for obj in self.delivery_transaction_bids:
            s += '%s<%s:Pnode.delivery_transaction_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Pnode.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.receipt_transaction_bids:
            s += '%s<%s:Pnode.receipt_transaction_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.ftrs:
            s += '%s<%s:Pnode.ftrs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.registered_resources:
            s += '%s<%s:Pnode.registered_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode_clearing is not None:
            s += '%s<%s:Pnode.pnode_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode_clearing.uri)
        s += '%s<%s:Pnode.usage>%s</%s:Pnode.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
        s += '%s<%s:Pnode.is_public>%s</%s:Pnode.is_public>' % \
            (indent, ns_prefix, self.is_public, ns_prefix)
        s += '%s<%s:Pnode.begin_period>%s</%s:Pnode.begin_period>' % \
            (indent, ns_prefix, self.begin_period, ns_prefix)
        s += '%s<%s:Pnode.end_period>%s</%s:Pnode.end_period>' % \
            (indent, ns_prefix, self.end_period, ns_prefix)
        s += '%s<%s:Pnode.type>%s</%s:Pnode.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Pnode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pnode.serialize


class BaseCaseConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
    """
    # <<< base_case_constraint_limit
    # @generated
    def __init__(self, security_constraint_sum=None, **kw_args):
        """ Initialises a new 'BaseCaseConstraintLimit' instance.
        """

        self._security_constraint_sum = None
        self.security_constraint_sum = security_constraint_sum


        super(BaseCaseConstraintLimit, self).__init__(**kw_args)
    # >>> base_case_constraint_limit

    # <<< security_constraint_sum
    # @generated
    def get_security_constraint_sum(self):
        """ 
        """
        return self._security_constraint_sum

    def set_security_constraint_sum(self, value):
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._base_case_constraint_limit = None

        self._security_constraint_sum = value
        if self._security_constraint_sum is not None:
            self._security_constraint_sum._base_case_constraint_limit = self

    security_constraint_sum = property(get_security_constraint_sum, set_security_constraint_sum)
    # >>> security_constraint_sum


    def __str__(self):
        """ Returns a string representation of the BaseCaseConstraintLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< base_case_constraint_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BaseCaseConstraintLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BaseCaseConstraintLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.security_constraint_sum is not None:
            s += '%s<%s:BaseCaseConstraintLimit.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BaseCaseConstraintLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> base_case_constraint_limit.serialize


class FTR(Agreement):
    """ Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate.
    """
    # <<< ftr
    # @generated
    def __init__(self, action='', class='', base_energy=0.0, optimized='', ftr_type='', pnodes=None, energy_price_curve=None, flowgate=None, **kw_args):
        """ Initialises a new 'FTR' instance.
        """
        # Buy, Sell 
        self.action = action

        # Peak, Off-peak, 24-hour 
        self.class = class

        # Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource. 
        self.base_energy = base_energy

        # Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase 
        self.optimized = optimized

        # Type of rights being offered (product) allowed to be auctioned (option, obligation). 
        self.ftr_type = ftr_type


        self._pnodes = []
        if pnodes is not None:
            self.pnodes = pnodes
        else:
            self.pnodes = []

        self._energy_price_curve = None
        self.energy_price_curve = energy_price_curve

        self._flowgate = None
        self.flowgate = flowgate


        super(FTR, self).__init__(**kw_args)
    # >>> ftr

    # <<< pnodes
    # @generated
    def get_pnodes(self):
        """ 
        """
        return self._pnodes

    def set_pnodes(self, value):
        for p in self._pnodes:
            filtered = [q for q in p.ftrs if q != self]
            self._pnodes._ftrs = filtered
        for r in value:
            if self not in r._ftrs:
                r._ftrs.append(self)
        self._pnodes = value

    pnodes = property(get_pnodes, set_pnodes)

    def add_pnodes(self, *pnodes):
        for obj in pnodes:
            if self not in obj._ftrs:
                obj._ftrs.append(self)
            self._pnodes.append(obj)

    def remove_pnodes(self, *pnodes):
        for obj in pnodes:
            if self in obj._ftrs:
                obj._ftrs.remove(self)
            self._pnodes.remove(obj)
    # >>> pnodes

    # <<< energy_price_curve
    # @generated
    def get_energy_price_curve(self):
        """ 
        """
        return self._energy_price_curve

    def set_energy_price_curve(self, value):
        if self._energy_price_curve is not None:
            filtered = [x for x in self.energy_price_curve.ftrs if x != self]
            self._energy_price_curve._ftrs = filtered

        self._energy_price_curve = value
        if self._energy_price_curve is not None:
            self._energy_price_curve._ftrs.append(self)

    energy_price_curve = property(get_energy_price_curve, set_energy_price_curve)
    # >>> energy_price_curve

    # <<< flowgate
    # @generated
    def get_flowgate(self):
        """ 
        """
        return self._flowgate

    def set_flowgate(self, value):
        if self._flowgate is not None:
            filtered = [x for x in self.flowgate.ftrs if x != self]
            self._flowgate._ftrs = filtered

        self._flowgate = value
        if self._flowgate is not None:
            self._flowgate._ftrs.append(self)

    flowgate = property(get_flowgate, set_flowgate)
    # >>> flowgate


    def __str__(self):
        """ Returns a string representation of the FTR.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ftr.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FTR.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FTR", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.pnodes:
            s += '%s<%s:FTR.pnodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_price_curve is not None:
            s += '%s<%s:FTR.energy_price_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_price_curve.uri)
        if self.flowgate is not None:
            s += '%s<%s:FTR.flowgate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.flowgate.uri)
        s += '%s<%s:FTR.action>%s</%s:FTR.action>' % \
            (indent, ns_prefix, self.action, ns_prefix)
        s += '%s<%s:FTR.class>%s</%s:FTR.class>' % \
            (indent, ns_prefix, self.class, ns_prefix)
        s += '%s<%s:FTR.base_energy>%s</%s:FTR.base_energy>' % \
            (indent, ns_prefix, self.base_energy, ns_prefix)
        s += '%s<%s:FTR.optimized>%s</%s:FTR.optimized>' % \
            (indent, ns_prefix, self.optimized, ns_prefix)
        s += '%s<%s:FTR.ftr_type>%s</%s:FTR.ftr_type>' % \
            (indent, ns_prefix, self.ftr_type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "FTR")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ftr.serialize


class ReserveReqCurve(RegularIntervalSchedule):
    """ A curve relating  reserve requirement versus time, showing the values of a specific reserve requirement for each unit of the period covered. The  curve can be based on 'absolute' time or on 'normalized' time.  X is time, typically expressed in absolute time Y1 is reserve requirement, typically expressed in MW
    """
    # <<< reserve_req_curve
    # @generated
    def __init__(self, reserve_req=None, **kw_args):
        """ Initialises a new 'ReserveReqCurve' instance.
        """

        self._reserve_req = None
        self.reserve_req = reserve_req


        super(ReserveReqCurve, self).__init__(**kw_args)
    # >>> reserve_req_curve

    # <<< reserve_req
    # @generated
    def get_reserve_req(self):
        """ 
        """
        return self._reserve_req

    def set_reserve_req(self, value):
        if self._reserve_req is not None:
            self._reserve_req._reserve_req_curve = None

        self._reserve_req = value
        if self._reserve_req is not None:
            self._reserve_req._reserve_req_curve = self

    reserve_req = property(get_reserve_req, set_reserve_req)
    # >>> reserve_req


    def __str__(self):
        """ Returns a string representation of the ReserveReqCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reserve_req_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReserveReqCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReserveReqCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.reserve_req is not None:
            s += '%s<%s:ReserveReqCurve.reserve_req rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reserve_req.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReserveReqCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reserve_req_curve.serialize


class SecurityConstraints(IdentifiedObject):
    """ Typical for regional transmission operators (RTOs), these constraints include transmission as well as generation group constraints identified in both base case and critical contingency cases.
    """
    # <<< security_constraints
    # @generated
    def __init__(self, max_mw=0.0, actual_mw=0.0, min_mw=0.0, rto=None, **kw_args):
        """ Initialises a new 'SecurityConstraints' instance.
        """
        # Maximum MW limit 
        self.max_mw = max_mw

        # Actual branch or group of branches MW flow (only for transmission constraints) 
        self.actual_mw = actual_mw

        # Minimum MW limit (only for transmission constraints). 
        self.min_mw = min_mw


        self._rto = None
        self.rto = rto


        super(SecurityConstraints, self).__init__(**kw_args)
    # >>> security_constraints

    # <<< rto
    # @generated
    def get_rto(self):
        """ 
        """
        return self._rto

    def set_rto(self, value):
        if self._rto is not None:
            filtered = [x for x in self.rto.security_constraints if x != self]
            self._rto._security_constraints = filtered

        self._rto = value
        if self._rto is not None:
            self._rto._security_constraints.append(self)

    rto = property(get_rto, set_rto)
    # >>> rto


    def __str__(self):
        """ Returns a string representation of the SecurityConstraints.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< security_constraints.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SecurityConstraints.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SecurityConstraints", self.uri)
        if format:
            indent += ' ' * depth

        if self.rto is not None:
            s += '%s<%s:SecurityConstraints.rto rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rto.uri)
        s += '%s<%s:SecurityConstraints.max_mw>%s</%s:SecurityConstraints.max_mw>' % \
            (indent, ns_prefix, self.max_mw, ns_prefix)
        s += '%s<%s:SecurityConstraints.actual_mw>%s</%s:SecurityConstraints.actual_mw>' % \
            (indent, ns_prefix, self.actual_mw, ns_prefix)
        s += '%s<%s:SecurityConstraints.min_mw>%s</%s:SecurityConstraints.min_mw>' % \
            (indent, ns_prefix, self.min_mw, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SecurityConstraints")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> security_constraints.serialize


class MWLimitSchedule(Curve):
    """ Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)
    """
    # <<< mwlimit_schedule
    # @generated
    def __init__(self, security_constraint_limit=None, **kw_args):
        """ Initialises a new 'MWLimitSchedule' instance.
        """

        self._security_constraint_limit = None
        self.security_constraint_limit = security_constraint_limit


        super(MWLimitSchedule, self).__init__(**kw_args)
    # >>> mwlimit_schedule

    # <<< security_constraint_limit
    # @generated
    def get_security_constraint_limit(self):
        """ 
        """
        return self._security_constraint_limit

    def set_security_constraint_limit(self, value):
        if self._security_constraint_limit is not None:
            self._security_constraint_limit._mwlimit_schedules = None

        self._security_constraint_limit = value
        if self._security_constraint_limit is not None:
            self._security_constraint_limit._mwlimit_schedules = self

    security_constraint_limit = property(get_security_constraint_limit, set_security_constraint_limit)
    # >>> security_constraint_limit


    def __str__(self):
        """ Returns a string representation of the MWLimitSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< mwlimit_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MWLimitSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MWLimitSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.security_constraint_limit is not None:
            s += '%s<%s:MWLimitSchedule.security_constraint_limit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_limit.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MWLimitSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> mwlimit_schedule.serialize


class BidSet(IdentifiedObject):
    """ As set of mutually exclusive bids for which a maximum of one may be scheduled. Of these generating bids, only one generating bid can be scheduled at a time.
    """
    # <<< bid_set
    # @generated
    def __init__(self, generating_bids=None, **kw_args):
        """ Initialises a new 'BidSet' instance.
        """

        self._generating_bids = []
        if generating_bids is not None:
            self.generating_bids = generating_bids
        else:
            self.generating_bids = []


        super(BidSet, self).__init__(**kw_args)
    # >>> bid_set

    # <<< generating_bids
    # @generated
    def get_generating_bids(self):
        """ 
        """
        return self._generating_bids

    def set_generating_bids(self, value):
        for x in self._generating_bids:
            x._bid_set = None
        for y in value:
            y._bid_set = self
        self._generating_bids = value

    generating_bids = property(get_generating_bids, set_generating_bids)

    def add_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._bid_set = self
            self._generating_bids.append(obj)

    def remove_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._bid_set = None
            self._generating_bids.remove(obj)
    # >>> generating_bids


    def __str__(self):
        """ Returns a string representation of the BidSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bid_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BidSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BidSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.generating_bids:
            s += '%s<%s:BidSet.generating_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BidSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bid_set.serialize


class TransmissionReliabilityMargin(IdentifiedObject):
    """ Transmission Reliability Margin (TRM) is defined as that amount of transmission transfer capability necessary to ensure that the interconnected transmission network is secure under a reasonable range of uncertainties in system conditions.
    """
    # <<< transmission_reliability_margin
    # @generated
    def __init__(self, value_unit='', trm_value=0.0, trm_type='', flowgate=None, **kw_args):
        """ Initialises a new 'TransmissionReliabilityMargin' instance.
        """
        # unit of the TRM value. Could be MW or Percentage. 
        self.value_unit = value_unit

        # Value of the TRM 
        self.trm_value = trm_value

        # the type of TRM 
        self.trm_type = trm_type


        self._flowgate = []
        if flowgate is not None:
            self.flowgate = flowgate
        else:
            self.flowgate = []


        super(TransmissionReliabilityMargin, self).__init__(**kw_args)
    # >>> transmission_reliability_margin

    # <<< flowgate
    # @generated
    def get_flowgate(self):
        """ A fowgate may have 0 to 1 TRM
        """
        return self._flowgate

    def set_flowgate(self, value):
        for x in self._flowgate:
            x._transmission_reliability_margin = None
        for y in value:
            y._transmission_reliability_margin = self
        self._flowgate = value

    flowgate = property(get_flowgate, set_flowgate)

    def add_flowgate(self, *flowgate):
        for obj in flowgate:
            obj._transmission_reliability_margin = self
            self._flowgate.append(obj)

    def remove_flowgate(self, *flowgate):
        for obj in flowgate:
            obj._transmission_reliability_margin = None
            self._flowgate.remove(obj)
    # >>> flowgate


    def __str__(self):
        """ Returns a string representation of the TransmissionReliabilityMargin.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transmission_reliability_margin.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransmissionReliabilityMargin.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransmissionReliabilityMargin", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.flowgate:
            s += '%s<%s:TransmissionReliabilityMargin.flowgate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:TransmissionReliabilityMargin.value_unit>%s</%s:TransmissionReliabilityMargin.value_unit>' % \
            (indent, ns_prefix, self.value_unit, ns_prefix)
        s += '%s<%s:TransmissionReliabilityMargin.trm_value>%s</%s:TransmissionReliabilityMargin.trm_value>' % \
            (indent, ns_prefix, self.trm_value, ns_prefix)
        s += '%s<%s:TransmissionReliabilityMargin.trm_type>%s</%s:TransmissionReliabilityMargin.trm_type>' % \
            (indent, ns_prefix, self.trm_type, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransmissionReliabilityMargin")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transmission_reliability_margin.serialize


class BidPriceCurve(Curve):
    """ Relationship between unit operating price in $/hour (Y-axis) and unit output in MW (X-axis).
    """
    # <<< bid_price_curve
    # @generated
    def __init__(self, product_bids=None, **kw_args):
        """ Initialises a new 'BidPriceCurve' instance.
        """

        self._product_bids = []
        if product_bids is not None:
            self.product_bids = product_bids
        else:
            self.product_bids = []


        super(BidPriceCurve, self).__init__(**kw_args)
    # >>> bid_price_curve

    # <<< product_bids
    # @generated
    def get_product_bids(self):
        """ 
        """
        return self._product_bids

    def set_product_bids(self, value):
        for x in self._product_bids:
            x._bid_price_curve = None
        for y in value:
            y._bid_price_curve = self
        self._product_bids = value

    product_bids = property(get_product_bids, set_product_bids)

    def add_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._bid_price_curve = self
            self._product_bids.append(obj)

    def remove_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._bid_price_curve = None
            self._product_bids.remove(obj)
    # >>> product_bids


    def __str__(self):
        """ Returns a string representation of the BidPriceCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bid_price_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BidPriceCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BidPriceCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.product_bids:
            s += '%s<%s:BidPriceCurve.product_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BidPriceCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bid_price_curve.serialize


class BilateralTransaction(Element):
    """ Bilateral transaction
    """
    # <<< bilateral_transaction
    # @generated
    def __init__(self, scope='', curtail_time_max=0, curtail_time_min=0, market_type='', purchase_time_min=0, purchase_time_max=0, total_tran_charge_max=0.0, transaction_type='', **kw_args):
        """ Initialises a new 'BilateralTransaction' instance.
        """
        # Transaction scope: 'Internal' 'External' 
        self.scope = scope

        # Maximum curtailment time in number of trading intervals 
        self.curtail_time_max = curtail_time_max

        # Minimum curtailment time in number of trading intervals 
        self.curtail_time_min = curtail_time_min

        # Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead 
        self.market_type = market_type

        # Minimum purchase time in number of trading intervals 
        self.purchase_time_min = purchase_time_min

        # Maximum purchase time in number of trading intervals 
        self.purchase_time_max = purchase_time_max

        # Maximum total transmission (congestion) charges in monetary units 
        self.total_tran_charge_max = total_tran_charge_max

        # Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading 
        self.transaction_type = transaction_type



        super(BilateralTransaction, self).__init__(**kw_args)
    # >>> bilateral_transaction


    def __str__(self):
        """ Returns a string representation of the BilateralTransaction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bilateral_transaction.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BilateralTransaction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BilateralTransaction", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BilateralTransaction.scope>%s</%s:BilateralTransaction.scope>' % \
            (indent, ns_prefix, self.scope, ns_prefix)
        s += '%s<%s:BilateralTransaction.curtail_time_max>%s</%s:BilateralTransaction.curtail_time_max>' % \
            (indent, ns_prefix, self.curtail_time_max, ns_prefix)
        s += '%s<%s:BilateralTransaction.curtail_time_min>%s</%s:BilateralTransaction.curtail_time_min>' % \
            (indent, ns_prefix, self.curtail_time_min, ns_prefix)
        s += '%s<%s:BilateralTransaction.market_type>%s</%s:BilateralTransaction.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)
        s += '%s<%s:BilateralTransaction.purchase_time_min>%s</%s:BilateralTransaction.purchase_time_min>' % \
            (indent, ns_prefix, self.purchase_time_min, ns_prefix)
        s += '%s<%s:BilateralTransaction.purchase_time_max>%s</%s:BilateralTransaction.purchase_time_max>' % \
            (indent, ns_prefix, self.purchase_time_max, ns_prefix)
        s += '%s<%s:BilateralTransaction.total_tran_charge_max>%s</%s:BilateralTransaction.total_tran_charge_max>' % \
            (indent, ns_prefix, self.total_tran_charge_max, ns_prefix)
        s += '%s<%s:BilateralTransaction.transaction_type>%s</%s:BilateralTransaction.transaction_type>' % \
            (indent, ns_prefix, self.transaction_type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BilateralTransaction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bilateral_transaction.serialize


class MarketProduct(IdentifiedObject):
    """ A product traded by an RTO (e.g., energy, 10 minute spinning reserve).  Ancillary service product examples include: Regulation Up Regulation Dn Spinning Reserve Non-Spinning Reserve Operating Reserve
    """
    # <<< market_product
    # @generated
    def __init__(self, market=None, registered_resources=None, reserve_reqs=None, product_bids=None, **kw_args):
        """ Initialises a new 'MarketProduct' instance.
        """

        self._market = None
        self.market = market

        self._registered_resources = []
        if registered_resources is not None:
            self.registered_resources = registered_resources
        else:
            self.registered_resources = []

        self._reserve_reqs = []
        if reserve_reqs is not None:
            self.reserve_reqs = reserve_reqs
        else:
            self.reserve_reqs = []

        self._product_bids = []
        if product_bids is not None:
            self.product_bids = product_bids
        else:
            self.product_bids = []


        super(MarketProduct, self).__init__(**kw_args)
    # >>> market_product

    # <<< market
    # @generated
    def get_market(self):
        """ 
        """
        return self._market

    def set_market(self, value):
        if self._market is not None:
            filtered = [x for x in self.market.market_products if x != self]
            self._market._market_products = filtered

        self._market = value
        if self._market is not None:
            self._market._market_products.append(self)

    market = property(get_market, set_market)
    # >>> market

    # <<< registered_resources
    # @generated
    def get_registered_resources(self):
        """ A registered resource is eligible to bid market products
        """
        return self._registered_resources

    def set_registered_resources(self, value):
        for p in self._registered_resources:
            filtered = [q for q in p.market_products if q != self]
            self._registered_resources._market_products = filtered
        for r in value:
            if self not in r._market_products:
                r._market_products.append(self)
        self._registered_resources = value

    registered_resources = property(get_registered_resources, set_registered_resources)

    def add_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self not in obj._market_products:
                obj._market_products.append(self)
            self._registered_resources.append(obj)

    def remove_registered_resources(self, *registered_resources):
        for obj in registered_resources:
            if self in obj._market_products:
                obj._market_products.remove(self)
            self._registered_resources.remove(obj)
    # >>> registered_resources

    # <<< reserve_reqs
    # @generated
    def get_reserve_reqs(self):
        """ Market product associated with reserve requirement must be a reserve or regulation product.
        """
        return self._reserve_reqs

    def set_reserve_reqs(self, value):
        for x in self._reserve_reqs:
            x._market_product = None
        for y in value:
            y._market_product = self
        self._reserve_reqs = value

    reserve_reqs = property(get_reserve_reqs, set_reserve_reqs)

    def add_reserve_reqs(self, *reserve_reqs):
        for obj in reserve_reqs:
            obj._market_product = self
            self._reserve_reqs.append(obj)

    def remove_reserve_reqs(self, *reserve_reqs):
        for obj in reserve_reqs:
            obj._market_product = None
            self._reserve_reqs.remove(obj)
    # >>> reserve_reqs

    # <<< product_bids
    # @generated
    def get_product_bids(self):
        """ 
        """
        return self._product_bids

    def set_product_bids(self, value):
        for x in self._product_bids:
            x._market_product = None
        for y in value:
            y._market_product = self
        self._product_bids = value

    product_bids = property(get_product_bids, set_product_bids)

    def add_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._market_product = self
            self._product_bids.append(obj)

    def remove_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._market_product = None
            self._product_bids.remove(obj)
    # >>> product_bids


    def __str__(self):
        """ Returns a string representation of the MarketProduct.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_product.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketProduct.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketProduct", self.uri)
        if format:
            indent += ' ' * depth

        if self.market is not None:
            s += '%s<%s:MarketProduct.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.registered_resources:
            s += '%s<%s:MarketProduct.registered_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reserve_reqs:
            s += '%s<%s:MarketProduct.reserve_reqs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.product_bids:
            s += '%s<%s:MarketProduct.product_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketProduct")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_product.serialize


class Flowgate(PowerSystemResource):
    """ A flowgate, is single or group of transmission elements intended to model MW flow impact relating to transmission limitations and transmission service usage.
    """
    # <<< flowgate
    # @generated
    def __init__(self, coordinated_flag=False, counter_flow_value=0, reciprocal_flag=False, managing_entity_flag=False, out_of_service_date='', coordination_study_date='', atc_flag=False, in_service_date='', idc_assigned_id=0, idc_operational_name='', positive_impact_value=0, deletion_date='', sub_control_area=None, violation_limits=None, transmission_provider=None, transmission_reliability_margin=None, power_transormers=None, idc_type=None, lines=None, capacity_benefit_margin=None, afc_use_code=None, ftrs=None, **kw_args):
        """ Initialises a new 'Flowgate' instance.
        """
        # Flag to indicate if Flowgate qualified as coordinated Flowgate 
        self.coordinated_flag = coordinated_flag

        # Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less. 
        self.counter_flow_value = counter_flow_value

        # Flag to indicate if Flowgate qualified as reciprocal Flowgate 
        self.reciprocal_flag = reciprocal_flag

        # Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false. 
        self.managing_entity_flag = managing_entity_flag

        # Date at which point Flowgate becomes inactive. Used to insert outage condition. 
        self.out_of_service_date = out_of_service_date

        # Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet. 
        self.coordination_study_date = coordination_study_date

        # Flag to indicate if Flowgate is utilized for coordination of ATC. 
        self.atc_flag = atc_flag

        # Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition. 
        self.in_service_date = in_service_date

        # The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate. 
        self.idc_assigned_id = idc_assigned_id

        # The Registered Name utilized in the IDC and/or Book of Flowgates 
        self.idc_operational_name = idc_operational_name

        # Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less. 
        self.positive_impact_value = positive_impact_value

        # Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC). 
        self.deletion_date = deletion_date


        self._sub_control_area = None
        self.sub_control_area = sub_control_area

        self._violation_limits = []
        if violation_limits is not None:
            self.violation_limits = violation_limits
        else:
            self.violation_limits = []

        self._transmission_provider = []
        if transmission_provider is not None:
            self.transmission_provider = transmission_provider
        else:
            self.transmission_provider = []

        self._transmission_reliability_margin = None
        self.transmission_reliability_margin = transmission_reliability_margin

        self._power_transormers = []
        if power_transormers is not None:
            self.power_transormers = power_transormers
        else:
            self.power_transormers = []

        self.idc_type = idc_type

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []

        self._capacity_benefit_margin = []
        if capacity_benefit_margin is not None:
            self.capacity_benefit_margin = capacity_benefit_margin
        else:
            self.capacity_benefit_margin = []

        self.afc_use_code = afc_use_code

        self._ftrs = []
        if ftrs is not None:
            self.ftrs = ftrs
        else:
            self.ftrs = []


        super(Flowgate, self).__init__(**kw_args)
    # >>> flowgate

    # <<< sub_control_area
    # @generated
    def get_sub_control_area(self):
        """ A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        """
        return self._sub_control_area

    def set_sub_control_area(self, value):
        if self._sub_control_area is not None:
            filtered = [x for x in self.sub_control_area.flowgate if x != self]
            self._sub_control_area._flowgate = filtered

        self._sub_control_area = value
        if self._sub_control_area is not None:
            self._sub_control_area._flowgate.append(self)

    sub_control_area = property(get_sub_control_area, set_sub_control_area)
    # >>> sub_control_area

    # <<< violation_limits
    # @generated
    def get_violation_limits(self):
        """ 
        """
        return self._violation_limits

    def set_violation_limits(self, value):
        for x in self._violation_limits:
            x._flowgate = None
        for y in value:
            y._flowgate = self
        self._violation_limits = value

    violation_limits = property(get_violation_limits, set_violation_limits)

    def add_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._flowgate = self
            self._violation_limits.append(obj)

    def remove_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._flowgate = None
            self._violation_limits.remove(obj)
    # >>> violation_limits

    # <<< transmission_provider
    # @generated
    def get_transmission_provider(self):
        """ A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
        """
        return self._transmission_provider

    def set_transmission_provider(self, value):
        for p in self._transmission_provider:
            filtered = [q for q in p.flowgate if q != self]
            self._transmission_provider._flowgate = filtered
        for r in value:
            if self not in r._flowgate:
                r._flowgate.append(self)
        self._transmission_provider = value

    transmission_provider = property(get_transmission_provider, set_transmission_provider)

    def add_transmission_provider(self, *transmission_provider):
        for obj in transmission_provider:
            if self not in obj._flowgate:
                obj._flowgate.append(self)
            self._transmission_provider.append(obj)

    def remove_transmission_provider(self, *transmission_provider):
        for obj in transmission_provider:
            if self in obj._flowgate:
                obj._flowgate.remove(self)
            self._transmission_provider.remove(obj)
    # >>> transmission_provider

    # <<< transmission_reliability_margin
    # @generated
    def get_transmission_reliability_margin(self):
        """ A fowgate may have 0 to 1 TRM
        """
        return self._transmission_reliability_margin

    def set_transmission_reliability_margin(self, value):
        if self._transmission_reliability_margin is not None:
            filtered = [x for x in self.transmission_reliability_margin.flowgate if x != self]
            self._transmission_reliability_margin._flowgate = filtered

        self._transmission_reliability_margin = value
        if self._transmission_reliability_margin is not None:
            self._transmission_reliability_margin._flowgate.append(self)

    transmission_reliability_margin = property(get_transmission_reliability_margin, set_transmission_reliability_margin)
    # >>> transmission_reliability_margin

    # <<< power_transormers
    # @generated
    def get_power_transormers(self):
        """ 
        """
        return self._power_transormers

    def set_power_transormers(self, value):
        for p in self._power_transormers:
            filtered = [q for q in p.flowgates if q != self]
            self._power_transormers._flowgates = filtered
        for r in value:
            if self not in r._flowgates:
                r._flowgates.append(self)
        self._power_transormers = value

    power_transormers = property(get_power_transormers, set_power_transormers)

    def add_power_transormers(self, *power_transormers):
        for obj in power_transormers:
            if self not in obj._flowgates:
                obj._flowgates.append(self)
            self._power_transormers.append(obj)

    def remove_power_transormers(self, *power_transormers):
        for obj in power_transormers:
            if self in obj._flowgates:
                obj._flowgates.remove(self)
            self._power_transormers.remove(obj)
    # >>> power_transormers

    # <<< idc_type
    # @generated
    # The type of Flowgate.  Values are 'PERMANENT' (in Book of Flowgates) or 'TEMPORARY'.
    idc_type = None
    # >>> idc_type

    # <<< lines
    # @generated
    def get_lines(self):
        """ 
        """
        return self._lines

    def set_lines(self, value):
        for p in self._lines:
            filtered = [q for q in p.flowgates if q != self]
            self._lines._flowgates = filtered
        for r in value:
            if self not in r._flowgates:
                r._flowgates.append(self)
        self._lines = value

    lines = property(get_lines, set_lines)

    def add_lines(self, *lines):
        for obj in lines:
            if self not in obj._flowgates:
                obj._flowgates.append(self)
            self._lines.append(obj)

    def remove_lines(self, *lines):
        for obj in lines:
            if self in obj._flowgates:
                obj._flowgates.remove(self)
            self._lines.remove(obj)
    # >>> lines

    # <<< capacity_benefit_margin
    # @generated
    def get_capacity_benefit_margin(self):
        """ A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        """
        return self._capacity_benefit_margin

    def set_capacity_benefit_margin(self, value):
        for p in self._capacity_benefit_margin:
            filtered = [q for q in p.flowgate if q != self]
            self._capacity_benefit_margin._flowgate = filtered
        for r in value:
            if self not in r._flowgate:
                r._flowgate.append(self)
        self._capacity_benefit_margin = value

    capacity_benefit_margin = property(get_capacity_benefit_margin, set_capacity_benefit_margin)

    def add_capacity_benefit_margin(self, *capacity_benefit_margin):
        for obj in capacity_benefit_margin:
            if self not in obj._flowgate:
                obj._flowgate.append(self)
            self._capacity_benefit_margin.append(obj)

    def remove_capacity_benefit_margin(self, *capacity_benefit_margin):
        for obj in capacity_benefit_margin:
            if self in obj._flowgate:
                obj._flowgate.remove(self)
            self._capacity_benefit_margin.remove(obj)
    # >>> capacity_benefit_margin

    # <<< afc_use_code
    # @generated
    # Used to indicate if FG should be used only for certain types of AFC Calculations.  Values are 'FIRM,'  'NONFIRM,' and 'BOTH.'
    afc_use_code = None
    # >>> afc_use_code

    # <<< ftrs
    # @generated
    def get_ftrs(self):
        """ 
        """
        return self._ftrs

    def set_ftrs(self, value):
        for x in self._ftrs:
            x._flowgate = None
        for y in value:
            y._flowgate = self
        self._ftrs = value

    ftrs = property(get_ftrs, set_ftrs)

    def add_ftrs(self, *ftrs):
        for obj in ftrs:
            obj._flowgate = self
            self._ftrs.append(obj)

    def remove_ftrs(self, *ftrs):
        for obj in ftrs:
            obj._flowgate = None
            self._ftrs.remove(obj)
    # >>> ftrs


    def __str__(self):
        """ Returns a string representation of the Flowgate.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< flowgate.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Flowgate.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Flowgate", self.uri)
        if format:
            indent += ' ' * depth

        if self.sub_control_area is not None:
            s += '%s<%s:Flowgate.sub_control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sub_control_area.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Flowgate.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transmission_provider:
            s += '%s<%s:Flowgate.transmission_provider rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transmission_reliability_margin is not None:
            s += '%s<%s:Flowgate.transmission_reliability_margin rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transmission_reliability_margin.uri)
        for obj in self.power_transormers:
            s += '%s<%s:Flowgate.power_transormers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.idc_type is not None:
            s += '%s<%s:Flowgate.idc_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.idc_type.uri)
        for obj in self.lines:
            s += '%s<%s:Flowgate.lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.capacity_benefit_margin:
            s += '%s<%s:Flowgate.capacity_benefit_margin rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.afc_use_code is not None:
            s += '%s<%s:Flowgate.afc_use_code rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.afc_use_code.uri)
        for obj in self.ftrs:
            s += '%s<%s:Flowgate.ftrs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Flowgate.coordinated_flag>%s</%s:Flowgate.coordinated_flag>' % \
            (indent, ns_prefix, self.coordinated_flag, ns_prefix)
        s += '%s<%s:Flowgate.counter_flow_value>%s</%s:Flowgate.counter_flow_value>' % \
            (indent, ns_prefix, self.counter_flow_value, ns_prefix)
        s += '%s<%s:Flowgate.reciprocal_flag>%s</%s:Flowgate.reciprocal_flag>' % \
            (indent, ns_prefix, self.reciprocal_flag, ns_prefix)
        s += '%s<%s:Flowgate.managing_entity_flag>%s</%s:Flowgate.managing_entity_flag>' % \
            (indent, ns_prefix, self.managing_entity_flag, ns_prefix)
        s += '%s<%s:Flowgate.out_of_service_date>%s</%s:Flowgate.out_of_service_date>' % \
            (indent, ns_prefix, self.out_of_service_date, ns_prefix)
        s += '%s<%s:Flowgate.coordination_study_date>%s</%s:Flowgate.coordination_study_date>' % \
            (indent, ns_prefix, self.coordination_study_date, ns_prefix)
        s += '%s<%s:Flowgate.atc_flag>%s</%s:Flowgate.atc_flag>' % \
            (indent, ns_prefix, self.atc_flag, ns_prefix)
        s += '%s<%s:Flowgate.in_service_date>%s</%s:Flowgate.in_service_date>' % \
            (indent, ns_prefix, self.in_service_date, ns_prefix)
        s += '%s<%s:Flowgate.idc_assigned_id>%s</%s:Flowgate.idc_assigned_id>' % \
            (indent, ns_prefix, self.idc_assigned_id, ns_prefix)
        s += '%s<%s:Flowgate.idc_operational_name>%s</%s:Flowgate.idc_operational_name>' % \
            (indent, ns_prefix, self.idc_operational_name, ns_prefix)
        s += '%s<%s:Flowgate.positive_impact_value>%s</%s:Flowgate.positive_impact_value>' % \
            (indent, ns_prefix, self.positive_impact_value, ns_prefix)
        s += '%s<%s:Flowgate.deletion_date>%s</%s:Flowgate.deletion_date>' % \
            (indent, ns_prefix, self.deletion_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Flowgate")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> flowgate.serialize


class ViolationLimit(Limit):
    """ A type of limit that indicates if it is enforced and, through association, the organisation responsible for setting the limit.
    """
    # <<< violation_limit
    # @generated
    def __init__(self, enforced=False, organisations=None, flowgate=None, season=None, measurement=None, **kw_args):
        """ Initialises a new 'ViolationLimit' instance.
        """
        # True if limit is enforced. 
        self.enforced = enforced


        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []

        self._flowgate = None
        self.flowgate = flowgate

        self._season = None
        self.season = season

        self._measurement = None
        self.measurement = measurement


        super(ViolationLimit, self).__init__(**kw_args)
    # >>> violation_limit

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.violation_limits if q != self]
            self._organisations._violation_limits = filtered
        for r in value:
            if self not in r._violation_limits:
                r._violation_limits.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._violation_limits:
                obj._violation_limits.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._violation_limits:
                obj._violation_limits.remove(self)
            self._organisations.remove(obj)
    # >>> organisations

    # <<< flowgate
    # @generated
    def get_flowgate(self):
        """ 
        """
        return self._flowgate

    def set_flowgate(self, value):
        if self._flowgate is not None:
            filtered = [x for x in self.flowgate.violation_limits if x != self]
            self._flowgate._violation_limits = filtered

        self._flowgate = value
        if self._flowgate is not None:
            self._flowgate._violation_limits.append(self)

    flowgate = property(get_flowgate, set_flowgate)
    # >>> flowgate

    # <<< season
    # @generated
    def get_season(self):
        """ Limits may differ based on the season
        """
        return self._season

    def set_season(self, value):
        if self._season is not None:
            filtered = [x for x in self.season.violation_limits if x != self]
            self._season._violation_limits = filtered

        self._season = value
        if self._season is not None:
            self._season._violation_limits.append(self)

    season = property(get_season, set_season)
    # >>> season

    # <<< measurement
    # @generated
    def get_measurement(self):
        """ 
        """
        return self._measurement

    def set_measurement(self, value):
        if self._measurement is not None:
            filtered = [x for x in self.measurement.violation_limits if x != self]
            self._measurement._violation_limits = filtered

        self._measurement = value
        if self._measurement is not None:
            self._measurement._violation_limits.append(self)

    measurement = property(get_measurement, set_measurement)
    # >>> measurement


    def __str__(self):
        """ Returns a string representation of the ViolationLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< violation_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ViolationLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ViolationLimit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.organisations:
            s += '%s<%s:ViolationLimit.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.flowgate is not None:
            s += '%s<%s:ViolationLimit.flowgate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.flowgate.uri)
        if self.season is not None:
            s += '%s<%s:ViolationLimit.season rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.season.uri)
        if self.measurement is not None:
            s += '%s<%s:ViolationLimit.measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement.uri)
        s += '%s<%s:ViolationLimit.enforced>%s</%s:ViolationLimit.enforced>' % \
            (indent, ns_prefix, self.enforced, ns_prefix)
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
        for obj in self.procedures:
            s += '%s<%s:Limit.procedures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ViolationLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> violation_limit.serialize


class SensitivityPriceCurve(Curve):
    """ Optionally, this curve expresses elasticity of the associated requirement.  For example, used to reduce requirements when clearing price exceeds reasonable values when the supply quantity becomes scarce.  For example, a single point value of $1000/MW for a spinning reserve will cause a reduction in the required spinning reserve.  X axis is constrained quantity (e.g., MW) Y1 axis is money per constrained quantity
    """
    # <<< sensitivity_price_curve
    # @generated
    def __init__(self, reserve_req=None, **kw_args):
        """ Initialises a new 'SensitivityPriceCurve' instance.
        """

        self._reserve_req = None
        self.reserve_req = reserve_req


        super(SensitivityPriceCurve, self).__init__(**kw_args)
    # >>> sensitivity_price_curve

    # <<< reserve_req
    # @generated
    def get_reserve_req(self):
        """ 
        """
        return self._reserve_req

    def set_reserve_req(self, value):
        if self._reserve_req is not None:
            self._reserve_req._sensitivity_price_curve = None

        self._reserve_req = value
        if self._reserve_req is not None:
            self._reserve_req._sensitivity_price_curve = self

    reserve_req = property(get_reserve_req, set_reserve_req)
    # >>> reserve_req


    def __str__(self):
        """ Returns a string representation of the SensitivityPriceCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sensitivity_price_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SensitivityPriceCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SensitivityPriceCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.reserve_req is not None:
            s += '%s<%s:SensitivityPriceCurve.reserve_req rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reserve_req.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SensitivityPriceCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sensitivity_price_curve.serialize


class CapacityBenefitMargin(Profile):
    """ Capacity Benefit Margin (CBM) is defined as that amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. Reservation fo CBM by a load serving entity allows that entity to reduce its installed generating capacity below that which may otherwise have been necessary without interconnections to meet its generation reliability requirements.  CBM is modeled as a profile with values in different time periods which are represented by the profile data.
    """
    # <<< capacity_benefit_margin
    # @generated
    def __init__(self, season=None, flowgate=None, **kw_args):
        """ Initialises a new 'CapacityBenefitMargin' instance.
        """

        self._season = None
        self.season = season

        self._flowgate = []
        if flowgate is not None:
            self.flowgate = flowgate
        else:
            self.flowgate = []


        super(CapacityBenefitMargin, self).__init__(**kw_args)
    # >>> capacity_benefit_margin

    # <<< season
    # @generated
    def get_season(self):
        """ Capacity Benefit Margin may differ based on the season
        """
        return self._season

    def set_season(self, value):
        if self._season is not None:
            filtered = [x for x in self.season.capacity_benefit_margin if x != self]
            self._season._capacity_benefit_margin = filtered

        self._season = value
        if self._season is not None:
            self._season._capacity_benefit_margin.append(self)

    season = property(get_season, set_season)
    # >>> season

    # <<< flowgate
    # @generated
    def get_flowgate(self):
        """ A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        """
        return self._flowgate

    def set_flowgate(self, value):
        for p in self._flowgate:
            filtered = [q for q in p.capacity_benefit_margin if q != self]
            self._flowgate._capacity_benefit_margin = filtered
        for r in value:
            if self not in r._capacity_benefit_margin:
                r._capacity_benefit_margin.append(self)
        self._flowgate = value

    flowgate = property(get_flowgate, set_flowgate)

    def add_flowgate(self, *flowgate):
        for obj in flowgate:
            if self not in obj._capacity_benefit_margin:
                obj._capacity_benefit_margin.append(self)
            self._flowgate.append(obj)

    def remove_flowgate(self, *flowgate):
        for obj in flowgate:
            if self in obj._capacity_benefit_margin:
                obj._capacity_benefit_margin.remove(self)
            self._flowgate.remove(obj)
    # >>> flowgate


    def __str__(self):
        """ Returns a string representation of the CapacityBenefitMargin.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< capacity_benefit_margin.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CapacityBenefitMargin.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CapacityBenefitMargin", self.uri)
        if format:
            indent += ' ' * depth

        if self.season is not None:
            s += '%s<%s:CapacityBenefitMargin.season rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.season.uri)
        for obj in self.flowgate:
            s += '%s<%s:CapacityBenefitMargin.flowgate rdf:resource="#%s"/>' % \
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
        for obj in self.profile_datas:
            s += '%s<%s:Profile.profile_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CapacityBenefitMargin")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> capacity_benefit_margin.serialize


class RTO(ErpOrganisation):
    """ Regional transmission operator.
    """
    # <<< rto
    # @generated
    def __init__(self, pnodes=None, security_constraints=None, security_constraints_linear=None, resource_group_reqs=None, markets=None, **kw_args):
        """ Initialises a new 'RTO' instance.
        """

        self._pnodes = []
        if pnodes is not None:
            self.pnodes = pnodes
        else:
            self.pnodes = []

        self._security_constraints = []
        if security_constraints is not None:
            self.security_constraints = security_constraints
        else:
            self.security_constraints = []

        self._security_constraints_linear = []
        if security_constraints_linear is not None:
            self.security_constraints_linear = security_constraints_linear
        else:
            self.security_constraints_linear = []

        self._resource_group_reqs = []
        if resource_group_reqs is not None:
            self.resource_group_reqs = resource_group_reqs
        else:
            self.resource_group_reqs = []

        self._markets = []
        if markets is not None:
            self.markets = markets
        else:
            self.markets = []


        super(RTO, self).__init__(**kw_args)
    # >>> rto

    # <<< pnodes
    # @generated
    def get_pnodes(self):
        """ 
        """
        return self._pnodes

    def set_pnodes(self, value):
        for x in self._pnodes:
            x._rto = None
        for y in value:
            y._rto = self
        self._pnodes = value

    pnodes = property(get_pnodes, set_pnodes)

    def add_pnodes(self, *pnodes):
        for obj in pnodes:
            obj._rto = self
            self._pnodes.append(obj)

    def remove_pnodes(self, *pnodes):
        for obj in pnodes:
            obj._rto = None
            self._pnodes.remove(obj)
    # >>> pnodes

    # <<< security_constraints
    # @generated
    def get_security_constraints(self):
        """ 
        """
        return self._security_constraints

    def set_security_constraints(self, value):
        for x in self._security_constraints:
            x._rto = None
        for y in value:
            y._rto = self
        self._security_constraints = value

    security_constraints = property(get_security_constraints, set_security_constraints)

    def add_security_constraints(self, *security_constraints):
        for obj in security_constraints:
            obj._rto = self
            self._security_constraints.append(obj)

    def remove_security_constraints(self, *security_constraints):
        for obj in security_constraints:
            obj._rto = None
            self._security_constraints.remove(obj)
    # >>> security_constraints

    # <<< security_constraints_linear
    # @generated
    def get_security_constraints_linear(self):
        """ 
        """
        return self._security_constraints_linear

    def set_security_constraints_linear(self, value):
        for x in self._security_constraints_linear:
            x._rto = None
        for y in value:
            y._rto = self
        self._security_constraints_linear = value

    security_constraints_linear = property(get_security_constraints_linear, set_security_constraints_linear)

    def add_security_constraints_linear(self, *security_constraints_linear):
        for obj in security_constraints_linear:
            obj._rto = self
            self._security_constraints_linear.append(obj)

    def remove_security_constraints_linear(self, *security_constraints_linear):
        for obj in security_constraints_linear:
            obj._rto = None
            self._security_constraints_linear.remove(obj)
    # >>> security_constraints_linear

    # <<< resource_group_reqs
    # @generated
    def get_resource_group_reqs(self):
        """ 
        """
        return self._resource_group_reqs

    def set_resource_group_reqs(self, value):
        for p in self._resource_group_reqs:
            filtered = [q for q in p.rtos if q != self]
            self._resource_group_reqs._rtos = filtered
        for r in value:
            if self not in r._rtos:
                r._rtos.append(self)
        self._resource_group_reqs = value

    resource_group_reqs = property(get_resource_group_reqs, set_resource_group_reqs)

    def add_resource_group_reqs(self, *resource_group_reqs):
        for obj in resource_group_reqs:
            if self not in obj._rtos:
                obj._rtos.append(self)
            self._resource_group_reqs.append(obj)

    def remove_resource_group_reqs(self, *resource_group_reqs):
        for obj in resource_group_reqs:
            if self in obj._rtos:
                obj._rtos.remove(self)
            self._resource_group_reqs.remove(obj)
    # >>> resource_group_reqs

    # <<< markets
    # @generated
    def get_markets(self):
        """ 
        """
        return self._markets

    def set_markets(self, value):
        for x in self._markets:
            x._rto = None
        for y in value:
            y._rto = self
        self._markets = value

    markets = property(get_markets, set_markets)

    def add_markets(self, *markets):
        for obj in markets:
            obj._rto = self
            self._markets.append(obj)

    def remove_markets(self, *markets):
        for obj in markets:
            obj._rto = None
            self._markets.remove(obj)
    # >>> markets


    def __str__(self):
        """ Returns a string representation of the RTO.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< rto.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RTO.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RTO", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.pnodes:
            s += '%s<%s:RTO.pnodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.security_constraints:
            s += '%s<%s:RTO.security_constraints rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.security_constraints_linear:
            s += '%s<%s:RTO.security_constraints_linear rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resource_group_reqs:
            s += '%s<%s:RTO.resource_group_reqs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.markets:
            s += '%s<%s:RTO.markets rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RTO")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> rto.serialize


class LoadReductionPriceCurve(Curve):
    """ This is the price sensitivity that bidder expresses for allowing market load interruption.  Relationship between price (Y1-axis) vs. MW (X-axis).
    """
    # <<< load_reduction_price_curve
    # @generated
    def __init__(self, load_bids=None, **kw_args):
        """ Initialises a new 'LoadReductionPriceCurve' instance.
        """

        self._load_bids = []
        if load_bids is not None:
            self.load_bids = load_bids
        else:
            self.load_bids = []


        super(LoadReductionPriceCurve, self).__init__(**kw_args)
    # >>> load_reduction_price_curve

    # <<< load_bids
    # @generated
    def get_load_bids(self):
        """ 
        """
        return self._load_bids

    def set_load_bids(self, value):
        for x in self._load_bids:
            x._load_reduction_price_curve = None
        for y in value:
            y._load_reduction_price_curve = self
        self._load_bids = value

    load_bids = property(get_load_bids, set_load_bids)

    def add_load_bids(self, *load_bids):
        for obj in load_bids:
            obj._load_reduction_price_curve = self
            self._load_bids.append(obj)

    def remove_load_bids(self, *load_bids):
        for obj in load_bids:
            obj._load_reduction_price_curve = None
            self._load_bids.remove(obj)
    # >>> load_bids


    def __str__(self):
        """ Returns a string representation of the LoadReductionPriceCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_reduction_price_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadReductionPriceCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadReductionPriceCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.load_bids:
            s += '%s<%s:LoadReductionPriceCurve.load_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadReductionPriceCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_reduction_price_curve.serialize


class BillDeterminant(Document):
    # <<< bill_determinant
    # @generated
    def __init__(self, calculation_level='', precision_level='', unit_of_measure='', config_version='', number_interval=0, charge_profile=None, charge_profile_data=None, user_attributes=None, **kw_args):
        """ Initialises a new 'BillDeterminant' instance.
        """
        # Level in charge calculation order. 
        self.calculation_level = calculation_level

        # The level of precision in the current value. 
        self.precision_level = precision_level

        # The UOM for the current value of the Bill Determinant. 
        self.unit_of_measure = unit_of_measure

        # The version of configuration of calculation logic in the settlement. 
        self.config_version = config_version

        # Number of intervals of bill determiant in trade day, eg 300 for five minute intervals. 
        self.number_interval = number_interval


        self._charge_profile = None
        self.charge_profile = charge_profile

        self._charge_profile_data = []
        if charge_profile_data is not None:
            self.charge_profile_data = charge_profile_data
        else:
            self.charge_profile_data = []

        self._user_attributes = []
        if user_attributes is not None:
            self.user_attributes = user_attributes
        else:
            self.user_attributes = []


        super(BillDeterminant, self).__init__(**kw_args)
    # >>> bill_determinant

    # <<< charge_profile
    # @generated
    def get_charge_profile(self):
        """ 
        """
        return self._charge_profile

    def set_charge_profile(self, value):
        if self._charge_profile is not None:
            self._charge_profile._bill_determinant = None

        self._charge_profile = value
        if self._charge_profile is not None:
            self._charge_profile._bill_determinant = self

    charge_profile = property(get_charge_profile, set_charge_profile)
    # >>> charge_profile

    # <<< charge_profile_data
    # @generated
    def get_charge_profile_data(self):
        """ 
        """
        return self._charge_profile_data

    def set_charge_profile_data(self, value):
        for x in self._charge_profile_data:
            x._bill_determinant = None
        for y in value:
            y._bill_determinant = self
        self._charge_profile_data = value

    charge_profile_data = property(get_charge_profile_data, set_charge_profile_data)

    def add_charge_profile_data(self, *charge_profile_data):
        for obj in charge_profile_data:
            obj._bill_determinant = self
            self._charge_profile_data.append(obj)

    def remove_charge_profile_data(self, *charge_profile_data):
        for obj in charge_profile_data:
            obj._bill_determinant = None
            self._charge_profile_data.remove(obj)
    # >>> charge_profile_data

    # <<< user_attributes
    # @generated
    def get_user_attributes(self):
        """ 
        """
        return self._user_attributes

    def set_user_attributes(self, value):
        for p in self._user_attributes:
            filtered = [q for q in p.bill_determinants if q != self]
            self._user_attributes._bill_determinants = filtered
        for r in value:
            if self not in r._bill_determinants:
                r._bill_determinants.append(self)
        self._user_attributes = value

    user_attributes = property(get_user_attributes, set_user_attributes)

    def add_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self not in obj._bill_determinants:
                obj._bill_determinants.append(self)
            self._user_attributes.append(obj)

    def remove_user_attributes(self, *user_attributes):
        for obj in user_attributes:
            if self in obj._bill_determinants:
                obj._bill_determinants.remove(self)
            self._user_attributes.remove(obj)
    # >>> user_attributes


    def __str__(self):
        """ Returns a string representation of the BillDeterminant.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bill_determinant.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BillDeterminant.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BillDeterminant", self.uri)
        if format:
            indent += ' ' * depth

        if self.charge_profile is not None:
            s += '%s<%s:BillDeterminant.charge_profile rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.charge_profile.uri)
        for obj in self.charge_profile_data:
            s += '%s<%s:BillDeterminant.charge_profile_data rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.user_attributes:
            s += '%s<%s:BillDeterminant.user_attributes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BillDeterminant.calculation_level>%s</%s:BillDeterminant.calculation_level>' % \
            (indent, ns_prefix, self.calculation_level, ns_prefix)
        s += '%s<%s:BillDeterminant.precision_level>%s</%s:BillDeterminant.precision_level>' % \
            (indent, ns_prefix, self.precision_level, ns_prefix)
        s += '%s<%s:BillDeterminant.unit_of_measure>%s</%s:BillDeterminant.unit_of_measure>' % \
            (indent, ns_prefix, self.unit_of_measure, ns_prefix)
        s += '%s<%s:BillDeterminant.config_version>%s</%s:BillDeterminant.config_version>' % \
            (indent, ns_prefix, self.config_version, ns_prefix)
        s += '%s<%s:BillDeterminant.number_interval>%s</%s:BillDeterminant.number_interval>' % \
            (indent, ns_prefix, self.number_interval, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BillDeterminant")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bill_determinant.serialize


class ChargeProfileData(Element):
    # <<< charge_profile_data
    # @generated
    def __init__(self, sequence=0, value=0.0, time_stamp='', bill_determinant=None, charge_profile=None, **kw_args):
        """ Initialises a new 'ChargeProfileData' instance.
        """
        # The sequence number of the profile. 
        self.sequence = sequence

        # The value of an interval given a profile type (amount, price, or quantity), subject to the UOM. 
        self.value = value

        # The date and time of an interval. 
        self.time_stamp = time_stamp


        self._bill_determinant = None
        self.bill_determinant = bill_determinant

        self._charge_profile = None
        self.charge_profile = charge_profile


        super(ChargeProfileData, self).__init__(**kw_args)
    # >>> charge_profile_data

    # <<< bill_determinant
    # @generated
    def get_bill_determinant(self):
        """ 
        """
        return self._bill_determinant

    def set_bill_determinant(self, value):
        if self._bill_determinant is not None:
            filtered = [x for x in self.bill_determinant.charge_profile_data if x != self]
            self._bill_determinant._charge_profile_data = filtered

        self._bill_determinant = value
        if self._bill_determinant is not None:
            self._bill_determinant._charge_profile_data.append(self)

    bill_determinant = property(get_bill_determinant, set_bill_determinant)
    # >>> bill_determinant

    # <<< charge_profile
    # @generated
    def get_charge_profile(self):
        """ 
        """
        return self._charge_profile

    def set_charge_profile(self, value):
        if self._charge_profile is not None:
            filtered = [x for x in self.charge_profile.charge_profile_data if x != self]
            self._charge_profile._charge_profile_data = filtered

        self._charge_profile = value
        if self._charge_profile is not None:
            self._charge_profile._charge_profile_data.append(self)

    charge_profile = property(get_charge_profile, set_charge_profile)
    # >>> charge_profile


    def __str__(self):
        """ Returns a string representation of the ChargeProfileData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< charge_profile_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ChargeProfileData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ChargeProfileData", self.uri)
        if format:
            indent += ' ' * depth

        if self.bill_determinant is not None:
            s += '%s<%s:ChargeProfileData.bill_determinant rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bill_determinant.uri)
        if self.charge_profile is not None:
            s += '%s<%s:ChargeProfileData.charge_profile rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.charge_profile.uri)
        s += '%s<%s:ChargeProfileData.sequence>%s</%s:ChargeProfileData.sequence>' % \
            (indent, ns_prefix, self.sequence, ns_prefix)
        s += '%s<%s:ChargeProfileData.value>%s</%s:ChargeProfileData.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:ChargeProfileData.time_stamp>%s</%s:ChargeProfileData.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ChargeProfileData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> charge_profile_data.serialize


class StartUpCostCurve(Curve):
    """ Startup costs and time as a function of down time.  Relationship between unit startup cost (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """
    # <<< start_up_cost_curve
    # @generated
    def __init__(self, generating_bids=None, registered_generators=None, **kw_args):
        """ Initialises a new 'StartUpCostCurve' instance.
        """

        self._generating_bids = []
        if generating_bids is not None:
            self.generating_bids = generating_bids
        else:
            self.generating_bids = []

        self._registered_generators = []
        if registered_generators is not None:
            self.registered_generators = registered_generators
        else:
            self.registered_generators = []


        super(StartUpCostCurve, self).__init__(**kw_args)
    # >>> start_up_cost_curve

    # <<< generating_bids
    # @generated
    def get_generating_bids(self):
        """ 
        """
        return self._generating_bids

    def set_generating_bids(self, value):
        for x in self._generating_bids:
            x._start_up_cost_curve = None
        for y in value:
            y._start_up_cost_curve = self
        self._generating_bids = value

    generating_bids = property(get_generating_bids, set_generating_bids)

    def add_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._start_up_cost_curve = self
            self._generating_bids.append(obj)

    def remove_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._start_up_cost_curve = None
            self._generating_bids.remove(obj)
    # >>> generating_bids

    # <<< registered_generators
    # @generated
    def get_registered_generators(self):
        """ 
        """
        return self._registered_generators

    def set_registered_generators(self, value):
        for p in self._registered_generators:
            filtered = [q for q in p.start_up_cost_curves if q != self]
            self._registered_generators._start_up_cost_curves = filtered
        for r in value:
            if self not in r._start_up_cost_curves:
                r._start_up_cost_curves.append(self)
        self._registered_generators = value

    registered_generators = property(get_registered_generators, set_registered_generators)

    def add_registered_generators(self, *registered_generators):
        for obj in registered_generators:
            if self not in obj._start_up_cost_curves:
                obj._start_up_cost_curves.append(self)
            self._registered_generators.append(obj)

    def remove_registered_generators(self, *registered_generators):
        for obj in registered_generators:
            if self in obj._start_up_cost_curves:
                obj._start_up_cost_curves.remove(self)
            self._registered_generators.remove(obj)
    # >>> registered_generators


    def __str__(self):
        """ Returns a string representation of the StartUpCostCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< start_up_cost_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StartUpCostCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StartUpCostCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.generating_bids:
            s += '%s<%s:StartUpCostCurve.generating_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.registered_generators:
            s += '%s<%s:StartUpCostCurve.registered_generators rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "StartUpCostCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> start_up_cost_curve.serialize


class NotificationTimeCurve(Curve):
    """ Notification time curve as a function of down time.  Relationship between crew notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """
    # <<< notification_time_curve
    # @generated
    def __init__(self, generating_bids=None, **kw_args):
        """ Initialises a new 'NotificationTimeCurve' instance.
        """

        self._generating_bids = []
        if generating_bids is not None:
            self.generating_bids = generating_bids
        else:
            self.generating_bids = []


        super(NotificationTimeCurve, self).__init__(**kw_args)
    # >>> notification_time_curve

    # <<< generating_bids
    # @generated
    def get_generating_bids(self):
        """ 
        """
        return self._generating_bids

    def set_generating_bids(self, value):
        for x in self._generating_bids:
            x._notification_time_curve = None
        for y in value:
            y._notification_time_curve = self
        self._generating_bids = value

    generating_bids = property(get_generating_bids, set_generating_bids)

    def add_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._notification_time_curve = self
            self._generating_bids.append(obj)

    def remove_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._notification_time_curve = None
            self._generating_bids.remove(obj)
    # >>> generating_bids


    def __str__(self):
        """ Returns a string representation of the NotificationTimeCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< notification_time_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NotificationTimeCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NotificationTimeCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.generating_bids:
            s += '%s<%s:NotificationTimeCurve.generating_bids rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "NotificationTimeCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> notification_time_curve.serialize


class UnitInitialConditions(IdentifiedObject):
    """ Resource status at the end of a given clearing period.
    """
    # <<< unit_initial_conditions
    # @generated
    def __init__(self, resource_status=0, cum_status_changes=0, status_date='', resource_mw=0.0, time_in_status=0.0, generating_unit=None, cum_energy=None, **kw_args):
        """ Initialises a new 'UnitInitialConditions' instance.
        """
        # Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process 
        self.resource_status = resource_status

        # Cumulative number of status changes of the resource. 
        self.cum_status_changes = cum_status_changes

        # Time and date for resourceStatus 
        self.status_date = status_date

        # Resource MW output at the end of previous clearing period. 
        self.resource_mw = resource_mw

        # Time in market trading intervals the resource is in the state as of the end of the previous clearing period. 
        self.time_in_status = time_in_status


        self._generating_unit = None
        self.generating_unit = generating_unit

        self.cum_energy = cum_energy


        super(UnitInitialConditions, self).__init__(**kw_args)
    # >>> unit_initial_conditions

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ 
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.unit_initial_conditions if x != self]
            self._generating_unit._unit_initial_conditions = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._unit_initial_conditions.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit

    # <<< cum_energy
    # @generated
    # Cumulative energy production over trading period.
    cum_energy = None
    # >>> cum_energy


    def __str__(self):
        """ Returns a string representation of the UnitInitialConditions.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< unit_initial_conditions.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the UnitInitialConditions.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "UnitInitialConditions", self.uri)
        if format:
            indent += ' ' * depth

        if self.generating_unit is not None:
            s += '%s<%s:UnitInitialConditions.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        if self.cum_energy is not None:
            s += '%s<%s:UnitInitialConditions.cum_energy rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cum_energy.uri)
        s += '%s<%s:UnitInitialConditions.resource_status>%s</%s:UnitInitialConditions.resource_status>' % \
            (indent, ns_prefix, self.resource_status, ns_prefix)
        s += '%s<%s:UnitInitialConditions.cum_status_changes>%s</%s:UnitInitialConditions.cum_status_changes>' % \
            (indent, ns_prefix, self.cum_status_changes, ns_prefix)
        s += '%s<%s:UnitInitialConditions.status_date>%s</%s:UnitInitialConditions.status_date>' % \
            (indent, ns_prefix, self.status_date, ns_prefix)
        s += '%s<%s:UnitInitialConditions.resource_mw>%s</%s:UnitInitialConditions.resource_mw>' % \
            (indent, ns_prefix, self.resource_mw, ns_prefix)
        s += '%s<%s:UnitInitialConditions.time_in_status>%s</%s:UnitInitialConditions.time_in_status>' % \
            (indent, ns_prefix, self.time_in_status, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "UnitInitialConditions")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> unit_initial_conditions.serialize


class ReserveReq(ResourceGroupReq):
    """ Requirements for minimum amount of reserve and/or regulation to be supplied by a set of qualified resources.
    """
    # <<< reserve_req
    # @generated
    def __init__(self, market_product=None, reserve_req_curve=None, sensitivity_price_curve=None, **kw_args):
        """ Initialises a new 'ReserveReq' instance.
        """

        self._market_product = None
        self.market_product = market_product

        self._reserve_req_curve = None
        self.reserve_req_curve = reserve_req_curve

        self._sensitivity_price_curve = None
        self.sensitivity_price_curve = sensitivity_price_curve


        super(ReserveReq, self).__init__(**kw_args)
    # >>> reserve_req

    # <<< market_product
    # @generated
    def get_market_product(self):
        """ Market product associated with reserve requirement must be a reserve or regulation product.
        """
        return self._market_product

    def set_market_product(self, value):
        if self._market_product is not None:
            filtered = [x for x in self.market_product.reserve_reqs if x != self]
            self._market_product._reserve_reqs = filtered

        self._market_product = value
        if self._market_product is not None:
            self._market_product._reserve_reqs.append(self)

    market_product = property(get_market_product, set_market_product)
    # >>> market_product

    # <<< reserve_req_curve
    # @generated
    def get_reserve_req_curve(self):
        """ 
        """
        return self._reserve_req_curve

    def set_reserve_req_curve(self, value):
        if self._reserve_req_curve is not None:
            self._reserve_req_curve._reserve_req = None

        self._reserve_req_curve = value
        if self._reserve_req_curve is not None:
            self._reserve_req_curve._reserve_req = self

    reserve_req_curve = property(get_reserve_req_curve, set_reserve_req_curve)
    # >>> reserve_req_curve

    # <<< sensitivity_price_curve
    # @generated
    def get_sensitivity_price_curve(self):
        """ 
        """
        return self._sensitivity_price_curve

    def set_sensitivity_price_curve(self, value):
        if self._sensitivity_price_curve is not None:
            self._sensitivity_price_curve._reserve_req = None

        self._sensitivity_price_curve = value
        if self._sensitivity_price_curve is not None:
            self._sensitivity_price_curve._reserve_req = self

    sensitivity_price_curve = property(get_sensitivity_price_curve, set_sensitivity_price_curve)
    # >>> sensitivity_price_curve


    def __str__(self):
        """ Returns a string representation of the ReserveReq.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reserve_req.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReserveReq.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReserveReq", self.uri)
        if format:
            indent += ' ' * depth

        if self.market_product is not None:
            s += '%s<%s:ReserveReq.market_product rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market_product.uri)
        if self.reserve_req_curve is not None:
            s += '%s<%s:ReserveReq.reserve_req_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reserve_req_curve.uri)
        if self.sensitivity_price_curve is not None:
            s += '%s<%s:ReserveReq.sensitivity_price_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sensitivity_price_curve.uri)
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
        if self.resource_group is not None:
            s += '%s<%s:ResourceGroupReq.resource_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.resource_group.uri)
        for obj in self.rtos:
            s += '%s<%s:ResourceGroupReq.rtos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReserveReq")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reserve_req.serialize


class TerminalConstraintTerm(ConstraintTerm):
    """ A constraint term associated with a specific terminal on a physical piece of equipment.
    """
    # <<< terminal_constraint_term
    # @generated
    def __init__(self, terminal=None, **kw_args):
        """ Initialises a new 'TerminalConstraintTerm' instance.
        """

        self._terminal = None
        self.terminal = terminal


        super(TerminalConstraintTerm, self).__init__(**kw_args)
    # >>> terminal_constraint_term

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ 
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.terminal_constraints if x != self]
            self._terminal._terminal_constraints = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._terminal_constraints.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal


    def __str__(self):
        """ Returns a string representation of the TerminalConstraintTerm.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< terminal_constraint_term.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TerminalConstraintTerm.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TerminalConstraintTerm", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:TerminalConstraintTerm.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
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
        if self.security_constraint_sum is not None:
            s += '%s<%s:ConstraintTerm.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
        s += '%s<%s:ConstraintTerm.factor>%s</%s:ConstraintTerm.factor>' % \
            (indent, ns_prefix, self.factor, ns_prefix)
        s += '%s<%s:ConstraintTerm.function>%s</%s:ConstraintTerm.function>' % \
            (indent, ns_prefix, self.function, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TerminalConstraintTerm")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> terminal_constraint_term.serialize


class LossPenaltyFactor(MarketFactors):
    """ Loss penalty factor applied to a ConnectivityNode for a given time interval.
    """
    # <<< loss_penalty_factor
    # @generated
    def __init__(self, connectivity_nodes=None, loss_factor=None, **kw_args):
        """ Initialises a new 'LossPenaltyFactor' instance.
        """

        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []

        self.loss_factor = loss_factor


        super(LossPenaltyFactor, self).__init__(**kw_args)
    # >>> loss_penalty_factor

    # <<< connectivity_nodes
    # @generated
    def get_connectivity_nodes(self):
        """ 
        """
        return self._connectivity_nodes

    def set_connectivity_nodes(self, value):
        for p in self._connectivity_nodes:
            filtered = [q for q in p.loss_penalty_factors if q != self]
            self._connectivity_nodes._loss_penalty_factors = filtered
        for r in value:
            if self not in r._loss_penalty_factors:
                r._loss_penalty_factors.append(self)
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            if self not in obj._loss_penalty_factors:
                obj._loss_penalty_factors.append(self)
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            if self in obj._loss_penalty_factors:
                obj._loss_penalty_factors.remove(self)
            self._connectivity_nodes.remove(obj)
    # >>> connectivity_nodes

    # <<< loss_factor
    # @generated
    # Loss penalty factor.
    loss_factor = None
    # >>> loss_factor


    def __str__(self):
        """ Returns a string representation of the LossPenaltyFactor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< loss_penalty_factor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LossPenaltyFactor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LossPenaltyFactor", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.connectivity_nodes:
            s += '%s<%s:LossPenaltyFactor.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.loss_factor is not None:
            s += '%s<%s:LossPenaltyFactor.loss_factor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.loss_factor.uri)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LossPenaltyFactor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> loss_penalty_factor.serialize


class PnodeClearing(MarketFactors):
    """ Pricing node clearing results posted for a given settlement period.
    """
    # <<< pnode_clearing
    # @generated
    def __init__(self, congest_lmp=0.0, loss_lmp=0.0, cost_lmp=0.0, pnode=None, **kw_args):
        """ Initialises a new 'PnodeClearing' instance.
        """
        # Congestion component of Location Marginal Price (LMP) in monetary units per MW. 
        self.congest_lmp = congest_lmp

        # Loss component of Location Marginal Price (LMP) in monetary units per MW. 
        self.loss_lmp = loss_lmp

        # Cost component of Locational Marginal Pricing (LMP) in monetary units per MW. 
        self.cost_lmp = cost_lmp


        self._pnode = None
        self.pnode = pnode


        super(PnodeClearing, self).__init__(**kw_args)
    # >>> pnode_clearing

    # <<< pnode
    # @generated
    def get_pnode(self):
        """ 
        """
        return self._pnode

    def set_pnode(self, value):
        if self._pnode is not None:
            self._pnode._pnode_clearing = None

        self._pnode = value
        if self._pnode is not None:
            self._pnode._pnode_clearing = self

    pnode = property(get_pnode, set_pnode)
    # >>> pnode


    def __str__(self):
        """ Returns a string representation of the PnodeClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pnode_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PnodeClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PnodeClearing", self.uri)
        if format:
            indent += ' ' * depth

        if self.pnode is not None:
            s += '%s<%s:PnodeClearing.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        s += '%s<%s:PnodeClearing.congest_lmp>%s</%s:PnodeClearing.congest_lmp>' % \
            (indent, ns_prefix, self.congest_lmp, ns_prefix)
        s += '%s<%s:PnodeClearing.loss_lmp>%s</%s:PnodeClearing.loss_lmp>' % \
            (indent, ns_prefix, self.loss_lmp, ns_prefix)
        s += '%s<%s:PnodeClearing.cost_lmp>%s</%s:PnodeClearing.cost_lmp>' % \
            (indent, ns_prefix, self.cost_lmp, ns_prefix)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PnodeClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pnode_clearing.serialize


class ResourceBid(Bid):
    """ Energy bid for generation, load, or virtual type for the whole of the market-trading period (i.e., one day in day ahead market or one hour in the real time market)
    """
    # <<< resource_bid
    # @generated
    def __init__(self, start_ups_max_day=0, energy_min_day=0.0, energy_max_day=0.0, virtual=False, start_ups_max_week=0, commodity_type='', shut_downs_max_week=0, shut_downs_max_day=0, **kw_args):
        """ Initialises a new 'ResourceBid' instance.
        """
        # Maximum number of startups per day. 
        self.start_ups_max_day = start_ups_max_day

        # Minimum amount of energy per day which has to be produced during the trading period in MWh 
        self.energy_min_day = energy_min_day

        # Maximum amount of energy per day which can be produced during the trading period in MWh 
        self.energy_max_day = energy_max_day

        # True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent 
        self.virtual = virtual

        # Maximum number of startups per week. 
        self.start_ups_max_week = start_ups_max_week

        # Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve 
        self.commodity_type = commodity_type

        # Maximum number of shutdowns per week. 
        self.shut_downs_max_week = shut_downs_max_week

        # Maximum number of shutdowns per day. 
        self.shut_downs_max_day = shut_downs_max_day



        super(ResourceBid, self).__init__(**kw_args)
    # >>> resource_bid


    def __str__(self):
        """ Returns a string representation of the ResourceBid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< resource_bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ResourceBid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ResourceBid", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ResourceBid.start_ups_max_day>%s</%s:ResourceBid.start_ups_max_day>' % \
            (indent, ns_prefix, self.start_ups_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_min_day>%s</%s:ResourceBid.energy_min_day>' % \
            (indent, ns_prefix, self.energy_min_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_max_day>%s</%s:ResourceBid.energy_max_day>' % \
            (indent, ns_prefix, self.energy_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.virtual>%s</%s:ResourceBid.virtual>' % \
            (indent, ns_prefix, self.virtual, ns_prefix)
        s += '%s<%s:ResourceBid.start_ups_max_week>%s</%s:ResourceBid.start_ups_max_week>' % \
            (indent, ns_prefix, self.start_ups_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.commodity_type>%s</%s:ResourceBid.commodity_type>' % \
            (indent, ns_prefix, self.commodity_type, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_week>%s</%s:ResourceBid.shut_downs_max_week>' % \
            (indent, ns_prefix, self.shut_downs_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_day>%s</%s:ResourceBid.shut_downs_max_day>' % \
            (indent, ns_prefix, self.shut_downs_max_day, ns_prefix)
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
        if self.market is not None:
            s += '%s<%s:Bid.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.product_bids:
            s += '%s<%s:Bid.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bid_clearing is not None:
            s += '%s<%s:Bid.bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_clearing.uri)
        s += '%s<%s:Bid.stop_time>%s</%s:Bid.stop_time>' % \
            (indent, ns_prefix, self.stop_time, ns_prefix)
        s += '%s<%s:Bid.start_time>%s</%s:Bid.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Bid.market_type>%s</%s:Bid.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ResourceBid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> resource_bid.serialize


class LoadBid(ResourceBid):
    # <<< load_bid
    # @generated
    def __init__(self, min_time_bet_load_red=0.0, min_load_reduction_cost=0.0, min_load_reduction_interval=0.0, min_load=0.0, req_notice_time=0.0, min_load_reduction=0.0, shutdown_cost=0.0, load_reduction_price_curve=None, registered_load=None, pick_up_ramp_rate=None, drop_ramp_rate=None, **kw_args):
        """ Initialises a new 'LoadBid' instance.
        """
        # Shortest time that load must be left at normal levels before a new load reduction. 
        self.min_time_bet_load_red = min_time_bet_load_red

        # Cost in $ at the minimum reduced load 
        self.min_load_reduction_cost = min_load_reduction_cost

        # Shortest period load reduction must be maintained before load can be restored to normal levels. 
        self.min_load_reduction_interval = min_load_reduction_interval

        # Minimum MW load below which it may not be reduced. 
        self.min_load = min_load

        # Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction. 
        self.req_notice_time = req_notice_time

        # Minimum MW for a load reduction (e.g., MW rating of a discrete pump. 
        self.min_load_reduction = min_load_reduction

        # The fixed cost associated with committing a load reduction. 
        self.shutdown_cost = shutdown_cost


        self._load_reduction_price_curve = None
        self.load_reduction_price_curve = load_reduction_price_curve

        self._registered_load = None
        self.registered_load = registered_load

        self.pick_up_ramp_rate = pick_up_ramp_rate

        self.drop_ramp_rate = drop_ramp_rate


        super(LoadBid, self).__init__(**kw_args)
    # >>> load_bid

    # <<< load_reduction_price_curve
    # @generated
    def get_load_reduction_price_curve(self):
        """ 
        """
        return self._load_reduction_price_curve

    def set_load_reduction_price_curve(self, value):
        if self._load_reduction_price_curve is not None:
            filtered = [x for x in self.load_reduction_price_curve.load_bids if x != self]
            self._load_reduction_price_curve._load_bids = filtered

        self._load_reduction_price_curve = value
        if self._load_reduction_price_curve is not None:
            self._load_reduction_price_curve._load_bids.append(self)

    load_reduction_price_curve = property(get_load_reduction_price_curve, set_load_reduction_price_curve)
    # >>> load_reduction_price_curve

    # <<< registered_load
    # @generated
    def get_registered_load(self):
        """ 
        """
        return self._registered_load

    def set_registered_load(self, value):
        if self._registered_load is not None:
            filtered = [x for x in self.registered_load.load_bids if x != self]
            self._registered_load._load_bids = filtered

        self._registered_load = value
        if self._registered_load is not None:
            self._registered_load._load_bids.append(self)

    registered_load = property(get_registered_load, set_registered_load)
    # >>> registered_load

    # <<< pick_up_ramp_rate
    # @generated
    # Maximum rate load may be restored (MW/minute)
    pick_up_ramp_rate = None
    # >>> pick_up_ramp_rate

    # <<< drop_ramp_rate
    # @generated
    # Maximum rate that load can be reduced (MW/minute)
    drop_ramp_rate = None
    # >>> drop_ramp_rate


    def __str__(self):
        """ Returns a string representation of the LoadBid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadBid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadBid", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_reduction_price_curve is not None:
            s += '%s<%s:LoadBid.load_reduction_price_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_reduction_price_curve.uri)
        if self.registered_load is not None:
            s += '%s<%s:LoadBid.registered_load rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.registered_load.uri)
        if self.pick_up_ramp_rate is not None:
            s += '%s<%s:LoadBid.pick_up_ramp_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pick_up_ramp_rate.uri)
        if self.drop_ramp_rate is not None:
            s += '%s<%s:LoadBid.drop_ramp_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.drop_ramp_rate.uri)
        s += '%s<%s:LoadBid.min_time_bet_load_red>%s</%s:LoadBid.min_time_bet_load_red>' % \
            (indent, ns_prefix, self.min_time_bet_load_red, ns_prefix)
        s += '%s<%s:LoadBid.min_load_reduction_cost>%s</%s:LoadBid.min_load_reduction_cost>' % \
            (indent, ns_prefix, self.min_load_reduction_cost, ns_prefix)
        s += '%s<%s:LoadBid.min_load_reduction_interval>%s</%s:LoadBid.min_load_reduction_interval>' % \
            (indent, ns_prefix, self.min_load_reduction_interval, ns_prefix)
        s += '%s<%s:LoadBid.min_load>%s</%s:LoadBid.min_load>' % \
            (indent, ns_prefix, self.min_load, ns_prefix)
        s += '%s<%s:LoadBid.req_notice_time>%s</%s:LoadBid.req_notice_time>' % \
            (indent, ns_prefix, self.req_notice_time, ns_prefix)
        s += '%s<%s:LoadBid.min_load_reduction>%s</%s:LoadBid.min_load_reduction>' % \
            (indent, ns_prefix, self.min_load_reduction, ns_prefix)
        s += '%s<%s:LoadBid.shutdown_cost>%s</%s:LoadBid.shutdown_cost>' % \
            (indent, ns_prefix, self.shutdown_cost, ns_prefix)
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
        if self.market is not None:
            s += '%s<%s:Bid.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.product_bids:
            s += '%s<%s:Bid.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bid_clearing is not None:
            s += '%s<%s:Bid.bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_clearing.uri)
        s += '%s<%s:Bid.stop_time>%s</%s:Bid.stop_time>' % \
            (indent, ns_prefix, self.stop_time, ns_prefix)
        s += '%s<%s:Bid.start_time>%s</%s:Bid.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Bid.market_type>%s</%s:Bid.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)
        s += '%s<%s:ResourceBid.start_ups_max_day>%s</%s:ResourceBid.start_ups_max_day>' % \
            (indent, ns_prefix, self.start_ups_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_min_day>%s</%s:ResourceBid.energy_min_day>' % \
            (indent, ns_prefix, self.energy_min_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_max_day>%s</%s:ResourceBid.energy_max_day>' % \
            (indent, ns_prefix, self.energy_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.virtual>%s</%s:ResourceBid.virtual>' % \
            (indent, ns_prefix, self.virtual, ns_prefix)
        s += '%s<%s:ResourceBid.start_ups_max_week>%s</%s:ResourceBid.start_ups_max_week>' % \
            (indent, ns_prefix, self.start_ups_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.commodity_type>%s</%s:ResourceBid.commodity_type>' % \
            (indent, ns_prefix, self.commodity_type, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_week>%s</%s:ResourceBid.shut_downs_max_week>' % \
            (indent, ns_prefix, self.shut_downs_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_day>%s</%s:ResourceBid.shut_downs_max_day>' % \
            (indent, ns_prefix, self.shut_downs_max_day, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadBid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_bid.serialize


class GeneratingBid(ResourceBid):
    # <<< generating_bid
    # @generated
    def __init__(self, max_emergency_mw=0.0, maximum_economic_mw=0.0, minimum_economic_mw=0.0, down_time_max=0.0, operating_mode='', startup_time=0.0, min_emergency_mw=0.0, no_load_cost=0.0, minimum_down_time=0.0, start_up_type=0, up_time_min=0.0, up_time_max=0.0, notification_time=0.0, start_up_ramp_rate=None, notification_time_curve=None, registered_generator=None, start_up_cost_curve=None, bid_set=None, start_up_time_curve=None, **kw_args):
        """ Initialises a new 'GeneratingBid' instance.
        """
        # Power rating available for unit under emergency conditions greater than or equal to maximum economic limit. 
        self.max_emergency_mw = max_emergency_mw

        # Maximum high economic MW limit, that should not exceed the maximum operating MW limit 
        self.maximum_economic_mw = maximum_economic_mw

        # Low economic MW limit that must be greater than or equal to the minimum operating MW limit 
        self.minimum_economic_mw = minimum_economic_mw

        # Maximum down time. 
        self.down_time_max = down_time_max

        # Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable) 
        self.operating_mode = operating_mode

        # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        self.startup_time = startup_time

        # Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum. 
        self.min_emergency_mw = min_emergency_mw

        # Resource fixed no load cost. 
        self.no_load_cost = no_load_cost

        # Minimum time interval between unit shutdown and startup 
        self.minimum_down_time = minimum_down_time

        # Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time 
        self.start_up_type = start_up_type

        # Minimum up time. 
        self.up_time_min = up_time_min

        # Maximum up time. 
        self.up_time_max = up_time_max

        # Time required for crew notification prior to start up of the unit. 
        self.notification_time = notification_time


        self.start_up_ramp_rate = start_up_ramp_rate

        self._notification_time_curve = None
        self.notification_time_curve = notification_time_curve

        self._registered_generator = None
        self.registered_generator = registered_generator

        self._start_up_cost_curve = None
        self.start_up_cost_curve = start_up_cost_curve

        self._bid_set = None
        self.bid_set = bid_set

        self._start_up_time_curve = None
        self.start_up_time_curve = start_up_time_curve


        super(GeneratingBid, self).__init__(**kw_args)
    # >>> generating_bid

    # <<< start_up_ramp_rate
    # @generated
    # Resource startup ramp rate (MW/minute)
    start_up_ramp_rate = None
    # >>> start_up_ramp_rate

    # <<< notification_time_curve
    # @generated
    def get_notification_time_curve(self):
        """ 
        """
        return self._notification_time_curve

    def set_notification_time_curve(self, value):
        if self._notification_time_curve is not None:
            filtered = [x for x in self.notification_time_curve.generating_bids if x != self]
            self._notification_time_curve._generating_bids = filtered

        self._notification_time_curve = value
        if self._notification_time_curve is not None:
            self._notification_time_curve._generating_bids.append(self)

    notification_time_curve = property(get_notification_time_curve, set_notification_time_curve)
    # >>> notification_time_curve

    # <<< registered_generator
    # @generated
    def get_registered_generator(self):
        """ 
        """
        return self._registered_generator

    def set_registered_generator(self, value):
        if self._registered_generator is not None:
            filtered = [x for x in self.registered_generator.generating_bids if x != self]
            self._registered_generator._generating_bids = filtered

        self._registered_generator = value
        if self._registered_generator is not None:
            self._registered_generator._generating_bids.append(self)

    registered_generator = property(get_registered_generator, set_registered_generator)
    # >>> registered_generator

    # <<< start_up_cost_curve
    # @generated
    def get_start_up_cost_curve(self):
        """ 
        """
        return self._start_up_cost_curve

    def set_start_up_cost_curve(self, value):
        if self._start_up_cost_curve is not None:
            filtered = [x for x in self.start_up_cost_curve.generating_bids if x != self]
            self._start_up_cost_curve._generating_bids = filtered

        self._start_up_cost_curve = value
        if self._start_up_cost_curve is not None:
            self._start_up_cost_curve._generating_bids.append(self)

    start_up_cost_curve = property(get_start_up_cost_curve, set_start_up_cost_curve)
    # >>> start_up_cost_curve

    # <<< bid_set
    # @generated
    def get_bid_set(self):
        """ 
        """
        return self._bid_set

    def set_bid_set(self, value):
        if self._bid_set is not None:
            filtered = [x for x in self.bid_set.generating_bids if x != self]
            self._bid_set._generating_bids = filtered

        self._bid_set = value
        if self._bid_set is not None:
            self._bid_set._generating_bids.append(self)

    bid_set = property(get_bid_set, set_bid_set)
    # >>> bid_set

    # <<< start_up_time_curve
    # @generated
    def get_start_up_time_curve(self):
        """ 
        """
        return self._start_up_time_curve

    def set_start_up_time_curve(self, value):
        if self._start_up_time_curve is not None:
            filtered = [x for x in self.start_up_time_curve.generating_bids if x != self]
            self._start_up_time_curve._generating_bids = filtered

        self._start_up_time_curve = value
        if self._start_up_time_curve is not None:
            self._start_up_time_curve._generating_bids.append(self)

    start_up_time_curve = property(get_start_up_time_curve, set_start_up_time_curve)
    # >>> start_up_time_curve


    def __str__(self):
        """ Returns a string representation of the GeneratingBid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< generating_bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeneratingBid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeneratingBid", self.uri)
        if format:
            indent += ' ' * depth

        if self.start_up_ramp_rate is not None:
            s += '%s<%s:GeneratingBid.start_up_ramp_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.start_up_ramp_rate.uri)
        if self.notification_time_curve is not None:
            s += '%s<%s:GeneratingBid.notification_time_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.notification_time_curve.uri)
        if self.registered_generator is not None:
            s += '%s<%s:GeneratingBid.registered_generator rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.registered_generator.uri)
        if self.start_up_cost_curve is not None:
            s += '%s<%s:GeneratingBid.start_up_cost_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.start_up_cost_curve.uri)
        if self.bid_set is not None:
            s += '%s<%s:GeneratingBid.bid_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_set.uri)
        if self.start_up_time_curve is not None:
            s += '%s<%s:GeneratingBid.start_up_time_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.start_up_time_curve.uri)
        s += '%s<%s:GeneratingBid.max_emergency_mw>%s</%s:GeneratingBid.max_emergency_mw>' % \
            (indent, ns_prefix, self.max_emergency_mw, ns_prefix)
        s += '%s<%s:GeneratingBid.maximum_economic_mw>%s</%s:GeneratingBid.maximum_economic_mw>' % \
            (indent, ns_prefix, self.maximum_economic_mw, ns_prefix)
        s += '%s<%s:GeneratingBid.minimum_economic_mw>%s</%s:GeneratingBid.minimum_economic_mw>' % \
            (indent, ns_prefix, self.minimum_economic_mw, ns_prefix)
        s += '%s<%s:GeneratingBid.down_time_max>%s</%s:GeneratingBid.down_time_max>' % \
            (indent, ns_prefix, self.down_time_max, ns_prefix)
        s += '%s<%s:GeneratingBid.operating_mode>%s</%s:GeneratingBid.operating_mode>' % \
            (indent, ns_prefix, self.operating_mode, ns_prefix)
        s += '%s<%s:GeneratingBid.startup_time>%s</%s:GeneratingBid.startup_time>' % \
            (indent, ns_prefix, self.startup_time, ns_prefix)
        s += '%s<%s:GeneratingBid.min_emergency_mw>%s</%s:GeneratingBid.min_emergency_mw>' % \
            (indent, ns_prefix, self.min_emergency_mw, ns_prefix)
        s += '%s<%s:GeneratingBid.no_load_cost>%s</%s:GeneratingBid.no_load_cost>' % \
            (indent, ns_prefix, self.no_load_cost, ns_prefix)
        s += '%s<%s:GeneratingBid.minimum_down_time>%s</%s:GeneratingBid.minimum_down_time>' % \
            (indent, ns_prefix, self.minimum_down_time, ns_prefix)
        s += '%s<%s:GeneratingBid.start_up_type>%s</%s:GeneratingBid.start_up_type>' % \
            (indent, ns_prefix, self.start_up_type, ns_prefix)
        s += '%s<%s:GeneratingBid.up_time_min>%s</%s:GeneratingBid.up_time_min>' % \
            (indent, ns_prefix, self.up_time_min, ns_prefix)
        s += '%s<%s:GeneratingBid.up_time_max>%s</%s:GeneratingBid.up_time_max>' % \
            (indent, ns_prefix, self.up_time_max, ns_prefix)
        s += '%s<%s:GeneratingBid.notification_time>%s</%s:GeneratingBid.notification_time>' % \
            (indent, ns_prefix, self.notification_time, ns_prefix)
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
        if self.market is not None:
            s += '%s<%s:Bid.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.product_bids:
            s += '%s<%s:Bid.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bid_clearing is not None:
            s += '%s<%s:Bid.bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_clearing.uri)
        s += '%s<%s:Bid.stop_time>%s</%s:Bid.stop_time>' % \
            (indent, ns_prefix, self.stop_time, ns_prefix)
        s += '%s<%s:Bid.start_time>%s</%s:Bid.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Bid.market_type>%s</%s:Bid.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)
        s += '%s<%s:ResourceBid.start_ups_max_day>%s</%s:ResourceBid.start_ups_max_day>' % \
            (indent, ns_prefix, self.start_ups_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_min_day>%s</%s:ResourceBid.energy_min_day>' % \
            (indent, ns_prefix, self.energy_min_day, ns_prefix)
        s += '%s<%s:ResourceBid.energy_max_day>%s</%s:ResourceBid.energy_max_day>' % \
            (indent, ns_prefix, self.energy_max_day, ns_prefix)
        s += '%s<%s:ResourceBid.virtual>%s</%s:ResourceBid.virtual>' % \
            (indent, ns_prefix, self.virtual, ns_prefix)
        s += '%s<%s:ResourceBid.start_ups_max_week>%s</%s:ResourceBid.start_ups_max_week>' % \
            (indent, ns_prefix, self.start_ups_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.commodity_type>%s</%s:ResourceBid.commodity_type>' % \
            (indent, ns_prefix, self.commodity_type, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_week>%s</%s:ResourceBid.shut_downs_max_week>' % \
            (indent, ns_prefix, self.shut_downs_max_week, ns_prefix)
        s += '%s<%s:ResourceBid.shut_downs_max_day>%s</%s:ResourceBid.shut_downs_max_day>' % \
            (indent, ns_prefix, self.shut_downs_max_day, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeneratingBid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> generating_bid.serialize


class RegisteredGenerator(RegisteredResource):
    # <<< registered_generator
    # @generated
    def __init__(self, maximum_allowable_spinning_reserve=0.0, high_control_limit=0.0, maximum_operating_mw=0.0, low_control_limit=0.0, minimum_operating_mw=0.0, raise_ramp_rate=None, unit_initial_conditions=None, ramp_rate_curves=None, generating_bids=None, lower_control_rate=None, start_up_cost_curves=None, spin_reserve_ramp=None, generating_unit=None, lower_ramp_rate=None, raise_control_rate=None, **kw_args):
        """ Initialises a new 'RegisteredGenerator' instance.
        """
        # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve

        # High limit for secondary (AGC) control 
        self.high_control_limit = high_control_limit

        # This is the maximum operating MW limit the dispatcher can enter for this unit 
        self.maximum_operating_mw = maximum_operating_mw

        # Low limit for secondary (AGC) control 
        self.low_control_limit = low_control_limit

        # This is the minimum operating MW limit the dispatcher can enter for this unit. 
        self.minimum_operating_mw = minimum_operating_mw


        self.raise_ramp_rate = raise_ramp_rate

        self._unit_initial_conditions = []
        if unit_initial_conditions is not None:
            self.unit_initial_conditions = unit_initial_conditions
        else:
            self.unit_initial_conditions = []

        self._ramp_rate_curves = []
        if ramp_rate_curves is not None:
            self.ramp_rate_curves = ramp_rate_curves
        else:
            self.ramp_rate_curves = []

        self._generating_bids = []
        if generating_bids is not None:
            self.generating_bids = generating_bids
        else:
            self.generating_bids = []

        self.lower_control_rate = lower_control_rate

        self._start_up_cost_curves = []
        if start_up_cost_curves is not None:
            self.start_up_cost_curves = start_up_cost_curves
        else:
            self.start_up_cost_curves = []

        self.spin_reserve_ramp = spin_reserve_ramp

        self._generating_unit = None
        self.generating_unit = generating_unit

        self.lower_ramp_rate = lower_ramp_rate

        self.raise_control_rate = raise_control_rate


        super(RegisteredGenerator, self).__init__(**kw_args)
    # >>> registered_generator

    # <<< raise_ramp_rate
    # @generated
    raise_ramp_rate = None
    # >>> raise_ramp_rate

    # <<< unit_initial_conditions
    # @generated
    def get_unit_initial_conditions(self):
        """ 
        """
        return self._unit_initial_conditions

    def set_unit_initial_conditions(self, value):
        for x in self._unit_initial_conditions:
            x._generating_unit = None
        for y in value:
            y._generating_unit = self
        self._unit_initial_conditions = value

    unit_initial_conditions = property(get_unit_initial_conditions, set_unit_initial_conditions)

    def add_unit_initial_conditions(self, *unit_initial_conditions):
        for obj in unit_initial_conditions:
            obj._generating_unit = self
            self._unit_initial_conditions.append(obj)

    def remove_unit_initial_conditions(self, *unit_initial_conditions):
        for obj in unit_initial_conditions:
            obj._generating_unit = None
            self._unit_initial_conditions.remove(obj)
    # >>> unit_initial_conditions

    # <<< ramp_rate_curves
    # @generated
    def get_ramp_rate_curves(self):
        """ 
        """
        return self._ramp_rate_curves

    def set_ramp_rate_curves(self, value):
        for p in self._ramp_rate_curves:
            filtered = [q for q in p.generating_unit if q != self]
            self._ramp_rate_curves._generating_unit = filtered
        for r in value:
            if self not in r._generating_unit:
                r._generating_unit.append(self)
        self._ramp_rate_curves = value

    ramp_rate_curves = property(get_ramp_rate_curves, set_ramp_rate_curves)

    def add_ramp_rate_curves(self, *ramp_rate_curves):
        for obj in ramp_rate_curves:
            if self not in obj._generating_unit:
                obj._generating_unit.append(self)
            self._ramp_rate_curves.append(obj)

    def remove_ramp_rate_curves(self, *ramp_rate_curves):
        for obj in ramp_rate_curves:
            if self in obj._generating_unit:
                obj._generating_unit.remove(self)
            self._ramp_rate_curves.remove(obj)
    # >>> ramp_rate_curves

    # <<< generating_bids
    # @generated
    def get_generating_bids(self):
        """ 
        """
        return self._generating_bids

    def set_generating_bids(self, value):
        for x in self._generating_bids:
            x._registered_generator = None
        for y in value:
            y._registered_generator = self
        self._generating_bids = value

    generating_bids = property(get_generating_bids, set_generating_bids)

    def add_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._registered_generator = self
            self._generating_bids.append(obj)

    def remove_generating_bids(self, *generating_bids):
        for obj in generating_bids:
            obj._registered_generator = None
            self._generating_bids.remove(obj)
    # >>> generating_bids

    # <<< lower_control_rate
    # @generated
    # Regulation down response rate in MW per minute
    lower_control_rate = None
    # >>> lower_control_rate

    # <<< start_up_cost_curves
    # @generated
    def get_start_up_cost_curves(self):
        """ 
        """
        return self._start_up_cost_curves

    def set_start_up_cost_curves(self, value):
        for p in self._start_up_cost_curves:
            filtered = [q for q in p.registered_generators if q != self]
            self._start_up_cost_curves._registered_generators = filtered
        for r in value:
            if self not in r._registered_generators:
                r._registered_generators.append(self)
        self._start_up_cost_curves = value

    start_up_cost_curves = property(get_start_up_cost_curves, set_start_up_cost_curves)

    def add_start_up_cost_curves(self, *start_up_cost_curves):
        for obj in start_up_cost_curves:
            if self not in obj._registered_generators:
                obj._registered_generators.append(self)
            self._start_up_cost_curves.append(obj)

    def remove_start_up_cost_curves(self, *start_up_cost_curves):
        for obj in start_up_cost_curves:
            if self in obj._registered_generators:
                obj._registered_generators.remove(self)
            self._start_up_cost_curves.remove(obj)
    # >>> start_up_cost_curves

    # <<< spin_reserve_ramp
    # @generated
    spin_reserve_ramp = None
    # >>> spin_reserve_ramp

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ 
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            self._generating_unit._registered_generator = None

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._registered_generator = self

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit

    # <<< lower_ramp_rate
    # @generated
    lower_ramp_rate = None
    # >>> lower_ramp_rate

    # <<< raise_control_rate
    # @generated
    # Regulation up response rate in MW per minute
    raise_control_rate = None
    # >>> raise_control_rate


    def __str__(self):
        """ Returns a string representation of the RegisteredGenerator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< registered_generator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegisteredGenerator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegisteredGenerator", self.uri)
        if format:
            indent += ' ' * depth

        if self.raise_ramp_rate is not None:
            s += '%s<%s:RegisteredGenerator.raise_ramp_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.raise_ramp_rate.uri)
        for obj in self.unit_initial_conditions:
            s += '%s<%s:RegisteredGenerator.unit_initial_conditions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.ramp_rate_curves:
            s += '%s<%s:RegisteredGenerator.ramp_rate_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.generating_bids:
            s += '%s<%s:RegisteredGenerator.generating_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.lower_control_rate is not None:
            s += '%s<%s:RegisteredGenerator.lower_control_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.lower_control_rate.uri)
        for obj in self.start_up_cost_curves:
            s += '%s<%s:RegisteredGenerator.start_up_cost_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.spin_reserve_ramp is not None:
            s += '%s<%s:RegisteredGenerator.spin_reserve_ramp rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.spin_reserve_ramp.uri)
        if self.generating_unit is not None:
            s += '%s<%s:RegisteredGenerator.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        if self.lower_ramp_rate is not None:
            s += '%s<%s:RegisteredGenerator.lower_ramp_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.lower_ramp_rate.uri)
        if self.raise_control_rate is not None:
            s += '%s<%s:RegisteredGenerator.raise_control_rate rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.raise_control_rate.uri)
        s += '%s<%s:RegisteredGenerator.maximum_allowable_spinning_reserve>%s</%s:RegisteredGenerator.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:RegisteredGenerator.high_control_limit>%s</%s:RegisteredGenerator.high_control_limit>' % \
            (indent, ns_prefix, self.high_control_limit, ns_prefix)
        s += '%s<%s:RegisteredGenerator.maximum_operating_mw>%s</%s:RegisteredGenerator.maximum_operating_mw>' % \
            (indent, ns_prefix, self.maximum_operating_mw, ns_prefix)
        s += '%s<%s:RegisteredGenerator.low_control_limit>%s</%s:RegisteredGenerator.low_control_limit>' % \
            (indent, ns_prefix, self.low_control_limit, ns_prefix)
        s += '%s<%s:RegisteredGenerator.minimum_operating_mw>%s</%s:RegisteredGenerator.minimum_operating_mw>' % \
            (indent, ns_prefix, self.minimum_operating_mw, ns_prefix)
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
        for obj in self.meters:
            s += '%s<%s:RegisteredResource.meters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.markets:
            s += '%s<%s:RegisteredResource.markets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resource_groups:
            s += '%s<%s:RegisteredResource.resource_groups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.market_products:
            s += '%s<%s:RegisteredResource.market_products rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:RegisteredResource.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.organisation is not None:
            s += '%s<%s:RegisteredResource.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        s += '%s<%s:RegisteredResource.rto_id>%s</%s:RegisteredResource.rto_id>' % \
            (indent, ns_prefix, self.rto_id, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegisteredGenerator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> registered_generator.serialize


class MarketCaseClearing(MarketFactors):
    """ Market case clearing results are posted for a given settlement period.
    """
    # <<< market_case_clearing
    # @generated
    def __init__(self, modified_date='', posted_date='', case_type='', ancillary_service_clearing=None, **kw_args):
        """ Initialises a new 'MarketCaseClearing' instance.
        """
        # Last time and date clearing results were manually modified. 
        self.modified_date = modified_date

        # Bid clearing results posted time and date. 
        self.posted_date = posted_date

        # Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2' 
        self.case_type = case_type


        self._ancillary_service_clearing = []
        if ancillary_service_clearing is not None:
            self.ancillary_service_clearing = ancillary_service_clearing
        else:
            self.ancillary_service_clearing = []


        super(MarketCaseClearing, self).__init__(**kw_args)
    # >>> market_case_clearing

    # <<< ancillary_service_clearing
    # @generated
    def get_ancillary_service_clearing(self):
        """ 
        """
        return self._ancillary_service_clearing

    def set_ancillary_service_clearing(self, value):
        for x in self._ancillary_service_clearing:
            x._market_case_clearing = None
        for y in value:
            y._market_case_clearing = self
        self._ancillary_service_clearing = value

    ancillary_service_clearing = property(get_ancillary_service_clearing, set_ancillary_service_clearing)

    def add_ancillary_service_clearing(self, *ancillary_service_clearing):
        for obj in ancillary_service_clearing:
            obj._market_case_clearing = self
            self._ancillary_service_clearing.append(obj)

    def remove_ancillary_service_clearing(self, *ancillary_service_clearing):
        for obj in ancillary_service_clearing:
            obj._market_case_clearing = None
            self._ancillary_service_clearing.remove(obj)
    # >>> ancillary_service_clearing


    def __str__(self):
        """ Returns a string representation of the MarketCaseClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_case_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketCaseClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketCaseClearing", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.ancillary_service_clearing:
            s += '%s<%s:MarketCaseClearing.ancillary_service_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:MarketCaseClearing.modified_date>%s</%s:MarketCaseClearing.modified_date>' % \
            (indent, ns_prefix, self.modified_date, ns_prefix)
        s += '%s<%s:MarketCaseClearing.posted_date>%s</%s:MarketCaseClearing.posted_date>' % \
            (indent, ns_prefix, self.posted_date, ns_prefix)
        s += '%s<%s:MarketCaseClearing.case_type>%s</%s:MarketCaseClearing.case_type>' % \
            (indent, ns_prefix, self.case_type, ns_prefix)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketCaseClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_case_clearing.serialize


class RegisteredLoad(RegisteredResource):
    # <<< registered_load
    # @generated
    def __init__(self, load_area=None, load_bids=None, **kw_args):
        """ Initialises a new 'RegisteredLoad' instance.
        """

        self._load_area = None
        self.load_area = load_area

        self._load_bids = []
        if load_bids is not None:
            self.load_bids = load_bids
        else:
            self.load_bids = []


        super(RegisteredLoad, self).__init__(**kw_args)
    # >>> registered_load

    # <<< load_area
    # @generated
    def get_load_area(self):
        """ 
        """
        return self._load_area

    def set_load_area(self, value):
        if self._load_area is not None:
            filtered = [x for x in self.load_area.registered_loads if x != self]
            self._load_area._registered_loads = filtered

        self._load_area = value
        if self._load_area is not None:
            self._load_area._registered_loads.append(self)

    load_area = property(get_load_area, set_load_area)
    # >>> load_area

    # <<< load_bids
    # @generated
    def get_load_bids(self):
        """ 
        """
        return self._load_bids

    def set_load_bids(self, value):
        for x in self._load_bids:
            x._registered_load = None
        for y in value:
            y._registered_load = self
        self._load_bids = value

    load_bids = property(get_load_bids, set_load_bids)

    def add_load_bids(self, *load_bids):
        for obj in load_bids:
            obj._registered_load = self
            self._load_bids.append(obj)

    def remove_load_bids(self, *load_bids):
        for obj in load_bids:
            obj._registered_load = None
            self._load_bids.remove(obj)
    # >>> load_bids


    def __str__(self):
        """ Returns a string representation of the RegisteredLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< registered_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegisteredLoad.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegisteredLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_area is not None:
            s += '%s<%s:RegisteredLoad.load_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_area.uri)
        for obj in self.load_bids:
            s += '%s<%s:RegisteredLoad.load_bids rdf:resource="#%s"/>' % \
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
        for obj in self.meters:
            s += '%s<%s:RegisteredResource.meters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.markets:
            s += '%s<%s:RegisteredResource.markets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.resource_groups:
            s += '%s<%s:RegisteredResource.resource_groups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.market_products:
            s += '%s<%s:RegisteredResource.market_products rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:RegisteredResource.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.organisation is not None:
            s += '%s<%s:RegisteredResource.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        s += '%s<%s:RegisteredResource.rto_id>%s</%s:RegisteredResource.rto_id>' % \
            (indent, ns_prefix, self.rto_id, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegisteredLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> registered_load.serialize


class AncillaryServiceClearing(MarketFactors):
    """ Ancillary services clearing results are posted for a given settlement period.
    """
    # <<< ancillary_service_clearing
    # @generated
    def __init__(self, cleared_mw=0.0, mcp=0.0, commodity_type='', market_case_clearing=None, **kw_args):
        """ Initialises a new 'AncillaryServiceClearing' instance.
        """
        # Cleared MWs. 
        self.cleared_mw = cleared_mw

        # Market clearing price (MCP) in monetary units. 
        self.mcp = mcp

        # Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve 
        self.commodity_type = commodity_type


        self._market_case_clearing = None
        self.market_case_clearing = market_case_clearing


        super(AncillaryServiceClearing, self).__init__(**kw_args)
    # >>> ancillary_service_clearing

    # <<< market_case_clearing
    # @generated
    def get_market_case_clearing(self):
        """ 
        """
        return self._market_case_clearing

    def set_market_case_clearing(self, value):
        if self._market_case_clearing is not None:
            filtered = [x for x in self.market_case_clearing.ancillary_service_clearing if x != self]
            self._market_case_clearing._ancillary_service_clearing = filtered

        self._market_case_clearing = value
        if self._market_case_clearing is not None:
            self._market_case_clearing._ancillary_service_clearing.append(self)

    market_case_clearing = property(get_market_case_clearing, set_market_case_clearing)
    # >>> market_case_clearing


    def __str__(self):
        """ Returns a string representation of the AncillaryServiceClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ancillary_service_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AncillaryServiceClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AncillaryServiceClearing", self.uri)
        if format:
            indent += ' ' * depth

        if self.market_case_clearing is not None:
            s += '%s<%s:AncillaryServiceClearing.market_case_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market_case_clearing.uri)
        s += '%s<%s:AncillaryServiceClearing.cleared_mw>%s</%s:AncillaryServiceClearing.cleared_mw>' % \
            (indent, ns_prefix, self.cleared_mw, ns_prefix)
        s += '%s<%s:AncillaryServiceClearing.mcp>%s</%s:AncillaryServiceClearing.mcp>' % \
            (indent, ns_prefix, self.mcp, ns_prefix)
        s += '%s<%s:AncillaryServiceClearing.commodity_type>%s</%s:AncillaryServiceClearing.commodity_type>' % \
            (indent, ns_prefix, self.commodity_type, ns_prefix)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AncillaryServiceClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ancillary_service_clearing.serialize


class NodeConstraintTerm(ConstraintTerm):
    """ To be used only to constrain a quantity that cannot be associated with a terminal. For example, a registered generating unit that is not electrically connected to the network.
    """
    # <<< node_constraint_term
    # @generated
    def __init__(self, connectivity_node=None, **kw_args):
        """ Initialises a new 'NodeConstraintTerm' instance.
        """

        self._connectivity_node = None
        self.connectivity_node = connectivity_node


        super(NodeConstraintTerm, self).__init__(**kw_args)
    # >>> node_constraint_term

    # <<< connectivity_node
    # @generated
    def get_connectivity_node(self):
        """ 
        """
        return self._connectivity_node

    def set_connectivity_node(self, value):
        if self._connectivity_node is not None:
            filtered = [x for x in self.connectivity_node.node_constraint_terms if x != self]
            self._connectivity_node._node_constraint_terms = filtered

        self._connectivity_node = value
        if self._connectivity_node is not None:
            self._connectivity_node._node_constraint_terms.append(self)

    connectivity_node = property(get_connectivity_node, set_connectivity_node)
    # >>> connectivity_node


    def __str__(self):
        """ Returns a string representation of the NodeConstraintTerm.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< node_constraint_term.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NodeConstraintTerm.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NodeConstraintTerm", self.uri)
        if format:
            indent += ' ' * depth

        if self.connectivity_node is not None:
            s += '%s<%s:NodeConstraintTerm.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node.uri)
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
        if self.security_constraint_sum is not None:
            s += '%s<%s:ConstraintTerm.security_constraint_sum rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.security_constraint_sum.uri)
        s += '%s<%s:ConstraintTerm.factor>%s</%s:ConstraintTerm.factor>' % \
            (indent, ns_prefix, self.factor, ns_prefix)
        s += '%s<%s:ConstraintTerm.function>%s</%s:ConstraintTerm.function>' % \
            (indent, ns_prefix, self.function, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NodeConstraintTerm")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> node_constraint_term.serialize


class ProductBidClearing(MarketFactors):
    """ Product Bid clearing results posted for a given settlement period.
    """
    # <<< product_bid_clearing
    # @generated
    def __init__(self, cleared_mw=0.0, product_bids=None, **kw_args):
        """ Initialises a new 'ProductBidClearing' instance.
        """
        # Cleared MWs. 
        self.cleared_mw = cleared_mw


        self._product_bids = []
        if product_bids is not None:
            self.product_bids = product_bids
        else:
            self.product_bids = []


        super(ProductBidClearing, self).__init__(**kw_args)
    # >>> product_bid_clearing

    # <<< product_bids
    # @generated
    def get_product_bids(self):
        """ 
        """
        return self._product_bids

    def set_product_bids(self, value):
        for x in self._product_bids:
            x._product_bid_clearing = None
        for y in value:
            y._product_bid_clearing = self
        self._product_bids = value

    product_bids = property(get_product_bids, set_product_bids)

    def add_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._product_bid_clearing = self
            self._product_bids.append(obj)

    def remove_product_bids(self, *product_bids):
        for obj in product_bids:
            obj._product_bid_clearing = None
            self._product_bids.remove(obj)
    # >>> product_bids


    def __str__(self):
        """ Returns a string representation of the ProductBidClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< product_bid_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProductBidClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProductBidClearing", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.product_bids:
            s += '%s<%s:ProductBidClearing.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProductBidClearing.cleared_mw>%s</%s:ProductBidClearing.cleared_mw>' % \
            (indent, ns_prefix, self.cleared_mw, ns_prefix)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProductBidClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> product_bid_clearing.serialize


class TransactionBid(Bid):
    """ Bilateral or scheduled transactions for energy and ancillary services considered by market clearing process
    """
    # <<< transaction_bid
    # @generated
    def __init__(self, delivery_pnode=None, receipt_pnode=None, energy_trans_id=None, energy_profiles=None, **kw_args):
        """ Initialises a new 'TransactionBid' instance.
        """

        self._delivery_pnode = None
        self.delivery_pnode = delivery_pnode

        self._receipt_pnode = None
        self.receipt_pnode = receipt_pnode

        self._energy_trans_id = None
        self.energy_trans_id = energy_trans_id

        self._energy_profiles = []
        if energy_profiles is not None:
            self.energy_profiles = energy_profiles
        else:
            self.energy_profiles = []


        super(TransactionBid, self).__init__(**kw_args)
    # >>> transaction_bid

    # <<< delivery_pnode
    # @generated
    def get_delivery_pnode(self):
        """ 
        """
        return self._delivery_pnode

    def set_delivery_pnode(self, value):
        if self._delivery_pnode is not None:
            filtered = [x for x in self.delivery_pnode.delivery_transaction_bids if x != self]
            self._delivery_pnode._delivery_transaction_bids = filtered

        self._delivery_pnode = value
        if self._delivery_pnode is not None:
            self._delivery_pnode._delivery_transaction_bids.append(self)

    delivery_pnode = property(get_delivery_pnode, set_delivery_pnode)
    # >>> delivery_pnode

    # <<< receipt_pnode
    # @generated
    def get_receipt_pnode(self):
        """ 
        """
        return self._receipt_pnode

    def set_receipt_pnode(self, value):
        if self._receipt_pnode is not None:
            filtered = [x for x in self.receipt_pnode.receipt_transaction_bids if x != self]
            self._receipt_pnode._receipt_transaction_bids = filtered

        self._receipt_pnode = value
        if self._receipt_pnode is not None:
            self._receipt_pnode._receipt_transaction_bids.append(self)

    receipt_pnode = property(get_receipt_pnode, set_receipt_pnode)
    # >>> receipt_pnode

    # <<< energy_trans_id
    # @generated
    def get_energy_trans_id(self):
        """ 
        """
        return self._energy_trans_id

    def set_energy_trans_id(self, value):
        if self._energy_trans_id is not None:
            filtered = [x for x in self.energy_trans_id.energy_trans_id if x != self]
            self._energy_trans_id._energy_trans_id = filtered

        self._energy_trans_id = value
        if self._energy_trans_id is not None:
            self._energy_trans_id._energy_trans_id.append(self)

    energy_trans_id = property(get_energy_trans_id, set_energy_trans_id)
    # >>> energy_trans_id

    # <<< energy_profiles
    # @generated
    def get_energy_profiles(self):
        """ 
        """
        return self._energy_profiles

    def set_energy_profiles(self, value):
        for x in self._energy_profiles:
            x._transaction_bid = None
        for y in value:
            y._transaction_bid = self
        self._energy_profiles = value

    energy_profiles = property(get_energy_profiles, set_energy_profiles)

    def add_energy_profiles(self, *energy_profiles):
        for obj in energy_profiles:
            obj._transaction_bid = self
            self._energy_profiles.append(obj)

    def remove_energy_profiles(self, *energy_profiles):
        for obj in energy_profiles:
            obj._transaction_bid = None
            self._energy_profiles.remove(obj)
    # >>> energy_profiles


    def __str__(self):
        """ Returns a string representation of the TransactionBid.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transaction_bid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransactionBid.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransactionBid", self.uri)
        if format:
            indent += ' ' * depth

        if self.delivery_pnode is not None:
            s += '%s<%s:TransactionBid.delivery_pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.delivery_pnode.uri)
        if self.receipt_pnode is not None:
            s += '%s<%s:TransactionBid.receipt_pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.receipt_pnode.uri)
        if self.energy_trans_id is not None:
            s += '%s<%s:TransactionBid.energy_trans_id rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_trans_id.uri)
        for obj in self.energy_profiles:
            s += '%s<%s:TransactionBid.energy_profiles rdf:resource="#%s"/>' % \
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
        if self.market is not None:
            s += '%s<%s:Bid.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        for obj in self.product_bids:
            s += '%s<%s:Bid.product_bids rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.bid_clearing is not None:
            s += '%s<%s:Bid.bid_clearing rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bid_clearing.uri)
        s += '%s<%s:Bid.stop_time>%s</%s:Bid.stop_time>' % \
            (indent, ns_prefix, self.stop_time, ns_prefix)
        s += '%s<%s:Bid.start_time>%s</%s:Bid.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:Bid.market_type>%s</%s:Bid.market_type>' % \
            (indent, ns_prefix, self.market_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransactionBid")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transaction_bid.serialize


class SecurityConstraintsClearing(MarketFactors):
    """ Binding security constrained clearing results posted for a given settlement period.
    """
    # <<< security_constraints_clearing
    # @generated
    def __init__(self, mw_limit=0.0, mw_flow=0.0, shadow_price=0.0, **kw_args):
        """ Initialises a new 'SecurityConstraintsClearing' instance.
        """
        # Binding MW limit. 
        self.mw_limit = mw_limit

        # Optimal MW flow 
        self.mw_flow = mw_flow

        # Security constraint shadow price. 
        self.shadow_price = shadow_price



        super(SecurityConstraintsClearing, self).__init__(**kw_args)
    # >>> security_constraints_clearing


    def __str__(self):
        """ Returns a string representation of the SecurityConstraintsClearing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< security_constraints_clearing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SecurityConstraintsClearing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SecurityConstraintsClearing", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:SecurityConstraintsClearing.mw_limit>%s</%s:SecurityConstraintsClearing.mw_limit>' % \
            (indent, ns_prefix, self.mw_limit, ns_prefix)
        s += '%s<%s:SecurityConstraintsClearing.mw_flow>%s</%s:SecurityConstraintsClearing.mw_flow>' % \
            (indent, ns_prefix, self.mw_flow, ns_prefix)
        s += '%s<%s:SecurityConstraintsClearing.shadow_price>%s</%s:SecurityConstraintsClearing.shadow_price>' % \
            (indent, ns_prefix, self.shadow_price, ns_prefix)
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SecurityConstraintsClearing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> security_constraints_clearing.serialize


class SecurityConstraintSum(MarketFactors):
    """ Typically provided by RTO systems, constraints identified in both base case and critical contingency cases have to be transferred. A constraint has N (>=1) constraint terms. A term is represented by an instance of TerminalConstraintTerm.  The constraint expression is: minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue where: - cn is ConstraintTerm.factor  - xn is the flow at the terminal Flow into the associated equipment is positive for the purpose of ConnectivityNode NodeConstraintTerm  k is SecurityConstraintsLinear.resourceMW The units of k are assumed to be same as the units of the flows, xn.  The constants, cn, are dimensionless. With these conventions, cn and k are all positive for a typical constraint such as 'weighted sum of generation must be less than limit'. Furthermore, cn are all 1.0 for a case such as 'interface flow must be less than limit', assuming the terminals are chosen on the importing side of the interface.
    """
    # <<< security_constraint_sum
    # @generated
    def __init__(self, default_constraint_limit=None, constraint_terms=None, rto=None, base_case_constraint_limit=None, contingency_constraint_limits=None, **kw_args):
        """ Initialises a new 'SecurityConstraintSum' instance.
        """

        self._default_constraint_limit = None
        self.default_constraint_limit = default_constraint_limit

        self._constraint_terms = []
        if constraint_terms is not None:
            self.constraint_terms = constraint_terms
        else:
            self.constraint_terms = []

        self._rto = None
        self.rto = rto

        self._base_case_constraint_limit = None
        self.base_case_constraint_limit = base_case_constraint_limit

        self._contingency_constraint_limits = []
        if contingency_constraint_limits is not None:
            self.contingency_constraint_limits = contingency_constraint_limits
        else:
            self.contingency_constraint_limits = []


        super(SecurityConstraintSum, self).__init__(**kw_args)
    # >>> security_constraint_sum

    # <<< default_constraint_limit
    # @generated
    def get_default_constraint_limit(self):
        """ 
        """
        return self._default_constraint_limit

    def set_default_constraint_limit(self, value):
        if self._default_constraint_limit is not None:
            self._default_constraint_limit._security_constraint_sum = None

        self._default_constraint_limit = value
        if self._default_constraint_limit is not None:
            self._default_constraint_limit._security_constraint_sum = self

    default_constraint_limit = property(get_default_constraint_limit, set_default_constraint_limit)
    # >>> default_constraint_limit

    # <<< constraint_terms
    # @generated
    def get_constraint_terms(self):
        """ 
        """
        return self._constraint_terms

    def set_constraint_terms(self, value):
        for x in self._constraint_terms:
            x._security_constraint_sum = None
        for y in value:
            y._security_constraint_sum = self
        self._constraint_terms = value

    constraint_terms = property(get_constraint_terms, set_constraint_terms)

    def add_constraint_terms(self, *constraint_terms):
        for obj in constraint_terms:
            obj._security_constraint_sum = self
            self._constraint_terms.append(obj)

    def remove_constraint_terms(self, *constraint_terms):
        for obj in constraint_terms:
            obj._security_constraint_sum = None
            self._constraint_terms.remove(obj)
    # >>> constraint_terms

    # <<< rto
    # @generated
    def get_rto(self):
        """ 
        """
        return self._rto

    def set_rto(self, value):
        if self._rto is not None:
            filtered = [x for x in self.rto.security_constraints_linear if x != self]
            self._rto._security_constraints_linear = filtered

        self._rto = value
        if self._rto is not None:
            self._rto._security_constraints_linear.append(self)

    rto = property(get_rto, set_rto)
    # >>> rto

    # <<< base_case_constraint_limit
    # @generated
    def get_base_case_constraint_limit(self):
        """ 
        """
        return self._base_case_constraint_limit

    def set_base_case_constraint_limit(self, value):
        if self._base_case_constraint_limit is not None:
            self._base_case_constraint_limit._security_constraint_sum = None

        self._base_case_constraint_limit = value
        if self._base_case_constraint_limit is not None:
            self._base_case_constraint_limit._security_constraint_sum = self

    base_case_constraint_limit = property(get_base_case_constraint_limit, set_base_case_constraint_limit)
    # >>> base_case_constraint_limit

    # <<< contingency_constraint_limits
    # @generated
    def get_contingency_constraint_limits(self):
        """ 
        """
        return self._contingency_constraint_limits

    def set_contingency_constraint_limits(self, value):
        for x in self._contingency_constraint_limits:
            x._security_constraint_sum = None
        for y in value:
            y._security_constraint_sum = self
        self._contingency_constraint_limits = value

    contingency_constraint_limits = property(get_contingency_constraint_limits, set_contingency_constraint_limits)

    def add_contingency_constraint_limits(self, *contingency_constraint_limits):
        for obj in contingency_constraint_limits:
            obj._security_constraint_sum = self
            self._contingency_constraint_limits.append(obj)

    def remove_contingency_constraint_limits(self, *contingency_constraint_limits):
        for obj in contingency_constraint_limits:
            obj._security_constraint_sum = None
            self._contingency_constraint_limits.remove(obj)
    # >>> contingency_constraint_limits


    def __str__(self):
        """ Returns a string representation of the SecurityConstraintSum.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< security_constraint_sum.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SecurityConstraintSum.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SecurityConstraintSum", self.uri)
        if format:
            indent += ' ' * depth

        if self.default_constraint_limit is not None:
            s += '%s<%s:SecurityConstraintSum.default_constraint_limit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.default_constraint_limit.uri)
        for obj in self.constraint_terms:
            s += '%s<%s:SecurityConstraintSum.constraint_terms rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.rto is not None:
            s += '%s<%s:SecurityConstraintSum.rto rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rto.uri)
        if self.base_case_constraint_limit is not None:
            s += '%s<%s:SecurityConstraintSum.base_case_constraint_limit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_case_constraint_limit.uri)
        for obj in self.contingency_constraint_limits:
            s += '%s<%s:SecurityConstraintSum.contingency_constraint_limits rdf:resource="#%s"/>' % \
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
        for obj in self.erp_invoices:
            s += '%s<%s:MarketFactors.erp_invoices rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.market is not None:
            s += '%s<%s:MarketFactors.market rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.market.uri)
        s += '%s<%s:MarketFactors.interval_start_time>%s</%s:MarketFactors.interval_start_time>' % \
            (indent, ns_prefix, self.interval_start_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SecurityConstraintSum")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> security_constraint_sum.serialize


# <<< market_operations
# @generated
# >>> market_operations
