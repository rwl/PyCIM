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

"""The package contains portions of the model defined byEnterprise Resource Planning (ERP) standards like those proposed by the Open Applications Group (OAG). It is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (as defined by OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeld 'Erp...' should be associated with the appropriate classes of that standard. In fact, definitions of 'Erp...' classes are based on OAG Nouns to facilitate this process.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Enterprise Resource Planning (ERP) Support Package contains portions of the model defined by ERP standards like those proposed by the Open Applications Group (OAG). This package is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeled 'Erp...' should be associated with the appropriate classes of that standard.'
"""

ns_prefix = "cimInfERPSupport"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfERPSupport"

from CIM14v13.IEC61968.Informative.InfERPSupport.ErpIssueInventory import ErpIssueInventory
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation
from CIM14v13.IEC61968.Informative.InfERPSupport.DocErpPersonRole import DocErpPersonRole
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPayableLineItem import ErpPayableLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.OrgOrgRole import OrgOrgRole
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpReqLineItem import ErpReqLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpLedger import ErpLedger
from CIM14v13.IEC61968.Informative.InfERPSupport.DocOrgRole import DocOrgRole
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpInventory import ErpInventory
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpJournal import ErpJournal
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpProjectAccounting import ErpProjectAccounting
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem import ErpQuoteLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPerson import ErpPerson
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem import ErpRecDelvLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpBankAccount import ErpBankAccount
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPurchaseOrder import ErpPurchaseOrder
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpInvoice import ErpInvoice
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpBomItemData import ErpBomItemData
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpItemMaster import ErpItemMaster
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpInventoryCount import ErpInventoryCount
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpEngChangeOrder import ErpEngChangeOrder
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPayable import ErpPayable
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPayment import ErpPayment
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpQuote import ErpQuote
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPOLineItem import ErpPOLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpReceiveDelivery import ErpReceiveDelivery
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpTimeEntry import ErpTimeEntry
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpChartOfAccounts import ErpChartOfAccounts
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpLedgerBudget import ErpLedgerBudget
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpRequisition import ErpRequisition
from CIM14v13.IEC61968.Informative.InfERPSupport.OrgErpPersonRole import OrgErpPersonRole
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpBOM import ErpBOM
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpTimeSheet import ErpTimeSheet
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpSalesOrder import ErpSalesOrder
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpRecLineItem import ErpRecLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpSiteLevelData import ErpSiteLevelData
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpPersonnel import ErpPersonnel
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpReceivable import ErpReceivable
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpLedgerEntry import ErpLedgerEntry
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpLedBudLineItem import ErpLedBudLineItem
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpTelephoneNumber import ErpTelephoneNumber
from CIM14v13.IEC61968.Informative.InfERPSupport.ErpCompetency import ErpCompetency
