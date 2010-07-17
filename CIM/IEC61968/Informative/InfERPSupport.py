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

""" The package contains portions of the model defined byEnterprise Resource Planning (ERP) standards like those proposed by the Open Applications Group (OAG). It is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (as defined by OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeld 'Erp...' should be associated with the appropriate classes of that standard. In fact, definitions of 'Erp...' classes are based on OAG Nouns to facilitate this process.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Enterprise Resource Planning (ERP) Support Package contains portions of the model defined by ERP standards like those proposed by the Open Applications Group (OAG). This package is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeled 'Erp...' should be associated with the appropriate classes of that standard.'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Organisation
from CIM.IEC61968.Informative.InfCommon import Role
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Informative.InfCommon import BankAccount
from CIM.IEC61968.Common import TelephoneNumber
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import Money



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Int, Date, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of ERP account.
ErpAccountKind = Enum("estimate", "reversal", "statistical", "normal", desc="Kind of ERP account.")
# Kind of ERP invoice.
ErpInvoiceKind = Enum("sales", "purchase", desc="Kind of ERP invoice.")
# Kind of bill media.
BillMediaKind = Enum("other", "paper", "electronic", desc="Kind of bill media.")
# Kind of invoice line item.
ErpInvoiceLineItemKind = Enum("recalculation", "initial", "other", desc="Kind of invoice line item.")

#------------------------------------------------------------------------------
#  "ErpIssueInventory" class:
#------------------------------------------------------------------------------

class ErpIssueInventory(IdentifiedObject):
    """ Can be used to request an application to process an issue or request information about an issue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    TypeMaterial = Instance("CIM.IEC61968.Informative.InfWork.TypeMaterial",
        transient=True,
        opposite="ErpIssueInventories",
        editor=InstanceEditor(name="_typematerials"))

    def _get_typematerials(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.TypeMaterial" ]
        else:
            return []

    _typematerials = Property(fget=_get_typematerials)

    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        transient=True,
        opposite="ErpInventoryIssues",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    #--------------------------------------------------------------------------
    #  Begin "ErpIssueInventory" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "TypeMaterial", "TypeAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpIssueInventory",
        title="ErpIssueInventory",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpIssueInventory" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpOrganisation" class:
#------------------------------------------------------------------------------

class ErpOrganisation(Organisation):
    """ Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DocumentRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.DocOrgRole"))

    ActivityRecords = List(Instance("CIM.IEC61968.Common.ActivityRecord"))

    LocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.OrgLocRole"))

    ErpPersonRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.OrgErpPersonRole"))

    ViolationLimits = List(Instance("CIM.IEC61968.Informative.MarketOperations.ViolationLimit"))

    Requests = List(Instance("CIM.IEC61968.Informative.InfWork.Request"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    IntSchedAgreement = List(Instance("CIM.IEC61968.Informative.Financial.IntSchedAgreement"))

    RegisteredResources = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource"))

    PowerSystemResourceRoles = List(Instance("CIM.IEC61968.Informative.InfOperations.OrgPsrRole"))

    AssetRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.OrgAssetRole"))

    LandPropertyRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.OrgPropertyRole"))

    ParentOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.OrgOrgRole"))

    ChildOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.OrgOrgRole"))

    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"))

    # Designated code for organisation.
    code = Str(desc="Designated code for organisation.")

    # Category by utility's corporate standards and practices.
    category = Str(desc="Category by utility's corporate standards and practices.")

    # Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition).
    mode = Str(desc="Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition).")

    # True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation.
    optOut = Bool(desc="True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation.")

    # Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location.
    industryID = Str(desc="Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location.")

    # True if organisation is profit center.
    isProfitCenter = Bool(desc="True if organisation is profit center.")

    # True if organisation is cost center.
    isCostCenter = Bool(desc="True if organisation is cost center.")

    # Unique identifier for organisation relative to its governing authority, for example a federal tax identifier.
    governmentID = Str(desc="Unique identifier for organisation relative to its governing authority, for example a federal tax identifier.")

    #--------------------------------------------------------------------------
    #  Begin "ErpOrganisation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        title="ErpOrganisation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpOrganisation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocErpPersonRole" class:
#------------------------------------------------------------------------------

class DocErpPersonRole(Role):
    """ Roles played between Persons and Documents.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="DocumentRoles",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ErpPersonRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    #--------------------------------------------------------------------------
    #  Begin "DocErpPersonRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpPerson", "Document",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.DocErpPersonRole",
        title="DocErpPersonRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocErpPersonRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPayableLineItem" class:
#------------------------------------------------------------------------------

class ErpPayableLineItem(IdentifiedObject):
    """ Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as credit memos.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpJournalEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    ErpPayments = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayment"))

    ErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        transient=True,
        opposite="ErpPayableLineItem",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    ErpPayable = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayable",
        transient=True,
        opposite="ErpPayableLineItems",
        editor=InstanceEditor(name="_erppayables"))

    def _get_erppayables(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPayable" ]
        else:
            return []

    _erppayables = Property(fget=_get_erppayables)

    #--------------------------------------------------------------------------
    #  Begin "ErpPayableLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpJournalEntries", "status", "ErpPayments", "ErpInvoiceLineItem", "ErpPayable",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem",
        title="ErpPayableLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPayableLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgOrgRole" class:
#------------------------------------------------------------------------------

class OrgOrgRole(Role):
    """ Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ChildOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="ParentOrganisationRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    ParentOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="ChildOrganisationRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    # Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc.
    clientID = Str(desc="Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc.")

    #--------------------------------------------------------------------------
    #  Begin "OrgOrgRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category", "clientID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ChildOrganisation", "ParentOrganisation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.OrgOrgRole",
        title="OrgOrgRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgOrgRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpReqLineItem" class:
#------------------------------------------------------------------------------

class ErpReqLineItem(IdentifiedObject):
    """ Information that describes a requested item and its attributes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpRequisition = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRequisition",
        transient=True,
        opposite="ErpReqLineItems",
        editor=InstanceEditor(name="_erprequisitions"))

    def _get_erprequisitions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpRequisition" ]
        else:
            return []

    _erprequisitions = Property(fget=_get_erprequisitions)

    TypeMaterial = Instance("CIM.IEC61968.Informative.InfWork.TypeMaterial",
        transient=True,
        opposite="ErpReqLineItems",
        editor=InstanceEditor(name="_typematerials"))

    def _get_typematerials(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.TypeMaterial" ]
        else:
            return []

    _typematerials = Property(fget=_get_typematerials)

    ErpPOLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem",
        transient=True,
        opposite="ErpReqLineItem",
        editor=InstanceEditor(name="_erppolineitems"))

    def _get_erppolineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem" ]
        else:
            return []

    _erppolineitems = Property(fget=_get_erppolineitems)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    ErpQuoteLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem",
        transient=True,
        opposite="ErpReqLineItem",
        editor=InstanceEditor(name="_erpquotelineitems"))

    def _get_erpquotelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem" ]
        else:
            return []

    _erpquotelineitems = Property(fget=_get_erpquotelineitems)

    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        transient=True,
        opposite="ErpReqLineItems",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    deliveryDate = AbsoluteDate

    code = Str

    # Quantity of item requisitioned.
    quantity = Int(desc="Quantity of item requisitioned.")

    # Cost of material
    cost = Money(desc="Cost of material")

    #--------------------------------------------------------------------------
    #  Begin "ErpReqLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "deliveryDate", "code", "quantity", "cost",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpRequisition", "TypeMaterial", "ErpPOLineItem", "status", "ErpQuoteLineItem", "TypeAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem",
        title="ErpReqLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpReqLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpLedger" class:
#------------------------------------------------------------------------------

class ErpLedger(Document):
    """ In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpLedgerEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry"))

    #--------------------------------------------------------------------------
    #  Begin "ErpLedger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpLedgerEntries",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpLedger",
        title="ErpLedger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpLedger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocOrgRole" class:
#------------------------------------------------------------------------------

class DocOrgRole(Role):
    """ Roles played between Organisations and Documents.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="DocumentRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ErpOrganisationRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    #--------------------------------------------------------------------------
    #  Begin "DocOrgRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpOrganisation", "Document",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.DocOrgRole",
        title="DocOrgRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocOrgRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpInventory" class:
#------------------------------------------------------------------------------

class ErpInventory(IdentifiedObject):
    """ Utility inventory-related information about an item or part (and not for description of the item and its attributes). It is used by ERP applications to enable the synchronization of Inventory data that exists on separate Item Master databases. This data is not the master data that describes the attributes of the item such as dimensions, weight, or unit of measure - it describes the item as it exists at a specific location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="ErpInventory",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpInventory" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpInventory",
        title="ErpInventory",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpInventory" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpJournal" class:
#------------------------------------------------------------------------------

class ErpJournal(Document):
    """ Book for recording accounting transactions as they occur. Transactions and adjustments are first recorded in a journal, which is like a diary of instructions, advising which account to be charged and by how much. A journal represents a change in the balances of a business's financial accounts. Many tasks or transactions throughout an enterprise will result in the creation of a journal. Some examples are creating a customer invoice, paying a vendor, transferring inventory, or paying employees.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpJournalEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry"))

    #--------------------------------------------------------------------------
    #  Begin "ErpJournal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpJournalEntries",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpJournal",
        title="ErpJournal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpJournal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpProjectAccounting" class:
#------------------------------------------------------------------------------

class ErpProjectAccounting(Document):
    """ Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Projects = List(Instance("CIM.IEC61968.Informative.InfWork.Project"))

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    ErpTimeEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpTimeEntry"))

    #--------------------------------------------------------------------------
    #  Begin "ErpProjectAccounting" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Projects", "WorkCostDetails", "Works", "ErpTimeEntries",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting",
        title="ErpProjectAccounting",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpProjectAccounting" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpQuoteLineItem" class:
#------------------------------------------------------------------------------

class ErpQuoteLineItem(IdentifiedObject):
    """ Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AssetModelCatalogueItem = Instance("CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem",
        transient=True,
        opposite="ErpQuoteLineItems",
        editor=InstanceEditor(name="_assetmodelcatalogueitems"))

    def _get_assetmodelcatalogueitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem" ]
        else:
            return []

    _assetmodelcatalogueitems = Property(fget=_get_assetmodelcatalogueitems)

    Design = Instance("CIM.IEC61968.Informative.InfWork.Design",
        transient=True,
        opposite="ErpQuoteLineItem",
        editor=InstanceEditor(name="_designs"))

    def _get_designs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Design" ]
        else:
            return []

    _designs = Property(fget=_get_designs)

    Request = Instance("CIM.IEC61968.Informative.InfWork.Request",
        transient=True,
        opposite="ErpQuoteLineItem",
        editor=InstanceEditor(name="_requests"))

    def _get_requests(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Request" ]
        else:
            return []

    _requests = Property(fget=_get_requests)

    ErpReqLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem",
        transient=True,
        opposite="ErpQuoteLineItem",
        editor=InstanceEditor(name="_erpreqlineitems"))

    def _get_erpreqlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem" ]
        else:
            return []

    _erpreqlineitems = Property(fget=_get_erpreqlineitems)

    # Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
    ErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        desc="Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.",
        transient=True,
        opposite="ErpQuoteLineItem",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    ErpQuote = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuote",
        transient=True,
        opposite="ErpQuoteLineItems",
        editor=InstanceEditor(name="_erpquotes"))

    def _get_erpquotes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpQuote" ]
        else:
            return []

    _erpquotes = Property(fget=_get_erpquotes)

    #--------------------------------------------------------------------------
    #  Begin "ErpQuoteLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "AssetModelCatalogueItem", "Design", "Request", "ErpReqLineItem", "ErpInvoiceLineItem", "status", "ErpQuote",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem",
        title="ErpQuoteLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpQuoteLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPerson" class:
#------------------------------------------------------------------------------

class ErpPerson(IdentifiedObject):
    """ General purpose information for name and other information to contact people.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpTelephoneNumbers = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpTelephoneNumber"))

    DocumentRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.DocErpPersonRole"))

    ElectronicAddresses = List(Instance("CIM.IEC61968.Common.ElectronicAddress"))

    # All Crews to which this ErpPerson belongs.
    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"),
        desc="All Crews to which this ErpPerson belongs.")

    Appointments = List(Instance("CIM.IEC61968.Informative.InfWork.Appointment"))

    LaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.LaborItem"))

    MeasurementValues = List(Instance("CIM.IEC61970.Meas.MeasurementValue"))

    CallBacks = List(Instance("CIM.IEC61968.Informative.InfOperations.CallBack"))

    ActivityRecords = List(Instance("CIM.IEC61968.Common.ActivityRecord"))

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.OrgErpPersonRole"))

    Crafts = List(Instance("CIM.IEC61968.Informative.InfCommon.Craft"))

    LocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.ErpPersonLocRole"))

    Skills = List(Instance("CIM.IEC61968.Informative.InfCommon.Skill"))

    CustomerData = Instance("CIM.IEC61968.Customers.Customer",
        transient=True,
        opposite="ErpPersons",
        editor=InstanceEditor(name="_customers"))

    def _get_customers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.Customer" ]
        else:
            return []

    _customers = Property(fget=_get_customers)

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    SwitchingStepRoles = List(Instance("CIM.IEC61968.Informative.InfOperations.ErpPersonScheduleStepRole"))

    ErpPersonnel = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPersonnel",
        transient=True,
        opposite="ErpPersons",
        editor=InstanceEditor(name="_erppersonnels"))

    def _get_erppersonnels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPersonnel" ]
        else:
            return []

    _erppersonnels = Property(fget=_get_erppersonnels)

    ErpCompetency = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpCompetency",
        transient=True,
        opposite="ErpPersons",
        editor=InstanceEditor(name="_erpcompetencys"))

    def _get_erpcompetencys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpCompetency" ]
        else:
            return []

    _erpcompetencys = Property(fget=_get_erpcompetencys)

    LandPropertyRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.PersonPropertyRole"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.
    prefix = Str(desc="A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.")

    # Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States).
    governmentID = Str(desc="Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States).")

    # Person's last (family, sir) name.
    lastName = Str(desc="Person's last (family, sir) name.")

    # Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations.
    category = Str(desc="Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations.")

    # Person's first name.
    firstName = Str(desc="Person's first name.")

    # A suffix for the person's name, such as II, III, etc.
    suffix = Str(desc="A suffix for the person's name, such as II, III, etc.")

    # Special service needs for the person (contact) are described; examples include life support, etc.
    specialNeed = Str(desc="Special service needs for the person (contact) are described; examples include life support, etc.")

    # Middle name(s) or initial(s).
    mName = Str(desc="Middle name(s) or initial(s).")

    #--------------------------------------------------------------------------
    #  Begin "ErpPerson" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "prefix", "governmentID", "lastName", "category", "firstName", "suffix", "specialNeed", "mName",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ErpTelephoneNumbers", "DocumentRoles", "ElectronicAddresses", "Crews", "Appointments", "LaborItems", "MeasurementValues", "CallBacks", "ActivityRecords", "ErpOrganisationRoles", "Crafts", "LocationRoles", "Skills", "CustomerData", "ChangeItems", "SwitchingStepRoles", "ErpPersonnel", "ErpCompetency", "LandPropertyRoles", "status",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        title="ErpPerson",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPerson" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpRecDelvLineItem" class:
