# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Common.Document import Document

class CustomerBillingInfo(Document):
    """The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """

    def __init__(self, kind='separateEssUdc', pymtPlanType='', billingDate='', pymtPlanAmt=0.0, outBalance=0.0, lastPaymentAmt=0.0, lastPaymentDate='', dueDate='', ErpInvoiceLineItems=None, CustomerAccount=None, *args, **kw_args):
        """Initializes a new 'CustomerBillingInfo' instance.

        @param kind: Kind of bill customer receives. Values are: "separateEssUdc", "other", "consolidatedEss", "consolidatedUdc"
        @param pymtPlanType: Type of payment plan. 
        @param billingDate: Business date designated for the billing run which produced this CustomerBillingInfo. 
        @param pymtPlanAmt: Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        @param outBalance: Outstanding balance on the CustomerAccount as of the statement date. 
        @param lastPaymentAmt: Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param lastPaymentDate: Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param dueDate: Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        @param ErpInvoiceLineItems:
        @param CustomerAccount:
        """
        #: Kind of bill customer receives. Values are: "separateEssUdc", "other", "consolidatedEss", "consolidatedUdc"
        self.kind = kind

        #: Type of payment plan. 
        self.pymtPlanType = pymtPlanType

        #: Business date designated for the billing run which produced this CustomerBillingInfo. 
        self.billingDate = billingDate

        #: Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        self.pymtPlanAmt = pymtPlanAmt

        #: Outstanding balance on the CustomerAccount as of the statement date. 
        self.outBalance = outBalance

        #: Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.lastPaymentAmt = lastPaymentAmt

        #: Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.lastPaymentDate = lastPaymentDate

        #: Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        self.dueDate = dueDate

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        super(CustomerBillingInfo, self).__init__(*args, **kw_args)

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for p in self._ErpInvoiceLineItems:
            filtered = [q for q in p.CustomerBillingInfos if q != self]
            self._ErpInvoiceLineItems._CustomerBillingInfos = filtered
        for r in value:
            if self not in r._CustomerBillingInfos:
                r._CustomerBillingInfos.append(self)
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self not in obj._CustomerBillingInfos:
                obj._CustomerBillingInfos.append(self)
            self._ErpInvoiceLineItems.append(obj)

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self in obj._CustomerBillingInfos:
                obj._CustomerBillingInfos.remove(self)
            self._ErpInvoiceLineItems.remove(obj)

    def getCustomerAccount(self):
        
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.CustomerBillingInfos if x != self]
            self._CustomerAccount._CustomerBillingInfos = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            self._CustomerAccount._CustomerBillingInfos.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

