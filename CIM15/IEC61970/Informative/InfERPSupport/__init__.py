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

"""The package contains portions of the model defined byEnterprise Resource Planning (ERP) standards like those proposed by the Open Applications Group (OAG). It is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (as defined by OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeld 'Erp...' should be associated with the appropriate classes of that standard. In fact, definitions of 'Erp...' classes are based on OAG Nouns to facilitate this process.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Enterprise Resource Planning (ERP) Support Package contains portions of the model defined by ERP standards like those proposed by the Open Applications Group (OAG). This package is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeled 'Erp...' should be associated with the appropriate classes of that standard.'
"""

from CIM15.IEC61970.Informative.InfERPSupport.ErpRecDelvLineItem import ErpRecDelvLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpLedgerBudget import ErpLedgerBudget
from CIM15.IEC61970.Informative.InfERPSupport.ErpTimeEntry import ErpTimeEntry
from CIM15.IEC61970.Informative.InfERPSupport.ErpCompetency import ErpCompetency
from CIM15.IEC61970.Informative.InfERPSupport.ErpPurchaseOrder import ErpPurchaseOrder
from CIM15.IEC61970.Informative.InfERPSupport.ErpEngChangeOrder import ErpEngChangeOrder
from CIM15.IEC61970.Informative.InfERPSupport.ErpProjectAccounting import ErpProjectAccounting
from CIM15.IEC61970.Informative.InfERPSupport.ErpRecLineItem import ErpRecLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpPayableLineItem import ErpPayableLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpLedBudLineItem import ErpLedBudLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpRequisition import ErpRequisition
from CIM15.IEC61970.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation
from CIM15.IEC61970.Informative.InfERPSupport.ErpInvoice import ErpInvoice
from CIM15.IEC61970.Informative.InfERPSupport.DocErpPersonRole import DocErpPersonRole
from CIM15.IEC61970.Informative.InfERPSupport.ErpBankAccount import ErpBankAccount
from CIM15.IEC61970.Informative.InfERPSupport.ErpQuote import ErpQuote
from CIM15.IEC61970.Informative.InfERPSupport.ErpPerson import ErpPerson
from CIM15.IEC61970.Informative.InfERPSupport.ErpItemMaster import ErpItemMaster
from CIM15.IEC61970.Informative.InfERPSupport.ErpBOM import ErpBOM
from CIM15.IEC61970.Informative.InfERPSupport.ErpInventoryCount import ErpInventoryCount
from CIM15.IEC61970.Informative.InfERPSupport.ErpIssueInventory import ErpIssueInventory
from CIM15.IEC61970.Informative.InfERPSupport.ErpPayable import ErpPayable
from CIM15.IEC61970.Informative.InfERPSupport.ErpLedger import ErpLedger
from CIM15.IEC61970.Informative.InfERPSupport.ErpPOLineItem import ErpPOLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpLedgerEntry import ErpLedgerEntry
from CIM15.IEC61970.Informative.InfERPSupport.ErpPayment import ErpPayment
from CIM15.IEC61970.Informative.InfERPSupport.ErpReceivable import ErpReceivable
from CIM15.IEC61970.Informative.InfERPSupport.DocOrgRole import DocOrgRole
from CIM15.IEC61970.Informative.InfERPSupport.ErpReqLineItem import ErpReqLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpTimeSheet import ErpTimeSheet
from CIM15.IEC61970.Informative.InfERPSupport.ErpInventory import ErpInventory
from CIM15.IEC61970.Informative.InfERPSupport.ErpChartOfAccounts import ErpChartOfAccounts
from CIM15.IEC61970.Informative.InfERPSupport.ErpSiteLevelData import ErpSiteLevelData
from CIM15.IEC61970.Informative.InfERPSupport.OrgErpPersonRole import OrgErpPersonRole
from CIM15.IEC61970.Informative.InfERPSupport.ErpReceiveDelivery import ErpReceiveDelivery
from CIM15.IEC61970.Informative.InfERPSupport.ErpSalesOrder import ErpSalesOrder
from CIM15.IEC61970.Informative.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from CIM15.IEC61970.Informative.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from CIM15.IEC61970.Informative.InfERPSupport.OrgOrgRole import OrgOrgRole
from CIM15.IEC61970.Informative.InfERPSupport.ErpJournal import ErpJournal
from CIM15.IEC61970.Informative.InfERPSupport.ErpPersonnel import ErpPersonnel
from CIM15.IEC61970.Informative.InfERPSupport.ErpQuoteLineItem import ErpQuoteLineItem
from CIM15.IEC61970.Informative.InfERPSupport.ErpBomItemData import ErpBomItemData

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfERPSupport"
nsPrefix = "cimInfERPSupport"


class ErpInvoiceLineItemKind(str):
    """Values are: other, recalculation, initial
    """
    pass

class ErpInvoiceKind(str):
    """Values are: sales, purchase
    """
    pass

class ErpAccountKind(str):
    """Values are: normal, estimate, statistical, reversal
    """
    pass

class BillMediaKind(str):
    """Values are: other, paper, electronic
    """
    pass