#------------------------------------------------------------------------------

class ErpRecDelvLineItem(IdentifiedObject):
    """ Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    ErpPOLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem",
        transient=True,
        opposite="ErpRecDelLineItem",
        editor=InstanceEditor(name="_erppolineitems"))

    def _get_erppolineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem" ]
        else:
            return []

    _erppolineitems = Property(fget=_get_erppolineitems)

    ErpReceiveDelivery = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReceiveDelivery",
        transient=True,
        opposite="ErpRecDelvLineItems",
        editor=InstanceEditor(name="_erpreceivedeliverys"))

    def _get_erpreceivedeliverys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpReceiveDelivery" ]
        else:
            return []

    _erpreceivedeliverys = Property(fget=_get_erpreceivedeliverys)

    MaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.MaterialItem"))

    ErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        transient=True,
        opposite="ErpRecDelvLineItem",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    #--------------------------------------------------------------------------
    #  Begin "ErpRecDelvLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpPOLineItem", "ErpReceiveDelivery", "MaterialItems", "ErpInvoiceLineItem", "Assets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem",
        title="ErpRecDelvLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpRecDelvLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpBankAccount" class:
#------------------------------------------------------------------------------

class ErpBankAccount(BankAccount):
    """ Relationship under a particular name, usually evidenced by a deposit against which withdrawals can be made. Types of bank accounts include: demand, time, custodial, joint, trustee, corporate, special, and regular accounts. A statement of transactions during a fiscal period and the resulting balance is maintained on each account. For Payment metering, the account is associated with Bank and Supplier, reflecting details of the bank account used for depositing revenue collected by TokenVendor. The name of the account holder should be specified in 'name' attribute.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Bank ABA.
    bankABA = Str(desc="Bank ABA.")

    #--------------------------------------------------------------------------
    #  Begin "ErpBankAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "accountNumber", "bankABA",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ServiceSupplier", "Bank", "BankStatements",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpBankAccount",
        title="ErpBankAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpBankAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPurchaseOrder" class:
