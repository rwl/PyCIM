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

""" The package is used to define detailed customer models.
"""

from cim14v13.iec61968.common import Agreement
from cim14v13.iec61968.common import Document
from cim14v13.iec61970.core import Curve

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfCustomers"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfCustomers"

class ExternalCustomerAgreement(Agreement):
    """ A type of customer agreement involving an external agency. For example, a customer may form a contracts with an Energy Service Supplier if Direct Access is permitted.
    """
    pass
    # <<< external_customer_agreement
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExternalCustomerAgreement' instance.

        """


        super(ExternalCustomerAgreement, self).__init__(*args, **kw_args)
    # >>> external_customer_agreement



class StandardIndustryCode(Document):
    """ The Standard Industrial Classification (SIC) are the codes that identify the type of products/service an industry is involved in, and used for statutory reporting purposes. For example, in the USA these codes are located by the federal government, and then published in a book entitled 'The Standard Industrial Classification Manual'. The codes are arranged in a hierarchical structure. Note that Residential Service Agreements are not classified according to the SIC codes.
    """
    # <<< standard_industry_code
    # @generated
    def __init__(self, code='', customer_agreements=None, *args, **kw_args):
        """ Initialises a new 'StandardIndustryCode' instance.

        @param code: Standard alphanumeric code assigned to a particular product/service within an industry. 
        @param customer_agreements:
        """
        # Standard alphanumeric code assigned to a particular product/service within an industry. 
        self.code = code


        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []


        super(StandardIndustryCode, self).__init__(*args, **kw_args)
    # >>> standard_industry_code

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ 
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._standard_industry_code = None
        for y in value:
            y._standard_industry_code = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._standard_industry_code = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._standard_industry_code = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements



class CustomerBillingInfo(Document):
    """ The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """
    # <<< customer_billing_info
    # @generated
    def __init__(self, kind='separate_ess_udc', pymt_plan_type='', billing_date='', pymt_plan_amt=0.0, out_balance=0.0, last_payment_amt=0.0, last_payment_date='', due_date='', erp_invoice_line_items=None, customer_account=None, *args, **kw_args):
        """ Initialises a new 'CustomerBillingInfo' instance.

        @param kind: Kind of bill customer receives. Values are: "separate_ess_udc", "other", "consolidated_ess", "consolidated_udc"
        @param pymt_plan_type: Type of payment plan. 
        @param billing_date: Business date designated for the billing run which produced this CustomerBillingInfo. 
        @param pymt_plan_amt: Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        @param out_balance: Outstanding balance on the CustomerAccount as of the statement date. 
        @param last_payment_amt: Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param last_payment_date: Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param due_date: Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        @param erp_invoice_line_items:
        @param customer_account:
        """
        # Kind of bill customer receives. Values are: "separate_ess_udc", "other", "consolidated_ess", "consolidated_udc"
        self.kind = kind

        # Type of payment plan. 
        self.pymt_plan_type = pymt_plan_type

        # Business date designated for the billing run which produced this CustomerBillingInfo. 
        self.billing_date = billing_date

        # Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        self.pymt_plan_amt = pymt_plan_amt

        # Outstanding balance on the CustomerAccount as of the statement date. 
        self.out_balance = out_balance

        # Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.last_payment_amt = last_payment_amt

        # Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.last_payment_date = last_payment_date

        # Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        self.due_date = due_date


        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []

        self._customer_account = None
        self.customer_account = customer_account


        super(CustomerBillingInfo, self).__init__(*args, **kw_args)
    # >>> customer_billing_info

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for p in self._erp_invoice_line_items:
            filtered = [q for q in p.customer_billing_infos if q != self]
            self._erp_invoice_line_items._customer_billing_infos = filtered
        for r in value:
            if self not in r._customer_billing_infos:
                r._customer_billing_infos.append(self)
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self not in obj._customer_billing_infos:
                obj._customer_billing_infos.append(self)
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self in obj._customer_billing_infos:
                obj._customer_billing_infos.remove(self)
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ 
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.customer_billing_infos if x != self]
            self._customer_account._customer_billing_infos = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._customer_billing_infos.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account



class OutageHistory(Document):
    """ A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """
    # <<< outage_history
    # @generated
    def __init__(self, outage_reports=None, *args, **kw_args):
        """ Initialises a new 'OutageHistory' instance.

        @param outage_reports: OutageReports per customer for which this OutageHistory is created.
        """

        self._outage_reports = []
        if outage_reports is not None:
            self.outage_reports = outage_reports
        else:
            self.outage_reports = []


        super(OutageHistory, self).__init__(*args, **kw_args)
    # >>> outage_history

    # <<< outage_reports
    # @generated
    def get_outage_reports(self):
        """ OutageReports per customer for which this OutageHistory is created.
        """
        return self._outage_reports

    def set_outage_reports(self, value):
        for x in self._outage_reports:
            x._outage_history = None
        for y in value:
            y._outage_history = self
        self._outage_reports = value

    outage_reports = property(get_outage_reports, set_outage_reports)

    def add_outage_reports(self, *outage_reports):
        for obj in outage_reports:
            obj._outage_history = self
            self._outage_reports.append(obj)

    def remove_outage_reports(self, *outage_reports):
        for obj in outage_reports:
            obj._outage_history = None
            self._outage_reports.remove(obj)
    # >>> outage_reports



class WorkBillingInfo(Document):
    """ Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """
    # <<< work_billing_info
    # @generated
    def __init__(self, due_date_time='', received_date_time='', deposit=0.0, work_price=0.0, discount=0.0, cost_estimate=0.0, issue_date_time='', erp_line_items=None, customer_account=None, works=None, *args, **kw_args):
        """ Initialises a new 'WorkBillingInfo' instance.

        @param due_date_time: Date and time by which payment for bill is expected from client. 
        @param received_date_time: Date payment was received from client. 
        @param deposit: Amount of price on deposit. 
        @param work_price: Amount of bill. 
        @param discount: Discount from standard price. 
        @param cost_estimate: Estimated cost for work. 
        @param issue_date_time: Date and time bill was issued to client. 
        @param erp_line_items:
        @param customer_account:
        @param works:
        """
        # Date and time by which payment for bill is expected from client. 
        self.due_date_time = due_date_time

        # Date payment was received from client. 
        self.received_date_time = received_date_time

        # Amount of price on deposit. 
        self.deposit = deposit

        # Amount of bill. 
        self.work_price = work_price

        # Discount from standard price. 
        self.discount = discount

        # Estimated cost for work. 
        self.cost_estimate = cost_estimate

        # Date and time bill was issued to client. 
        self.issue_date_time = issue_date_time


        self._erp_line_items = []
        if erp_line_items is not None:
            self.erp_line_items = erp_line_items
        else:
            self.erp_line_items = []

        self._customer_account = None
        self.customer_account = customer_account

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []


        super(WorkBillingInfo, self).__init__(*args, **kw_args)
    # >>> work_billing_info

    # <<< erp_line_items
    # @generated
    def get_erp_line_items(self):
        """ 
        """
        return self._erp_line_items

    def set_erp_line_items(self, value):
        for p in self._erp_line_items:
            filtered = [q for q in p.work_billing_infos if q != self]
            self._erp_line_items._work_billing_infos = filtered
        for r in value:
            if self not in r._work_billing_infos:
                r._work_billing_infos.append(self)
        self._erp_line_items = value

    erp_line_items = property(get_erp_line_items, set_erp_line_items)

    def add_erp_line_items(self, *erp_line_items):
        for obj in erp_line_items:
            if self not in obj._work_billing_infos:
                obj._work_billing_infos.append(self)
            self._erp_line_items.append(obj)

    def remove_erp_line_items(self, *erp_line_items):
        for obj in erp_line_items:
            if self in obj._work_billing_infos:
                obj._work_billing_infos.remove(self)
            self._erp_line_items.remove(obj)
    # >>> erp_line_items

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ 
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.work_billing_infos if x != self]
            self._customer_account._work_billing_infos = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._work_billing_infos.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._work_billing_info = None
        for y in value:
            y._work_billing_info = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._work_billing_info = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._work_billing_info = None
            self._works.remove(obj)
    # >>> works



class PowerQualityPricing(Document):
    """ Pricing can be based on power quality.
    """
    # <<< power_quality_pricing
    # @generated
    def __init__(self, emergency_low_volt_limit=0.0, emergency_high_volt_limit=0.0, volt_limit_viol_cost=0.0, value_uninterrupted_service_p=0.0, normal_low_volt_limit=0.0, volt_imbalance_viol_cost=0.0, normal_high_volt_limit=0.0, power_factor_min=0.0, value_uninterrupted_service_energy=0.0, pricing_structure=None, service_delivery_points=None, *args, **kw_args):
        """ Initialises a new 'PowerQualityPricing' instance.

        @param emergency_low_volt_limit: Emergency low voltage limit. 
        @param emergency_high_volt_limit: Emergency high voltage limit. 
        @param volt_limit_viol_cost: Voltage limit violation cost (Cost per unit Voltage). 
        @param value_uninterrupted_service_p: Value of uninterrupted service (Cost per active power). 
        @param normal_low_volt_limit: Normal low voltage limit. 
        @param volt_imbalance_viol_cost: Voltage imbalance violation cost (Cost per unit Voltage). 
        @param normal_high_volt_limit: Normal high voltage limit. 
        @param power_factor_min: Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here. 
        @param value_uninterrupted_service_energy: Value of uninterrupted service (Cost per energy). 
        @param pricing_structure:
        @param service_delivery_points:
        """
        # Emergency low voltage limit. 
        self.emergency_low_volt_limit = emergency_low_volt_limit

        # Emergency high voltage limit. 
        self.emergency_high_volt_limit = emergency_high_volt_limit

        # Voltage limit violation cost (Cost per unit Voltage). 
        self.volt_limit_viol_cost = volt_limit_viol_cost

        # Value of uninterrupted service (Cost per active power). 
        self.value_uninterrupted_service_p = value_uninterrupted_service_p

        # Normal low voltage limit. 
        self.normal_low_volt_limit = normal_low_volt_limit

        # Voltage imbalance violation cost (Cost per unit Voltage). 
        self.volt_imbalance_viol_cost = volt_imbalance_viol_cost

        # Normal high voltage limit. 
        self.normal_high_volt_limit = normal_high_volt_limit

        # Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here. 
        self.power_factor_min = power_factor_min

        # Value of uninterrupted service (Cost per energy). 
        self.value_uninterrupted_service_energy = value_uninterrupted_service_energy


        self._pricing_structure = None
        self.pricing_structure = pricing_structure

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []


        super(PowerQualityPricing, self).__init__(*args, **kw_args)
    # >>> power_quality_pricing

    # <<< pricing_structure
    # @generated
    def get_pricing_structure(self):
        """ 
        """
        return self._pricing_structure

    def set_pricing_structure(self, value):
        if self._pricing_structure is not None:
            filtered = [x for x in self.pricing_structure.power_quality_pricings if x != self]
            self._pricing_structure._power_quality_pricings = filtered

        self._pricing_structure = value
        if self._pricing_structure is not None:
            self._pricing_structure._power_quality_pricings.append(self)

    pricing_structure = property(get_pricing_structure, set_pricing_structure)
    # >>> pricing_structure

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ 
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for p in self._service_delivery_points:
            filtered = [q for q in p.power_quality_pricings if q != self]
            self._service_delivery_points._power_quality_pricings = filtered
        for r in value:
            if self not in r._power_quality_pricings:
                r._power_quality_pricings.append(self)
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self not in obj._power_quality_pricings:
                obj._power_quality_pricings.append(self)
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self in obj._power_quality_pricings:
                obj._power_quality_pricings.remove(self)
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points



class ServiceGuarantee(Document):
    """ A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """
    # <<< service_guarantee
    # @generated
    def __init__(self, automatic_pay=False, service_requirement='', pay_amount=0.0, application_period=None, *args, **kw_args):
        """ Initialises a new 'ServiceGuarantee' instance.

        @param automatic_pay: True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment. 
        @param service_requirement: Explanation of the requirement and conditions for satisfying it. 
        @param pay_amount: Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'. 
        @param application_period: Period in which this service guantee applies.
        """
        # True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment. 
        self.automatic_pay = automatic_pay

        # Explanation of the requirement and conditions for satisfying it. 
        self.service_requirement = service_requirement

        # Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'. 
        self.pay_amount = pay_amount


        self.application_period = application_period


        super(ServiceGuarantee, self).__init__(*args, **kw_args)
    # >>> service_guarantee

    # <<< application_period
    # @generated
    # Period in which this service guantee applies.
    application_period = None
    # >>> application_period



class SubscribePowerCurve(Curve):
    """ Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.
    """
    # <<< subscribe_power_curve
    # @generated
    def __init__(self, pricing_structure=None, *args, **kw_args):
        """ Initialises a new 'SubscribePowerCurve' instance.

        @param pricing_structure:
        """

        self._pricing_structure = None
        self.pricing_structure = pricing_structure


        super(SubscribePowerCurve, self).__init__(*args, **kw_args)
    # >>> subscribe_power_curve

    # <<< pricing_structure
    # @generated
    def get_pricing_structure(self):
        """ 
        """
        return self._pricing_structure

    def set_pricing_structure(self, value):
        if self._pricing_structure is not None:
            self._pricing_structure._subscribe_power_curve = None

        self._pricing_structure = value
        if self._pricing_structure is not None:
            self._pricing_structure._subscribe_power_curve = self

    pricing_structure = property(get_pricing_structure, set_pricing_structure)
    # >>> pricing_structure



# <<< inf_customers
# @generated
# >>> inf_customers
