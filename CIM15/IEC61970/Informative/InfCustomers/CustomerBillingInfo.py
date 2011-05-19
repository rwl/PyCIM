# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Common.Document import Document

class CustomerBillingInfo(Document):
    """The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """

    def __init__(self, pymtPlanType='', kind="consolidatedUdc", pymtPlanAmt=0.0, lastPaymentAmt=0.0, dueDate='', outBalance=0.0, lastPaymentDate='', billingDate='', ErpInvoiceLineItems=None, CustomerAccount=None, *args, **kw_args):
        """Initialises a new 'CustomerBillingInfo' instance.

        @param pymtPlanType: Type of payment plan. 
        @param kind: Kind of bill customer receives. Values are: "consolidatedUdc", "other", "separateEssUdc", "consolidatedEss"
        @param pymtPlanAmt: Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        @param lastPaymentAmt: Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param dueDate: Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        @param outBalance: Outstanding balance on the CustomerAccount as of the statement date. 
        @param lastPaymentDate: Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        @param billingDate: Business date designated for the billing run which produced this CustomerBillingInfo. 
        @param ErpInvoiceLineItems:
        @param CustomerAccount:
        """
        #: Type of payment plan.
        self.pymtPlanType = pymtPlanType

        #: Kind of bill customer receives. Values are: "consolidatedUdc", "other", "separateEssUdc", "consolidatedEss"
        self.kind = kind

        #: Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up.
        self.pymtPlanAmt = pymtPlanAmt

        #: Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
        self.lastPaymentAmt = lastPaymentAmt

        #: Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'.
        self.dueDate = dueDate

        #: Outstanding balance on the CustomerAccount as of the statement date.
        self.outBalance = outBalance

        #: Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
        self.lastPaymentDate = lastPaymentDate

        #: Business date designated for the billing run which produced this CustomerBillingInfo.
        self.billingDate = billingDate

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        super(CustomerBillingInfo, self).__init__(*args, **kw_args)

    _attrs = ["pymtPlanType", "kind", "pymtPlanAmt", "lastPaymentAmt", "dueDate", "outBalance", "lastPaymentDate", "billingDate"]
    _attr_types = {"pymtPlanType": str, "kind": str, "pymtPlanAmt": float, "lastPaymentAmt": float, "dueDate": str, "outBalance": float, "lastPaymentDate": str, "billingDate": str}
    _defaults = {"pymtPlanType": '', "kind": "consolidatedUdc", "pymtPlanAmt": 0.0, "lastPaymentAmt": 0.0, "dueDate": '', "outBalance": 0.0, "lastPaymentDate": '', "billingDate": ''}
    _enums = {"kind": "CustomerBillingKind"}
    _refs = ["ErpInvoiceLineItems", "CustomerAccount"]
    _many_refs = ["ErpInvoiceLineItems"]

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
            if self not in self._CustomerAccount._CustomerBillingInfos:
                self._CustomerAccount._CustomerBillingInfos.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