#------------------------------------------------------------------------------

class ErpPurchaseOrder(Document):
    """ A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPOLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpPurchaseOrder" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpPOLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPurchaseOrder",
        title="ErpPurchaseOrder",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPurchaseOrder" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpInvoice" class:
#------------------------------------------------------------------------------

class ErpInvoice(Document):
    """ A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CustomerAccount = Instance("CIM.IEC61968.Customers.CustomerAccount",
        transient=True,
        opposite="ErpInvoicees",
        editor=InstanceEditor(name="_customeraccounts"))

    def _get_customeraccounts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAccount" ]
        else:
            return []

    _customeraccounts = Property(fget=_get_customeraccounts)

    ErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    # Kind of media by which the CustomerBillingInfo was delivered.
    billMediaKind = BillMediaKind(desc="Kind of media by which the CustomerBillingInfo was delivered.")

    # Kind of invoice (default is 'sales').
    kind = ErpInvoiceKind(desc="Kind of invoice (default is 'sales').")

    # Total amount due on this invoice based on line items and applicable adjustments.
    amount = Money(desc="Total amount due on this invoice based on line items and applicable adjustments.")

    # True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote.
    proForma = Bool(desc="True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote.")

    # Date and time when the invoice is issued.
    transactionDateTime = Date(desc="Date and time when the invoice is issued.")

    # Date on which the customer billing statement/invoice was printed/mailed.
    mailedDate = AbsoluteDate(desc="Date on which the customer billing statement/invoice was printed/mailed.")

    # Calculated date upon which the Invoice amount is due.
    dueDate = AbsoluteDate(desc="Calculated date upon which the Invoice amount is due.")

    # Type of invoice transfer.
    transferType = Str(desc="Type of invoice transfer.")

    # Number of an invoice to be reference by this invoice.
    referenceNumber = Str(desc="Number of an invoice to be reference by this invoice.")

    #--------------------------------------------------------------------------
    #  Begin "ErpInvoice" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "billMediaKind", "kind", "amount", "proForma", "transactionDateTime", "mailedDate", "dueDate", "transferType", "referenceNumber",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CustomerAccount", "ErpInvoiceLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpInvoice",
        title="ErpInvoice",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpInvoice" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpBomItemData" class:
