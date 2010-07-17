#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

""" Defines TreeNodes interface for the model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu \
    import Action, Menu

from CIM import *
from CIM.IEC61968 import *
from CIM.IEC61970 import *
from CIM.PackageDependencies import *
from CIM.IEC61968.Informative import *
from CIM.IEC61968.Common import *
from CIM.IEC61968.Assets import *
from CIM.IEC61968.AssetModels import *
from CIM.IEC61968.PaymentMetering import *
from CIM.IEC61968.Metering import *
from CIM.IEC61968.Work import *
from CIM.IEC61968.Customers import *
from CIM.IEC61968.WiresExt import *
from CIM.IEC61968.LoadControl import *
from CIM.IEC61968.Informative.InfPaymentMetering import *
from CIM.IEC61968.Informative.InfERPSupport import *
from CIM.IEC61968.Informative.InfLocations import *
from CIM.IEC61968.Informative.InfWork import *
from CIM.IEC61968.Informative.Financial import *
from CIM.IEC61968.Informative.InfAssets import *
from CIM.IEC61968.Informative.InfAssetModels import *
from CIM.IEC61968.Informative.EnergyScheduling import *
from CIM.IEC61968.Informative.InfCommon import *
from CIM.IEC61968.Informative.MarketOperations import *
from CIM.IEC61968.Informative.InfGMLSupport import *
from CIM.IEC61968.Informative.InfOperations import *
from CIM.IEC61968.Informative.InfTypeAsset import *
from CIM.IEC61968.Informative.Reservation import *
from CIM.IEC61968.Informative.InfCustomers import *
from CIM.IEC61968.Informative.InfLoadControl import *
from CIM.IEC61968.Informative.InfMetering import *
from CIM.IEC61970.Core import *
from CIM.IEC61970.Wires import *
from CIM.IEC61970.OperationalLimits import *
from CIM.IEC61970.StateVariables import *
from CIM.IEC61970.Meas import *
from CIM.IEC61970.Generation import *
from CIM.IEC61970.SCADA import *
from CIM.IEC61970.LoadModel import *
from CIM.IEC61970.Domain import *
from CIM.IEC61970.Contingency import *
from CIM.IEC61970.ControlArea import *
from CIM.IEC61970.Equivalents import *
from CIM.IEC61970.Outage import *
from CIM.IEC61970.Protection import *
from CIM.IEC61970.Topology import *
from CIM.IEC61970.Generation.Production import *
from CIM.IEC61970.Generation.GenerationDynamics import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------
# <<< constants
# @generated
IMAGE_PATH = ""
# >>> constants

#------------------------------------------------------------------------------
#  Tree nodes:
#------------------------------------------------------------------------------

CombinedVersion_TreeNode = TreeNode(
    node_for=[CombinedVersion],
        tooltip="The combined version denotes the versions of the subpackages that have been combined into the total CIIMmodel. This is a convenience instead of having to look at each subpackage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PowerROCPerMin_TreeNode = TreeNode(
    node_for=[PowerROCPerMin],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RateOfChange_TreeNode = TreeNode(
    node_for=[RateOfChange],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnumeratedType_TreeNode = TreeNode(
    node_for=[EnumeratedType],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FreqBiasFactor_TreeNode = TreeNode(
    node_for=[FreqBiasFactor],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FlowgateIdcType_TreeNode = TreeNode(
    node_for=[FlowgateIdcType],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Quantity_TreeNode = TreeNode(
    node_for=[Quantity],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergyAsMWh_TreeNode = TreeNode(
    node_for=[EnergyAsMWh],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FlowgateAfcUseCode_TreeNode = TreeNode(
    node_for=[FlowgateAfcUseCode],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PenaltyFactor_TreeNode = TreeNode(
    node_for=[PenaltyFactor],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Element_TreeNode = TreeNode(
    node_for=[Element],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Model_TreeNode = TreeNode(
    node_for=[Model],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Model_Elements_TreeNode = TreeNode(
    node_for=[Model],
    children="Elements",
    label="=Elements",
    tooltip="",
    add=[Element],
    move=[Element],
    icon_path=IMAGE_PATH)

IEC61968CIMVersion_TreeNode = TreeNode(
    node_for=[IEC61968CIMVersion],
        tooltip="IEC 61968 version number assigned to this UML model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReceiptSummary_TreeNode = TreeNode(
    node_for=[ReceiptSummary],
        tooltip="Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BankStatement_TreeNode = TreeNode(
    node_for=[BankStatement],
    label="name",
    tooltip="A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TSPAgreement_TreeNode = TreeNode(
    node_for=[TSPAgreement],
    label="name",
    tooltip="A contractual agreement between a supplier (utility) and a transaction service provider (a type of organisation) that governs the terms and conditions, under which authorisation the transaction service provider may process transactions on behalf of the supplier.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransactionSummary_TreeNode = TreeNode(
    node_for=[TransactionSummary],
        tooltip="The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Bank_TreeNode = TreeNode(
    node_for=[Bank],
    label="name",
    tooltip="Organisation that is a commercial bank, agency, or other institution that offers a similar service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Bank_BankAccounts_TreeNode = TreeNode(
    node_for=[Bank],
    children="BankAccounts",
    label="=BankAccounts",
    tooltip="All BankAccounts this Bank provides.",
    add=[BankAccount],
    move=[BankAccount],
    icon_path=IMAGE_PATH)

SDPAccountingFunction_TreeNode = TreeNode(
    node_for=[SDPAccountingFunction],
    label="name",
    tooltip="Service delivery point accounting function, particularly for payment meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SDPAccountingFunction_ChargeRegisters_TreeNode = TreeNode(
    node_for=[SDPAccountingFunction],
    children="ChargeRegisters",
    label="=ChargeRegisters",
    tooltip="",
    add=[ChargeRegister],
    move=[ChargeRegister],
    icon_path=IMAGE_PATH)
SDPAccountingFunction_CreditRegisters_TreeNode = TreeNode(
    node_for=[SDPAccountingFunction],
    children="CreditRegisters",
    label="=CreditRegisters",
    tooltip="",
    add=[CreditRegister],
    move=[CreditRegister],
    icon_path=IMAGE_PATH)

CreditRegister_TreeNode = TreeNode(
    node_for=[CreditRegister],
    label="name",
    tooltip="Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Token_TreeNode = TreeNode(
    node_for=[Token],
    label="name",
    tooltip="The token that is transferred to the payment meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ChargeRegister_TreeNode = TreeNode(
    node_for=[ChargeRegister],
    label="name",
    tooltip="Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpIssueInventory_TreeNode = TreeNode(
    node_for=[ErpIssueInventory],
    label="name",
    tooltip="Can be used to request an application to process an issue or request information about an issue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpOrganisation_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    label="name",
    tooltip="Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpOrganisation_DocumentRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="DocumentRoles",
    label="=DocumentRoles",
    tooltip="",
    add=[DocOrgRole],
    move=[DocOrgRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_ActivityRecords_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ActivityRecords",
    label="=ActivityRecords",
    tooltip="",
    add=[ActivityRecord],
    move=[ActivityRecord],
    icon_path=IMAGE_PATH)
ErpOrganisation_LocationRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="LocationRoles",
    label="=LocationRoles",
    tooltip="",
    add=[OrgLocRole],
    move=[OrgLocRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_ErpPersonRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ErpPersonRoles",
    label="=ErpPersonRoles",
    tooltip="",
    add=[OrgErpPersonRole],
    move=[OrgErpPersonRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_ViolationLimits_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ViolationLimits",
    label="=ViolationLimits",
    tooltip="",
    add=[ViolationLimit],
    move=[ViolationLimit],
    icon_path=IMAGE_PATH)
ErpOrganisation_Requests_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="Requests",
    label="=Requests",
    tooltip="",
    add=[Request],
    move=[Request],
    icon_path=IMAGE_PATH)
ErpOrganisation_ChangeItems_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
ErpOrganisation_IntSchedAgreement_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="IntSchedAgreement",
    label="=IntSchedAgreement",
    tooltip="",
    add=[IntSchedAgreement],
    move=[IntSchedAgreement],
    icon_path=IMAGE_PATH)
ErpOrganisation_RegisteredResources_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="RegisteredResources",
    label="=RegisteredResources",
    tooltip="",
    add=[RegisteredResource],
    move=[RegisteredResource],
    icon_path=IMAGE_PATH)
ErpOrganisation_PowerSystemResourceRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="PowerSystemResourceRoles",
    label="=PowerSystemResourceRoles",
    tooltip="",
    add=[OrgPsrRole],
    move=[OrgPsrRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_AssetRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="AssetRoles",
    label="=AssetRoles",
    tooltip="",
    add=[OrgAssetRole],
    move=[OrgAssetRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_LandPropertyRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="LandPropertyRoles",
    label="=LandPropertyRoles",
    tooltip="",
    add=[OrgPropertyRole],
    move=[OrgPropertyRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_ParentOrganisationRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ParentOrganisationRoles",
    label="=ParentOrganisationRoles",
    tooltip="",
    add=[OrgOrgRole],
    move=[OrgOrgRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_ChildOrganisationRoles_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="ChildOrganisationRoles",
    label="=ChildOrganisationRoles",
    tooltip="",
    add=[OrgOrgRole],
    move=[OrgOrgRole],
    icon_path=IMAGE_PATH)
ErpOrganisation_Crews_TreeNode = TreeNode(
    node_for=[ErpOrganisation],
    children="Crews",
    label="=Crews",
    tooltip="",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)

DocErpPersonRole_TreeNode = TreeNode(
    node_for=[DocErpPersonRole],
    label="name",
    tooltip="Roles played between Persons and Documents.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpPayableLineItem_TreeNode = TreeNode(
    node_for=[ErpPayableLineItem],
    label="name",
    tooltip="Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as credit memos.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPayableLineItem_ErpJournalEntries_TreeNode = TreeNode(
    node_for=[ErpPayableLineItem],
    children="ErpJournalEntries",
    label="=ErpJournalEntries",
    tooltip="",
    add=[ErpJournalEntry],
    move=[ErpJournalEntry],
    icon_path=IMAGE_PATH)
ErpPayableLineItem_ErpPayments_TreeNode = TreeNode(
    node_for=[ErpPayableLineItem],
    children="ErpPayments",
    label="=ErpPayments",
    tooltip="",
    add=[ErpPayment],
    move=[ErpPayment],
    icon_path=IMAGE_PATH)

OrgOrgRole_TreeNode = TreeNode(
    node_for=[OrgOrgRole],
    label="name",
    tooltip="Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpReqLineItem_TreeNode = TreeNode(
    node_for=[ErpReqLineItem],
    label="name",
    tooltip="Information that describes a requested item and its attributes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpLedger_TreeNode = TreeNode(
    node_for=[ErpLedger],
    label="name",
    tooltip="In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpLedger_ErpLedgerEntries_TreeNode = TreeNode(
    node_for=[ErpLedger],
    children="ErpLedgerEntries",
    label="=ErpLedgerEntries",
    tooltip="",
    add=[ErpLedgerEntry],
    move=[ErpLedgerEntry],
    icon_path=IMAGE_PATH)

DocOrgRole_TreeNode = TreeNode(
    node_for=[DocOrgRole],
    label="name",
    tooltip="Roles played between Organisations and Documents.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpInventory_TreeNode = TreeNode(
    node_for=[ErpInventory],
    label="name",
    tooltip="Utility inventory-related information about an item or part (and not for description of the item and its attributes). It is used by ERP applications to enable the synchronization of Inventory data that exists on separate Item Master databases. This data is not the master data that describes the attributes of the item such as dimensions, weight, or unit of measure - it describes the item as it exists at a specific location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpJournal_TreeNode = TreeNode(
    node_for=[ErpJournal],
    label="name",
    tooltip="Book for recording accounting transactions as they occur. Transactions and adjustments are first recorded in a journal, which is like a diary of instructions, advising which account to be charged and by how much. A journal represents a change in the balances of a business's financial accounts. Many tasks or transactions throughout an enterprise will result in the creation of a journal. Some examples are creating a customer invoice, paying a vendor, transferring inventory, or paying employees.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpJournal_ErpJournalEntries_TreeNode = TreeNode(
    node_for=[ErpJournal],
    children="ErpJournalEntries",
    label="=ErpJournalEntries",
    tooltip="",
    add=[ErpJournalEntry],
    move=[ErpJournalEntry],
    icon_path=IMAGE_PATH)

ErpProjectAccounting_TreeNode = TreeNode(
    node_for=[ErpProjectAccounting],
    label="name",
    tooltip="Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpProjectAccounting_Projects_TreeNode = TreeNode(
    node_for=[ErpProjectAccounting],
    children="Projects",
    label="=Projects",
    tooltip="",
    add=[Project],
    move=[Project],
    icon_path=IMAGE_PATH)
ErpProjectAccounting_WorkCostDetails_TreeNode = TreeNode(
    node_for=[ErpProjectAccounting],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)
ErpProjectAccounting_Works_TreeNode = TreeNode(
    node_for=[ErpProjectAccounting],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)
ErpProjectAccounting_ErpTimeEntries_TreeNode = TreeNode(
    node_for=[ErpProjectAccounting],
    children="ErpTimeEntries",
    label="=ErpTimeEntries",
    tooltip="",
    add=[ErpTimeEntry],
    move=[ErpTimeEntry],
    icon_path=IMAGE_PATH)

ErpQuoteLineItem_TreeNode = TreeNode(
    node_for=[ErpQuoteLineItem],
    label="name",
    tooltip="Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpPerson_TreeNode = TreeNode(
    node_for=[ErpPerson],
    label="name",
    tooltip="General purpose information for name and other information to contact people.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPerson_ErpTelephoneNumbers_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="ErpTelephoneNumbers",
    label="=ErpTelephoneNumbers",
    tooltip="",
    add=[ErpTelephoneNumber],
    move=[ErpTelephoneNumber],
    icon_path=IMAGE_PATH)
ErpPerson_DocumentRoles_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="DocumentRoles",
    label="=DocumentRoles",
    tooltip="",
    add=[DocErpPersonRole],
    move=[DocErpPersonRole],
    icon_path=IMAGE_PATH)
ErpPerson_ElectronicAddresses_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="ElectronicAddresses",
    label="=ElectronicAddresses",
    tooltip="",
    add=[ElectronicAddress],
    move=[ElectronicAddress],
    icon_path=IMAGE_PATH)
ErpPerson_Crews_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="Crews",
    label="=Crews",
    tooltip="All Crews to which this ErpPerson belongs.",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)
ErpPerson_Appointments_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="Appointments",
    label="=Appointments",
    tooltip="",
    add=[Appointment],
    move=[Appointment],
    icon_path=IMAGE_PATH)
ErpPerson_LaborItems_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="LaborItems",
    label="=LaborItems",
    tooltip="",
    add=[LaborItem],
    move=[LaborItem],
    icon_path=IMAGE_PATH)
ErpPerson_MeasurementValues_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="MeasurementValues",
    label="=MeasurementValues",
    tooltip="",
    add=[MeasurementValue],
    move=[MeasurementValue],
    icon_path=IMAGE_PATH)
ErpPerson_CallBacks_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="CallBacks",
    label="=CallBacks",
    tooltip="",
    add=[CallBack],
    move=[CallBack],
    icon_path=IMAGE_PATH)
ErpPerson_ActivityRecords_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="ActivityRecords",
    label="=ActivityRecords",
    tooltip="",
    add=[ActivityRecord],
    move=[ActivityRecord],
    icon_path=IMAGE_PATH)
ErpPerson_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[OrgErpPersonRole],
    move=[OrgErpPersonRole],
    icon_path=IMAGE_PATH)
ErpPerson_Crafts_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="Crafts",
    label="=Crafts",
    tooltip="",
    add=[Craft],
    move=[Craft],
    icon_path=IMAGE_PATH)
ErpPerson_LocationRoles_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="LocationRoles",
    label="=LocationRoles",
    tooltip="",
    add=[ErpPersonLocRole],
    move=[ErpPersonLocRole],
    icon_path=IMAGE_PATH)
ErpPerson_Skills_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="Skills",
    label="=Skills",
    tooltip="",
    add=[Skill],
    move=[Skill],
    icon_path=IMAGE_PATH)
ErpPerson_ChangeItems_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
ErpPerson_SwitchingStepRoles_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="SwitchingStepRoles",
    label="=SwitchingStepRoles",
    tooltip="",
    add=[ErpPersonScheduleStepRole],
    move=[ErpPersonScheduleStepRole],
    icon_path=IMAGE_PATH)
ErpPerson_LandPropertyRoles_TreeNode = TreeNode(
    node_for=[ErpPerson],
    children="LandPropertyRoles",
    label="=LandPropertyRoles",
    tooltip="",
    add=[PersonPropertyRole],
    move=[PersonPropertyRole],
    icon_path=IMAGE_PATH)

ErpRecDelvLineItem_TreeNode = TreeNode(
    node_for=[ErpRecDelvLineItem],
    label="name",
    tooltip="Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpRecDelvLineItem_MaterialItems_TreeNode = TreeNode(
    node_for=[ErpRecDelvLineItem],
    children="MaterialItems",
    label="=MaterialItems",
    tooltip="",
    add=[MaterialItem],
    move=[MaterialItem],
    icon_path=IMAGE_PATH)
ErpRecDelvLineItem_Assets_TreeNode = TreeNode(
    node_for=[ErpRecDelvLineItem],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)

ErpBankAccount_TreeNode = TreeNode(
    node_for=[ErpBankAccount],
    label="name",
    tooltip="Relationship under a particular name, usually evidenced by a deposit against which withdrawals can be made. Types of bank accounts include: demand, time, custodial, joint, trustee, corporate, special, and regular accounts. A statement of transactions during a fiscal period and the resulting balance is maintained on each account. For Payment metering, the account is associated with Bank and Supplier, reflecting details of the bank account used for depositing revenue collected by TokenVendor. The name of the account holder should be specified in 'name' attribute.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpPurchaseOrder_TreeNode = TreeNode(
    node_for=[ErpPurchaseOrder],
    label="name",
    tooltip="A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPurchaseOrder_ErpPOLineItems_TreeNode = TreeNode(
    node_for=[ErpPurchaseOrder],
    children="ErpPOLineItems",
    label="=ErpPOLineItems",
    tooltip="",
    add=[ErpPOLineItem],
    move=[ErpPOLineItem],
    icon_path=IMAGE_PATH)

ErpInvoice_TreeNode = TreeNode(
    node_for=[ErpInvoice],
    label="name",
    tooltip="A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpInvoice_ErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[ErpInvoice],
    children="ErpInvoiceLineItems",
    label="=ErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)

ErpBomItemData_TreeNode = TreeNode(
    node_for=[ErpBomItemData],
    label="name",
    tooltip="An individual item on a bill of materials.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpItemMaster_TreeNode = TreeNode(
    node_for=[ErpItemMaster],
    label="name",
    tooltip="Any unique purchased part for manufactured product tracked by ERP systems for a utility. Item, as used by the OAG, refers to the basic information about an item, including its attributes, cost, and locations. It does not include item quantities. Compare to the Inventory, which includes all quantities and other location-specific information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpInventoryCount_TreeNode = TreeNode(
    node_for=[ErpInventoryCount],
    label="name",
    tooltip="This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpEngChangeOrder_TreeNode = TreeNode(
    node_for=[ErpEngChangeOrder],
    label="name",
    tooltip="General Utility Engineering Change Order information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpInvoiceLineItem_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    label="name",
    tooltip="An individual line item on an invoice.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpInvoiceLineItem_WorkBillingInfos_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="WorkBillingInfos",
    label="=WorkBillingInfos",
    tooltip="",
    add=[WorkBillingInfo],
    move=[WorkBillingInfo],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_MarketFactors_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="MarketFactors",
    label="=MarketFactors",
    tooltip="",
    add=[MarketFactors],
    move=[MarketFactors],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_ErpJournalEntries_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="ErpJournalEntries",
    label="=ErpJournalEntries",
    tooltip="",
    add=[ErpJournalEntry],
    move=[ErpJournalEntry],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_CustomerBillingInfos_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="CustomerBillingInfos",
    label="=CustomerBillingInfos",
    tooltip="Customer billing for services rendered.",
    add=[CustomerBillingInfo],
    move=[CustomerBillingInfo],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_UserAttributes_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_ComponentErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="ComponentErpInvoiceLineItems",
    label="=ComponentErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_ErpPayments_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="ErpPayments",
    label="=ErpPayments",
    tooltip="",
    add=[ErpPayment],
    move=[ErpPayment],
    icon_path=IMAGE_PATH)
ErpInvoiceLineItem_Settlements_TreeNode = TreeNode(
    node_for=[ErpInvoiceLineItem],
    children="Settlements",
    label="=Settlements",
    tooltip="",
    add=[Settlement],
    move=[Settlement],
    icon_path=IMAGE_PATH)

ErpPayable_TreeNode = TreeNode(
    node_for=[ErpPayable],
    label="name",
    tooltip="A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPayable_ContractorItems_TreeNode = TreeNode(
    node_for=[ErpPayable],
    children="ContractorItems",
    label="=ContractorItems",
    tooltip="",
    add=[ContractorItem],
    move=[ContractorItem],
    icon_path=IMAGE_PATH)
ErpPayable_ErpPayableLineItems_TreeNode = TreeNode(
    node_for=[ErpPayable],
    children="ErpPayableLineItems",
    label="=ErpPayableLineItems",
    tooltip="",
    add=[ErpPayableLineItem],
    move=[ErpPayableLineItem],
    icon_path=IMAGE_PATH)

ErpPayment_TreeNode = TreeNode(
    node_for=[ErpPayment],
    label="name",
    tooltip="Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPayment_ErpRecLineItems_TreeNode = TreeNode(
    node_for=[ErpPayment],
    children="ErpRecLineItems",
    label="=ErpRecLineItems",
    tooltip="",
    add=[ErpRecLineItem],
    move=[ErpRecLineItem],
    icon_path=IMAGE_PATH)
ErpPayment_ErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[ErpPayment],
    children="ErpInvoiceLineItems",
    label="=ErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)
ErpPayment_ErpPayableLineItems_TreeNode = TreeNode(
    node_for=[ErpPayment],
    children="ErpPayableLineItems",
    label="=ErpPayableLineItems",
    tooltip="",
    add=[ErpPayableLineItem],
    move=[ErpPayableLineItem],
    icon_path=IMAGE_PATH)

ErpQuote_TreeNode = TreeNode(
    node_for=[ErpQuote],
    label="name",
    tooltip="Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpQuote_ErpQuoteLineItems_TreeNode = TreeNode(
    node_for=[ErpQuote],
    children="ErpQuoteLineItems",
    label="=ErpQuoteLineItems",
    tooltip="",
    add=[ErpQuoteLineItem],
    move=[ErpQuoteLineItem],
    icon_path=IMAGE_PATH)

ErpJournalEntry_TreeNode = TreeNode(
    node_for=[ErpJournalEntry],
    label="name",
    tooltip="Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpJournalEntry_ErpPayableLineItems_TreeNode = TreeNode(
    node_for=[ErpJournalEntry],
    children="ErpPayableLineItems",
    label="=ErpPayableLineItems",
    tooltip="",
    add=[ErpPayableLineItem],
    move=[ErpPayableLineItem],
    icon_path=IMAGE_PATH)
ErpJournalEntry_CostTypes_TreeNode = TreeNode(
    node_for=[ErpJournalEntry],
    children="CostTypes",
    label="=CostTypes",
    tooltip="",
    add=[CostType],
    move=[CostType],
    icon_path=IMAGE_PATH)
ErpJournalEntry_ErpRecLineItems_TreeNode = TreeNode(
    node_for=[ErpJournalEntry],
    children="ErpRecLineItems",
    label="=ErpRecLineItems",
    tooltip="",
    add=[ErpRecLineItem],
    move=[ErpRecLineItem],
    icon_path=IMAGE_PATH)

ErpPOLineItem_TreeNode = TreeNode(
    node_for=[ErpPOLineItem],
    label="name",
    tooltip="Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpReceiveDelivery_TreeNode = TreeNode(
    node_for=[ErpReceiveDelivery],
    label="name",
    tooltip="Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpReceiveDelivery_ErpRecDelvLineItems_TreeNode = TreeNode(
    node_for=[ErpReceiveDelivery],
    children="ErpRecDelvLineItems",
    label="=ErpRecDelvLineItems",
    tooltip="",
    add=[ErpRecDelvLineItem],
    move=[ErpRecDelvLineItem],
    icon_path=IMAGE_PATH)

ErpTimeEntry_TreeNode = TreeNode(
    node_for=[ErpTimeEntry],
    label="name",
    tooltip="An individual entry on an ErpTimeSheet.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpChartOfAccounts_TreeNode = TreeNode(
    node_for=[ErpChartOfAccounts],
    label="name",
    tooltip="Accounting structure of a business. Each account represents a financial aspect of a business, such as its Accounts Payable, or the value of its inventory, or its office supply expenses.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpLedgerBudget_TreeNode = TreeNode(
    node_for=[ErpLedgerBudget],
    label="name",
    tooltip="Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpLedgerBudget_ErpLedBudLineItems_TreeNode = TreeNode(
    node_for=[ErpLedgerBudget],
    children="ErpLedBudLineItems",
    label="=ErpLedBudLineItems",
    tooltip="",
    add=[ErpLedBudLineItem],
    move=[ErpLedBudLineItem],
    icon_path=IMAGE_PATH)

ErpRequisition_TreeNode = TreeNode(
    node_for=[ErpRequisition],
    label="name",
    tooltip="General information that applies to a utility requisition that is a request for the purchase of goods or services. Typically, a requisition leads to the creation of a purchase order to a specific supplier.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpRequisition_ErpReqLineItems_TreeNode = TreeNode(
    node_for=[ErpRequisition],
    children="ErpReqLineItems",
    label="=ErpReqLineItems",
    tooltip="",
    add=[ErpReqLineItem],
    move=[ErpReqLineItem],
    icon_path=IMAGE_PATH)

OrgErpPersonRole_TreeNode = TreeNode(
    node_for=[OrgErpPersonRole],
    label="name",
    tooltip="Roles played between Persons and Organisations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpBOM_TreeNode = TreeNode(
    node_for=[ErpBOM],
    label="name",
    tooltip="Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpBOM_ErpBomItemDatas_TreeNode = TreeNode(
    node_for=[ErpBOM],
    children="ErpBomItemDatas",
    label="=ErpBomItemDatas",
    tooltip="",
    add=[ErpBomItemData],
    move=[ErpBomItemData],
    icon_path=IMAGE_PATH)

ErpTimeSheet_TreeNode = TreeNode(
    node_for=[ErpTimeSheet],
    label="name",
    tooltip="Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpTimeSheet_ErpTimeEntries_TreeNode = TreeNode(
    node_for=[ErpTimeSheet],
    children="ErpTimeEntries",
    label="=ErpTimeEntries",
    tooltip="",
    add=[ErpTimeEntry],
    move=[ErpTimeEntry],
    icon_path=IMAGE_PATH)

ErpSalesOrder_TreeNode = TreeNode(
    node_for=[ErpSalesOrder],
    label="name",
    tooltip="General purpose Sales Order is used for utility service orders, etc. As used by the OAG, the SalesOrder is a step beyond a PurchaseOrder in that the receiving entity of the order also communicates SalesInformoration about the Order along with the Order itself.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpRecLineItem_TreeNode = TreeNode(
    node_for=[ErpRecLineItem],
    label="name",
    tooltip="Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpRecLineItem_ErpPayments_TreeNode = TreeNode(
    node_for=[ErpRecLineItem],
    children="ErpPayments",
    label="=ErpPayments",
    tooltip="",
    add=[ErpPayment],
    move=[ErpPayment],
    icon_path=IMAGE_PATH)
ErpRecLineItem_ErpJournalEntries_TreeNode = TreeNode(
    node_for=[ErpRecLineItem],
    children="ErpJournalEntries",
    label="=ErpJournalEntries",
    tooltip="",
    add=[ErpJournalEntry],
    move=[ErpJournalEntry],
    icon_path=IMAGE_PATH)

ErpSiteLevelData_TreeNode = TreeNode(
    node_for=[ErpSiteLevelData],
    label="name",
    tooltip="For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpPersonnel_TreeNode = TreeNode(
    node_for=[ErpPersonnel],
    label="name",
    tooltip="Information that applies to the basic data about a utility person, used by ERP applications to transfer Personnel data for a worker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpPersonnel_ErpPersons_TreeNode = TreeNode(
    node_for=[ErpPersonnel],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)

ErpReceivable_TreeNode = TreeNode(
    node_for=[ErpReceivable],
    label="name",
    tooltip="Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpReceivable_ErpRecLineItems_TreeNode = TreeNode(
    node_for=[ErpReceivable],
    children="ErpRecLineItems",
    label="=ErpRecLineItems",
    tooltip="",
    add=[ErpRecLineItem],
    move=[ErpRecLineItem],
    icon_path=IMAGE_PATH)

ErpLedgerEntry_TreeNode = TreeNode(
    node_for=[ErpLedgerEntry],
    label="name",
    tooltip="Details of an individual entry in a ledger, which was posted from a journal on the posted date.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpLedgerEntry_UserAttributes_TreeNode = TreeNode(
    node_for=[ErpLedgerEntry],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
ErpLedgerEntry_Settlements_TreeNode = TreeNode(
    node_for=[ErpLedgerEntry],
    children="Settlements",
    label="=Settlements",
    tooltip="",
    add=[Settlement],
    move=[Settlement],
    icon_path=IMAGE_PATH)

ErpLedBudLineItem_TreeNode = TreeNode(
    node_for=[ErpLedBudLineItem],
    label="name",
    tooltip="Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpTelephoneNumber_TreeNode = TreeNode(
    node_for=[ErpTelephoneNumber],
    label="name",
    tooltip="The telephone number for a person or organisation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpTelephoneNumber_ErpPersons_TreeNode = TreeNode(
    node_for=[ErpTelephoneNumber],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)

ErpCompetency_TreeNode = TreeNode(
    node_for=[ErpCompetency],
    label="name",
    tooltip="Information that describes aptitudes of a utility employee. Unlike Skills that an ErpPerson must be certified to perform before undertaking certain type of assignments (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human Resource (HR) matters such as schooling, training, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ErpCompetency_ErpPersons_TreeNode = TreeNode(
    node_for=[ErpCompetency],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)

LocLocRole_TreeNode = TreeNode(
    node_for=[LocLocRole],
    label="name",
    tooltip="The relationship between one Location and another Location. One 'roleType' is 'Directions,' for which an additional attribute serves for providing a textual description for navigating from one location to another location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RightOfWay_TreeNode = TreeNode(
    node_for=[RightOfWay],
    label="name",
    tooltip="A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RightOfWay_LandProperties_TreeNode = TreeNode(
    node_for=[RightOfWay],
    children="LandProperties",
    label="=LandProperties",
    tooltip="All land properties this right of way applies to.",
    add=[LandProperty],
    move=[LandProperty],
    icon_path=IMAGE_PATH)

OrgLocRole_TreeNode = TreeNode(
    node_for=[OrgLocRole],
    label="name",
    tooltip="Roles played between Organisations and Locations, for example a service territory or school district. Note that roles dealing with use of a specific piece of property should be defined based on the relationship between OccupationsOfProperty and Location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OrgPropertyRole_TreeNode = TreeNode(
    node_for=[OrgPropertyRole],
    label="name",
    tooltip="Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OrgPropertyRole_LandProperty_TreeNode = TreeNode(
    node_for=[OrgPropertyRole],
    children="LandProperty",
    label="=LandProperty",
    tooltip="",
    add=[LandProperty],
    move=[LandProperty],
    icon_path=IMAGE_PATH)

AssetLocRole_TreeNode = TreeNode(
    node_for=[AssetLocRole],
    label="name",
    tooltip="Roles played between Assets and Locations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ErpPersonLocRole_TreeNode = TreeNode(
    node_for=[ErpPersonLocRole],
    label="name",
    tooltip="Roles played between People and Locations. Some Locations are somewhat static, like the person's home address. Other may be dynamic, for example when the person is part of a crew driving around in truck.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Route_TreeNode = TreeNode(
    node_for=[Route],
    label="name",
    tooltip="Route that is followed, for example by service crews.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Route_Locations_TreeNode = TreeNode(
    node_for=[Route],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)
Route_Crews_TreeNode = TreeNode(
    node_for=[Route],
    children="Crews",
    label="=Crews",
    tooltip="",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)

Zone_TreeNode = TreeNode(
    node_for=[Zone],
    label="name",
    tooltip="Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DocLocRole_TreeNode = TreeNode(
    node_for=[DocLocRole],
    label="name",
    tooltip="Roles played between Documents and Locations. For example, as ErpAddress is a type of Location and WorkBilling is a type of Document, a role is the address for which to mail the invoice. As a TroubleTicket is a type of Document, one instance of Location may be the address for which the trouble is reported.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SchematicLocation_TreeNode = TreeNode(
    node_for=[SchematicLocation],
    label="name",
    tooltip="Schematic location. Intended to be used in the context of diagrams (worked out by WG13 in 2008 and 2009).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RedLine_TreeNode = TreeNode(
    node_for=[RedLine],
    label="name",
    tooltip="This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RedLine_Locations_TreeNode = TreeNode(
    node_for=[RedLine],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

LocationGrant_TreeNode = TreeNode(
    node_for=[LocationGrant],
    label="name",
    tooltip="A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LandProperty_TreeNode = TreeNode(
    node_for=[LandProperty],
    label="name",
    tooltip="Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LandProperty_LocationGrants_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="LocationGrants",
    label="=LocationGrants",
    tooltip="All location grants this land property has.",
    add=[LocationGrant],
    move=[LocationGrant],
    icon_path=IMAGE_PATH)
LandProperty_AssetContainers_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="AssetContainers",
    label="=AssetContainers",
    tooltip="",
    add=[AssetContainer],
    move=[AssetContainer],
    icon_path=IMAGE_PATH)
LandProperty_ErpSiteLevelDatas_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="ErpSiteLevelDatas",
    label="=ErpSiteLevelDatas",
    tooltip="",
    add=[ErpSiteLevelData],
    move=[ErpSiteLevelData],
    icon_path=IMAGE_PATH)
LandProperty_ErpPersonRoles_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="ErpPersonRoles",
    label="=ErpPersonRoles",
    tooltip="",
    add=[PersonPropertyRole],
    move=[PersonPropertyRole],
    icon_path=IMAGE_PATH)
LandProperty_Locations_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="Locations",
    label="=Locations",
    tooltip="The spatail description of a piece of property.",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)
LandProperty_RightOfWays_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="RightOfWays",
    label="=RightOfWays",
    tooltip="All rights of way this land property has.",
    add=[RightOfWay],
    move=[RightOfWay],
    icon_path=IMAGE_PATH)
LandProperty_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[LandProperty],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[OrgPropertyRole],
    move=[OrgPropertyRole],
    icon_path=IMAGE_PATH)

Hazard_TreeNode = TreeNode(
    node_for=[Hazard],
    label="name",
    tooltip="A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Hazard_Assets_TreeNode = TreeNode(
    node_for=[Hazard],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
Hazard_Locations_TreeNode = TreeNode(
    node_for=[Hazard],
    children="Locations",
    label="=Locations",
    tooltip="The point or polygon location of a given hazard.",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

PersonPropertyRole_TreeNode = TreeNode(
    node_for=[PersonPropertyRole],
    label="name",
    tooltip="The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DesignLocation_TreeNode = TreeNode(
    node_for=[DesignLocation],
    label="name",
    tooltip="A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DesignLocation_MaterialItems_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="MaterialItems",
    label="=MaterialItems",
    tooltip="",
    add=[MaterialItem],
    move=[MaterialItem],
    icon_path=IMAGE_PATH)
DesignLocation_DesignLocationCUs_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="DesignLocationCUs",
    label="=DesignLocationCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)
DesignLocation_Designs_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="Designs",
    label="=Designs",
    tooltip="",
    add=[Design],
    move=[Design],
    icon_path=IMAGE_PATH)
DesignLocation_MiscCostItems_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="MiscCostItems",
    label="=MiscCostItems",
    tooltip="",
    add=[MiscCostItem],
    move=[MiscCostItem],
    icon_path=IMAGE_PATH)
DesignLocation_ConditionFactors_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="ConditionFactors",
    label="=ConditionFactors",
    tooltip="",
    add=[ConditionFactor],
    move=[ConditionFactor],
    icon_path=IMAGE_PATH)
DesignLocation_Diagrams_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="Diagrams",
    label="=Diagrams",
    tooltip="",
    add=[Diagram],
    move=[Diagram],
    icon_path=IMAGE_PATH)
DesignLocation_ErpBomItemDatas_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="ErpBomItemDatas",
    label="=ErpBomItemDatas",
    tooltip="",
    add=[ErpBomItemData],
    move=[ErpBomItemData],
    icon_path=IMAGE_PATH)
DesignLocation_WorkLocations_TreeNode = TreeNode(
    node_for=[DesignLocation],
    children="WorkLocations",
    label="=WorkLocations",
    tooltip="",
    add=[WorkLocation],
    move=[WorkLocation],
    icon_path=IMAGE_PATH)

Capability_TreeNode = TreeNode(
    node_for=[Capability],
    label="name",
    tooltip="Capabilities of a crew.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Capability_WorkTasks_TreeNode = TreeNode(
    node_for=[Capability],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)
Capability_Crafts_TreeNode = TreeNode(
    node_for=[Capability],
    children="Crafts",
    label="=Crafts",
    tooltip="",
    add=[Craft],
    move=[Craft],
    icon_path=IMAGE_PATH)

Design_TreeNode = TreeNode(
    node_for=[Design],
    label="name",
    tooltip="A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Design_DesignLocationsCUs_TreeNode = TreeNode(
    node_for=[Design],
    children="DesignLocationsCUs",
    label="=DesignLocationsCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)
Design_WorkCostDetails_TreeNode = TreeNode(
    node_for=[Design],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)
Design_DesignLocations_TreeNode = TreeNode(
    node_for=[Design],
    children="DesignLocations",
    label="=DesignLocations",
    tooltip="",
    add=[DesignLocation],
    move=[DesignLocation],
    icon_path=IMAGE_PATH)
Design_ErpBOMs_TreeNode = TreeNode(
    node_for=[Design],
    children="ErpBOMs",
    label="=ErpBOMs",
    tooltip="",
    add=[ErpBOM],
    move=[ErpBOM],
    icon_path=IMAGE_PATH)
Design_ConditionFactors_TreeNode = TreeNode(
    node_for=[Design],
    children="ConditionFactors",
    label="=ConditionFactors",
    tooltip="",
    add=[ConditionFactor],
    move=[ConditionFactor],
    icon_path=IMAGE_PATH)
Design_WorkTasks_TreeNode = TreeNode(
    node_for=[Design],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)

LaborItem_TreeNode = TreeNode(
    node_for=[LaborItem],
    label="name",
    tooltip="Labor used for work order.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LaborItem_ErpPersons_TreeNode = TreeNode(
    node_for=[LaborItem],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)

CUMaterialItem_TreeNode = TreeNode(
    node_for=[CUMaterialItem],
    label="name",
    tooltip="Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUMaterialItem_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUMaterialItem],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)
CUMaterialItem_PropertyUnits_TreeNode = TreeNode(
    node_for=[CUMaterialItem],
    children="PropertyUnits",
    label="=PropertyUnits",
    tooltip="",
    add=[PropertyUnit],
    move=[PropertyUnit],
    icon_path=IMAGE_PATH)

NonStandardItem_TreeNode = TreeNode(
    node_for=[NonStandardItem],
    label="name",
    tooltip="This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TypeMaterial_TreeNode = TreeNode(
    node_for=[TypeMaterial],
    label="name",
    tooltip="Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TypeMaterial_ErpReqLineItems_TreeNode = TreeNode(
    node_for=[TypeMaterial],
    children="ErpReqLineItems",
    label="=ErpReqLineItems",
    tooltip="",
    add=[ErpReqLineItem],
    move=[ErpReqLineItem],
    icon_path=IMAGE_PATH)
TypeMaterial_ErpIssueInventories_TreeNode = TreeNode(
    node_for=[TypeMaterial],
    children="ErpIssueInventories",
    label="=ErpIssueInventories",
    tooltip="",
    add=[ErpIssueInventory],
    move=[ErpIssueInventory],
    icon_path=IMAGE_PATH)
TypeMaterial_CUMaterialItems_TreeNode = TreeNode(
    node_for=[TypeMaterial],
    children="CUMaterialItems",
    label="=CUMaterialItems",
    tooltip="",
    add=[CUMaterialItem],
    move=[CUMaterialItem],
    icon_path=IMAGE_PATH)
TypeMaterial_MaterialItems_TreeNode = TreeNode(
    node_for=[TypeMaterial],
    children="MaterialItems",
    label="=MaterialItems",
    tooltip="",
    add=[MaterialItem],
    move=[MaterialItem],
    icon_path=IMAGE_PATH)

Appointment_TreeNode = TreeNode(
    node_for=[Appointment],
    label="name",
    tooltip="Meeting time and location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Appointment_ErpPersons_TreeNode = TreeNode(
    node_for=[Appointment],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)

MaterialItem_TreeNode = TreeNode(
    node_for=[MaterialItem],
    label="name",
    tooltip="The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MaterialItem_Usages_TreeNode = TreeNode(
    node_for=[MaterialItem],
    children="Usages",
    label="=Usages",
    tooltip="",
    add=[Usage],
    move=[Usage],
    icon_path=IMAGE_PATH)
MaterialItem_ErpInventoryCounts_TreeNode = TreeNode(
    node_for=[MaterialItem],
    children="ErpInventoryCounts",
    label="=ErpInventoryCounts",
    tooltip="",
    add=[ErpInventoryCount],
    move=[ErpInventoryCount],
    icon_path=IMAGE_PATH)
MaterialItem_ErpRecDelvLineItems_TreeNode = TreeNode(
    node_for=[MaterialItem],
    children="ErpRecDelvLineItems",
    label="=ErpRecDelvLineItems",
    tooltip="",
    add=[ErpRecDelvLineItem],
    move=[ErpRecDelvLineItem],
    icon_path=IMAGE_PATH)
MaterialItem_ErpPOLineItems_TreeNode = TreeNode(
    node_for=[MaterialItem],
    children="ErpPOLineItems",
    label="=ErpPOLineItems",
    tooltip="",
    add=[ErpPOLineItem],
    move=[ErpPOLineItem],
    icon_path=IMAGE_PATH)

CUContractorItem_TreeNode = TreeNode(
    node_for=[CUContractorItem],
    label="name",
    tooltip="Compatible unit contractor item.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUContractorItem_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUContractorItem],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

CompatibleUnit_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    label="name",
    tooltip="A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompatibleUnit_CUWorkEquipmentItems_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="CUWorkEquipmentItems",
    label="=CUWorkEquipmentItems",
    tooltip="",
    add=[CUWorkEquipmentItem],
    move=[CUWorkEquipmentItem],
    icon_path=IMAGE_PATH)
CompatibleUnit_CUContractorItems_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="CUContractorItems",
    label="=CUContractorItems",
    tooltip="",
    add=[CUContractorItem],
    move=[CUContractorItem],
    icon_path=IMAGE_PATH)
CompatibleUnit_Procedures_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="Procedures",
    label="=Procedures",
    tooltip="",
    add=[Procedure],
    move=[Procedure],
    icon_path=IMAGE_PATH)
CompatibleUnit_CUAssets_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="CUAssets",
    label="=CUAssets",
    tooltip="",
    add=[CUAsset],
    move=[CUAsset],
    icon_path=IMAGE_PATH)
CompatibleUnit_CUMaterialItems_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="CUMaterialItems",
    label="=CUMaterialItems",
    tooltip="",
    add=[CUMaterialItem],
    move=[CUMaterialItem],
    icon_path=IMAGE_PATH)
CompatibleUnit_CULaborItems_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="CULaborItems",
    label="=CULaborItems",
    tooltip="",
    add=[CULaborItem],
    move=[CULaborItem],
    icon_path=IMAGE_PATH)
CompatibleUnit_DesignLocationCUs_TreeNode = TreeNode(
    node_for=[CompatibleUnit],
    children="DesignLocationCUs",
    label="=DesignLocationCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)

InfoQuestion_TreeNode = TreeNode(
    node_for=[InfoQuestion],
    label="name",
    tooltip="Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MaintenanceDataSet_TreeNode = TreeNode(
    node_for=[MaintenanceDataSet],
    label="name",
    tooltip="The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Regulation_TreeNode = TreeNode(
    node_for=[Regulation],
    label="name",
    tooltip="Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Usage_TreeNode = TreeNode(
    node_for=[Usage],
    label="name",
    tooltip="The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AccessPermit_TreeNode = TreeNode(
    node_for=[AccessPermit],
    label="name",
    tooltip="A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WorkStatusEntry_TreeNode = TreeNode(
    node_for=[WorkStatusEntry],
    label="name",
    tooltip="A type of ActivityRecord that records information about the status of an item, such as a Work or WorkTask, at a point in time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WorkTask_TreeNode = TreeNode(
    node_for=[WorkTask],
    label="name",
    tooltip="A set of tasks is required to implement a design.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkTask_ContractorItems_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="ContractorItems",
    label="=ContractorItems",
    tooltip="",
    add=[ContractorItem],
    move=[ContractorItem],
    icon_path=IMAGE_PATH)
WorkTask_Crews_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="Crews",
    label="=Crews",
    tooltip="All Crews participating in this WorkTask.",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)
WorkTask_WorkCostDetails_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)
WorkTask_Usages_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="Usages",
    label="=Usages",
    tooltip="",
    add=[Usage],
    move=[Usage],
    icon_path=IMAGE_PATH)
WorkTask_QualificationRequirements_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="QualificationRequirements",
    label="=QualificationRequirements",
    tooltip="",
    add=[QualificationRequirement],
    move=[QualificationRequirement],
    icon_path=IMAGE_PATH)
WorkTask_LaborItems_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="LaborItems",
    label="=LaborItems",
    tooltip="",
    add=[LaborItem],
    move=[LaborItem],
    icon_path=IMAGE_PATH)
WorkTask_MaterialItems_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="MaterialItems",
    label="=MaterialItems",
    tooltip="",
    add=[MaterialItem],
    move=[MaterialItem],
    icon_path=IMAGE_PATH)
WorkTask_EquipmentItems_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="EquipmentItems",
    label="=EquipmentItems",
    tooltip="",
    add=[EquipmentItem],
    move=[EquipmentItem],
    icon_path=IMAGE_PATH)
WorkTask_DesignLocationCUs_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="DesignLocationCUs",
    label="=DesignLocationCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)
WorkTask_Assets_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
WorkTask_Capabilities_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="Capabilities",
    label="=Capabilities",
    tooltip="",
    add=[Capability],
    move=[Capability],
    icon_path=IMAGE_PATH)
WorkTask_MiscCostItems_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="MiscCostItems",
    label="=MiscCostItems",
    tooltip="",
    add=[MiscCostItem],
    move=[MiscCostItem],
    icon_path=IMAGE_PATH)
WorkTask_SwitchingSchedules_TreeNode = TreeNode(
    node_for=[WorkTask],
    children="SwitchingSchedules",
    label="=SwitchingSchedules",
    tooltip="",
    add=[SwitchingSchedule],
    move=[SwitchingSchedule],
    icon_path=IMAGE_PATH)

Request_TreeNode = TreeNode(
    node_for=[Request],
    label="name",
    tooltip="A request for work, service or project.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Request_Projects_TreeNode = TreeNode(
    node_for=[Request],
    children="Projects",
    label="=Projects",
    tooltip="",
    add=[Project],
    move=[Project],
    icon_path=IMAGE_PATH)
Request_Works_TreeNode = TreeNode(
    node_for=[Request],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)

CUAllowableAction_TreeNode = TreeNode(
    node_for=[CUAllowableAction],
    label="name",
    tooltip="Allowed actions: Install, Remove, Transfer, Abandon, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUAllowableAction_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUAllowableAction],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

Project_TreeNode = TreeNode(
    node_for=[Project],
    label="name",
    tooltip="A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Project_Works_TreeNode = TreeNode(
    node_for=[Project],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)
Project_Requests_TreeNode = TreeNode(
    node_for=[Project],
    children="Requests",
    label="=Requests",
    tooltip="",
    add=[Request],
    move=[Request],
    icon_path=IMAGE_PATH)
Project_SubProjects_TreeNode = TreeNode(
    node_for=[Project],
    children="SubProjects",
    label="=SubProjects",
    tooltip="",
    add=[Project],
    move=[Project],
    icon_path=IMAGE_PATH)

CUAsset_TreeNode = TreeNode(
    node_for=[CUAsset],
    label="name",
    tooltip="Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUAsset_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUAsset],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

PropertyUnit_TreeNode = TreeNode(
    node_for=[PropertyUnit],
    label="name",
    tooltip="Unit of property for reporting purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PropertyUnit_CUMaterialItems_TreeNode = TreeNode(
    node_for=[PropertyUnit],
    children="CUMaterialItems",
    label="=CUMaterialItems",
    tooltip="",
    add=[CUMaterialItem],
    move=[CUMaterialItem],
    icon_path=IMAGE_PATH)
PropertyUnit_CompatibleUnits_TreeNode = TreeNode(
    node_for=[PropertyUnit],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)
PropertyUnit_WorkCostDetails_TreeNode = TreeNode(
    node_for=[PropertyUnit],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)

InspectionDataSet_TreeNode = TreeNode(
    node_for=[InspectionDataSet],
    label="name",
    tooltip="Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

InspectionDataSet_AccordingToSchedules_TreeNode = TreeNode(
    node_for=[InspectionDataSet],
    children="AccordingToSchedules",
    label="=AccordingToSchedules",
    tooltip="",
    add=[ScheduleParameterInfo],
    move=[ScheduleParameterInfo],
    icon_path=IMAGE_PATH)

CostType_TreeNode = TreeNode(
    node_for=[CostType],
    label="name",
    tooltip="A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CostType_WorkCostDetails_TreeNode = TreeNode(
    node_for=[CostType],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)
CostType_ErpJournalEntries_TreeNode = TreeNode(
    node_for=[CostType],
    children="ErpJournalEntries",
    label="=ErpJournalEntries",
    tooltip="",
    add=[ErpJournalEntry],
    move=[ErpJournalEntry],
    icon_path=IMAGE_PATH)
CostType_ChildCostTypes_TreeNode = TreeNode(
    node_for=[CostType],
    children="ChildCostTypes",
    label="=ChildCostTypes",
    tooltip="",
    add=[CostType],
    move=[CostType],
    icon_path=IMAGE_PATH)
CostType_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CostType],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

WorkCostSummary_TreeNode = TreeNode(
    node_for=[WorkCostSummary],
    label="name",
    tooltip="A roll up by cost category for the entire cost of a work order. For example, total labor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MiscCostItem_TreeNode = TreeNode(
    node_for=[MiscCostItem],
    label="name",
    tooltip="Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CULaborItem_TreeNode = TreeNode(
    node_for=[CULaborItem],
    label="name",
    tooltip="Compatible unit labor item.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CULaborItem_QualificationRequirements_TreeNode = TreeNode(
    node_for=[CULaborItem],
    children="QualificationRequirements",
    label="=QualificationRequirements",
    tooltip="",
    add=[QualificationRequirement],
    move=[QualificationRequirement],
    icon_path=IMAGE_PATH)
CULaborItem_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CULaborItem],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

CULaborCode_TreeNode = TreeNode(
    node_for=[CULaborCode],
    label="name",
    tooltip="Labor code associated with various compatible unit labor items.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CULaborCode_CULaborItems_TreeNode = TreeNode(
    node_for=[CULaborCode],
    children="CULaborItems",
    label="=CULaborItems",
    tooltip="",
    add=[CULaborItem],
    move=[CULaborItem],
    icon_path=IMAGE_PATH)

ShiftPattern_TreeNode = TreeNode(
    node_for=[ShiftPattern],
    label="name",
    tooltip="The patterns of shifts worked by people or crews.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShiftPattern_Crews_TreeNode = TreeNode(
    node_for=[ShiftPattern],
    children="Crews",
    label="=Crews",
    tooltip="",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)

OverheadCost_TreeNode = TreeNode(
    node_for=[OverheadCost],
    label="name",
    tooltip="Overhead cost applied to work order.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OverheadCost_WorkCostDetails_TreeNode = TreeNode(
    node_for=[OverheadCost],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)
OverheadCost_WorkTasks_TreeNode = TreeNode(
    node_for=[OverheadCost],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)

DesignLocationCU_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    label="name",
    tooltip="Compatible unit at a given design location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DesignLocationCU_Designs_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    children="Designs",
    label="=Designs",
    tooltip="",
    add=[Design],
    move=[Design],
    icon_path=IMAGE_PATH)
DesignLocationCU_CUGroups_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    children="CUGroups",
    label="=CUGroups",
    tooltip="",
    add=[CUGroup],
    move=[CUGroup],
    icon_path=IMAGE_PATH)
DesignLocationCU_ConditionFactors_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    children="ConditionFactors",
    label="=ConditionFactors",
    tooltip="",
    add=[ConditionFactor],
    move=[ConditionFactor],
    icon_path=IMAGE_PATH)
DesignLocationCU_WorkTasks_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)
DesignLocationCU_CompatibleUnits_TreeNode = TreeNode(
    node_for=[DesignLocationCU],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

WorkFlowStep_TreeNode = TreeNode(
    node_for=[WorkFlowStep],
    label="name",
    tooltip="A pre-defined set of work steps for a given type of work.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkFlowStep_WorkTasks_TreeNode = TreeNode(
    node_for=[WorkFlowStep],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)

ConditionFactor_TreeNode = TreeNode(
    node_for=[ConditionFactor],
    label="name",
    tooltip="This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConditionFactor_DesignLocationCUs_TreeNode = TreeNode(
    node_for=[ConditionFactor],
    children="DesignLocationCUs",
    label="=DesignLocationCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)
ConditionFactor_DesignLocations_TreeNode = TreeNode(
    node_for=[ConditionFactor],
    children="DesignLocations",
    label="=DesignLocations",
    tooltip="",
    add=[DesignLocation],
    move=[DesignLocation],
    icon_path=IMAGE_PATH)
ConditionFactor_Designs_TreeNode = TreeNode(
    node_for=[ConditionFactor],
    children="Designs",
    label="=Designs",
    tooltip="",
    add=[Design],
    move=[Design],
    icon_path=IMAGE_PATH)

OneCallRequest_TreeNode = TreeNode(
    node_for=[OneCallRequest],
    label="name",
    tooltip="A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OneCallRequest_WorkLocations_TreeNode = TreeNode(
    node_for=[OneCallRequest],
    children="WorkLocations",
    label="=WorkLocations",
    tooltip="",
    add=[WorkLocation],
    move=[WorkLocation],
    icon_path=IMAGE_PATH)

Assignment_TreeNode = TreeNode(
    node_for=[Assignment],
    label="name",
    tooltip="An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Assignment_Crews_TreeNode = TreeNode(
    node_for=[Assignment],
    children="Crews",
    label="=Crews",
    tooltip="All Crews having this Assignment.",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)

QualificationRequirement_TreeNode = TreeNode(
    node_for=[QualificationRequirement],
    label="name",
    tooltip="Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

QualificationRequirement_Specifications_TreeNode = TreeNode(
    node_for=[QualificationRequirement],
    children="Specifications",
    label="=Specifications",
    tooltip="",
    add=[Specification],
    move=[Specification],
    icon_path=IMAGE_PATH)
QualificationRequirement_WorkTasks_TreeNode = TreeNode(
    node_for=[QualificationRequirement],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)
QualificationRequirement_CULaborItems_TreeNode = TreeNode(
    node_for=[QualificationRequirement],
    children="CULaborItems",
    label="=CULaborItems",
    tooltip="",
    add=[CULaborItem],
    move=[CULaborItem],
    icon_path=IMAGE_PATH)
QualificationRequirement_Skills_TreeNode = TreeNode(
    node_for=[QualificationRequirement],
    children="Skills",
    label="=Skills",
    tooltip="",
    add=[Skill],
    move=[Skill],
    icon_path=IMAGE_PATH)

Crew_TreeNode = TreeNode(
    node_for=[Crew],
    label="name",
    tooltip="A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Crew_Capabilities_TreeNode = TreeNode(
    node_for=[Crew],
    children="Capabilities",
    label="=Capabilities",
    tooltip="",
    add=[Capability],
    move=[Capability],
    icon_path=IMAGE_PATH)
Crew_WorkTasks_TreeNode = TreeNode(
    node_for=[Crew],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="All WorkTasks this Crew participates in.",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)
Crew_Vehicles_TreeNode = TreeNode(
    node_for=[Crew],
    children="Vehicles",
    label="=Vehicles",
    tooltip="",
    add=[Vehicle],
    move=[Vehicle],
    icon_path=IMAGE_PATH)
Crew_CrewMembers_TreeNode = TreeNode(
    node_for=[Crew],
    children="CrewMembers",
    label="=CrewMembers",
    tooltip="All ErpPersons that are members of this Crew.",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)
Crew_Assignments_TreeNode = TreeNode(
    node_for=[Crew],
    children="Assignments",
    label="=Assignments",
    tooltip="All Assignments for this Crew.",
    add=[Assignment],
    move=[Assignment],
    icon_path=IMAGE_PATH)
Crew_Tools_TreeNode = TreeNode(
    node_for=[Crew],
    children="Tools",
    label="=Tools",
    tooltip="",
    add=[Tool],
    move=[Tool],
    icon_path=IMAGE_PATH)
Crew_OutageSteps_TreeNode = TreeNode(
    node_for=[Crew],
    children="OutageSteps",
    label="=OutageSteps",
    tooltip="",
    add=[OutageStep],
    move=[OutageStep],
    icon_path=IMAGE_PATH)
Crew_WorkEquipmentAssets_TreeNode = TreeNode(
    node_for=[Crew],
    children="WorkEquipmentAssets",
    label="=WorkEquipmentAssets",
    tooltip="",
    add=[WorkEquipmentAsset],
    move=[WorkEquipmentAsset],
    icon_path=IMAGE_PATH)
Crew_Locations_TreeNode = TreeNode(
    node_for=[Crew],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)
Crew_ShiftPatterns_TreeNode = TreeNode(
    node_for=[Crew],
    children="ShiftPatterns",
    label="=ShiftPatterns",
    tooltip="",
    add=[ShiftPattern],
    move=[ShiftPattern],
    icon_path=IMAGE_PATH)
Crew_SwitchingSchedules_TreeNode = TreeNode(
    node_for=[Crew],
    children="SwitchingSchedules",
    label="=SwitchingSchedules",
    tooltip="All SwitchingSchedules executed by this Crew.",
    add=[SwitchingSchedule],
    move=[SwitchingSchedule],
    icon_path=IMAGE_PATH)
Crew_Organisations_TreeNode = TreeNode(
    node_for=[Crew],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[ErpOrganisation],
    move=[ErpOrganisation],
    icon_path=IMAGE_PATH)

DiagnosisDataSet_TreeNode = TreeNode(
    node_for=[DiagnosisDataSet],
    label="name",
    tooltip="The result of a problem (typically an asset failure) diagnosis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ContractorItem_TreeNode = TreeNode(
    node_for=[ContractorItem],
    label="name",
    tooltip="Contractor information for work task.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ContractorItem_ErpPayables_TreeNode = TreeNode(
    node_for=[ContractorItem],
    children="ErpPayables",
    label="=ErpPayables",
    tooltip="",
    add=[ErpPayable],
    move=[ErpPayable],
    icon_path=IMAGE_PATH)

CUGroup_TreeNode = TreeNode(
    node_for=[CUGroup],
    label="name",
    tooltip="A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUGroup_ParentCUGroups_TreeNode = TreeNode(
    node_for=[CUGroup],
    children="ParentCUGroups",
    label="=ParentCUGroups",
    tooltip="",
    add=[CUGroup],
    move=[CUGroup],
    icon_path=IMAGE_PATH)
CUGroup_ChildCUGroups_TreeNode = TreeNode(
    node_for=[CUGroup],
    children="ChildCUGroups",
    label="=ChildCUGroups",
    tooltip="",
    add=[CUGroup],
    move=[CUGroup],
    icon_path=IMAGE_PATH)
CUGroup_DesignLocationCUs_TreeNode = TreeNode(
    node_for=[CUGroup],
    children="DesignLocationCUs",
    label="=DesignLocationCUs",
    tooltip="",
    add=[DesignLocationCU],
    move=[DesignLocationCU],
    icon_path=IMAGE_PATH)
CUGroup_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUGroup],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

CUWorkEquipmentItem_TreeNode = TreeNode(
    node_for=[CUWorkEquipmentItem],
    label="name",
    tooltip="Compatible unit for various types of WorkEquipmentAssets, including vehicles.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CUWorkEquipmentItem_CompatibleUnits_TreeNode = TreeNode(
    node_for=[CUWorkEquipmentItem],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)

WorkLocation_TreeNode = TreeNode(
    node_for=[WorkLocation],
    label="name",
    tooltip="Information about a particular location for various forms of work such as a one call request.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkLocation_DesignLocations_TreeNode = TreeNode(
    node_for=[WorkLocation],
    children="DesignLocations",
    label="=DesignLocations",
    tooltip="",
    add=[DesignLocation],
    move=[DesignLocation],
    icon_path=IMAGE_PATH)

WorkCostDetail_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    label="name",
    tooltip="A collection of all of the individual cost items collected from multiple sources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkCostDetail_LaborItems_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="LaborItems",
    label="=LaborItems",
    tooltip="",
    add=[LaborItem],
    move=[LaborItem],
    icon_path=IMAGE_PATH)
WorkCostDetail_EquipmentItems_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="EquipmentItems",
    label="=EquipmentItems",
    tooltip="",
    add=[EquipmentItem],
    move=[EquipmentItem],
    icon_path=IMAGE_PATH)
WorkCostDetail_MiscCostItems_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="MiscCostItems",
    label="=MiscCostItems",
    tooltip="",
    add=[MiscCostItem],
    move=[MiscCostItem],
    icon_path=IMAGE_PATH)
WorkCostDetail_Works_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)
WorkCostDetail_ContractorItems_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="ContractorItems",
    label="=ContractorItems",
    tooltip="",
    add=[ContractorItem],
    move=[ContractorItem],
    icon_path=IMAGE_PATH)
WorkCostDetail_MaterialItems_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="MaterialItems",
    label="=MaterialItems",
    tooltip="",
    add=[MaterialItem],
    move=[MaterialItem],
    icon_path=IMAGE_PATH)
WorkCostDetail_PropertyUnits_TreeNode = TreeNode(
    node_for=[WorkCostDetail],
    children="PropertyUnits",
    label="=PropertyUnits",
    tooltip="",
    add=[PropertyUnit],
    move=[PropertyUnit],
    icon_path=IMAGE_PATH)

EquipmentItem_TreeNode = TreeNode(
    node_for=[EquipmentItem],
    label="name",
    tooltip="An equipment item, such as a vehicle, used for a work order.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusinessCase_TreeNode = TreeNode(
    node_for=[BusinessCase],
    label="name",
    tooltip="Business justification for capital expenditures, usually addressing operations and maintenance costs as well.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusinessCase_Works_TreeNode = TreeNode(
    node_for=[BusinessCase],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)
BusinessCase_Projects_TreeNode = TreeNode(
    node_for=[BusinessCase],
    children="Projects",
    label="=Projects",
    tooltip="",
    add=[Project],
    move=[Project],
    icon_path=IMAGE_PATH)

Marketer_TreeNode = TreeNode(
    node_for=[Marketer],
    label="name",
    tooltip="Matches buyers and sellers, and secures transmission (and other ancillary services) needed to complete the energy transaction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Marketer_HeldBy_TreeNode = TreeNode(
    node_for=[Marketer],
    children="HeldBy",
    label="=HeldBy",
    tooltip="A Marketer holds title to a ServiceReservation.",
    add=[ServiceReservation],
    move=[ServiceReservation],
    icon_path=IMAGE_PATH)
Marketer_Resells_EnergyProduct_TreeNode = TreeNode(
    node_for=[Marketer],
    children="Resells_EnergyProduct",
    label="=Resells_EnergyProduct",
    tooltip="A Marketer may resell an EnergyProduct.",
    add=[EnergyProduct],
    move=[EnergyProduct],
    icon_path=IMAGE_PATH)
Marketer_HoldsTitleTo_EnergyProducts_TreeNode = TreeNode(
    node_for=[Marketer],
    children="HoldsTitleTo_EnergyProducts",
    label="=HoldsTitleTo_EnergyProducts",
    tooltip="A Marketer holds title to an EnergyProduct.",
    add=[EnergyProduct],
    move=[EnergyProduct],
    icon_path=IMAGE_PATH)

FinancialVersion_TreeNode = TreeNode(
    node_for=[FinancialVersion],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CustomerConsumer_TreeNode = TreeNode(
    node_for=[CustomerConsumer],
    label="name",
    tooltip="The energy buyer in the energy marketplace.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CustomerConsumer_ServicePoint_TreeNode = TreeNode(
    node_for=[CustomerConsumer],
    children="ServicePoint",
    label="=ServicePoint",
    tooltip="A CustomerConsumer may have one or more ServicePoints.",
    add=[ServicePoint],
    move=[ServicePoint],
    icon_path=IMAGE_PATH)
CustomerConsumer_TieLines_TreeNode = TreeNode(
    node_for=[CustomerConsumer],
    children="TieLines",
    label="=TieLines",
    tooltip="A  ControlAreaOperator or CustomerConsumer may ring their perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)

TransmissionProvider_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    label="name",
    tooltip="Provider of the transmission capacity (interconnecting wires between Generation and Consumption) required to fulfill and Energy Transaction's energy exchange. Posts information for transmission paths and AvailableTransmissionCapacities on a reservation node. Buys and sells its products and services on the same reservation node.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionProvider_TransmissionProducts_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="TransmissionProducts",
    label="=TransmissionProducts",
    tooltip="A TransmissionProvider offers a TransmissionProduct.",
    add=[TransmissionProduct],
    move=[TransmissionProduct],
    icon_path=IMAGE_PATH)
TransmissionProvider_Flowgate_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="Flowgate",
    label="=Flowgate",
    tooltip="A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)
TransmissionProvider_ServicePoint_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="ServicePoint",
    label="=ServicePoint",
    tooltip="A TransmissionProvider registers one or more ServicePoints.",
    add=[ServicePoint],
    move=[ServicePoint],
    icon_path=IMAGE_PATH)
TransmissionProvider_AncillaryServices_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="AncillaryServices",
    label="=AncillaryServices",
    tooltip="A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.",
    add=[AncillaryService],
    move=[AncillaryService],
    icon_path=IMAGE_PATH)
TransmissionProvider_For_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="For",
    label="=For",
    tooltip="Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.",
    add=[LossProfile],
    move=[LossProfile],
    icon_path=IMAGE_PATH)
TransmissionProvider_OfferedBy_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="OfferedBy",
    label="=OfferedBy",
    tooltip="The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)
TransmissionProvider_SoldBy_TreeNode = TreeNode(
    node_for=[TransmissionProvider],
    children="SoldBy",
    label="=SoldBy",
    tooltip="A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.",
    add=[ServiceReservation],
    move=[ServiceReservation],
    icon_path=IMAGE_PATH)

TransmissionProduct_TreeNode = TreeNode(
    node_for=[TransmissionProduct],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionProduct_Offers_TreeNode = TreeNode(
    node_for=[TransmissionProduct],
    children="Offers",
    label="=Offers",
    tooltip="A transmission product is offered as a transmission service along a transmission path.",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)
TransmissionProduct_LocationFor_TreeNode = TreeNode(
    node_for=[TransmissionProduct],
    children="LocationFor",
    label="=LocationFor",
    tooltip="A transmission product is located on a transmission path.",
    add=[TransmissionPath],
    move=[TransmissionPath],
    icon_path=IMAGE_PATH)

GenerationProvider_TreeNode = TreeNode(
    node_for=[GenerationProvider],
    label="name",
    tooltip="The energy seller in the energy marketplace.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GenerationProvider_GeneratingUnits_TreeNode = TreeNode(
    node_for=[GenerationProvider],
    children="GeneratingUnits",
    label="=GeneratingUnits",
    tooltip="A GenerationProvider operates one or more GeneratingUnits.",
    add=[GeneratingUnit],
    move=[GeneratingUnit],
    icon_path=IMAGE_PATH)
GenerationProvider_EnergyProducts_TreeNode = TreeNode(
    node_for=[GenerationProvider],
    children="EnergyProducts",
    label="=EnergyProducts",
    tooltip="",
    add=[EnergyProduct],
    move=[EnergyProduct],
    icon_path=IMAGE_PATH)
GenerationProvider_ServicePoint_TreeNode = TreeNode(
    node_for=[GenerationProvider],
    children="ServicePoint",
    label="=ServicePoint",
    tooltip="A GenerationProvider has one or more ServicePoints where energy is injected into the network.",
    add=[ServicePoint],
    move=[ServicePoint],
    icon_path=IMAGE_PATH)

OpenAccessProduct_TreeNode = TreeNode(
    node_for=[OpenAccessProduct],
    label="name",
    tooltip="Contracts for services offered commercially.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OpenAccessProduct_ProvidedBy_TransmissionService_TreeNode = TreeNode(
    node_for=[OpenAccessProduct],
    children="ProvidedBy_TransmissionService",
    label="=ProvidedBy_TransmissionService",
    tooltip="A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)
OpenAccessProduct_AncillaryServices_TreeNode = TreeNode(
    node_for=[OpenAccessProduct],
    children="AncillaryServices",
    label="=AncillaryServices",
    tooltip="AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.",
    add=[AncillaryService],
    move=[AncillaryService],
    icon_path=IMAGE_PATH)

IntSchedAgreement_TreeNode = TreeNode(
    node_for=[IntSchedAgreement],
    label="name",
    tooltip="A type of agreement that provides the default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IntSchedAgreement_Organisations_TreeNode = TreeNode(
    node_for=[IntSchedAgreement],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[ErpOrganisation],
    move=[ErpOrganisation],
    icon_path=IMAGE_PATH)

ControlAreaOperator_TreeNode = TreeNode(
    node_for=[ControlAreaOperator],
    label="name",
    tooltip="Operates the Control Area. Approves and implements energy transactions. Verifies both Inter-Control Area and Intra-Control Area transactions for the power system before granting approval (and implementing) the transactions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlAreaOperator_AncillaryService_TreeNode = TreeNode(
    node_for=[ControlAreaOperator],
    children="AncillaryService",
    label="=AncillaryService",
    tooltip="Sale of ancillary services provided by ControlAreaOperators.",
    add=[AncillaryService],
    move=[AncillaryService],
    icon_path=IMAGE_PATH)
ControlAreaOperator_TieLines_TreeNode = TreeNode(
    node_for=[ControlAreaOperator],
    children="TieLines",
    label="=TieLines",
    tooltip="A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)

FailureEvent_TreeNode = TreeNode(
    node_for=[FailureEvent],
    label="name",
    tooltip="An event where an asset has failed to perform its functions within specified parameters.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ElectricalAsset_TreeNode = TreeNode(
    node_for=[ElectricalAsset],
    label="name",
    tooltip="An asset that has (or can have) a role in the electrical network.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ElectricalAsset_ElectricalInfos_TreeNode = TreeNode(
    node_for=[ElectricalAsset],
    children="ElectricalInfos",
    label="=ElectricalInfos",
    tooltip="",
    add=[ElectricalInfo],
    move=[ElectricalInfo],
    icon_path=IMAGE_PATH)

SwitchAsset_TreeNode = TreeNode(
    node_for=[SwitchAsset],
    label="name",
    tooltip="Physical asset performing Switch function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SwitchInfo_TreeNode = TreeNode(
    node_for=[SwitchInfo],
    label="name",
    tooltip="Properties of a switch.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchInfo_SwitchAssets_TreeNode = TreeNode(
    node_for=[SwitchInfo],
    children="SwitchAssets",
    label="=SwitchAssets",
    tooltip="",
    add=[SwitchAsset],
    move=[SwitchAsset],
    icon_path=IMAGE_PATH)

RecloserInfo_TreeNode = TreeNode(
    node_for=[RecloserInfo],
    label="name",
    tooltip="Properties of reclosers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RecloserInfo_RecloserAssetModels_TreeNode = TreeNode(
    node_for=[RecloserInfo],
    children="RecloserAssetModels",
    label="=RecloserAssetModels",
    tooltip="",
    add=[RecloserAssetModel],
    move=[RecloserAssetModel],
    icon_path=IMAGE_PATH)
RecloserInfo_RecloserAssets_TreeNode = TreeNode(
    node_for=[RecloserInfo],
    children="RecloserAssets",
    label="=RecloserAssets",
    tooltip="",
    add=[RecloserAsset],
    move=[RecloserAsset],
    icon_path=IMAGE_PATH)

PowerRating_TreeNode = TreeNode(
    node_for=[PowerRating],
    label="name",
    tooltip="There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerRating_TransformerAssets_TreeNode = TreeNode(
    node_for=[PowerRating],
    children="TransformerAssets",
    label="=TransformerAssets",
    tooltip="",
    add=[TransformerAsset],
    move=[TransformerAsset],
    icon_path=IMAGE_PATH)

BusbarAsset_TreeNode = TreeNode(
    node_for=[BusbarAsset],
    label="name",
    tooltip="Physical asset used to perform the BusbarSection's role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StructureSupport_TreeNode = TreeNode(
    node_for=[StructureSupport],
    label="name",
    tooltip="Support for Structures.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Guy_TreeNode = TreeNode(
    node_for=[Guy],
    label="name",
    tooltip="A type of support for structures.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurrentTransformerInfo_TreeNode = TreeNode(
    node_for=[CurrentTransformerInfo],
    label="name",
    tooltip="Used to define either the required additional electrical properties of a type of Current Transformer (CT) or a CT Model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CurrentTransformerInfo_CurrentTransformerAssets_TreeNode = TreeNode(
    node_for=[CurrentTransformerInfo],
    children="CurrentTransformerAssets",
    label="=CurrentTransformerAssets",
    tooltip="",
    add=[CurrentTransformerAsset],
    move=[CurrentTransformerAsset],
    icon_path=IMAGE_PATH)
CurrentTransformerInfo_CurrentTransformerAssertModels_TreeNode = TreeNode(
    node_for=[CurrentTransformerInfo],
    children="CurrentTransformerAssertModels",
    label="=CurrentTransformerAssertModels",
    tooltip="",
    add=[CurrentTransformerAssetModel],
    move=[CurrentTransformerAssetModel],
    icon_path=IMAGE_PATH)

ConductorAsset_TreeNode = TreeNode(
    node_for=[ConductorAsset],
    label="name",
    tooltip="Physical asset used to perform the conductor's role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CableAsset_TreeNode = TreeNode(
    node_for=[CableAsset],
    label="name",
    tooltip="Insultated physical cable for performing the Conductor role used in undergrond and other applications..",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CableAsset_DuctBanks_TreeNode = TreeNode(
    node_for=[CableAsset],
    children="DuctBanks",
    label="=DuctBanks",
    tooltip="",
    add=[DuctBank],
    move=[DuctBank],
    icon_path=IMAGE_PATH)

Medium_TreeNode = TreeNode(
    node_for=[Medium],
    label="name",
    tooltip="A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Medium_Assets_TreeNode = TreeNode(
    node_for=[Medium],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)

ProcedureDataSet_TreeNode = TreeNode(
    node_for=[ProcedureDataSet],
    label="name",
    tooltip="A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProcedureDataSet_Properties_TreeNode = TreeNode(
    node_for=[ProcedureDataSet],
    children="Properties",
    label="=Properties",
    tooltip="UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
ProcedureDataSet_MeasurementValues_TreeNode = TreeNode(
    node_for=[ProcedureDataSet],
    children="MeasurementValues",
    label="=MeasurementValues",
    tooltip="",
    add=[MeasurementValue],
    move=[MeasurementValue],
    icon_path=IMAGE_PATH)
ProcedureDataSet_TransformerObservations_TreeNode = TreeNode(
    node_for=[ProcedureDataSet],
    children="TransformerObservations",
    label="=TransformerObservations",
    tooltip="",
    add=[TransformerObservation],
    move=[TransformerObservation],
    icon_path=IMAGE_PATH)

Vehicle_TreeNode = TreeNode(
    node_for=[Vehicle],
    label="name",
    tooltip="A vehicle is a type of utility asset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WorkEquipmentAsset_TreeNode = TreeNode(
    node_for=[WorkEquipmentAsset],
    label="name",
    tooltip="Various equipment used to perform units of work by crews, office staff, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkEquipmentAsset_Usages_TreeNode = TreeNode(
    node_for=[WorkEquipmentAsset],
    children="Usages",
    label="=Usages",
    tooltip="",
    add=[Usage],
    move=[Usage],
    icon_path=IMAGE_PATH)

GeneratorAsset_TreeNode = TreeNode(
    node_for=[GeneratorAsset],
    label="name",
    tooltip="Physical asset performing the Generator role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Tool_TreeNode = TreeNode(
    node_for=[Tool],
    label="name",
    tooltip="Utility asset typically used by utility resources like crews and persons. As is the case for other assets, tools must be maintained.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerAsset_TreeNode = TreeNode(
    node_for=[TransformerAsset],
    label="name",
    tooltip="A specific physical (vs. logical) transformer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerAsset_PowerRatings_TreeNode = TreeNode(
    node_for=[TransformerAsset],
    children="PowerRatings",
    label="=PowerRatings",
    tooltip="",
    add=[PowerRating],
    move=[PowerRating],
    icon_path=IMAGE_PATH)
TransformerAsset_TransformerObservations_TreeNode = TreeNode(
    node_for=[TransformerAsset],
    children="TransformerObservations",
    label="=TransformerObservations",
    tooltip="",
    add=[TransformerObservation],
    move=[TransformerObservation],
    icon_path=IMAGE_PATH)

Facility_TreeNode = TreeNode(
    node_for=[Facility],
    label="name",
    tooltip="A facility may contain buildings, storage facilities, switching facilities, power generation, manufacturing facilities, maintenance facilities, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Structure_TreeNode = TreeNode(
    node_for=[Structure],
    label="name",
    tooltip="Construction holding assets such as conductors, transformers, switchgear, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Structure_StructureSupports_TreeNode = TreeNode(
    node_for=[Structure],
    children="StructureSupports",
    label="=StructureSupports",
    tooltip="",
    add=[StructureSupport],
    move=[StructureSupport],
    icon_path=IMAGE_PATH)

UndergroundStructure_TreeNode = TreeNode(
    node_for=[UndergroundStructure],
    label="name",
    tooltip="Abstract class for underground structures. Typical structure types are: BURD, Enclosure, Hand Hole, Manhole, Pad/Slab, Subsurface Enclosure, Trench, Tunnel, Vault, Pull/Splice Box.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AssetAssetRole_TreeNode = TreeNode(
    node_for=[AssetAssetRole],
    label="name",
    tooltip="Roles played between Assets and other Assets.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindingInsulation_TreeNode = TreeNode(
    node_for=[WindingInsulation],
    label="name",
    tooltip="Winding insulation condition as a result of a test.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerObservation_TreeNode = TreeNode(
    node_for=[TransformerObservation],
    label="name",
    tooltip="Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerObservation_WindingInsulationPFs_TreeNode = TreeNode(
    node_for=[TransformerObservation],
    children="WindingInsulationPFs",
    label="=WindingInsulationPFs",
    tooltip="",
    add=[WindingInsulation],
    move=[WindingInsulation],
    icon_path=IMAGE_PATH)
TransformerObservation_BushingInsultationPFs_TreeNode = TreeNode(
    node_for=[TransformerObservation],
    children="BushingInsultationPFs",
    label="=BushingInsultationPFs",
    tooltip="",
    add=[BushingInsulationPF],
    move=[BushingInsulationPF],
    icon_path=IMAGE_PATH)
TransformerObservation_ProcedureDataSets_TreeNode = TreeNode(
    node_for=[TransformerObservation],
    children="ProcedureDataSets",
    label="=ProcedureDataSets",
    tooltip="",
    add=[ProcedureDataSet],
    move=[ProcedureDataSet],
    icon_path=IMAGE_PATH)

ShuntCompensatorAsset_TreeNode = TreeNode(
    node_for=[ShuntCompensatorAsset],
    label="name",
    tooltip="For a shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is the physical asset performing the ShuntCompensator role (PSR).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SurgeProtectorAsset_TreeNode = TreeNode(
    node_for=[SurgeProtectorAsset],
    label="name",
    tooltip="Physical asset performing SurgeProtector function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CompositeSwitchInfo_TreeNode = TreeNode(
    node_for=[CompositeSwitchInfo],
    label="name",
    tooltip="Properties of a composite switch.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompositeSwitchInfo_CompositeSwitchAssets_TreeNode = TreeNode(
    node_for=[CompositeSwitchInfo],
    children="CompositeSwitchAssets",
    label="=CompositeSwitchAssets",
    tooltip="",
    add=[CompositeSwitchAsset],
    move=[CompositeSwitchAsset],
    icon_path=IMAGE_PATH)

PotentialTransformerAsset_TreeNode = TreeNode(
    node_for=[PotentialTransformerAsset],
    label="name",
    tooltip="Physical asset performing Potential Transformer (PT) function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TestDataSet_TreeNode = TreeNode(
    node_for=[TestDataSet],
    label="name",
    tooltip="Test results, usually obtained by a lab or other independent organisation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FACTSDeviceAsset_TreeNode = TreeNode(
    node_for=[FACTSDeviceAsset],
    label="name",
    tooltip="Physical asset used to perform the FACTSDevice's role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OverheadConductorAsset_TreeNode = TreeNode(
    node_for=[OverheadConductorAsset],
    label="name",
    tooltip="Physical conductor performing the Conductor role that is used in overhead applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShuntImpedanceInfo_TreeNode = TreeNode(
    node_for=[ShuntImpedanceInfo],
    label="name",
    tooltip="Properties of a shunt impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShuntImpedanceInfo_ShuntCompensatorAssets_TreeNode = TreeNode(
    node_for=[ShuntImpedanceInfo],
    children="ShuntCompensatorAssets",
    label="=ShuntCompensatorAssets",
    tooltip="",
    add=[ShuntCompensatorAsset],
    move=[ShuntCompensatorAsset],
    icon_path=IMAGE_PATH)

DuctBank_TreeNode = TreeNode(
    node_for=[DuctBank],
    label="name",
    tooltip="A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DuctBank_CableAssets_TreeNode = TreeNode(
    node_for=[DuctBank],
    children="CableAssets",
    label="=CableAssets",
    tooltip="",
    add=[CableAsset],
    move=[CableAsset],
    icon_path=IMAGE_PATH)

SVCAsset_TreeNode = TreeNode(
    node_for=[SVCAsset],
    label="name",
    tooltip="Physical asset performing StaticVarCompensator function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectionEquipmentAsset_TreeNode = TreeNode(
    node_for=[ProtectionEquipmentAsset],
    label="name",
    tooltip="Physical asset performing ProtectionEquipment function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Manhole_TreeNode = TreeNode(
    node_for=[Manhole],
    label="name",
    tooltip="Provides access at key locations to underground cables, equipment, etc. housed inside a protective vault.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Procedure_TreeNode = TreeNode(
    node_for=[Procedure],
    label="name",
    tooltip="A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Procedure_CompatibleUnits_TreeNode = TreeNode(
    node_for=[Procedure],
    children="CompatibleUnits",
    label="=CompatibleUnits",
    tooltip="",
    add=[CompatibleUnit],
    move=[CompatibleUnit],
    icon_path=IMAGE_PATH)
Procedure_ProcedureDataSets_TreeNode = TreeNode(
    node_for=[Procedure],
    children="ProcedureDataSets",
    label="=ProcedureDataSets",
    tooltip="",
    add=[ProcedureDataSet],
    move=[ProcedureDataSet],
    icon_path=IMAGE_PATH)
Procedure_ProcedureValues_TreeNode = TreeNode(
    node_for=[Procedure],
    children="ProcedureValues",
    label="=ProcedureValues",
    tooltip="UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
Procedure_Limits_TreeNode = TreeNode(
    node_for=[Procedure],
    children="Limits",
    label="=Limits",
    tooltip="",
    add=[Limit],
    move=[Limit],
    icon_path=IMAGE_PATH)

BreakerAsset_TreeNode = TreeNode(
    node_for=[BreakerAsset],
    label="name",
    tooltip="Physical asset performing Breaker role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapChangerAsset_TreeNode = TreeNode(
    node_for=[TapChangerAsset],
    label="name",
    tooltip="Physical asset performing TapChanger function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PotentialTransformerInfo_TreeNode = TreeNode(
    node_for=[PotentialTransformerInfo],
    label="name",
    tooltip="Used to define either the required additional electrical properties of a type of a Potential Transformer (PT), or a PT Model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PotentialTransformerInfo_PotentialTransformerAssets_TreeNode = TreeNode(
    node_for=[PotentialTransformerInfo],
    children="PotentialTransformerAssets",
    label="=PotentialTransformerAssets",
    tooltip="",
    add=[PotentialTransformerAsset],
    move=[PotentialTransformerAsset],
    icon_path=IMAGE_PATH)
PotentialTransformerInfo_PotentialTransformerAssetModels_TreeNode = TreeNode(
    node_for=[PotentialTransformerInfo],
    children="PotentialTransformerAssetModels",
    label="=PotentialTransformerAssetModels",
    tooltip="",
    add=[PotentialTransformerAssetModel],
    move=[PotentialTransformerAssetModel],
    icon_path=IMAGE_PATH)

AssetPsrRole_TreeNode = TreeNode(
    node_for=[AssetPsrRole],
    label="name",
    tooltip="Roles played between Assets and Power System Resources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DocAssetRole_TreeNode = TreeNode(
    node_for=[DocAssetRole],
    label="name",
    tooltip="Roles played between Documents and Assets.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SubstationAsset_TreeNode = TreeNode(
    node_for=[SubstationAsset],
    label="name",
    tooltip="A grouping of assets such as conductors, transformers, switchgear, etc. When located on the ground surface, it is usually surrounded by some kind of fence with a locked gate. It may also be located inside buildings, in underground vaults, and on structures. Use 'category' for utility-specific categorisation (such as Air Cooled, Gas Insultated, etc.).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SeriesCompensatorAsset_TreeNode = TreeNode(
    node_for=[SeriesCompensatorAsset],
    label="name",
    tooltip="For a a series capacitor or reactor, this is the physical asset performing the SeriesCompensator role (PSR).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SVCInfo_TreeNode = TreeNode(
    node_for=[SVCInfo],
    label="name",
    tooltip="Properties for an SVC, allowing the capacitive and inductive ratings for each phase to be specified individually if required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SVCInfo_SVCTypeAssets_TreeNode = TreeNode(
    node_for=[SVCInfo],
    children="SVCTypeAssets",
    label="=SVCTypeAssets",
    tooltip="",
    add=[SVCTypeAsset],
    move=[SVCTypeAsset],
    icon_path=IMAGE_PATH)

CompositeSwitchAsset_TreeNode = TreeNode(
    node_for=[CompositeSwitchAsset],
    label="name",
    tooltip="Physical asset that performs a given CompositeSwitch's role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AssetPropertyCurve_TreeNode = TreeNode(
    node_for=[AssetPropertyCurve],
    label="name",
    tooltip="An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetPropertyCurve_Assets_TreeNode = TreeNode(
    node_for=[AssetPropertyCurve],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)

Pole_TreeNode = TreeNode(
    node_for=[Pole],
    label="name",
    tooltip="A long, slender piece of wood, metal, etc. usually rounded that stands vertically from the ground and is used for mounting various types of overhead equipment. Dimensions of Pole are specified in associated DimensionsInfo.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Pole_SupportStreetlights_TreeNode = TreeNode(
    node_for=[Pole],
    children="SupportStreetlights",
    label="=SupportStreetlights",
    tooltip="Streetlight(s) may be attached to a pole.",
    add=[Streetlight],
    move=[Streetlight],
    icon_path=IMAGE_PATH)

Specification_TreeNode = TreeNode(
    node_for=[Specification],
    label="name",
    tooltip="Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Specification_AssetProperites_TreeNode = TreeNode(
    node_for=[Specification],
    children="AssetProperites",
    label="=AssetProperites",
    tooltip="UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
Specification_QualificationRequirements_TreeNode = TreeNode(
    node_for=[Specification],
    children="QualificationRequirements",
    label="=QualificationRequirements",
    tooltip="",
    add=[QualificationRequirement],
    move=[QualificationRequirement],
    icon_path=IMAGE_PATH)
Specification_Ratings_TreeNode = TreeNode(
    node_for=[Specification],
    children="Ratings",
    label="=Ratings",
    tooltip="UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
Specification_DimensionsInfos_TreeNode = TreeNode(
    node_for=[Specification],
    children="DimensionsInfos",
    label="=DimensionsInfos",
    tooltip="",
    add=[DimensionsInfo],
    move=[DimensionsInfo],
    icon_path=IMAGE_PATH)
Specification_ReliabilityInfos_TreeNode = TreeNode(
    node_for=[Specification],
    children="ReliabilityInfos",
    label="=ReliabilityInfos",
    tooltip="",
    add=[ReliabilityInfo],
    move=[ReliabilityInfo],
    icon_path=IMAGE_PATH)
Specification_Mediums_TreeNode = TreeNode(
    node_for=[Specification],
    children="Mediums",
    label="=Mediums",
    tooltip="",
    add=[Medium],
    move=[Medium],
    icon_path=IMAGE_PATH)
Specification_AssetPropertyCurves_TreeNode = TreeNode(
    node_for=[Specification],
    children="AssetPropertyCurves",
    label="=AssetPropertyCurves",
    tooltip="",
    add=[AssetPropertyCurve],
    move=[AssetPropertyCurve],
    icon_path=IMAGE_PATH)

BushingInsulationPF_TreeNode = TreeNode(
    node_for=[BushingInsulationPF],
    label="name",
    tooltip="Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DimensionsInfo_TreeNode = TreeNode(
    node_for=[DimensionsInfo],
    label="name",
    tooltip="As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DimensionsInfo_Assets_TreeNode = TreeNode(
    node_for=[DimensionsInfo],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
DimensionsInfo_Specifications_TreeNode = TreeNode(
    node_for=[DimensionsInfo],
    children="Specifications",
    label="=Specifications",
    tooltip="",
    add=[Specification],
    move=[Specification],
    icon_path=IMAGE_PATH)
DimensionsInfo_Locations_TreeNode = TreeNode(
    node_for=[DimensionsInfo],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

Anchor_TreeNode = TreeNode(
    node_for=[Anchor],
    label="name",
    tooltip="A type of support for structures, used to hold poles secure.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ComEquipmentAsset_TreeNode = TreeNode(
    node_for=[ComEquipmentAsset],
    label="name",
    tooltip="Communicaiton equipment, other than media, such as gateways, routers, controllers, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ComEquipmentAsset_DeviceFunctions_TreeNode = TreeNode(
    node_for=[ComEquipmentAsset],
    children="DeviceFunctions",
    label="=DeviceFunctions",
    tooltip="All device functions of this communication equipment asset.",
    add=[DeviceFunction],
    move=[DeviceFunction],
    icon_path=IMAGE_PATH)

CurrentTransformerAsset_TreeNode = TreeNode(
    node_for=[CurrentTransformerAsset],
    label="name",
    tooltip="Physical asset performing Current Transformer (CT) function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ResistorAsset_TreeNode = TreeNode(
    node_for=[ResistorAsset],
    label="name",
    tooltip="Physical asset performing Resistor function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Streetlight_TreeNode = TreeNode(
    node_for=[Streetlight],
    label="name",
    tooltip="Streetlight asset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BushingAsset_TreeNode = TreeNode(
    node_for=[BushingAsset],
    label="name",
    tooltip="Physical bushing that insulates and protects from abrasion a conductor that passes through it. It is associated with a specific Terminal, which is in turn associated with a ConductingEquipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BushingAsset_BushingInsulationPFs_TreeNode = TreeNode(
    node_for=[BushingAsset],
    children="BushingInsulationPFs",
    label="=BushingInsulationPFs",
    tooltip="",
    add=[BushingInsulationPF],
    move=[BushingInsulationPF],
    icon_path=IMAGE_PATH)

JointAsset_TreeNode = TreeNode(
    node_for=[JointAsset],
    label="name",
    tooltip="Physical asset connecting two or more cable assets. It includes the portion of cable under wipes, welds, or other seals.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RecloserAsset_TreeNode = TreeNode(
    node_for=[RecloserAsset],
    label="name",
    tooltip="Physical recloser performing a reclosing function, which is modeled through Breaker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Cabinet_TreeNode = TreeNode(
    node_for=[Cabinet],
    label="name",
    tooltip="Enclosure that offers protection to the equipment it contains and/or safety to people/animals outside it.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReliabilityInfo_TreeNode = TreeNode(
    node_for=[ReliabilityInfo],
    label="name",
    tooltip="Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReliabilityInfo_Assets_TreeNode = TreeNode(
    node_for=[ReliabilityInfo],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)

Tower_TreeNode = TreeNode(
    node_for=[Tower],
    label="name",
    tooltip="Large structure used to carry transmission lines, subtransmission lines, and/or other equipment/lines (e.g., communication). Dimensions of the Tower are specified in associated DimensionsInfo class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FaultIndicatorAsset_TreeNode = TreeNode(
    node_for=[FaultIndicatorAsset],
    label="name",
    tooltip="Physical asset performing FaultIndicator function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OrgAssetRole_TreeNode = TreeNode(
    node_for=[OrgAssetRole],
    label="name",
    tooltip="The roles played between an Organisations and an Asset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FinancialInfo_TreeNode = TreeNode(
    node_for=[FinancialInfo],
    label="name",
    tooltip="Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BreakerInfo_TreeNode = TreeNode(
    node_for=[BreakerInfo],
    label="name",
    tooltip="Properties of breakers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BreakerInfo_BreakerAssets_TreeNode = TreeNode(
    node_for=[BreakerInfo],
    children="BreakerAssets",
    label="=BreakerAssets",
    tooltip="",
    add=[BreakerAsset],
    move=[BreakerAsset],
    icon_path=IMAGE_PATH)
BreakerInfo_BreakerAssetModels_TreeNode = TreeNode(
    node_for=[BreakerInfo],
    children="BreakerAssetModels",
    label="=BreakerAssetModels",
    tooltip="",
    add=[BreakerAssetModel],
    move=[BreakerAssetModel],
    icon_path=IMAGE_PATH)

ElectricalAssetModel_TreeNode = TreeNode(
    node_for=[ElectricalAssetModel],
    label="name",
    tooltip="Documentation for a type of ElectricalAsset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ElectricalAssetModel_ElectricalInfos_TreeNode = TreeNode(
    node_for=[ElectricalAssetModel],
    children="ElectricalInfos",
    label="=ElectricalInfos",
    tooltip="",
    add=[ElectricalInfo],
    move=[ElectricalInfo],
    icon_path=IMAGE_PATH)

ComFunctionAssetModel_TreeNode = TreeNode(
    node_for=[ComFunctionAssetModel],
    label="name",
    tooltip="Documentation for a type of communication function of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SwitchAssetModel_TreeNode = TreeNode(
    node_for=[SwitchAssetModel],
    label="name",
    tooltip="Documentation for a type of a switch asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchAssetModel_SwitchAssets_TreeNode = TreeNode(
    node_for=[SwitchAssetModel],
    children="SwitchAssets",
    label="=SwitchAssets",
    tooltip="",
    add=[SwitchAsset],
    move=[SwitchAsset],
    icon_path=IMAGE_PATH)

VehicleAssetModel_TreeNode = TreeNode(
    node_for=[VehicleAssetModel],
    label="name",
    tooltip="Documentation for a type of a vehicle of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VehicleAssetModel_Vehicles_TreeNode = TreeNode(
    node_for=[VehicleAssetModel],
    children="Vehicles",
    label="=Vehicles",
    tooltip="",
    add=[Vehicle],
    move=[Vehicle],
    icon_path=IMAGE_PATH)

MeterAssetModel_TreeNode = TreeNode(
    node_for=[MeterAssetModel],
    label="name",
    tooltip="Documentation for a type of a meter asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeterAssetModel_MeterAssets_TreeNode = TreeNode(
    node_for=[MeterAssetModel],
    children="MeterAssets",
    label="=MeterAssets",
    tooltip="",
    add=[MeterAsset],
    move=[MeterAsset],
    icon_path=IMAGE_PATH)

FACTSDeviceAssetModel_TreeNode = TreeNode(
    node_for=[FACTSDeviceAssetModel],
    label="name",
    tooltip="A particular model of FACTS device provided from a manufacturer. A FACTS devices are used for the dynamic control of voltage, impedance and phase angle of high voltage AC transmission lines. FACTS device types include: - SVC = Static Var Compensator - STATCOM = Static Synchronous Compensator - TCPAR = Thyristor Controlled Phase-Angle Regulator - TCSC = Thyristor Controlled Series Capacitor - TCVL = Thyristor Controlled Voltage Limiter - TSBR = Thyristor Switched Braking Resistor - TSSC = Thyristor Switched Series Capacitor - UPFC = Unified Power Flow Controller",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FACTSDeviceAssetModel_FACTSDeviceAssets_TreeNode = TreeNode(
    node_for=[FACTSDeviceAssetModel],
    children="FACTSDeviceAssets",
    label="=FACTSDeviceAssets",
    tooltip="",
    add=[FACTSDeviceAsset],
    move=[FACTSDeviceAsset],
    icon_path=IMAGE_PATH)

WorkEquipmentAssetModel_TreeNode = TreeNode(
    node_for=[WorkEquipmentAssetModel],
    label="name",
    tooltip="Documentation for a type of an equipment used for work of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkEquipmentAssetModel_WorkEquipmentAssets_TreeNode = TreeNode(
    node_for=[WorkEquipmentAssetModel],
    children="WorkEquipmentAssets",
    label="=WorkEquipmentAssets",
    tooltip="",
    add=[WorkEquipmentAsset],
    move=[WorkEquipmentAsset],
    icon_path=IMAGE_PATH)

RecloserAssetModel_TreeNode = TreeNode(
    node_for=[RecloserAssetModel],
    label="name",
    tooltip="Documentation for a type of a recloser asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RecloserAssetModel_RecloserAssets_TreeNode = TreeNode(
    node_for=[RecloserAssetModel],
    children="RecloserAssets",
    label="=RecloserAssets",
    tooltip="",
    add=[RecloserAsset],
    move=[RecloserAsset],
    icon_path=IMAGE_PATH)

AssetModelCatalogueItem_TreeNode = TreeNode(
    node_for=[AssetModelCatalogueItem],
    label="name",
    tooltip="Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetModelCatalogueItem_ErpQuoteLineItems_TreeNode = TreeNode(
    node_for=[AssetModelCatalogueItem],
    children="ErpQuoteLineItems",
    label="=ErpQuoteLineItems",
    tooltip="",
    add=[ErpQuoteLineItem],
    move=[ErpQuoteLineItem],
    icon_path=IMAGE_PATH)
AssetModelCatalogueItem_ErpPOLineItems_TreeNode = TreeNode(
    node_for=[AssetModelCatalogueItem],
    children="ErpPOLineItems",
    label="=ErpPOLineItems",
    tooltip="",
    add=[ErpPOLineItem],
    move=[ErpPOLineItem],
    icon_path=IMAGE_PATH)

ShuntCompensatorAssetModel_TreeNode = TreeNode(
    node_for=[ShuntCompensatorAssetModel],
    label="name",
    tooltip="For application as shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer (Organisation). There are typically many instances of an asset associated with a single asset model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShuntCompensatorAssetModel_ShuntCompensatorAssets_TreeNode = TreeNode(
    node_for=[ShuntCompensatorAssetModel],
    children="ShuntCompensatorAssets",
    label="=ShuntCompensatorAssets",
    tooltip="",
    add=[ShuntCompensatorAsset],
    move=[ShuntCompensatorAsset],
    icon_path=IMAGE_PATH)

SVCAssetModel_TreeNode = TreeNode(
    node_for=[SVCAssetModel],
    label="name",
    tooltip="Documentation for a type of a Static Var Compensator of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SVCAssetModel_SVCAssets_TreeNode = TreeNode(
    node_for=[SVCAssetModel],
    children="SVCAssets",
    label="=SVCAssets",
    tooltip="",
    add=[SVCAsset],
    move=[SVCAsset],
    icon_path=IMAGE_PATH)

BreakerAssetModel_TreeNode = TreeNode(
    node_for=[BreakerAssetModel],
    label="name",
    tooltip="Documentation for a type of a breaker asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BreakerAssetModel_BreakerAssets_TreeNode = TreeNode(
    node_for=[BreakerAssetModel],
    children="BreakerAssets",
    label="=BreakerAssets",
    tooltip="",
    add=[BreakerAsset],
    move=[BreakerAsset],
    icon_path=IMAGE_PATH)

GeneratorAssetModel_TreeNode = TreeNode(
    node_for=[GeneratorAssetModel],
    label="name",
    tooltip="Documentation for a type of generation equipment of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratorAssetModel_GeneratorAssets_TreeNode = TreeNode(
    node_for=[GeneratorAssetModel],
    children="GeneratorAssets",
    label="=GeneratorAssets",
    tooltip="",
    add=[GeneratorAsset],
    move=[GeneratorAsset],
    icon_path=IMAGE_PATH)

ToolAssetModel_TreeNode = TreeNode(
    node_for=[ToolAssetModel],
    label="name",
    tooltip="Documentation for a type of a tool of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ToolAssetModel_Tools_TreeNode = TreeNode(
    node_for=[ToolAssetModel],
    children="Tools",
    label="=Tools",
    tooltip="",
    add=[Tool],
    move=[Tool],
    icon_path=IMAGE_PATH)

ResistorAssetModel_TreeNode = TreeNode(
    node_for=[ResistorAssetModel],
    label="name",
    tooltip="Documentation for a type of a resistor asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ResistorAssetModel_ResistorAssets_TreeNode = TreeNode(
    node_for=[ResistorAssetModel],
    children="ResistorAssets",
    label="=ResistorAssets",
    tooltip="",
    add=[ResistorAsset],
    move=[ResistorAsset],
    icon_path=IMAGE_PATH)

TapChangerAssetModel_TreeNode = TreeNode(
    node_for=[TapChangerAssetModel],
    label="name",
    tooltip="Documentation for a type of a tap changer of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TapChangerAssetModel_TapChangerAssets_TreeNode = TreeNode(
    node_for=[TapChangerAssetModel],
    children="TapChangerAssets",
    label="=TapChangerAssets",
    tooltip="",
    add=[TapChangerAsset],
    move=[TapChangerAsset],
    icon_path=IMAGE_PATH)

SurgeProtectorAssetModel_TreeNode = TreeNode(
    node_for=[SurgeProtectorAssetModel],
    label="name",
    tooltip="Documentation for a type of an SurgeProtector asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SurgeProtectorAssetModel_SurgeProtectorAssets_TreeNode = TreeNode(
    node_for=[SurgeProtectorAssetModel],
    children="SurgeProtectorAssets",
    label="=SurgeProtectorAssets",
    tooltip="",
    add=[SurgeProtectorAsset],
    move=[SurgeProtectorAsset],
    icon_path=IMAGE_PATH)

CabinetModel_TreeNode = TreeNode(
    node_for=[CabinetModel],
    label="name",
    tooltip="Documentation for a type of Cabinet of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CabinetModel_Cabinets_TreeNode = TreeNode(
    node_for=[CabinetModel],
    children="Cabinets",
    label="=Cabinets",
    tooltip="",
    add=[Cabinet],
    move=[Cabinet],
    icon_path=IMAGE_PATH)

CompositeSwitchAssetModel_TreeNode = TreeNode(
    node_for=[CompositeSwitchAssetModel],
    label="name",
    tooltip="Documentation for a type of a composite switch asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompositeSwitchAssetModel_CompositeSwitchAssets_TreeNode = TreeNode(
    node_for=[CompositeSwitchAssetModel],
    children="CompositeSwitchAssets",
    label="=CompositeSwitchAssets",
    tooltip="",
    add=[CompositeSwitchAsset],
    move=[CompositeSwitchAsset],
    icon_path=IMAGE_PATH)

ProtectionEquipmentAssetModel_TreeNode = TreeNode(
    node_for=[ProtectionEquipmentAssetModel],
    label="name",
    tooltip="Documentation for a type of protection equipment asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectionEquipmentAssetModel_ProtectionEquipmentAssets_TreeNode = TreeNode(
    node_for=[ProtectionEquipmentAssetModel],
    children="ProtectionEquipmentAssets",
    label="=ProtectionEquipmentAssets",
    tooltip="",
    add=[ProtectionEquipmentAsset],
    move=[ProtectionEquipmentAsset],
    icon_path=IMAGE_PATH)

AssetModelCatalogue_TreeNode = TreeNode(
    node_for=[AssetModelCatalogue],
    label="name",
    tooltip="Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetModelCatalogue_AssetModelCatalogueItems_TreeNode = TreeNode(
    node_for=[AssetModelCatalogue],
    children="AssetModelCatalogueItems",
    label="=AssetModelCatalogueItems",
    tooltip="",
    add=[AssetModelCatalogueItem],
    move=[AssetModelCatalogueItem],
    icon_path=IMAGE_PATH)

PotentialTransformerAssetModel_TreeNode = TreeNode(
    node_for=[PotentialTransformerAssetModel],
    label="name",
    tooltip="A particular model supplied by a manufacturer of a Potential Transformer (PT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PotentialTransformerAssetModel_PotentialTransformerAssets_TreeNode = TreeNode(
    node_for=[PotentialTransformerAssetModel],
    children="PotentialTransformerAssets",
    label="=PotentialTransformerAssets",
    tooltip="",
    add=[PotentialTransformerAsset],
    move=[PotentialTransformerAsset],
    icon_path=IMAGE_PATH)

BushingModel_TreeNode = TreeNode(
    node_for=[BushingModel],
    label="name",
    tooltip="Documentation for a type of a bushing of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerAssetModel_TreeNode = TreeNode(
    node_for=[TransformerAssetModel],
    label="name",
    tooltip="Documentation for a type of a transformer of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerAssetModel_TransformerAssets_TreeNode = TreeNode(
    node_for=[TransformerAssetModel],
    children="TransformerAssets",
    label="=TransformerAssets",
    tooltip="",
    add=[TransformerAsset],
    move=[TransformerAsset],
    icon_path=IMAGE_PATH)

TowerAssetModel_TreeNode = TreeNode(
    node_for=[TowerAssetModel],
    label="name",
    tooltip="A type of tower supplied by a given manufacturer or constructed from a common design.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TowerAssetModel_Towers_TreeNode = TreeNode(
    node_for=[TowerAssetModel],
    children="Towers",
    label="=Towers",
    tooltip="",
    add=[Tower],
    move=[Tower],
    icon_path=IMAGE_PATH)

CurrentTransformerAssetModel_TreeNode = TreeNode(
    node_for=[CurrentTransformerAssetModel],
    label="name",
    tooltip="A particular model supplied by a manufacturer of a Current Transformer (CT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CurrentTransformerAssetModel_CurrentTransformerAssets_TreeNode = TreeNode(
    node_for=[CurrentTransformerAssetModel],
    children="CurrentTransformerAssets",
    label="=CurrentTransformerAssets",
    tooltip="",
    add=[CurrentTransformerAsset],
    move=[CurrentTransformerAsset],
    icon_path=IMAGE_PATH)

PoleModel_TreeNode = TreeNode(
    node_for=[PoleModel],
    label="name",
    tooltip="A type of pole supplied by a given manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PoleModel_Poles_TreeNode = TreeNode(
    node_for=[PoleModel],
    children="Poles",
    label="=Poles",
    tooltip="",
    add=[Pole],
    move=[Pole],
    icon_path=IMAGE_PATH)

FaultIndicatorAssetModel_TreeNode = TreeNode(
    node_for=[FaultIndicatorAssetModel],
    label="name",
    tooltip="Documentation for a type of an FaultIndicator asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FaultIndicatorAssetModel_FaultIndicatorAssets_TreeNode = TreeNode(
    node_for=[FaultIndicatorAssetModel],
    children="FaultIndicatorAssets",
    label="=FaultIndicatorAssets",
    tooltip="",
    add=[FaultIndicatorAsset],
    move=[FaultIndicatorAsset],
    icon_path=IMAGE_PATH)

AssetFunctionAssetModel_TreeNode = TreeNode(
    node_for=[AssetFunctionAssetModel],
    label="name",
    tooltip="Documentation for a type of an asset function of a particular product model made by a manufacturer.(Organisation). Asset Functions are typically component parts of Assets or Asset Containers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetFunctionAssetModel_AssetFunctions_TreeNode = TreeNode(
    node_for=[AssetFunctionAssetModel],
    children="AssetFunctions",
    label="=AssetFunctions",
    tooltip="",
    add=[AssetFunction],
    move=[AssetFunction],
    icon_path=IMAGE_PATH)

StreetlightAssetModel_TreeNode = TreeNode(
    node_for=[StreetlightAssetModel],
    label="name",
    tooltip="Documentation for a type of a streelight of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StreetlightAssetModel_Streetlights_TreeNode = TreeNode(
    node_for=[StreetlightAssetModel],
    children="Streetlights",
    label="=Streetlights",
    tooltip="",
    add=[Streetlight],
    move=[Streetlight],
    icon_path=IMAGE_PATH)
StreetlightAssetModel_StreetlightTypeAssets_TreeNode = TreeNode(
    node_for=[StreetlightAssetModel],
    children="StreetlightTypeAssets",
    label="=StreetlightTypeAssets",
    tooltip="",
    add=[StreetlightTypeAsset],
    move=[StreetlightTypeAsset],
    icon_path=IMAGE_PATH)

SeriesCompensatorAssetModel_TreeNode = TreeNode(
    node_for=[SeriesCompensatorAssetModel],
    label="name",
    tooltip="For application as a series capacitor or reactor, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConductorAssetModel_TreeNode = TreeNode(
    node_for=[ConductorAssetModel],
    label="name",
    tooltip="A type of conductor made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductorAssetModel_ConductorAssets_TreeNode = TreeNode(
    node_for=[ConductorAssetModel],
    children="ConductorAssets",
    label="=ConductorAssets",
    tooltip="",
    add=[ConductorAsset],
    move=[ConductorAsset],
    icon_path=IMAGE_PATH)

BusbarAssetModel_TreeNode = TreeNode(
    node_for=[BusbarAssetModel],
    label="name",
    tooltip="Documentation for a type of a busbar asset of a particular product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusbarAssetModel_BusbarAssets_TreeNode = TreeNode(
    node_for=[BusbarAssetModel],
    children="BusbarAssets",
    label="=BusbarAssets",
    tooltip="",
    add=[BusbarAsset],
    move=[BusbarAsset],
    icon_path=IMAGE_PATH)

EnergyTransaction_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    label="name",
    tooltip="Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EnergyTransaction_CurtailmentProfiles_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    children="CurtailmentProfiles",
    label="=CurtailmentProfiles",
    tooltip="An EnergyTransaction may be curtailed by any of the participating entities.",
    add=[CurtailmentProfile],
    move=[CurtailmentProfile],
    icon_path=IMAGE_PATH)
EnergyTransaction_EnergyTransId_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    children="EnergyTransId",
    label="=EnergyTransId",
    tooltip="",
    add=[TransactionBid],
    move=[TransactionBid],
    icon_path=IMAGE_PATH)
EnergyTransaction_EnergyPriceCurves_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    children="EnergyPriceCurves",
    label="=EnergyPriceCurves",
    tooltip="",
    add=[EnergyPriceCurve],
    move=[EnergyPriceCurve],
    icon_path=IMAGE_PATH)
EnergyTransaction_LossProfiles_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    children="LossProfiles",
    label="=LossProfiles",
    tooltip="An EnergyTransaction may have a LossProfile.",
    add=[LossProfile],
    move=[LossProfile],
    icon_path=IMAGE_PATH)
EnergyTransaction_EnergyProfiles_TreeNode = TreeNode(
    node_for=[EnergyTransaction],
    children="EnergyProfiles",
    label="=EnergyProfiles",
    tooltip="An EnergyTransaction must have at least one EnergyProfile.",
    add=[EnergyProfile],
    move=[EnergyProfile],
    icon_path=IMAGE_PATH)

Reserve_TreeNode = TreeNode(
    node_for=[Reserve],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Reserve_AreaReserveSpec_TreeNode = TreeNode(
    node_for=[Reserve],
    children="AreaReserveSpec",
    label="=AreaReserveSpec",
    tooltip="A Reserve type of energy transaction can count towards an area reserve specification.",
    add=[AreaReserveSpec],
    move=[AreaReserveSpec],
    icon_path=IMAGE_PATH)

AvailableTransmissionCapacity_TreeNode = TreeNode(
    node_for=[AvailableTransmissionCapacity],
    label="name",
    tooltip="Amount of possible flow by direction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AvailableTransmissionCapacity_ScheduleFor_TreeNode = TreeNode(
    node_for=[AvailableTransmissionCapacity],
    children="ScheduleFor",
    label="=ScheduleFor",
    tooltip="A transmission schedule posts the available transmission capacity for a transmission line.",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)

Block_TreeNode = TreeNode(
    node_for=[Block],
    label="name",
    tooltip="A block is a simple transaction type, with no additional relationships.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProfileData_TreeNode = TreeNode(
    node_for=[ProfileData],
        tooltip="Data for profile.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProfileData_Profile_TreeNode = TreeNode(
    node_for=[ProfileData],
    children="Profile",
    label="=Profile",
    tooltip="A profile has profile data associated with it.",
    add=[Profile],
    move=[Profile],
    icon_path=IMAGE_PATH)

Profile_TreeNode = TreeNode(
    node_for=[Profile],
    label="name",
    tooltip="A profile is a simpler curve type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Profile_ProfileDatas_TreeNode = TreeNode(
    node_for=[Profile],
    children="ProfileDatas",
    label="=ProfileDatas",
    tooltip="A profile has profile data associated with it.",
    add=[ProfileData],
    move=[ProfileData],
    icon_path=IMAGE_PATH)

LossProfile_TreeNode = TreeNode(
    node_for=[LossProfile],
    label="name",
    tooltip="LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurtailmentProfile_TreeNode = TreeNode(
    node_for=[CurtailmentProfile],
    label="name",
    tooltip="Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SubControlArea_TreeNode = TreeNode(
    node_for=[SubControlArea],
    label="name",
    tooltip="SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubControlArea_Flowgate_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="Flowgate",
    label="=Flowgate",
    tooltip="A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)
SubControlArea_Export_EnergyTransactions_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="Export_EnergyTransactions",
    label="=Export_EnergyTransactions",
    tooltip="Energy is transferred between interchange areas",
    add=[EnergyTransaction],
    move=[EnergyTransaction],
    icon_path=IMAGE_PATH)
SubControlArea_Import_EnergyTransactions_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="Import_EnergyTransactions",
    label="=Import_EnergyTransactions",
    tooltip="Energy is transferred between interchange areas",
    add=[EnergyTransaction],
    move=[EnergyTransaction],
    icon_path=IMAGE_PATH)
SubControlArea_PartOf_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="PartOf",
    label="=PartOf",
    tooltip="A transmission path's service point is part of an interchange area",
    add=[ServicePoint],
    move=[ServicePoint],
    icon_path=IMAGE_PATH)
SubControlArea_SideA_TieLines_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="SideA_TieLines",
    label="=SideA_TieLines",
    tooltip="The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)
SubControlArea_GeneratingUnits_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="GeneratingUnits",
    label="=GeneratingUnits",
    tooltip="A GeneratingUnit injects energy into a SubControlArea.",
    add=[GeneratingUnit],
    move=[GeneratingUnit],
    icon_path=IMAGE_PATH)
SubControlArea_SideB_TieLines_TreeNode = TreeNode(
    node_for=[SubControlArea],
    children="SideB_TieLines",
    label="=SideB_TieLines",
    tooltip="The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)

TransmissionRightOfWay_TreeNode = TreeNode(
    node_for=[TransmissionRightOfWay],
    label="name",
    tooltip="A collection of transmission lines that are close proximity to each other.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionRightOfWay_Lines_TreeNode = TreeNode(
    node_for=[TransmissionRightOfWay],
    children="Lines",
    label="=Lines",
    tooltip="A transmission line can be part of a transmission corridor",
    add=[Line],
    move=[Line],
    icon_path=IMAGE_PATH)

EnergySchedulingVersion_TreeNode = TreeNode(
    node_for=[EnergySchedulingVersion],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Dynamic_TreeNode = TreeNode(
    node_for=[Dynamic],
    label="name",
    tooltip="A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Dynamic_TieLines_TreeNode = TreeNode(
    node_for=[Dynamic],
    children="TieLines",
    label="=TieLines",
    tooltip="A dynamic energy transaction can act as a pseudo tie line.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)

EnergyProfile_TreeNode = TreeNode(
    node_for=[EnergyProfile],
    label="name",
    tooltip="Specifies the start time, stop time, level for an EnergyTransaction.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HostControlArea_TreeNode = TreeNode(
    node_for=[HostControlArea],
    label="name",
    tooltip="A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HostControlArea_InadvertentAccounts_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="InadvertentAccounts",
    label="=InadvertentAccounts",
    tooltip="A control area can have one or more net inadvertent interchange accounts",
    add=[InadvertentAccount],
    move=[InadvertentAccount],
    icon_path=IMAGE_PATH)
HostControlArea_SideA_TieLines_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="SideA_TieLines",
    label="=SideA_TieLines",
    tooltip="A HostControlArea can have zero or more tie lines.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)
HostControlArea_SubControlAreas_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="SubControlAreas",
    label="=SubControlAreas",
    tooltip="The interchange area  may operate as a control area",
    add=[SubControlArea],
    move=[SubControlArea],
    icon_path=IMAGE_PATH)
HostControlArea_SideB_TieLines_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="SideB_TieLines",
    label="=SideB_TieLines",
    tooltip="A HostControlArea can have zero or more tie lines.",
    add=[TieLine],
    move=[TieLine],
    icon_path=IMAGE_PATH)
HostControlArea_Receive_DynamicSchedules_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="Receive_DynamicSchedules",
    label="=Receive_DynamicSchedules",
    tooltip="A control area can receive dynamic schedules from other control areas",
    add=[DynamicSchedule],
    move=[DynamicSchedule],
    icon_path=IMAGE_PATH)
HostControlArea_Send_DynamicSchedules_TreeNode = TreeNode(
    node_for=[HostControlArea],
    children="Send_DynamicSchedules",
    label="=Send_DynamicSchedules",
    tooltip="A control area can send dynamic schedules to other control areas",
    add=[DynamicSchedule],
    move=[DynamicSchedule],
    icon_path=IMAGE_PATH)

InadvertentAccount_TreeNode = TreeNode(
    node_for=[InadvertentAccount],
    label="name",
    tooltip="An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransmissionCorridor_TreeNode = TreeNode(
    node_for=[TransmissionCorridor],
    label="name",
    tooltip="A corridor containing one or more rights of way",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionCorridor_TransmissionRightOfWays_TreeNode = TreeNode(
    node_for=[TransmissionCorridor],
    children="TransmissionRightOfWays",
    label="=TransmissionRightOfWays",
    tooltip="A transmission right-of-way is a member of a transmission corridor",
    add=[TransmissionRightOfWay],
    move=[TransmissionRightOfWay],
    icon_path=IMAGE_PATH)
TransmissionCorridor_ContainedIn_TreeNode = TreeNode(
    node_for=[TransmissionCorridor],
    children="ContainedIn",
    label="=ContainedIn",
    tooltip="A TransmissionPath is contained in a TransmissionCorridor.",
    add=[TransmissionPath],
    move=[TransmissionPath],
    icon_path=IMAGE_PATH)

AreaReserveSpec_TreeNode = TreeNode(
    node_for=[AreaReserveSpec],
        tooltip="The control area's reserve specification",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AreaReserveSpec_HostControlAreas_TreeNode = TreeNode(
    node_for=[AreaReserveSpec],
    children="HostControlAreas",
    label="=HostControlAreas",
    tooltip="A control area has one or more area reserve specifications",
    add=[HostControlArea],
    move=[HostControlArea],
    icon_path=IMAGE_PATH)

EnergyProduct_TreeNode = TreeNode(
    node_for=[EnergyProduct],
    label="name",
    tooltip="An EnergyProduct is offered commercially as a ContractOrTariff.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EnergyProduct_ServicePoint_TreeNode = TreeNode(
    node_for=[EnergyProduct],
    children="ServicePoint",
    label="=ServicePoint",
    tooltip="An EnergyProduct injects energy into a service point.",
    add=[ServicePoint],
    move=[ServicePoint],
    icon_path=IMAGE_PATH)
EnergyProduct_EnergyTransactions_TreeNode = TreeNode(
    node_for=[EnergyProduct],
    children="EnergyTransactions",
    label="=EnergyTransactions",
    tooltip="The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.",
    add=[EnergyTransaction],
    move=[EnergyTransaction],
    icon_path=IMAGE_PATH)
EnergyProduct_ResoldBy_Marketers_TreeNode = TreeNode(
    node_for=[EnergyProduct],
    children="ResoldBy_Marketers",
    label="=ResoldBy_Marketers",
    tooltip="A Marketer may resell an EnergyProduct.",
    add=[Marketer],
    move=[Marketer],
    icon_path=IMAGE_PATH)

TieLine_TreeNode = TreeNode(
    node_for=[TieLine],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TieLine_ControlAreaOperators_TreeNode = TreeNode(
    node_for=[TieLine],
    children="ControlAreaOperators",
    label="=ControlAreaOperators",
    tooltip="A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.",
    add=[ControlAreaOperator],
    move=[ControlAreaOperator],
    icon_path=IMAGE_PATH)

DynamicSchedule_TreeNode = TreeNode(
    node_for=[DynamicSchedule],
    label="name",
    tooltip="A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Role_TreeNode = TreeNode(
    node_for=[Role],
    label="name",
    tooltip="Enumeration of potential roles that might be played by one object relative to another.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ScheduledEvent_TreeNode = TreeNode(
    node_for=[ScheduledEvent],
    label="name",
    tooltip="Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ScheduledEvent_Assets_TreeNode = TreeNode(
    node_for=[ScheduledEvent],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)

Skill_TreeNode = TreeNode(
    node_for=[Skill],
    label="name",
    tooltip="Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Skill_Crafts_TreeNode = TreeNode(
    node_for=[Skill],
    children="Crafts",
    label="=Crafts",
    tooltip="",
    add=[Craft],
    move=[Craft],
    icon_path=IMAGE_PATH)
Skill_QualificationRequirements_TreeNode = TreeNode(
    node_for=[Skill],
    children="QualificationRequirements",
    label="=QualificationRequirements",
    tooltip="",
    add=[QualificationRequirement],
    move=[QualificationRequirement],
    icon_path=IMAGE_PATH)

BankAccount_TreeNode = TreeNode(
    node_for=[BankAccount],
    label="name",
    tooltip="Bank account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BankAccount_BankStatements_TreeNode = TreeNode(
    node_for=[BankAccount],
    children="BankStatements",
    label="=BankStatements",
    tooltip="All bank statements generated from this bank account.",
    add=[BankStatement],
    move=[BankStatement],
    icon_path=IMAGE_PATH)

MarketRole_TreeNode = TreeNode(
    node_for=[MarketRole],
    label="name",
    tooltip="Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketRole_Organisations_TreeNode = TreeNode(
    node_for=[MarketRole],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[Organisation],
    move=[Organisation],
    icon_path=IMAGE_PATH)

Diagram_TreeNode = TreeNode(
    node_for=[Diagram],
    label="name",
    tooltip="GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Diagram_GmlDiagramObjects_TreeNode = TreeNode(
    node_for=[Diagram],
    children="GmlDiagramObjects",
    label="=GmlDiagramObjects",
    tooltip="",
    add=[GmlDiagramObject],
    move=[GmlDiagramObject],
    icon_path=IMAGE_PATH)
Diagram_DesignLocations_TreeNode = TreeNode(
    node_for=[Diagram],
    children="DesignLocations",
    label="=DesignLocations",
    tooltip="",
    add=[DesignLocation],
    move=[DesignLocation],
    icon_path=IMAGE_PATH)

Map_TreeNode = TreeNode(
    node_for=[Map],
    label="name",
    tooltip="A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DocPsrRole_TreeNode = TreeNode(
    node_for=[DocPsrRole],
    label="name",
    tooltip="Potential roles that might played by a document relative to a type of PowerSystemResource.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Ratio_TreeNode = TreeNode(
    node_for=[Ratio],
        tooltip="Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DocDocRole_TreeNode = TreeNode(
    node_for=[DocDocRole],
    label="name",
    tooltip="Roles played between Documents and other Documents.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusinessPlan_TreeNode = TreeNode(
    node_for=[BusinessPlan],
    label="name",
    tooltip="A BusinessPlan is an organized sequence of predetermined actions required to complete a future organizational objective. It is a type of document that typically references a schedule, physical and/or logical resources (assets and/or PowerSystemResources), locations, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusinessRole_TreeNode = TreeNode(
    node_for=[BusinessRole],
    label="name",
    tooltip="A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusinessRole_Organisations_TreeNode = TreeNode(
    node_for=[BusinessRole],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[Organisation],
    move=[Organisation],
    icon_path=IMAGE_PATH)

Craft_TreeNode = TreeNode(
    node_for=[Craft],
    label="name",
    tooltip="Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Craft_Skills_TreeNode = TreeNode(
    node_for=[Craft],
    children="Skills",
    label="=Skills",
    tooltip="",
    add=[Skill],
    move=[Skill],
    icon_path=IMAGE_PATH)
Craft_ErpPersons_TreeNode = TreeNode(
    node_for=[Craft],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)
Craft_Capabilities_TreeNode = TreeNode(
    node_for=[Craft],
    children="Capabilities",
    label="=Capabilities",
    tooltip="",
    add=[Capability],
    move=[Capability],
    icon_path=IMAGE_PATH)

ScheduleParameterInfo_TreeNode = TreeNode(
    node_for=[ScheduleParameterInfo],
    label="name",
    tooltip="Schedule parameters for an activity that is to occur, is occurring, or has completed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ScheduleParameterInfo_ScheduledEvents_TreeNode = TreeNode(
    node_for=[ScheduleParameterInfo],
    children="ScheduledEvents",
    label="=ScheduledEvents",
    tooltip="",
    add=[ScheduledEvent],
    move=[ScheduledEvent],
    icon_path=IMAGE_PATH)
ScheduleParameterInfo_Documents_TreeNode = TreeNode(
    node_for=[ScheduleParameterInfo],
    children="Documents",
    label="=Documents",
    tooltip="",
    add=[Document],
    move=[Document],
    icon_path=IMAGE_PATH)

ContingencyConstraintLimit_TreeNode = TreeNode(
    node_for=[ContingencyConstraintLimit],
    label="name",
    tooltip="Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a constraint for a specific contingency. Use CurveSchedule XAxisUnits to specify MW or MVA.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ResourceGroupReq_TreeNode = TreeNode(
    node_for=[ResourceGroupReq],
    label="name",
    tooltip="Ancillary service requirements for a market.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ResourceGroupReq_RTOs_TreeNode = TreeNode(
    node_for=[ResourceGroupReq],
    children="RTOs",
    label="=RTOs",
    tooltip="",
    add=[RTO],
    move=[RTO],
    icon_path=IMAGE_PATH)

ReserveReq_TreeNode = TreeNode(
    node_for=[ReserveReq],
    label="name",
    tooltip="Requirements for minimum amount of reserve and/or regulation to be supplied by a set of qualified resources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MarketFactors_TreeNode = TreeNode(
    node_for=[MarketFactors],
    label="name",
    tooltip="Aggregation of market information relative for a specific time interval.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketFactors_ErpInvoices_TreeNode = TreeNode(
    node_for=[MarketFactors],
    children="ErpInvoices",
    label="=ErpInvoices",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)

Settlement_TreeNode = TreeNode(
    node_for=[Settlement],
    label="name",
    tooltip="Specifies a settlement run.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Settlement_ErpLedgerEntries_TreeNode = TreeNode(
    node_for=[Settlement],
    children="ErpLedgerEntries",
    label="=ErpLedgerEntries",
    tooltip="",
    add=[ErpLedgerEntry],
    move=[ErpLedgerEntry],
    icon_path=IMAGE_PATH)
Settlement_ErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[Settlement],
    children="ErpInvoiceLineItems",
    label="=ErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)

ConstraintTerm_TreeNode = TreeNode(
    node_for=[ConstraintTerm],
    label="name",
    tooltip="A constraint term is one element of a linear constraint.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TerminalConstraintTerm_TreeNode = TreeNode(
    node_for=[TerminalConstraintTerm],
    label="name",
    tooltip="A constraint term associated with a specific terminal on a physical piece of equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LossPenaltyFactor_TreeNode = TreeNode(
    node_for=[LossPenaltyFactor],
    label="name",
    tooltip="Loss penalty factor applied to a ConnectivityNode for a given time interval.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LossPenaltyFactor_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[LossPenaltyFactor],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

PnodeClearing_TreeNode = TreeNode(
    node_for=[PnodeClearing],
    label="name",
    tooltip="Pricing node clearing results posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Meter_TreeNode = TreeNode(
    node_for=[Meter],
    label="name",
    tooltip="This is generic logical meter object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergyPriceCurve_TreeNode = TreeNode(
    node_for=[EnergyPriceCurve],
    label="name",
    tooltip="Relationship between a price in $/hour (Y-axis) and a MW value (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EnergyPriceCurve_EnergyTransactions_TreeNode = TreeNode(
    node_for=[EnergyPriceCurve],
    children="EnergyTransactions",
    label="=EnergyTransactions",
    tooltip="",
    add=[EnergyTransaction],
    move=[EnergyTransaction],
    icon_path=IMAGE_PATH)
EnergyPriceCurve_FTRs_TreeNode = TreeNode(
    node_for=[EnergyPriceCurve],
    children="FTRs",
    label="=FTRs",
    tooltip="",
    add=[FTR],
    move=[FTR],
    icon_path=IMAGE_PATH)

MarketStatement_TreeNode = TreeNode(
    node_for=[MarketStatement],
    label="name",
    tooltip="A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketStatement_MarketStatementLineItem_TreeNode = TreeNode(
    node_for=[MarketStatement],
    children="MarketStatementLineItem",
    label="=MarketStatementLineItem",
    tooltip="",
    add=[MarketStatementLineItem],
    move=[MarketStatementLineItem],
    icon_path=IMAGE_PATH)

StartUpTimeCurve_TreeNode = TreeNode(
    node_for=[StartUpTimeCurve],
    label="name",
    tooltip="Startup time curve as a function of down time, where time is specified in seconds.  Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StartUpTimeCurve_GeneratingBids_TreeNode = TreeNode(
    node_for=[StartUpTimeCurve],
    children="GeneratingBids",
    label="=GeneratingBids",
    tooltip="",
    add=[GeneratingBid],
    move=[GeneratingBid],
    icon_path=IMAGE_PATH)

Bid_TreeNode = TreeNode(
    node_for=[Bid],
    label="name",
    tooltip="Represents both bids to purchase and offers to sell energy or ancillary services in an RTO-sponsored market.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Bid_ProductBids_TreeNode = TreeNode(
    node_for=[Bid],
    children="ProductBids",
    label="=ProductBids",
    tooltip="A bid comprises one or more product bids of market products",
    add=[ProductBid],
    move=[ProductBid],
    icon_path=IMAGE_PATH)

ResourceBid_TreeNode = TreeNode(
    node_for=[ResourceBid],
    label="name",
    tooltip="Energy bid for generation, load, or virtual type for the whole of the market-trading period (i.e., one day in day ahead market or one hour in the real time market)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadBid_TreeNode = TreeNode(
    node_for=[LoadBid],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BidClearing_TreeNode = TreeNode(
    node_for=[BidClearing],
        tooltip="Bid clearing results posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeneratingBid_TreeNode = TreeNode(
    node_for=[GeneratingBid],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ResourceGroup_TreeNode = TreeNode(
    node_for=[ResourceGroup],
    label="name",
    tooltip="A logical grouping of resources that are used to model location of types of requirements for ancillary services such as spinning reserve zones, regulation zones, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ResourceGroup_RegisteredResources_TreeNode = TreeNode(
    node_for=[ResourceGroup],
    children="RegisteredResources",
    label="=RegisteredResources",
    tooltip="",
    add=[RegisteredResource],
    move=[RegisteredResource],
    icon_path=IMAGE_PATH)
ResourceGroup_ResourceGroupReqs_TreeNode = TreeNode(
    node_for=[ResourceGroup],
    children="ResourceGroupReqs",
    label="=ResourceGroupReqs",
    tooltip="",
    add=[ResourceGroupReq],
    move=[ResourceGroupReq],
    icon_path=IMAGE_PATH)

PassThroughBill_TreeNode = TreeNode(
    node_for=[PassThroughBill],
    label="name",
    tooltip="Pass Through Bill is used for: 1)Two sided charge transactions with or without ISO involvement (hence the ?pass thru?) 2) Specific direct charges or payments that are calculated outside or provided directly to settlements 3) Specific charge bill determinants that are externally supplied and used in charge calculations",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PassThroughBill_UserAttributes_TreeNode = TreeNode(
    node_for=[PassThroughBill],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
PassThroughBill_ChargeProfiles_TreeNode = TreeNode(
    node_for=[PassThroughBill],
    children="ChargeProfiles",
    label="=ChargeProfiles",
    tooltip="",
    add=[ChargeProfile],
    move=[ChargeProfile],
    icon_path=IMAGE_PATH)

SchedulingCoordinator_TreeNode = TreeNode(
    node_for=[SchedulingCoordinator],
    label="name",
    tooltip="In certain ISO/RTO operations, market participants are represented by Scheduling Coordinators (SCs) that are registered with the ISO/RTO. One participant can register multiple SCs with the ISO/RTO.  Many participants can do business with the ISO/RTO using a single SC. Each generator resource can only be scheduled by one SC. One SC can schedule multiple generators. A load scheduling point can be used by multiple SCs. Each SC can schedule load at multiple scheduling points. Each SC can have more than one load schedule at any load scheduling point as long as each load schedule at the same load scheduling point has a separate resource ID and settlement-quality meter. An inter-tie scheduling point can be used by multiple SCs. Each SC can schedule interchange at multiple inter-tie scheduling points. An SC can have multiple interchange schedules at the same inter-tie scheduling point by assigning a unique interchange identifier to each interchange schedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RampRateCurve_TreeNode = TreeNode(
    node_for=[RampRateCurve],
    label="name",
    tooltip="Ramp rate as a function of resource MW output",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RampRateCurve_GeneratingUnit_TreeNode = TreeNode(
    node_for=[RampRateCurve],
    children="GeneratingUnit",
    label="=GeneratingUnit",
    tooltip="",
    add=[RegisteredGenerator],
    move=[RegisteredGenerator],
    icon_path=IMAGE_PATH)

ProductBid_TreeNode = TreeNode(
    node_for=[ProductBid],
    label="name",
    tooltip="Component of a bid that pertains to one market product.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DefaultConstraintLimit_TreeNode = TreeNode(
    node_for=[DefaultConstraintLimit],
    label="name",
    tooltip="Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) applied as a default value if no specific constraint limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ChargeProfile_TreeNode = TreeNode(
    node_for=[ChargeProfile],
    label="name",
    tooltip="A type of profile for financial charges",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ChargeProfile_ChargeProfileData_TreeNode = TreeNode(
    node_for=[ChargeProfile],
    children="ChargeProfileData",
    label="=ChargeProfileData",
    tooltip="",
    add=[ChargeProfileData],
    move=[ChargeProfileData],
    icon_path=IMAGE_PATH)

MarketStatementLineItem_TreeNode = TreeNode(
    node_for=[MarketStatementLineItem],
    label="name",
    tooltip="An individual line item on a statement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketStatementLineItem_ComponentMarketStatementLineItem_TreeNode = TreeNode(
    node_for=[MarketStatementLineItem],
    children="ComponentMarketStatementLineItem",
    label="=ComponentMarketStatementLineItem",
    tooltip="",
    add=[MarketStatementLineItem],
    move=[MarketStatementLineItem],
    icon_path=IMAGE_PATH)
MarketStatementLineItem_UserAttributes_TreeNode = TreeNode(
    node_for=[MarketStatementLineItem],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)

RegisteredResource_TreeNode = TreeNode(
    node_for=[RegisteredResource],
    label="name",
    tooltip="A resource that is registered through the RTO participant registration system. Examples include generating unit, customer meter, and a non-physical generator or load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegisteredResource_Meters_TreeNode = TreeNode(
    node_for=[RegisteredResource],
    children="Meters",
    label="=Meters",
    tooltip="",
    add=[Meter],
    move=[Meter],
    icon_path=IMAGE_PATH)
RegisteredResource_Markets_TreeNode = TreeNode(
    node_for=[RegisteredResource],
    children="Markets",
    label="=Markets",
    tooltip="",
    add=[Market],
    move=[Market],
    icon_path=IMAGE_PATH)
RegisteredResource_ResourceGroups_TreeNode = TreeNode(
    node_for=[RegisteredResource],
    children="ResourceGroups",
    label="=ResourceGroups",
    tooltip="",
    add=[ResourceGroup],
    move=[ResourceGroup],
    icon_path=IMAGE_PATH)
RegisteredResource_MarketProducts_TreeNode = TreeNode(
    node_for=[RegisteredResource],
    children="MarketProducts",
    label="=MarketProducts",
    tooltip="A registered resource is eligible to bid market products",
    add=[MarketProduct],
    move=[MarketProduct],
    icon_path=IMAGE_PATH)

RegisteredGenerator_TreeNode = TreeNode(
    node_for=[RegisteredGenerator],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegisteredGenerator_UnitInitialConditions_TreeNode = TreeNode(
    node_for=[RegisteredGenerator],
    children="UnitInitialConditions",
    label="=UnitInitialConditions",
    tooltip="",
    add=[UnitInitialConditions],
    move=[UnitInitialConditions],
    icon_path=IMAGE_PATH)
RegisteredGenerator_RampRateCurves_TreeNode = TreeNode(
    node_for=[RegisteredGenerator],
    children="RampRateCurves",
    label="=RampRateCurves",
    tooltip="",
    add=[RampRateCurve],
    move=[RampRateCurve],
    icon_path=IMAGE_PATH)
RegisteredGenerator_GeneratingBids_TreeNode = TreeNode(
    node_for=[RegisteredGenerator],
    children="GeneratingBids",
    label="=GeneratingBids",
    tooltip="",
    add=[GeneratingBid],
    move=[GeneratingBid],
    icon_path=IMAGE_PATH)
RegisteredGenerator_StartUpCostCurves_TreeNode = TreeNode(
    node_for=[RegisteredGenerator],
    children="StartUpCostCurves",
    label="=StartUpCostCurves",
    tooltip="",
    add=[StartUpCostCurve],
    move=[StartUpCostCurve],
    icon_path=IMAGE_PATH)

Market_TreeNode = TreeNode(
    node_for=[Market],
    label="name",
    tooltip="Market (e.g., DAM, HAM)  zzMarket operation control parameters.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Market_Bids_TreeNode = TreeNode(
    node_for=[Market],
    children="Bids",
    label="=Bids",
    tooltip="",
    add=[Bid],
    move=[Bid],
    icon_path=IMAGE_PATH)
Market_MarketProducts_TreeNode = TreeNode(
    node_for=[Market],
    children="MarketProducts",
    label="=MarketProducts",
    tooltip="",
    add=[MarketProduct],
    move=[MarketProduct],
    icon_path=IMAGE_PATH)
Market_RegisteredResources_TreeNode = TreeNode(
    node_for=[Market],
    children="RegisteredResources",
    label="=RegisteredResources",
    tooltip="",
    add=[RegisteredResource],
    move=[RegisteredResource],
    icon_path=IMAGE_PATH)
Market_Settlements_TreeNode = TreeNode(
    node_for=[Market],
    children="Settlements",
    label="=Settlements",
    tooltip="",
    add=[Settlement],
    move=[Settlement],
    icon_path=IMAGE_PATH)
Market_MarketFactors_TreeNode = TreeNode(
    node_for=[Market],
    children="MarketFactors",
    label="=MarketFactors",
    tooltip="",
    add=[MarketFactors],
    move=[MarketFactors],
    icon_path=IMAGE_PATH)

MarketCaseClearing_TreeNode = TreeNode(
    node_for=[MarketCaseClearing],
    label="name",
    tooltip="Market case clearing results are posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketCaseClearing_AncillaryServiceClearing_TreeNode = TreeNode(
    node_for=[MarketCaseClearing],
    children="AncillaryServiceClearing",
    label="=AncillaryServiceClearing",
    tooltip="",
    add=[AncillaryServiceClearing],
    move=[AncillaryServiceClearing],
    icon_path=IMAGE_PATH)

RegisteredLoad_TreeNode = TreeNode(
    node_for=[RegisteredLoad],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegisteredLoad_LoadBids_TreeNode = TreeNode(
    node_for=[RegisteredLoad],
    children="LoadBids",
    label="=LoadBids",
    tooltip="",
    add=[LoadBid],
    move=[LoadBid],
    icon_path=IMAGE_PATH)

Pnode_TreeNode = TreeNode(
    node_for=[Pnode],
    label="name",
    tooltip="A pricing node is directly associated with a connectivity node.  It is a pricing location for which market participants submit their bids, offers, buy/sell CRRs, and settle.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Pnode_DeliveryTransactionBids_TreeNode = TreeNode(
    node_for=[Pnode],
    children="DeliveryTransactionBids",
    label="=DeliveryTransactionBids",
    tooltip="",
    add=[TransactionBid],
    move=[TransactionBid],
    icon_path=IMAGE_PATH)
Pnode_Measurements_TreeNode = TreeNode(
    node_for=[Pnode],
    children="Measurements",
    label="=Measurements",
    tooltip="",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
Pnode_ReceiptTransactionBids_TreeNode = TreeNode(
    node_for=[Pnode],
    children="ReceiptTransactionBids",
    label="=ReceiptTransactionBids",
    tooltip="",
    add=[TransactionBid],
    move=[TransactionBid],
    icon_path=IMAGE_PATH)
Pnode_FTRs_TreeNode = TreeNode(
    node_for=[Pnode],
    children="FTRs",
    label="=FTRs",
    tooltip="",
    add=[FTR],
    move=[FTR],
    icon_path=IMAGE_PATH)
Pnode_RegisteredResources_TreeNode = TreeNode(
    node_for=[Pnode],
    children="RegisteredResources",
    label="=RegisteredResources",
    tooltip="A registered resource injects power at one or more connectivity nodes related to a pnode",
    add=[RegisteredResource],
    move=[RegisteredResource],
    icon_path=IMAGE_PATH)

AncillaryServiceClearing_TreeNode = TreeNode(
    node_for=[AncillaryServiceClearing],
    label="name",
    tooltip="Ancillary services clearing results are posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BaseCaseConstraintLimit_TreeNode = TreeNode(
    node_for=[BaseCaseConstraintLimit],
    label="name",
    tooltip="Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the BaseCaseConstraintLimit differs from the DefaultConstraintLimit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FTR_TreeNode = TreeNode(
    node_for=[FTR],
    label="name",
    tooltip="Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FTR_Pnodes_TreeNode = TreeNode(
    node_for=[FTR],
    children="Pnodes",
    label="=Pnodes",
    tooltip="",
    add=[Pnode],
    move=[Pnode],
    icon_path=IMAGE_PATH)

NodeConstraintTerm_TreeNode = TreeNode(
    node_for=[NodeConstraintTerm],
    label="name",
    tooltip="To be used only to constrain a quantity that cannot be associated with a terminal. For example, a registered generating unit that is not electrically connected to the network.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReserveReqCurve_TreeNode = TreeNode(
    node_for=[ReserveReqCurve],
    label="name",
    tooltip="A curve relating  reserve requirement versus time, showing the values of a specific reserve requirement for each unit of the period covered. The  curve can be based on 'absolute' time or on 'normalized' time.  X is time, typically expressed in absolute time Y1 is reserve requirement, typically expressed in MW",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SecurityConstraints_TreeNode = TreeNode(
    node_for=[SecurityConstraints],
    label="name",
    tooltip="Typical for regional transmission operators (RTOs), these constraints include transmission as well as generation group constraints identified in both base case and critical contingency cases.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MWLimitSchedule_TreeNode = TreeNode(
    node_for=[MWLimitSchedule],
    label="name",
    tooltip="Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BidSet_TreeNode = TreeNode(
    node_for=[BidSet],
    label="name",
    tooltip="As set of mutually exclusive bids for which a maximum of one may be scheduled. Of these generating bids, only one generating bid can be scheduled at a time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BidSet_GeneratingBids_TreeNode = TreeNode(
    node_for=[BidSet],
    children="GeneratingBids",
    label="=GeneratingBids",
    tooltip="",
    add=[GeneratingBid],
    move=[GeneratingBid],
    icon_path=IMAGE_PATH)

ProductBidClearing_TreeNode = TreeNode(
    node_for=[ProductBidClearing],
    label="name",
    tooltip="Product Bid clearing results posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProductBidClearing_ProductBids_TreeNode = TreeNode(
    node_for=[ProductBidClearing],
    children="ProductBids",
    label="=ProductBids",
    tooltip="",
    add=[ProductBid],
    move=[ProductBid],
    icon_path=IMAGE_PATH)

TransmissionReliabilityMargin_TreeNode = TreeNode(
    node_for=[TransmissionReliabilityMargin],
    label="name",
    tooltip="Transmission Reliability Margin (TRM) is defined as that amount of transmission transfer capability necessary to ensure that the interconnected transmission network is secure under a reasonable range of uncertainties in system conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionReliabilityMargin_Flowgate_TreeNode = TreeNode(
    node_for=[TransmissionReliabilityMargin],
    children="Flowgate",
    label="=Flowgate",
    tooltip="A fowgate may have 0 to 1 TRM",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)

BidPriceCurve_TreeNode = TreeNode(
    node_for=[BidPriceCurve],
    label="name",
    tooltip="Relationship between unit operating price in $/hour (Y-axis) and unit output in MW (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BidPriceCurve_ProductBids_TreeNode = TreeNode(
    node_for=[BidPriceCurve],
    children="ProductBids",
    label="=ProductBids",
    tooltip="",
    add=[ProductBid],
    move=[ProductBid],
    icon_path=IMAGE_PATH)

BilateralTransaction_TreeNode = TreeNode(
    node_for=[BilateralTransaction],
        tooltip="Bilateral transaction",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransactionBid_TreeNode = TreeNode(
    node_for=[TransactionBid],
    label="name",
    tooltip="Bilateral or scheduled transactions for energy and ancillary services considered by market clearing process",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransactionBid_EnergyProfiles_TreeNode = TreeNode(
    node_for=[TransactionBid],
    children="EnergyProfiles",
    label="=EnergyProfiles",
    tooltip="",
    add=[EnergyProfile],
    move=[EnergyProfile],
    icon_path=IMAGE_PATH)

MarketProduct_TreeNode = TreeNode(
    node_for=[MarketProduct],
    label="name",
    tooltip="A product traded by an RTO (e.g., energy, 10 minute spinning reserve).  Ancillary service product examples include: Regulation Up Regulation Dn Spinning Reserve Non-Spinning Reserve Operating Reserve",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MarketProduct_RegisteredResources_TreeNode = TreeNode(
    node_for=[MarketProduct],
    children="RegisteredResources",
    label="=RegisteredResources",
    tooltip="A registered resource is eligible to bid market products",
    add=[RegisteredResource],
    move=[RegisteredResource],
    icon_path=IMAGE_PATH)
MarketProduct_ReserveReqs_TreeNode = TreeNode(
    node_for=[MarketProduct],
    children="ReserveReqs",
    label="=ReserveReqs",
    tooltip="Market product associated with reserve requirement must be a reserve or regulation product.",
    add=[ReserveReq],
    move=[ReserveReq],
    icon_path=IMAGE_PATH)
MarketProduct_ProductBids_TreeNode = TreeNode(
    node_for=[MarketProduct],
    children="ProductBids",
    label="=ProductBids",
    tooltip="",
    add=[ProductBid],
    move=[ProductBid],
    icon_path=IMAGE_PATH)

SecurityConstraintsClearing_TreeNode = TreeNode(
    node_for=[SecurityConstraintsClearing],
    label="name",
    tooltip="Binding security constrained clearing results posted for a given settlement period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Flowgate_TreeNode = TreeNode(
    node_for=[Flowgate],
    label="name",
    tooltip="A flowgate, is single or group of transmission elements intended to model MW flow impact relating to transmission limitations and transmission service usage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Flowgate_ViolationLimits_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="ViolationLimits",
    label="=ViolationLimits",
    tooltip="",
    add=[ViolationLimit],
    move=[ViolationLimit],
    icon_path=IMAGE_PATH)
Flowgate_TransmissionProvider_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="TransmissionProvider",
    label="=TransmissionProvider",
    tooltip="A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.",
    add=[TransmissionProvider],
    move=[TransmissionProvider],
    icon_path=IMAGE_PATH)
Flowgate_PowerTransormers_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="PowerTransormers",
    label="=PowerTransormers",
    tooltip="",
    add=[PowerTransformer],
    move=[PowerTransformer],
    icon_path=IMAGE_PATH)
Flowgate_Lines_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="Lines",
    label="=Lines",
    tooltip="",
    add=[Line],
    move=[Line],
    icon_path=IMAGE_PATH)
Flowgate_CapacityBenefitMargin_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="CapacityBenefitMargin",
    label="=CapacityBenefitMargin",
    tooltip="A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data",
    add=[CapacityBenefitMargin],
    move=[CapacityBenefitMargin],
    icon_path=IMAGE_PATH)
Flowgate_FTRs_TreeNode = TreeNode(
    node_for=[Flowgate],
    children="FTRs",
    label="=FTRs",
    tooltip="",
    add=[FTR],
    move=[FTR],
    icon_path=IMAGE_PATH)

ViolationLimit_TreeNode = TreeNode(
    node_for=[ViolationLimit],
    label="name",
    tooltip="A type of limit that indicates if it is enforced and, through association, the organisation responsible for setting the limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ViolationLimit_Organisations_TreeNode = TreeNode(
    node_for=[ViolationLimit],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[ErpOrganisation],
    move=[ErpOrganisation],
    icon_path=IMAGE_PATH)

SensitivityPriceCurve_TreeNode = TreeNode(
    node_for=[SensitivityPriceCurve],
    label="name",
    tooltip="Optionally, this curve expresses elasticity of the associated requirement.  For example, used to reduce requirements when clearing price exceeds reasonable values when the supply quantity becomes scarce.  For example, a single point value of $1000/MW for a spinning reserve will cause a reduction in the required spinning reserve.  X axis is constrained quantity (e.g., MW) Y1 axis is money per constrained quantity",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CapacityBenefitMargin_TreeNode = TreeNode(
    node_for=[CapacityBenefitMargin],
    label="name",
    tooltip="Capacity Benefit Margin (CBM) is defined as that amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. Reservation fo CBM by a load serving entity allows that entity to reduce its installed generating capacity below that which may otherwise have been necessary without interconnections to meet its generation reliability requirements.  CBM is modeled as a profile with values in different time periods which are represented by the profile data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CapacityBenefitMargin_Flowgate_TreeNode = TreeNode(
    node_for=[CapacityBenefitMargin],
    children="Flowgate",
    label="=Flowgate",
    tooltip="A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)

RTO_TreeNode = TreeNode(
    node_for=[RTO],
    label="name",
    tooltip="Regional transmission operator.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RTO_Pnodes_TreeNode = TreeNode(
    node_for=[RTO],
    children="Pnodes",
    label="=Pnodes",
    tooltip="",
    add=[Pnode],
    move=[Pnode],
    icon_path=IMAGE_PATH)
RTO_SecurityConstraints_TreeNode = TreeNode(
    node_for=[RTO],
    children="SecurityConstraints",
    label="=SecurityConstraints",
    tooltip="",
    add=[SecurityConstraints],
    move=[SecurityConstraints],
    icon_path=IMAGE_PATH)
RTO_SecurityConstraintsLinear_TreeNode = TreeNode(
    node_for=[RTO],
    children="SecurityConstraintsLinear",
    label="=SecurityConstraintsLinear",
    tooltip="",
    add=[SecurityConstraintSum],
    move=[SecurityConstraintSum],
    icon_path=IMAGE_PATH)
RTO_ResourceGroupReqs_TreeNode = TreeNode(
    node_for=[RTO],
    children="ResourceGroupReqs",
    label="=ResourceGroupReqs",
    tooltip="",
    add=[ResourceGroupReq],
    move=[ResourceGroupReq],
    icon_path=IMAGE_PATH)
RTO_Markets_TreeNode = TreeNode(
    node_for=[RTO],
    children="Markets",
    label="=Markets",
    tooltip="",
    add=[Market],
    move=[Market],
    icon_path=IMAGE_PATH)

LoadReductionPriceCurve_TreeNode = TreeNode(
    node_for=[LoadReductionPriceCurve],
    label="name",
    tooltip="This is the price sensitivity that bidder expresses for allowing market load interruption.  Relationship between price (Y1-axis) vs. MW (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadReductionPriceCurve_LoadBids_TreeNode = TreeNode(
    node_for=[LoadReductionPriceCurve],
    children="LoadBids",
    label="=LoadBids",
    tooltip="",
    add=[LoadBid],
    move=[LoadBid],
    icon_path=IMAGE_PATH)

BillDeterminant_TreeNode = TreeNode(
    node_for=[BillDeterminant],
    label="name",
    tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BillDeterminant_ChargeProfileData_TreeNode = TreeNode(
    node_for=[BillDeterminant],
    children="ChargeProfileData",
    label="=ChargeProfileData",
    tooltip="",
    add=[ChargeProfileData],
    move=[ChargeProfileData],
    icon_path=IMAGE_PATH)
BillDeterminant_UserAttributes_TreeNode = TreeNode(
    node_for=[BillDeterminant],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)

ChargeProfileData_TreeNode = TreeNode(
    node_for=[ChargeProfileData],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SecurityConstraintSum_TreeNode = TreeNode(
    node_for=[SecurityConstraintSum],
    label="name",
    tooltip="Typically provided by RTO systems, constraints identified in both base case and critical contingency cases have to be transferred. A constraint has N (>=1) constraint terms. A term is represented by an instance of TerminalConstraintTerm.  The constraint expression is: minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue where: - cn is ConstraintTerm.factor  - xn is the flow at the terminal Flow into the associated equipment is positive for the purpose of ConnectivityNode NodeConstraintTerm  k is SecurityConstraintsLinear.resourceMW The units of k are assumed to be same as the units of the flows, xn.  The constants, cn, are dimensionless. With these conventions, cn and k are all positive for a typical constraint such as 'weighted sum of generation must be less than limit'. Furthermore, cn are all 1.0 for a case such as 'interface flow must be less than limit', assuming the terminals are chosen on the importing side of the interface.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SecurityConstraintSum_ConstraintTerms_TreeNode = TreeNode(
    node_for=[SecurityConstraintSum],
    children="ConstraintTerms",
    label="=ConstraintTerms",
    tooltip="",
    add=[ConstraintTerm],
    move=[ConstraintTerm],
    icon_path=IMAGE_PATH)
SecurityConstraintSum_ContingencyConstraintLimits_TreeNode = TreeNode(
    node_for=[SecurityConstraintSum],
    children="ContingencyConstraintLimits",
    label="=ContingencyConstraintLimits",
    tooltip="",
    add=[ContingencyConstraintLimit],
    move=[ContingencyConstraintLimit],
    icon_path=IMAGE_PATH)

StartUpCostCurve_TreeNode = TreeNode(
    node_for=[StartUpCostCurve],
    label="name",
    tooltip="Startup costs and time as a function of down time.  Relationship between unit startup cost (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StartUpCostCurve_GeneratingBids_TreeNode = TreeNode(
    node_for=[StartUpCostCurve],
    children="GeneratingBids",
    label="=GeneratingBids",
    tooltip="",
    add=[GeneratingBid],
    move=[GeneratingBid],
    icon_path=IMAGE_PATH)
StartUpCostCurve_RegisteredGenerators_TreeNode = TreeNode(
    node_for=[StartUpCostCurve],
    children="RegisteredGenerators",
    label="=RegisteredGenerators",
    tooltip="",
    add=[RegisteredGenerator],
    move=[RegisteredGenerator],
    icon_path=IMAGE_PATH)

NotificationTimeCurve_TreeNode = TreeNode(
    node_for=[NotificationTimeCurve],
    label="name",
    tooltip="Notification time curve as a function of down time.  Relationship between crew notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

NotificationTimeCurve_GeneratingBids_TreeNode = TreeNode(
    node_for=[NotificationTimeCurve],
    children="GeneratingBids",
    label="=GeneratingBids",
    tooltip="",
    add=[GeneratingBid],
    move=[GeneratingBid],
    icon_path=IMAGE_PATH)

UnitInitialConditions_TreeNode = TreeNode(
    node_for=[UnitInitialConditions],
    label="name",
    tooltip="Resource status at the end of a given clearing period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlPosition_TreeNode = TreeNode(
    node_for=[GmlPosition],
        tooltip="Position point with a GML coordinate reference system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlLabelPlacement_TreeNode = TreeNode(
    node_for=[GmlLabelPlacement],
    label="name",
    tooltip="Used to position a label relative to a point or a line.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlLabelPlacement_GmlTextSymbols_TreeNode = TreeNode(
    node_for=[GmlLabelPlacement],
    children="GmlTextSymbols",
    label="=GmlTextSymbols",
    tooltip="",
    add=[GmlTextSymbol],
    move=[GmlTextSymbol],
    icon_path=IMAGE_PATH)

GmlTopologyStyle_TreeNode = TreeNode(
    node_for=[GmlTopologyStyle],
    label="name",
    tooltip="The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlSvgParameter_TreeNode = TreeNode(
    node_for=[GmlSvgParameter],
    label="name",
    tooltip="Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlSvgParameter_GmlStokes_TreeNode = TreeNode(
    node_for=[GmlSvgParameter],
    children="GmlStokes",
    label="=GmlStokes",
    tooltip="",
    add=[GmlStroke],
    move=[GmlStroke],
    icon_path=IMAGE_PATH)
GmlSvgParameter_GmlFills_TreeNode = TreeNode(
    node_for=[GmlSvgParameter],
    children="GmlFills",
    label="=GmlFills",
    tooltip="",
    add=[GmlFill],
    move=[GmlFill],
    icon_path=IMAGE_PATH)
GmlSvgParameter_GmlFonts_TreeNode = TreeNode(
    node_for=[GmlSvgParameter],
    children="GmlFonts",
    label="=GmlFonts",
    tooltip="",
    add=[GmlFont],
    move=[GmlFont],
    icon_path=IMAGE_PATH)

GmlMark_TreeNode = TreeNode(
    node_for=[GmlMark],
    label="name",
    tooltip="Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlMark_GmlFIlls_TreeNode = TreeNode(
    node_for=[GmlMark],
    children="GmlFIlls",
    label="=GmlFIlls",
    tooltip="",
    add=[GmlFill],
    move=[GmlFill],
    icon_path=IMAGE_PATH)
GmlMark_GmlGraphics_TreeNode = TreeNode(
    node_for=[GmlMark],
    children="GmlGraphics",
    label="=GmlGraphics",
    tooltip="",
    add=[GmlGraphic],
    move=[GmlGraphic],
    icon_path=IMAGE_PATH)
GmlMark_GmlStrokes_TreeNode = TreeNode(
    node_for=[GmlMark],
    children="GmlStrokes",
    label="=GmlStrokes",
    tooltip="",
    add=[GmlStroke],
    move=[GmlStroke],
    icon_path=IMAGE_PATH)

GmlFont_TreeNode = TreeNode(
    node_for=[GmlFont],
    label="name",
    tooltip="Identifies a font of a certain family, style, and size.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlFont_GmlTextSymbols_TreeNode = TreeNode(
    node_for=[GmlFont],
    children="GmlTextSymbols",
    label="=GmlTextSymbols",
    tooltip="",
    add=[GmlTextSymbol],
    move=[GmlTextSymbol],
    icon_path=IMAGE_PATH)
GmlFont_GmlSvgParameters_TreeNode = TreeNode(
    node_for=[GmlFont],
    children="GmlSvgParameters",
    label="=GmlSvgParameters",
    tooltip="",
    add=[GmlSvgParameter],
    move=[GmlSvgParameter],
    icon_path=IMAGE_PATH)

GmlSymbol_TreeNode = TreeNode(
    node_for=[GmlSymbol],
    label="name",
    tooltip="Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlSymbol_GmlFeatureStyles_TreeNode = TreeNode(
    node_for=[GmlSymbol],
    children="GmlFeatureStyles",
    label="=GmlFeatureStyles",
    tooltip="",
    add=[GmlFeatureStyle],
    move=[GmlFeatureStyle],
    icon_path=IMAGE_PATH)

GmlPointSymbol_TreeNode = TreeNode(
    node_for=[GmlPointSymbol],
    label="name",
    tooltip="Used to draw a 'graphic' at a point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlSelector_TreeNode = TreeNode(
    node_for=[GmlSelector],
    label="name",
    tooltip="A diagram element that allows selection by a user, i.e. as 'hyperNode' for navigating between diagrams, or as composite object representing multiple grouped objects.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlSelector_Locations_TreeNode = TreeNode(
    node_for=[GmlSelector],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)
GmlSelector_ChangeItems_TreeNode = TreeNode(
    node_for=[GmlSelector],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)

GmlGeometryStyle_TreeNode = TreeNode(
    node_for=[GmlGeometryStyle],
    label="name",
    tooltip="The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlDiagramObject_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    label="name",
    tooltip="Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlDiagramObject_Diagrams_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="Diagrams",
    label="=Diagrams",
    tooltip="",
    add=[Diagram],
    move=[Diagram],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlLineSymbols_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlLineSymbols",
    label="=GmlLineSymbols",
    tooltip="",
    add=[GmlLineSymbol],
    move=[GmlLineSymbol],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlCoordinateSystems_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlCoordinateSystems",
    label="=GmlCoordinateSystems",
    tooltip="",
    add=[GmlCoordinateSystem],
    move=[GmlCoordinateSystem],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlRasterSymbols_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlRasterSymbols",
    label="=GmlRasterSymbols",
    tooltip="",
    add=[GmlRasterSymbol],
    move=[GmlRasterSymbol],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlPolygonSymbols_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlPolygonSymbols",
    label="=GmlPolygonSymbols",
    tooltip="",
    add=[GmlPolygonSymbol],
    move=[GmlPolygonSymbol],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlPointSymbols_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlPointSymbols",
    label="=GmlPointSymbols",
    tooltip="",
    add=[GmlPointSymbol],
    move=[GmlPointSymbol],
    icon_path=IMAGE_PATH)
GmlDiagramObject_GmlTextSymbols_TreeNode = TreeNode(
    node_for=[GmlDiagramObject],
    children="GmlTextSymbols",
    label="=GmlTextSymbols",
    tooltip="",
    add=[GmlTextSymbol],
    move=[GmlTextSymbol],
    icon_path=IMAGE_PATH)

GmlPolygonGeometry_TreeNode = TreeNode(
    node_for=[GmlPolygonGeometry],
    label="name",
    tooltip="Used to show the footprint of substations, sites, service territories, tax districts, school districts, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlFeatureType_TreeNode = TreeNode(
    node_for=[GmlFeatureType],
    label="name",
    tooltip="Type classification of feature.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlFeatureType_GmlFeatureStyles_TreeNode = TreeNode(
    node_for=[GmlFeatureType],
    children="GmlFeatureStyles",
    label="=GmlFeatureStyles",
    tooltip="",
    add=[GmlFeatureStyle],
    move=[GmlFeatureStyle],
    icon_path=IMAGE_PATH)

GmlHalo_TreeNode = TreeNode(
    node_for=[GmlHalo],
    label="name",
    tooltip="A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlHalo_GmlTextSymbols_TreeNode = TreeNode(
    node_for=[GmlHalo],
    children="GmlTextSymbols",
    label="=GmlTextSymbols",
    tooltip="",
    add=[GmlTextSymbol],
    move=[GmlTextSymbol],
    icon_path=IMAGE_PATH)

GmlObservation_TreeNode = TreeNode(
    node_for=[GmlObservation],
        tooltip="A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlObservation_ChangeItems_TreeNode = TreeNode(
    node_for=[GmlObservation],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
GmlObservation_GmlValues_TreeNode = TreeNode(
    node_for=[GmlObservation],
    children="GmlValues",
    label="=GmlValues",
    tooltip="",
    add=[GmlValue],
    move=[GmlValue],
    icon_path=IMAGE_PATH)
GmlObservation_Locations_TreeNode = TreeNode(
    node_for=[GmlObservation],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

GmlPolygonSymbol_TreeNode = TreeNode(
    node_for=[GmlPolygonSymbol],
    label="name",
    tooltip="Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlLineSymbol_TreeNode = TreeNode(
    node_for=[GmlLineSymbol],
    label="name",
    tooltip="Used to style a 'stroke' along a linear geometry type, such as a string of line segments.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlBaseSymbol_TreeNode = TreeNode(
    node_for=[GmlBaseSymbol],
    label="name",
    tooltip="Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlBaseSymbol_GmlSymbols_TreeNode = TreeNode(
    node_for=[GmlBaseSymbol],
    children="GmlSymbols",
    label="=GmlSymbols",
    tooltip="",
    add=[GmlSymbol],
    move=[GmlSymbol],
    icon_path=IMAGE_PATH)

GmlValue_TreeNode = TreeNode(
    node_for=[GmlValue],
    label="name",
    tooltip="Used for direct representation of values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlFill_TreeNode = TreeNode(
    node_for=[GmlFill],
    label="name",
    tooltip="Specifies how the area of the geometry will be filled.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlFill_GmlPolygonSymbols_TreeNode = TreeNode(
    node_for=[GmlFill],
    children="GmlPolygonSymbols",
    label="=GmlPolygonSymbols",
    tooltip="",
    add=[GmlPolygonSymbol],
    move=[GmlPolygonSymbol],
    icon_path=IMAGE_PATH)
GmlFill_GmlSvgParameters_TreeNode = TreeNode(
    node_for=[GmlFill],
    children="GmlSvgParameters",
    label="=GmlSvgParameters",
    tooltip="",
    add=[GmlSvgParameter],
    move=[GmlSvgParameter],
    icon_path=IMAGE_PATH)
GmlFill_GmlMarks_TreeNode = TreeNode(
    node_for=[GmlFill],
    children="GmlMarks",
    label="=GmlMarks",
    tooltip="",
    add=[GmlMark],
    move=[GmlMark],
    icon_path=IMAGE_PATH)
GmlFill_GmlTextSymbols_TreeNode = TreeNode(
    node_for=[GmlFill],
    children="GmlTextSymbols",
    label="=GmlTextSymbols",
    tooltip="",
    add=[GmlTextSymbol],
    move=[GmlTextSymbol],
    icon_path=IMAGE_PATH)

GmlPointGeometry_TreeNode = TreeNode(
    node_for=[GmlPointGeometry],
    label="name",
    tooltip="Typically used for rendering power system resources and/or point assets.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlRasterSymbol_TreeNode = TreeNode(
    node_for=[GmlRasterSymbol],
    label="name",
    tooltip="Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlColour_TreeNode = TreeNode(
    node_for=[GmlColour],
    label="name",
    tooltip="The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlColour_GmlFills_TreeNode = TreeNode(
    node_for=[GmlColour],
    children="GmlFills",
    label="=GmlFills",
    tooltip="",
    add=[GmlFill],
    move=[GmlFill],
    icon_path=IMAGE_PATH)
GmlColour_GmlFonts_TreeNode = TreeNode(
    node_for=[GmlColour],
    children="GmlFonts",
    label="=GmlFonts",
    tooltip="",
    add=[GmlFont],
    move=[GmlFont],
    icon_path=IMAGE_PATH)
GmlColour_GmlStrokes_TreeNode = TreeNode(
    node_for=[GmlColour],
    children="GmlStrokes",
    label="=GmlStrokes",
    tooltip="",
    add=[GmlStroke],
    move=[GmlStroke],
    icon_path=IMAGE_PATH)

GmlLineGeometry_TreeNode = TreeNode(
    node_for=[GmlLineGeometry],
    label="name",
    tooltip="Typically used for rendering linear assets and/or power system resources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlTextSymbol_TreeNode = TreeNode(
    node_for=[GmlTextSymbol],
    label="name",
    tooltip="Used for styling text labels, i.e., for rendering them according to various graphical parameters.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GmlLabelStyle_TreeNode = TreeNode(
    node_for=[GmlLabelStyle],
    label="name",
    tooltip="The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlLabelStyle_GmlGeometryStyles_TreeNode = TreeNode(
    node_for=[GmlLabelStyle],
    children="GmlGeometryStyles",
    label="=GmlGeometryStyles",
    tooltip="",
    add=[GmlGeometryStyle],
    move=[GmlGeometryStyle],
    icon_path=IMAGE_PATH)
GmlLabelStyle_GmlTopologyStyles_TreeNode = TreeNode(
    node_for=[GmlLabelStyle],
    children="GmlTopologyStyles",
    label="=GmlTopologyStyles",
    tooltip="",
    add=[GmlTopologyStyle],
    move=[GmlTopologyStyle],
    icon_path=IMAGE_PATH)

GmlGraphic_TreeNode = TreeNode(
    node_for=[GmlGraphic],
    label="name",
    tooltip="A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlGraphic_GmlMarks_TreeNode = TreeNode(
    node_for=[GmlGraphic],
    children="GmlMarks",
    label="=GmlMarks",
    tooltip="",
    add=[GmlMark],
    move=[GmlMark],
    icon_path=IMAGE_PATH)
GmlGraphic_GmlPointSymbols_TreeNode = TreeNode(
    node_for=[GmlGraphic],
    children="GmlPointSymbols",
    label="=GmlPointSymbols",
    tooltip="",
    add=[GmlPointSymbol],
    move=[GmlPointSymbol],
    icon_path=IMAGE_PATH)

GmlStroke_TreeNode = TreeNode(
    node_for=[GmlStroke],
    label="name",
    tooltip="The element encapsulating the graphical symbolization parameters for linear geometries.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlStroke_GmlSvgParameters_TreeNode = TreeNode(
    node_for=[GmlStroke],
    children="GmlSvgParameters",
    label="=GmlSvgParameters",
    tooltip="",
    add=[GmlSvgParameter],
    move=[GmlSvgParameter],
    icon_path=IMAGE_PATH)
GmlStroke_GmlLineSymbols_TreeNode = TreeNode(
    node_for=[GmlStroke],
    children="GmlLineSymbols",
    label="=GmlLineSymbols",
    tooltip="",
    add=[GmlLineSymbol],
    move=[GmlLineSymbol],
    icon_path=IMAGE_PATH)
GmlStroke_GmlMarks_TreeNode = TreeNode(
    node_for=[GmlStroke],
    children="GmlMarks",
    label="=GmlMarks",
    tooltip="",
    add=[GmlMark],
    move=[GmlMark],
    icon_path=IMAGE_PATH)
GmlStroke_GmlPolygonSymbols_TreeNode = TreeNode(
    node_for=[GmlStroke],
    children="GmlPolygonSymbols",
    label="=GmlPolygonSymbols",
    tooltip="",
    add=[GmlPolygonSymbol],
    move=[GmlPolygonSymbol],
    icon_path=IMAGE_PATH)

GmlCoordinateSystem_TreeNode = TreeNode(
    node_for=[GmlCoordinateSystem],
    label="name",
    tooltip="A coordinate reference system consists of a set of coordinate system axes that is related to the earth through a datum that defines the size and shape of the earth or some abstract reference system such as those used for rendering schemantic diagrams, internal views of items such as cabinets, vaults, etc. Geometries in GML indicate the coordinate reference system in which their measurements have been made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlCoordinateSystem_GmlPositions_TreeNode = TreeNode(
    node_for=[GmlCoordinateSystem],
    children="GmlPositions",
    label="=GmlPositions",
    tooltip="",
    add=[GmlPosition],
    move=[GmlPosition],
    icon_path=IMAGE_PATH)
GmlCoordinateSystem_GmlDiagramObjects_TreeNode = TreeNode(
    node_for=[GmlCoordinateSystem],
    children="GmlDiagramObjects",
    label="=GmlDiagramObjects",
    tooltip="",
    add=[GmlDiagramObject],
    move=[GmlDiagramObject],
    icon_path=IMAGE_PATH)
GmlCoordinateSystem_Diagrams_TreeNode = TreeNode(
    node_for=[GmlCoordinateSystem],
    children="Diagrams",
    label="=Diagrams",
    tooltip="",
    add=[Diagram],
    move=[Diagram],
    icon_path=IMAGE_PATH)

GmlFeatureStyle_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    label="name",
    tooltip="Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GmlFeatureStyle_GmlGeometryStyles_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    children="GmlGeometryStyles",
    label="=GmlGeometryStyles",
    tooltip="",
    add=[GmlGeometryStyle],
    move=[GmlGeometryStyle],
    icon_path=IMAGE_PATH)
GmlFeatureStyle_GmlFeatureTypes_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    children="GmlFeatureTypes",
    label="=GmlFeatureTypes",
    tooltip="",
    add=[GmlFeatureType],
    move=[GmlFeatureType],
    icon_path=IMAGE_PATH)
GmlFeatureStyle_GmlLabelStyles_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    children="GmlLabelStyles",
    label="=GmlLabelStyles",
    tooltip="",
    add=[GmlLabelStyle],
    move=[GmlLabelStyle],
    icon_path=IMAGE_PATH)
GmlFeatureStyle_GmlSymbols_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    children="GmlSymbols",
    label="=GmlSymbols",
    tooltip="",
    add=[GmlSymbol],
    move=[GmlSymbol],
    icon_path=IMAGE_PATH)
GmlFeatureStyle_GmlTobologyStyles_TreeNode = TreeNode(
    node_for=[GmlFeatureStyle],
    children="GmlTobologyStyles",
    label="=GmlTobologyStyles",
    tooltip="",
    add=[GmlTopologyStyle],
    move=[GmlTopologyStyle],
    icon_path=IMAGE_PATH)

SwitchingStep_TreeNode = TreeNode(
    node_for=[SwitchingStep],
    label="name",
    tooltip="A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchingStep_PowerSystemResources_TreeNode = TreeNode(
    node_for=[SwitchingStep],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

ErpPersonScheduleStepRole_TreeNode = TreeNode(
    node_for=[ErpPersonScheduleStepRole],
    label="name",
    tooltip="Roles played between Persons and Schedule Steps.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalRestriction_TreeNode = TreeNode(
    node_for=[OperationalRestriction],
    label="name",
    tooltip="A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  Since it is used in the network operations domain, it is associated with ConductingEquipment. In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SafetyDocument_TreeNode = TreeNode(
    node_for=[SafetyDocument],
    label="name",
    tooltip="A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SafetyDocument_ScheduleSteps_TreeNode = TreeNode(
    node_for=[SafetyDocument],
    children="ScheduleSteps",
    label="=ScheduleSteps",
    tooltip="",
    add=[SwitchingStep],
    move=[SwitchingStep],
    icon_path=IMAGE_PATH)
SafetyDocument_ClearanceTags_TreeNode = TreeNode(
    node_for=[SafetyDocument],
    children="ClearanceTags",
    label="=ClearanceTags",
    tooltip="",
    add=[ClearanceTag],
    move=[ClearanceTag],
    icon_path=IMAGE_PATH)

OutageStep_TreeNode = TreeNode(
    node_for=[OutageStep],
    label="name",
    tooltip="Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageStep_Crews_TreeNode = TreeNode(
    node_for=[OutageStep],
    children="Crews",
    label="=Crews",
    tooltip="",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)
OutageStep_OutageCodes_TreeNode = TreeNode(
    node_for=[OutageStep],
    children="OutageCodes",
    label="=OutageCodes",
    tooltip="Multiple outage codes may apply to an outage step.",
    add=[OutageCode],
    move=[OutageCode],
    icon_path=IMAGE_PATH)
OutageStep_ConductingEquipmentRoles_TreeNode = TreeNode(
    node_for=[OutageStep],
    children="ConductingEquipmentRoles",
    label="=ConductingEquipmentRoles",
    tooltip="",
    add=[OutageStepPsrRole],
    move=[OutageStepPsrRole],
    icon_path=IMAGE_PATH)

ComplianceEvent_TreeNode = TreeNode(
    node_for=[ComplianceEvent],
    label="name",
    tooltip="Compliance events are used for reporting regulatory or contract compliance issues and/or variances. These might be created as a consequence of local business processes and associated rules. It is anticipated that this class will be customised extensively to meet local implementation needs. Use inherited 'category' to indicate that, for example, expected performance will not be met or reported as mandated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PSREvent_TreeNode = TreeNode(
    node_for=[PSREvent],
    label="name",
    tooltip="Event recording the change in operational status of a PowerSystemResource.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OutageCode_TreeNode = TreeNode(
    node_for=[OutageCode],
    label="name",
    tooltip="Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageCode_OutageRecords_TreeNode = TreeNode(
    node_for=[OutageCode],
    children="OutageRecords",
    label="=OutageRecords",
    tooltip="",
    add=[OutageRecord],
    move=[OutageRecord],
    icon_path=IMAGE_PATH)
OutageCode_OutageSteps_TreeNode = TreeNode(
    node_for=[OutageCode],
    children="OutageSteps",
    label="=OutageSteps",
    tooltip="",
    add=[OutageStep],
    move=[OutageStep],
    icon_path=IMAGE_PATH)

OutageStepPsrRole_TreeNode = TreeNode(
    node_for=[OutageStepPsrRole],
    label="name",
    tooltip="Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NetworkDataSet_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    label="name",
    tooltip="Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

NetworkDataSet_Documents_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="Documents",
    label="=Documents",
    tooltip="",
    add=[Document],
    move=[Document],
    icon_path=IMAGE_PATH)
NetworkDataSet_CircuitSections_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="CircuitSections",
    label="=CircuitSections",
    tooltip="A NetworkDataSet may contain sections of circuits (vs. whole circuits).",
    add=[CircuitSection],
    move=[CircuitSection],
    icon_path=IMAGE_PATH)
NetworkDataSet_LandBases_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="LandBases",
    label="=LandBases",
    tooltip="",
    add=[LandBase],
    move=[LandBase],
    icon_path=IMAGE_PATH)
NetworkDataSet_ChangeSets_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="ChangeSets",
    label="=ChangeSets",
    tooltip="",
    add=[ChangeSet],
    move=[ChangeSet],
    icon_path=IMAGE_PATH)
NetworkDataSet_PowerSystemResources_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)
NetworkDataSet_ChangeItems_TreeNode = TreeNode(
    node_for=[NetworkDataSet],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)

CircuitSection_TreeNode = TreeNode(
    node_for=[CircuitSection],
    label="name",
    tooltip="Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CircuitSection_ConductorAssets_TreeNode = TreeNode(
    node_for=[CircuitSection],
    children="ConductorAssets",
    label="=ConductorAssets",
    tooltip="",
    add=[ConductorAsset],
    move=[ConductorAsset],
    icon_path=IMAGE_PATH)
CircuitSection_NetworkDataSets_TreeNode = TreeNode(
    node_for=[CircuitSection],
    children="NetworkDataSets",
    label="=NetworkDataSets",
    tooltip="",
    add=[NetworkDataSet],
    move=[NetworkDataSet],
    icon_path=IMAGE_PATH)
CircuitSection_PowerSystemResources_TreeNode = TreeNode(
    node_for=[CircuitSection],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)
CircuitSection_Circuits_TreeNode = TreeNode(
    node_for=[CircuitSection],
    children="Circuits",
    label="=Circuits",
    tooltip="",
    add=[Circuit],
    move=[Circuit],
    icon_path=IMAGE_PATH)

OutageRecord_TreeNode = TreeNode(
    node_for=[OutageRecord],
    label="name",
    tooltip="A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageRecord_OutageCodes_TreeNode = TreeNode(
    node_for=[OutageRecord],
    children="OutageCodes",
    label="=OutageCodes",
    tooltip="Multiple outage codes may apply to an outage record.",
    add=[OutageCode],
    move=[OutageCode],
    icon_path=IMAGE_PATH)
OutageRecord_OutageSteps_TreeNode = TreeNode(
    node_for=[OutageRecord],
    children="OutageSteps",
    label="=OutageSteps",
    tooltip="",
    add=[OutageStep],
    move=[OutageStep],
    icon_path=IMAGE_PATH)

CallBack_TreeNode = TreeNode(
    node_for=[CallBack],
    label="name",
    tooltip="Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CallBack_ErpPersons_TreeNode = TreeNode(
    node_for=[CallBack],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)
CallBack_Appointments_TreeNode = TreeNode(
    node_for=[CallBack],
    children="Appointments",
    label="=Appointments",
    tooltip="",
    add=[Appointment],
    move=[Appointment],
    icon_path=IMAGE_PATH)
CallBack_TroubleTickets_TreeNode = TreeNode(
    node_for=[CallBack],
    children="TroubleTickets",
    label="=TroubleTickets",
    tooltip="",
    add=[TroubleTicket],
    move=[TroubleTicket],
    icon_path=IMAGE_PATH)

ChangeItem_TreeNode = TreeNode(
    node_for=[ChangeItem],
    label="name",
    tooltip="Description for a single change within an ordered list of changes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OrgPsrRole_TreeNode = TreeNode(
    node_for=[OrgPsrRole],
    label="name",
    tooltip="Roles played between Organisations and Power System Resources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OutageNotification_TreeNode = TreeNode(
    node_for=[OutageNotification],
    label="name",
    tooltip="A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageNotification_CustomerDatas_TreeNode = TreeNode(
    node_for=[OutageNotification],
    children="CustomerDatas",
    label="=CustomerDatas",
    tooltip="",
    add=[Customer],
    move=[Customer],
    icon_path=IMAGE_PATH)

SwitchingSchedule_TreeNode = TreeNode(
    node_for=[SwitchingSchedule],
    label="name",
    tooltip="Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchingSchedule_ScheduleSteps_TreeNode = TreeNode(
    node_for=[SwitchingSchedule],
    children="ScheduleSteps",
    label="=ScheduleSteps",
    tooltip="",
    add=[SwitchingStep],
    move=[SwitchingStep],
    icon_path=IMAGE_PATH)
SwitchingSchedule_Crews_TreeNode = TreeNode(
    node_for=[SwitchingSchedule],
    children="Crews",
    label="=Crews",
    tooltip="All Crews executing this SwitchingSchedule.",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)

IncidentCode_TreeNode = TreeNode(
    node_for=[IncidentCode],
    label="name",
    tooltip="Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IncidentCode_IncidentRecords_TreeNode = TreeNode(
    node_for=[IncidentCode],
    children="IncidentRecords",
    label="=IncidentRecords",
    tooltip="",
    add=[IncidentRecord],
    move=[IncidentRecord],
    icon_path=IMAGE_PATH)

PlannedOutage_TreeNode = TreeNode(
    node_for=[PlannedOutage],
    label="name",
    tooltip="Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PlannedOutage_CustomerDatas_TreeNode = TreeNode(
    node_for=[PlannedOutage],
    children="CustomerDatas",
    label="=CustomerDatas",
    tooltip="All customers affected by this work. Derived from WorkOrder.connectedCustomers",
    add=[Customer],
    move=[Customer],
    icon_path=IMAGE_PATH)
PlannedOutage_OutageSchedules_TreeNode = TreeNode(
    node_for=[PlannedOutage],
    children="OutageSchedules",
    label="=OutageSchedules",
    tooltip="",
    add=[OutageSchedule],
    move=[OutageSchedule],
    icon_path=IMAGE_PATH)

TroubleTicket_TreeNode = TreeNode(
    node_for=[TroubleTicket],
    label="name",
    tooltip="A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TroubleTicket_CallBacks_TreeNode = TreeNode(
    node_for=[TroubleTicket],
    children="CallBacks",
    label="=CallBacks",
    tooltip="",
    add=[CallBack],
    move=[CallBack],
    icon_path=IMAGE_PATH)

IncidentRecord_TreeNode = TreeNode(
    node_for=[IncidentRecord],
    label="name",
    tooltip="Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IncidentRecord_IncidentCodes_TreeNode = TreeNode(
    node_for=[IncidentRecord],
    children="IncidentCodes",
    label="=IncidentCodes",
    tooltip="",
    add=[IncidentCode],
    move=[IncidentCode],
    icon_path=IMAGE_PATH)
IncidentRecord_TroubleTickets_TreeNode = TreeNode(
    node_for=[IncidentRecord],
    children="TroubleTickets",
    label="=TroubleTickets",
    tooltip="",
    add=[TroubleTicket],
    move=[TroubleTicket],
    icon_path=IMAGE_PATH)

ChangeSet_TreeNode = TreeNode(
    node_for=[ChangeSet],
    label="name",
    tooltip="The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ChangeSet_LandBases_TreeNode = TreeNode(
    node_for=[ChangeSet],
    children="LandBases",
    label="=LandBases",
    tooltip="",
    add=[LandBase],
    move=[LandBase],
    icon_path=IMAGE_PATH)
ChangeSet_NetworkDataSets_TreeNode = TreeNode(
    node_for=[ChangeSet],
    children="NetworkDataSets",
    label="=NetworkDataSets",
    tooltip="",
    add=[NetworkDataSet],
    move=[NetworkDataSet],
    icon_path=IMAGE_PATH)
ChangeSet_ChangeItems_TreeNode = TreeNode(
    node_for=[ChangeSet],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
ChangeSet_Documents_TreeNode = TreeNode(
    node_for=[ChangeSet],
    children="Documents",
    label="=Documents",
    tooltip="",
    add=[Document],
    move=[Document],
    icon_path=IMAGE_PATH)

OutageReport_TreeNode = TreeNode(
    node_for=[OutageReport],
    label="name",
    tooltip="Document with statistics of an outage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LandBase_TreeNode = TreeNode(
    node_for=[LandBase],
    label="name",
    tooltip="Land base data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Circuit_TreeNode = TreeNode(
    node_for=[Circuit],
    label="name",
    tooltip="EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TypeAsset_TreeNode = TreeNode(
    node_for=[TypeAsset],
    label="name",
    tooltip="Whereas an AssetModel is a particular model and version of a vendor's product, a TypeAsset is documentation for a generic asset or material item that may be used for design purposes. Any number of AssetModels may be used to perform this generic function. The primary role of the TypeAsset is typically defined by the PowereSystemResource it is associated with.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TypeAsset_AssetModels_TreeNode = TreeNode(
    node_for=[TypeAsset],
    children="AssetModels",
    label="=AssetModels",
    tooltip="A type of asset may be satisified with many different types of asset models.",
    add=[AssetModel],
    move=[AssetModel],
    icon_path=IMAGE_PATH)
TypeAsset_ErpInventoryIssues_TreeNode = TreeNode(
    node_for=[TypeAsset],
    children="ErpInventoryIssues",
    label="=ErpInventoryIssues",
    tooltip="",
    add=[ErpIssueInventory],
    move=[ErpIssueInventory],
    icon_path=IMAGE_PATH)
TypeAsset_ErpReqLineItems_TreeNode = TreeNode(
    node_for=[TypeAsset],
    children="ErpReqLineItems",
    label="=ErpReqLineItems",
    tooltip="",
    add=[ErpReqLineItem],
    move=[ErpReqLineItem],
    icon_path=IMAGE_PATH)
TypeAsset_ErpBomItemDatas_TreeNode = TreeNode(
    node_for=[TypeAsset],
    children="ErpBomItemDatas",
    label="=ErpBomItemDatas",
    tooltip="",
    add=[ErpBomItemData],
    move=[ErpBomItemData],
    icon_path=IMAGE_PATH)

ElectricalTypeAsset_TreeNode = TreeNode(
    node_for=[ElectricalTypeAsset],
    label="name",
    tooltip="Generic TypeAsset for all types of component in the network that have electrical characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ElectricalTypeAsset_ElectricalInfos_TreeNode = TreeNode(
    node_for=[ElectricalTypeAsset],
    children="ElectricalInfos",
    label="=ElectricalInfos",
    tooltip="",
    add=[ElectricalInfo],
    move=[ElectricalInfo],
    icon_path=IMAGE_PATH)

ShuntCompensatorTypeAsset_TreeNode = TreeNode(
    node_for=[ShuntCompensatorTypeAsset],
    label="name",
    tooltip="Documentation for a generic shunt compensator that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShuntCompensatorTypeAsset_ShuntCompensatorAssetModels_TreeNode = TreeNode(
    node_for=[ShuntCompensatorTypeAsset],
    children="ShuntCompensatorAssetModels",
    label="=ShuntCompensatorAssetModels",
    tooltip="",
    add=[ShuntCompensatorAssetModel],
    move=[ShuntCompensatorAssetModel],
    icon_path=IMAGE_PATH)

EndDeviceTypeAsset_TreeNode = TreeNode(
    node_for=[EndDeviceTypeAsset],
    label="name",
    tooltip="Documentation for generic End Device that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EndDeviceTypeAsset_EndDeviceModels_TreeNode = TreeNode(
    node_for=[EndDeviceTypeAsset],
    children="EndDeviceModels",
    label="=EndDeviceModels",
    tooltip="",
    add=[EndDeviceModel],
    move=[EndDeviceModel],
    icon_path=IMAGE_PATH)

MountingPoint_TreeNode = TreeNode(
    node_for=[MountingPoint],
    label="name",
    tooltip="Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MountingPoint_OverheadConductors_TreeNode = TreeNode(
    node_for=[MountingPoint],
    children="OverheadConductors",
    label="=OverheadConductors",
    tooltip="",
    add=[OverheadConductorAsset],
    move=[OverheadConductorAsset],
    icon_path=IMAGE_PATH)
MountingPoint_Connections_TreeNode = TreeNode(
    node_for=[MountingPoint],
    children="Connections",
    label="=Connections",
    tooltip="",
    add=[Connection],
    move=[Connection],
    icon_path=IMAGE_PATH)

BusbarTypeAsset_TreeNode = TreeNode(
    node_for=[BusbarTypeAsset],
    label="name",
    tooltip="Documentation for a generic busbar that may be used for design purposes. It is typically associated with PoserSystemResource BusbarSection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusbarTypeAsset_BusbarTypeAssets_TreeNode = TreeNode(
    node_for=[BusbarTypeAsset],
    children="BusbarTypeAssets",
    label="=BusbarTypeAssets",
    tooltip="",
    add=[BusbarAssetModel],
    move=[BusbarAssetModel],
    icon_path=IMAGE_PATH)

WorkEquipmentTypeAsset_TreeNode = TreeNode(
    node_for=[WorkEquipmentTypeAsset],
    label="name",
    tooltip="Documentation for generic equipment that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkEquipmentTypeAsset_WorkEquipmentAssetModels_TreeNode = TreeNode(
    node_for=[WorkEquipmentTypeAsset],
    children="WorkEquipmentAssetModels",
    label="=WorkEquipmentAssetModels",
    tooltip="",
    add=[WorkEquipmentAssetModel],
    move=[WorkEquipmentAssetModel],
    icon_path=IMAGE_PATH)

SwitchTypeAsset_TreeNode = TreeNode(
    node_for=[SwitchTypeAsset],
    label="name",
    tooltip="Documentation for a generic switch asset that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchTypeAsset_SwitchAssetModels_TreeNode = TreeNode(
    node_for=[SwitchTypeAsset],
    children="SwitchAssetModels",
    label="=SwitchAssetModels",
    tooltip="",
    add=[SwitchAssetModel],
    move=[SwitchAssetModel],
    icon_path=IMAGE_PATH)

StructureTypeAsset_TreeNode = TreeNode(
    node_for=[StructureTypeAsset],
    label="name",
    tooltip="A Type of Structural Asset with properties common to a large number of asset models.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StructureTypeAsset_MountConnections_TreeNode = TreeNode(
    node_for=[StructureTypeAsset],
    children="MountConnections",
    label="=MountConnections",
    tooltip="",
    add=[Connection],
    move=[Connection],
    icon_path=IMAGE_PATH)

TowerTypeAsset_TreeNode = TreeNode(
    node_for=[TowerTypeAsset],
    label="name",
    tooltip="Documentation for a generic tower that may be used for various purposes such as work planning. A transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TowerTypeAsset_TowerAssetModels_TreeNode = TreeNode(
    node_for=[TowerTypeAsset],
    children="TowerAssetModels",
    label="=TowerAssetModels",
    tooltip="",
    add=[TowerAssetModel],
    move=[TowerAssetModel],
    icon_path=IMAGE_PATH)

StreetlightTypeAsset_TreeNode = TreeNode(
    node_for=[StreetlightTypeAsset],
    label="name",
    tooltip="Documentation for a generic streetlight that may be used for various purposes such as work planning. Use 'category' for utility specific categorisation, such as luminar, grid light, lantern, open bottom, flood, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StreetlightTypeAsset_StreetlightAssetModels_TreeNode = TreeNode(
    node_for=[StreetlightTypeAsset],
    children="StreetlightAssetModels",
    label="=StreetlightAssetModels",
    tooltip="",
    add=[StreetlightAssetModel],
    move=[StreetlightAssetModel],
    icon_path=IMAGE_PATH)

ToolTypeAsset_TreeNode = TreeNode(
    node_for=[ToolTypeAsset],
    label="name",
    tooltip="Documentation for a generic tool that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ToolTypeAsset_ToolAssetModels_TreeNode = TreeNode(
    node_for=[ToolTypeAsset],
    children="ToolAssetModels",
    label="=ToolAssetModels",
    tooltip="",
    add=[ToolAssetModel],
    move=[ToolAssetModel],
    icon_path=IMAGE_PATH)

CompositeSwitchTypeAsset_TreeNode = TreeNode(
    node_for=[CompositeSwitchTypeAsset],
    label="name",
    tooltip="Documentation for a generic composite switch asset that may be used for design purposes. A composite wwitch is an amalgamation of multiple Switches.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompositeSwitchTypeAsset_CompositeSwitchAssetModels_TreeNode = TreeNode(
    node_for=[CompositeSwitchTypeAsset],
    children="CompositeSwitchAssetModels",
    label="=CompositeSwitchAssetModels",
    tooltip="",
    add=[CompositeSwitchAssetModel],
    move=[CompositeSwitchAssetModel],
    icon_path=IMAGE_PATH)
CompositeSwitchTypeAsset_SwitchTypesAssets_TreeNode = TreeNode(
    node_for=[CompositeSwitchTypeAsset],
    children="SwitchTypesAssets",
    label="=SwitchTypesAssets",
    tooltip="",
    add=[SwitchTypeAsset],
    move=[SwitchTypeAsset],
    icon_path=IMAGE_PATH)

TypeAssetCatalogue_TreeNode = TreeNode(
    node_for=[TypeAssetCatalogue],
    label="name",
    tooltip="Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TypeAssetCatalogue_TypeAssets_TreeNode = TreeNode(
    node_for=[TypeAssetCatalogue],
    children="TypeAssets",
    label="=TypeAssets",
    tooltip="",
    add=[TypeAsset],
    move=[TypeAsset],
    icon_path=IMAGE_PATH)

ComEquipmentTypeAsset_TreeNode = TreeNode(
    node_for=[ComEquipmentTypeAsset],
    label="name",
    tooltip="Documentation for a piece of Communication Equipment (e.g., gateway, router, network hub, etc.) that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FACTSDeviceTypeAsset_TreeNode = TreeNode(
    node_for=[FACTSDeviceTypeAsset],
    label="name",
    tooltip="Documentation for generic Flexible alternating current transmission systems (FACTS) devices that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FACTSDeviceTypeAsset_FACTSDeviceAssetModels_TreeNode = TreeNode(
    node_for=[FACTSDeviceTypeAsset],
    children="FACTSDeviceAssetModels",
    label="=FACTSDeviceAssetModels",
    tooltip="",
    add=[FACTSDeviceAssetModel],
    move=[FACTSDeviceAssetModel],
    icon_path=IMAGE_PATH)

SVCTypeAsset_TreeNode = TreeNode(
    node_for=[SVCTypeAsset],
    label="name",
    tooltip="Documentation for a generic Static Var Compensator (SVC) that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SVCTypeAsset_SvcInfos_TreeNode = TreeNode(
    node_for=[SVCTypeAsset],
    children="SvcInfos",
    label="=SvcInfos",
    tooltip="",
    add=[SVCInfo],
    move=[SVCInfo],
    icon_path=IMAGE_PATH)
SVCTypeAsset_SVCAssetModels_TreeNode = TreeNode(
    node_for=[SVCTypeAsset],
    children="SVCAssetModels",
    label="=SVCAssetModels",
    tooltip="",
    add=[SVCAssetModel],
    move=[SVCAssetModel],
    icon_path=IMAGE_PATH)

ResistorTypeAsset_TreeNode = TreeNode(
    node_for=[ResistorTypeAsset],
    label="name",
    tooltip="Documentation for a generic resistor that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ResistorTypeAsset_ResistorAssetModels_TreeNode = TreeNode(
    node_for=[ResistorTypeAsset],
    children="ResistorAssetModels",
    label="=ResistorAssetModels",
    tooltip="",
    add=[ResistorAssetModel],
    move=[ResistorAssetModel],
    icon_path=IMAGE_PATH)
ResistorTypeAsset_Resistors_TreeNode = TreeNode(
    node_for=[ResistorTypeAsset],
    children="Resistors",
    label="=Resistors",
    tooltip="",
    add=[Resistor],
    move=[Resistor],
    icon_path=IMAGE_PATH)

SeriesCompensatorTypeAsset_TreeNode = TreeNode(
    node_for=[SeriesCompensatorTypeAsset],
    label="name",
    tooltip="Documentation for a generic series compensator that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SeriesCompensatorTypeAsset_ShuntCompensatorAssetModels_TreeNode = TreeNode(
    node_for=[SeriesCompensatorTypeAsset],
    children="ShuntCompensatorAssetModels",
    label="=ShuntCompensatorAssetModels",
    tooltip="",
    add=[SeriesCompensatorAssetModel],
    move=[SeriesCompensatorAssetModel],
    icon_path=IMAGE_PATH)

FaultIndicatorTypeAsset_TreeNode = TreeNode(
    node_for=[FaultIndicatorTypeAsset],
    label="name",
    tooltip="Documentation for a generic fault indicator that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FaultIndicatorTypeAsset_FaultIndicatorAssetModels_TreeNode = TreeNode(
    node_for=[FaultIndicatorTypeAsset],
    children="FaultIndicatorAssetModels",
    label="=FaultIndicatorAssetModels",
    tooltip="",
    add=[FaultIndicatorAssetModel],
    move=[FaultIndicatorAssetModel],
    icon_path=IMAGE_PATH)
FaultIndicatorTypeAsset_FaultIndicators_TreeNode = TreeNode(
    node_for=[FaultIndicatorTypeAsset],
    children="FaultIndicators",
    label="=FaultIndicators",
    tooltip="",
    add=[FaultIndicator],
    move=[FaultIndicator],
    icon_path=IMAGE_PATH)

VehicleTypeAsset_TreeNode = TreeNode(
    node_for=[VehicleTypeAsset],
    label="name",
    tooltip="Documentation for a generic vehicle that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VehicleTypeAsset_VehicleAssetModels_TreeNode = TreeNode(
    node_for=[VehicleTypeAsset],
    children="VehicleAssetModels",
    label="=VehicleAssetModels",
    tooltip="",
    add=[VehicleAssetModel],
    move=[VehicleAssetModel],
    icon_path=IMAGE_PATH)

BreakerTypeAsset_TreeNode = TreeNode(
    node_for=[BreakerTypeAsset],
    label="name",
    tooltip="Documentation for a generic breaker asset that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BreakerTypeAsset_BreakerAssetModels_TreeNode = TreeNode(
    node_for=[BreakerTypeAsset],
    children="BreakerAssetModels",
    label="=BreakerAssetModels",
    tooltip="",
    add=[BreakerAssetModel],
    move=[BreakerAssetModel],
    icon_path=IMAGE_PATH)

PoleTypeAsset_TreeNode = TreeNode(
    node_for=[PoleTypeAsset],
    label="name",
    tooltip="Documentation for a generic pole that may be used for various purposes such as work planning. A pole typically has a single Connection with 1,2 or 3 mounting points.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PoleTypeAsset_PoleModels_TreeNode = TreeNode(
    node_for=[PoleTypeAsset],
    children="PoleModels",
    label="=PoleModels",
    tooltip="",
    add=[PoleModel],
    move=[PoleModel],
    icon_path=IMAGE_PATH)

DuctTypeAsset_TreeNode = TreeNode(
    node_for=[DuctTypeAsset],
    label="name",
    tooltip="A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DuctTypeAsset_CableAssets_TreeNode = TreeNode(
    node_for=[DuctTypeAsset],
    children="CableAssets",
    label="=CableAssets",
    tooltip="",
    add=[CableAsset],
    move=[CableAsset],
    icon_path=IMAGE_PATH)

SurgeProtectorTypeAsset_TreeNode = TreeNode(
    node_for=[SurgeProtectorTypeAsset],
    label="name",
    tooltip="Documentation for a generic surge arrestor that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SurgeProtectorTypeAsset_SurgeProtectors_TreeNode = TreeNode(
    node_for=[SurgeProtectorTypeAsset],
    children="SurgeProtectors",
    label="=SurgeProtectors",
    tooltip="",
    add=[SurgeProtector],
    move=[SurgeProtector],
    icon_path=IMAGE_PATH)
SurgeProtectorTypeAsset_SurgeProtectorAssetModels_TreeNode = TreeNode(
    node_for=[SurgeProtectorTypeAsset],
    children="SurgeProtectorAssetModels",
    label="=SurgeProtectorAssetModels",
    tooltip="",
    add=[SurgeProtectorAssetModel],
    move=[SurgeProtectorAssetModel],
    icon_path=IMAGE_PATH)

Connection_TreeNode = TreeNode(
    node_for=[Connection],
    label="name",
    tooltip="A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Connection_StructureTypeAssets_TreeNode = TreeNode(
    node_for=[Connection],
    children="StructureTypeAssets",
    label="=StructureTypeAssets",
    tooltip="",
    add=[StructureTypeAsset],
    move=[StructureTypeAsset],
    icon_path=IMAGE_PATH)
Connection_MountingPoints_TreeNode = TreeNode(
    node_for=[Connection],
    children="MountingPoints",
    label="=MountingPoints",
    tooltip="",
    add=[MountingPoint],
    move=[MountingPoint],
    icon_path=IMAGE_PATH)

ComFunctionTypeAsset_TreeNode = TreeNode(
    node_for=[ComFunctionTypeAsset],
    label="name",
    tooltip="Documentation for a generic communication function that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ComFunctionTypeAsset_ComFunctionAssetModels_TreeNode = TreeNode(
    node_for=[ComFunctionTypeAsset],
    children="ComFunctionAssetModels",
    label="=ComFunctionAssetModels",
    tooltip="",
    add=[ComFunctionAssetModel],
    move=[ComFunctionAssetModel],
    icon_path=IMAGE_PATH)

ProtectionEquipmentTypeAsset_TreeNode = TreeNode(
    node_for=[ProtectionEquipmentTypeAsset],
    label="name",
    tooltip="Documentation for generic protection equiment that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectionEquipmentTypeAsset_ProtectionEquipmentAssetModels_TreeNode = TreeNode(
    node_for=[ProtectionEquipmentTypeAsset],
    children="ProtectionEquipmentAssetModels",
    label="=ProtectionEquipmentAssetModels",
    tooltip="",
    add=[ProtectionEquipmentAssetModel],
    move=[ProtectionEquipmentAssetModel],
    icon_path=IMAGE_PATH)

CabinetTypeAsset_TreeNode = TreeNode(
    node_for=[CabinetTypeAsset],
    label="name",
    tooltip="Documentation for a generic cabinet that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CabinetTypeAsset_CabinetModels_TreeNode = TreeNode(
    node_for=[CabinetTypeAsset],
    children="CabinetModels",
    label="=CabinetModels",
    tooltip="",
    add=[CabinetModel],
    move=[CabinetModel],
    icon_path=IMAGE_PATH)

MeterTypeAsset_TreeNode = TreeNode(
    node_for=[MeterTypeAsset],
    label="name",
    tooltip="Documentation for a generic meter that may be used for design purposes. Rather than being associated with CustomerMeter, it is associated with EnergyConsumer as it may be used for many applications, such as tie line metering, in addition to customer metering.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeterTypeAsset_MeterAssetModels_TreeNode = TreeNode(
    node_for=[MeterTypeAsset],
    children="MeterAssetModels",
    label="=MeterAssetModels",
    tooltip="",
    add=[MeterAssetModel],
    move=[MeterAssetModel],
    icon_path=IMAGE_PATH)

GeneratorTypeAsset_TreeNode = TreeNode(
    node_for=[GeneratorTypeAsset],
    label="name",
    tooltip="Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratorTypeAsset_GeneratorAssetModels_TreeNode = TreeNode(
    node_for=[GeneratorTypeAsset],
    children="GeneratorAssetModels",
    label="=GeneratorAssetModels",
    tooltip="",
    add=[GeneratorAssetModel],
    move=[GeneratorAssetModel],
    icon_path=IMAGE_PATH)

SubstationTypeAsset_TreeNode = TreeNode(
    node_for=[SubstationTypeAsset],
    label="name",
    tooltip="Documentation for a type of substation that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AssetFunctionTypeAsset_TreeNode = TreeNode(
    node_for=[AssetFunctionTypeAsset],
    label="name",
    tooltip="Documentation for a generic Asset Function that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetFunctionTypeAsset_AssetFunctionAssetModels_TreeNode = TreeNode(
    node_for=[AssetFunctionTypeAsset],
    children="AssetFunctionAssetModels",
    label="=AssetFunctionAssetModels",
    tooltip="",
    add=[AssetFunctionAssetModel],
    move=[AssetFunctionAssetModel],
    icon_path=IMAGE_PATH)

PotentialTransformerTypeAsset_TreeNode = TreeNode(
    node_for=[PotentialTransformerTypeAsset],
    label="name",
    tooltip="Documentation for a generic Potential Transformer (PT) that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PotentialTransformerTypeAsset_PotentialTransformers_TreeNode = TreeNode(
    node_for=[PotentialTransformerTypeAsset],
    children="PotentialTransformers",
    label="=PotentialTransformers",
    tooltip="",
    add=[PotentialTransformer],
    move=[PotentialTransformer],
    icon_path=IMAGE_PATH)
PotentialTransformerTypeAsset_PotentialTransformerAssetModels_TreeNode = TreeNode(
    node_for=[PotentialTransformerTypeAsset],
    children="PotentialTransformerAssetModels",
    label="=PotentialTransformerAssetModels",
    tooltip="",
    add=[PotentialTransformerAssetModel],
    move=[PotentialTransformerAssetModel],
    icon_path=IMAGE_PATH)

RecloserTypeAsset_TreeNode = TreeNode(
    node_for=[RecloserTypeAsset],
    label="name",
    tooltip="Documentation for a generic recloser asset that may be used for design purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RecloserTypeAsset_RecloserAssetModels_TreeNode = TreeNode(
    node_for=[RecloserTypeAsset],
    children="RecloserAssetModels",
    label="=RecloserAssetModels",
    tooltip="",
    add=[RecloserAssetModel],
    move=[RecloserAssetModel],
    icon_path=IMAGE_PATH)

CurrentTransformerTypeAsset_TreeNode = TreeNode(
    node_for=[CurrentTransformerTypeAsset],
    label="name",
    tooltip="Documentation for a generic Current Transformer (CT) that may be used for various purposes such as work planning.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CurrentTransformerTypeAsset_CurrentTransformerAssetModels_TreeNode = TreeNode(
    node_for=[CurrentTransformerTypeAsset],
    children="CurrentTransformerAssetModels",
    label="=CurrentTransformerAssetModels",
    tooltip="",
    add=[CurrentTransformerAssetModel],
    move=[CurrentTransformerAssetModel],
    icon_path=IMAGE_PATH)
CurrentTransformerTypeAsset_CurrentTransformers_TreeNode = TreeNode(
    node_for=[CurrentTransformerTypeAsset],
    children="CurrentTransformers",
    label="=CurrentTransformers",
    tooltip="",
    add=[CurrentTransformer],
    move=[CurrentTransformer],
    icon_path=IMAGE_PATH)

DuctBankTypeAsset_TreeNode = TreeNode(
    node_for=[DuctBankTypeAsset],
    label="name",
    tooltip="A DuctBank contains multiple Ducts. The DuctBank itself should have no connections, since these are defined by the individual ducts within it. However, it will have a ConstructionType and the material it is constructed from.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DuctBankTypeAsset_DuctTypeAssets_TreeNode = TreeNode(
    node_for=[DuctBankTypeAsset],
    children="DuctTypeAssets",
    label="=DuctTypeAssets",
    tooltip="",
    add=[DuctTypeAsset],
    move=[DuctTypeAsset],
    icon_path=IMAGE_PATH)
DuctBankTypeAsset_DuctBanks_TreeNode = TreeNode(
    node_for=[DuctBankTypeAsset],
    children="DuctBanks",
    label="=DuctBanks",
    tooltip="",
    add=[DuctBank],
    move=[DuctBank],
    icon_path=IMAGE_PATH)

ReservationVersion_TreeNode = TreeNode(
    node_for=[ReservationVersion],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TiePoint_TreeNode = TreeNode(
    node_for=[TiePoint],
    label="name",
    tooltip="Site of an interface between interchange areas. The tie point can be a network branch (e.g., transmission line or transformer) or a switching device. For transmission lines, the interchange area boundary is usually at a designated point such as the middle of the line. Line end metering is then corrected for line losses.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TiePoint_For_Measurements_TreeNode = TreeNode(
    node_for=[TiePoint],
    children="For_Measurements",
    label="=For_Measurements",
    tooltip="A measurement is made on the A side of a tie point",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
TiePoint_By_Measurements_TreeNode = TreeNode(
    node_for=[TiePoint],
    children="By_Measurements",
    label="=By_Measurements",
    tooltip="A measurement is made on the B side of a tie point",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

TransmissionService_TreeNode = TreeNode(
    node_for=[TransmissionService],
    label="name",
    tooltip="Transmission products along posted transmission path.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionService_OfferedAs_TreeNode = TreeNode(
    node_for=[TransmissionService],
    children="OfferedAs",
    label="=OfferedAs",
    tooltip="A transmission product is offered as a transmission service along a transmission path.",
    add=[TransmissionProduct],
    move=[TransmissionProduct],
    icon_path=IMAGE_PATH)
TransmissionService_Offering_TreeNode = TreeNode(
    node_for=[TransmissionService],
    children="Offering",
    label="=Offering",
    tooltip="A transmission service is offered on a transmission path.",
    add=[TransmissionPath],
    move=[TransmissionPath],
    icon_path=IMAGE_PATH)
TransmissionService_ScheduledBy_TreeNode = TreeNode(
    node_for=[TransmissionService],
    children="ScheduledBy",
    label="=ScheduledBy",
    tooltip="A transmission schedule posts the available transmission capacity for a transmission line.",
    add=[AvailableTransmissionCapacity],
    move=[AvailableTransmissionCapacity],
    icon_path=IMAGE_PATH)
TransmissionService_ReservedBy_ServiceReservation_TreeNode = TreeNode(
    node_for=[TransmissionService],
    children="ReservedBy_ServiceReservation",
    label="=ReservedBy_ServiceReservation",
    tooltip="A service reservation reserves a particular transmission service.",
    add=[ServiceReservation],
    move=[ServiceReservation],
    icon_path=IMAGE_PATH)

ServicePoint_TreeNode = TreeNode(
    node_for=[ServicePoint],
    label="name",
    tooltip="Each ServicePoint is contained within (or on the boundary of) an ElectronicIinterchangeArea. ServicePoints are defined termination points of a transmission path (down to distribution level or to a customer - generation or consumption or both).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServicePoint_EnergyProducts_TreeNode = TreeNode(
    node_for=[ServicePoint],
    children="EnergyProducts",
    label="=EnergyProducts",
    tooltip="An EnergyProduct injects energy into a service point.",
    add=[EnergyProduct],
    move=[EnergyProduct],
    icon_path=IMAGE_PATH)
ServicePoint_HasAPOD__TreeNode = TreeNode(
    node_for=[ServicePoint],
    children="HasAPOD_",
    label="=HasAPOD_",
    tooltip="A transmission path has a 'point-of-delivery' service point",
    add=[TransmissionPath],
    move=[TransmissionPath],
    icon_path=IMAGE_PATH)
ServicePoint_HasAPOR__TreeNode = TreeNode(
    node_for=[ServicePoint],
    children="HasAPOR_",
    label="=HasAPOR_",
    tooltip="A transmission path has a 'point-of-receipt' service point",
    add=[TransmissionPath],
    move=[TransmissionPath],
    icon_path=IMAGE_PATH)

ServiceReservation_TreeNode = TreeNode(
    node_for=[ServiceReservation],
        tooltip="A ServiceReservation is a reservation for either AncillaryServices or TransmissionServices. In the case of TransmissionServices, this is the right to some amount of AvailableTransmissionCapacity for a product on a path in a direction for some specific period of time",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServiceReservation_Reserves_AncillaryServices_TreeNode = TreeNode(
    node_for=[ServiceReservation],
    children="Reserves_AncillaryServices",
    label="=Reserves_AncillaryServices",
    tooltip="A ServiceReservation guarantees a certain AncillaryService.",
    add=[AncillaryService],
    move=[AncillaryService],
    icon_path=IMAGE_PATH)
ServiceReservation_Reserves_TransmissionService_TreeNode = TreeNode(
    node_for=[ServiceReservation],
    children="Reserves_TransmissionService",
    label="=Reserves_TransmissionService",
    tooltip="A service reservation reserves a particular transmission service.",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)

TransmissionPath_TreeNode = TreeNode(
    node_for=[TransmissionPath],
        tooltip="An electrical connection, link, or line consisting of one or more parallel transmission elements between two areas of the interconnected electric systems, or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransmissionPath_OfferedOn_TreeNode = TreeNode(
    node_for=[TransmissionPath],
    children="OfferedOn",
    label="=OfferedOn",
    tooltip="A transmission service is offered on a transmission path.",
    add=[TransmissionService],
    move=[TransmissionService],
    icon_path=IMAGE_PATH)
TransmissionPath_LocatedOn_TreeNode = TreeNode(
    node_for=[TransmissionPath],
    children="LocatedOn",
    label="=LocatedOn",
    tooltip="A transmission product is located on a transmission path.",
    add=[TransmissionProduct],
    move=[TransmissionProduct],
    icon_path=IMAGE_PATH)

AncillaryService_TreeNode = TreeNode(
    node_for=[AncillaryService],
    label="name",
    tooltip="All of these services relate  to various aspects of insuring that the production of energy matches consumption of energy at any given time.  They are very critical to the security and reliability of the interconnected network. Some examples of AncillaryServices include Operating/Supplemental Reserve, Energy Imbalance Service, Operating/Spinning Reserve, Reactive Supply and Voltage Control, and Regulation and Frequency Response.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AncillaryService_TransmissionProviders_TreeNode = TreeNode(
    node_for=[AncillaryService],
    children="TransmissionProviders",
    label="=TransmissionProviders",
    tooltip="A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.",
    add=[TransmissionProvider],
    move=[TransmissionProvider],
    icon_path=IMAGE_PATH)

ExternalCustomerAgreement_TreeNode = TreeNode(
    node_for=[ExternalCustomerAgreement],
    label="name",
    tooltip="A type of customer agreement involving an external agency. For example, a customer may form a contracts with an Energy Service Supplier if Direct Access is permitted.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StandardIndustryCode_TreeNode = TreeNode(
    node_for=[StandardIndustryCode],
    label="name",
    tooltip="The Standard Industrial Classification (SIC) are the codes that identify the type of products/service an industry is involved in, and used for statutory reporting purposes. For example, in the USA these codes are located by the federal government, and then published in a book entitled 'The Standard Industrial Classification Manual'. The codes are arranged in a hierarchical structure. Note that Residential Service Agreements are not classified according to the SIC codes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StandardIndustryCode_CustomerAgreements_TreeNode = TreeNode(
    node_for=[StandardIndustryCode],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)

CustomerBillingInfo_TreeNode = TreeNode(
    node_for=[CustomerBillingInfo],
    label="name",
    tooltip="The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CustomerBillingInfo_ErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[CustomerBillingInfo],
    children="ErpInvoiceLineItems",
    label="=ErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)

OutageHistory_TreeNode = TreeNode(
    node_for=[OutageHistory],
    label="name",
    tooltip="A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageHistory_OutageReports_TreeNode = TreeNode(
    node_for=[OutageHistory],
    children="OutageReports",
    label="=OutageReports",
    tooltip="OutageReports per customer for which this OutageHistory is created.",
    add=[OutageReport],
    move=[OutageReport],
    icon_path=IMAGE_PATH)

WorkBillingInfo_TreeNode = TreeNode(
    node_for=[WorkBillingInfo],
    label="name",
    tooltip="Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WorkBillingInfo_ErpLineItems_TreeNode = TreeNode(
    node_for=[WorkBillingInfo],
    children="ErpLineItems",
    label="=ErpLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)
WorkBillingInfo_Works_TreeNode = TreeNode(
    node_for=[WorkBillingInfo],
    children="Works",
    label="=Works",
    tooltip="",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)

PowerQualityPricing_TreeNode = TreeNode(
    node_for=[PowerQualityPricing],
    label="name",
    tooltip="Pricing can be based on power quality.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerQualityPricing_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[PowerQualityPricing],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)

ServiceGuarantee_TreeNode = TreeNode(
    node_for=[ServiceGuarantee],
    label="name",
    tooltip="A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SubscribePowerCurve_TreeNode = TreeNode(
    node_for=[SubscribePowerCurve],
    label="name",
    tooltip="Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadMgmtFunction_TreeNode = TreeNode(
    node_for=[LoadMgmtFunction],
    label="name",
    tooltip="A collective function at an end device that manages the customer load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadMgmtFunction_Switches_TreeNode = TreeNode(
    node_for=[LoadMgmtFunction],
    children="Switches",
    label="=Switches",
    tooltip="",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)
LoadMgmtFunction_LoadMgmtRecords_TreeNode = TreeNode(
    node_for=[LoadMgmtFunction],
    children="LoadMgmtRecords",
    label="=LoadMgmtRecords",
    tooltip="",
    add=[LoadMgmtRecord],
    move=[LoadMgmtRecord],
    icon_path=IMAGE_PATH)

LoadLimitFunction_TreeNode = TreeNode(
    node_for=[LoadLimitFunction],
    label="name",
    tooltip="A kind of LoadMgmtFunction that limits the customer load to a given value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadMgmtRecord_TreeNode = TreeNode(
    node_for=[LoadMgmtRecord],
    label="name",
    tooltip="A log of actual measured load reductions as a result of load shed operations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadShedFunction_TreeNode = TreeNode(
    node_for=[LoadShedFunction],
    label="name",
    tooltip="A kind of LoadMgmtFunction that sheds a part of the customer load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ComPort_TreeNode = TreeNode(
    node_for=[ComPort],
    label="name",
    tooltip="Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WaterMeteringFunction_TreeNode = TreeNode(
    node_for=[WaterMeteringFunction],
    label="name",
    tooltip="Functionality performed by a water meter. It's entirely possible that the metering system would carry information to/from water meters even though it was built primarily to carry the higher-value electric meter data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GasMeteringFunction_TreeNode = TreeNode(
    node_for=[GasMeteringFunction],
    label="name",
    tooltip="Functionality performed by a gas meter. It's entirely possible that the metering system would carry information to/from gas meters even though it was built primarily to carry the higher-value electric meter data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeteringFunctionConfiguration_TreeNode = TreeNode(
    node_for=[MeteringFunctionConfiguration],
    label="name",
    tooltip="The configuration of data for a given meter function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeteringFunctionConfiguration_ElectricMeteringFunctions_TreeNode = TreeNode(
    node_for=[MeteringFunctionConfiguration],
    children="ElectricMeteringFunctions",
    label="=ElectricMeteringFunctions",
    tooltip="All electric metering functions with this configuration.",
    add=[ElectricMeteringFunction],
    move=[ElectricMeteringFunction],
    icon_path=IMAGE_PATH)

Organisation_TreeNode = TreeNode(
    node_for=[Organisation],
    label="name",
    tooltip="Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Organisation_BusinessRoles_TreeNode = TreeNode(
    node_for=[Organisation],
    children="BusinessRoles",
    label="=BusinessRoles",
    tooltip="",
    add=[BusinessRole],
    move=[BusinessRole],
    icon_path=IMAGE_PATH)
Organisation_TelephoneNumbers_TreeNode = TreeNode(
    node_for=[Organisation],
    children="TelephoneNumbers",
    label="=TelephoneNumbers",
    tooltip="All telephone numbers of this organisation.",
    add=[TelephoneNumber],
    move=[TelephoneNumber],
    icon_path=IMAGE_PATH)
Organisation_MarketRoles_TreeNode = TreeNode(
    node_for=[Organisation],
    children="MarketRoles",
    label="=MarketRoles",
    tooltip="",
    add=[MarketRole],
    move=[MarketRole],
    icon_path=IMAGE_PATH)
Organisation_ElectronicAddresses_TreeNode = TreeNode(
    node_for=[Organisation],
    children="ElectronicAddresses",
    label="=ElectronicAddresses",
    tooltip="All electronic addresses of this organisation.",
    add=[ElectronicAddress],
    move=[ElectronicAddress],
    icon_path=IMAGE_PATH)

ActivityRecord_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    label="name",
    tooltip="Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ActivityRecord_MarketFactors_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="MarketFactors",
    label="=MarketFactors",
    tooltip="",
    add=[MarketFactors],
    move=[MarketFactors],
    icon_path=IMAGE_PATH)
ActivityRecord_Documents_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="Documents",
    label="=Documents",
    tooltip="All documents for which this activity record has been created.",
    add=[Document],
    move=[Document],
    icon_path=IMAGE_PATH)
ActivityRecord_Organisations_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="Organisations",
    label="=Organisations",
    tooltip="",
    add=[ErpOrganisation],
    move=[ErpOrganisation],
    icon_path=IMAGE_PATH)
ActivityRecord_Assets_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="Assets",
    label="=Assets",
    tooltip="All assets for which this activity record has been created.",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
ActivityRecord_ErpPersons_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)
ActivityRecord_Locations_TreeNode = TreeNode(
    node_for=[ActivityRecord],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

Document_TreeNode = TreeNode(
    node_for=[Document],
    label="name",
    tooltip="Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Document_ActivityRecords_TreeNode = TreeNode(
    node_for=[Document],
    children="ActivityRecords",
    label="=ActivityRecords",
    tooltip="All activity records created for this document.",
    add=[ActivityRecord],
    move=[ActivityRecord],
    icon_path=IMAGE_PATH)
Document_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[DocOrgRole],
    move=[DocOrgRole],
    icon_path=IMAGE_PATH)
Document_ScheduledEvents_TreeNode = TreeNode(
    node_for=[Document],
    children="ScheduledEvents",
    label="=ScheduledEvents",
    tooltip="",
    add=[ScheduledEvent],
    move=[ScheduledEvent],
    icon_path=IMAGE_PATH)
Document_FromDocumentRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="FromDocumentRoles",
    label="=FromDocumentRoles",
    tooltip="",
    add=[DocDocRole],
    move=[DocDocRole],
    icon_path=IMAGE_PATH)
Document_LocationRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="LocationRoles",
    label="=LocationRoles",
    tooltip="",
    add=[DocLocRole],
    move=[DocLocRole],
    icon_path=IMAGE_PATH)
Document_PowerSystemResourceRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="PowerSystemResourceRoles",
    label="=PowerSystemResourceRoles",
    tooltip="",
    add=[DocPsrRole],
    move=[DocPsrRole],
    icon_path=IMAGE_PATH)
Document_NetworkDataSets_TreeNode = TreeNode(
    node_for=[Document],
    children="NetworkDataSets",
    label="=NetworkDataSets",
    tooltip="",
    add=[NetworkDataSet],
    move=[NetworkDataSet],
    icon_path=IMAGE_PATH)
Document_ErpPersonRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="ErpPersonRoles",
    label="=ErpPersonRoles",
    tooltip="",
    add=[DocErpPersonRole],
    move=[DocErpPersonRole],
    icon_path=IMAGE_PATH)
Document_ChangeItems_TreeNode = TreeNode(
    node_for=[Document],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
Document_Measurements_TreeNode = TreeNode(
    node_for=[Document],
    children="Measurements",
    label="=Measurements",
    tooltip="Measurements are specified in types of documents, such as procedures.",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
Document_ScheduleParameterInfos_TreeNode = TreeNode(
    node_for=[Document],
    children="ScheduleParameterInfos",
    label="=ScheduleParameterInfos",
    tooltip="",
    add=[ScheduleParameterInfo],
    move=[ScheduleParameterInfo],
    icon_path=IMAGE_PATH)
Document_ToDocumentRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="ToDocumentRoles",
    label="=ToDocumentRoles",
    tooltip="",
    add=[DocDocRole],
    move=[DocDocRole],
    icon_path=IMAGE_PATH)
Document_AssetRoles_TreeNode = TreeNode(
    node_for=[Document],
    children="AssetRoles",
    label="=AssetRoles",
    tooltip="",
    add=[DocAssetRole],
    move=[DocAssetRole],
    icon_path=IMAGE_PATH)
Document_ChangeSets_TreeNode = TreeNode(
    node_for=[Document],
    children="ChangeSets",
    label="=ChangeSets",
    tooltip="",
    add=[ChangeSet],
    move=[ChangeSet],
    icon_path=IMAGE_PATH)

PositionPoint_TreeNode = TreeNode(
    node_for=[PositionPoint],
        tooltip="Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Agreement_TreeNode = TreeNode(
    node_for=[Agreement],
    label="name",
    tooltip="Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Location_TreeNode = TreeNode(
    node_for=[Location],
    label="name",
    tooltip="The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Location_DocumentRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="DocumentRoles",
    label="=DocumentRoles",
    tooltip="",
    add=[DocLocRole],
    move=[DocLocRole],
    icon_path=IMAGE_PATH)
Location_ErpPersonRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="ErpPersonRoles",
    label="=ErpPersonRoles",
    tooltip="",
    add=[ErpPersonLocRole],
    move=[ErpPersonLocRole],
    icon_path=IMAGE_PATH)
Location_ElectronicAddresses_TreeNode = TreeNode(
    node_for=[Location],
    children="ElectronicAddresses",
    label="=ElectronicAddresses",
    tooltip="All electronic addresses of this location.",
    add=[ElectronicAddress],
    move=[ElectronicAddress],
    icon_path=IMAGE_PATH)
Location_ChangeItems_TreeNode = TreeNode(
    node_for=[Location],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
Location_Routes_TreeNode = TreeNode(
    node_for=[Location],
    children="Routes",
    label="=Routes",
    tooltip="",
    add=[Route],
    move=[Route],
    icon_path=IMAGE_PATH)
Location_PositionPoints_TreeNode = TreeNode(
    node_for=[Location],
    children="PositionPoints",
    label="=PositionPoints",
    tooltip="Sequence of position points describing this location.",
    add=[PositionPoint],
    move=[PositionPoint],
    icon_path=IMAGE_PATH)
Location_GmlSelectors_TreeNode = TreeNode(
    node_for=[Location],
    children="GmlSelectors",
    label="=GmlSelectors",
    tooltip="",
    add=[GmlSelector],
    move=[GmlSelector],
    icon_path=IMAGE_PATH)
Location_FromLocationRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="FromLocationRoles",
    label="=FromLocationRoles",
    tooltip="",
    add=[LocLocRole],
    move=[LocLocRole],
    icon_path=IMAGE_PATH)
Location_ToLocationRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="ToLocationRoles",
    label="=ToLocationRoles",
    tooltip="",
    add=[LocLocRole],
    move=[LocLocRole],
    icon_path=IMAGE_PATH)
Location_TelephoneNumbers_TreeNode = TreeNode(
    node_for=[Location],
    children="TelephoneNumbers",
    label="=TelephoneNumbers",
    tooltip="All telephone numbers of this location.",
    add=[TelephoneNumber],
    move=[TelephoneNumber],
    icon_path=IMAGE_PATH)
Location_LandProperties_TreeNode = TreeNode(
    node_for=[Location],
    children="LandProperties",
    label="=LandProperties",
    tooltip="",
    add=[LandProperty],
    move=[LandProperty],
    icon_path=IMAGE_PATH)
Location_Measurements_TreeNode = TreeNode(
    node_for=[Location],
    children="Measurements",
    label="=Measurements",
    tooltip="",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
Location_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[OrgLocRole],
    move=[OrgLocRole],
    icon_path=IMAGE_PATH)
Location_AssetRoles_TreeNode = TreeNode(
    node_for=[Location],
    children="AssetRoles",
    label="=AssetRoles",
    tooltip="",
    add=[AssetLocRole],
    move=[AssetLocRole],
    icon_path=IMAGE_PATH)
Location_Crews_TreeNode = TreeNode(
    node_for=[Location],
    children="Crews",
    label="=Crews",
    tooltip="",
    add=[Crew],
    move=[Crew],
    icon_path=IMAGE_PATH)
Location_RedLines_TreeNode = TreeNode(
    node_for=[Location],
    children="RedLines",
    label="=RedLines",
    tooltip="",
    add=[RedLine],
    move=[RedLine],
    icon_path=IMAGE_PATH)
Location_GmlObservatins_TreeNode = TreeNode(
    node_for=[Location],
    children="GmlObservatins",
    label="=GmlObservatins",
    tooltip="",
    add=[GmlObservation],
    move=[GmlObservation],
    icon_path=IMAGE_PATH)
Location_Hazards_TreeNode = TreeNode(
    node_for=[Location],
    children="Hazards",
    label="=Hazards",
    tooltip="",
    add=[Hazard],
    move=[Hazard],
    icon_path=IMAGE_PATH)
Location_ActivityRecords_TreeNode = TreeNode(
    node_for=[Location],
    children="ActivityRecords",
    label="=ActivityRecords",
    tooltip="",
    add=[ActivityRecord],
    move=[ActivityRecord],
    icon_path=IMAGE_PATH)

TimeSchedule_TreeNode = TreeNode(
    node_for=[TimeSchedule],
    label="name",
    tooltip="Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TimeSchedule_TimePoints_TreeNode = TreeNode(
    node_for=[TimeSchedule],
    children="TimePoints",
    label="=TimePoints",
    tooltip="Sequence of time points belonging to this time schedule.",
    add=[TimePoint],
    move=[TimePoint],
    icon_path=IMAGE_PATH)

StreetAddress_TreeNode = TreeNode(
    node_for=[StreetAddress],
        tooltip="General purpose street address information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TelephoneNumber_TreeNode = TreeNode(
    node_for=[TelephoneNumber],
    label="name",
    tooltip="Telephone number.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DateTimeInterval_TreeNode = TreeNode(
    node_for=[DateTimeInterval],
        tooltip="Interval of date and time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PostalAddress_TreeNode = TreeNode(
    node_for=[PostalAddress],
        tooltip="General purpose postal address information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TownDetail_TreeNode = TreeNode(
    node_for=[TownDetail],
    label="name",
    tooltip="Town details, in the context of address.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ElectronicAddress_TreeNode = TreeNode(
    node_for=[ElectronicAddress],
    label="name",
    tooltip="Electronic address information.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ElectronicAddress_ErpTelephoneNumbers_TreeNode = TreeNode(
    node_for=[ElectronicAddress],
    children="ErpTelephoneNumbers",
    label="=ErpTelephoneNumbers",
    tooltip="",
    add=[ErpTelephoneNumber],
    move=[ErpTelephoneNumber],
    icon_path=IMAGE_PATH)
ElectronicAddress_Locations_TreeNode = TreeNode(
    node_for=[ElectronicAddress],
    children="Locations",
    label="=Locations",
    tooltip="All locations having this electronic address.",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)

TimePoint_TreeNode = TreeNode(
    node_for=[TimePoint],
    label="name",
    tooltip="A point in time within a sequence of points in time relative to a TimeSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TimePoint_ScheduledEvents_TreeNode = TreeNode(
    node_for=[TimePoint],
    children="ScheduledEvents",
    label="=ScheduledEvents",
    tooltip="",
    add=[ScheduledEvent],
    move=[ScheduledEvent],
    icon_path=IMAGE_PATH)

UserAttribute_TreeNode = TreeNode(
    node_for=[UserAttribute],
    label="name",
    tooltip="Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

UserAttribute_PropertyAssets_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="PropertyAssets",
    label="=PropertyAssets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
UserAttribute_RatingAssets_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="RatingAssets",
    label="=RatingAssets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
UserAttribute_ErpLedgerEntries_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="ErpLedgerEntries",
    label="=ErpLedgerEntries",
    tooltip="",
    add=[ErpLedgerEntry],
    move=[ErpLedgerEntry],
    icon_path=IMAGE_PATH)
UserAttribute_ProcedureDataSets_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="ProcedureDataSets",
    label="=ProcedureDataSets",
    tooltip="",
    add=[ProcedureDataSet],
    move=[ProcedureDataSet],
    icon_path=IMAGE_PATH)
UserAttribute_PassThroughBills_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="PassThroughBills",
    label="=PassThroughBills",
    tooltip="",
    add=[PassThroughBill],
    move=[PassThroughBill],
    icon_path=IMAGE_PATH)
UserAttribute_ErpInvoiceLineItems_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="ErpInvoiceLineItems",
    label="=ErpInvoiceLineItems",
    tooltip="",
    add=[ErpInvoiceLineItem],
    move=[ErpInvoiceLineItem],
    icon_path=IMAGE_PATH)
UserAttribute_BillDeterminants_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="BillDeterminants",
    label="=BillDeterminants",
    tooltip="",
    add=[BillDeterminant],
    move=[BillDeterminant],
    icon_path=IMAGE_PATH)
UserAttribute_ErpStatementLineItems_TreeNode = TreeNode(
    node_for=[UserAttribute],
    children="ErpStatementLineItems",
    label="=ErpStatementLineItems",
    tooltip="",
    add=[MarketStatementLineItem],
    move=[MarketStatementLineItem],
    icon_path=IMAGE_PATH)

Status_TreeNode = TreeNode(
    node_for=[Status],
        tooltip="Current status information relevant to an entity.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StreetDetail_TreeNode = TreeNode(
    node_for=[StreetDetail],
    label="name",
    tooltip="Street details, in the context of address.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeoLocation_TreeNode = TreeNode(
    node_for=[GeoLocation],
    label="name",
    tooltip="Geographical location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeoLocation_PowerSystemResources_TreeNode = TreeNode(
    node_for=[GeoLocation],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="All power system resources at this geographical location.",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

Seal_TreeNode = TreeNode(
    node_for=[Seal],
    label="name",
    tooltip="Physically controls access to AssetContainers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Asset_TreeNode = TreeNode(
    node_for=[Asset],
    label="name",
    tooltip="Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Asset_Measurements_TreeNode = TreeNode(
    node_for=[Asset],
    children="Measurements",
    label="=Measurements",
    tooltip="",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
Asset_Hazards_TreeNode = TreeNode(
    node_for=[Asset],
    children="Hazards",
    label="=Hazards",
    tooltip="",
    add=[Hazard],
    move=[Hazard],
    icon_path=IMAGE_PATH)
Asset_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[OrgAssetRole],
    move=[OrgAssetRole],
    icon_path=IMAGE_PATH)
Asset_ScheduledEvents_TreeNode = TreeNode(
    node_for=[Asset],
    children="ScheduledEvents",
    label="=ScheduledEvents",
    tooltip="",
    add=[ScheduledEvent],
    move=[ScheduledEvent],
    icon_path=IMAGE_PATH)
Asset_Mediums_TreeNode = TreeNode(
    node_for=[Asset],
    children="Mediums",
    label="=Mediums",
    tooltip="",
    add=[Medium],
    move=[Medium],
    icon_path=IMAGE_PATH)
Asset_AssetFunctions_TreeNode = TreeNode(
    node_for=[Asset],
    children="AssetFunctions",
    label="=AssetFunctions",
    tooltip="",
    add=[AssetFunction],
    move=[AssetFunction],
    icon_path=IMAGE_PATH)
Asset_Properties_TreeNode = TreeNode(
    node_for=[Asset],
    children="Properties",
    label="=Properties",
    tooltip="UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
Asset_Ratings_TreeNode = TreeNode(
    node_for=[Asset],
    children="Ratings",
    label="=Ratings",
    tooltip="UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)
Asset_ActivityRecords_TreeNode = TreeNode(
    node_for=[Asset],
    children="ActivityRecords",
    label="=ActivityRecords",
    tooltip="All activity records created for this asset.",
    add=[ActivityRecord],
    move=[ActivityRecord],
    icon_path=IMAGE_PATH)
Asset_FromAssetRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="FromAssetRoles",
    label="=FromAssetRoles",
    tooltip="",
    add=[AssetAssetRole],
    move=[AssetAssetRole],
    icon_path=IMAGE_PATH)
Asset_LocationRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="LocationRoles",
    label="=LocationRoles",
    tooltip="",
    add=[AssetLocRole],
    move=[AssetLocRole],
    icon_path=IMAGE_PATH)
Asset_PowerSystemResourceRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="PowerSystemResourceRoles",
    label="=PowerSystemResourceRoles",
    tooltip="",
    add=[AssetPsrRole],
    move=[AssetPsrRole],
    icon_path=IMAGE_PATH)
Asset_DocumentRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="DocumentRoles",
    label="=DocumentRoles",
    tooltip="",
    add=[DocAssetRole],
    move=[DocAssetRole],
    icon_path=IMAGE_PATH)
Asset_ChangeItems_TreeNode = TreeNode(
    node_for=[Asset],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
Asset_ElectronicAddresses_TreeNode = TreeNode(
    node_for=[Asset],
    children="ElectronicAddresses",
    label="=ElectronicAddresses",
    tooltip="All electronic addresses of this asset.",
    add=[ElectronicAddress],
    move=[ElectronicAddress],
    icon_path=IMAGE_PATH)
Asset_ErpRecDeliveryItems_TreeNode = TreeNode(
    node_for=[Asset],
    children="ErpRecDeliveryItems",
    label="=ErpRecDeliveryItems",
    tooltip="",
    add=[ErpRecDelvLineItem],
    move=[ErpRecDelvLineItem],
    icon_path=IMAGE_PATH)
Asset_ReliabilityInfos_TreeNode = TreeNode(
    node_for=[Asset],
    children="ReliabilityInfos",
    label="=ReliabilityInfos",
    tooltip="",
    add=[ReliabilityInfo],
    move=[ReliabilityInfo],
    icon_path=IMAGE_PATH)
Asset_ToAssetRoles_TreeNode = TreeNode(
    node_for=[Asset],
    children="ToAssetRoles",
    label="=ToAssetRoles",
    tooltip="",
    add=[AssetAssetRole],
    move=[AssetAssetRole],
    icon_path=IMAGE_PATH)
Asset_AssetPropertyCurves_TreeNode = TreeNode(
    node_for=[Asset],
    children="AssetPropertyCurves",
    label="=AssetPropertyCurves",
    tooltip="",
    add=[AssetPropertyCurve],
    move=[AssetPropertyCurve],
    icon_path=IMAGE_PATH)

AssetFunction_TreeNode = TreeNode(
    node_for=[AssetFunction],
    label="name",
    tooltip="Function performed by an asset. Often, function is a module (or a board that plugs into a backplane) that can be replaced or updated without impacting the rest of the asset. Therefore functions are treated as assets because they have life-cycles that are independent of the asset containing the function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ElectricalInfo_TreeNode = TreeNode(
    node_for=[ElectricalInfo],
    label="name",
    tooltip="Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ElectricalInfo_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[ElectricalInfo],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets having this set of electrical properties.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)
ElectricalInfo_ElectricalTypeAssets_TreeNode = TreeNode(
    node_for=[ElectricalInfo],
    children="ElectricalTypeAssets",
    label="=ElectricalTypeAssets",
    tooltip="",
    add=[ElectricalTypeAsset],
    move=[ElectricalTypeAsset],
    icon_path=IMAGE_PATH)
ElectricalInfo_ElectricalAssets_TreeNode = TreeNode(
    node_for=[ElectricalInfo],
    children="ElectricalAssets",
    label="=ElectricalAssets",
    tooltip="",
    add=[ElectricalAsset],
    move=[ElectricalAsset],
    icon_path=IMAGE_PATH)
ElectricalInfo_ElectricalAssetModels_TreeNode = TreeNode(
    node_for=[ElectricalInfo],
    children="ElectricalAssetModels",
    label="=ElectricalAssetModels",
    tooltip="",
    add=[ElectricalAssetModel],
    move=[ElectricalAssetModel],
    icon_path=IMAGE_PATH)

ComMediaAsset_TreeNode = TreeNode(
    node_for=[ComMediaAsset],
    label="name",
    tooltip="Communication media such as fibre optic cable, power-line, telephone, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AssetContainer_TreeNode = TreeNode(
    node_for=[AssetContainer],
    label="name",
    tooltip="Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetContainer_LandProperties_TreeNode = TreeNode(
    node_for=[AssetContainer],
    children="LandProperties",
    label="=LandProperties",
    tooltip="",
    add=[LandProperty],
    move=[LandProperty],
    icon_path=IMAGE_PATH)
AssetContainer_Assets_TreeNode = TreeNode(
    node_for=[AssetContainer],
    children="Assets",
    label="=Assets",
    tooltip="",
    add=[Asset],
    move=[Asset],
    icon_path=IMAGE_PATH)
AssetContainer_Seals_TreeNode = TreeNode(
    node_for=[AssetContainer],
    children="Seals",
    label="=Seals",
    tooltip="All seals applied to this asset container.",
    add=[Seal],
    move=[Seal],
    icon_path=IMAGE_PATH)

AcceptanceTest_TreeNode = TreeNode(
    node_for=[AcceptanceTest],
        tooltip="Acceptance test for assets.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AssetModel_TreeNode = TreeNode(
    node_for=[AssetModel],
    label="name",
    tooltip="Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AssetModel_ErpInventoryCounts_TreeNode = TreeNode(
    node_for=[AssetModel],
    children="ErpInventoryCounts",
    label="=ErpInventoryCounts",
    tooltip="",
    add=[ErpInventoryCount],
    move=[ErpInventoryCount],
    icon_path=IMAGE_PATH)
AssetModel_AssetModelCatalogueItems_TreeNode = TreeNode(
    node_for=[AssetModel],
    children="AssetModelCatalogueItems",
    label="=AssetModelCatalogueItems",
    tooltip="",
    add=[AssetModelCatalogueItem],
    move=[AssetModelCatalogueItem],
    icon_path=IMAGE_PATH)

DistributionWindingTest_TreeNode = TreeNode(
    node_for=[DistributionWindingTest],
    label="name",
    tooltip="Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindingInfo_TreeNode = TreeNode(
    node_for=[WindingInfo],
    label="name",
    tooltip="Winding data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WindingInfo_WindingTests_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="WindingTests",
    label="=WindingTests",
    tooltip="All winding tests during which voltage or current was applied to this winding.",
    add=[DistributionWindingTest],
    move=[DistributionWindingTest],
    icon_path=IMAGE_PATH)
WindingInfo_Windings_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="Windings",
    label="=Windings",
    tooltip="All windings described by this winding data.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)
WindingInfo_ToWindingSpecs_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="ToWindingSpecs",
    label="=ToWindingSpecs",
    tooltip="Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)

ConductorInfo_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    label="name",
    tooltip="Conductor data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductorInfo_ConductorSegments_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this conductor data.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)
ConductorInfo_WireArrangements_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="All wire arrangements (single wires) that make this conductor.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)

CableInfo_TreeNode = TreeNode(
    node_for=[CableInfo],
    label="name",
    tooltip="Cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConcentricNeutralCableInfo_TreeNode = TreeNode(
    node_for=[ConcentricNeutralCableInfo],
    label="name",
    tooltip="Concentric neutral cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WireArrangement_TreeNode = TreeNode(
    node_for=[WireArrangement],
    label="name",
    tooltip="Identification, spacing and configuration of the wires of a Conductor, with reference to their type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WireType_TreeNode = TreeNode(
    node_for=[WireType],
    label="name",
    tooltip="Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WireType_WireArrangements_TreeNode = TreeNode(
    node_for=[WireType],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="All wire arrangements using this wire type.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)
WireType_ConcentricNeutralCableInfos_TreeNode = TreeNode(
    node_for=[WireType],
    children="ConcentricNeutralCableInfos",
    label="=ConcentricNeutralCableInfos",
    tooltip="All concentric neutral cables using this wire type.",
    add=[ConcentricNeutralCableInfo],
    move=[ConcentricNeutralCableInfo],
    icon_path=IMAGE_PATH)

ShortCircuitTest_TreeNode = TreeNode(
    node_for=[ShortCircuitTest],
    label="name",
    tooltip="Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShortCircuitTest_ShortedWindingSpecs_TreeNode = TreeNode(
    node_for=[ShortCircuitTest],
    children="ShortedWindingSpecs",
    label="=ShortedWindingSpecs",
    tooltip="All windings short-circuited during this test.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)

OverheadConductorInfo_TreeNode = TreeNode(
    node_for=[OverheadConductorInfo],
    label="name",
    tooltip="Overhead conductor data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OpenCircuitTest_TreeNode = TreeNode(
    node_for=[OpenCircuitTest],
    label="name",
    tooltip="Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OpenCircuitTest_MeasuredWindingSpecs_TreeNode = TreeNode(
    node_for=[OpenCircuitTest],
    children="MeasuredWindingSpecs",
    label="=MeasuredWindingSpecs",
    tooltip="All other windings measured during this test.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)

TransformerInfo_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    label="name",
    tooltip="Set of transformer data, from an equipment library.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerInfo_Transformers_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="Transformers",
    label="=Transformers",
    tooltip="All transformers that can be described with this transformer data.",
    add=[DistributionTransformer],
    move=[DistributionTransformer],
    icon_path=IMAGE_PATH)
TransformerInfo_TransformerAssets_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="TransformerAssets",
    label="=TransformerAssets",
    tooltip="",
    add=[TransformerAsset],
    move=[TransformerAsset],
    icon_path=IMAGE_PATH)
TransformerInfo_WindingInfos_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="WindingInfos",
    label="=WindingInfos",
    tooltip="Data for all the windings described by this transformer data.",
    add=[WindingInfo],
    move=[WindingInfo],
    icon_path=IMAGE_PATH)
TransformerInfo_TransformerAssetModels_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="TransformerAssetModels",
    label="=TransformerAssetModels",
    tooltip="",
    add=[TransformerAssetModel],
    move=[TransformerAssetModel],
    icon_path=IMAGE_PATH)

ToWindingSpec_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    label="name",
    tooltip="For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ToWindingSpec_OpenCircuitTests_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    children="OpenCircuitTests",
    label="=OpenCircuitTests",
    tooltip="All open-circuit tests in which this winding was measured.",
    add=[OpenCircuitTest],
    move=[OpenCircuitTest],
    icon_path=IMAGE_PATH)
ToWindingSpec_ShortCircuitTests_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    children="ShortCircuitTests",
    label="=ShortCircuitTests",
    tooltip="All short-circuit tests in which this winding was short-circuited.",
    add=[ShortCircuitTest],
    move=[ShortCircuitTest],
    icon_path=IMAGE_PATH)

TapeShieldCableInfo_TreeNode = TreeNode(
    node_for=[TapeShieldCableInfo],
    label="name",
    tooltip="Tape shield cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EndDeviceModel_TreeNode = TreeNode(
    node_for=[EndDeviceModel],
    label="name",
    tooltip="Documentation for particular end device product model made by a manufacturer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EndDeviceModel_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[EndDeviceModel],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets being of this model.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)

MerchantAccount_TreeNode = TreeNode(
    node_for=[MerchantAccount],
    label="name",
    tooltip="The operating account controlled by MerchantAgreement, against which Vendor may vend tokens or receipt payments. Transactions via VendorShift debit the account and bank deposits via BankStatement credit the account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MerchantAccount_Vendors_TreeNode = TreeNode(
    node_for=[MerchantAccount],
    children="Vendors",
    label="=Vendors",
    tooltip="All vendors selling tokens or receipt payments against this merchant account.",
    add=[Vendor],
    move=[Vendor],
    icon_path=IMAGE_PATH)
MerchantAccount_Transactors_TreeNode = TreeNode(
    node_for=[MerchantAccount],
    children="Transactors",
    label="=Transactors",
    tooltip="All transactors this merchant account is registered with.",
    add=[Transactor],
    move=[Transactor],
    icon_path=IMAGE_PATH)
MerchantAccount_BankStatements_TreeNode = TreeNode(
    node_for=[MerchantAccount],
    children="BankStatements",
    label="=BankStatements",
    tooltip="",
    add=[BankStatement],
    move=[BankStatement],
    icon_path=IMAGE_PATH)
MerchantAccount_VendorShifts_TreeNode = TreeNode(
    node_for=[MerchantAccount],
    children="VendorShifts",
    label="=VendorShifts",
    tooltip="All vendor shifts that operate on this merchant account.",
    add=[VendorShift],
    move=[VendorShift],
    icon_path=IMAGE_PATH)

AuxiliaryAccount_TreeNode = TreeNode(
    node_for=[AuxiliaryAccount],
    label="name",
    tooltip="Variable and dynamic part of AuxiliaryAgreement, generally representing the current state of the account related to the outstanding balance defined in AuxiliaryAgreement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AuxiliaryAccount_Charges_TreeNode = TreeNode(
    node_for=[AuxiliaryAccount],
    children="Charges",
    label="=Charges",
    tooltip="All charges levied on this account.",
    add=[Charge],
    move=[Charge],
    icon_path=IMAGE_PATH)
AuxiliaryAccount_PaymentTransactions_TreeNode = TreeNode(
    node_for=[AuxiliaryAccount],
    children="PaymentTransactions",
    label="=PaymentTransactions",
    tooltip="All payments against this account.",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)

BankAccountDetail_TreeNode = TreeNode(
    node_for=[BankAccountDetail],
        tooltip="Details of a bank account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AccountMovement_TreeNode = TreeNode(
    node_for=[AccountMovement],
        tooltip="Credit/debit movements for an account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TimeTariffInterval_TreeNode = TreeNode(
    node_for=[TimeTariffInterval],
        tooltip="One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TimeTariffInterval_TariffProfiles_TreeNode = TreeNode(
    node_for=[TimeTariffInterval],
    children="TariffProfiles",
    label="=TariffProfiles",
    tooltip="All tariff profiles defined by this time tariff interval.",
    add=[TariffProfile],
    move=[TariffProfile],
    icon_path=IMAGE_PATH)
TimeTariffInterval_Charges_TreeNode = TreeNode(
    node_for=[TimeTariffInterval],
    children="Charges",
    label="=Charges",
    tooltip="All charges used to define this time tariff interval.",
    add=[Charge],
    move=[Charge],
    icon_path=IMAGE_PATH)

Due_TreeNode = TreeNode(
    node_for=[Due],
        tooltip="Details on amounts due for an account.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConsumptionTariffInterval_TreeNode = TreeNode(
    node_for=[ConsumptionTariffInterval],
        tooltip="One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConsumptionTariffInterval_Charges_TreeNode = TreeNode(
    node_for=[ConsumptionTariffInterval],
    children="Charges",
    label="=Charges",
    tooltip="All charges used to define this consumption tariff interval.",
    add=[Charge],
    move=[Charge],
    icon_path=IMAGE_PATH)
ConsumptionTariffInterval_TariffProfiles_TreeNode = TreeNode(
    node_for=[ConsumptionTariffInterval],
    children="TariffProfiles",
    label="=TariffProfiles",
    tooltip="All tariff profiles defined by this consumption tariff interval.",
    add=[TariffProfile],
    move=[TariffProfile],
    icon_path=IMAGE_PATH)

Cashier_TreeNode = TreeNode(
    node_for=[Cashier],
    label="name",
    tooltip="The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Cashier_ElectronicAddresses_TreeNode = TreeNode(
    node_for=[Cashier],
    children="ElectronicAddresses",
    label="=ElectronicAddresses",
    tooltip="",
    add=[ElectronicAddress],
    move=[ElectronicAddress],
    icon_path=IMAGE_PATH)
Cashier_CashierShifts_TreeNode = TreeNode(
    node_for=[Cashier],
    children="CashierShifts",
    label="=CashierShifts",
    tooltip="All shifts operated by this cashier.",
    add=[CashierShift],
    move=[CashierShift],
    icon_path=IMAGE_PATH)

Shift_TreeNode = TreeNode(
    node_for=[Shift],
    label="name",
    tooltip="Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from Receipt attributes: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Shift_ReceiptSummaries_TreeNode = TreeNode(
    node_for=[Shift],
    children="ReceiptSummaries",
    label="=ReceiptSummaries",
    tooltip="All receipt summaries for this shift.",
    add=[ReceiptSummary],
    move=[ReceiptSummary],
    icon_path=IMAGE_PATH)
Shift_TransactionSummaries_TreeNode = TreeNode(
    node_for=[Shift],
    children="TransactionSummaries",
    label="=TransactionSummaries",
    tooltip="All transaction summaries recorded for this shift.",
    add=[TransactionSummary],
    move=[TransactionSummary],
    icon_path=IMAGE_PATH)

VendorShift_TreeNode = TreeNode(
    node_for=[VendorShift],
    label="name",
    tooltip="The operating shift for a vendor during which he may transact against the merchant's account. It aggregates transactions and receipts during the shift and periodically debits a merchant account. The totals in VendorShift should always = sum of totals aggregated in all cashier shifts that were open under the particular vendor shift.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VendorShift_Transactions_TreeNode = TreeNode(
    node_for=[VendorShift],
    children="Transactions",
    label="=Transactions",
    tooltip="",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)
VendorShift_Receipts_TreeNode = TreeNode(
    node_for=[VendorShift],
    children="Receipts",
    label="=Receipts",
    tooltip="",
    add=[Receipt],
    move=[Receipt],
    icon_path=IMAGE_PATH)

MerchantAgreement_TreeNode = TreeNode(
    node_for=[MerchantAgreement],
    label="name",
    tooltip="A formal controlling contractual agreement between Supplier and Merchant, in terms of which Merchant is authorised to vend tokens and receipt payments on behalf of Supplier. Merchant is accountable to Supplier for revenue collected at PointOfSale.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MerchantAgreement_MerchantAccounts_TreeNode = TreeNode(
    node_for=[MerchantAgreement],
    children="MerchantAccounts",
    label="=MerchantAccounts",
    tooltip="All merchant accounts instantiated as a result of this merchant agreement.",
    add=[MerchantAccount],
    move=[MerchantAccount],
    icon_path=IMAGE_PATH)

Charge_TreeNode = TreeNode(
    node_for=[Charge],
    label="name",
    tooltip="A charge element associated with other entities such as tariff structures, auxiliary agreements or other charge elements. The total charge amount applicable to this instance of Charge is the sum of fixedPortion plus percentagePortion.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Charge_ConsumptionTariffIntervals_TreeNode = TreeNode(
    node_for=[Charge],
    children="ConsumptionTariffIntervals",
    label="=ConsumptionTariffIntervals",
    tooltip="Tariff intervals to which this consumption-based charge must be levied.",
    add=[ConsumptionTariffInterval],
    move=[ConsumptionTariffInterval],
    icon_path=IMAGE_PATH)
Charge_AuxiliaryAccounts_TreeNode = TreeNode(
    node_for=[Charge],
    children="AuxiliaryAccounts",
    label="=AuxiliaryAccounts",
    tooltip="All auxiliary accounts to which this charge must be levied.",
    add=[AuxiliaryAccount],
    move=[AuxiliaryAccount],
    icon_path=IMAGE_PATH)
Charge_TimeTariffIntervals_TreeNode = TreeNode(
    node_for=[Charge],
    children="TimeTariffIntervals",
    label="=TimeTariffIntervals",
    tooltip="Tariff intervals to which this time-based charge must be levied.",
    add=[TimeTariffInterval],
    move=[TimeTariffInterval],
    icon_path=IMAGE_PATH)
Charge_ChildCharges_TreeNode = TreeNode(
    node_for=[Charge],
    children="ChildCharges",
    label="=ChildCharges",
    tooltip="All sub-components of this complex charge.",
    add=[Charge],
    move=[Charge],
    icon_path=IMAGE_PATH)

ServiceSupplier_TreeNode = TreeNode(
    node_for=[ServiceSupplier],
    label="name",
    tooltip="Organisation that provides services to Customers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServiceSupplier_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[ServiceSupplier],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points this service supplier utilises to deliver a service.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)
ServiceSupplier_CustomerAgreements_TreeNode = TreeNode(
    node_for=[ServiceSupplier],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All customer agreements of this service supplier.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
ServiceSupplier_BankAccounts_TreeNode = TreeNode(
    node_for=[ServiceSupplier],
    children="BankAccounts",
    label="=BankAccounts",
    tooltip="All BackAccounts this ServiceSupplier owns.",
    add=[BankAccount],
    move=[BankAccount],
    icon_path=IMAGE_PATH)

Receipt_TreeNode = TreeNode(
    node_for=[Receipt],
    label="name",
    tooltip="Record of total receipted payment from customer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Receipt_Transactions_TreeNode = TreeNode(
    node_for=[Receipt],
    children="Transactions",
    label="=Transactions",
    tooltip="All transactions recorded for this receipted payment.",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)
Receipt_Tenders_TreeNode = TreeNode(
    node_for=[Receipt],
    children="Tenders",
    label="=Tenders",
    tooltip="All payments received in the form of tenders recorded by this receipt.",
    add=[Tender],
    move=[Tender],
    icon_path=IMAGE_PATH)

Tender_TreeNode = TreeNode(
    node_for=[Tender],
    label="name",
    tooltip="Tender is what is 'offered' by the customer towards making a payment and is often more than the required payment (hence the need for 'change'). The payment is thus that part of the Tender that goes towards settlement of a particular transaction. Tender is modelled as an aggregation of Cheque and Card. Both these tender types can exist in a single tender bid thus 'accountHolderName' must exist separately in each of Cheque and Card as each could have a different account holder name.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PointOfSale_TreeNode = TreeNode(
    node_for=[PointOfSale],
    label="name",
    tooltip="Logical point where transactions take place with operational interaction between Cashier and the payment system; in certain cases PointOfSale interacts directly with the end customer, in which case Cashier might not be a real person: for example a self-service kiosk or over the internet.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PointOfSale_Tokens_TreeNode = TreeNode(
    node_for=[PointOfSale],
    children="Tokens",
    label="=Tokens",
    tooltip="All Tokens sold or dispensed at this PointOfSale.",
    add=[Token],
    move=[Token],
    icon_path=IMAGE_PATH)
PointOfSale_CashierShifts_TreeNode = TreeNode(
    node_for=[PointOfSale],
    children="CashierShifts",
    label="=CashierShifts",
    tooltip="All shifts this point of sale operated in.",
    add=[CashierShift],
    move=[CashierShift],
    icon_path=IMAGE_PATH)

CashierShift_TreeNode = TreeNode(
    node_for=[CashierShift],
    label="name",
    tooltip="The operating shift for a cashier, during which he may transact against the CashierShift, subject to VendorShift being open.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CashierShift_Receipts_TreeNode = TreeNode(
    node_for=[CashierShift],
    children="Receipts",
    label="=Receipts",
    tooltip="All Receipts recorded for this Shift.",
    add=[Receipt],
    move=[Receipt],
    icon_path=IMAGE_PATH)
CashierShift_Transactions_TreeNode = TreeNode(
    node_for=[CashierShift],
    children="Transactions",
    label="=Transactions",
    tooltip="",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)

Transaction_TreeNode = TreeNode(
    node_for=[Transaction],
    label="name",
    tooltip="The record of details of payment for service or token sale.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Transaction_UserAttributes_TreeNode = TreeNode(
    node_for=[Transaction],
    children="UserAttributes",
    label="=UserAttributes",
    tooltip="All snapshots of meter parameters recorded at the time of this transaction. Use 'name' and 'value.value' attributes to specify name and value of a parameter from meter.",
    add=[UserAttribute],
    move=[UserAttribute],
    icon_path=IMAGE_PATH)

Transactor_TreeNode = TreeNode(
    node_for=[Transactor],
    label="name",
    tooltip="The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Transactor_MerchantAccounts_TreeNode = TreeNode(
    node_for=[Transactor],
    children="MerchantAccounts",
    label="=MerchantAccounts",
    tooltip="All merchant accounts registered with this transactor.",
    add=[MerchantAccount],
    move=[MerchantAccount],
    icon_path=IMAGE_PATH)

AccountingUnit_TreeNode = TreeNode(
    node_for=[AccountingUnit],
        tooltip="Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TariffProfile_TreeNode = TreeNode(
    node_for=[TariffProfile],
    label="name",
    tooltip="A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TariffProfile_ConsumptionTariffIntervals_TreeNode = TreeNode(
    node_for=[TariffProfile],
    children="ConsumptionTariffIntervals",
    label="=ConsumptionTariffIntervals",
    tooltip="All consumption tariff intervals used to define this tariff profile.",
    add=[ConsumptionTariffInterval],
    move=[ConsumptionTariffInterval],
    icon_path=IMAGE_PATH)
TariffProfile_Tariffs_TreeNode = TreeNode(
    node_for=[TariffProfile],
    children="Tariffs",
    label="=Tariffs",
    tooltip="All tariffs defined by this tariff profile.",
    add=[Tariff],
    move=[Tariff],
    icon_path=IMAGE_PATH)
TariffProfile_TimeTariffIntervals_TreeNode = TreeNode(
    node_for=[TariffProfile],
    children="TimeTariffIntervals",
    label="=TimeTariffIntervals",
    tooltip="All time tariff intervals used to define this tariff profile.",
    add=[TimeTariffInterval],
    move=[TimeTariffInterval],
    icon_path=IMAGE_PATH)

LineDetail_TreeNode = TreeNode(
    node_for=[LineDetail],
        tooltip="Details on an amount line, with rounding, date and note.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AuxiliaryAgreement_TreeNode = TreeNode(
    node_for=[AuxiliaryAgreement],
    label="name",
    tooltip="An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of AuxiliaryAgreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AuxiliaryAgreement_AuxiliaryAccounts_TreeNode = TreeNode(
    node_for=[AuxiliaryAgreement],
    children="AuxiliaryAccounts",
    label="=AuxiliaryAccounts",
    tooltip="All auxiliary accounts regulated by this agreement.",
    add=[AuxiliaryAccount],
    move=[AuxiliaryAccount],
    icon_path=IMAGE_PATH)

Card_TreeNode = TreeNode(
    node_for=[Card],
        tooltip="Documentation of the tender when it is a type of card (credit, debit, etc).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Vendor_TreeNode = TreeNode(
    node_for=[Vendor],
    label="name",
    tooltip="The entity that owns PointOfSale and contracts with Cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by Merchant who is a type of Organisation. Vendor is accountable to Merchant for revenue collected, who is in turn accountable to Supplier.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Vendor_PointOfSales_TreeNode = TreeNode(
    node_for=[Vendor],
    children="PointOfSales",
    label="=PointOfSales",
    tooltip="All points of sale this Vendor controls.",
    add=[PointOfSale],
    move=[PointOfSale],
    icon_path=IMAGE_PATH)
Vendor_BankStatements_TreeNode = TreeNode(
    node_for=[Vendor],
    children="BankStatements",
    label="=BankStatements",
    tooltip="All BankStatements reflecting deposits made by this Vendor.",
    add=[BankStatement],
    move=[BankStatement],
    icon_path=IMAGE_PATH)
Vendor_Cashiers_TreeNode = TreeNode(
    node_for=[Vendor],
    children="Cashiers",
    label="=Cashiers",
    tooltip="All Cachiers managed by this Vendor.",
    add=[Cashier],
    move=[Cashier],
    icon_path=IMAGE_PATH)
Vendor_VendorShifts_TreeNode = TreeNode(
    node_for=[Vendor],
    children="VendorShifts",
    label="=VendorShifts",
    tooltip="All vendor shifts opened and owned by this vendor.",
    add=[VendorShift],
    move=[VendorShift],
    icon_path=IMAGE_PATH)

Cheque_TreeNode = TreeNode(
    node_for=[Cheque],
        tooltip="The actual tender when it is a type of cheque.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SDPLocation_TreeNode = TreeNode(
    node_for=[SDPLocation],
    label="name",
    tooltip="Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the Service Agreement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SDPLocation_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[SDPLocation],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points at this location.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)

DeviceFunction_TreeNode = TreeNode(
    node_for=[DeviceFunction],
    label="name",
    tooltip="Function performed by a device such as a meter, communication equipment, controllers, etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DeviceFunction_Registers_TreeNode = TreeNode(
    node_for=[DeviceFunction],
    children="Registers",
    label="=Registers",
    tooltip="All registers for quantities metered by this device function.",
    add=[Register],
    move=[Register],
    icon_path=IMAGE_PATH)
DeviceFunction_EndDeviceEvents_TreeNode = TreeNode(
    node_for=[DeviceFunction],
    children="EndDeviceEvents",
    label="=EndDeviceEvents",
    tooltip="All events reported by this device function.",
    add=[EndDeviceEvent],
    move=[EndDeviceEvent],
    icon_path=IMAGE_PATH)

ComFunction_TreeNode = TreeNode(
    node_for=[ComFunction],
    label="name",
    tooltip="Communication function of communication equipment or a device such as a meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IntervalReading_TreeNode = TreeNode(
    node_for=[IntervalReading],
    label="name",
    tooltip="Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IntervalReading_IntervalBlocks_TreeNode = TreeNode(
    node_for=[IntervalReading],
    children="IntervalBlocks",
    label="=IntervalBlocks",
    tooltip="All blocks containing this interval reading.",
    add=[IntervalBlock],
    move=[IntervalBlock],
    icon_path=IMAGE_PATH)
IntervalReading_ReadingQualities_TreeNode = TreeNode(
    node_for=[IntervalReading],
    children="ReadingQualities",
    label="=ReadingQualities",
    tooltip="Used only if quality of this interval reading value is different than 'Good'.",
    add=[ReadingQuality],
    move=[ReadingQuality],
    icon_path=IMAGE_PATH)

ReadingType_TreeNode = TreeNode(
    node_for=[ReadingType],
    label="name",
    tooltip="Type of data conveyed by a specific Reading.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReadingType_Readings_TreeNode = TreeNode(
    node_for=[ReadingType],
    children="Readings",
    label="=Readings",
    tooltip="All reading values with this type information.",
    add=[Reading],
    move=[Reading],
    icon_path=IMAGE_PATH)
ReadingType_IntervalBlocks_TreeNode = TreeNode(
    node_for=[ReadingType],
    children="IntervalBlocks",
    label="=IntervalBlocks",
    tooltip="All blocks containing interval reading values with this type information.",
    add=[IntervalBlock],
    move=[IntervalBlock],
    icon_path=IMAGE_PATH)

EndDeviceAsset_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    label="name",
    tooltip="AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EndDeviceAsset_EndDeviceGroups_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    children="EndDeviceGroups",
    label="=EndDeviceGroups",
    tooltip="All end device groups referring to this end device asset.",
    add=[EndDeviceGroup],
    move=[EndDeviceGroup],
    icon_path=IMAGE_PATH)
EndDeviceAsset_EndDeviceControls_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    children="EndDeviceControls",
    label="=EndDeviceControls",
    tooltip="All end device controls sending commands to this end device asset.",
    add=[EndDeviceControl],
    move=[EndDeviceControl],
    icon_path=IMAGE_PATH)
EndDeviceAsset_ElectricalInfos_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    children="ElectricalInfos",
    label="=ElectricalInfos",
    tooltip="All sets of electrical properties for this end device asset.",
    add=[ElectricalInfo],
    move=[ElectricalInfo],
    icon_path=IMAGE_PATH)
EndDeviceAsset_Readings_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    children="Readings",
    label="=Readings",
    tooltip="",
    add=[Reading],
    move=[Reading],
    icon_path=IMAGE_PATH)
EndDeviceAsset_DeviceFunctions_TreeNode = TreeNode(
    node_for=[EndDeviceAsset],
    children="DeviceFunctions",
    label="=DeviceFunctions",
    tooltip="All device functions this end device asset performs.",
    add=[DeviceFunction],
    move=[DeviceFunction],
    icon_path=IMAGE_PATH)

MeterAsset_TreeNode = TreeNode(
    node_for=[MeterAsset],
    label="name",
    tooltip="Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeterAsset_MeterReadings_TreeNode = TreeNode(
    node_for=[MeterAsset],
    children="MeterReadings",
    label="=MeterReadings",
    tooltip="All meter readings provided by this meter asset.",
    add=[MeterReading],
    move=[MeterReading],
    icon_path=IMAGE_PATH)
MeterAsset_VendingTransactions_TreeNode = TreeNode(
    node_for=[MeterAsset],
    children="VendingTransactions",
    label="=VendingTransactions",
    tooltip="All vending transactions on this meter asset.",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)
MeterAsset_MeterServiceWorks_TreeNode = TreeNode(
    node_for=[MeterAsset],
    children="MeterServiceWorks",
    label="=MeterServiceWorks",
    tooltip="All non-replacement works on this meter asset.",
    add=[MeterServiceWork],
    move=[MeterServiceWork],
    icon_path=IMAGE_PATH)
MeterAsset_MeterReplacementWorks_TreeNode = TreeNode(
    node_for=[MeterAsset],
    children="MeterReplacementWorks",
    label="=MeterReplacementWorks",
    tooltip="All works on replacement of this old meter asset.",
    add=[MeterServiceWork],
    move=[MeterServiceWork],
    icon_path=IMAGE_PATH)

ElectricMeteringFunction_TreeNode = TreeNode(
    node_for=[ElectricMeteringFunction],
    label="name",
    tooltip="Functionality performed by an electric meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Reading_TreeNode = TreeNode(
    node_for=[Reading],
    label="name",
    tooltip="Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Reading_ReadingQualities_TreeNode = TreeNode(
    node_for=[Reading],
    children="ReadingQualities",
    label="=ReadingQualities",
    tooltip="Used only if quality of this reading value is different than 'Good'.",
    add=[ReadingQuality],
    move=[ReadingQuality],
    icon_path=IMAGE_PATH)
Reading_MeterReadings_TreeNode = TreeNode(
    node_for=[Reading],
    children="MeterReadings",
    label="=MeterReadings",
    tooltip="All meter readings (sets of values) containing this reading value.",
    add=[MeterReading],
    move=[MeterReading],
    icon_path=IMAGE_PATH)

Register_TreeNode = TreeNode(
    node_for=[Register],
    label="name",
    tooltip="Display for quantity that is metered on an end device such as a meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReadingQuality_TreeNode = TreeNode(
    node_for=[ReadingQuality],
        tooltip="Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not used unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeterServiceWork_TreeNode = TreeNode(
    node_for=[MeterServiceWork],
    label="name",
    tooltip="Work involving meters.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IntervalBlock_TreeNode = TreeNode(
    node_for=[IntervalBlock],
        tooltip="Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IntervalBlock_IntervalReadings_TreeNode = TreeNode(
    node_for=[IntervalBlock],
    children="IntervalReadings",
    label="=IntervalReadings",
    tooltip="Interval reading contained in this block.",
    add=[IntervalReading],
    move=[IntervalReading],
    icon_path=IMAGE_PATH)

MeterReading_TreeNode = TreeNode(
    node_for=[MeterReading],
    label="name",
    tooltip="Set of values obtained from the meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeterReading_IntervalBlocks_TreeNode = TreeNode(
    node_for=[MeterReading],
    children="IntervalBlocks",
    label="=IntervalBlocks",
    tooltip="All interval blocks contained in this meter reading.",
    add=[IntervalBlock],
    move=[IntervalBlock],
    icon_path=IMAGE_PATH)
MeterReading_Readings_TreeNode = TreeNode(
    node_for=[MeterReading],
    children="Readings",
    label="=Readings",
    tooltip="All reading values contained within this meter reading.",
    add=[Reading],
    move=[Reading],
    icon_path=IMAGE_PATH)
MeterReading_EndDeviceEvents_TreeNode = TreeNode(
    node_for=[MeterReading],
    children="EndDeviceEvents",
    label="=EndDeviceEvents",
    tooltip="All end device events associated with this set of measured values.",
    add=[EndDeviceEvent],
    move=[EndDeviceEvent],
    icon_path=IMAGE_PATH)

DemandResponseProgram_TreeNode = TreeNode(
    node_for=[DemandResponseProgram],
    label="name",
    tooltip="Demand response program.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DemandResponseProgram_EndDeviceGroups_TreeNode = TreeNode(
    node_for=[DemandResponseProgram],
    children="EndDeviceGroups",
    label="=EndDeviceGroups",
    tooltip="All groups of end devices with this demand response program.",
    add=[EndDeviceGroup],
    move=[EndDeviceGroup],
    icon_path=IMAGE_PATH)
DemandResponseProgram_CustomerAgreements_TreeNode = TreeNode(
    node_for=[DemandResponseProgram],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All customer agreements with this demand response program.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
DemandResponseProgram_EndDeviceControls_TreeNode = TreeNode(
    node_for=[DemandResponseProgram],
    children="EndDeviceControls",
    label="=EndDeviceControls",
    tooltip="All end device controls with this demand response program.",
    add=[EndDeviceControl],
    move=[EndDeviceControl],
    icon_path=IMAGE_PATH)

EndDeviceEvent_TreeNode = TreeNode(
    node_for=[EndDeviceEvent],
    label="name",
    tooltip="Event detected by a DeviceFunction associated with EndDeviceAsset.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EndDeviceControl_TreeNode = TreeNode(
    node_for=[EndDeviceControl],
    label="name",
    tooltip="Instructs an EndDeviceAsset (or EndDeviceGroup) to perform a specified action.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ServiceDeliveryPoint_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    label="name",
    tooltip="Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServiceDeliveryPoint_SDPLocations_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    children="SDPLocations",
    label="=SDPLocations",
    tooltip="All locations of this service delivery point.",
    add=[SDPLocation],
    move=[SDPLocation],
    icon_path=IMAGE_PATH)
ServiceDeliveryPoint_MeterReadings_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    children="MeterReadings",
    label="=MeterReadings",
    tooltip="All meter readings obtained from this service delivery point.",
    add=[MeterReading],
    move=[MeterReading],
    icon_path=IMAGE_PATH)
ServiceDeliveryPoint_PricingStructures_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    children="PricingStructures",
    label="=PricingStructures",
    tooltip="All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).",
    add=[PricingStructure],
    move=[PricingStructure],
    icon_path=IMAGE_PATH)
ServiceDeliveryPoint_PowerQualityPricings_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    children="PowerQualityPricings",
    label="=PowerQualityPricings",
    tooltip="",
    add=[PowerQualityPricing],
    move=[PowerQualityPricing],
    icon_path=IMAGE_PATH)
ServiceDeliveryPoint_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[ServiceDeliveryPoint],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets at this service delivery point.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)

EndDeviceGroup_TreeNode = TreeNode(
    node_for=[EndDeviceGroup],
    label="name",
    tooltip="Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EndDeviceGroup_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[EndDeviceGroup],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets this end device group refers to.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)
EndDeviceGroup_EndDeviceControls_TreeNode = TreeNode(
    node_for=[EndDeviceGroup],
    children="EndDeviceControls",
    label="=EndDeviceControls",
    tooltip="All end device controls sending commands to this end device group.",
    add=[EndDeviceControl],
    move=[EndDeviceControl],
    icon_path=IMAGE_PATH)

Pending_TreeNode = TreeNode(
    node_for=[Pending],
        tooltip="When present, a scalar conversion that is associated with IntervalBlock and which needs to be applied to every contained IntervalReading value. This conversion results in a new associated ReadingType, reflecting the true dimensions of interval reading values after the conversion.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Pending_IntervalBlocks_TreeNode = TreeNode(
    node_for=[Pending],
    children="IntervalBlocks",
    label="=IntervalBlocks",
    tooltip="All blocks of interval reading values to which this pending conversion applies.",
    add=[IntervalBlock],
    move=[IntervalBlock],
    icon_path=IMAGE_PATH)

Work_TreeNode = TreeNode(
    node_for=[Work],
    label="name",
    tooltip="Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Work_WorkFlowSteps_TreeNode = TreeNode(
    node_for=[Work],
    children="WorkFlowSteps",
    label="=WorkFlowSteps",
    tooltip="",
    add=[WorkFlowStep],
    move=[WorkFlowStep],
    icon_path=IMAGE_PATH)
Work_Customers_TreeNode = TreeNode(
    node_for=[Work],
    children="Customers",
    label="=Customers",
    tooltip="All the customers for which this work is performed.",
    add=[Customer],
    move=[Customer],
    icon_path=IMAGE_PATH)
Work_WorkTasks_TreeNode = TreeNode(
    node_for=[Work],
    children="WorkTasks",
    label="=WorkTasks",
    tooltip="",
    add=[WorkTask],
    move=[WorkTask],
    icon_path=IMAGE_PATH)
Work_Designs_TreeNode = TreeNode(
    node_for=[Work],
    children="Designs",
    label="=Designs",
    tooltip="",
    add=[Design],
    move=[Design],
    icon_path=IMAGE_PATH)
Work_WorkCostDetails_TreeNode = TreeNode(
    node_for=[Work],
    children="WorkCostDetails",
    label="=WorkCostDetails",
    tooltip="",
    add=[WorkCostDetail],
    move=[WorkCostDetail],
    icon_path=IMAGE_PATH)

ServiceCategory_TreeNode = TreeNode(
    node_for=[ServiceCategory],
    label="name",
    tooltip="Category of service provided to the customer.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServiceCategory_CustomerAgreements_TreeNode = TreeNode(
    node_for=[ServiceCategory],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
ServiceCategory_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[ServiceCategory],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points that deliver this category of service.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)
ServiceCategory_SPAccountingFunctions_TreeNode = TreeNode(
    node_for=[ServiceCategory],
    children="SPAccountingFunctions",
    label="=SPAccountingFunctions",
    tooltip="",
    add=[SDPAccountingFunction],
    move=[SDPAccountingFunction],
    icon_path=IMAGE_PATH)
ServiceCategory_PricingStructures_TreeNode = TreeNode(
    node_for=[ServiceCategory],
    children="PricingStructures",
    label="=PricingStructures",
    tooltip="All pricing structures applicable to this service category.",
    add=[PricingStructure],
    move=[PricingStructure],
    icon_path=IMAGE_PATH)

CustomerAccount_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    label="name",
    tooltip="Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CustomerAccount_WorkBillingInfos_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    children="WorkBillingInfos",
    label="=WorkBillingInfos",
    tooltip="",
    add=[WorkBillingInfo],
    move=[WorkBillingInfo],
    icon_path=IMAGE_PATH)
CustomerAccount_PaymentTransactions_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    children="PaymentTransactions",
    label="=PaymentTransactions",
    tooltip="All payment transactions for this customer account.",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)
CustomerAccount_CustomerAgreements_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All agreements for this customer account.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
CustomerAccount_CustomerBillingInfos_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    children="CustomerBillingInfos",
    label="=CustomerBillingInfos",
    tooltip="",
    add=[CustomerBillingInfo],
    move=[CustomerBillingInfo],
    icon_path=IMAGE_PATH)
CustomerAccount_ErpInvoicees_TreeNode = TreeNode(
    node_for=[CustomerAccount],
    children="ErpInvoicees",
    label="=ErpInvoicees",
    tooltip="",
    add=[ErpInvoice],
    move=[ErpInvoice],
    icon_path=IMAGE_PATH)

Tariff_TreeNode = TreeNode(
    node_for=[Tariff],
    label="name",
    tooltip="Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For Rate Schedules it is frequently allocated by the affiliated Public Utilities Commission.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Tariff_PricingStructures_TreeNode = TreeNode(
    node_for=[Tariff],
    children="PricingStructures",
    label="=PricingStructures",
    tooltip="All pricing structures using this tariff.",
    add=[PricingStructure],
    move=[PricingStructure],
    icon_path=IMAGE_PATH)
Tariff_TariffProfiles_TreeNode = TreeNode(
    node_for=[Tariff],
    children="TariffProfiles",
    label="=TariffProfiles",
    tooltip="All tariff profiles using this tariff.",
    add=[TariffProfile],
    move=[TariffProfile],
    icon_path=IMAGE_PATH)

PricingStructure_TreeNode = TreeNode(
    node_for=[PricingStructure],
    label="name",
    tooltip="Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PricingStructure_Tariffs_TreeNode = TreeNode(
    node_for=[PricingStructure],
    children="Tariffs",
    label="=Tariffs",
    tooltip="All tariffs used by this pricing structure.",
    add=[Tariff],
    move=[Tariff],
    icon_path=IMAGE_PATH)
PricingStructure_PowerQualityPricings_TreeNode = TreeNode(
    node_for=[PricingStructure],
    children="PowerQualityPricings",
    label="=PowerQualityPricings",
    tooltip="",
    add=[PowerQualityPricing],
    move=[PowerQualityPricing],
    icon_path=IMAGE_PATH)
PricingStructure_Transactions_TreeNode = TreeNode(
    node_for=[PricingStructure],
    children="Transactions",
    label="=Transactions",
    tooltip="All transactions applying this pricing structure.",
    add=[Transaction],
    move=[Transaction],
    icon_path=IMAGE_PATH)
PricingStructure_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[PricingStructure],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)
PricingStructure_CustomerAgreements_TreeNode = TreeNode(
    node_for=[PricingStructure],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All customer agreements with this pricing structure.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)

Customer_TreeNode = TreeNode(
    node_for=[Customer],
    label="name",
    tooltip="Organisation receiving services from ServiceSupplier.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Customer_TroubleTickets_TreeNode = TreeNode(
    node_for=[Customer],
    children="TroubleTickets",
    label="=TroubleTickets",
    tooltip="",
    add=[TroubleTicket],
    move=[TroubleTicket],
    icon_path=IMAGE_PATH)
Customer_Works_TreeNode = TreeNode(
    node_for=[Customer],
    children="Works",
    label="=Works",
    tooltip="All the works performed for this customer.",
    add=[Work],
    move=[Work],
    icon_path=IMAGE_PATH)
Customer_OutageNotifications_TreeNode = TreeNode(
    node_for=[Customer],
    children="OutageNotifications",
    label="=OutageNotifications",
    tooltip="",
    add=[OutageNotification],
    move=[OutageNotification],
    icon_path=IMAGE_PATH)
Customer_ErpPersons_TreeNode = TreeNode(
    node_for=[Customer],
    children="ErpPersons",
    label="=ErpPersons",
    tooltip="",
    add=[ErpPerson],
    move=[ErpPerson],
    icon_path=IMAGE_PATH)
Customer_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[Customer],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets of this customer.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)
Customer_CustomerAgreements_TreeNode = TreeNode(
    node_for=[Customer],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All agreements of this customer.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)

CustomerAgreement_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    label="name",
    tooltip="Agreement between the Customer and the ServiceSupplier to pay for service at a specific ServiceLocation. It records certain billing information about the type of service provided at the ServiceLocation and is used during charge creation to determine the type of service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CustomerAgreement_ServiceLocations_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="ServiceLocations",
    label="=ServiceLocations",
    tooltip="All service locations regulated by this customer agreement.",
    add=[ServiceLocation],
    move=[ServiceLocation],
    icon_path=IMAGE_PATH)
CustomerAgreement_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points regulated by this customer agreement.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)
CustomerAgreement_MeterReadings_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="MeterReadings",
    label="=MeterReadings",
    tooltip="(could be deprecated in the future) All meter readings for this customer agreement.",
    add=[MeterReading],
    move=[MeterReading],
    icon_path=IMAGE_PATH)
CustomerAgreement_AuxiliaryAgreements_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="AuxiliaryAgreements",
    label="=AuxiliaryAgreements",
    tooltip="All (non-service related) auxiliary agreements that refer to this customer agreement.",
    add=[AuxiliaryAgreement],
    move=[AuxiliaryAgreement],
    icon_path=IMAGE_PATH)
CustomerAgreement_Equipments_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="Equipments",
    label="=Equipments",
    tooltip="",
    add=[Equipment],
    move=[Equipment],
    icon_path=IMAGE_PATH)
CustomerAgreement_EndDeviceControls_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="EndDeviceControls",
    label="=EndDeviceControls",
    tooltip="Could be deprecated in the future.",
    add=[EndDeviceControl],
    move=[EndDeviceControl],
    icon_path=IMAGE_PATH)
CustomerAgreement_PricingStructures_TreeNode = TreeNode(
    node_for=[CustomerAgreement],
    children="PricingStructures",
    label="=PricingStructures",
    tooltip="All pricing structures applicable to this customer agreement.",
    add=[PricingStructure],
    move=[PricingStructure],
    icon_path=IMAGE_PATH)

ServiceLocation_TreeNode = TreeNode(
    node_for=[ServiceLocation],
    label="name",
    tooltip="A customer ServiceLocation has one or more ServiceDeliveryPoint(s), which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the ServiceLocation is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the ServiceDeliveryPoint is used to define the actual conducting equipment that the EndDeviceAsset attaches to at the utility customer's ServiceLocation. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ServiceLocation_CustomerAgreements_TreeNode = TreeNode(
    node_for=[ServiceLocation],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="All customer agreements regulating this service location.",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
ServiceLocation_EndDeviceAssets_TreeNode = TreeNode(
    node_for=[ServiceLocation],
    children="EndDeviceAssets",
    label="=EndDeviceAssets",
    tooltip="All end device assets that measure the service delivered to this service location.",
    add=[EndDeviceAsset],
    move=[EndDeviceAsset],
    icon_path=IMAGE_PATH)
ServiceLocation_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[ServiceLocation],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="All service delivery points delivering service (of the same type) to this service location.",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)

PerLengthPhaseImpedance_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    label="name",
    tooltip="Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PerLengthPhaseImpedance_PhaseImpedanceData_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    children="PhaseImpedanceData",
    label="=PhaseImpedanceData",
    tooltip="All data that belong to this conductor phase impedance.",
    add=[PhaseImpedanceData],
    move=[PhaseImpedanceData],
    icon_path=IMAGE_PATH)
PerLengthPhaseImpedance_ConductorSegments_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this phase impedance.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)

DistributionTransformerWinding_TreeNode = TreeNode(
    node_for=[DistributionTransformerWinding],
    label="name",
    tooltip="Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DistributionTransformerWinding_FromWindingInsulations_TreeNode = TreeNode(
    node_for=[DistributionTransformerWinding],
    children="FromWindingInsulations",
    label="=FromWindingInsulations",
    tooltip="",
    add=[WindingInsulation],
    move=[WindingInsulation],
    icon_path=IMAGE_PATH)
DistributionTransformerWinding_ToWindingInsulations_TreeNode = TreeNode(
    node_for=[DistributionTransformerWinding],
    children="ToWindingInsulations",
    label="=ToWindingInsulations",
    tooltip="",
    add=[WindingInsulation],
    move=[WindingInsulation],
    icon_path=IMAGE_PATH)

WindingPiImpedance_TreeNode = TreeNode(
    node_for=[WindingPiImpedance],
    label="name",
    tooltip="Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WindingPiImpedance_Windings_TreeNode = TreeNode(
    node_for=[WindingPiImpedance],
    children="Windings",
    label="=Windings",
    tooltip="All windings having this Pi impedance.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)

DistributionTransformer_TreeNode = TreeNode(
    node_for=[DistributionTransformer],
    label="name",
    tooltip="An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DistributionTransformer_TransformerObservations_TreeNode = TreeNode(
    node_for=[DistributionTransformer],
    children="TransformerObservations",
    label="=TransformerObservations",
    tooltip="",
    add=[TransformerObservation],
    move=[TransformerObservation],
    icon_path=IMAGE_PATH)
DistributionTransformer_Windings_TreeNode = TreeNode(
    node_for=[DistributionTransformer],
    children="Windings",
    label="=Windings",
    tooltip="All windings of this transformer.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)

DistributionLineSegment_TreeNode = TreeNode(
    node_for=[DistributionLineSegment],
    label="name",
    tooltip="Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DistributionLineSegment_ConductorAssets_TreeNode = TreeNode(
    node_for=[DistributionLineSegment],
    children="ConductorAssets",
    label="=ConductorAssets",
    tooltip="",
    add=[ConductorAsset],
    move=[ConductorAsset],
    icon_path=IMAGE_PATH)

PerLengthSequenceImpedance_TreeNode = TreeNode(
    node_for=[PerLengthSequenceImpedance],
    label="name",
    tooltip="Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PerLengthSequenceImpedance_ConductorSegments_TreeNode = TreeNode(
    node_for=[PerLengthSequenceImpedance],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this sequence impedance.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)

TransformerBank_TreeNode = TreeNode(
    node_for=[TransformerBank],
    label="name",
    tooltip="An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerBank_Transformers_TreeNode = TreeNode(
    node_for=[TransformerBank],
    children="Transformers",
    label="=Transformers",
    tooltip="All transformers that belong to this bank.",
    add=[DistributionTransformer],
    move=[DistributionTransformer],
    icon_path=IMAGE_PATH)

DistributionTapChanger_TreeNode = TreeNode(
    node_for=[DistributionTapChanger],
    label="name",
    tooltip="Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PhaseImpedanceData_TreeNode = TreeNode(
    node_for=[PhaseImpedanceData],
        tooltip="Triplet of resistance, reactance, and susceptance matrix element values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConnectDisconnectFunction_TreeNode = TreeNode(
    node_for=[ConnectDisconnectFunction],
    label="name",
    tooltip="A function that will disconnect or reconnect the customer's load under defined conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectDisconnectFunction_Switches_TreeNode = TreeNode(
    node_for=[ConnectDisconnectFunction],
    children="Switches",
    label="=Switches",
    tooltip="",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)

RemoteConnectDisconnectInfo_TreeNode = TreeNode(
    node_for=[RemoteConnectDisconnectInfo],
        tooltip="Details of remote connect disconnect function.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IEC61970CIMVersion_TreeNode = TreeNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IdentifiedObject_TreeNode = TreeNode(
    node_for=[IdentifiedObject],
    label="name",
    tooltip="This is a root class to provide common naming attributes for all classes needing naming attributes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeographicalRegion_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    label="name",
    tooltip="A geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeographicalRegion_Regions_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    children="Regions",
    label="=Regions",
    tooltip="The association is used in the naming hierarchy.",
    add=[SubGeographicalRegion],
    move=[SubGeographicalRegion],
    icon_path=IMAGE_PATH)

PowerSystemResource_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    label="name",
    tooltip="A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerSystemResource_ChangeItems_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
PowerSystemResource_AssetRoles_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="AssetRoles",
    label="=AssetRoles",
    tooltip="",
    add=[AssetPsrRole],
    move=[AssetPsrRole],
    icon_path=IMAGE_PATH)
PowerSystemResource_SafetyDocuments_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="SafetyDocuments",
    label="=SafetyDocuments",
    tooltip="",
    add=[SafetyDocument],
    move=[SafetyDocument],
    icon_path=IMAGE_PATH)
PowerSystemResource_Measurements_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="Measurements",
    label="=Measurements",
    tooltip="The Measurements that are included in the naming hierarchy where the PSR is the containing object",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
PowerSystemResource_ErpOrganisationRoles_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="ErpOrganisationRoles",
    label="=ErpOrganisationRoles",
    tooltip="",
    add=[OrgPsrRole],
    move=[OrgPsrRole],
    icon_path=IMAGE_PATH)
PowerSystemResource_PsrLists_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="PsrLists",
    label="=PsrLists",
    tooltip="",
    add=[PsrList],
    move=[PsrList],
    icon_path=IMAGE_PATH)
PowerSystemResource_PSREvent_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="PSREvent",
    label="=PSREvent",
    tooltip="All events associated with this power system resource.",
    add=[PSREvent],
    move=[PSREvent],
    icon_path=IMAGE_PATH)
PowerSystemResource_OperatingShare_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="OperatingShare",
    label="=OperatingShare",
    tooltip="The linkage to any number of operating share objects.",
    add=[OperatingShare],
    move=[OperatingShare],
    icon_path=IMAGE_PATH)
PowerSystemResource_ScheduleSteps_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="ScheduleSteps",
    label="=ScheduleSteps",
    tooltip="",
    add=[SwitchingStep],
    move=[SwitchingStep],
    icon_path=IMAGE_PATH)
PowerSystemResource_DocumentRoles_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="DocumentRoles",
    label="=DocumentRoles",
    tooltip="",
    add=[DocPsrRole],
    move=[DocPsrRole],
    icon_path=IMAGE_PATH)
PowerSystemResource_ReportingGroup_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="ReportingGroup",
    label="=ReportingGroup",
    tooltip="Reporting groups to which this PSR belongs.",
    add=[ReportingGroup],
    move=[ReportingGroup],
    icon_path=IMAGE_PATH)
PowerSystemResource_CircuitSections_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="CircuitSections",
    label="=CircuitSections",
    tooltip="",
    add=[CircuitSection],
    move=[CircuitSection],
    icon_path=IMAGE_PATH)
PowerSystemResource_NetworkDataSets_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="NetworkDataSets",
    label="=NetworkDataSets",
    tooltip="",
    add=[NetworkDataSet],
    move=[NetworkDataSet],
    icon_path=IMAGE_PATH)

Equipment_TreeNode = TreeNode(
    node_for=[Equipment],
    label="name",
    tooltip="The parts of a power system that are physical devices, electronic or mechanical",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Equipment_ContingencyEquipment_TreeNode = TreeNode(
    node_for=[Equipment],
    children="ContingencyEquipment",
    label="=ContingencyEquipment",
    tooltip="The contingency element associated with the equipment.",
    add=[ContingencyEquipment],
    move=[ContingencyEquipment],
    icon_path=IMAGE_PATH)
Equipment_CustomerAgreements_TreeNode = TreeNode(
    node_for=[Equipment],
    children="CustomerAgreements",
    label="=CustomerAgreements",
    tooltip="",
    add=[CustomerAgreement],
    move=[CustomerAgreement],
    icon_path=IMAGE_PATH)
Equipment_OperationalLimitSet_TreeNode = TreeNode(
    node_for=[Equipment],
    children="OperationalLimitSet",
    label="=OperationalLimitSet",
    tooltip="The equipment limit sets associated with the equipment.",
    add=[OperationalLimitSet],
    move=[OperationalLimitSet],
    icon_path=IMAGE_PATH)

ConductingEquipment_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    label="name",
    tooltip="The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductingEquipment_Terminals_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="Terminals",
    label="=Terminals",
    tooltip="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)
ConductingEquipment_ClearanceTags_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="ClearanceTags",
    label="=ClearanceTags",
    tooltip="Conducting equipment may have multiple clearance tags for authorized field work",
    add=[ClearanceTag],
    move=[ClearanceTag],
    icon_path=IMAGE_PATH)
ConductingEquipment_OutageStepRoles_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="OutageStepRoles",
    label="=OutageStepRoles",
    tooltip="",
    add=[OutageStepPsrRole],
    move=[OutageStepPsrRole],
    icon_path=IMAGE_PATH)
ConductingEquipment_ElectricalAssets_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="ElectricalAssets",
    label="=ElectricalAssets",
    tooltip="",
    add=[ElectricalAsset],
    move=[ElectricalAsset],
    icon_path=IMAGE_PATH)
ConductingEquipment_ProtectionEquipments_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="ProtectionEquipments",
    label="=ProtectionEquipments",
    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.",
    add=[ProtectionEquipment],
    move=[ProtectionEquipment],
    icon_path=IMAGE_PATH)

Curve_TreeNode = TreeNode(
    node_for=[Curve],
    label="name",
    tooltip="Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Curve_CurveDatas_TreeNode = TreeNode(
    node_for=[Curve],
    children="CurveDatas",
    label="=CurveDatas",
    tooltip="The point data values that define a curve",
    add=[CurveData],
    move=[CurveData],
    icon_path=IMAGE_PATH)

ReportingSuperGroup_TreeNode = TreeNode(
    node_for=[ReportingSuperGroup],
    label="name",
    tooltip="A reporting super group, groups reporting groups for a higher level report.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReportingSuperGroup_ReportingGroup_TreeNode = TreeNode(
    node_for=[ReportingSuperGroup],
    children="ReportingGroup",
    label="=ReportingGroup",
    tooltip="Reporting groups that are grouped under this group group.",
    add=[ReportingGroup],
    move=[ReportingGroup],
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_TopologicalNode_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes which belong to this connectivity node container.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)
ConnectivityNodeContainer_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="Connectivity nodes contained by this container.",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

EquipmentContainer_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquipmentContainer_Equipments_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    children="Equipments",
    label="=Equipments",
    tooltip="The association is used in the naming hierarchy.",
    add=[Equipment],
    move=[Equipment],
    icon_path=IMAGE_PATH)

Substation_TreeNode = TreeNode(
    node_for=[Substation],
    label="name",
    tooltip="A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Substation_VoltageLevels_TreeNode = TreeNode(
    node_for=[Substation],
    children="VoltageLevels",
    label="=VoltageLevels",
    tooltip="The association is used in the naming hierarchy.",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)
Substation_Bays_TreeNode = TreeNode(
    node_for=[Substation],
    children="Bays",
    label="=Bays",
    tooltip="The association is used in the naming hierarchy.",
    add=[Bay],
    move=[Bay],
    icon_path=IMAGE_PATH)

BasicIntervalSchedule_TreeNode = TreeNode(
    node_for=[BasicIntervalSchedule],
    label="name",
    tooltip="Schedule of values at points in time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IrregularIntervalSchedule_TreeNode = TreeNode(
    node_for=[IrregularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IrregularIntervalSchedule_TimePoints_TreeNode = TreeNode(
    node_for=[IrregularIntervalSchedule],
    children="TimePoints",
    label="=TimePoints",
    tooltip="The point data values that define a curve",
    add=[IrregularTimePoint],
    move=[IrregularTimePoint],
    icon_path=IMAGE_PATH)

IrregularTimePoint_TreeNode = TreeNode(
    node_for=[IrregularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PsrList_TreeNode = TreeNode(
    node_for=[PsrList],
    label="name",
    tooltip="Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PsrList_PowerSystemResources_TreeNode = TreeNode(
    node_for=[PsrList],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

RegularIntervalSchedule_TreeNode = TreeNode(
    node_for=[RegularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegularIntervalSchedule_TimePoints_TreeNode = TreeNode(
    node_for=[RegularIntervalSchedule],
    children="TimePoints",
    label="=TimePoints",
    tooltip="The point data values that define a curve",
    add=[RegularTimePoint],
    move=[RegularTimePoint],
    icon_path=IMAGE_PATH)

RegularTimePoint_TreeNode = TreeNode(
    node_for=[RegularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperatingParticipant_TreeNode = TreeNode(
    node_for=[OperatingParticipant],
    label="name",
    tooltip="An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperatingParticipant_OperatingShare_TreeNode = TreeNode(
    node_for=[OperatingParticipant],
    children="OperatingShare",
    label="=OperatingShare",
    tooltip="The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.",
    add=[OperatingShare],
    move=[OperatingShare],
    icon_path=IMAGE_PATH)

Bay_TreeNode = TreeNode(
    node_for=[Bay],
    label="name",
    tooltip="A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ModelingAuthority_TreeNode = TreeNode(
    node_for=[ModelingAuthority],
    label="name",
    tooltip="A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ModelingAuthority_ModelingAuthoritySets_TreeNode = TreeNode(
    node_for=[ModelingAuthority],
    children="ModelingAuthoritySets",
    label="=ModelingAuthoritySets",
    tooltip="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.",
    add=[ModelingAuthoritySet],
    move=[ModelingAuthoritySet],
    icon_path=IMAGE_PATH)

VoltageLevel_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VoltageLevel_Bays_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    children="Bays",
    label="=Bays",
    tooltip="The association is used in the naming hierarchy.",
    add=[Bay],
    move=[Bay],
    icon_path=IMAGE_PATH)

Terminal_TreeNode = TreeNode(
    node_for=[Terminal],
    label="name",
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Terminal_HasSecond_MutualCoupling_TreeNode = TreeNode(
    node_for=[Terminal],
    children="HasSecond_MutualCoupling",
    label="=HasSecond_MutualCoupling",
    tooltip="Mutual couplings with the branch associated as the first branch.",
    add=[MutualCoupling],
    move=[MutualCoupling],
    icon_path=IMAGE_PATH)
Terminal_OperationalLimitSet_TreeNode = TreeNode(
    node_for=[Terminal],
    children="OperationalLimitSet",
    label="=OperationalLimitSet",
    tooltip="The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.",
    add=[OperationalLimitSet],
    move=[OperationalLimitSet],
    icon_path=IMAGE_PATH)
Terminal_HasFirst_MutualCoupling_TreeNode = TreeNode(
    node_for=[Terminal],
    children="HasFirst_MutualCoupling",
    label="=HasFirst_MutualCoupling",
    tooltip="Mutual couplings associated with the branch as the first branch.",
    add=[MutualCoupling],
    move=[MutualCoupling],
    icon_path=IMAGE_PATH)
Terminal_TieFlow_TreeNode = TreeNode(
    node_for=[Terminal],
    children="TieFlow",
    label="=TieFlow",
    tooltip="The control area tie flows to which this terminal associates.",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)
Terminal_Measurements_TreeNode = TreeNode(
    node_for=[Terminal],
    children="Measurements",
    label="=Measurements",
    tooltip="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)
Terminal_RegulatingControl_TreeNode = TreeNode(
    node_for=[Terminal],
    children="RegulatingControl",
    label="=RegulatingControl",
    tooltip="The terminal is regulated by a control.",
    add=[RegulatingControl],
    move=[RegulatingControl],
    icon_path=IMAGE_PATH)
Terminal_TerminalConstraints_TreeNode = TreeNode(
    node_for=[Terminal],
    children="TerminalConstraints",
    label="=TerminalConstraints",
    tooltip="",
    add=[TerminalConstraintTerm],
    move=[TerminalConstraintTerm],
    icon_path=IMAGE_PATH)
Terminal_BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[Terminal],
    children="BranchGroupTerminal",
    label="=BranchGroupTerminal",
    tooltip="The directed branch group terminals for which the terminal is monitored.",
    add=[BranchGroupTerminal],
    move=[BranchGroupTerminal],
    icon_path=IMAGE_PATH)

Unit_TreeNode = TreeNode(
    node_for=[Unit],
    label="name",
    tooltip="Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Unit_Controls_TreeNode = TreeNode(
    node_for=[Unit],
    children="Controls",
    label="=Controls",
    tooltip="The Controls having the Unit.",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)
Unit_ProtectionEquipments_TreeNode = TreeNode(
    node_for=[Unit],
    children="ProtectionEquipments",
    label="=ProtectionEquipments",
    tooltip="The Protection Equipments having the Unit.",
    add=[ProtectionEquipment],
    move=[ProtectionEquipment],
    icon_path=IMAGE_PATH)
Unit_Measurements_TreeNode = TreeNode(
    node_for=[Unit],
    children="Measurements",
    label="=Measurements",
    tooltip="The Measurements having the Unit",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

CurveData_TreeNode = TreeNode(
    node_for=[CurveData],
        tooltip="Data point values for defining a curve or schedule",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperatingShare_TreeNode = TreeNode(
    node_for=[OperatingShare],
        tooltip="Specifies the contract relationship between a PowerSystemResource and a contract participant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReportingGroup_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    label="name",
    tooltip="A reporting group is used for various ad-hoc groupings used for reporting.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReportingGroup_TopologicalNode_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes that belong to the reporting group.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)
ReportingGroup_BusNameMarker_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="BusNameMarker",
    label="=BusNameMarker",
    tooltip="The BusNameMarkers that belong to this reporting group.",
    add=[BusNameMarker],
    move=[BusNameMarker],
    icon_path=IMAGE_PATH)
ReportingGroup_PowerSystemResource_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="PowerSystemResource",
    label="=PowerSystemResource",
    tooltip="PSR's which belong to this reporting group.",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

PSRType_TreeNode = TreeNode(
    node_for=[PSRType],
    label="name",
    tooltip="Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PSRType_PowerSystemResources_TreeNode = TreeNode(
    node_for=[PSRType],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="Power system resources classified with this PSRType.",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

SubGeographicalRegion_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    label="name",
    tooltip="A subset of a geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubGeographicalRegion_Substations_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Substations",
    label="=Substations",
    tooltip="The association is used in the naming hierarchy.",
    add=[Substation],
    move=[Substation],
    icon_path=IMAGE_PATH)
SubGeographicalRegion_Lines_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Lines",
    label="=Lines",
    tooltip="A Line can be contained by a SubGeographical Region.",
    add=[Line],
    move=[Line],
    icon_path=IMAGE_PATH)

BaseVoltage_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    label="name",
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BaseVoltage_VoltageLevel_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="VoltageLevel",
    label="=VoltageLevel",
    tooltip="The VoltageLevels having this BaseVoltage.",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)
BaseVoltage_ConductingEquipment_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="ConductingEquipment",
    label="=ConductingEquipment",
    tooltip="Use association to ConductingEquipment only when there is no VoltageLevel container used.",
    add=[ConductingEquipment],
    move=[ConductingEquipment],
    icon_path=IMAGE_PATH)
BaseVoltage_TopologicalNode_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes at the base voltage.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

BasePower_TreeNode = TreeNode(
    node_for=[BasePower],
    label="name",
    tooltip="The BasePower class defines the base power used in the per unit calculations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ModelingAuthoritySet_TreeNode = TreeNode(
    node_for=[ModelingAuthoritySet],
    label="name",
    tooltip="A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ModelingAuthoritySet_IdentifiedObjects_TreeNode = TreeNode(
    node_for=[ModelingAuthoritySet],
    children="IdentifiedObjects",
    label="=IdentifiedObjects",
    tooltip="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.",
    add=[IdentifiedObject],
    move=[IdentifiedObject],
    icon_path=IMAGE_PATH)

Switch_TreeNode = TreeNode(
    node_for=[Switch],
    label="name",
    tooltip="A generic device designed to close, or open, or both, one or more electric circuits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Switch_LoadMgmtFunctions_TreeNode = TreeNode(
    node_for=[Switch],
    children="LoadMgmtFunctions",
    label="=LoadMgmtFunctions",
    tooltip="",
    add=[LoadMgmtFunction],
    move=[LoadMgmtFunction],
    icon_path=IMAGE_PATH)
Switch_SwitchSchedules_TreeNode = TreeNode(
    node_for=[Switch],
    children="SwitchSchedules",
    label="=SwitchSchedules",
    tooltip="A Switch can be associated with SwitchSchedules.",
    add=[SwitchSchedule],
    move=[SwitchSchedule],
    icon_path=IMAGE_PATH)
Switch_ConnectDisconnectFunctions_TreeNode = TreeNode(
    node_for=[Switch],
    children="ConnectDisconnectFunctions",
    label="=ConnectDisconnectFunctions",
    tooltip="",
    add=[ConnectDisconnectFunction],
    move=[ConnectDisconnectFunction],
    icon_path=IMAGE_PATH)
Switch_SwitchingOperations_TreeNode = TreeNode(
    node_for=[Switch],
    children="SwitchingOperations",
    label="=SwitchingOperations",
    tooltip="A switch may be operated by many schedules.",
    add=[SwitchingOperation],
    move=[SwitchingOperation],
    icon_path=IMAGE_PATH)

Fuse_TreeNode = TreeNode(
    node_for=[Fuse],
    label="name",
    tooltip="An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatExchanger_TreeNode = TreeNode(
    node_for=[HeatExchanger],
    label="name",
    tooltip="Equipment for the cooling of electrical equipment and the extraction of heat",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapChanger_TreeNode = TreeNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TapChanger_TapSchedules_TreeNode = TreeNode(
    node_for=[TapChanger],
    children="TapSchedules",
    label="=TapSchedules",
    tooltip="A TapChanger can have TapSchedules.",
    add=[TapSchedule],
    move=[TapSchedule],
    icon_path=IMAGE_PATH)

PhaseTapChanger_TreeNode = TreeNode(
    node_for=[PhaseTapChanger],
    label="name",
    tooltip="A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulatingControl_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    label="name",
    tooltip="Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulatingControl_RegulationSchedule_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="RegulationSchedule",
    label="=RegulationSchedule",
    tooltip="Schedule for this Regulating regulating control.",
    add=[RegulationSchedule],
    move=[RegulationSchedule],
    icon_path=IMAGE_PATH)
RegulatingControl_TapChanger_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="TapChanger",
    label="=TapChanger",
    tooltip="copy from reg conduting eq",
    add=[TapChanger],
    move=[TapChanger],
    icon_path=IMAGE_PATH)
RegulatingControl_RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="RegulatingCondEq",
    label="=RegulatingCondEq",
    tooltip="The equipment that participates in this regulating control scheme.",
    add=[RegulatingCondEq],
    move=[RegulatingCondEq],
    icon_path=IMAGE_PATH)

TapSchedule_TreeNode = TreeNode(
    node_for=[TapSchedule],
    label="name",
    tooltip="A pre-established pattern over time for a tap step.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergyConsumer_TreeNode = TreeNode(
    node_for=[EnergyConsumer],
    label="name",
    tooltip="Generic user of energy - a  point of consumption on the power system model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EnergyConsumer_ServiceDeliveryPoints_TreeNode = TreeNode(
    node_for=[EnergyConsumer],
    children="ServiceDeliveryPoints",
    label="=ServiceDeliveryPoints",
    tooltip="",
    add=[ServiceDeliveryPoint],
    move=[ServiceDeliveryPoint],
    icon_path=IMAGE_PATH)

EnergySource_TreeNode = TreeNode(
    node_for=[EnergySource],
    label="name",
    tooltip="A generic equivalent for an energy supplier on a transmission or distribution voltage level.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SwitchSchedule_TreeNode = TreeNode(
    node_for=[SwitchSchedule],
    label="name",
    tooltip="A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Line_TreeNode = TreeNode(
    node_for=[Line],
    label="name",
    tooltip="A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Line_Flowgates_TreeNode = TreeNode(
    node_for=[Line],
    children="Flowgates",
    label="=Flowgates",
    tooltip="",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)

RatioVariationCurve_TreeNode = TreeNode(
    node_for=[RatioVariationCurve],
    label="name",
    tooltip="A Ratio Variation Curve describes the change in tap ratio in relationship to tap step changes.  The tap step is represented using the xValue and the ratio using y1value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReactiveCapabilityCurve_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    label="name",
    tooltip="Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReactiveCapabilityCurve_SynchronousMachines_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    children="SynchronousMachines",
    label="=SynchronousMachines",
    tooltip="Synchronous machines using this curve.",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)
ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachines_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    children="InitiallyUsedBySynchronousMachines",
    label="=InitiallyUsedBySynchronousMachines",
    tooltip="Synchronous machines using this curve as default.",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

Connector_TreeNode = TreeNode(
    node_for=[Connector],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Resistor_TreeNode = TreeNode(
    node_for=[Resistor],
    label="name",
    tooltip="Resistor, typically used in filter configurations or as earthing resistor for transformers.  Used for electrical model of distribution networks.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectedSwitch_TreeNode = TreeNode(
    node_for=[ProtectedSwitch],
    label="name",
    tooltip="A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectedSwitch_RecloseSequences_TreeNode = TreeNode(
    node_for=[ProtectedSwitch],
    children="RecloseSequences",
    label="=RecloseSequences",
    tooltip="A breaker may have zero or more automatic reclosures after a trip occurs.",
    add=[RecloseSequence],
    move=[RecloseSequence],
    icon_path=IMAGE_PATH)

Disconnector_TreeNode = TreeNode(
    node_for=[Disconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Breaker_TreeNode = TreeNode(
    node_for=[Breaker],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Jumper_TreeNode = TreeNode(
    node_for=[Jumper],
    label="name",
    tooltip="A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SeriesCompensator_TreeNode = TreeNode(
    node_for=[SeriesCompensator],
    label="name",
    tooltip="A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindingTest_TreeNode = TreeNode(
    node_for=[WindingTest],
    label="name",
    tooltip="Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Conductor_TreeNode = TreeNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ACLineSegment_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PowerTransformer_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    label="name",
    tooltip="An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerTransformer_TransformerWindings_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    children="TransformerWindings",
    label="=TransformerWindings",
    tooltip="A transformer has windings",
    add=[TransformerWinding],
    move=[TransformerWinding],
    icon_path=IMAGE_PATH)
PowerTransformer_Flowgates_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    children="Flowgates",
    label="=Flowgates",
    tooltip="",
    add=[Flowgate],
    move=[Flowgate],
    icon_path=IMAGE_PATH)

MutualCoupling_TreeNode = TreeNode(
    node_for=[MutualCoupling],
    label="name",
    tooltip="This class represents the zero sequence line mutual coupling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Ground_TreeNode = TreeNode(
    node_for=[Ground],
    label="name",
    tooltip="A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Ground_WindingInsulations_TreeNode = TreeNode(
    node_for=[Ground],
    children="WindingInsulations",
    label="=WindingInsulations",
    tooltip="",
    add=[WindingInsulation],
    move=[WindingInsulation],
    icon_path=IMAGE_PATH)

ImpedanceVariationCurve_TreeNode = TreeNode(
    node_for=[ImpedanceVariationCurve],
    label="name",
    tooltip="An Impedance Variation Curve describes the change in Transformer Winding impedance values in relationship to tap step changes.  The tap step is represented using the xValue, resistance using y1value, reactance using y2value, and magnetizing susceptance using y3value.  The resistance (r), reactance (x), and magnetizing susceptance (b) of the associated TransformerWinding define the impedance when the tap is at neutral step.  The curve values represent the change to the impedance from the neutral step values.  The impedance at a non-neutral step is calculated by adding the neutral step impedance (from the TransformerWinding) to the delta value from the curve.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Plant_TreeNode = TreeNode(
    node_for=[Plant],
    label="name",
    tooltip="A Plant is a collection of equipment for purposes of generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusbarSection_TreeNode = TreeNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingCondEq],
    label="name",
    tooltip="RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulatingCondEq_Controls_TreeNode = TreeNode(
    node_for=[RegulatingCondEq],
    children="Controls",
    label="=Controls",
    tooltip="The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)

ShuntCompensator_TreeNode = TreeNode(
    node_for=[ShuntCompensator],
    label="name",
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SynchronousMachine_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SynchronousMachine_ReactiveCapabilityCurves_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    children="ReactiveCapabilityCurves",
    label="=ReactiveCapabilityCurves",
    tooltip="All available Reactive capability curves for this SynchronousMachine.",
    add=[ReactiveCapabilityCurve],
    move=[ReactiveCapabilityCurve],
    icon_path=IMAGE_PATH)
SynchronousMachine_PrimeMovers_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    children="PrimeMovers",
    label="=PrimeMovers",
    tooltip="Prime movers that drive this SynchronousMachine.",
    add=[PrimeMover],
    move=[PrimeMover],
    icon_path=IMAGE_PATH)

PhaseVariationCurve_TreeNode = TreeNode(
    node_for=[PhaseVariationCurve],
    label="name",
    tooltip="A Ratio Variation Curve describes the change in tap ratio in relationship to tap step changes.  The tap step is represented using the xValue and the ratio using y1value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FrequencyConverter_TreeNode = TreeNode(
    node_for=[FrequencyConverter],
    label="name",
    tooltip="A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerWinding_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    label="name",
    tooltip="A winding is associated with each defined terminal of a transformer (or phase shifter).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerWinding_To_WindingTest_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    children="To_WindingTest",
    label="=To_WindingTest",
    tooltip="The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.",
    add=[WindingTest],
    move=[WindingTest],
    icon_path=IMAGE_PATH)
TransformerWinding_From_WindingTest_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    children="From_WindingTest",
    label="=From_WindingTest",
    tooltip="The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.",
    add=[WindingTest],
    move=[WindingTest],
    icon_path=IMAGE_PATH)

Junction_TreeNode = TreeNode(
    node_for=[Junction],
    label="name",
    tooltip="A point where one or more conducting equipments are connected with zero resistance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DCLineSegment_TreeNode = TreeNode(
    node_for=[DCLineSegment],
    label="name",
    tooltip="A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RatioTapChanger_TreeNode = TreeNode(
    node_for=[RatioTapChanger],
    label="name",
    tooltip="A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CompositeSwitch_TreeNode = TreeNode(
    node_for=[CompositeSwitch],
    label="name",
    tooltip="A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompositeSwitch_Switches_TreeNode = TreeNode(
    node_for=[CompositeSwitch],
    children="Switches",
    label="=Switches",
    tooltip="Switches contained in this Composite switch.",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)

VoltageControlZone_TreeNode = TreeNode(
    node_for=[VoltageControlZone],
    label="name",
    tooltip="An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RectifierInverter_TreeNode = TreeNode(
    node_for=[RectifierInverter],
    label="name",
    tooltip="Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StaticVarCompensator_TreeNode = TreeNode(
    node_for=[StaticVarCompensator],
    label="name",
    tooltip="A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadBreakSwitch_TreeNode = TreeNode(
    node_for=[LoadBreakSwitch],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulationSchedule_TreeNode = TreeNode(
    node_for=[RegulationSchedule],
    label="name",
    tooltip="A pre-established pattern over time for a controlled variable, e.g., busbar voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulationSchedule_VoltageControlZones_TreeNode = TreeNode(
    node_for=[RegulationSchedule],
    children="VoltageControlZones",
    label="=VoltageControlZones",
    tooltip="A VoltageControlZone may have a  voltage regulation schedule.",
    add=[VoltageControlZone],
    move=[VoltageControlZone],
    icon_path=IMAGE_PATH)

GroundDisconnector_TreeNode = TreeNode(
    node_for=[GroundDisconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimit],
    label="name",
    tooltip="A value associated with a specific kind of limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VoltageLimit_TreeNode = TreeNode(
    node_for=[VoltageLimit],
    label="name",
    tooltip="Operational limit applied to voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ApparentPowerLimit_TreeNode = TreeNode(
    node_for=[ApparentPowerLimit],
    label="name",
    tooltip="Apparent power limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BranchGroup_TreeNode = TreeNode(
    node_for=[BranchGroup],
    label="name",
    tooltip="A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BranchGroup_BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[BranchGroup],
    children="BranchGroupTerminal",
    label="=BranchGroupTerminal",
    tooltip="The directed branch group terminals to be summed.",
    add=[BranchGroupTerminal],
    move=[BranchGroupTerminal],
    icon_path=IMAGE_PATH)

ActivePowerLimit_TreeNode = TreeNode(
    node_for=[ActivePowerLimit],
    label="name",
    tooltip="Limit on active power flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[BranchGroupTerminal],
        tooltip="A specific directed terminal flow for a branch group.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimitSet_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    label="name",
    tooltip="A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitSet_OperationalLimitValue_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    children="OperationalLimitValue",
    label="=OperationalLimitValue",
    tooltip="Values of equipment limits.",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)

CurrentLimit_TreeNode = TreeNode(
    node_for=[CurrentLimit],
    label="name",
    tooltip="Operational limit on current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimitType_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
        tooltip="A type of limit.  The meaning of a specific limit is described in this class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitType_OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
    children="OperationalLimit",
    label="=OperationalLimit",
    tooltip="The operational limits associated with this type of limit.",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)

StateVariable_TreeNode = TreeNode(
    node_for=[StateVariable],
        tooltip="An abstract class for state variables.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvInjection_TreeNode = TreeNode(
    node_for=[SvInjection],
        tooltip="Injectixon state variable.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvPowerFlow_TreeNode = TreeNode(
    node_for=[SvPowerFlow],
        tooltip="State variable for power flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvStatus_TreeNode = TreeNode(
    node_for=[SvStatus],
        tooltip="State variable for status.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvVoltage_TreeNode = TreeNode(
    node_for=[SvVoltage],
        tooltip="State variable for voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvTapStep_TreeNode = TreeNode(
    node_for=[SvTapStep],
        tooltip="State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvShortCircuit_TreeNode = TreeNode(
    node_for=[SvShortCircuit],
        tooltip="State variable for short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvShuntCompensatorSections_TreeNode = TreeNode(
    node_for=[SvShuntCompensatorSections],
        tooltip="State variable for the number of sections in service for a shunt compensator.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LimitSet_TreeNode = TreeNode(
    node_for=[LimitSet],
    label="name",
    tooltip="Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AccumulatorLimitSet_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    label="name",
    tooltip="An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AccumulatorLimitSet_Measurements_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    children="Measurements",
    label="=Measurements",
    tooltip="The Measurements using the LimitSet.",
    add=[Accumulator],
    move=[Accumulator],
    icon_path=IMAGE_PATH)
AccumulatorLimitSet_Limits_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    children="Limits",
    label="=Limits",
    tooltip="The limit values used for supervision of Measurements.",
    add=[AccumulatorLimit],
    move=[AccumulatorLimit],
    icon_path=IMAGE_PATH)

AnalogLimitSet_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    label="name",
    tooltip="An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AnalogLimitSet_Limits_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    children="Limits",
    label="=Limits",
    tooltip="The limit values used for supervision of Measurements.",
    add=[AnalogLimit],
    move=[AnalogLimit],
    icon_path=IMAGE_PATH)
AnalogLimitSet_Measurements_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    children="Measurements",
    label="=Measurements",
    tooltip="The Measurements using the LimitSet.",
    add=[Analog],
    move=[Analog],
    icon_path=IMAGE_PATH)

MeasurementValue_TreeNode = TreeNode(
    node_for=[MeasurementValue],
    label="name",
    tooltip="The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeasurementValue_GmlValues_TreeNode = TreeNode(
    node_for=[MeasurementValue],
    children="GmlValues",
    label="=GmlValues",
    tooltip="",
    add=[GmlValue],
    move=[GmlValue],
    icon_path=IMAGE_PATH)
MeasurementValue_ProcedureDataSets_TreeNode = TreeNode(
    node_for=[MeasurementValue],
    children="ProcedureDataSets",
    label="=ProcedureDataSets",
    tooltip="",
    add=[ProcedureDataSet],
    move=[ProcedureDataSet],
    icon_path=IMAGE_PATH)

AccumulatorValue_TreeNode = TreeNode(
    node_for=[AccumulatorValue],
    label="name",
    tooltip="AccumulatorValue represents a accumulated (counted) MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ValueAliasSet_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    label="name",
    tooltip="Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ValueAliasSet_Discretes_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Discretes",
    label="=Discretes",
    tooltip="The Measurements using the set for translation",
    add=[Discrete],
    move=[Discrete],
    icon_path=IMAGE_PATH)
ValueAliasSet_Commands_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Commands",
    label="=Commands",
    tooltip="The ValueAliasSet used for translation of a Control value to a name.",
    add=[Command],
    move=[Command],
    icon_path=IMAGE_PATH)
ValueAliasSet_Values_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Values",
    label="=Values",
    tooltip="The ValueToAlias mappings included in the set",
    add=[ValueToAlias],
    move=[ValueToAlias],
    icon_path=IMAGE_PATH)

PotentialTransformer_TreeNode = TreeNode(
    node_for=[PotentialTransformer],
    label="name",
    tooltip="Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Limit_TreeNode = TreeNode(
    node_for=[Limit],
    label="name",
    tooltip="Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Limit_Procedures_TreeNode = TreeNode(
    node_for=[Limit],
    children="Procedures",
    label="=Procedures",
    tooltip="",
    add=[Procedure],
    move=[Procedure],
    icon_path=IMAGE_PATH)

AccumulatorLimit_TreeNode = TreeNode(
    node_for=[AccumulatorLimit],
    label="name",
    tooltip="Limit values for Accumulator measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Measurement_TreeNode = TreeNode(
    node_for=[Measurement],
    label="name",
    tooltip="A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Measurement_DynamicSchedules_TreeNode = TreeNode(
    node_for=[Measurement],
    children="DynamicSchedules",
    label="=DynamicSchedules",
    tooltip="A measurement is a data source for dynamic interchange schedules",
    add=[DynamicSchedule],
    move=[DynamicSchedule],
    icon_path=IMAGE_PATH)
Measurement_Documents_TreeNode = TreeNode(
    node_for=[Measurement],
    children="Documents",
    label="=Documents",
    tooltip="Measurements are specified in types of documents, such as procedures.",
    add=[Document],
    move=[Document],
    icon_path=IMAGE_PATH)
Measurement_Locations_TreeNode = TreeNode(
    node_for=[Measurement],
    children="Locations",
    label="=Locations",
    tooltip="",
    add=[Location],
    move=[Location],
    icon_path=IMAGE_PATH)
Measurement_ChangeItems_TreeNode = TreeNode(
    node_for=[Measurement],
    children="ChangeItems",
    label="=ChangeItems",
    tooltip="",
    add=[ChangeItem],
    move=[ChangeItem],
    icon_path=IMAGE_PATH)
Measurement_ViolationLimits_TreeNode = TreeNode(
    node_for=[Measurement],
    children="ViolationLimits",
    label="=ViolationLimits",
    tooltip="",
    add=[ViolationLimit],
    move=[ViolationLimit],
    icon_path=IMAGE_PATH)

Analog_TreeNode = TreeNode(
    node_for=[Analog],
    label="name",
    tooltip="Analog represents an analog Measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Analog_AnalogValues_TreeNode = TreeNode(
    node_for=[Analog],
    children="AnalogValues",
    label="=AnalogValues",
    tooltip="The values connected to this measurement.",
    add=[AnalogValue],
    move=[AnalogValue],
    icon_path=IMAGE_PATH)
Analog_LimitSets_TreeNode = TreeNode(
    node_for=[Analog],
    children="LimitSets",
    label="=LimitSets",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[AnalogLimitSet],
    move=[AnalogLimitSet],
    icon_path=IMAGE_PATH)

Control_TreeNode = TreeNode(
    node_for=[Control],
    label="name",
    tooltip="Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SetPoint_TreeNode = TreeNode(
    node_for=[SetPoint],
    label="name",
    tooltip="A SetPoint is an analog control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AnalogLimit_TreeNode = TreeNode(
    node_for=[AnalogLimit],
    label="name",
    tooltip="Limit values for Analog measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Discrete_TreeNode = TreeNode(
    node_for=[Discrete],
    label="name",
    tooltip="Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Discrete_DiscreteValues_TreeNode = TreeNode(
    node_for=[Discrete],
    children="DiscreteValues",
    label="=DiscreteValues",
    tooltip="The values connected to this measurement.",
    add=[DiscreteValue],
    move=[DiscreteValue],
    icon_path=IMAGE_PATH)

ValueToAlias_TreeNode = TreeNode(
    node_for=[ValueToAlias],
    label="name",
    tooltip="Describes the translation of one particular value into a name, e.g. 1->'Open'",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Quality61850_TreeNode = TreeNode(
    node_for=[Quality61850],
        tooltip="Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeasurementValueSource_TreeNode = TreeNode(
    node_for=[MeasurementValueSource],
    label="name",
    tooltip="MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeasurementValueSource_MeasurementValues_TreeNode = TreeNode(
    node_for=[MeasurementValueSource],
    children="MeasurementValues",
    label="=MeasurementValues",
    tooltip="The MeasurementValues updated by the source",
    add=[MeasurementValue],
    move=[MeasurementValue],
    icon_path=IMAGE_PATH)

Accumulator_TreeNode = TreeNode(
    node_for=[Accumulator],
    label="name",
    tooltip="Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Accumulator_AccumulatorValues_TreeNode = TreeNode(
    node_for=[Accumulator],
    children="AccumulatorValues",
    label="=AccumulatorValues",
    tooltip="The values connected to this measurement.",
    add=[AccumulatorValue],
    move=[AccumulatorValue],
    icon_path=IMAGE_PATH)
Accumulator_LimitSets_TreeNode = TreeNode(
    node_for=[Accumulator],
    children="LimitSets",
    label="=LimitSets",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[AccumulatorLimitSet],
    move=[AccumulatorLimitSet],
    icon_path=IMAGE_PATH)

CurrentTransformer_TreeNode = TreeNode(
    node_for=[CurrentTransformer],
    label="name",
    tooltip="Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StringMeasurementValue_TreeNode = TreeNode(
    node_for=[StringMeasurementValue],
    label="name",
    tooltip="StringMeasurementValue represents a measurement value of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ControlType_TreeNode = TreeNode(
    node_for=[ControlType],
    label="name",
    tooltip="Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlType_Controls_TreeNode = TreeNode(
    node_for=[ControlType],
    children="Controls",
    label="=Controls",
    tooltip="The Controls having the ControlType",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)

Command_TreeNode = TreeNode(
    node_for=[Command],
    label="name",
    tooltip="A Command is a discrete control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DiscreteValue_TreeNode = TreeNode(
    node_for=[DiscreteValue],
    label="name",
    tooltip="DiscreteValue represents a discrete MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeasurementValueQuality_TreeNode = TreeNode(
    node_for=[MeasurementValueQuality],
        tooltip="Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AnalogValue_TreeNode = TreeNode(
    node_for=[AnalogValue],
    label="name",
    tooltip="AnalogValue represents an analog MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AnalogValue_AltTieMeas_TreeNode = TreeNode(
    node_for=[AnalogValue],
    children="AltTieMeas",
    label="=AltTieMeas",
    tooltip="The usage of the measurement within the control area specification.",
    add=[AltTieMeas],
    move=[AltTieMeas],
    icon_path=IMAGE_PATH)
AnalogValue_AltGeneratingUnit_TreeNode = TreeNode(
    node_for=[AnalogValue],
    children="AltGeneratingUnit",
    label="=AltGeneratingUnit",
    tooltip="The alternate generating unit for which this measurement value applies.",
    add=[AltGeneratingUnitMeas],
    move=[AltGeneratingUnitMeas],
    icon_path=IMAGE_PATH)

StringMeasurement_TreeNode = TreeNode(
    node_for=[StringMeasurement],
    label="name",
    tooltip="StringMeasurement represents a measurement with values of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StringMeasurement_StringMeasurementValues_TreeNode = TreeNode(
    node_for=[StringMeasurement],
    children="StringMeasurementValues",
    label="=StringMeasurementValues",
    tooltip="The values connected to this measurement.",
    add=[StringMeasurementValue],
    move=[StringMeasurementValue],
    icon_path=IMAGE_PATH)

PenstockLossCurve_TreeNode = TreeNode(
    node_for=[PenstockLossCurve],
    label="name",
    tooltip="Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratingUnit_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="ControlArea specifications for this generating unit.",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)
GeneratingUnit_GenUnitOpCostCurves_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="GenUnitOpCostCurves",
    label="=GenUnitOpCostCurves",
    tooltip="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.",
    add=[GenUnitOpCostCurve],
    move=[GenUnitOpCostCurve],
    icon_path=IMAGE_PATH)
GeneratingUnit_SynchronousMachines_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="SynchronousMachines",
    label="=SynchronousMachines",
    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unit",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)
GeneratingUnit_GrossToNetActivePowerCurves_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="GrossToNetActivePowerCurves",
    label="=GrossToNetActivePowerCurves",
    tooltip="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit",
    add=[GrossToNetActivePowerCurve],
    move=[GrossToNetActivePowerCurve],
    icon_path=IMAGE_PATH)

ThermalGeneratingUnit_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ThermalGeneratingUnit_EmmissionAccounts_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="EmmissionAccounts",
    label="=EmmissionAccounts",
    tooltip="A thermal generating unit may have one or more emission allowance accounts",
    add=[EmissionAccount],
    move=[EmissionAccount],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_FuelAllocationSchedules_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="FuelAllocationSchedules",
    label="=FuelAllocationSchedules",
    tooltip="A thermal generating unit may have one or more fuel allocation schedules",
    add=[FuelAllocationSchedule],
    move=[FuelAllocationSchedule],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_EmissionCurves_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="EmissionCurves",
    label="=EmissionCurves",
    tooltip="A thermal generating unit may have  one or more emission curves",
    add=[EmissionCurve],
    move=[EmissionCurve],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_FossilFuels_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="FossilFuels",
    label="=FossilFuels",
    tooltip="A thermal generating unit may have one or more fossil fuels",
    add=[FossilFuel],
    move=[FossilFuel],
    icon_path=IMAGE_PATH)

IncrementalHeatRateCurve_TreeNode = TreeNode(
    node_for=[IncrementalHeatRateCurve],
    label="name",
    tooltip="Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatInputCurve_TreeNode = TreeNode(
    node_for=[HeatInputCurve],
    label="name",
    tooltip="Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Reservoir_TreeNode = TreeNode(
    node_for=[Reservoir],
    label="name",
    tooltip="A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Reservoir_InflowForecasts_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="InflowForecasts",
    label="=InflowForecasts",
    tooltip="A reservoir may have a 'natural' inflow forecast.",
    add=[InflowForecast],
    move=[InflowForecast],
    icon_path=IMAGE_PATH)
Reservoir_SpillsIntoReservoirs_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="SpillsIntoReservoirs",
    label="=SpillsIntoReservoirs",
    tooltip="A reservoir may spill into a downstream reservoir",
    add=[Reservoir],
    move=[Reservoir],
    icon_path=IMAGE_PATH)
Reservoir_UpstreamFromHydroPowerPlants_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="UpstreamFromHydroPowerPlants",
    label="=UpstreamFromHydroPowerPlants",
    tooltip="Generators are supplied water from or pumps discharge water to an upstream reservoir",
    add=[HydroPowerPlant],
    move=[HydroPowerPlant],
    icon_path=IMAGE_PATH)
Reservoir_LevelVsVolumeCurves_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="LevelVsVolumeCurves",
    label="=LevelVsVolumeCurves",
    tooltip="A reservoir may have a level versus volume relationship.",
    add=[LevelVsVolumeCurve],
    move=[LevelVsVolumeCurve],
    icon_path=IMAGE_PATH)
Reservoir_HydroPowerPlants_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="HydroPowerPlants",
    label="=HydroPowerPlants",
    tooltip="Generators discharge water to or pumps are supplied water from a downstream reservoir",
    add=[HydroPowerPlant],
    move=[HydroPowerPlant],
    icon_path=IMAGE_PATH)

GenUnitOpCostCurve_TreeNode = TreeNode(
    node_for=[GenUnitOpCostCurve],
    label="name",
    tooltip="Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindGeneratingUnit_TreeNode = TreeNode(
    node_for=[WindGeneratingUnit],
    label="name",
    tooltip="A wind driven generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartMainFuelCurve_TreeNode = TreeNode(
    node_for=[StartMainFuelCurve],
    label="name",
    tooltip="The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CogenerationPlant_TreeNode = TreeNode(
    node_for=[CogenerationPlant],
    label="name",
    tooltip="A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CogenerationPlant_ThermalGeneratingUnits_TreeNode = TreeNode(
    node_for=[CogenerationPlant],
    children="ThermalGeneratingUnits",
    label="=ThermalGeneratingUnits",
    tooltip="A thermal generating unit may be a member of a cogeneration plant",
    add=[ThermalGeneratingUnit],
    move=[ThermalGeneratingUnit],
    icon_path=IMAGE_PATH)

GrossToNetActivePowerCurve_TreeNode = TreeNode(
    node_for=[GrossToNetActivePowerCurve],
    label="name",
    tooltip="Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AirCompressor_TreeNode = TreeNode(
    node_for=[AirCompressor],
    label="name",
    tooltip="Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShutdownCurve_TreeNode = TreeNode(
    node_for=[ShutdownCurve],
    label="name",
    tooltip="Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FuelAllocationSchedule_TreeNode = TreeNode(
    node_for=[FuelAllocationSchedule],
    label="name",
    tooltip="The amount of fuel of a given type which is allocated for consumption over a specified period of time",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TailbayLossCurve_TreeNode = TreeNode(
    node_for=[TailbayLossCurve],
    label="name",
    tooltip="Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPumpOpSchedule_TreeNode = TreeNode(
    node_for=[HydroPumpOpSchedule],
    label="name",
    tooltip="The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FossilFuel_TreeNode = TreeNode(
    node_for=[FossilFuel],
    label="name",
    tooltip="The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FossilFuel_FuelAllocationSchedules_TreeNode = TreeNode(
    node_for=[FossilFuel],
    children="FuelAllocationSchedules",
    label="=FuelAllocationSchedules",
    tooltip="A fuel allocation schedule must have a fossil fuel",
    add=[FuelAllocationSchedule],
    move=[FuelAllocationSchedule],
    icon_path=IMAGE_PATH)

TargetLevelSchedule_TreeNode = TreeNode(
    node_for=[TargetLevelSchedule],
    label="name",
    tooltip="Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPump_TreeNode = TreeNode(
    node_for=[HydroPump],
    label="name",
    tooltip="A synchronous motor-driven pump, typically associated with a pumped storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPowerPlant_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    label="name",
    tooltip="A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HydroPowerPlant_HydroPumps_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    children="HydroPumps",
    label="=HydroPumps",
    tooltip="The hydro pump may be a member of a pumped storage plant or a pump for distributing water",
    add=[HydroPump],
    move=[HydroPump],
    icon_path=IMAGE_PATH)
HydroPowerPlant_HydroGeneratingUnits_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    children="HydroGeneratingUnits",
    label="=HydroGeneratingUnits",
    tooltip="The hydro generating unit belongs to a hydro power plant",
    add=[HydroGeneratingUnit],
    move=[HydroGeneratingUnit],
    icon_path=IMAGE_PATH)

InflowForecast_TreeNode = TreeNode(
    node_for=[InflowForecast],
    label="name",
    tooltip="Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CombinedCyclePlant_TreeNode = TreeNode(
    node_for=[CombinedCyclePlant],
    label="name",
    tooltip="A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CombinedCyclePlant_ThermalGeneratingUnits_TreeNode = TreeNode(
    node_for=[CombinedCyclePlant],
    children="ThermalGeneratingUnits",
    label="=ThermalGeneratingUnits",
    tooltip="A thermal generating unit may be a member of a combined cycle plant",
    add=[ThermalGeneratingUnit],
    move=[ThermalGeneratingUnit],
    icon_path=IMAGE_PATH)

HydroGeneratingEfficiencyCurve_TreeNode = TreeNode(
    node_for=[HydroGeneratingEfficiencyCurve],
    label="name",
    tooltip="Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NuclearGeneratingUnit_TreeNode = TreeNode(
    node_for=[NuclearGeneratingUnit],
    label="name",
    tooltip="A nuclear generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartIgnFuelCurve_TreeNode = TreeNode(
    node_for=[StartIgnFuelCurve],
    label="name",
    tooltip="The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CAESPlant_TreeNode = TreeNode(
    node_for=[CAESPlant],
    label="name",
    tooltip="Compressed air energy storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenUnitOpSchedule_TreeNode = TreeNode(
    node_for=[GenUnitOpSchedule],
    label="name",
    tooltip="The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamSendoutSchedule_TreeNode = TreeNode(
    node_for=[SteamSendoutSchedule],
    label="name",
    tooltip="The cogeneration plant's steam sendout schedule in volume per time unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartRampCurve_TreeNode = TreeNode(
    node_for=[StartRampCurve],
    label="name",
    tooltip="Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatRateCurve_TreeNode = TreeNode(
    node_for=[HeatRateCurve],
    label="name",
    tooltip="Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LevelVsVolumeCurve_TreeNode = TreeNode(
    node_for=[LevelVsVolumeCurve],
    label="name",
    tooltip="Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EmissionCurve_TreeNode = TreeNode(
    node_for=[EmissionCurve],
    label="name",
    tooltip="Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartupModel_TreeNode = TreeNode(
    node_for=[StartupModel],
    label="name",
    tooltip="Unit start up characteristics depending on how long the unit has been off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroGeneratingUnit_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HydroGeneratingUnit_TailbayLossCurve_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    children="TailbayLossCurve",
    label="=TailbayLossCurve",
    tooltip="A hydro generating unit has a tailbay loss curve",
    add=[TailbayLossCurve],
    move=[TailbayLossCurve],
    icon_path=IMAGE_PATH)
HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    children="HydroGeneratingEfficiencyCurves",
    label="=HydroGeneratingEfficiencyCurves",
    tooltip="A hydro generating unit has an efficiency curve",
    add=[HydroGeneratingEfficiencyCurve],
    move=[HydroGeneratingEfficiencyCurve],
    icon_path=IMAGE_PATH)

EmissionAccount_TreeNode = TreeNode(
    node_for=[EmissionAccount],
    label="name",
    tooltip="Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamSupply_TreeNode = TreeNode(
    node_for=[SteamSupply],
    label="name",
    tooltip="Steam supply for steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SteamSupply_SteamTurbines_TreeNode = TreeNode(
    node_for=[SteamSupply],
    children="SteamTurbines",
    label="=SteamTurbines",
    tooltip="Steam turbines may have steam supplied by a steam supply",
    add=[SteamTurbine],
    move=[SteamTurbine],
    icon_path=IMAGE_PATH)

FossilSteamSupply_TreeNode = TreeNode(
    node_for=[FossilSteamSupply],
    label="name",
    tooltip="Fossil fueled boiler (e.g., coal, oil, gas)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatRecoveryBoiler_TreeNode = TreeNode(
    node_for=[HeatRecoveryBoiler],
    label="name",
    tooltip="The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HeatRecoveryBoiler_CombustionTurbines_TreeNode = TreeNode(
    node_for=[HeatRecoveryBoiler],
    children="CombustionTurbines",
    label="=CombustionTurbines",
    tooltip="A combustion turbine may have a heat recovery boiler for making steam",
    add=[CombustionTurbine],
    move=[CombustionTurbine],
    icon_path=IMAGE_PATH)

PrimeMover_TreeNode = TreeNode(
    node_for=[PrimeMover],
    label="name",
    tooltip="The machine used to develop mechanical energy used to drive a generator.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PrimeMover_SynchronousMachines_TreeNode = TreeNode(
    node_for=[PrimeMover],
    children="SynchronousMachines",
    label="=SynchronousMachines",
    tooltip="Synchronous machines this Prime mover drives.",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

HydroTurbine_TreeNode = TreeNode(
    node_for=[HydroTurbine],
    label="name",
    tooltip="A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Subcritical_TreeNode = TreeNode(
    node_for=[Subcritical],
    label="name",
    tooltip="Once-through subcritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BWRSteamSupply_TreeNode = TreeNode(
    node_for=[BWRSteamSupply],
    label="name",
    tooltip="Boiling water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CTTempActivePowerCurve_TreeNode = TreeNode(
    node_for=[CTTempActivePowerCurve],
    label="name",
    tooltip="Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DrumBoiler_TreeNode = TreeNode(
    node_for=[DrumBoiler],
    label="name",
    tooltip="Drum boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CombustionTurbine_TreeNode = TreeNode(
    node_for=[CombustionTurbine],
    label="name",
    tooltip="A prime mover that is typically fueled by gas or light oil",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Supercritical_TreeNode = TreeNode(
    node_for=[Supercritical],
    label="name",
    tooltip="Once-through supercritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PWRSteamSupply_TreeNode = TreeNode(
    node_for=[PWRSteamSupply],
    label="name",
    tooltip="Pressurized water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamTurbine_TreeNode = TreeNode(
    node_for=[SteamTurbine],
    label="name",
    tooltip="Steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SteamTurbine_SteamSupplys_TreeNode = TreeNode(
    node_for=[SteamTurbine],
    children="SteamSupplys",
    label="=SteamSupplys",
    tooltip="Steam turbines may have steam supplied by a steam supply",
    add=[SteamSupply],
    move=[SteamSupply],
    icon_path=IMAGE_PATH)

CommunicationLink_TreeNode = TreeNode(
    node_for=[CommunicationLink],
    label="name",
    tooltip="The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CommunicationLink_RemoteUnits_TreeNode = TreeNode(
    node_for=[CommunicationLink],
    children="RemoteUnits",
    label="=RemoteUnits",
    tooltip="RTUs may be attached to communication links.",
    add=[RemoteUnit],
    move=[RemoteUnit],
    icon_path=IMAGE_PATH)

RemotePoint_TreeNode = TreeNode(
    node_for=[RemotePoint],
    label="name",
    tooltip="For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemoteSource_TreeNode = TreeNode(
    node_for=[RemoteSource],
    label="name",
    tooltip="Remote sources are state variables that are telemetered or calculated within the remote unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemoteControl_TreeNode = TreeNode(
    node_for=[RemoteControl],
    label="name",
    tooltip="Remote controls are ouputs that are sent by the remote unit to actuators in the process.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemoteUnit_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    label="name",
    tooltip="A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RemoteUnit_CommunicationLinks_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    children="CommunicationLinks",
    label="=CommunicationLinks",
    tooltip="RTUs may be attached to communication links.",
    add=[CommunicationLink],
    move=[CommunicationLink],
    icon_path=IMAGE_PATH)
RemoteUnit_RemotePoints_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    children="RemotePoints",
    label="=RemotePoints",
    tooltip="Remote points this Remote unit contains.",
    add=[RemotePoint],
    move=[RemotePoint],
    icon_path=IMAGE_PATH)

PowerCutZone_TreeNode = TreeNode(
    node_for=[PowerCutZone],
    label="name",
    tooltip="An area or zone of the power system which is used for load shedding purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerCutZone_EnergyConsumers_TreeNode = TreeNode(
    node_for=[PowerCutZone],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="An energy consumer is assigned to a power cut zone",
    add=[EnergyConsumer],
    move=[EnergyConsumer],
    icon_path=IMAGE_PATH)

SeasonDayTypeSchedule_TreeNode = TreeNode(
    node_for=[SeasonDayTypeSchedule],
    label="name",
    tooltip="The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DayType_TreeNode = TreeNode(
    node_for=[DayType],
    label="name",
    tooltip="Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DayType_SeasonDayTypeSchedules_TreeNode = TreeNode(
    node_for=[DayType],
    children="SeasonDayTypeSchedules",
    label="=SeasonDayTypeSchedules",
    tooltip="Schedules that use this DayType.",
    add=[SeasonDayTypeSchedule],
    move=[SeasonDayTypeSchedule],
    icon_path=IMAGE_PATH)

EnergyArea_TreeNode = TreeNode(
    node_for=[EnergyArea],
    label="name",
    tooltip="The class describes an area having energy production or consumption. The class is the basis for further specialization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SubLoadArea_TreeNode = TreeNode(
    node_for=[SubLoadArea],
    label="name",
    tooltip="The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubLoadArea_LoadGroups_TreeNode = TreeNode(
    node_for=[SubLoadArea],
    children="LoadGroups",
    label="=LoadGroups",
    tooltip="The Loadgroups in the SubLoadArea.",
    add=[LoadGroup],
    move=[LoadGroup],
    icon_path=IMAGE_PATH)

StationSupply_TreeNode = TreeNode(
    node_for=[StationSupply],
    label="name",
    tooltip="Station supply with load derived from the station output.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NonConformLoad_TreeNode = TreeNode(
    node_for=[NonConformLoad],
    label="name",
    tooltip="NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NonConformLoadSchedule_TreeNode = TreeNode(
    node_for=[NonConformLoadSchedule],
    label="name",
    tooltip="An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConformLoad_TreeNode = TreeNode(
    node_for=[ConformLoad],
    label="name",
    tooltip="ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConformLoadSchedule_TreeNode = TreeNode(
    node_for=[ConformLoadSchedule],
    label="name",
    tooltip="A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Season_TreeNode = TreeNode(
    node_for=[Season],
    label="name",
    tooltip="A specified time period of the year, e.g., Spring, Summer, Fall, Winter",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Season_CapacityBenefitMargin_TreeNode = TreeNode(
    node_for=[Season],
    children="CapacityBenefitMargin",
    label="=CapacityBenefitMargin",
    tooltip="Capacity Benefit Margin may differ based on the season",
    add=[CapacityBenefitMargin],
    move=[CapacityBenefitMargin],
    icon_path=IMAGE_PATH)
Season_ViolationLimits_TreeNode = TreeNode(
    node_for=[Season],
    children="ViolationLimits",
    label="=ViolationLimits",
    tooltip="Limits may differ based on the season",
    add=[ViolationLimit],
    move=[ViolationLimit],
    icon_path=IMAGE_PATH)
Season_SeasonDayTypeSchedules_TreeNode = TreeNode(
    node_for=[Season],
    children="SeasonDayTypeSchedules",
    label="=SeasonDayTypeSchedules",
    tooltip="Schedules that use this Season.",
    add=[SeasonDayTypeSchedule],
    move=[SeasonDayTypeSchedule],
    icon_path=IMAGE_PATH)

LoadGroup_TreeNode = TreeNode(
    node_for=[LoadGroup],
    label="name",
    tooltip="The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadGroup_RegisteredLoads_TreeNode = TreeNode(
    node_for=[LoadGroup],
    children="RegisteredLoads",
    label="=RegisteredLoads",
    tooltip="",
    add=[RegisteredLoad],
    move=[RegisteredLoad],
    icon_path=IMAGE_PATH)

LoadResponseCharacteristic_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadResponseCharacteristic_EnergyConsumer_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    children="EnergyConsumer",
    label="=EnergyConsumer",
    tooltip="The set of loads that have the response characteristics.",
    add=[EnergyConsumer],
    move=[EnergyConsumer],
    icon_path=IMAGE_PATH)

NonConformLoadGroup_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    label="name",
    tooltip="Loads that do not follow a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

NonConformLoadGroup_EnergyConsumers_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="Conform loads assigned to this ConformLoadGroup.",
    add=[NonConformLoad],
    move=[NonConformLoad],
    icon_path=IMAGE_PATH)
NonConformLoadGroup_NonConformLoadSchedules_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    children="NonConformLoadSchedules",
    label="=NonConformLoadSchedules",
    tooltip="The NonConformLoadSchedules in the NonConformLoadGroup.",
    add=[NonConformLoadSchedule],
    move=[NonConformLoadSchedule],
    icon_path=IMAGE_PATH)

LoadArea_TreeNode = TreeNode(
    node_for=[LoadArea],
    label="name",
    tooltip="The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadArea_SubLoadAreas_TreeNode = TreeNode(
    node_for=[LoadArea],
    children="SubLoadAreas",
    label="=SubLoadAreas",
    tooltip="The SubLoadAreas in the LoadArea.",
    add=[SubLoadArea],
    move=[SubLoadArea],
    icon_path=IMAGE_PATH)

ConformLoadGroup_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    label="name",
    tooltip="Load that follows a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConformLoadGroup_ConformLoadSchedules_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    children="ConformLoadSchedules",
    label="=ConformLoadSchedules",
    tooltip="The ConformLoadSchedules in the ConformLoadGroup.",
    add=[ConformLoadSchedule],
    move=[ConformLoadSchedule],
    icon_path=IMAGE_PATH)
ConformLoadGroup_EnergyConsumers_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="Conform loads assigned to this ConformLoadGroup.",
    add=[ConformLoad],
    move=[ConformLoad],
    icon_path=IMAGE_PATH)

Contingency_TreeNode = TreeNode(
    node_for=[Contingency],
    label="name",
    tooltip="An event threatening system reliability, consisting of one or more contingency elements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Contingency_ContingencyConstraintLimit_TreeNode = TreeNode(
    node_for=[Contingency],
    children="ContingencyConstraintLimit",
    label="=ContingencyConstraintLimit",
    tooltip="",
    add=[ContingencyConstraintLimit],
    move=[ContingencyConstraintLimit],
    icon_path=IMAGE_PATH)
Contingency_ContingencyElement_TreeNode = TreeNode(
    node_for=[Contingency],
    children="ContingencyElement",
    label="=ContingencyElement",
    tooltip="A contingency can have any number of contingency elements.",
    add=[ContingencyElement],
    move=[ContingencyElement],
    icon_path=IMAGE_PATH)

ContingencyElement_TreeNode = TreeNode(
    node_for=[ContingencyElement],
    label="name",
    tooltip="An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ContingencyEquipment_TreeNode = TreeNode(
    node_for=[ContingencyEquipment],
    label="name",
    tooltip="A equipment to which the in service status is to change such as a power transformer or AC line segment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TieFlow_TreeNode = TreeNode(
    node_for=[TieFlow],
        tooltip="A flow specification in terms of location and direction for a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TieFlow_AltTieMeas_TreeNode = TreeNode(
    node_for=[TieFlow],
    children="AltTieMeas",
    label="=AltTieMeas",
    tooltip="The primary and alternate tie flow measurements associated with the tie flow.",
    add=[AltTieMeas],
    move=[AltTieMeas],
    icon_path=IMAGE_PATH)

ControlArea_TreeNode = TreeNode(
    node_for=[ControlArea],
    label="name",
    tooltip="A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlArea_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="The generating unit specificaitons for the control area.",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)
ControlArea_TieFlow_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="TieFlow",
    label="=TieFlow",
    tooltip="The tie flows associated with the control area.",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)

ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlAreaGeneratingUnit],
        tooltip="A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlAreaGeneratingUnit_AltGeneratingUnitMeas_TreeNode = TreeNode(
    node_for=[ControlAreaGeneratingUnit],
    children="AltGeneratingUnitMeas",
    label="=AltGeneratingUnitMeas",
    tooltip="The link to prioritized measurements for this GeneratingUnit.",
    add=[AltGeneratingUnitMeas],
    move=[AltGeneratingUnitMeas],
    icon_path=IMAGE_PATH)

AltGeneratingUnitMeas_TreeNode = TreeNode(
    node_for=[AltGeneratingUnitMeas],
        tooltip="A prioritized measurement to be used for the generating unit in the control area specificaiton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AltTieMeas_TreeNode = TreeNode(
    node_for=[AltTieMeas],
        tooltip="A prioritized measurement to be used for the tie flow as part of the control area specification.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentEquipment_TreeNode = TreeNode(
    node_for=[EquivalentEquipment],
    label="name",
    tooltip="The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentBranch_TreeNode = TreeNode(
    node_for=[EquivalentBranch],
    label="name",
    tooltip="The class represents equivalent branches.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentShunt_TreeNode = TreeNode(
    node_for=[EquivalentShunt],
    label="name",
    tooltip="The class represents equivalent shunts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentInjection_TreeNode = TreeNode(
    node_for=[EquivalentInjection],
    label="name",
    tooltip="This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the local connectivity node.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentNetwork_TreeNode = TreeNode(
    node_for=[EquivalentNetwork],
    label="name",
    tooltip="A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquivalentNetwork_EquivalentEquipments_TreeNode = TreeNode(
    node_for=[EquivalentNetwork],
    children="EquivalentEquipments",
    label="=EquivalentEquipments",
    tooltip="The associated reduced equivalents.",
    add=[EquivalentEquipment],
    move=[EquivalentEquipment],
    icon_path=IMAGE_PATH)

ClearanceTag_TreeNode = TreeNode(
    node_for=[ClearanceTag],
    label="name",
    tooltip="A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ClearanceTagType_TreeNode = TreeNode(
    node_for=[ClearanceTagType],
    label="name",
    tooltip="Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ClearanceTagType_ClearanceTags_TreeNode = TreeNode(
    node_for=[ClearanceTagType],
    children="ClearanceTags",
    label="=ClearanceTags",
    tooltip="The ClearanceTags currently being defined for this type.",
    add=[ClearanceTag],
    move=[ClearanceTag],
    icon_path=IMAGE_PATH)

OutageSchedule_TreeNode = TreeNode(
    node_for=[OutageSchedule],
    label="name",
    tooltip="The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageSchedule_SwitchingOperations_TreeNode = TreeNode(
    node_for=[OutageSchedule],
    children="SwitchingOperations",
    label="=SwitchingOperations",
    tooltip="An OutageSchedule may operate many switches.",
    add=[SwitchingOperation],
    move=[SwitchingOperation],
    icon_path=IMAGE_PATH)

SwitchingOperation_TreeNode = TreeNode(
    node_for=[SwitchingOperation],
    label="name",
    tooltip="A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchingOperation_Switches_TreeNode = TreeNode(
    node_for=[SwitchingOperation],
    children="Switches",
    label="=Switches",
    tooltip="A switch may be operated by many schedules.",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)

FaultIndicator_TreeNode = TreeNode(
    node_for=[FaultIndicator],
    label="name",
    tooltip="A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with the dispatch of crews to 'most likely' part of the network (i.e. assists with determining circuit section where the fault most likely happened).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FaultIndicator_FaultIndicatorAssets_TreeNode = TreeNode(
    node_for=[FaultIndicator],
    children="FaultIndicatorAssets",
    label="=FaultIndicatorAssets",
    tooltip="",
    add=[FaultIndicatorAsset],
    move=[FaultIndicatorAsset],
    icon_path=IMAGE_PATH)

SurgeProtector_TreeNode = TreeNode(
    node_for=[SurgeProtector],
    label="name",
    tooltip="Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RecloseSequence_TreeNode = TreeNode(
    node_for=[RecloseSequence],
    label="name",
    tooltip="A reclose sequence (open and close) is defined for each possible reclosure of a breaker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectionEquipment_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    label="name",
    tooltip="An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectionEquipment_ProtectedSwitches_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    children="ProtectedSwitches",
    label="=ProtectedSwitches",
    tooltip="Protected switches operated by this ProtectionEquipment.",
    add=[ProtectedSwitch],
    move=[ProtectedSwitch],
    icon_path=IMAGE_PATH)
ProtectionEquipment_ConductingEquipments_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    children="ConductingEquipments",
    label="=ConductingEquipments",
    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.",
    add=[ConductingEquipment],
    move=[ConductingEquipment],
    icon_path=IMAGE_PATH)

SynchrocheckRelay_TreeNode = TreeNode(
    node_for=[SynchrocheckRelay],
    label="name",
    tooltip="A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurrentRelay_TreeNode = TreeNode(
    node_for=[CurrentRelay],
    label="name",
    tooltip="A device that checks current flow values in any direction or designated direction",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusNameMarker_TreeNode = TreeNode(
    node_for=[BusNameMarker],
    label="name",
    tooltip="Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusNameMarker_ConnectivityNode_TreeNode = TreeNode(
    node_for=[BusNameMarker],
    children="ConnectivityNode",
    label="=ConnectivityNode",
    tooltip="The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

ConnectivityNode_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    label="name",
    tooltip="Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNode_LossPenaltyFactors_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    children="LossPenaltyFactors",
    label="=LossPenaltyFactors",
    tooltip="",
    add=[LossPenaltyFactor],
    move=[LossPenaltyFactor],
    icon_path=IMAGE_PATH)
ConnectivityNode_NodeConstraintTerms_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    children="NodeConstraintTerms",
    label="=NodeConstraintTerms",
    tooltip="",
    add=[NodeConstraintTerm],
    move=[NodeConstraintTerm],
    icon_path=IMAGE_PATH)
ConnectivityNode_Terminals_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    children="Terminals",
    label="=Terminals",
    tooltip="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)

TopologicalNode_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    label="name",
    tooltip="A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalNode_Terminal_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    children="Terminal",
    label="=Terminal",
    tooltip="The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)
TopologicalNode_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

TopologicalIsland_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    label="name",
    tooltip="An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalIsland_TopologicalNodes_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    children="TopologicalNodes",
    label="=TopologicalNodes",
    tooltip="A topological node belongs to a topological island",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

PackageDependenciesCIMVeresion_TreeNode = TreeNode(
    node_for=[PackageDependenciesCIMVeresion],
        tooltip="The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)



#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    Element_TreeNode,
    Model_TreeNode,
    Model_Elements_TreeNode,
    CombinedVersion_TreeNode,
    PowerROCPerMin_TreeNode,
    RateOfChange_TreeNode,
    EnumeratedType_TreeNode,
    FreqBiasFactor_TreeNode,
    FlowgateIdcType_TreeNode,
    Quantity_TreeNode,
    EnergyAsMWh_TreeNode,
    FlowgateAfcUseCode_TreeNode,
    PenaltyFactor_TreeNode,
    IEC61968CIMVersion_TreeNode,
    ReceiptSummary_TreeNode,
    TransactionSummary_TreeNode,
    FinancialVersion_TreeNode,
    ProfileData_TreeNode,
    ProfileData_Profile_TreeNode,
    LossProfile_TreeNode,
    CurtailmentProfile_TreeNode,
    EnergySchedulingVersion_TreeNode,
    EnergyProfile_TreeNode,
    AreaReserveSpec_TreeNode,
    AreaReserveSpec_HostControlAreas_TreeNode,
    TieLine_TreeNode,
    TieLine_ControlAreaOperators_TreeNode,
    Ratio_TreeNode,
    BidClearing_TreeNode,
    ChargeProfile_TreeNode,
    ChargeProfile_ChargeProfileData_TreeNode,
    BilateralTransaction_TreeNode,
    TransactionBid_TreeNode,
    TransactionBid_EnergyProfiles_TreeNode,
    CapacityBenefitMargin_TreeNode,
    CapacityBenefitMargin_Flowgate_TreeNode,
    ChargeProfileData_TreeNode,
    GmlObservation_TreeNode,
    GmlObservation_ChangeItems_TreeNode,
    GmlObservation_GmlValues_TreeNode,
    GmlObservation_Locations_TreeNode,
    ReservationVersion_TreeNode,
    ServiceReservation_TreeNode,
    ServiceReservation_Reserves_AncillaryServices_TreeNode,
    ServiceReservation_Reserves_TransmissionService_TreeNode,
    TransmissionPath_TreeNode,
    TransmissionPath_OfferedOn_TreeNode,
    TransmissionPath_LocatedOn_TreeNode,
    PositionPoint_TreeNode,
    StreetAddress_TreeNode,
    DateTimeInterval_TreeNode,
    PostalAddress_TreeNode,
    TownDetail_TreeNode,
    UserAttribute_TreeNode,
    UserAttribute_PropertyAssets_TreeNode,
    UserAttribute_RatingAssets_TreeNode,
    UserAttribute_ErpLedgerEntries_TreeNode,
    UserAttribute_ProcedureDataSets_TreeNode,
    UserAttribute_PassThroughBills_TreeNode,
    UserAttribute_ErpInvoiceLineItems_TreeNode,
    UserAttribute_BillDeterminants_TreeNode,
    UserAttribute_ErpStatementLineItems_TreeNode,
    Status_TreeNode,
    StreetDetail_TreeNode,
    AcceptanceTest_TreeNode,
    BankAccountDetail_TreeNode,
    AccountMovement_TreeNode,
    TimeTariffInterval_TreeNode,
    TimeTariffInterval_TariffProfiles_TreeNode,
    TimeTariffInterval_Charges_TreeNode,
    Due_TreeNode,
    ConsumptionTariffInterval_TreeNode,
    ConsumptionTariffInterval_Charges_TreeNode,
    ConsumptionTariffInterval_TariffProfiles_TreeNode,
    AccountingUnit_TreeNode,
    LineDetail_TreeNode,
    Card_TreeNode,
    Cheque_TreeNode,
    ReadingQuality_TreeNode,
    IntervalBlock_TreeNode,
    IntervalBlock_IntervalReadings_TreeNode,
    Pending_TreeNode,
    Pending_IntervalBlocks_TreeNode,
    PhaseImpedanceData_TreeNode,
    RemoteConnectDisconnectInfo_TreeNode,
    IEC61970CIMVersion_TreeNode,
    IdentifiedObject_TreeNode,
    GeographicalRegion_TreeNode,
    GeographicalRegion_Regions_TreeNode,
    PowerSystemResource_TreeNode,
    PowerSystemResource_ChangeItems_TreeNode,
    PowerSystemResource_AssetRoles_TreeNode,
    PowerSystemResource_SafetyDocuments_TreeNode,
    PowerSystemResource_Measurements_TreeNode,
    PowerSystemResource_ErpOrganisationRoles_TreeNode,
    PowerSystemResource_PsrLists_TreeNode,
    PowerSystemResource_PSREvent_TreeNode,
    PowerSystemResource_OperatingShare_TreeNode,
    PowerSystemResource_ScheduleSteps_TreeNode,
    PowerSystemResource_DocumentRoles_TreeNode,
    PowerSystemResource_ReportingGroup_TreeNode,
    PowerSystemResource_CircuitSections_TreeNode,
    PowerSystemResource_NetworkDataSets_TreeNode,
    Equipment_TreeNode,
    Equipment_ContingencyEquipment_TreeNode,
    Equipment_CustomerAgreements_TreeNode,
    Equipment_OperationalLimitSet_TreeNode,
    ConductingEquipment_TreeNode,
    ConductingEquipment_Terminals_TreeNode,
    ConductingEquipment_ClearanceTags_TreeNode,
    ConductingEquipment_OutageStepRoles_TreeNode,
    ConductingEquipment_ElectricalAssets_TreeNode,
    ConductingEquipment_ProtectionEquipments_TreeNode,
    Curve_TreeNode,
    Curve_CurveDatas_TreeNode,
    ReportingSuperGroup_TreeNode,
    ReportingSuperGroup_ReportingGroup_TreeNode,
    ConnectivityNodeContainer_TreeNode,
    ConnectivityNodeContainer_TopologicalNode_TreeNode,
    ConnectivityNodeContainer_ConnectivityNodes_TreeNode,
    EquipmentContainer_TreeNode,
    EquipmentContainer_Equipments_TreeNode,
    Substation_TreeNode,
    Substation_VoltageLevels_TreeNode,
    Substation_Bays_TreeNode,
    BasicIntervalSchedule_TreeNode,
    IrregularIntervalSchedule_TreeNode,
    IrregularIntervalSchedule_TimePoints_TreeNode,
    IrregularTimePoint_TreeNode,
    PsrList_TreeNode,
    PsrList_PowerSystemResources_TreeNode,
    RegularIntervalSchedule_TreeNode,
    RegularIntervalSchedule_TimePoints_TreeNode,
    RegularTimePoint_TreeNode,
    OperatingParticipant_TreeNode,
    OperatingParticipant_OperatingShare_TreeNode,
    Bay_TreeNode,
    ModelingAuthority_TreeNode,
    ModelingAuthority_ModelingAuthoritySets_TreeNode,
    VoltageLevel_TreeNode,
    VoltageLevel_Bays_TreeNode,
    Terminal_TreeNode,
    Terminal_HasSecond_MutualCoupling_TreeNode,
    Terminal_OperationalLimitSet_TreeNode,
    Terminal_HasFirst_MutualCoupling_TreeNode,
    Terminal_TieFlow_TreeNode,
    Terminal_Measurements_TreeNode,
    Terminal_RegulatingControl_TreeNode,
    Terminal_TerminalConstraints_TreeNode,
    Terminal_BranchGroupTerminal_TreeNode,
    Unit_TreeNode,
    Unit_Controls_TreeNode,
    Unit_ProtectionEquipments_TreeNode,
    Unit_Measurements_TreeNode,
    CurveData_TreeNode,
    OperatingShare_TreeNode,
    ReportingGroup_TreeNode,
    ReportingGroup_TopologicalNode_TreeNode,
    ReportingGroup_BusNameMarker_TreeNode,
    ReportingGroup_PowerSystemResource_TreeNode,
    PSRType_TreeNode,
    PSRType_PowerSystemResources_TreeNode,
    SubGeographicalRegion_TreeNode,
    SubGeographicalRegion_Substations_TreeNode,
    SubGeographicalRegion_Lines_TreeNode,
    BaseVoltage_TreeNode,
    BaseVoltage_VoltageLevel_TreeNode,
    BaseVoltage_ConductingEquipment_TreeNode,
    BaseVoltage_TopologicalNode_TreeNode,
    BasePower_TreeNode,
    ModelingAuthoritySet_TreeNode,
    ModelingAuthoritySet_IdentifiedObjects_TreeNode,
    Switch_TreeNode,
    Switch_LoadMgmtFunctions_TreeNode,
    Switch_SwitchSchedules_TreeNode,
    Switch_ConnectDisconnectFunctions_TreeNode,
    Switch_SwitchingOperations_TreeNode,
    Fuse_TreeNode,
    HeatExchanger_TreeNode,
    TapChanger_TreeNode,
    TapChanger_TapSchedules_TreeNode,
    PhaseTapChanger_TreeNode,
    RegulatingControl_TreeNode,
    RegulatingControl_RegulationSchedule_TreeNode,
    RegulatingControl_TapChanger_TreeNode,
    RegulatingControl_RegulatingCondEq_TreeNode,
    EnergyConsumer_TreeNode,
    EnergyConsumer_ServiceDeliveryPoints_TreeNode,
    EnergySource_TreeNode,
    Line_TreeNode,
    Line_Flowgates_TreeNode,
    RatioVariationCurve_TreeNode,
    ReactiveCapabilityCurve_TreeNode,
    ReactiveCapabilityCurve_SynchronousMachines_TreeNode,
    ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachines_TreeNode,
    Connector_TreeNode,
    Resistor_TreeNode,
    ProtectedSwitch_TreeNode,
    ProtectedSwitch_RecloseSequences_TreeNode,
    Disconnector_TreeNode,
    Breaker_TreeNode,
    Jumper_TreeNode,
    SeriesCompensator_TreeNode,
    WindingTest_TreeNode,
    Conductor_TreeNode,
    ACLineSegment_TreeNode,
    PowerTransformer_TreeNode,
    PowerTransformer_TransformerWindings_TreeNode,
    PowerTransformer_Flowgates_TreeNode,
    MutualCoupling_TreeNode,
    Ground_TreeNode,
    Ground_WindingInsulations_TreeNode,
    ImpedanceVariationCurve_TreeNode,
    Plant_TreeNode,
    BusbarSection_TreeNode,
    RegulatingCondEq_TreeNode,
    RegulatingCondEq_Controls_TreeNode,
    ShuntCompensator_TreeNode,
    SynchronousMachine_TreeNode,
    SynchronousMachine_ReactiveCapabilityCurves_TreeNode,
    SynchronousMachine_PrimeMovers_TreeNode,
    PhaseVariationCurve_TreeNode,
    FrequencyConverter_TreeNode,
    TransformerWinding_TreeNode,
    TransformerWinding_To_WindingTest_TreeNode,
    TransformerWinding_From_WindingTest_TreeNode,
    Junction_TreeNode,
    DCLineSegment_TreeNode,
    RatioTapChanger_TreeNode,
    CompositeSwitch_TreeNode,
    CompositeSwitch_Switches_TreeNode,
    VoltageControlZone_TreeNode,
    RectifierInverter_TreeNode,
    StaticVarCompensator_TreeNode,
    LoadBreakSwitch_TreeNode,
    GroundDisconnector_TreeNode,
    OperationalLimit_TreeNode,
    VoltageLimit_TreeNode,
    ApparentPowerLimit_TreeNode,
    BranchGroup_TreeNode,
    BranchGroup_BranchGroupTerminal_TreeNode,
    ActivePowerLimit_TreeNode,
    BranchGroupTerminal_TreeNode,
    OperationalLimitSet_TreeNode,
    OperationalLimitSet_OperationalLimitValue_TreeNode,
    CurrentLimit_TreeNode,
    OperationalLimitType_TreeNode,
    OperationalLimitType_OperationalLimit_TreeNode,
    StateVariable_TreeNode,
    SvInjection_TreeNode,
    SvPowerFlow_TreeNode,
    SvStatus_TreeNode,
    SvVoltage_TreeNode,
    SvTapStep_TreeNode,
    SvShortCircuit_TreeNode,
    SvShuntCompensatorSections_TreeNode,
    LimitSet_TreeNode,
    AccumulatorLimitSet_TreeNode,
    AccumulatorLimitSet_Measurements_TreeNode,
    AccumulatorLimitSet_Limits_TreeNode,
    AnalogLimitSet_TreeNode,
    AnalogLimitSet_Limits_TreeNode,
    AnalogLimitSet_Measurements_TreeNode,
    MeasurementValue_TreeNode,
    MeasurementValue_GmlValues_TreeNode,
    MeasurementValue_ProcedureDataSets_TreeNode,
    AccumulatorValue_TreeNode,
    ValueAliasSet_TreeNode,
    ValueAliasSet_Discretes_TreeNode,
    ValueAliasSet_Commands_TreeNode,
    ValueAliasSet_Values_TreeNode,
    PotentialTransformer_TreeNode,
    Limit_TreeNode,
    Limit_Procedures_TreeNode,
    AccumulatorLimit_TreeNode,
    Measurement_TreeNode,
    Measurement_DynamicSchedules_TreeNode,
    Measurement_Documents_TreeNode,
    Measurement_Locations_TreeNode,
    Measurement_ChangeItems_TreeNode,
    Measurement_ViolationLimits_TreeNode,
    Analog_TreeNode,
    Analog_AnalogValues_TreeNode,
    Analog_LimitSets_TreeNode,
    Control_TreeNode,
    SetPoint_TreeNode,
    AnalogLimit_TreeNode,
    Discrete_TreeNode,
    Discrete_DiscreteValues_TreeNode,
    ValueToAlias_TreeNode,
    Quality61850_TreeNode,
    MeasurementValueSource_TreeNode,
    MeasurementValueSource_MeasurementValues_TreeNode,
    Accumulator_TreeNode,
    Accumulator_AccumulatorValues_TreeNode,
    Accumulator_LimitSets_TreeNode,
    CurrentTransformer_TreeNode,
    StringMeasurementValue_TreeNode,
    ControlType_TreeNode,
    ControlType_Controls_TreeNode,
    Command_TreeNode,
    DiscreteValue_TreeNode,
    MeasurementValueQuality_TreeNode,
    AnalogValue_TreeNode,
    AnalogValue_AltTieMeas_TreeNode,
    AnalogValue_AltGeneratingUnit_TreeNode,
    StringMeasurement_TreeNode,
    StringMeasurement_StringMeasurementValues_TreeNode,
    PenstockLossCurve_TreeNode,
    GeneratingUnit_TreeNode,
    GeneratingUnit_ControlAreaGeneratingUnit_TreeNode,
    GeneratingUnit_GenUnitOpCostCurves_TreeNode,
    GeneratingUnit_SynchronousMachines_TreeNode,
    GeneratingUnit_GrossToNetActivePowerCurves_TreeNode,
    ThermalGeneratingUnit_TreeNode,
    ThermalGeneratingUnit_EmmissionAccounts_TreeNode,
    ThermalGeneratingUnit_FuelAllocationSchedules_TreeNode,
    ThermalGeneratingUnit_EmissionCurves_TreeNode,
    ThermalGeneratingUnit_FossilFuels_TreeNode,
    IncrementalHeatRateCurve_TreeNode,
    HeatInputCurve_TreeNode,
    Reservoir_TreeNode,
    Reservoir_InflowForecasts_TreeNode,
    Reservoir_SpillsIntoReservoirs_TreeNode,
    Reservoir_UpstreamFromHydroPowerPlants_TreeNode,
    Reservoir_LevelVsVolumeCurves_TreeNode,
    Reservoir_HydroPowerPlants_TreeNode,
    GenUnitOpCostCurve_TreeNode,
    WindGeneratingUnit_TreeNode,
    StartMainFuelCurve_TreeNode,
    CogenerationPlant_TreeNode,
    CogenerationPlant_ThermalGeneratingUnits_TreeNode,
    GrossToNetActivePowerCurve_TreeNode,
    AirCompressor_TreeNode,
    ShutdownCurve_TreeNode,
    FuelAllocationSchedule_TreeNode,
    TailbayLossCurve_TreeNode,
    HydroPumpOpSchedule_TreeNode,
    FossilFuel_TreeNode,
    FossilFuel_FuelAllocationSchedules_TreeNode,
    TargetLevelSchedule_TreeNode,
    HydroPump_TreeNode,
    HydroPowerPlant_TreeNode,
    HydroPowerPlant_HydroPumps_TreeNode,
    HydroPowerPlant_HydroGeneratingUnits_TreeNode,
    InflowForecast_TreeNode,
    CombinedCyclePlant_TreeNode,
    CombinedCyclePlant_ThermalGeneratingUnits_TreeNode,
    HydroGeneratingEfficiencyCurve_TreeNode,
    NuclearGeneratingUnit_TreeNode,
    StartIgnFuelCurve_TreeNode,
    CAESPlant_TreeNode,
    GenUnitOpSchedule_TreeNode,
    SteamSendoutSchedule_TreeNode,
    StartRampCurve_TreeNode,
    HeatRateCurve_TreeNode,
    LevelVsVolumeCurve_TreeNode,
    EmissionCurve_TreeNode,
    StartupModel_TreeNode,
    HydroGeneratingUnit_TreeNode,
    HydroGeneratingUnit_TailbayLossCurve_TreeNode,
    HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_TreeNode,
    EmissionAccount_TreeNode,
    SteamSupply_TreeNode,
    SteamSupply_SteamTurbines_TreeNode,
    FossilSteamSupply_TreeNode,
    HeatRecoveryBoiler_TreeNode,
    HeatRecoveryBoiler_CombustionTurbines_TreeNode,
    PrimeMover_TreeNode,
    PrimeMover_SynchronousMachines_TreeNode,
    HydroTurbine_TreeNode,
    Subcritical_TreeNode,
    BWRSteamSupply_TreeNode,
    CTTempActivePowerCurve_TreeNode,
    DrumBoiler_TreeNode,
    CombustionTurbine_TreeNode,
    Supercritical_TreeNode,
    PWRSteamSupply_TreeNode,
    SteamTurbine_TreeNode,
    SteamTurbine_SteamSupplys_TreeNode,
    CommunicationLink_TreeNode,
    CommunicationLink_RemoteUnits_TreeNode,
    RemotePoint_TreeNode,
    RemoteSource_TreeNode,
    RemoteControl_TreeNode,
    RemoteUnit_TreeNode,
    RemoteUnit_CommunicationLinks_TreeNode,
    RemoteUnit_RemotePoints_TreeNode,
    PowerCutZone_TreeNode,
    PowerCutZone_EnergyConsumers_TreeNode,
    SeasonDayTypeSchedule_TreeNode,
    DayType_TreeNode,
    DayType_SeasonDayTypeSchedules_TreeNode,
    EnergyArea_TreeNode,
    SubLoadArea_TreeNode,
    SubLoadArea_LoadGroups_TreeNode,
    StationSupply_TreeNode,
    NonConformLoad_TreeNode,
    NonConformLoadSchedule_TreeNode,
    ConformLoad_TreeNode,
    ConformLoadSchedule_TreeNode,
    Season_TreeNode,
    Season_CapacityBenefitMargin_TreeNode,
    Season_ViolationLimits_TreeNode,
    Season_SeasonDayTypeSchedules_TreeNode,
    LoadGroup_TreeNode,
    LoadGroup_RegisteredLoads_TreeNode,
    LoadResponseCharacteristic_TreeNode,
    LoadResponseCharacteristic_EnergyConsumer_TreeNode,
    NonConformLoadGroup_TreeNode,
    NonConformLoadGroup_EnergyConsumers_TreeNode,
    NonConformLoadGroup_NonConformLoadSchedules_TreeNode,
    LoadArea_TreeNode,
    LoadArea_SubLoadAreas_TreeNode,
    ConformLoadGroup_TreeNode,
    ConformLoadGroup_ConformLoadSchedules_TreeNode,
    ConformLoadGroup_EnergyConsumers_TreeNode,
    Contingency_TreeNode,
    Contingency_ContingencyConstraintLimit_TreeNode,
    Contingency_ContingencyElement_TreeNode,
    ContingencyElement_TreeNode,
    ContingencyEquipment_TreeNode,
    TieFlow_TreeNode,
    TieFlow_AltTieMeas_TreeNode,
    ControlArea_TreeNode,
    ControlArea_ControlAreaGeneratingUnit_TreeNode,
    ControlArea_TieFlow_TreeNode,
    ControlAreaGeneratingUnit_TreeNode,
    ControlAreaGeneratingUnit_AltGeneratingUnitMeas_TreeNode,
    AltGeneratingUnitMeas_TreeNode,
    AltTieMeas_TreeNode,
    EquivalentEquipment_TreeNode,
    EquivalentBranch_TreeNode,
    EquivalentShunt_TreeNode,
    EquivalentInjection_TreeNode,
    EquivalentNetwork_TreeNode,
    EquivalentNetwork_EquivalentEquipments_TreeNode,
    ClearanceTag_TreeNode,
    ClearanceTagType_TreeNode,
    ClearanceTagType_ClearanceTags_TreeNode,
    OutageSchedule_TreeNode,
    OutageSchedule_SwitchingOperations_TreeNode,
    SwitchingOperation_TreeNode,
    SwitchingOperation_Switches_TreeNode,
    FaultIndicator_TreeNode,
    FaultIndicator_FaultIndicatorAssets_TreeNode,
    SurgeProtector_TreeNode,
    RecloseSequence_TreeNode,
    ProtectionEquipment_TreeNode,
    ProtectionEquipment_ProtectedSwitches_TreeNode,
    ProtectionEquipment_ConductingEquipments_TreeNode,
    SynchrocheckRelay_TreeNode,
    CurrentRelay_TreeNode,
    BusNameMarker_TreeNode,
    BusNameMarker_ConnectivityNode_TreeNode,
    ConnectivityNode_TreeNode,
    ConnectivityNode_LossPenaltyFactors_TreeNode,
    ConnectivityNode_NodeConstraintTerms_TreeNode,
    ConnectivityNode_Terminals_TreeNode,
    TopologicalNode_TreeNode,
    TopologicalNode_Terminal_TreeNode,
    TopologicalNode_ConnectivityNodes_TreeNode,
    TopologicalIsland_TreeNode,
    TopologicalIsland_TopologicalNodes_TreeNode,
    PackageDependenciesCIMVeresion_TreeNode,
    CreditRegister_TreeNode,
    Token_TreeNode,
    ChargeRegister_TreeNode,
    ErpIssueInventory_TreeNode,
    ErpPayableLineItem_TreeNode,
    ErpPayableLineItem_ErpJournalEntries_TreeNode,
    ErpPayableLineItem_ErpPayments_TreeNode,
    ErpReqLineItem_TreeNode,
    ErpInventory_TreeNode,
    ErpQuoteLineItem_TreeNode,
    ErpPerson_TreeNode,
    ErpPerson_ErpTelephoneNumbers_TreeNode,
    ErpPerson_DocumentRoles_TreeNode,
    ErpPerson_ElectronicAddresses_TreeNode,
    ErpPerson_Crews_TreeNode,
    ErpPerson_Appointments_TreeNode,
    ErpPerson_LaborItems_TreeNode,
    ErpPerson_MeasurementValues_TreeNode,
    ErpPerson_CallBacks_TreeNode,
    ErpPerson_ActivityRecords_TreeNode,
    ErpPerson_ErpOrganisationRoles_TreeNode,
    ErpPerson_Crafts_TreeNode,
    ErpPerson_LocationRoles_TreeNode,
    ErpPerson_Skills_TreeNode,
    ErpPerson_ChangeItems_TreeNode,
    ErpPerson_SwitchingStepRoles_TreeNode,
    ErpPerson_LandPropertyRoles_TreeNode,
    ErpRecDelvLineItem_TreeNode,
    ErpRecDelvLineItem_MaterialItems_TreeNode,
    ErpRecDelvLineItem_Assets_TreeNode,
    ErpBankAccount_TreeNode,
    ErpBomItemData_TreeNode,
    ErpItemMaster_TreeNode,
    ErpInventoryCount_TreeNode,
    ErpJournalEntry_TreeNode,
    ErpJournalEntry_ErpPayableLineItems_TreeNode,
    ErpJournalEntry_CostTypes_TreeNode,
    ErpJournalEntry_ErpRecLineItems_TreeNode,
    ErpTimeEntry_TreeNode,
    ErpRecLineItem_TreeNode,
    ErpRecLineItem_ErpPayments_TreeNode,
    ErpRecLineItem_ErpJournalEntries_TreeNode,
    ErpSiteLevelData_TreeNode,
    ErpPersonnel_TreeNode,
    ErpPersonnel_ErpPersons_TreeNode,
    ErpLedgerEntry_TreeNode,
    ErpLedgerEntry_UserAttributes_TreeNode,
    ErpLedgerEntry_Settlements_TreeNode,
    ErpLedBudLineItem_TreeNode,
    ErpCompetency_TreeNode,
    ErpCompetency_ErpPersons_TreeNode,
    Route_TreeNode,
    Route_Locations_TreeNode,
    Route_Crews_TreeNode,
    RedLine_TreeNode,
    RedLine_Locations_TreeNode,
    LandProperty_TreeNode,
    LandProperty_LocationGrants_TreeNode,
    LandProperty_AssetContainers_TreeNode,
    LandProperty_ErpSiteLevelDatas_TreeNode,
    LandProperty_ErpPersonRoles_TreeNode,
    LandProperty_Locations_TreeNode,
    LandProperty_RightOfWays_TreeNode,
    LandProperty_ErpOrganisationRoles_TreeNode,
    Hazard_TreeNode,
    Hazard_Assets_TreeNode,
    Hazard_Locations_TreeNode,
    DesignLocation_TreeNode,
    DesignLocation_MaterialItems_TreeNode,
    DesignLocation_DesignLocationCUs_TreeNode,
    DesignLocation_Designs_TreeNode,
    DesignLocation_MiscCostItems_TreeNode,
    DesignLocation_ConditionFactors_TreeNode,
    DesignLocation_Diagrams_TreeNode,
    DesignLocation_ErpBomItemDatas_TreeNode,
    DesignLocation_WorkLocations_TreeNode,
    Capability_TreeNode,
    Capability_WorkTasks_TreeNode,
    Capability_Crafts_TreeNode,
    LaborItem_TreeNode,
    LaborItem_ErpPersons_TreeNode,
    CUMaterialItem_TreeNode,
    CUMaterialItem_CompatibleUnits_TreeNode,
    CUMaterialItem_PropertyUnits_TreeNode,
    MaterialItem_TreeNode,
    MaterialItem_Usages_TreeNode,
    MaterialItem_ErpInventoryCounts_TreeNode,
    MaterialItem_ErpRecDelvLineItems_TreeNode,
    MaterialItem_ErpPOLineItems_TreeNode,
    CUContractorItem_TreeNode,
    CUContractorItem_CompatibleUnits_TreeNode,
    Usage_TreeNode,
    CUAllowableAction_TreeNode,
    CUAllowableAction_CompatibleUnits_TreeNode,
    CUAsset_TreeNode,
    CUAsset_CompatibleUnits_TreeNode,
    PropertyUnit_TreeNode,
    PropertyUnit_CUMaterialItems_TreeNode,
    PropertyUnit_CompatibleUnits_TreeNode,
    PropertyUnit_WorkCostDetails_TreeNode,
    CostType_TreeNode,
    CostType_WorkCostDetails_TreeNode,
    CostType_ErpJournalEntries_TreeNode,
    CostType_ChildCostTypes_TreeNode,
    CostType_CompatibleUnits_TreeNode,
    MiscCostItem_TreeNode,
    CULaborItem_TreeNode,
    CULaborItem_QualificationRequirements_TreeNode,
    CULaborItem_CompatibleUnits_TreeNode,
    CULaborCode_TreeNode,
    CULaborCode_CULaborItems_TreeNode,
    ShiftPattern_TreeNode,
    ShiftPattern_Crews_TreeNode,
    OverheadCost_TreeNode,
    OverheadCost_WorkCostDetails_TreeNode,
    OverheadCost_WorkTasks_TreeNode,
    DesignLocationCU_TreeNode,
    DesignLocationCU_Designs_TreeNode,
    DesignLocationCU_CUGroups_TreeNode,
    DesignLocationCU_ConditionFactors_TreeNode,
    DesignLocationCU_WorkTasks_TreeNode,
    DesignLocationCU_CompatibleUnits_TreeNode,
    WorkFlowStep_TreeNode,
    WorkFlowStep_WorkTasks_TreeNode,
    ConditionFactor_TreeNode,
    ConditionFactor_DesignLocationCUs_TreeNode,
    ConditionFactor_DesignLocations_TreeNode,
    ConditionFactor_Designs_TreeNode,
    QualificationRequirement_TreeNode,
    QualificationRequirement_Specifications_TreeNode,
    QualificationRequirement_WorkTasks_TreeNode,
    QualificationRequirement_CULaborItems_TreeNode,
    QualificationRequirement_Skills_TreeNode,
    Crew_TreeNode,
    Crew_Capabilities_TreeNode,
    Crew_WorkTasks_TreeNode,
    Crew_Vehicles_TreeNode,
    Crew_CrewMembers_TreeNode,
    Crew_Assignments_TreeNode,
    Crew_Tools_TreeNode,
    Crew_OutageSteps_TreeNode,
    Crew_WorkEquipmentAssets_TreeNode,
    Crew_Locations_TreeNode,
    Crew_ShiftPatterns_TreeNode,
    Crew_SwitchingSchedules_TreeNode,
    Crew_Organisations_TreeNode,
    ContractorItem_TreeNode,
    ContractorItem_ErpPayables_TreeNode,
    CUGroup_TreeNode,
    CUGroup_ParentCUGroups_TreeNode,
    CUGroup_ChildCUGroups_TreeNode,
    CUGroup_DesignLocationCUs_TreeNode,
    CUGroup_CompatibleUnits_TreeNode,
    CUWorkEquipmentItem_TreeNode,
    CUWorkEquipmentItem_CompatibleUnits_TreeNode,
    WorkLocation_TreeNode,
    WorkLocation_DesignLocations_TreeNode,
    EquipmentItem_TreeNode,
    TransmissionProduct_TreeNode,
    TransmissionProduct_Offers_TreeNode,
    TransmissionProduct_LocationFor_TreeNode,
    ElectricalAsset_TreeNode,
    ElectricalAsset_ElectricalInfos_TreeNode,
    SwitchAsset_TreeNode,
    PowerRating_TreeNode,
    PowerRating_TransformerAssets_TreeNode,
    BusbarAsset_TreeNode,
    StructureSupport_TreeNode,
    Guy_TreeNode,
    ConductorAsset_TreeNode,
    CableAsset_TreeNode,
    CableAsset_DuctBanks_TreeNode,
    Medium_TreeNode,
    Medium_Assets_TreeNode,
    Vehicle_TreeNode,
    WorkEquipmentAsset_TreeNode,
    WorkEquipmentAsset_Usages_TreeNode,
    GeneratorAsset_TreeNode,
    Tool_TreeNode,
    TransformerAsset_TreeNode,
    TransformerAsset_PowerRatings_TreeNode,
    TransformerAsset_TransformerObservations_TreeNode,
    UndergroundStructure_TreeNode,
    WindingInsulation_TreeNode,
    TransformerObservation_TreeNode,
    TransformerObservation_WindingInsulationPFs_TreeNode,
    TransformerObservation_BushingInsultationPFs_TreeNode,
    TransformerObservation_ProcedureDataSets_TreeNode,
    ShuntCompensatorAsset_TreeNode,
    SurgeProtectorAsset_TreeNode,
    CompositeSwitchInfo_TreeNode,
    CompositeSwitchInfo_CompositeSwitchAssets_TreeNode,
    PotentialTransformerAsset_TreeNode,
    FACTSDeviceAsset_TreeNode,
    OverheadConductorAsset_TreeNode,
    DuctBank_TreeNode,
    DuctBank_CableAssets_TreeNode,
    SVCAsset_TreeNode,
    ProtectionEquipmentAsset_TreeNode,
    Manhole_TreeNode,
    BreakerAsset_TreeNode,
    TapChangerAsset_TreeNode,
    SeriesCompensatorAsset_TreeNode,
    CompositeSwitchAsset_TreeNode,
    AssetPropertyCurve_TreeNode,
    AssetPropertyCurve_Assets_TreeNode,
    Pole_TreeNode,
    Pole_SupportStreetlights_TreeNode,
    BushingInsulationPF_TreeNode,
    DimensionsInfo_TreeNode,
    DimensionsInfo_Assets_TreeNode,
    DimensionsInfo_Specifications_TreeNode,
    DimensionsInfo_Locations_TreeNode,
    Anchor_TreeNode,
    CurrentTransformerAsset_TreeNode,
    ResistorAsset_TreeNode,
    Streetlight_TreeNode,
    BushingAsset_TreeNode,
    BushingAsset_BushingInsulationPFs_TreeNode,
    JointAsset_TreeNode,
    RecloserAsset_TreeNode,
    ReliabilityInfo_TreeNode,
    ReliabilityInfo_Assets_TreeNode,
    Tower_TreeNode,
    FaultIndicatorAsset_TreeNode,
    FinancialInfo_TreeNode,
    BreakerInfo_TreeNode,
    BreakerInfo_BreakerAssets_TreeNode,
    BreakerInfo_BreakerAssetModels_TreeNode,
    AssetModelCatalogue_TreeNode,
    AssetModelCatalogue_AssetModelCatalogueItems_TreeNode,
    TransformerAssetModel_TreeNode,
    TransformerAssetModel_TransformerAssets_TreeNode,
    TowerAssetModel_TreeNode,
    TowerAssetModel_Towers_TreeNode,
    PoleModel_TreeNode,
    PoleModel_Poles_TreeNode,
    AssetFunctionAssetModel_TreeNode,
    AssetFunctionAssetModel_AssetFunctions_TreeNode,
    ConductorAssetModel_TreeNode,
    ConductorAssetModel_ConductorAssets_TreeNode,
    AvailableTransmissionCapacity_TreeNode,
    AvailableTransmissionCapacity_ScheduleFor_TreeNode,
    Profile_TreeNode,
    Profile_ProfileDatas_TreeNode,
    SubControlArea_TreeNode,
    SubControlArea_Flowgate_TreeNode,
    SubControlArea_Export_EnergyTransactions_TreeNode,
    SubControlArea_Import_EnergyTransactions_TreeNode,
    SubControlArea_PartOf_TreeNode,
    SubControlArea_SideA_TieLines_TreeNode,
    SubControlArea_GeneratingUnits_TreeNode,
    SubControlArea_SideB_TieLines_TreeNode,
    TransmissionRightOfWay_TreeNode,
    TransmissionRightOfWay_Lines_TreeNode,
    HostControlArea_TreeNode,
    HostControlArea_InadvertentAccounts_TreeNode,
    HostControlArea_SideA_TieLines_TreeNode,
    HostControlArea_SubControlAreas_TreeNode,
    HostControlArea_SideB_TieLines_TreeNode,
    HostControlArea_Receive_DynamicSchedules_TreeNode,
    HostControlArea_Send_DynamicSchedules_TreeNode,
    InadvertentAccount_TreeNode,
    TransmissionCorridor_TreeNode,
    TransmissionCorridor_TransmissionRightOfWays_TreeNode,
    TransmissionCorridor_ContainedIn_TreeNode,
    DynamicSchedule_TreeNode,
    Role_TreeNode,
    ScheduledEvent_TreeNode,
    ScheduledEvent_Assets_TreeNode,
    MarketRole_TreeNode,
    MarketRole_Organisations_TreeNode,
    DocPsrRole_TreeNode,
    DocDocRole_TreeNode,
    BusinessRole_TreeNode,
    BusinessRole_Organisations_TreeNode,
    Craft_TreeNode,
    Craft_Skills_TreeNode,
    Craft_ErpPersons_TreeNode,
    Craft_Capabilities_TreeNode,
    ScheduleParameterInfo_TreeNode,
    ScheduleParameterInfo_ScheduledEvents_TreeNode,
    ScheduleParameterInfo_Documents_TreeNode,
    ContingencyConstraintLimit_TreeNode,
    ResourceGroupReq_TreeNode,
    ResourceGroupReq_RTOs_TreeNode,
    ReserveReq_TreeNode,
    ConstraintTerm_TreeNode,
    TerminalConstraintTerm_TreeNode,
    Meter_TreeNode,
    EnergyPriceCurve_TreeNode,
    EnergyPriceCurve_EnergyTransactions_TreeNode,
    EnergyPriceCurve_FTRs_TreeNode,
    StartUpTimeCurve_TreeNode,
    StartUpTimeCurve_GeneratingBids_TreeNode,
    ResourceBid_TreeNode,
    LoadBid_TreeNode,
    GeneratingBid_TreeNode,
    ResourceGroup_TreeNode,
    ResourceGroup_RegisteredResources_TreeNode,
    ResourceGroup_ResourceGroupReqs_TreeNode,
    RampRateCurve_TreeNode,
    RampRateCurve_GeneratingUnit_TreeNode,
    ProductBid_TreeNode,
    DefaultConstraintLimit_TreeNode,
    MarketStatementLineItem_TreeNode,
    MarketStatementLineItem_ComponentMarketStatementLineItem_TreeNode,
    MarketStatementLineItem_UserAttributes_TreeNode,
    RegisteredResource_TreeNode,
    RegisteredResource_Meters_TreeNode,
    RegisteredResource_Markets_TreeNode,
    RegisteredResource_ResourceGroups_TreeNode,
    RegisteredResource_MarketProducts_TreeNode,
    RegisteredGenerator_TreeNode,
    RegisteredGenerator_UnitInitialConditions_TreeNode,
    RegisteredGenerator_RampRateCurves_TreeNode,
    RegisteredGenerator_GeneratingBids_TreeNode,
    RegisteredGenerator_StartUpCostCurves_TreeNode,
    Market_TreeNode,
    Market_Bids_TreeNode,
    Market_MarketProducts_TreeNode,
    Market_RegisteredResources_TreeNode,
    Market_Settlements_TreeNode,
    Market_MarketFactors_TreeNode,
    RegisteredLoad_TreeNode,
    RegisteredLoad_LoadBids_TreeNode,
    Pnode_TreeNode,
    Pnode_DeliveryTransactionBids_TreeNode,
    Pnode_Measurements_TreeNode,
    Pnode_ReceiptTransactionBids_TreeNode,
    Pnode_FTRs_TreeNode,
    Pnode_RegisteredResources_TreeNode,
    BaseCaseConstraintLimit_TreeNode,
    NodeConstraintTerm_TreeNode,
    ReserveReqCurve_TreeNode,
    SecurityConstraints_TreeNode,
    MWLimitSchedule_TreeNode,
    BidSet_TreeNode,
    BidSet_GeneratingBids_TreeNode,
    TransmissionReliabilityMargin_TreeNode,
    TransmissionReliabilityMargin_Flowgate_TreeNode,
    BidPriceCurve_TreeNode,
    BidPriceCurve_ProductBids_TreeNode,
    MarketProduct_TreeNode,
    MarketProduct_RegisteredResources_TreeNode,
    MarketProduct_ReserveReqs_TreeNode,
    MarketProduct_ProductBids_TreeNode,
    Flowgate_TreeNode,
    Flowgate_ViolationLimits_TreeNode,
    Flowgate_TransmissionProvider_TreeNode,
    Flowgate_PowerTransormers_TreeNode,
    Flowgate_Lines_TreeNode,
    Flowgate_CapacityBenefitMargin_TreeNode,
    Flowgate_FTRs_TreeNode,
    ViolationLimit_TreeNode,
    ViolationLimit_Organisations_TreeNode,
    SensitivityPriceCurve_TreeNode,
    LoadReductionPriceCurve_TreeNode,
    LoadReductionPriceCurve_LoadBids_TreeNode,
    StartUpCostCurve_TreeNode,
    StartUpCostCurve_GeneratingBids_TreeNode,
    StartUpCostCurve_RegisteredGenerators_TreeNode,
    NotificationTimeCurve_TreeNode,
    NotificationTimeCurve_GeneratingBids_TreeNode,
    UnitInitialConditions_TreeNode,
    GmlPosition_TreeNode,
    GmlLabelPlacement_TreeNode,
    GmlLabelPlacement_GmlTextSymbols_TreeNode,
    GmlTopologyStyle_TreeNode,
    GmlSvgParameter_TreeNode,
    GmlSvgParameter_GmlStokes_TreeNode,
    GmlSvgParameter_GmlFills_TreeNode,
    GmlSvgParameter_GmlFonts_TreeNode,
    GmlMark_TreeNode,
    GmlMark_GmlFIlls_TreeNode,
    GmlMark_GmlGraphics_TreeNode,
    GmlMark_GmlStrokes_TreeNode,
    GmlFont_TreeNode,
    GmlFont_GmlTextSymbols_TreeNode,
    GmlFont_GmlSvgParameters_TreeNode,
    GmlSymbol_TreeNode,
    GmlSymbol_GmlFeatureStyles_TreeNode,
    GmlPointSymbol_TreeNode,
    GmlSelector_TreeNode,
    GmlSelector_Locations_TreeNode,
    GmlSelector_ChangeItems_TreeNode,
    GmlGeometryStyle_TreeNode,
    GmlDiagramObject_TreeNode,
    GmlDiagramObject_Diagrams_TreeNode,
    GmlDiagramObject_GmlLineSymbols_TreeNode,
    GmlDiagramObject_GmlCoordinateSystems_TreeNode,
    GmlDiagramObject_GmlRasterSymbols_TreeNode,
    GmlDiagramObject_GmlPolygonSymbols_TreeNode,
    GmlDiagramObject_GmlPointSymbols_TreeNode,
    GmlDiagramObject_GmlTextSymbols_TreeNode,
    GmlPolygonGeometry_TreeNode,
    GmlFeatureType_TreeNode,
    GmlFeatureType_GmlFeatureStyles_TreeNode,
    GmlHalo_TreeNode,
    GmlHalo_GmlTextSymbols_TreeNode,
    GmlPolygonSymbol_TreeNode,
    GmlLineSymbol_TreeNode,
    GmlBaseSymbol_TreeNode,
    GmlBaseSymbol_GmlSymbols_TreeNode,
    GmlValue_TreeNode,
    GmlFill_TreeNode,
    GmlFill_GmlPolygonSymbols_TreeNode,
    GmlFill_GmlSvgParameters_TreeNode,
    GmlFill_GmlMarks_TreeNode,
    GmlFill_GmlTextSymbols_TreeNode,
    GmlPointGeometry_TreeNode,
    GmlRasterSymbol_TreeNode,
    GmlColour_TreeNode,
    GmlColour_GmlFills_TreeNode,
    GmlColour_GmlFonts_TreeNode,
    GmlColour_GmlStrokes_TreeNode,
    GmlLineGeometry_TreeNode,
    GmlTextSymbol_TreeNode,
    GmlLabelStyle_TreeNode,
    GmlLabelStyle_GmlGeometryStyles_TreeNode,
    GmlLabelStyle_GmlTopologyStyles_TreeNode,
    GmlGraphic_TreeNode,
    GmlGraphic_GmlMarks_TreeNode,
    GmlGraphic_GmlPointSymbols_TreeNode,
    GmlStroke_TreeNode,
    GmlStroke_GmlSvgParameters_TreeNode,
    GmlStroke_GmlLineSymbols_TreeNode,
    GmlStroke_GmlMarks_TreeNode,
    GmlStroke_GmlPolygonSymbols_TreeNode,
    GmlCoordinateSystem_TreeNode,
    GmlCoordinateSystem_GmlPositions_TreeNode,
    GmlCoordinateSystem_GmlDiagramObjects_TreeNode,
    GmlCoordinateSystem_Diagrams_TreeNode,
    GmlFeatureStyle_TreeNode,
    GmlFeatureStyle_GmlGeometryStyles_TreeNode,
    GmlFeatureStyle_GmlFeatureTypes_TreeNode,
    GmlFeatureStyle_GmlLabelStyles_TreeNode,
    GmlFeatureStyle_GmlSymbols_TreeNode,
    GmlFeatureStyle_GmlTobologyStyles_TreeNode,
    SwitchingStep_TreeNode,
    SwitchingStep_PowerSystemResources_TreeNode,
    ErpPersonScheduleStepRole_TreeNode,
    OutageStep_TreeNode,
    OutageStep_Crews_TreeNode,
    OutageStep_OutageCodes_TreeNode,
    OutageStep_ConductingEquipmentRoles_TreeNode,
    OutageCode_TreeNode,
    OutageCode_OutageRecords_TreeNode,
    OutageCode_OutageSteps_TreeNode,
    OutageStepPsrRole_TreeNode,
    NetworkDataSet_TreeNode,
    NetworkDataSet_Documents_TreeNode,
    NetworkDataSet_CircuitSections_TreeNode,
    NetworkDataSet_LandBases_TreeNode,
    NetworkDataSet_ChangeSets_TreeNode,
    NetworkDataSet_PowerSystemResources_TreeNode,
    NetworkDataSet_ChangeItems_TreeNode,
    CircuitSection_TreeNode,
    CircuitSection_ConductorAssets_TreeNode,
    CircuitSection_NetworkDataSets_TreeNode,
    CircuitSection_PowerSystemResources_TreeNode,
    CircuitSection_Circuits_TreeNode,
    CallBack_TreeNode,
    CallBack_ErpPersons_TreeNode,
    CallBack_Appointments_TreeNode,
    CallBack_TroubleTickets_TreeNode,
    ChangeItem_TreeNode,
    OrgPsrRole_TreeNode,
    IncidentCode_TreeNode,
    IncidentCode_IncidentRecords_TreeNode,
    ChangeSet_TreeNode,
    ChangeSet_LandBases_TreeNode,
    ChangeSet_NetworkDataSets_TreeNode,
    ChangeSet_ChangeItems_TreeNode,
    ChangeSet_Documents_TreeNode,
    Circuit_TreeNode,
    MountingPoint_TreeNode,
    MountingPoint_OverheadConductors_TreeNode,
    MountingPoint_Connections_TreeNode,
    TypeAssetCatalogue_TreeNode,
    TypeAssetCatalogue_TypeAssets_TreeNode,
    ComEquipmentTypeAsset_TreeNode,
    VehicleTypeAsset_TreeNode,
    VehicleTypeAsset_VehicleAssetModels_TreeNode,
    Connection_TreeNode,
    Connection_StructureTypeAssets_TreeNode,
    Connection_MountingPoints_TreeNode,
    SubstationTypeAsset_TreeNode,
    AssetFunctionTypeAsset_TreeNode,
    AssetFunctionTypeAsset_AssetFunctionAssetModels_TreeNode,
    TiePoint_TreeNode,
    TiePoint_For_Measurements_TreeNode,
    TiePoint_By_Measurements_TreeNode,
    TransmissionService_TreeNode,
    TransmissionService_OfferedAs_TreeNode,
    TransmissionService_Offering_TreeNode,
    TransmissionService_ScheduledBy_TreeNode,
    TransmissionService_ReservedBy_ServiceReservation_TreeNode,
    ServicePoint_TreeNode,
    ServicePoint_EnergyProducts_TreeNode,
    ServicePoint_HasAPOD__TreeNode,
    ServicePoint_HasAPOR__TreeNode,
    AncillaryService_TreeNode,
    AncillaryService_TransmissionProviders_TreeNode,
    SubscribePowerCurve_TreeNode,
    ComPort_TreeNode,
    MeteringFunctionConfiguration_TreeNode,
    MeteringFunctionConfiguration_ElectricMeteringFunctions_TreeNode,
    Organisation_TreeNode,
    Organisation_BusinessRoles_TreeNode,
    Organisation_TelephoneNumbers_TreeNode,
    Organisation_MarketRoles_TreeNode,
    Organisation_ElectronicAddresses_TreeNode,
    ActivityRecord_TreeNode,
    ActivityRecord_MarketFactors_TreeNode,
    ActivityRecord_Documents_TreeNode,
    ActivityRecord_Organisations_TreeNode,
    ActivityRecord_Assets_TreeNode,
    ActivityRecord_ErpPersons_TreeNode,
    ActivityRecord_Locations_TreeNode,
    Document_TreeNode,
    Document_ActivityRecords_TreeNode,
    Document_ErpOrganisationRoles_TreeNode,
    Document_ScheduledEvents_TreeNode,
    Document_FromDocumentRoles_TreeNode,
    Document_LocationRoles_TreeNode,
    Document_PowerSystemResourceRoles_TreeNode,
    Document_NetworkDataSets_TreeNode,
    Document_ErpPersonRoles_TreeNode,
    Document_ChangeItems_TreeNode,
    Document_Measurements_TreeNode,
    Document_ScheduleParameterInfos_TreeNode,
    Document_ToDocumentRoles_TreeNode,
    Document_AssetRoles_TreeNode,
    Document_ChangeSets_TreeNode,
    Agreement_TreeNode,
    Location_TreeNode,
    Location_DocumentRoles_TreeNode,
    Location_ErpPersonRoles_TreeNode,
    Location_ElectronicAddresses_TreeNode,
    Location_ChangeItems_TreeNode,
    Location_Routes_TreeNode,
    Location_PositionPoints_TreeNode,
    Location_GmlSelectors_TreeNode,
    Location_FromLocationRoles_TreeNode,
    Location_ToLocationRoles_TreeNode,
    Location_TelephoneNumbers_TreeNode,
    Location_LandProperties_TreeNode,
    Location_Measurements_TreeNode,
    Location_ErpOrganisationRoles_TreeNode,
    Location_AssetRoles_TreeNode,
    Location_Crews_TreeNode,
    Location_RedLines_TreeNode,
    Location_GmlObservatins_TreeNode,
    Location_Hazards_TreeNode,
    Location_ActivityRecords_TreeNode,
    TimeSchedule_TreeNode,
    TimeSchedule_TimePoints_TreeNode,
    TelephoneNumber_TreeNode,
    ElectronicAddress_TreeNode,
    ElectronicAddress_ErpTelephoneNumbers_TreeNode,
    ElectronicAddress_Locations_TreeNode,
    TimePoint_TreeNode,
    TimePoint_ScheduledEvents_TreeNode,
    GeoLocation_TreeNode,
    GeoLocation_PowerSystemResources_TreeNode,
    Seal_TreeNode,
    Asset_TreeNode,
    Asset_Measurements_TreeNode,
    Asset_Hazards_TreeNode,
    Asset_ErpOrganisationRoles_TreeNode,
    Asset_ScheduledEvents_TreeNode,
    Asset_Mediums_TreeNode,
    Asset_AssetFunctions_TreeNode,
    Asset_Properties_TreeNode,
    Asset_Ratings_TreeNode,
    Asset_ActivityRecords_TreeNode,
    Asset_FromAssetRoles_TreeNode,
    Asset_LocationRoles_TreeNode,
    Asset_PowerSystemResourceRoles_TreeNode,
    Asset_DocumentRoles_TreeNode,
    Asset_ChangeItems_TreeNode,
    Asset_ElectronicAddresses_TreeNode,
    Asset_ErpRecDeliveryItems_TreeNode,
    Asset_ReliabilityInfos_TreeNode,
    Asset_ToAssetRoles_TreeNode,
    Asset_AssetPropertyCurves_TreeNode,
    AssetFunction_TreeNode,
    ElectricalInfo_TreeNode,
    ElectricalInfo_EndDeviceAssets_TreeNode,
    ElectricalInfo_ElectricalTypeAssets_TreeNode,
    ElectricalInfo_ElectricalAssets_TreeNode,
    ElectricalInfo_ElectricalAssetModels_TreeNode,
    ComMediaAsset_TreeNode,
    AssetContainer_TreeNode,
    AssetContainer_LandProperties_TreeNode,
    AssetContainer_Assets_TreeNode,
    AssetContainer_Seals_TreeNode,
    AssetModel_TreeNode,
    AssetModel_ErpInventoryCounts_TreeNode,
    AssetModel_AssetModelCatalogueItems_TreeNode,
    DistributionWindingTest_TreeNode,
    WindingInfo_TreeNode,
    WindingInfo_WindingTests_TreeNode,
    WindingInfo_Windings_TreeNode,
    WindingInfo_ToWindingSpecs_TreeNode,
    ConductorInfo_TreeNode,
    ConductorInfo_ConductorSegments_TreeNode,
    ConductorInfo_WireArrangements_TreeNode,
    CableInfo_TreeNode,
    ConcentricNeutralCableInfo_TreeNode,
    WireArrangement_TreeNode,
    WireType_TreeNode,
    WireType_WireArrangements_TreeNode,
    WireType_ConcentricNeutralCableInfos_TreeNode,
    ShortCircuitTest_TreeNode,
    ShortCircuitTest_ShortedWindingSpecs_TreeNode,
    OverheadConductorInfo_TreeNode,
    OpenCircuitTest_TreeNode,
    OpenCircuitTest_MeasuredWindingSpecs_TreeNode,
    TransformerInfo_TreeNode,
    TransformerInfo_Transformers_TreeNode,
    TransformerInfo_TransformerAssets_TreeNode,
    TransformerInfo_WindingInfos_TreeNode,
    TransformerInfo_TransformerAssetModels_TreeNode,
    ToWindingSpec_TreeNode,
    ToWindingSpec_OpenCircuitTests_TreeNode,
    ToWindingSpec_ShortCircuitTests_TreeNode,
    TapeShieldCableInfo_TreeNode,
    EndDeviceModel_TreeNode,
    EndDeviceModel_EndDeviceAssets_TreeNode,
    MerchantAccount_TreeNode,
    MerchantAccount_Vendors_TreeNode,
    MerchantAccount_Transactors_TreeNode,
    MerchantAccount_BankStatements_TreeNode,
    MerchantAccount_VendorShifts_TreeNode,
    AuxiliaryAccount_TreeNode,
    AuxiliaryAccount_Charges_TreeNode,
    AuxiliaryAccount_PaymentTransactions_TreeNode,
    Cashier_TreeNode,
    Cashier_ElectronicAddresses_TreeNode,
    Cashier_CashierShifts_TreeNode,
    Shift_TreeNode,
    Shift_ReceiptSummaries_TreeNode,
    Shift_TransactionSummaries_TreeNode,
    VendorShift_TreeNode,
    VendorShift_Transactions_TreeNode,
    VendorShift_Receipts_TreeNode,
    MerchantAgreement_TreeNode,
    MerchantAgreement_MerchantAccounts_TreeNode,
    Charge_TreeNode,
    Charge_ConsumptionTariffIntervals_TreeNode,
    Charge_AuxiliaryAccounts_TreeNode,
    Charge_TimeTariffIntervals_TreeNode,
    Charge_ChildCharges_TreeNode,
    ServiceSupplier_TreeNode,
    ServiceSupplier_ServiceDeliveryPoints_TreeNode,
    ServiceSupplier_CustomerAgreements_TreeNode,
    ServiceSupplier_BankAccounts_TreeNode,
    Receipt_TreeNode,
    Receipt_Transactions_TreeNode,
    Receipt_Tenders_TreeNode,
    Tender_TreeNode,
    PointOfSale_TreeNode,
    PointOfSale_Tokens_TreeNode,
    PointOfSale_CashierShifts_TreeNode,
    CashierShift_TreeNode,
    CashierShift_Receipts_TreeNode,
    CashierShift_Transactions_TreeNode,
    Transaction_TreeNode,
    Transaction_UserAttributes_TreeNode,
    Transactor_TreeNode,
    Transactor_MerchantAccounts_TreeNode,
    TariffProfile_TreeNode,
    TariffProfile_ConsumptionTariffIntervals_TreeNode,
    TariffProfile_Tariffs_TreeNode,
    TariffProfile_TimeTariffIntervals_TreeNode,
    AuxiliaryAgreement_TreeNode,
    AuxiliaryAgreement_AuxiliaryAccounts_TreeNode,
    Vendor_TreeNode,
    Vendor_PointOfSales_TreeNode,
    Vendor_BankStatements_TreeNode,
    Vendor_Cashiers_TreeNode,
    Vendor_VendorShifts_TreeNode,
    SDPLocation_TreeNode,
    SDPLocation_ServiceDeliveryPoints_TreeNode,
    DeviceFunction_TreeNode,
    DeviceFunction_Registers_TreeNode,
    DeviceFunction_EndDeviceEvents_TreeNode,
    ComFunction_TreeNode,
    IntervalReading_TreeNode,
    IntervalReading_IntervalBlocks_TreeNode,
    IntervalReading_ReadingQualities_TreeNode,
    ReadingType_TreeNode,
    ReadingType_Readings_TreeNode,
    ReadingType_IntervalBlocks_TreeNode,
    EndDeviceAsset_TreeNode,
    EndDeviceAsset_EndDeviceGroups_TreeNode,
    EndDeviceAsset_EndDeviceControls_TreeNode,
    EndDeviceAsset_ElectricalInfos_TreeNode,
    EndDeviceAsset_Readings_TreeNode,
    EndDeviceAsset_DeviceFunctions_TreeNode,
    MeterAsset_TreeNode,
    MeterAsset_MeterReadings_TreeNode,
    MeterAsset_VendingTransactions_TreeNode,
    MeterAsset_MeterServiceWorks_TreeNode,
    MeterAsset_MeterReplacementWorks_TreeNode,
    ElectricMeteringFunction_TreeNode,
    Reading_TreeNode,
    Reading_ReadingQualities_TreeNode,
    Reading_MeterReadings_TreeNode,
    Register_TreeNode,
    MeterServiceWork_TreeNode,
    MeterReading_TreeNode,
    MeterReading_IntervalBlocks_TreeNode,
    MeterReading_Readings_TreeNode,
    MeterReading_EndDeviceEvents_TreeNode,
    DemandResponseProgram_TreeNode,
    DemandResponseProgram_EndDeviceGroups_TreeNode,
    DemandResponseProgram_CustomerAgreements_TreeNode,
    DemandResponseProgram_EndDeviceControls_TreeNode,
    EndDeviceEvent_TreeNode,
    EndDeviceControl_TreeNode,
    ServiceDeliveryPoint_TreeNode,
    ServiceDeliveryPoint_SDPLocations_TreeNode,
    ServiceDeliveryPoint_MeterReadings_TreeNode,
    ServiceDeliveryPoint_PricingStructures_TreeNode,
    ServiceDeliveryPoint_PowerQualityPricings_TreeNode,
    ServiceDeliveryPoint_EndDeviceAssets_TreeNode,
    EndDeviceGroup_TreeNode,
    EndDeviceGroup_EndDeviceAssets_TreeNode,
    EndDeviceGroup_EndDeviceControls_TreeNode,
    Work_TreeNode,
    Work_WorkFlowSteps_TreeNode,
    Work_Customers_TreeNode,
    Work_WorkTasks_TreeNode,
    Work_Designs_TreeNode,
    Work_WorkCostDetails_TreeNode,
    ServiceCategory_TreeNode,
    ServiceCategory_CustomerAgreements_TreeNode,
    ServiceCategory_ServiceDeliveryPoints_TreeNode,
    ServiceCategory_SPAccountingFunctions_TreeNode,
    ServiceCategory_PricingStructures_TreeNode,
    CustomerAccount_TreeNode,
    CustomerAccount_WorkBillingInfos_TreeNode,
    CustomerAccount_PaymentTransactions_TreeNode,
    CustomerAccount_CustomerAgreements_TreeNode,
    CustomerAccount_CustomerBillingInfos_TreeNode,
    CustomerAccount_ErpInvoicees_TreeNode,
    Tariff_TreeNode,
    Tariff_PricingStructures_TreeNode,
    Tariff_TariffProfiles_TreeNode,
    PricingStructure_TreeNode,
    PricingStructure_Tariffs_TreeNode,
    PricingStructure_PowerQualityPricings_TreeNode,
    PricingStructure_Transactions_TreeNode,
    PricingStructure_ServiceDeliveryPoints_TreeNode,
    PricingStructure_CustomerAgreements_TreeNode,
    Customer_TreeNode,
    Customer_TroubleTickets_TreeNode,
    Customer_Works_TreeNode,
    Customer_OutageNotifications_TreeNode,
    Customer_ErpPersons_TreeNode,
    Customer_EndDeviceAssets_TreeNode,
    Customer_CustomerAgreements_TreeNode,
    CustomerAgreement_TreeNode,
    CustomerAgreement_ServiceLocations_TreeNode,
    CustomerAgreement_ServiceDeliveryPoints_TreeNode,
    CustomerAgreement_MeterReadings_TreeNode,
    CustomerAgreement_AuxiliaryAgreements_TreeNode,
    CustomerAgreement_Equipments_TreeNode,
    CustomerAgreement_EndDeviceControls_TreeNode,
    CustomerAgreement_PricingStructures_TreeNode,
    ServiceLocation_TreeNode,
    ServiceLocation_CustomerAgreements_TreeNode,
    ServiceLocation_EndDeviceAssets_TreeNode,
    ServiceLocation_ServiceDeliveryPoints_TreeNode,
    PerLengthPhaseImpedance_TreeNode,
    PerLengthPhaseImpedance_PhaseImpedanceData_TreeNode,
    PerLengthPhaseImpedance_ConductorSegments_TreeNode,
    DistributionTransformerWinding_TreeNode,
    DistributionTransformerWinding_FromWindingInsulations_TreeNode,
    DistributionTransformerWinding_ToWindingInsulations_TreeNode,
    WindingPiImpedance_TreeNode,
    WindingPiImpedance_Windings_TreeNode,
    DistributionTransformer_TreeNode,
    DistributionTransformer_TransformerObservations_TreeNode,
    DistributionTransformer_Windings_TreeNode,
    DistributionLineSegment_TreeNode,
    DistributionLineSegment_ConductorAssets_TreeNode,
    PerLengthSequenceImpedance_TreeNode,
    PerLengthSequenceImpedance_ConductorSegments_TreeNode,
    TransformerBank_TreeNode,
    TransformerBank_Transformers_TreeNode,
    DistributionTapChanger_TreeNode,
    ConnectDisconnectFunction_TreeNode,
    ConnectDisconnectFunction_Switches_TreeNode,
    TapSchedule_TreeNode,
    SwitchSchedule_TreeNode,
    RegulationSchedule_TreeNode,
    RegulationSchedule_VoltageControlZones_TreeNode,
    BankStatement_TreeNode,
    TSPAgreement_TreeNode,
    Bank_TreeNode,
    Bank_BankAccounts_TreeNode,
    SDPAccountingFunction_TreeNode,
    SDPAccountingFunction_ChargeRegisters_TreeNode,
    SDPAccountingFunction_CreditRegisters_TreeNode,
    ErpOrganisation_TreeNode,
    ErpOrganisation_DocumentRoles_TreeNode,
    ErpOrganisation_ActivityRecords_TreeNode,
    ErpOrganisation_LocationRoles_TreeNode,
    ErpOrganisation_ErpPersonRoles_TreeNode,
    ErpOrganisation_ViolationLimits_TreeNode,
    ErpOrganisation_Requests_TreeNode,
    ErpOrganisation_ChangeItems_TreeNode,
    ErpOrganisation_IntSchedAgreement_TreeNode,
    ErpOrganisation_RegisteredResources_TreeNode,
    ErpOrganisation_PowerSystemResourceRoles_TreeNode,
    ErpOrganisation_AssetRoles_TreeNode,
    ErpOrganisation_LandPropertyRoles_TreeNode,
    ErpOrganisation_ParentOrganisationRoles_TreeNode,
    ErpOrganisation_ChildOrganisationRoles_TreeNode,
    ErpOrganisation_Crews_TreeNode,
    DocErpPersonRole_TreeNode,
    OrgOrgRole_TreeNode,
    ErpLedger_TreeNode,
    ErpLedger_ErpLedgerEntries_TreeNode,
    DocOrgRole_TreeNode,
    ErpJournal_TreeNode,
    ErpJournal_ErpJournalEntries_TreeNode,
    ErpProjectAccounting_TreeNode,
    ErpProjectAccounting_Projects_TreeNode,
    ErpProjectAccounting_WorkCostDetails_TreeNode,
    ErpProjectAccounting_Works_TreeNode,
    ErpProjectAccounting_ErpTimeEntries_TreeNode,
    ErpPurchaseOrder_TreeNode,
    ErpPurchaseOrder_ErpPOLineItems_TreeNode,
    ErpInvoice_TreeNode,
    ErpInvoice_ErpInvoiceLineItems_TreeNode,
    ErpEngChangeOrder_TreeNode,
    ErpInvoiceLineItem_TreeNode,
    ErpInvoiceLineItem_WorkBillingInfos_TreeNode,
    ErpInvoiceLineItem_MarketFactors_TreeNode,
    ErpInvoiceLineItem_ErpJournalEntries_TreeNode,
    ErpInvoiceLineItem_CustomerBillingInfos_TreeNode,
    ErpInvoiceLineItem_UserAttributes_TreeNode,
    ErpInvoiceLineItem_ComponentErpInvoiceLineItems_TreeNode,
    ErpInvoiceLineItem_ErpPayments_TreeNode,
    ErpInvoiceLineItem_Settlements_TreeNode,
    ErpPayable_TreeNode,
    ErpPayable_ContractorItems_TreeNode,
    ErpPayable_ErpPayableLineItems_TreeNode,
    ErpPayment_TreeNode,
    ErpPayment_ErpRecLineItems_TreeNode,
    ErpPayment_ErpInvoiceLineItems_TreeNode,
    ErpPayment_ErpPayableLineItems_TreeNode,
    ErpQuote_TreeNode,
    ErpQuote_ErpQuoteLineItems_TreeNode,
    ErpPOLineItem_TreeNode,
    ErpReceiveDelivery_TreeNode,
    ErpReceiveDelivery_ErpRecDelvLineItems_TreeNode,
    ErpChartOfAccounts_TreeNode,
    ErpLedgerBudget_TreeNode,
    ErpLedgerBudget_ErpLedBudLineItems_TreeNode,
    ErpRequisition_TreeNode,
    ErpRequisition_ErpReqLineItems_TreeNode,
    OrgErpPersonRole_TreeNode,
    ErpBOM_TreeNode,
    ErpBOM_ErpBomItemDatas_TreeNode,
    ErpTimeSheet_TreeNode,
    ErpTimeSheet_ErpTimeEntries_TreeNode,
    ErpSalesOrder_TreeNode,
    ErpReceivable_TreeNode,
    ErpReceivable_ErpRecLineItems_TreeNode,
    ErpTelephoneNumber_TreeNode,
    ErpTelephoneNumber_ErpPersons_TreeNode,
    LocLocRole_TreeNode,
    RightOfWay_TreeNode,
    RightOfWay_LandProperties_TreeNode,
    OrgLocRole_TreeNode,
    OrgPropertyRole_TreeNode,
    OrgPropertyRole_LandProperty_TreeNode,
    AssetLocRole_TreeNode,
    ErpPersonLocRole_TreeNode,
    Zone_TreeNode,
    DocLocRole_TreeNode,
    SchematicLocation_TreeNode,
    LocationGrant_TreeNode,
    PersonPropertyRole_TreeNode,
    Design_TreeNode,
    Design_DesignLocationsCUs_TreeNode,
    Design_WorkCostDetails_TreeNode,
    Design_DesignLocations_TreeNode,
    Design_ErpBOMs_TreeNode,
    Design_ConditionFactors_TreeNode,
    Design_WorkTasks_TreeNode,
    NonStandardItem_TreeNode,
    TypeMaterial_TreeNode,
    TypeMaterial_ErpReqLineItems_TreeNode,
    TypeMaterial_ErpIssueInventories_TreeNode,
    TypeMaterial_CUMaterialItems_TreeNode,
    TypeMaterial_MaterialItems_TreeNode,
    Appointment_TreeNode,
    Appointment_ErpPersons_TreeNode,
    CompatibleUnit_TreeNode,
    CompatibleUnit_CUWorkEquipmentItems_TreeNode,
    CompatibleUnit_CUContractorItems_TreeNode,
    CompatibleUnit_Procedures_TreeNode,
    CompatibleUnit_CUAssets_TreeNode,
    CompatibleUnit_CUMaterialItems_TreeNode,
    CompatibleUnit_CULaborItems_TreeNode,
    CompatibleUnit_DesignLocationCUs_TreeNode,
    InfoQuestion_TreeNode,
    Regulation_TreeNode,
    AccessPermit_TreeNode,
    WorkStatusEntry_TreeNode,
    WorkTask_TreeNode,
    WorkTask_ContractorItems_TreeNode,
    WorkTask_Crews_TreeNode,
    WorkTask_WorkCostDetails_TreeNode,
    WorkTask_Usages_TreeNode,
    WorkTask_QualificationRequirements_TreeNode,
    WorkTask_LaborItems_TreeNode,
    WorkTask_MaterialItems_TreeNode,
    WorkTask_EquipmentItems_TreeNode,
    WorkTask_DesignLocationCUs_TreeNode,
    WorkTask_Assets_TreeNode,
    WorkTask_Capabilities_TreeNode,
    WorkTask_MiscCostItems_TreeNode,
    WorkTask_SwitchingSchedules_TreeNode,
    Request_TreeNode,
    Request_Projects_TreeNode,
    Request_Works_TreeNode,
    Project_TreeNode,
    Project_Works_TreeNode,
    Project_Requests_TreeNode,
    Project_SubProjects_TreeNode,
    WorkCostSummary_TreeNode,
    OneCallRequest_TreeNode,
    OneCallRequest_WorkLocations_TreeNode,
    Assignment_TreeNode,
    Assignment_Crews_TreeNode,
    WorkCostDetail_TreeNode,
    WorkCostDetail_LaborItems_TreeNode,
    WorkCostDetail_EquipmentItems_TreeNode,
    WorkCostDetail_MiscCostItems_TreeNode,
    WorkCostDetail_Works_TreeNode,
    WorkCostDetail_ContractorItems_TreeNode,
    WorkCostDetail_MaterialItems_TreeNode,
    WorkCostDetail_PropertyUnits_TreeNode,
    BusinessCase_TreeNode,
    BusinessCase_Works_TreeNode,
    BusinessCase_Projects_TreeNode,
    Marketer_TreeNode,
    Marketer_HeldBy_TreeNode,
    Marketer_Resells_EnergyProduct_TreeNode,
    Marketer_HoldsTitleTo_EnergyProducts_TreeNode,
    CustomerConsumer_TreeNode,
    CustomerConsumer_ServicePoint_TreeNode,
    CustomerConsumer_TieLines_TreeNode,
    TransmissionProvider_TreeNode,
    TransmissionProvider_TransmissionProducts_TreeNode,
    TransmissionProvider_Flowgate_TreeNode,
    TransmissionProvider_ServicePoint_TreeNode,
    TransmissionProvider_AncillaryServices_TreeNode,
    TransmissionProvider_For_TreeNode,
    TransmissionProvider_OfferedBy_TreeNode,
    TransmissionProvider_SoldBy_TreeNode,
    GenerationProvider_TreeNode,
    GenerationProvider_GeneratingUnits_TreeNode,
    GenerationProvider_EnergyProducts_TreeNode,
    GenerationProvider_ServicePoint_TreeNode,
    OpenAccessProduct_TreeNode,
    OpenAccessProduct_ProvidedBy_TransmissionService_TreeNode,
    OpenAccessProduct_AncillaryServices_TreeNode,
    IntSchedAgreement_TreeNode,
    IntSchedAgreement_Organisations_TreeNode,
    ControlAreaOperator_TreeNode,
    ControlAreaOperator_AncillaryService_TreeNode,
    ControlAreaOperator_TieLines_TreeNode,
    FailureEvent_TreeNode,
    SwitchInfo_TreeNode,
    SwitchInfo_SwitchAssets_TreeNode,
    RecloserInfo_TreeNode,
    RecloserInfo_RecloserAssetModels_TreeNode,
    RecloserInfo_RecloserAssets_TreeNode,
    CurrentTransformerInfo_TreeNode,
    CurrentTransformerInfo_CurrentTransformerAssets_TreeNode,
    CurrentTransformerInfo_CurrentTransformerAssertModels_TreeNode,
    ProcedureDataSet_TreeNode,
    ProcedureDataSet_Properties_TreeNode,
    ProcedureDataSet_MeasurementValues_TreeNode,
    ProcedureDataSet_TransformerObservations_TreeNode,
    Facility_TreeNode,
    Structure_TreeNode,
    Structure_StructureSupports_TreeNode,
    AssetAssetRole_TreeNode,
    TestDataSet_TreeNode,
    ShuntImpedanceInfo_TreeNode,
    ShuntImpedanceInfo_ShuntCompensatorAssets_TreeNode,
    Procedure_TreeNode,
    Procedure_CompatibleUnits_TreeNode,
    Procedure_ProcedureDataSets_TreeNode,
    Procedure_ProcedureValues_TreeNode,
    Procedure_Limits_TreeNode,
    PotentialTransformerInfo_TreeNode,
    PotentialTransformerInfo_PotentialTransformerAssets_TreeNode,
    PotentialTransformerInfo_PotentialTransformerAssetModels_TreeNode,
    AssetPsrRole_TreeNode,
    DocAssetRole_TreeNode,
    SubstationAsset_TreeNode,
    SVCInfo_TreeNode,
    SVCInfo_SVCTypeAssets_TreeNode,
    Specification_TreeNode,
    Specification_AssetProperites_TreeNode,
    Specification_QualificationRequirements_TreeNode,
    Specification_Ratings_TreeNode,
    Specification_DimensionsInfos_TreeNode,
    Specification_ReliabilityInfos_TreeNode,
    Specification_Mediums_TreeNode,
    Specification_AssetPropertyCurves_TreeNode,
    ComEquipmentAsset_TreeNode,
    ComEquipmentAsset_DeviceFunctions_TreeNode,
    Cabinet_TreeNode,
    OrgAssetRole_TreeNode,
    ElectricalAssetModel_TreeNode,
    ElectricalAssetModel_ElectricalInfos_TreeNode,
    ComFunctionAssetModel_TreeNode,
    SwitchAssetModel_TreeNode,
    SwitchAssetModel_SwitchAssets_TreeNode,
    VehicleAssetModel_TreeNode,
    VehicleAssetModel_Vehicles_TreeNode,
    MeterAssetModel_TreeNode,
    MeterAssetModel_MeterAssets_TreeNode,
    FACTSDeviceAssetModel_TreeNode,
    FACTSDeviceAssetModel_FACTSDeviceAssets_TreeNode,
    WorkEquipmentAssetModel_TreeNode,
    WorkEquipmentAssetModel_WorkEquipmentAssets_TreeNode,
    RecloserAssetModel_TreeNode,
    RecloserAssetModel_RecloserAssets_TreeNode,
    AssetModelCatalogueItem_TreeNode,
    AssetModelCatalogueItem_ErpQuoteLineItems_TreeNode,
    AssetModelCatalogueItem_ErpPOLineItems_TreeNode,
    ShuntCompensatorAssetModel_TreeNode,
    ShuntCompensatorAssetModel_ShuntCompensatorAssets_TreeNode,
    SVCAssetModel_TreeNode,
    SVCAssetModel_SVCAssets_TreeNode,
    BreakerAssetModel_TreeNode,
    BreakerAssetModel_BreakerAssets_TreeNode,
    GeneratorAssetModel_TreeNode,
    GeneratorAssetModel_GeneratorAssets_TreeNode,
    ToolAssetModel_TreeNode,
    ToolAssetModel_Tools_TreeNode,
    ResistorAssetModel_TreeNode,
    ResistorAssetModel_ResistorAssets_TreeNode,
    TapChangerAssetModel_TreeNode,
    TapChangerAssetModel_TapChangerAssets_TreeNode,
    SurgeProtectorAssetModel_TreeNode,
    SurgeProtectorAssetModel_SurgeProtectorAssets_TreeNode,
    CabinetModel_TreeNode,
    CabinetModel_Cabinets_TreeNode,
    CompositeSwitchAssetModel_TreeNode,
    CompositeSwitchAssetModel_CompositeSwitchAssets_TreeNode,
    ProtectionEquipmentAssetModel_TreeNode,
    ProtectionEquipmentAssetModel_ProtectionEquipmentAssets_TreeNode,
    PotentialTransformerAssetModel_TreeNode,
    PotentialTransformerAssetModel_PotentialTransformerAssets_TreeNode,
    BushingModel_TreeNode,
    CurrentTransformerAssetModel_TreeNode,
    CurrentTransformerAssetModel_CurrentTransformerAssets_TreeNode,
    FaultIndicatorAssetModel_TreeNode,
    FaultIndicatorAssetModel_FaultIndicatorAssets_TreeNode,
    StreetlightAssetModel_TreeNode,
    StreetlightAssetModel_Streetlights_TreeNode,
    StreetlightAssetModel_StreetlightTypeAssets_TreeNode,
    SeriesCompensatorAssetModel_TreeNode,
    BusbarAssetModel_TreeNode,
    BusbarAssetModel_BusbarAssets_TreeNode,
    EnergyTransaction_TreeNode,
    EnergyTransaction_CurtailmentProfiles_TreeNode,
    EnergyTransaction_EnergyTransId_TreeNode,
    EnergyTransaction_EnergyPriceCurves_TreeNode,
    EnergyTransaction_LossProfiles_TreeNode,
    EnergyTransaction_EnergyProfiles_TreeNode,
    Reserve_TreeNode,
    Reserve_AreaReserveSpec_TreeNode,
    Block_TreeNode,
    Dynamic_TreeNode,
    Dynamic_TieLines_TreeNode,
    EnergyProduct_TreeNode,
    EnergyProduct_ServicePoint_TreeNode,
    EnergyProduct_EnergyTransactions_TreeNode,
    EnergyProduct_ResoldBy_Marketers_TreeNode,
    Skill_TreeNode,
    Skill_Crafts_TreeNode,
    Skill_QualificationRequirements_TreeNode,
    BankAccount_TreeNode,
    BankAccount_BankStatements_TreeNode,
    Diagram_TreeNode,
    Diagram_GmlDiagramObjects_TreeNode,
    Diagram_DesignLocations_TreeNode,
    Map_TreeNode,
    BusinessPlan_TreeNode,
    MarketFactors_TreeNode,
    MarketFactors_ErpInvoices_TreeNode,
    Settlement_TreeNode,
    Settlement_ErpLedgerEntries_TreeNode,
    Settlement_ErpInvoiceLineItems_TreeNode,
    LossPenaltyFactor_TreeNode,
    LossPenaltyFactor_ConnectivityNodes_TreeNode,
    PnodeClearing_TreeNode,
    MarketStatement_TreeNode,
    MarketStatement_MarketStatementLineItem_TreeNode,
    Bid_TreeNode,
    Bid_ProductBids_TreeNode,
    PassThroughBill_TreeNode,
    PassThroughBill_UserAttributes_TreeNode,
    PassThroughBill_ChargeProfiles_TreeNode,
    SchedulingCoordinator_TreeNode,
    MarketCaseClearing_TreeNode,
    MarketCaseClearing_AncillaryServiceClearing_TreeNode,
    AncillaryServiceClearing_TreeNode,
    FTR_TreeNode,
    FTR_Pnodes_TreeNode,
    ProductBidClearing_TreeNode,
    ProductBidClearing_ProductBids_TreeNode,
    SecurityConstraintsClearing_TreeNode,
    RTO_TreeNode,
    RTO_Pnodes_TreeNode,
    RTO_SecurityConstraints_TreeNode,
    RTO_SecurityConstraintsLinear_TreeNode,
    RTO_ResourceGroupReqs_TreeNode,
    RTO_Markets_TreeNode,
    BillDeterminant_TreeNode,
    BillDeterminant_ChargeProfileData_TreeNode,
    BillDeterminant_UserAttributes_TreeNode,
    SecurityConstraintSum_TreeNode,
    SecurityConstraintSum_ConstraintTerms_TreeNode,
    SecurityConstraintSum_ContingencyConstraintLimits_TreeNode,
    OperationalRestriction_TreeNode,
    SafetyDocument_TreeNode,
    SafetyDocument_ScheduleSteps_TreeNode,
    SafetyDocument_ClearanceTags_TreeNode,
    ComplianceEvent_TreeNode,
    PSREvent_TreeNode,
    OutageRecord_TreeNode,
    OutageRecord_OutageCodes_TreeNode,
    OutageRecord_OutageSteps_TreeNode,
    OutageNotification_TreeNode,
    OutageNotification_CustomerDatas_TreeNode,
    SwitchingSchedule_TreeNode,
    SwitchingSchedule_ScheduleSteps_TreeNode,
    SwitchingSchedule_Crews_TreeNode,
    PlannedOutage_TreeNode,
    PlannedOutage_CustomerDatas_TreeNode,
    PlannedOutage_OutageSchedules_TreeNode,
    TroubleTicket_TreeNode,
    TroubleTicket_CallBacks_TreeNode,
    IncidentRecord_TreeNode,
    IncidentRecord_IncidentCodes_TreeNode,
    IncidentRecord_TroubleTickets_TreeNode,
    OutageReport_TreeNode,
    LandBase_TreeNode,
    TypeAsset_TreeNode,
    TypeAsset_AssetModels_TreeNode,
    TypeAsset_ErpInventoryIssues_TreeNode,
    TypeAsset_ErpReqLineItems_TreeNode,
    TypeAsset_ErpBomItemDatas_TreeNode,
    ElectricalTypeAsset_TreeNode,
    ElectricalTypeAsset_ElectricalInfos_TreeNode,
    ShuntCompensatorTypeAsset_TreeNode,
    ShuntCompensatorTypeAsset_ShuntCompensatorAssetModels_TreeNode,
    EndDeviceTypeAsset_TreeNode,
    EndDeviceTypeAsset_EndDeviceModels_TreeNode,
    BusbarTypeAsset_TreeNode,
    BusbarTypeAsset_BusbarTypeAssets_TreeNode,
    WorkEquipmentTypeAsset_TreeNode,
    WorkEquipmentTypeAsset_WorkEquipmentAssetModels_TreeNode,
    SwitchTypeAsset_TreeNode,
    SwitchTypeAsset_SwitchAssetModels_TreeNode,
    StructureTypeAsset_TreeNode,
    StructureTypeAsset_MountConnections_TreeNode,
    TowerTypeAsset_TreeNode,
    TowerTypeAsset_TowerAssetModels_TreeNode,
    StreetlightTypeAsset_TreeNode,
    StreetlightTypeAsset_StreetlightAssetModels_TreeNode,
    ToolTypeAsset_TreeNode,
    ToolTypeAsset_ToolAssetModels_TreeNode,
    CompositeSwitchTypeAsset_TreeNode,
    CompositeSwitchTypeAsset_CompositeSwitchAssetModels_TreeNode,
    CompositeSwitchTypeAsset_SwitchTypesAssets_TreeNode,
    FACTSDeviceTypeAsset_TreeNode,
    FACTSDeviceTypeAsset_FACTSDeviceAssetModels_TreeNode,
    SVCTypeAsset_TreeNode,
    SVCTypeAsset_SvcInfos_TreeNode,
    SVCTypeAsset_SVCAssetModels_TreeNode,
    ResistorTypeAsset_TreeNode,
    ResistorTypeAsset_ResistorAssetModels_TreeNode,
    ResistorTypeAsset_Resistors_TreeNode,
    SeriesCompensatorTypeAsset_TreeNode,
    SeriesCompensatorTypeAsset_ShuntCompensatorAssetModels_TreeNode,
    FaultIndicatorTypeAsset_TreeNode,
    FaultIndicatorTypeAsset_FaultIndicatorAssetModels_TreeNode,
    FaultIndicatorTypeAsset_FaultIndicators_TreeNode,
    BreakerTypeAsset_TreeNode,
    BreakerTypeAsset_BreakerAssetModels_TreeNode,
    PoleTypeAsset_TreeNode,
    PoleTypeAsset_PoleModels_TreeNode,
    DuctTypeAsset_TreeNode,
    DuctTypeAsset_CableAssets_TreeNode,
    SurgeProtectorTypeAsset_TreeNode,
    SurgeProtectorTypeAsset_SurgeProtectors_TreeNode,
    SurgeProtectorTypeAsset_SurgeProtectorAssetModels_TreeNode,
    ComFunctionTypeAsset_TreeNode,
    ComFunctionTypeAsset_ComFunctionAssetModels_TreeNode,
    ProtectionEquipmentTypeAsset_TreeNode,
    ProtectionEquipmentTypeAsset_ProtectionEquipmentAssetModels_TreeNode,
    CabinetTypeAsset_TreeNode,
    CabinetTypeAsset_CabinetModels_TreeNode,
    MeterTypeAsset_TreeNode,
    MeterTypeAsset_MeterAssetModels_TreeNode,
    GeneratorTypeAsset_TreeNode,
    GeneratorTypeAsset_GeneratorAssetModels_TreeNode,
    PotentialTransformerTypeAsset_TreeNode,
    PotentialTransformerTypeAsset_PotentialTransformers_TreeNode,
    PotentialTransformerTypeAsset_PotentialTransformerAssetModels_TreeNode,
    RecloserTypeAsset_TreeNode,
    RecloserTypeAsset_RecloserAssetModels_TreeNode,
    CurrentTransformerTypeAsset_TreeNode,
    CurrentTransformerTypeAsset_CurrentTransformerAssetModels_TreeNode,
    CurrentTransformerTypeAsset_CurrentTransformers_TreeNode,
    DuctBankTypeAsset_TreeNode,
    DuctBankTypeAsset_DuctTypeAssets_TreeNode,
    DuctBankTypeAsset_DuctBanks_TreeNode,
    ExternalCustomerAgreement_TreeNode,
    StandardIndustryCode_TreeNode,
    StandardIndustryCode_CustomerAgreements_TreeNode,
    CustomerBillingInfo_TreeNode,
    CustomerBillingInfo_ErpInvoiceLineItems_TreeNode,
    OutageHistory_TreeNode,
    OutageHistory_OutageReports_TreeNode,
    WorkBillingInfo_TreeNode,
    WorkBillingInfo_ErpLineItems_TreeNode,
    WorkBillingInfo_Works_TreeNode,
    PowerQualityPricing_TreeNode,
    PowerQualityPricing_ServiceDeliveryPoints_TreeNode,
    ServiceGuarantee_TreeNode,
    LoadMgmtFunction_TreeNode,
    LoadMgmtFunction_Switches_TreeNode,
    LoadMgmtFunction_LoadMgmtRecords_TreeNode,
    LoadLimitFunction_TreeNode,
    LoadMgmtRecord_TreeNode,
    LoadShedFunction_TreeNode,
    WaterMeteringFunction_TreeNode,
    GasMeteringFunction_TreeNode,
    MaintenanceDataSet_TreeNode,
    InspectionDataSet_TreeNode,
    InspectionDataSet_AccordingToSchedules_TreeNode,
    DiagnosisDataSet_TreeNode,
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  CIM Tree Editor:
#------------------------------------------------------------------------------

CIMTreeEditor = TreeEditor(nodes=tree_nodes, editable=True)

#------------------------------------------------------------------------------
#  Begin "CIMTreeEditor" user region:
#------------------------------------------------------------------------------
# @generated
class TreeRoot(HasTraits):

    # Root element of the model tree.
    root = Instance(HasTraits)

    # Traits view to display.
    view = View(
        Item('root',
            editor=CIMTreeEditor,
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

#------------------------------------------------------------------------------
#  End "CIMTreeEditor" user region:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    root = TreeRoot()
    root.configure_traits()

# EOF -------------------------------------------------------------------------