#------------------------------------------------------------------------------

class ErpBomItemData(IdentifiedObject):
    """ An individual item on a bill of materials.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DesignLocation = Instance("CIM.IEC61968.Informative.InfWork.DesignLocation",
        transient=True,
        opposite="ErpBomItemDatas",
        editor=InstanceEditor(name="_designlocations"))

    def _get_designlocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.DesignLocation" ]
        else:
            return []

    _designlocations = Property(fget=_get_designlocations)

    ErpBOM = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpBOM",
        transient=True,
        opposite="ErpBomItemDatas",
        editor=InstanceEditor(name="_erpboms"))

    def _get_erpboms(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpBOM" ]
        else:
            return []

    _erpboms = Property(fget=_get_erpboms)

    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        transient=True,
        opposite="ErpBomItemDatas",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    #--------------------------------------------------------------------------
    #  Begin "ErpBomItemData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DesignLocation", "ErpBOM", "TypeAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpBomItemData",
        title="ErpBomItemData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpBomItemData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpItemMaster" class:
#------------------------------------------------------------------------------

class ErpItemMaster(IdentifiedObject):
    """ Any unique purchased part for manufactured product tracked by ERP systems for a utility. Item, as used by the OAG, refers to the basic information about an item, including its attributes, cost, and locations. It does not include item quantities. Compare to the Inventory, which includes all quantities and other location-specific information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="ErpItemMaster",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpItemMaster" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpItemMaster",
        title="ErpItemMaster",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpItemMaster" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpInventoryCount" class:
#------------------------------------------------------------------------------

class ErpInventoryCount(IdentifiedObject):
    """ This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AssetModel = Instance("CIM.IEC61968.AssetModels.AssetModel",
        transient=True,
        opposite="ErpInventoryCounts",
        editor=InstanceEditor(name="_assetmodels"))

    def _get_assetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.AssetModel" ]
        else:
            return []

    _assetmodels = Property(fget=_get_assetmodels)

    MaterialItem = Instance("CIM.IEC61968.Informative.InfWork.MaterialItem",
        transient=True,
        opposite="ErpInventoryCounts",
        editor=InstanceEditor(name="_materialitems"))

    def _get_materialitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.MaterialItem" ]
        else:
            return []

    _materialitems = Property(fget=_get_materialitems)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpInventoryCount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "AssetModel", "MaterialItem", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpInventoryCount",
        title="ErpInventoryCount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpInventoryCount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpEngChangeOrder" class:
#------------------------------------------------------------------------------

class ErpEngChangeOrder(Document):
    """ General Utility Engineering Change Order information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ErpEngChangeOrder" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpEngChangeOrder",
        title="ErpEngChangeOrder",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpEngChangeOrder" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpInvoiceLineItem" class:
#------------------------------------------------------------------------------

class ErpInvoiceLineItem(Document):
    """ An individual line item on an invoice.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkBillingInfos = List(Instance("CIM.IEC61968.Informative.InfCustomers.WorkBillingInfo"))

    ErpRecLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem",
        transient=True,
        opposite="ErpInvoiceLineItem",
        editor=InstanceEditor(name="_erpreclineitems"))

    def _get_erpreclineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem" ]
        else:
            return []

    _erpreclineitems = Property(fget=_get_erpreclineitems)

    MarketFactors = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketFactors"))

    ErpJournalEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry"))

    # Bill period for the line item.
    billPeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Bill period for the line item.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    ErpRecDelvLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem",
        transient=True,
        opposite="ErpInvoiceLineItem",
        editor=InstanceEditor(name="_erprecdelvlineitems"))

    def _get_erprecdelvlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem" ]
        else:
            return []

    _erprecdelvlineitems = Property(fget=_get_erprecdelvlineitems)

    # Customer billing for services rendered.
    CustomerBillingInfos = List(Instance("CIM.IEC61968.Informative.InfCustomers.CustomerBillingInfo"),
        desc="Customer billing for services rendered.")

    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"))

    ContainerErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        transient=True,
        opposite="ComponentErpInvoiceLineItems",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    ComponentErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    ErpPayments = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayment"))

    Settlements = List(Instance("CIM.IEC61968.Informative.MarketOperations.Settlement"))

    ErpInvoice = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoice",
        transient=True,
        opposite="ErpInvoiceLineItems",
        editor=InstanceEditor(name="_erpinvoices"))

    def _get_erpinvoices(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoice" ]
        else:
            return []

    _erpinvoices = Property(fget=_get_erpinvoices)

    ErpQuoteLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem",
        transient=True,
        opposite="ErpInvoiceLineItem",
        editor=InstanceEditor(name="_erpquotelineitems"))

    def _get_erpquotelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem" ]
        else:
            return []

    _erpquotelineitems = Property(fget=_get_erpquotelineitems)

    ErpPayableLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem",
        transient=True,
        opposite="ErpInvoiceLineItem",
        editor=InstanceEditor(name="_erppayablelineitems"))

    def _get_erppayablelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem" ]
        else:
            return []

    _erppayablelineitems = Property(fget=_get_erppayablelineitems)

    # Kind of line item.
    kind = ErpInvoiceLineItemKind(desc="Kind of line item.")

    # Line item number on invoice statement.
    lineNumber = Str(desc="Line item number on invoice statement.")

    # Net line item charge amount.
    netAmount = Float(desc="Net line item charge amount.")

    # General Ledger account code, must be a valid combination.
    glAccount = Str(desc="General Ledger account code, must be a valid combination.")

    # Date and time line item will be posted to the General Ledger.
    glDateTime = Date(desc="Date and time line item will be posted to the General Ledger.")

    # Amount due for this line item.
    lineAmount = Float(desc="Amount due for this line item.")

    # Previous line item charge amount.
    previousAmount = Float(desc="Previous line item charge amount.")

    # Version number of the bill run.
    lineVersion = Str(desc="Version number of the bill run.")

    #--------------------------------------------------------------------------
    #  Begin "ErpInvoiceLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "lineNumber", "netAmount", "glAccount", "glDateTime", "lineAmount", "previousAmount", "lineVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkBillingInfos", "ErpRecLineItem", "MarketFactors", "ErpJournalEntries", "billPeriod", "ErpRecDelvLineItem", "CustomerBillingInfos", "UserAttributes", "ContainerErpInvoiceLineItem", "ComponentErpInvoiceLineItems", "ErpPayments", "Settlements", "ErpInvoice", "ErpQuoteLineItem", "ErpPayableLineItem",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        title="ErpInvoiceLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpInvoiceLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPayable" class:
#------------------------------------------------------------------------------

class ErpPayable(Document):
    """ A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ContractorItems = List(Instance("CIM.IEC61968.Informative.InfWork.ContractorItem"))

    ErpPayableLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpPayable" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ContractorItems", "ErpPayableLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPayable",
        title="ErpPayable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPayable" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPayment" class:
#------------------------------------------------------------------------------

class ErpPayment(Document):
    """ Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpRecLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem"))

    ErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    ErpPayableLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem"))

    # Payment terms (e.g., net 30).
    termsPayment = Str(desc="Payment terms (e.g., net 30).")

    #--------------------------------------------------------------------------
    #  Begin "ErpPayment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "termsPayment",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpRecLineItems", "ErpInvoiceLineItems", "ErpPayableLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPayment",
        title="ErpPayment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPayment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpQuote" class:
#------------------------------------------------------------------------------

class ErpQuote(Document):
    """ Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpQuoteLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpQuote" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpQuoteLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpQuote",
        title="ErpQuote",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpQuote" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpJournalEntry" class:
#------------------------------------------------------------------------------

class ErpJournalEntry(IdentifiedObject):
    """ Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPayableLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayableLineItem"))

    ErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        transient=True,
        opposite="ErpJournalEntries",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    ErpJournal = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournal",
        transient=True,
        opposite="ErpJournalEntries",
        editor=InstanceEditor(name="_erpjournals"))

    def _get_erpjournals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpJournal" ]
        else:
            return []

    _erpjournals = Property(fget=_get_erpjournals)

    CostTypes = List(Instance("CIM.IEC61968.Informative.InfWork.CostType"))

    ErpLedgerEntry = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry",
        transient=True,
        opposite="ErpJounalEntry",
        editor=InstanceEditor(name="_erpledgerentrys"))

    def _get_erpledgerentrys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry" ]
        else:
            return []

    _erpledgerentrys = Property(fget=_get_erpledgerentrys)

    ErpRecLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem"))

    # Date and time journal entry was recorded.
    transactionDateTime = Date(desc="Date and time journal entry was recorded.")

    # Account identifier for this entry.
    accountID = Str(desc="Account identifier for this entry.")

    # Date and time this entry is to be posted to the ledger.
    postingDateTime = Date(desc="Date and time this entry is to be posted to the ledger.")

    # The amount of the debit or credit for this account.
    amount = Money(desc="The amount of the debit or credit for this account.")

    # The identifer of the source for this entry.
    sourceID = Str(desc="The identifer of the source for this entry.")

    #--------------------------------------------------------------------------
    #  Begin "ErpJournalEntry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "transactionDateTime", "accountID", "postingDateTime", "amount", "sourceID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpPayableLineItems", "ErpInvoiceLineItem", "status", "ErpJournal", "CostTypes", "ErpLedgerEntry", "ErpRecLineItems",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry",
        title="ErpJournalEntry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpJournalEntry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPOLineItem" class:
#------------------------------------------------------------------------------

class ErpPOLineItem(Document):
    """ Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpReqLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem",
        transient=True,
        opposite="ErpPOLineItem",
        editor=InstanceEditor(name="_erpreqlineitems"))

    def _get_erpreqlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem" ]
        else:
            return []

    _erpreqlineitems = Property(fget=_get_erpreqlineitems)

    ErpRecDelLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem",
        transient=True,
        opposite="ErpPOLineItem",
        editor=InstanceEditor(name="_erprecdelvlineitems"))

    def _get_erprecdelvlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem" ]
        else:
            return []

    _erprecdelvlineitems = Property(fget=_get_erprecdelvlineitems)

    AssetModelCatalogueItem = Instance("CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem",
        transient=True,
        opposite="ErpPOLineItems",
        editor=InstanceEditor(name="_assetmodelcatalogueitems"))

    def _get_assetmodelcatalogueitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem" ]
        else:
            return []

    _assetmodelcatalogueitems = Property(fget=_get_assetmodelcatalogueitems)

    ErpPurchaseOrder = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPurchaseOrder",
        transient=True,
        opposite="ErpPOLineItems",
        editor=InstanceEditor(name="_erppurchaseorders"))

    def _get_erppurchaseorders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPurchaseOrder" ]
        else:
            return []

    _erppurchaseorders = Property(fget=_get_erppurchaseorders)

    MaterialItem = Instance("CIM.IEC61968.Informative.InfWork.MaterialItem",
        transient=True,
        opposite="ErpPOLineItems",
        editor=InstanceEditor(name="_materialitems"))

    def _get_materialitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.MaterialItem" ]
        else:
            return []

    _materialitems = Property(fget=_get_materialitems)

    #--------------------------------------------------------------------------
    #  Begin "ErpPOLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpReqLineItem", "ErpRecDelLineItem", "AssetModelCatalogueItem", "ErpPurchaseOrder", "MaterialItem",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem",
        title="ErpPOLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPOLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpReceiveDelivery" class:
#------------------------------------------------------------------------------

class ErpReceiveDelivery(Document):
    """ Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpRecDelvLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpReceiveDelivery" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpRecDelvLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpReceiveDelivery",
        title="ErpReceiveDelivery",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpReceiveDelivery" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpTimeEntry" class:
#------------------------------------------------------------------------------

class ErpTimeEntry(IdentifiedObject):
    """ An individual entry on an ErpTimeSheet.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpProjectAccounting = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting",
        transient=True,
        opposite="ErpTimeEntries",
        editor=InstanceEditor(name="_erpprojectaccountings"))

    def _get_erpprojectaccountings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting" ]
        else:
            return []

    _erpprojectaccountings = Property(fget=_get_erpprojectaccountings)

    ErpTimeSheet = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpTimeSheet",
        transient=True,
        opposite="ErpTimeEntries",
        editor=InstanceEditor(name="_erptimesheets"))

    def _get_erptimesheets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpTimeSheet" ]
        else:
            return []

    _erptimesheets = Property(fget=_get_erptimesheets)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpTimeEntry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpProjectAccounting", "ErpTimeSheet", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpTimeEntry",
        title="ErpTimeEntry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpTimeEntry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpChartOfAccounts" class:
#------------------------------------------------------------------------------

class ErpChartOfAccounts(Document):
    """ Accounting structure of a business. Each account represents a financial aspect of a business, such as its Accounts Payable, or the value of its inventory, or its office supply expenses.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ErpChartOfAccounts" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpChartOfAccounts",
        title="ErpChartOfAccounts",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpChartOfAccounts" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpLedgerBudget" class:
#------------------------------------------------------------------------------

class ErpLedgerBudget(Document):
    """ Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpLedBudLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedBudLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpLedgerBudget" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpLedBudLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpLedgerBudget",
        title="ErpLedgerBudget",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpLedgerBudget" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpRequisition" class:
#------------------------------------------------------------------------------

class ErpRequisition(Document):
    """ General information that applies to a utility requisition that is a request for the purchase of goods or services. Typically, a requisition leads to the creation of a purchase order to a specific supplier.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpReqLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpRequisition" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpReqLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpRequisition",
        title="ErpRequisition",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpRequisition" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgErpPersonRole" class:
#------------------------------------------------------------------------------

class OrgErpPersonRole(Role):
    """ Roles played between Persons and Organisations.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="ErpPersonRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="ErpOrganisationRoles",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    # Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc.
    clientID = Str(desc="Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc.")

    #--------------------------------------------------------------------------
    #  Begin "OrgErpPersonRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category", "clientID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpOrganisation", "ErpPerson",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.OrgErpPersonRole",
        title="OrgErpPersonRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgErpPersonRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpBOM" class:
#------------------------------------------------------------------------------

class ErpBOM(Document):
    """ Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Design = Instance("CIM.IEC61968.Informative.InfWork.Design",
        transient=True,
        opposite="ErpBOMs",
        editor=InstanceEditor(name="_designs"))

    def _get_designs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Design" ]
        else:
            return []

    _designs = Property(fget=_get_designs)

    ErpBomItemDatas = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpBomItemData"))

    #--------------------------------------------------------------------------
    #  Begin "ErpBOM" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Design", "ErpBomItemDatas",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpBOM",
        title="ErpBOM",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpBOM" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpTimeSheet" class:
#------------------------------------------------------------------------------

class ErpTimeSheet(Document):
    """ Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpTimeEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpTimeEntry"))

    #--------------------------------------------------------------------------
    #  Begin "ErpTimeSheet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpTimeEntries",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpTimeSheet",
        title="ErpTimeSheet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpTimeSheet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpSalesOrder" class:
#------------------------------------------------------------------------------

class ErpSalesOrder(Document):
    """ General purpose Sales Order is used for utility service orders, etc. As used by the OAG, the SalesOrder is a step beyond a PurchaseOrder in that the receiving entity of the order also communicates SalesInformoration about the Order along with the Order itself.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ErpSalesOrder" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpSalesOrder",
        title="ErpSalesOrder",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpSalesOrder" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpRecLineItem" class:
#------------------------------------------------------------------------------

class ErpRecLineItem(IdentifiedObject):
    """ Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpInvoiceLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem",
        transient=True,
        opposite="ErpRecLineItem",
        editor=InstanceEditor(name="_erpinvoicelineitems"))

    def _get_erpinvoicelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem" ]
        else:
            return []

    _erpinvoicelineitems = Property(fget=_get_erpinvoicelineitems)

    ErpPayments = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayment"))

    ErpJournalEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry"))

    ErpReceivable = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReceivable",
        transient=True,
        opposite="ErpRecLineItems",
        editor=InstanceEditor(name="_erpreceivables"))

    def _get_erpreceivables(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpReceivable" ]
        else:
            return []

    _erpreceivables = Property(fget=_get_erpreceivables)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpRecLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpInvoiceLineItem", "ErpPayments", "ErpJournalEntries", "ErpReceivable", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem",
        title="ErpRecLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpRecLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpSiteLevelData" class:
#------------------------------------------------------------------------------

class ErpSiteLevelData(IdentifiedObject):
    """ For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    LandProperty = Instance("CIM.IEC61968.Informative.InfLocations.LandProperty",
        transient=True,
        opposite="ErpSiteLevelDatas",
        editor=InstanceEditor(name="_landpropertys"))

    def _get_landpropertys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfLocations.LandProperty" ]
        else:
            return []

    _landpropertys = Property(fget=_get_landpropertys)

    #--------------------------------------------------------------------------
    #  Begin "ErpSiteLevelData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "LandProperty",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpSiteLevelData",
        title="ErpSiteLevelData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpSiteLevelData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPersonnel" class:
#------------------------------------------------------------------------------

class ErpPersonnel(IdentifiedObject):
    """ Information that applies to the basic data about a utility person, used by ERP applications to transfer Personnel data for a worker.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpPersonnel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpPersons", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpPersonnel",
        title="ErpPersonnel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPersonnel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpReceivable" class:
#------------------------------------------------------------------------------

class ErpReceivable(Document):
    """ Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpRecLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecLineItem"))

    #--------------------------------------------------------------------------
    #  Begin "ErpReceivable" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpRecLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpReceivable",
        title="ErpReceivable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpReceivable" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpLedgerEntry" class:
#------------------------------------------------------------------------------

class ErpLedgerEntry(IdentifiedObject):
    """ Details of an individual entry in a ledger, which was posted from a journal on the posted date.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpLedger = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedger",
        transient=True,
        opposite="ErpLedgerEntries",
        editor=InstanceEditor(name="_erpledgers"))

    def _get_erpledgers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpLedger" ]
        else:
            return []

    _erpledgers = Property(fget=_get_erpledgers)

    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"))

    ErpLedgerEntry = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedBudLineItem",
        transient=True,
        opposite="ErpLedBudLineItem",
        editor=InstanceEditor(name="_erpledbudlineitems"))

    def _get_erpledbudlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpLedBudLineItem" ]
        else:
            return []

    _erpledbudlineitems = Property(fget=_get_erpledbudlineitems)

    Settlements = List(Instance("CIM.IEC61968.Informative.MarketOperations.Settlement"))

    ErpJounalEntry = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry",
        transient=True,
        opposite="ErpLedgerEntry",
        editor=InstanceEditor(name="_erpjournalentrys"))

    def _get_erpjournalentrys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry" ]
        else:
            return []

    _erpjournalentrys = Property(fget=_get_erpjournalentrys)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Kind of account for this entry.
    accountKind = ErpAccountKind(desc="Kind of account for this entry.")

    # The amount of the debit or credit for this account.
    amount = Money(desc="The amount of the debit or credit for this account.")

    # Account identifier for this entry.
    accountID = Str(desc="Account identifier for this entry.")

    # Date and time journal entry was recorded.
    transactionDateTime = Date(desc="Date and time journal entry was recorded.")

    # Date and time this entry was posted to the ledger.
    postedDateTime = Date(desc="Date and time this entry was posted to the ledger.")

    #--------------------------------------------------------------------------
    #  Begin "ErpLedgerEntry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "accountKind", "amount", "accountID", "transactionDateTime", "postedDateTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpLedger", "UserAttributes", "ErpLedgerEntry", "Settlements", "ErpJounalEntry", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry",
        title="ErpLedgerEntry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpLedgerEntry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpLedBudLineItem" class:
#------------------------------------------------------------------------------

class ErpLedBudLineItem(IdentifiedObject):
    """ Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpLedgerBudget = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerBudget",
        transient=True,
        opposite="ErpLedBudLineItems",
        editor=InstanceEditor(name="_erpledgerbudgets"))

    def _get_erpledgerbudgets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpLedgerBudget" ]
        else:
            return []

    _erpledgerbudgets = Property(fget=_get_erpledgerbudgets)

    ErpLedBudLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry",
        transient=True,
        opposite="ErpLedgerEntry",
        editor=InstanceEditor(name="_erpledgerentrys"))

    def _get_erpledgerentrys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry" ]
        else:
            return []

    _erpledgerentrys = Property(fget=_get_erpledgerentrys)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "ErpLedBudLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpLedgerBudget", "ErpLedBudLineItem", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpLedBudLineItem",
        title="ErpLedBudLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpLedBudLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpTelephoneNumber" class:
#------------------------------------------------------------------------------

class ErpTelephoneNumber(TelephoneNumber):
    """ The telephone number for a person or organisation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ElectronicAddress = Instance("CIM.IEC61968.Common.ElectronicAddress",
        transient=True,
        opposite="ErpTelephoneNumbers",
        editor=InstanceEditor(name="_electronicaddresss"))

    def _get_electronicaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.ElectronicAddress" ]
        else:
            return []

    _electronicaddresss = Property(fget=_get_electronicaddresss)

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other.
    usage = Str(desc="The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other.")

    #--------------------------------------------------------------------------
    #  Begin "ErpTelephoneNumber" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cityCode", "countryCode", "extension", "areaCode", "localNumber", "usage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Organisation", "Location", "ElectronicAddress", "ErpPersons", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpTelephoneNumber",
        title="ErpTelephoneNumber",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpTelephoneNumber" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpCompetency" class:
#------------------------------------------------------------------------------

class ErpCompetency(IdentifiedObject):
    """ Information that describes aptitudes of a utility employee. Unlike Skills that an ErpPerson must be certified to perform before undertaking certain type of assignments (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human Resource (HR) matters such as schooling, training, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    #--------------------------------------------------------------------------
    #  Begin "ErpCompetency" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpPersons",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfERPSupport.ErpCompetency",
        title="ErpCompetency",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpCompetency" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
