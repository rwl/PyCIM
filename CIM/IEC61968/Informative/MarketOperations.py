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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Document
from CIM import Element
from CIM.IEC61968.Informative.InfERPSupport import ErpOrganisation
from CIM.IEC61968.Informative.EnergyScheduling import Profile
from CIM.IEC61968.Common import Agreement
from CIM.IEC61970.Core import RegularIntervalSchedule
from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61970.Meas import Limit
from CIM.IEC61970.Domain import CostPerEnergyUnit
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Minutes
from CIM.IEC61970.Domain import Money



from enthought.traits.api import Instance, List, Property, Date, Str, Int, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ContingencyConstraintLimit" class:
#------------------------------------------------------------------------------

class ContingencyConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a constraint for a specific contingency. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MWLimitSchedules = Instance("CIM.IEC61968.Informative.MarketOperations.MWLimitSchedule",
        transient=True,
        opposite="SecurityConstraintLimit",
        editor=InstanceEditor(name="_mwlimitschedules"))

    def _get_mwlimitschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MWLimitSchedule" ]
        else:
            return []

    _mwlimitschedules = Property(fget=_get_mwlimitschedules)

    Contingency = Instance("CIM.IEC61970.Contingency.Contingency",
        transient=True,
        opposite="ContingencyConstraintLimit",
        editor=InstanceEditor(name="_contingencys"))

    def _get_contingencys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Contingency.Contingency" ]
        else:
            return []

    _contingencys = Property(fget=_get_contingencys)

    SecurityConstraintSum = Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum",
        transient=True,
        opposite="ContingencyConstraintLimits",
        editor=InstanceEditor(name="_securityconstraintsums"))

    def _get_securityconstraintsums(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum" ]
        else:
            return []

    _securityconstraintsums = Property(fget=_get_securityconstraintsums)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "MWLimitSchedules", "Contingency", "SecurityConstraintSum",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ContingencyConstraintLimit",
        title="ContingencyConstraintLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContingencyConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResourceGroupReq" class:
#------------------------------------------------------------------------------

class ResourceGroupReq(IdentifiedObject):
    """ Ancillary service requirements for a market.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ResourceGroup = Instance("CIM.IEC61968.Informative.MarketOperations.ResourceGroup",
        transient=True,
        opposite="ResourceGroupReqs",
        editor=InstanceEditor(name="_resourcegroups"))

    def _get_resourcegroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ResourceGroup" ]
        else:
            return []

    _resourcegroups = Property(fget=_get_resourcegroups)

    RTOs = List(Instance("CIM.IEC61968.Informative.MarketOperations.RTO"))

    #--------------------------------------------------------------------------
    #  Begin "ResourceGroupReq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ResourceGroup", "RTOs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ResourceGroupReq",
        title="ResourceGroupReq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResourceGroupReq" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketFactors" class:
#------------------------------------------------------------------------------

class MarketFactors(Document):
    """ Aggregation of market information relative for a specific time interval.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpInvoices = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    Market = Instance("CIM.IEC61968.Informative.MarketOperations.Market",
        transient=True,
        opposite="MarketFactors",
        editor=InstanceEditor(name="_markets"))

    def _get_markets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Market" ]
        else:
            return []

    _markets = Property(fget=_get_markets)

    # The start of the time interval for which requirement is defined.
    intervalStartTime = Date(desc="The start of the time interval for which requirement is defined.")

    #--------------------------------------------------------------------------
    #  Begin "MarketFactors" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MarketFactors",
        title="MarketFactors",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketFactors" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Settlement" class:
#------------------------------------------------------------------------------

class Settlement(Document):
    """ Specifies a settlement run.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Market = Instance("CIM.IEC61968.Informative.MarketOperations.Market",
        transient=True,
        opposite="Settlements",
        editor=InstanceEditor(name="_markets"))

    def _get_markets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Market" ]
        else:
            return []

    _markets = Property(fget=_get_markets)

    ErpLedgerEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry"))

    ErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    # The trade date on which the settlement is run.
    tradeDate = Date(desc="The trade date on which the settlement is run.")

    #--------------------------------------------------------------------------
    #  Begin "Settlement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "tradeDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ErpLedgerEntries", "ErpInvoiceLineItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Settlement",
        title="Settlement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Settlement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConstraintTerm" class:
#------------------------------------------------------------------------------

class ConstraintTerm(IdentifiedObject):
    """ A constraint term is one element of a linear constraint.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SecurityConstraintSum = Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum",
        transient=True,
        opposite="ConstraintTerms",
        editor=InstanceEditor(name="_securityconstraintsums"))

    def _get_securityconstraintsums(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum" ]
        else:
            return []

    _securityconstraintsums = Property(fget=_get_securityconstraintsums)

    factor = Str

    # The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow.
    function = Str(desc="The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow.")

    #--------------------------------------------------------------------------
    #  Begin "ConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "factor", "function",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SecurityConstraintSum",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ConstraintTerm",
        title="ConstraintTerm",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Meter" class:
#------------------------------------------------------------------------------

class Meter(IdentifiedObject):
    """ This is generic logical meter object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegisteredResource = Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource",
        transient=True,
        opposite="Meters",
        editor=InstanceEditor(name="_registeredresources"))

    def _get_registeredresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RegisteredResource" ]
        else:
            return []

    _registeredresources = Property(fget=_get_registeredresources)

    #--------------------------------------------------------------------------
    #  Begin "Meter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RegisteredResource",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Meter",
        title="Meter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Meter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyPriceCurve" class:
#------------------------------------------------------------------------------

class EnergyPriceCurve(Curve):
    """ Relationship between a price in $/hour (Y-axis) and a MW value (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EnergyTransactions = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction"))

    FTRs = List(Instance("CIM.IEC61968.Informative.MarketOperations.FTR"))

    #--------------------------------------------------------------------------
    #  Begin "EnergyPriceCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "EnergyTransactions", "FTRs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.EnergyPriceCurve",
        title="EnergyPriceCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyPriceCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketStatement" class:
#------------------------------------------------------------------------------

class MarketStatement(Document):
    """ A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MarketStatementLineItem = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem"))

    # The date of which Settlement is run.
    tradeDate = Date(desc="The date of which Settlement is run.")

    # The version number of previous statement (in the case of true up).
    referenceNumber = Str(desc="The version number of previous statement (in the case of true up).")

    # The start of a bill period.
    start = Date(desc="The start of a bill period.")

    # The end of a bill period.
    end = Date(desc="The end of a bill period.")

    # The date of which this statement is issued.
    transactionDate = Date(desc="The date of which this statement is issued.")

    #--------------------------------------------------------------------------
    #  Begin "MarketStatement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "tradeDate", "referenceNumber", "start", "end", "transactionDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "MarketStatementLineItem",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MarketStatement",
        title="MarketStatement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketStatement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartUpTimeCurve" class:
#------------------------------------------------------------------------------

class StartUpTimeCurve(Curve):
    """ Startup time curve as a function of down time, where time is specified in seconds.  Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.GeneratingBid"))

    #--------------------------------------------------------------------------
    #  Begin "StartUpTimeCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.StartUpTimeCurve",
        title="StartUpTimeCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartUpTimeCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Bid" class:
#------------------------------------------------------------------------------

class Bid(Document):
    """ Represents both bids to purchase and offers to sell energy or ancillary services in an RTO-sponsored market.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Market = Instance("CIM.IEC61968.Informative.MarketOperations.Market",
        transient=True,
        opposite="Bids",
        editor=InstanceEditor(name="_markets"))

    def _get_markets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Market" ]
        else:
            return []

    _markets = Property(fget=_get_markets)

    # A bid comprises one or more product bids of market products
    ProductBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.ProductBid"),
        desc="A bid comprises one or more product bids of market products")

    BidClearing = Instance("CIM.IEC61968.Informative.MarketOperations.BidClearing",
        transient=True,
        opposite="Bid",
        editor=InstanceEditor(name="_bidclearings"))

    def _get_bidclearings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BidClearing" ]
        else:
            return []

    _bidclearings = Property(fget=_get_bidclearings)

    # Stop time and date for which bid is applicable.
    stopTime = Date(desc="Stop time and date for which bid is applicable.")

    # Start time and date for which bid applies.
    startTime = Date(desc="Start time and date for which bid applies.")

    marketType = Str

    #--------------------------------------------------------------------------
    #  Begin "Bid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stopTime", "startTime", "marketType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ProductBids", "BidClearing",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Bid",
        title="Bid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BidClearing" class:
#------------------------------------------------------------------------------

class BidClearing(Element):
    """ Bid clearing results posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Bid = Instance("CIM.IEC61968.Informative.MarketOperations.Bid",
        transient=True,
        opposite="BidClearing",
        editor=InstanceEditor(name="_bids"))

    def _get_bids(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Bid" ]
        else:
            return []

    _bids = Property(fget=_get_bids)

    # No-load cost in monetary units.
    noLoadCost = Money(desc="No-load cost in monetary units.")

    # Start up cost in case of energy commodity in monetary units.
    startUpCost = Money(desc="Start up cost in case of energy commodity in monetary units.")

    # Energy lost opportunity cost in monetary units.
    lostOpCost = Money(desc="Energy lost opportunity cost in monetary units.")

    #--------------------------------------------------------------------------
    #  Begin "BidClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "noLoadCost", "startUpCost", "lostOpCost",
                label="Attributes"),
            VGroup("Parent", "Bid",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BidClearing",
        title="BidClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BidClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResourceGroup" class:
#------------------------------------------------------------------------------

class ResourceGroup(IdentifiedObject):
    """ A logical grouping of resources that are used to model location of types of requirements for ancillary services such as spinning reserve zones, regulation zones, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegisteredResources = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource"))

    ResourceGroupReqs = List(Instance("CIM.IEC61968.Informative.MarketOperations.ResourceGroupReq"))

    #--------------------------------------------------------------------------
    #  Begin "ResourceGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RegisteredResources", "ResourceGroupReqs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ResourceGroup",
        title="ResourceGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResourceGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PassThroughBill" class:
#------------------------------------------------------------------------------

class PassThroughBill(Document):
    """ Pass Through Bill is used for: 1)Two sided charge transactions with or without ISO involvement (hence the ?pass thru?) 2) Specific direct charges or payments that are calculated outside or provided directly to settlements 3) Specific charge bill determinants that are externally supplied and used in charge calculations
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MarketStatementLineItem = Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem",
        transient=True,
        opposite="PassThroughBill",
        editor=InstanceEditor(name="_marketstatementlineitems"))

    def _get_marketstatementlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem" ]
        else:
            return []

    _marketstatementlineitems = Property(fget=_get_marketstatementlineitems)

    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"))

    ChargeProfiles = List(Instance("CIM.IEC61968.Informative.MarketOperations.ChargeProfile"))

    # The product quantity.
    quantity = Instance("CIM.Quantity",
        desc="The product quantity.",
        transient=True,
        editor=InstanceEditor(name="_quantitys"))

    def _get_quantitys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Quantity" ]
        else:
            return []

    _quantitys = Property(fget=_get_quantitys)

    # The date the transaction occurs.
    transactionDate = Date(desc="The date the transaction occurs.")

    # The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant
    transactionType = Str(desc="The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant")

    # The settlement run type, for example: prelim, final, and rerun.
    billRunType = Str(desc="The settlement run type, for example: prelim, final, and rerun.")

    # The time zone code
    timeZone = Str(desc="The time zone code")

    # The tax on services taken.
    taxAmount = Money(desc="The tax on services taken.")

    # The effective date of the transaction
    effectiveDate = Date(desc="The effective date of the transaction")

    # The trade date
    tradeDate = Date(desc="The trade date")

    # Bill period start date
    billStart = Date(desc="Bill period start date")

    # The price of product/service.
    price = Money(desc="The price of product/service.")

    # The company to which the PTB transaction is sold.
    soldTo = Str(desc="The company to which the PTB transaction is sold.")

    # The previous bill period start date
    previousStart = Date(desc="The previous bill period start date")

    # The company by which the PTB transaction service is provided.
    providedBy = Str(desc="The company by which the PTB transaction service is provided.")

    # The product identifier for determining the charge type of the transaction.
    productCode = Str(desc="The product identifier for determining the charge type of the transaction.")

    # A flag indicating whether there is a profile data associated with the PTB.
    isProfiled = Bool(desc="A flag indicating whether there is a profile data associated with the PTB.")

    # The previous bill period end date
    previousEnd = Date(desc="The previous bill period end date")

    # The start date of service provided, if periodic.
    serviceStart = Date(desc="The start date of service provided, if periodic.")

    # The company to which the PTB transaction is paid.
    paidTo = Str(desc="The company to which the PTB transaction is paid.")

    # Bill period end date
    billEnd = Date(desc="Bill period end date")

    # The charge amount of the product/service.
    amount = Money(desc="The charge amount of the product/service.")

    # The end date of service provided, if periodic.
    serviceEnd = Date(desc="The end date of service provided, if periodic.")

    # The company to which the PTB transaction is billed.
    billedTo = Str(desc="The company to which the PTB transaction is billed.")

    # Disputed transaction indicator
    isDisputed = Bool(desc="Disputed transaction indicator")

    #--------------------------------------------------------------------------
    #  Begin "PassThroughBill" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "transactionDate", "transactionType", "billRunType", "timeZone", "taxAmount", "effectiveDate", "tradeDate", "billStart", "price", "soldTo", "previousStart", "providedBy", "productCode", "isProfiled", "previousEnd", "serviceStart", "paidTo", "billEnd", "amount", "serviceEnd", "billedTo", "isDisputed",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "MarketStatementLineItem", "UserAttributes", "ChargeProfiles", "quantity",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.PassThroughBill",
        title="PassThroughBill",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PassThroughBill" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SchedulingCoordinator" class:
#------------------------------------------------------------------------------

class SchedulingCoordinator(ErpOrganisation):
    """ In certain ISO/RTO operations, market participants are represented by Scheduling Coordinators (SCs) that are registered with the ISO/RTO. One participant can register multiple SCs with the ISO/RTO.  Many participants can do business with the ISO/RTO using a single SC. Each generator resource can only be scheduled by one SC. One SC can schedule multiple generators. A load scheduling point can be used by multiple SCs. Each SC can schedule load at multiple scheduling points. Each SC can have more than one load schedule at any load scheduling point as long as each load schedule at the same load scheduling point has a separate resource ID and settlement-quality meter. An inter-tie scheduling point can be used by multiple SCs. Each SC can schedule interchange at multiple inter-tie scheduling points. An SC can have multiple interchange schedules at the same inter-tie scheduling point by assigning a unique interchange identifier to each interchange schedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "SchedulingCoordinator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.SchedulingCoordinator",
        title="SchedulingCoordinator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SchedulingCoordinator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RampRateCurve" class:
#------------------------------------------------------------------------------

class RampRateCurve(Curve):
    """ Ramp rate as a function of resource MW output
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingUnit = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator"))

    # How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource)
    rampRateType = Str(desc="How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource)")

    #--------------------------------------------------------------------------
    #  Begin "RampRateCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "rampRateType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.RampRateCurve",
        title="RampRateCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RampRateCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProductBid" class:
#------------------------------------------------------------------------------

class ProductBid(IdentifiedObject):
    """ Component of a bid that pertains to one market product.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A bid comprises one or more product bids of market products
    Bid = Instance("CIM.IEC61968.Informative.MarketOperations.Bid",
        desc="A bid comprises one or more product bids of market products",
        transient=True,
        opposite="ProductBids",
        editor=InstanceEditor(name="_bids"))

    def _get_bids(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Bid" ]
        else:
            return []

    _bids = Property(fget=_get_bids)

    MarketProduct = Instance("CIM.IEC61968.Informative.MarketOperations.MarketProduct",
        transient=True,
        opposite="ProductBids",
        editor=InstanceEditor(name="_marketproducts"))

    def _get_marketproducts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketProduct" ]
        else:
            return []

    _marketproducts = Property(fget=_get_marketproducts)

    BidPriceCurve = Instance("CIM.IEC61968.Informative.MarketOperations.BidPriceCurve",
        transient=True,
        opposite="ProductBids",
        editor=InstanceEditor(name="_bidpricecurves"))

    def _get_bidpricecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BidPriceCurve" ]
        else:
            return []

    _bidpricecurves = Property(fget=_get_bidpricecurves)

    ProductBidClearing = Instance("CIM.IEC61968.Informative.MarketOperations.ProductBidClearing",
        transient=True,
        opposite="ProductBids",
        editor=InstanceEditor(name="_productbidclearings"))

    def _get_productbidclearings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ProductBidClearing" ]
        else:
            return []

    _productbidclearings = Property(fget=_get_productbidclearings)

    #--------------------------------------------------------------------------
    #  Begin "ProductBid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Bid", "MarketProduct", "BidPriceCurve", "ProductBidClearing",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ProductBid",
        title="ProductBid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProductBid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DefaultConstraintLimit" class:
#------------------------------------------------------------------------------

class DefaultConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) applied as a default value if no specific constraint limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SecurityConstraintSum = Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum",
        transient=True,
        opposite="DefaultConstraintLimit",
        editor=InstanceEditor(name="_securityconstraintsums"))

    def _get_securityconstraintsums(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum" ]
        else:
            return []

    _securityconstraintsums = Property(fget=_get_securityconstraintsums)

    #--------------------------------------------------------------------------
    #  Begin "DefaultConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "SecurityConstraintSum",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.DefaultConstraintLimit",
        title="DefaultConstraintLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DefaultConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ChargeProfile" class:
#------------------------------------------------------------------------------

class ChargeProfile(Profile):
    """ A type of profile for financial charges
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BillDeterminant = Instance("CIM.IEC61968.Informative.MarketOperations.BillDeterminant",
        transient=True,
        opposite="ChargeProfile",
        editor=InstanceEditor(name="_billdeterminants"))

    def _get_billdeterminants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BillDeterminant" ]
        else:
            return []

    _billdeterminants = Property(fget=_get_billdeterminants)

    PassTroughBill = Instance("CIM.IEC61968.Informative.MarketOperations.PassThroughBill",
        transient=True,
        opposite="ChargeProfiles",
        editor=InstanceEditor(name="_passthroughbills"))

    def _get_passthroughbills(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.PassThroughBill" ]
        else:
            return []

    _passthroughbills = Property(fget=_get_passthroughbills)

    ChargeProfileData = List(Instance("CIM.IEC61968.Informative.MarketOperations.ChargeProfileData"))

    # The unit of measure applied to the value attribute of the profile data.
    unitOfMeasure = Str(desc="The unit of measure applied to the value attribute of the profile data.")

    # The calculation frequency, daily or monthly.
    frequency = Str(desc="The calculation frequency, daily or monthly.")

    # The number of intervals in the profile data.
    numberInterval = Int(desc="The number of intervals in the profile data.")

    # The type of profile.  It could be amount, price, or quantity.
    type = Str(desc="The type of profile.  It could be amount, price, or quantity.")

    #--------------------------------------------------------------------------
    #  Begin "ChargeProfile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "unitOfMeasure", "frequency", "numberInterval", "type",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas", "BillDeterminant", "PassTroughBill", "ChargeProfileData",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ChargeProfile",
        title="ChargeProfile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ChargeProfile" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketStatementLineItem" class:
#------------------------------------------------------------------------------

class MarketStatementLineItem(IdentifiedObject):
    """ An individual line item on a statement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MarketStatement = Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatement",
        transient=True,
        opposite="MarketStatementLineItem",
        editor=InstanceEditor(name="_marketstatements"))

    def _get_marketstatements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketStatement" ]
        else:
            return []

    _marketstatements = Property(fget=_get_marketstatements)

    PassThroughBill = Instance("CIM.IEC61968.Informative.MarketOperations.PassThroughBill",
        transient=True,
        opposite="MarketStatementLineItem",
        editor=InstanceEditor(name="_passthroughbills"))

    def _get_passthroughbills(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.PassThroughBill" ]
        else:
            return []

    _passthroughbills = Property(fget=_get_passthroughbills)

    ContainerMarketStatementLineItem = Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem",
        transient=True,
        opposite="ComponentMarketStatementLineItem",
        editor=InstanceEditor(name="_marketstatementlineitems"))

    def _get_marketstatementlineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem" ]
        else:
            return []

    _marketstatementlineitems = Property(fget=_get_marketstatementlineitems)

    ComponentMarketStatementLineItem = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem"))

    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"))

    # Previous ISO settlement amount.
    previousISOAmount = Float(desc="Previous ISO settlement amount.")

    # The number of intervals.
    intervalNumber = Str(desc="The number of intervals.")

    # Net settlement quantity, subject to the UOM.
    netQuantity = Float(desc="Net settlement quantity, subject to the UOM.")

    # The date of which the settlement is run.
    intervalDate = Date(desc="The date of which the settlement is run.")

    # Previous settlement amount.
    previousAmount = Float(desc="Previous settlement amount.")

    # Net ISO settlement amount.
    netISOAmount = Float(desc="Net ISO settlement amount.")

    # Net settlement price.
    netPrice = Float(desc="Net settlement price.")

    # Current settlement amount.
    currentAmount = Float(desc="Current settlement amount.")

    # Net ISO settlement quantity.
    netISOQuantity = Float(desc="Net ISO settlement quantity.")

    # Previous settlement quantity, subject to the UOM.
    previousQuantity = Float(desc="Previous settlement quantity, subject to the UOM.")

    # The unit of measure for the quantity element of the line item.
    quantityUOM = Str(desc="The unit of measure for the quantity element of the line item.")

    # Previous settlement price.
    previsouPrice = Float(desc="Previous settlement price.")

    # Previous ISO settlement quantity.
    previousISOQuantity = Float(desc="Previous ISO settlement quantity.")

    # Current ISO settlement amount.
    currentISOAmount = Float(desc="Current ISO settlement amount.")

    # Current settlement quantity, subject to the UOM.
    currentQuantity = Float(desc="Current settlement quantity, subject to the UOM.")

    # Current settlement price.
    currentPrice = Float(desc="Current settlement price.")

    # Net settlement amount.
    netAmount = Float(desc="Net settlement amount.")

    # Current ISO settlement quantity.
    currentISOQuantity = Float(desc="Current ISO settlement quantity.")

    #--------------------------------------------------------------------------
    #  Begin "MarketStatementLineItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "previousISOAmount", "intervalNumber", "netQuantity", "intervalDate", "previousAmount", "netISOAmount", "netPrice", "currentAmount", "netISOQuantity", "previousQuantity", "quantityUOM", "previsouPrice", "previousISOQuantity", "currentISOAmount", "currentQuantity", "currentPrice", "netAmount", "currentISOQuantity",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "MarketStatement", "PassThroughBill", "ContainerMarketStatementLineItem", "ComponentMarketStatementLineItem", "UserAttributes",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem",
        title="MarketStatementLineItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketStatementLineItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegisteredResource" class:
#------------------------------------------------------------------------------

class RegisteredResource(IdentifiedObject):
    """ A resource that is registered through the RTO participant registration system. Examples include generating unit, customer meter, and a non-physical generator or load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Meters = List(Instance("CIM.IEC61968.Informative.MarketOperations.Meter"))

    Markets = List(Instance("CIM.IEC61968.Informative.MarketOperations.Market"))

    ResourceGroups = List(Instance("CIM.IEC61968.Informative.MarketOperations.ResourceGroup"))

    # A registered resource is eligible to bid market products
    MarketProducts = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketProduct"),
        desc="A registered resource is eligible to bid market products")

    # A registered resource injects power at one or more connectivity nodes related to a pnode
    Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        desc="A registered resource injects power at one or more connectivity nodes related to a pnode",
        transient=True,
        opposite="RegisteredResources",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    Organisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="RegisteredResources",
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

    # Unique name obtained via RTO registration
    rtoID = Str(desc="Unique name obtained via RTO registration")

    #--------------------------------------------------------------------------
    #  Begin "RegisteredResource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "rtoID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Meters", "Markets", "ResourceGroups", "MarketProducts", "Pnode", "Organisation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.RegisteredResource",
        title="RegisteredResource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegisteredResource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Market" class:
#------------------------------------------------------------------------------

class Market(IdentifiedObject):
    """ Market (e.g., DAM, HAM)  zzMarket operation control parameters.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Bids = List(Instance("CIM.IEC61968.Informative.MarketOperations.Bid"))

    MarketProducts = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketProduct"))

    RegisteredResources = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource"))

    Settlements = List(Instance("CIM.IEC61968.Informative.MarketOperations.Settlement"))

    MarketFactors = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketFactors"))

    RTO = Instance("CIM.IEC61968.Informative.MarketOperations.RTO",
        transient=True,
        opposite="Markets",
        editor=InstanceEditor(name="_rtos"))

    def _get_rtos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RTO" ]
        else:
            return []

    _rtos = Property(fget=_get_rtos)

    # Ramping time interval for non-spinning reserve.
    rampIntervalNonSpinRes = Minutes(desc="Ramping time interval for non-spinning reserve.")

    # Local time zone.
    localTimeZone = Str(desc="Local time zone.")

    # Ramping time interval for energy.
    rampIntervalEnergy = Minutes(desc="Ramping time interval for energy.")

    # The type of a market.
    type = Str(desc="The type of a market.")

    # Trading time interval length.
    timeIntervalLength = Minutes(desc="Trading time interval length.")

    # Ramping time interval for spinning reserve.
    rampIntervalSpinRes = Minutes(desc="Ramping time interval for spinning reserve.")

    # True if daylight savings time (DST) is in effect.
    dst = Bool(desc="True if daylight savings time (DST) is in effect.")

    # Ramping time interval for regulation.
    rampIntervalReg = Minutes(desc="Ramping time interval for regulation.")

    # Market end time.
    end = Date(desc="Market end time.")

    # Market start time.
    start = Date(desc="Market start time.")

    #--------------------------------------------------------------------------
    #  Begin "Market" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "rampIntervalNonSpinRes", "localTimeZone", "rampIntervalEnergy", "type", "timeIntervalLength", "rampIntervalSpinRes", "dst", "rampIntervalReg", "end", "start",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Bids", "MarketProducts", "RegisteredResources", "Settlements", "MarketFactors", "RTO",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Market",
        title="Market",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Market" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Pnode" class:
#------------------------------------------------------------------------------

class Pnode(IdentifiedObject):
    """ A pricing node is directly associated with a connectivity node.  It is a pricing location for which market participants submit their bids, offers, buy/sell CRRs, and settle.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConnectivityNode = Instance("CIM.IEC61970.Topology.ConnectivityNode",
        transient=True,
        opposite="Pnode",
        editor=InstanceEditor(name="_connectivitynodes"))

    def _get_connectivitynodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    RTO = Instance("CIM.IEC61968.Informative.MarketOperations.RTO",
        transient=True,
        opposite="Pnodes",
        editor=InstanceEditor(name="_rtos"))

    def _get_rtos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RTO" ]
        else:
            return []

    _rtos = Property(fget=_get_rtos)

    DeliveryTransactionBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.TransactionBid"))

    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"))

    ReceiptTransactionBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.TransactionBid"))

    FTRs = List(Instance("CIM.IEC61968.Informative.MarketOperations.FTR"))

    # A registered resource injects power at one or more connectivity nodes related to a pnode
    RegisteredResources = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource"),
        desc="A registered resource injects power at one or more connectivity nodes related to a pnode")

    PnodeClearing = Instance("CIM.IEC61968.Informative.MarketOperations.PnodeClearing",
        transient=True,
        opposite="Pnode",
        editor=InstanceEditor(name="_pnodeclearings"))

    def _get_pnodeclearings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.PnodeClearing" ]
        else:
            return []

    _pnodeclearings = Property(fget=_get_pnodeclearings)

    # Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub'
    usage = Str(desc="Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub'")

    # True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions
    isPublic = Bool(desc="True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions")

    # Start date-time of the period in which the price node definition is valid.
    beginPeriod = Date(desc="Start date-time of the period in which the price node definition is valid.")

    # End date-time of the period in which the price node definition is valid
    endPeriod = Date(desc="End date-time of the period in which the price node definition is valid")

    # Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B)
    type = Str(desc="Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B)")

    #--------------------------------------------------------------------------
    #  Begin "Pnode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "isPublic", "beginPeriod", "endPeriod", "type",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConnectivityNode", "RTO", "DeliveryTransactionBids", "Measurements", "ReceiptTransactionBids", "FTRs", "RegisteredResources", "PnodeClearing",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Pnode",
        title="Pnode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Pnode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BaseCaseConstraintLimit" class:
#------------------------------------------------------------------------------

class BaseCaseConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SecurityConstraintSum = Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum",
        transient=True,
        opposite="BaseCaseConstraintLimit",
        editor=InstanceEditor(name="_securityconstraintsums"))

    def _get_securityconstraintsums(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum" ]
        else:
            return []

    _securityconstraintsums = Property(fget=_get_securityconstraintsums)

    #--------------------------------------------------------------------------
    #  Begin "BaseCaseConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "SecurityConstraintSum",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BaseCaseConstraintLimit",
        title="BaseCaseConstraintLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseCaseConstraintLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FTR" class:
#------------------------------------------------------------------------------

class FTR(Agreement):
    """ Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Pnodes = List(Instance("CIM.IEC61968.Informative.MarketOperations.Pnode"))

    EnergyPriceCurve = Instance("CIM.IEC61968.Informative.MarketOperations.EnergyPriceCurve",
        transient=True,
        opposite="FTRs",
        editor=InstanceEditor(name="_energypricecurves"))

    def _get_energypricecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.EnergyPriceCurve" ]
        else:
            return []

    _energypricecurves = Property(fget=_get_energypricecurves)

    Flowgate = Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate",
        transient=True,
        opposite="FTRs",
        editor=InstanceEditor(name="_flowgates"))

    def _get_flowgates(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Flowgate" ]
        else:
            return []

    _flowgates = Property(fget=_get_flowgates)

    # Buy, Sell
    action = Str(desc="Buy, Sell")

    # Peak, Off-peak, 24-hour
    class = Str(desc="Peak, Off-peak, 24-hour")

    # Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource.
    baseEnergy = ActivePower(desc="Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource.")

    # Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase
    optimized = Str(desc="Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase")

    # Type of rights being offered (product) allowed to be auctioned (option, obligation).
    ftrType = Str(desc="Type of rights being offered (product) allowed to be auctioned (option, obligation).")

    #--------------------------------------------------------------------------
    #  Begin "FTR" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate", "action", "class", "baseEnergy", "optimized", "ftrType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "Pnodes", "EnergyPriceCurve", "Flowgate",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.FTR",
        title="FTR",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FTR" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReserveReqCurve" class:
#------------------------------------------------------------------------------

class ReserveReqCurve(RegularIntervalSchedule):
    """ A curve relating  reserve requirement versus time, showing the values of a specific reserve requirement for each unit of the period covered. The  curve can be based on 'absolute' time or on 'normalized' time.  X is time, typically expressed in absolute time Y1 is reserve requirement, typically expressed in MW
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReserveReq = Instance("CIM.IEC61968.Informative.MarketOperations.ReserveReq",
        transient=True,
        opposite="ReserveReqCurve",
        editor=InstanceEditor(name="_reservereqs"))

    def _get_reservereqs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ReserveReq" ]
        else:
            return []

    _reservereqs = Property(fget=_get_reservereqs)

    #--------------------------------------------------------------------------
    #  Begin "ReserveReqCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "ReserveReq",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ReserveReqCurve",
        title="ReserveReqCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReserveReqCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SecurityConstraints" class:
#------------------------------------------------------------------------------

class SecurityConstraints(IdentifiedObject):
    """ Typical for regional transmission operators (RTOs), these constraints include transmission as well as generation group constraints identified in both base case and critical contingency cases.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RTO = Instance("CIM.IEC61968.Informative.MarketOperations.RTO",
        transient=True,
        opposite="SecurityConstraints",
        editor=InstanceEditor(name="_rtos"))

    def _get_rtos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RTO" ]
        else:
            return []

    _rtos = Property(fget=_get_rtos)

    # Maximum MW limit
    maxMW = ActivePower(desc="Maximum MW limit")

    # Actual branch or group of branches MW flow (only for transmission constraints)
    actualMW = ActivePower(desc="Actual branch or group of branches MW flow (only for transmission constraints)")

    # Minimum MW limit (only for transmission constraints).
    minMW = ActivePower(desc="Minimum MW limit (only for transmission constraints).")

    #--------------------------------------------------------------------------
    #  Begin "SecurityConstraints" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "maxMW", "actualMW", "minMW",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RTO",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.SecurityConstraints",
        title="SecurityConstraints",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SecurityConstraints" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MWLimitSchedule" class:
#------------------------------------------------------------------------------

class MWLimitSchedule(Curve):
    """ Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SecurityConstraintLimit = Instance("CIM.IEC61968.Informative.MarketOperations.ContingencyConstraintLimit",
        transient=True,
        opposite="MWLimitSchedules",
        editor=InstanceEditor(name="_contingencyconstraintlimits"))

    def _get_contingencyconstraintlimits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ContingencyConstraintLimit" ]
        else:
            return []

    _contingencyconstraintlimits = Property(fget=_get_contingencyconstraintlimits)

    #--------------------------------------------------------------------------
    #  Begin "MWLimitSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "SecurityConstraintLimit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MWLimitSchedule",
        title="MWLimitSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MWLimitSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BidSet" class:
#------------------------------------------------------------------------------

class BidSet(IdentifiedObject):
    """ As set of mutually exclusive bids for which a maximum of one may be scheduled. Of these generating bids, only one generating bid can be scheduled at a time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.GeneratingBid"))

    #--------------------------------------------------------------------------
    #  Begin "BidSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GeneratingBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BidSet",
        title="BidSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BidSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionReliabilityMargin" class:
#------------------------------------------------------------------------------

class TransmissionReliabilityMargin(IdentifiedObject):
    """ Transmission Reliability Margin (TRM) is defined as that amount of transmission transfer capability necessary to ensure that the interconnected transmission network is secure under a reasonable range of uncertainties in system conditions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A fowgate may have 0 to 1 TRM
    Flowgate = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"),
        desc="A fowgate may have 0 to 1 TRM")

    # unit of the TRM value. Could be MW or Percentage.
    valueUnit = Str(desc="unit of the TRM value. Could be MW or Percentage.")

    # Value of the TRM
    trmValue = Float(desc="Value of the TRM")

    # the type of TRM
    TrmType = Str(desc="the type of TRM")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionReliabilityMargin" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "valueUnit", "trmValue", "TrmType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Flowgate",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.TransmissionReliabilityMargin",
        title="TransmissionReliabilityMargin",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionReliabilityMargin" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BidPriceCurve" class:
#------------------------------------------------------------------------------

class BidPriceCurve(Curve):
    """ Relationship between unit operating price in $/hour (Y-axis) and unit output in MW (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ProductBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.ProductBid"))

    #--------------------------------------------------------------------------
    #  Begin "BidPriceCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ProductBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BidPriceCurve",
        title="BidPriceCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BidPriceCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BilateralTransaction" class:
#------------------------------------------------------------------------------

class BilateralTransaction(Element):
    """ Bilateral transaction
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Transaction scope: 'Internal' 'External'
    scope = Str(desc="Transaction scope: 'Internal' 'External'")

    # Maximum curtailment time in number of trading intervals
    curtailTimeMax = Int(desc="Maximum curtailment time in number of trading intervals")

    # Minimum curtailment time in number of trading intervals
    curtailTimeMin = Int(desc="Minimum curtailment time in number of trading intervals")

    # Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead
    marketType = Str(desc="Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead")

    # Minimum purchase time in number of trading intervals
    purchaseTimeMin = Int(desc="Minimum purchase time in number of trading intervals")

    # Maximum purchase time in number of trading intervals
    purchaseTimeMax = Int(desc="Maximum purchase time in number of trading intervals")

    # Maximum total transmission (congestion) charges in monetary units
    totalTranChargeMax = Money(desc="Maximum total transmission (congestion) charges in monetary units")

    # Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading
    transactionType = Str(desc="Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading")

    #--------------------------------------------------------------------------
    #  Begin "BilateralTransaction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "scope", "curtailTimeMax", "curtailTimeMin", "marketType", "purchaseTimeMin", "purchaseTimeMax", "totalTranChargeMax", "transactionType",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BilateralTransaction",
        title="BilateralTransaction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BilateralTransaction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketProduct" class:
#------------------------------------------------------------------------------

class MarketProduct(IdentifiedObject):
    """ A product traded by an RTO (e.g., energy, 10 minute spinning reserve).  Ancillary service product examples include: Regulation Up Regulation Dn Spinning Reserve Non-Spinning Reserve Operating Reserve
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Market = Instance("CIM.IEC61968.Informative.MarketOperations.Market",
        transient=True,
        opposite="MarketProducts",
        editor=InstanceEditor(name="_markets"))

    def _get_markets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Market" ]
        else:
            return []

    _markets = Property(fget=_get_markets)

    # A registered resource is eligible to bid market products
    RegisteredResources = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredResource"),
        desc="A registered resource is eligible to bid market products")

    # Market product associated with reserve requirement must be a reserve or regulation product.
    ReserveReqs = List(Instance("CIM.IEC61968.Informative.MarketOperations.ReserveReq"),
        desc="Market product associated with reserve requirement must be a reserve or regulation product.")

    ProductBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.ProductBid"))

    #--------------------------------------------------------------------------
    #  Begin "MarketProduct" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Market", "RegisteredResources", "ReserveReqs", "ProductBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MarketProduct",
        title="MarketProduct",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketProduct" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Flowgate" class:
#------------------------------------------------------------------------------

class Flowgate(PowerSystemResource):
    """ A flowgate, is single or group of transmission elements intended to model MW flow impact relating to transmission limitations and transmission service usage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
    SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area",
        transient=True,
        opposite="Flowgate",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    ViolationLimits = List(Instance("CIM.IEC61968.Informative.MarketOperations.ViolationLimit"))

    # A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
    TransmissionProvider = List(Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider"),
        desc="A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.")

    # A fowgate may have 0 to 1 TRM
    TransmissionReliabilityMargin = Instance("CIM.IEC61968.Informative.MarketOperations.TransmissionReliabilityMargin",
        desc="A fowgate may have 0 to 1 TRM",
        transient=True,
        opposite="Flowgate",
        editor=InstanceEditor(name="_transmissionreliabilitymargins"))

    def _get_transmissionreliabilitymargins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.TransmissionReliabilityMargin" ]
        else:
            return []

    _transmissionreliabilitymargins = Property(fget=_get_transmissionreliabilitymargins)

    PowerTransormers = List(Instance("CIM.IEC61970.Wires.PowerTransformer"))

    # The type of Flowgate.  Values are 'PERMANENT' (in Book of Flowgates) or 'TEMPORARY'.
    IdcType = Instance("CIM.FlowgateIdcType",
        desc="The type of Flowgate.  Values are 'PERMANENT' (in Book of Flowgates) or 'TEMPORARY'.",
        transient=True,
        editor=InstanceEditor(name="_flowgateidctypes"))

    def _get_flowgateidctypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.FlowgateIdcType" ]
        else:
            return []

    _flowgateidctypes = Property(fget=_get_flowgateidctypes)

    Lines = List(Instance("CIM.IEC61970.Wires.Line"))

    # A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
    CapacityBenefitMargin = List(Instance("CIM.IEC61968.Informative.MarketOperations.CapacityBenefitMargin"),
        desc="A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data")

    # Used to indicate if FG should be used only for certain types of AFC Calculations.  Values are 'FIRM,'  'NONFIRM,' and 'BOTH.'
    AfcUseCode = Instance("CIM.FlowgateAfcUseCode",
        desc="Used to indicate if FG should be used only for certain types of AFC Calculations.  Values are 'FIRM,'  'NONFIRM,' and 'BOTH.'",
        transient=True,
        editor=InstanceEditor(name="_flowgateafcusecodes"))

    def _get_flowgateafcusecodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.FlowgateAfcUseCode" ]
        else:
            return []

    _flowgateafcusecodes = Property(fget=_get_flowgateafcusecodes)

    FTRs = List(Instance("CIM.IEC61968.Informative.MarketOperations.FTR"))

    # Flag to indicate if Flowgate qualified as coordinated Flowgate
    coordinatedFlag = Bool(desc="Flag to indicate if Flowgate qualified as coordinated Flowgate")

    # Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less.
    counterFlowValue = Int(desc="Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less.")

    # Flag to indicate if Flowgate qualified as reciprocal Flowgate
    reciprocalFlag = Bool(desc="Flag to indicate if Flowgate qualified as reciprocal Flowgate")

    # Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false.
    managingEntityFlag = Bool(desc="Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false.")

    # Date at which point Flowgate becomes inactive. Used to insert outage condition.
    outOfServiceDate = Date(desc="Date at which point Flowgate becomes inactive. Used to insert outage condition.")

    # Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet.
    coordinationStudyDate = Date(desc="Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet.")

    # Flag to indicate if Flowgate is utilized for coordination of ATC.
    AtcFlag = Bool(desc="Flag to indicate if Flowgate is utilized for coordination of ATC.")

    # Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition.
    inServiceDate = Date(desc="Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition.")

    # The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate.
    IdcAssignedId = Int(desc="The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate.")

    # The Registered Name utilized in the IDC and/or Book of Flowgates
    IdcOperationalName = Str(desc="The Registered Name utilized in the IDC and/or Book of Flowgates")

    # Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less.
    positiveImpactValue = Int(desc="Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less.")

    # Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC).
    deletionDate = Date(desc="Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC).")

    #--------------------------------------------------------------------------
    #  Begin "Flowgate" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "coordinatedFlag", "counterFlowValue", "reciprocalFlag", "managingEntityFlag", "outOfServiceDate", "coordinationStudyDate", "AtcFlag", "inServiceDate", "IdcAssignedId", "IdcOperationalName", "positiveImpactValue", "deletionDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SubControlArea", "ViolationLimits", "TransmissionProvider", "TransmissionReliabilityMargin", "PowerTransormers", "IdcType", "Lines", "CapacityBenefitMargin", "AfcUseCode", "FTRs",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.Flowgate",
        title="Flowgate",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Flowgate" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ViolationLimit" class:
#------------------------------------------------------------------------------

class ViolationLimit(Limit):
    """ A type of limit that indicates if it is enforced and, through association, the organisation responsible for setting the limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Organisations = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation"))

    Flowgate = Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate",
        transient=True,
        opposite="ViolationLimits",
        editor=InstanceEditor(name="_flowgates"))

    def _get_flowgates(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Flowgate" ]
        else:
            return []

    _flowgates = Property(fget=_get_flowgates)

    # Limits may differ based on the season
    Season = Instance("CIM.IEC61970.LoadModel.Season",
        desc="Limits may differ based on the season",
        transient=True,
        opposite="ViolationLimits",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    Measurement = Instance("CIM.IEC61970.Meas.Measurement",
        transient=True,
        opposite="ViolationLimits",
        editor=InstanceEditor(name="_measurements"))

    def _get_measurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Measurement" ]
        else:
            return []

    _measurements = Property(fget=_get_measurements)

    # True if limit is enforced.
    enforced = Bool(desc="True if limit is enforced.")

    #--------------------------------------------------------------------------
    #  Begin "ViolationLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "enforced",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Procedures", "Organisations", "Flowgate", "Season", "Measurement",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ViolationLimit",
        title="ViolationLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ViolationLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SensitivityPriceCurve" class:
#------------------------------------------------------------------------------

class SensitivityPriceCurve(Curve):
    """ Optionally, this curve expresses elasticity of the associated requirement.  For example, used to reduce requirements when clearing price exceeds reasonable values when the supply quantity becomes scarce.  For example, a single point value of $1000/MW for a spinning reserve will cause a reduction in the required spinning reserve.  X axis is constrained quantity (e.g., MW) Y1 axis is money per constrained quantity
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReserveReq = Instance("CIM.IEC61968.Informative.MarketOperations.ReserveReq",
        transient=True,
        opposite="SensitivityPriceCurve",
        editor=InstanceEditor(name="_reservereqs"))

    def _get_reservereqs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ReserveReq" ]
        else:
            return []

    _reservereqs = Property(fget=_get_reservereqs)

    #--------------------------------------------------------------------------
    #  Begin "SensitivityPriceCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ReserveReq",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.SensitivityPriceCurve",
        title="SensitivityPriceCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SensitivityPriceCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CapacityBenefitMargin" class:
#------------------------------------------------------------------------------

class CapacityBenefitMargin(Profile):
    """ Capacity Benefit Margin (CBM) is defined as that amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. Reservation fo CBM by a load serving entity allows that entity to reduce its installed generating capacity below that which may otherwise have been necessary without interconnections to meet its generation reliability requirements.  CBM is modeled as a profile with values in different time periods which are represented by the profile data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Capacity Benefit Margin may differ based on the season
    Season = Instance("CIM.IEC61970.LoadModel.Season",
        desc="Capacity Benefit Margin may differ based on the season",
        transient=True,
        opposite="CapacityBenefitMargin",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    # A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
    Flowgate = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"),
        desc="A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data")

    #--------------------------------------------------------------------------
    #  Begin "CapacityBenefitMargin" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas", "Season", "Flowgate",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.CapacityBenefitMargin",
        title="CapacityBenefitMargin",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CapacityBenefitMargin" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RTO" class:
#------------------------------------------------------------------------------

class RTO(ErpOrganisation):
    """ Regional transmission operator.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Pnodes = List(Instance("CIM.IEC61968.Informative.MarketOperations.Pnode"))

    SecurityConstraints = List(Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraints"))

    SecurityConstraintsLinear = List(Instance("CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum"))

    ResourceGroupReqs = List(Instance("CIM.IEC61968.Informative.MarketOperations.ResourceGroupReq"))

    Markets = List(Instance("CIM.IEC61968.Informative.MarketOperations.Market"))

    #--------------------------------------------------------------------------
    #  Begin "RTO" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "Pnodes", "SecurityConstraints", "SecurityConstraintsLinear", "ResourceGroupReqs", "Markets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.RTO",
        title="RTO",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RTO" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadReductionPriceCurve" class:
#------------------------------------------------------------------------------

class LoadReductionPriceCurve(Curve):
    """ This is the price sensitivity that bidder expresses for allowing market load interruption.  Relationship between price (Y1-axis) vs. MW (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LoadBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.LoadBid"))

    #--------------------------------------------------------------------------
    #  Begin "LoadReductionPriceCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "LoadBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.LoadReductionPriceCurve",
        title="LoadReductionPriceCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadReductionPriceCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BillDeterminant" class:
#------------------------------------------------------------------------------

class BillDeterminant(Document):
    ChargeProfile = Instance("CIM.IEC61968.Informative.MarketOperations.ChargeProfile",
        transient=True,
        opposite="BillDeterminant",
        editor=InstanceEditor(name="_chargeprofiles"))

    def _get_chargeprofiles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ChargeProfile" ]
        else:
            return []

    _chargeprofiles = Property(fget=_get_chargeprofiles)

    ChargeProfileData = List(Instance("CIM.IEC61968.Informative.MarketOperations.ChargeProfileData"))

    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"))

    # Level in charge calculation order.
    calculationLevel = Str(desc="Level in charge calculation order.")

    # The level of precision in the current value.
    precisionLevel = Str(desc="The level of precision in the current value.")

    # The UOM for the current value of the Bill Determinant.
    unitOfMeasure = Str(desc="The UOM for the current value of the Bill Determinant.")

    # The version of configuration of calculation logic in the settlement.
    configVersion = Str(desc="The version of configuration of calculation logic in the settlement.")

    # Number of intervals of bill determiant in trade day, eg 300 for five minute intervals.
    numberInterval = Int(desc="Number of intervals of bill determiant in trade day, eg 300 for five minute intervals.")

    #--------------------------------------------------------------------------
    #  Begin "BillDeterminant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "calculationLevel", "precisionLevel", "unitOfMeasure", "configVersion", "numberInterval",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ChargeProfile", "ChargeProfileData", "UserAttributes",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.BillDeterminant",
        title="BillDeterminant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BillDeterminant" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ChargeProfileData" class:
#------------------------------------------------------------------------------

class ChargeProfileData(Element):
    BillDeterminant = Instance("CIM.IEC61968.Informative.MarketOperations.BillDeterminant",
        transient=True,
        opposite="ChargeProfileData",
        editor=InstanceEditor(name="_billdeterminants"))

    def _get_billdeterminants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BillDeterminant" ]
        else:
            return []

    _billdeterminants = Property(fget=_get_billdeterminants)

    ChargeProfile = Instance("CIM.IEC61968.Informative.MarketOperations.ChargeProfile",
        transient=True,
        opposite="ChargeProfileData",
        editor=InstanceEditor(name="_chargeprofiles"))

    def _get_chargeprofiles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ChargeProfile" ]
        else:
            return []

    _chargeprofiles = Property(fget=_get_chargeprofiles)

    # The sequence number of the profile.
    sequence = Int(desc="The sequence number of the profile.")

    # The value of an interval given a profile type (amount, price, or quantity), subject to the UOM.
    value = Float(desc="The value of an interval given a profile type (amount, price, or quantity), subject to the UOM.")

    # The date and time of an interval.
    timeStamp = Date(desc="The date and time of an interval.")

    #--------------------------------------------------------------------------
    #  Begin "ChargeProfileData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequence", "value", "timeStamp",
                label="Attributes"),
            VGroup("Parent", "BillDeterminant", "ChargeProfile",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ChargeProfileData",
        title="ChargeProfileData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ChargeProfileData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartUpCostCurve" class:
#------------------------------------------------------------------------------

class StartUpCostCurve(Curve):
    """ Startup costs and time as a function of down time.  Relationship between unit startup cost (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.GeneratingBid"))

    RegisteredGenerators = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator"))

    #--------------------------------------------------------------------------
    #  Begin "StartUpCostCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingBids", "RegisteredGenerators",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.StartUpCostCurve",
        title="StartUpCostCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartUpCostCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NotificationTimeCurve" class:
#------------------------------------------------------------------------------

class NotificationTimeCurve(Curve):
    """ Notification time curve as a function of down time.  Relationship between crew notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.GeneratingBid"))

    #--------------------------------------------------------------------------
    #  Begin "NotificationTimeCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.NotificationTimeCurve",
        title="NotificationTimeCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NotificationTimeCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "UnitInitialConditions" class:
#------------------------------------------------------------------------------

class UnitInitialConditions(IdentifiedObject):
    """ Resource status at the end of a given clearing period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingUnit = Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator",
        transient=True,
        opposite="UnitInitialConditions",
        editor=InstanceEditor(name="_registeredgenerators"))

    def _get_registeredgenerators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator" ]
        else:
            return []

    _registeredgenerators = Property(fget=_get_registeredgenerators)

    # Cumulative energy production over trading period.
    cumEnergy = Instance("CIM.EnergyAsMWh",
        desc="Cumulative energy production over trading period.",
        transient=True,
        editor=InstanceEditor(name="_energyasmwhs"))

    def _get_energyasmwhs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.EnergyAsMWh" ]
        else:
            return []

    _energyasmwhs = Property(fget=_get_energyasmwhs)

    # Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process
    resourceStatus = Int(desc="Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process")

    # Cumulative number of status changes of the resource.
    cumStatusChanges = Int(desc="Cumulative number of status changes of the resource.")

    # Time and date for resourceStatus
    statusDate = Date(desc="Time and date for resourceStatus")

    # Resource MW output at the end of previous clearing period.
    resourceMW = ActivePower(desc="Resource MW output at the end of previous clearing period.")

    # Time in market trading intervals the resource is in the state as of the end of the previous clearing period.
    timeInStatus = Minutes(desc="Time in market trading intervals the resource is in the state as of the end of the previous clearing period.")

    #--------------------------------------------------------------------------
    #  Begin "UnitInitialConditions" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "resourceStatus", "cumStatusChanges", "statusDate", "resourceMW", "timeInStatus",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GeneratingUnit", "cumEnergy",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.UnitInitialConditions",
        title="UnitInitialConditions",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "UnitInitialConditions" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReserveReq" class:
#------------------------------------------------------------------------------

class ReserveReq(ResourceGroupReq):
    """ Requirements for minimum amount of reserve and/or regulation to be supplied by a set of qualified resources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Market product associated with reserve requirement must be a reserve or regulation product.
    MarketProduct = Instance("CIM.IEC61968.Informative.MarketOperations.MarketProduct",
        desc="Market product associated with reserve requirement must be a reserve or regulation product.",
        transient=True,
        opposite="ReserveReqs",
        editor=InstanceEditor(name="_marketproducts"))

    def _get_marketproducts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketProduct" ]
        else:
            return []

    _marketproducts = Property(fget=_get_marketproducts)

    ReserveReqCurve = Instance("CIM.IEC61968.Informative.MarketOperations.ReserveReqCurve",
        transient=True,
        opposite="ReserveReq",
        editor=InstanceEditor(name="_reservereqcurves"))

    def _get_reservereqcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.ReserveReqCurve" ]
        else:
            return []

    _reservereqcurves = Property(fget=_get_reservereqcurves)

    SensitivityPriceCurve = Instance("CIM.IEC61968.Informative.MarketOperations.SensitivityPriceCurve",
        transient=True,
        opposite="ReserveReq",
        editor=InstanceEditor(name="_sensitivitypricecurves"))

    def _get_sensitivitypricecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.SensitivityPriceCurve" ]
        else:
            return []

    _sensitivitypricecurves = Property(fget=_get_sensitivitypricecurves)

    #--------------------------------------------------------------------------
    #  Begin "ReserveReq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ResourceGroup", "RTOs", "MarketProduct", "ReserveReqCurve", "SensitivityPriceCurve",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ReserveReq",
        title="ReserveReq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReserveReq" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TerminalConstraintTerm" class:
#------------------------------------------------------------------------------

class TerminalConstraintTerm(ConstraintTerm):
    """ A constraint term associated with a specific terminal on a physical piece of equipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Terminal = Instance("CIM.IEC61970.Core.Terminal",
        transient=True,
        opposite="TerminalConstraints",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    #--------------------------------------------------------------------------
    #  Begin "TerminalConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "factor", "function",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SecurityConstraintSum", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.TerminalConstraintTerm",
        title="TerminalConstraintTerm",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TerminalConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LossPenaltyFactor" class:
#------------------------------------------------------------------------------

class LossPenaltyFactor(MarketFactors):
    """ Loss penalty factor applied to a ConnectivityNode for a given time interval.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConnectivityNodes = List(Instance("CIM.IEC61970.Topology.ConnectivityNode"))

    # Loss penalty factor.
    lossFactor = Instance("CIM.PenaltyFactor",
        desc="Loss penalty factor.",
        transient=True,
        editor=InstanceEditor(name="_penaltyfactors"))

    def _get_penaltyfactors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PenaltyFactor" ]
        else:
            return []

    _penaltyfactors = Property(fget=_get_penaltyfactors)

    #--------------------------------------------------------------------------
    #  Begin "LossPenaltyFactor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "ConnectivityNodes", "lossFactor",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.LossPenaltyFactor",
        title="LossPenaltyFactor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LossPenaltyFactor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PnodeClearing" class:
#------------------------------------------------------------------------------

class PnodeClearing(MarketFactors):
    """ Pricing node clearing results posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        transient=True,
        opposite="PnodeClearing",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    # Congestion component of Location Marginal Price (LMP) in monetary units per MW.
    congestLMP = CostPerEnergyUnit(desc="Congestion component of Location Marginal Price (LMP) in monetary units per MW.")

    # Loss component of Location Marginal Price (LMP) in monetary units per MW.
    lossLMP = CostPerEnergyUnit(desc="Loss component of Location Marginal Price (LMP) in monetary units per MW.")

    # Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
    costLMP = CostPerEnergyUnit(desc="Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.")

    #--------------------------------------------------------------------------
    #  Begin "PnodeClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime", "congestLMP", "lossLMP", "costLMP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "Pnode",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.PnodeClearing",
        title="PnodeClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PnodeClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResourceBid" class:
#------------------------------------------------------------------------------

class ResourceBid(Bid):
    """ Energy bid for generation, load, or virtual type for the whole of the market-trading period (i.e., one day in day ahead market or one hour in the real time market)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum number of startups per day.
    startUpsMaxDay = Int(desc="Maximum number of startups per day.")

    # Minimum amount of energy per day which has to be produced during the trading period in MWh
    energyMinDay = ActivePower(desc="Minimum amount of energy per day which has to be produced during the trading period in MWh")

    # Maximum amount of energy per day which can be produced during the trading period in MWh
    energyMaxDay = ActivePower(desc="Maximum amount of energy per day which can be produced during the trading period in MWh")

    # True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent
    virtual = Bool(desc="True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent")

    # Maximum number of startups per week.
    startUpsMaxWeek = Int(desc="Maximum number of startups per week.")

    # Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
    commodityType = Str(desc="Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve")

    # Maximum number of shutdowns per week.
    shutDownsMaxWeek = Int(desc="Maximum number of shutdowns per week.")

    # Maximum number of shutdowns per day.
    shutDownsMaxDay = Int(desc="Maximum number of shutdowns per day.")

    #--------------------------------------------------------------------------
    #  Begin "ResourceBid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stopTime", "startTime", "marketType", "startUpsMaxDay", "energyMinDay", "energyMaxDay", "virtual", "startUpsMaxWeek", "commodityType", "shutDownsMaxWeek", "shutDownsMaxDay",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ProductBids", "BidClearing",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ResourceBid",
        title="ResourceBid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResourceBid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadBid" class:
#------------------------------------------------------------------------------

class LoadBid(ResourceBid):
    LoadReductionPriceCurve = Instance("CIM.IEC61968.Informative.MarketOperations.LoadReductionPriceCurve",
        transient=True,
        opposite="LoadBids",
        editor=InstanceEditor(name="_loadreductionpricecurves"))

    def _get_loadreductionpricecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.LoadReductionPriceCurve" ]
        else:
            return []

    _loadreductionpricecurves = Property(fget=_get_loadreductionpricecurves)

    RegisteredLoad = Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredLoad",
        transient=True,
        opposite="LoadBids",
        editor=InstanceEditor(name="_registeredloads"))

    def _get_registeredloads(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RegisteredLoad" ]
        else:
            return []

    _registeredloads = Property(fget=_get_registeredloads)

    # Maximum rate load may be restored (MW/minute)
    pickUpRampRate = Instance("CIM.RateOfChange",
        desc="Maximum rate load may be restored (MW/minute)",
        transient=True,
        editor=InstanceEditor(name="_rateofchanges"))

    def _get_rateofchanges(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.RateOfChange" ]
        else:
            return []

    _rateofchanges = Property(fget=_get_rateofchanges)

    # Maximum rate that load can be reduced (MW/minute)
    dropRampRate = Instance("CIM.RateOfChange",
        desc="Maximum rate that load can be reduced (MW/minute)",
        transient=True,
        editor=InstanceEditor(name="_rateofchanges"))

    def _get_rateofchanges(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.RateOfChange" ]
        else:
            return []

    _rateofchanges = Property(fget=_get_rateofchanges)

    # Shortest time that load must be left at normal levels before a new load reduction.
    minTimeBetLoadRed = Minutes(desc="Shortest time that load must be left at normal levels before a new load reduction.")

    # Cost in $ at the minimum reduced load
    minLoadReductionCost = Money(desc="Cost in $ at the minimum reduced load")

    # Shortest period load reduction must be maintained before load can be restored to normal levels.
    minLoadReductionInterval = Minutes(desc="Shortest period load reduction must be maintained before load can be restored to normal levels.")

    # Minimum MW load below which it may not be reduced.
    minLoad = ActivePower(desc="Minimum MW load below which it may not be reduced.")

    # Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction.
    reqNoticeTime = Minutes(desc="Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction.")

    # Minimum MW for a load reduction (e.g., MW rating of a discrete pump.
    minLoadReduction = ActivePower(desc="Minimum MW for a load reduction (e.g., MW rating of a discrete pump.")

    # The fixed cost associated with committing a load reduction.
    shutdownCost = Money(desc="The fixed cost associated with committing a load reduction.")

    #--------------------------------------------------------------------------
    #  Begin "LoadBid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stopTime", "startTime", "marketType", "startUpsMaxDay", "energyMinDay", "energyMaxDay", "virtual", "startUpsMaxWeek", "commodityType", "shutDownsMaxWeek", "shutDownsMaxDay", "minTimeBetLoadRed", "minLoadReductionCost", "minLoadReductionInterval", "minLoad", "reqNoticeTime", "minLoadReduction", "shutdownCost",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ProductBids", "BidClearing", "LoadReductionPriceCurve", "RegisteredLoad", "pickUpRampRate", "dropRampRate",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.LoadBid",
        title="LoadBid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadBid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratingBid" class:
#------------------------------------------------------------------------------

class GeneratingBid(ResourceBid):
    # Resource startup ramp rate (MW/minute)
    startUpRampRate = Instance("CIM.RateOfChange",
        desc="Resource startup ramp rate (MW/minute)",
        transient=True,
        editor=InstanceEditor(name="_rateofchanges"))

    def _get_rateofchanges(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.RateOfChange" ]
        else:
            return []

    _rateofchanges = Property(fget=_get_rateofchanges)

    NotificationTimeCurve = Instance("CIM.IEC61968.Informative.MarketOperations.NotificationTimeCurve",
        transient=True,
        opposite="GeneratingBids",
        editor=InstanceEditor(name="_notificationtimecurves"))

    def _get_notificationtimecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.NotificationTimeCurve" ]
        else:
            return []

    _notificationtimecurves = Property(fget=_get_notificationtimecurves)

    RegisteredGenerator = Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator",
        transient=True,
        opposite="GeneratingBids",
        editor=InstanceEditor(name="_registeredgenerators"))

    def _get_registeredgenerators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator" ]
        else:
            return []

    _registeredgenerators = Property(fget=_get_registeredgenerators)

    StartUpCostCurve = Instance("CIM.IEC61968.Informative.MarketOperations.StartUpCostCurve",
        transient=True,
        opposite="GeneratingBids",
        editor=InstanceEditor(name="_startupcostcurves"))

    def _get_startupcostcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.StartUpCostCurve" ]
        else:
            return []

    _startupcostcurves = Property(fget=_get_startupcostcurves)

    BidSet = Instance("CIM.IEC61968.Informative.MarketOperations.BidSet",
        transient=True,
        opposite="GeneratingBids",
        editor=InstanceEditor(name="_bidsets"))

    def _get_bidsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BidSet" ]
        else:
            return []

    _bidsets = Property(fget=_get_bidsets)

    StartUpTimeCurve = Instance("CIM.IEC61968.Informative.MarketOperations.StartUpTimeCurve",
        transient=True,
        opposite="GeneratingBids",
        editor=InstanceEditor(name="_startuptimecurves"))

    def _get_startuptimecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.StartUpTimeCurve" ]
        else:
            return []

    _startuptimecurves = Property(fget=_get_startuptimecurves)

    # Power rating available for unit under emergency conditions greater than or equal to maximum economic limit.
    maxEmergencyMW = ActivePower(desc="Power rating available for unit under emergency conditions greater than or equal to maximum economic limit.")

    # Maximum high economic MW limit, that should not exceed the maximum operating MW limit
    maximumEconomicMW = ActivePower(desc="Maximum high economic MW limit, that should not exceed the maximum operating MW limit")

    # Low economic MW limit that must be greater than or equal to the minimum operating MW limit
    minimumEconomicMW = ActivePower(desc="Low economic MW limit that must be greater than or equal to the minimum operating MW limit")

    # Maximum down time.
    downTimeMax = Minutes(desc="Maximum down time.")

    # Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable)
    operatingMode = Str(desc="Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable)")

    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startupTime = Minutes(desc="Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied")

    # Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum.
    minEmergencyMW = ActivePower(desc="Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum.")

    # Resource fixed no load cost.
    noLoadCost = Money(desc="Resource fixed no load cost.")

    # Minimum time interval between unit shutdown and startup
    minimumDownTime = Minutes(desc="Minimum time interval between unit shutdown and startup")

    # Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time
    startUpType = Int(desc="Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time")

    # Minimum up time.
    upTimeMin = Minutes(desc="Minimum up time.")

    # Maximum up time.
    upTimeMax = Minutes(desc="Maximum up time.")

    # Time required for crew notification prior to start up of the unit.
    notificationTime = Minutes(desc="Time required for crew notification prior to start up of the unit.")

    #--------------------------------------------------------------------------
    #  Begin "GeneratingBid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stopTime", "startTime", "marketType", "startUpsMaxDay", "energyMinDay", "energyMaxDay", "virtual", "startUpsMaxWeek", "commodityType", "shutDownsMaxWeek", "shutDownsMaxDay", "maxEmergencyMW", "maximumEconomicMW", "minimumEconomicMW", "downTimeMax", "operatingMode", "startupTime", "minEmergencyMW", "noLoadCost", "minimumDownTime", "startUpType", "upTimeMin", "upTimeMax", "notificationTime",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ProductBids", "BidClearing", "startUpRampRate", "NotificationTimeCurve", "RegisteredGenerator", "StartUpCostCurve", "BidSet", "StartUpTimeCurve",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.GeneratingBid",
        title="GeneratingBid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratingBid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegisteredGenerator" class:
#------------------------------------------------------------------------------

class RegisteredGenerator(RegisteredResource):
    raiseRampRate = Instance("CIM.PowerROCPerMin",
        transient=True,
        editor=InstanceEditor(name="_powerrocpermins"))

    def _get_powerrocpermins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PowerROCPerMin" ]
        else:
            return []

    _powerrocpermins = Property(fget=_get_powerrocpermins)

    UnitInitialConditions = List(Instance("CIM.IEC61968.Informative.MarketOperations.UnitInitialConditions"))

    RampRateCurves = List(Instance("CIM.IEC61968.Informative.MarketOperations.RampRateCurve"))

    GeneratingBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.GeneratingBid"))

    # Regulation down response rate in MW per minute
    lowerControlRate = Instance("CIM.PowerROCPerMin",
        desc="Regulation down response rate in MW per minute",
        transient=True,
        editor=InstanceEditor(name="_powerrocpermins"))

    def _get_powerrocpermins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PowerROCPerMin" ]
        else:
            return []

    _powerrocpermins = Property(fget=_get_powerrocpermins)

    StartUpCostCurves = List(Instance("CIM.IEC61968.Informative.MarketOperations.StartUpCostCurve"))

    spinReserveRamp = Instance("CIM.PowerROCPerMin",
        transient=True,
        editor=InstanceEditor(name="_powerrocpermins"))

    def _get_powerrocpermins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PowerROCPerMin" ]
        else:
            return []

    _powerrocpermins = Property(fget=_get_powerrocpermins)

    GeneratingUnit = Instance("CIM.IEC61970.Generation.Production.GeneratingUnit",
        transient=True,
        opposite="RegisteredGenerator",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    lowerRampRate = Instance("CIM.PowerROCPerMin",
        transient=True,
        editor=InstanceEditor(name="_powerrocpermins"))

    def _get_powerrocpermins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PowerROCPerMin" ]
        else:
            return []

    _powerrocpermins = Property(fget=_get_powerrocpermins)

    # Regulation up response rate in MW per minute
    raiseControlRate = Instance("CIM.PowerROCPerMin",
        desc="Regulation up response rate in MW per minute",
        transient=True,
        editor=InstanceEditor(name="_powerrocpermins"))

    def _get_powerrocpermins(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.PowerROCPerMin" ]
        else:
            return []

    _powerrocpermins = Property(fget=_get_powerrocpermins)

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = ActivePower(desc="Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.")

    # High limit for secondary (AGC) control
    highControlLimit = ActivePower(desc="High limit for secondary (AGC) control")

    # This is the maximum operating MW limit the dispatcher can enter for this unit
    maximumOperatingMW = ActivePower(desc="This is the maximum operating MW limit the dispatcher can enter for this unit")

    # Low limit for secondary (AGC) control
    lowControlLImit = ActivePower(desc="Low limit for secondary (AGC) control")

    # This is the minimum operating MW limit the dispatcher can enter for this unit.
    minimumOperatingMW = ActivePower(desc="This is the minimum operating MW limit the dispatcher can enter for this unit.")

    #--------------------------------------------------------------------------
    #  Begin "RegisteredGenerator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "rtoID", "maximumAllowableSpinningReserve", "highControlLimit", "maximumOperatingMW", "lowControlLImit", "minimumOperatingMW",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Meters", "Markets", "ResourceGroups", "MarketProducts", "Pnode", "Organisation", "raiseRampRate", "UnitInitialConditions", "RampRateCurves", "GeneratingBids", "lowerControlRate", "StartUpCostCurves", "spinReserveRamp", "GeneratingUnit", "lowerRampRate", "raiseControlRate",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator",
        title="RegisteredGenerator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegisteredGenerator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketCaseClearing" class:
#------------------------------------------------------------------------------

class MarketCaseClearing(MarketFactors):
    """ Market case clearing results are posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AncillaryServiceClearing = List(Instance("CIM.IEC61968.Informative.MarketOperations.AncillaryServiceClearing"))

    # Last time and date clearing results were manually modified.
    modifiedDate = Date(desc="Last time and date clearing results were manually modified.")

    # Bid clearing results posted time and date.
    postedDate = Date(desc="Bid clearing results posted time and date.")

    # Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2'
    caseType = Str(desc="Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2'")

    #--------------------------------------------------------------------------
    #  Begin "MarketCaseClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime", "modifiedDate", "postedDate", "caseType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "AncillaryServiceClearing",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.MarketCaseClearing",
        title="MarketCaseClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketCaseClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegisteredLoad" class:
#------------------------------------------------------------------------------

class RegisteredLoad(RegisteredResource):
    LoadArea = Instance("CIM.IEC61970.LoadModel.LoadGroup",
        transient=True,
        opposite="RegisteredLoads",
        editor=InstanceEditor(name="_loadgroups"))

    def _get_loadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.LoadGroup" ]
        else:
            return []

    _loadgroups = Property(fget=_get_loadgroups)

    LoadBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.LoadBid"))

    #--------------------------------------------------------------------------
    #  Begin "RegisteredLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "rtoID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Meters", "Markets", "ResourceGroups", "MarketProducts", "Pnode", "Organisation", "LoadArea", "LoadBids",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.RegisteredLoad",
        title="RegisteredLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegisteredLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AncillaryServiceClearing" class:
#------------------------------------------------------------------------------

class AncillaryServiceClearing(MarketFactors):
    """ Ancillary services clearing results are posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MarketCaseClearing = Instance("CIM.IEC61968.Informative.MarketOperations.MarketCaseClearing",
        transient=True,
        opposite="AncillaryServiceClearing",
        editor=InstanceEditor(name="_marketcaseclearings"))

    def _get_marketcaseclearings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.MarketCaseClearing" ]
        else:
            return []

    _marketcaseclearings = Property(fget=_get_marketcaseclearings)

    # Cleared MWs.
    clearedMW = ActivePower(desc="Cleared MWs.")

    # Market clearing price (MCP) in monetary units.
    mcp = Money(desc="Market clearing price (MCP) in monetary units.")

    # Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
    commodityType = Str(desc="Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve")

    #--------------------------------------------------------------------------
    #  Begin "AncillaryServiceClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime", "clearedMW", "mcp", "commodityType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "MarketCaseClearing",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.AncillaryServiceClearing",
        title="AncillaryServiceClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AncillaryServiceClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NodeConstraintTerm" class:
#------------------------------------------------------------------------------

class NodeConstraintTerm(ConstraintTerm):
    """ To be used only to constrain a quantity that cannot be associated with a terminal. For example, a registered generating unit that is not electrically connected to the network.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConnectivityNode = Instance("CIM.IEC61970.Topology.ConnectivityNode",
        transient=True,
        opposite="NodeConstraintTerms",
        editor=InstanceEditor(name="_connectivitynodes"))

    def _get_connectivitynodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    #--------------------------------------------------------------------------
    #  Begin "NodeConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "factor", "function",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SecurityConstraintSum", "ConnectivityNode",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.NodeConstraintTerm",
        title="NodeConstraintTerm",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NodeConstraintTerm" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProductBidClearing" class:
#------------------------------------------------------------------------------

class ProductBidClearing(MarketFactors):
    """ Product Bid clearing results posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ProductBids = List(Instance("CIM.IEC61968.Informative.MarketOperations.ProductBid"))

    # Cleared MWs.
    clearedMW = ActivePower(desc="Cleared MWs.")

    #--------------------------------------------------------------------------
    #  Begin "ProductBidClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime", "clearedMW",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "ProductBids",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.ProductBidClearing",
        title="ProductBidClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProductBidClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransactionBid" class:
#------------------------------------------------------------------------------

class TransactionBid(Bid):
    """ Bilateral or scheduled transactions for energy and ancillary services considered by market clearing process
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Delivery_Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        transient=True,
        opposite="DeliveryTransactionBids",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    Receipt_Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        transient=True,
        opposite="ReceiptTransactionBids",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    EnergyTransId = Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction",
        transient=True,
        opposite="EnergyTransId",
        editor=InstanceEditor(name="_energytransactions"))

    def _get_energytransactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction" ]
        else:
            return []

    _energytransactions = Property(fget=_get_energytransactions)

    EnergyProfiles = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProfile"))

    #--------------------------------------------------------------------------
    #  Begin "TransactionBid" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stopTime", "startTime", "marketType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Market", "ProductBids", "BidClearing", "Delivery_Pnode", "Receipt_Pnode", "EnergyTransId", "EnergyProfiles",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.TransactionBid",
        title="TransactionBid",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransactionBid" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SecurityConstraintsClearing" class:
#------------------------------------------------------------------------------

class SecurityConstraintsClearing(MarketFactors):
    """ Binding security constrained clearing results posted for a given settlement period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Binding MW limit.
    mwLimit = ActivePower(desc="Binding MW limit.")

    # Optimal MW flow
    mwFlow = ActivePower(desc="Optimal MW flow")

    # Security constraint shadow price.
    shadowPrice = Money(desc="Security constraint shadow price.")

    #--------------------------------------------------------------------------
    #  Begin "SecurityConstraintsClearing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime", "mwLimit", "mwFlow", "shadowPrice",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.SecurityConstraintsClearing",
        title="SecurityConstraintsClearing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SecurityConstraintsClearing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SecurityConstraintSum" class:
#------------------------------------------------------------------------------

class SecurityConstraintSum(MarketFactors):
    """ Typically provided by RTO systems, constraints identified in both base case and critical contingency cases have to be transferred. A constraint has N (>=1) constraint terms. A term is represented by an instance of TerminalConstraintTerm.  The constraint expression is: minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue where: - cn is ConstraintTerm.factor  - xn is the flow at the terminal Flow into the associated equipment is positive for the purpose of ConnectivityNode NodeConstraintTerm  k is SecurityConstraintsLinear.resourceMW The units of k are assumed to be same as the units of the flows, xn.  The constants, cn, are dimensionless. With these conventions, cn and k are all positive for a typical constraint such as 'weighted sum of generation must be less than limit'. Furthermore, cn are all 1.0 for a case such as 'interface flow must be less than limit', assuming the terminals are chosen on the importing side of the interface.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DefaultConstraintLimit = Instance("CIM.IEC61968.Informative.MarketOperations.DefaultConstraintLimit",
        transient=True,
        opposite="SecurityConstraintSum",
        editor=InstanceEditor(name="_defaultconstraintlimits"))

    def _get_defaultconstraintlimits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.DefaultConstraintLimit" ]
        else:
            return []

    _defaultconstraintlimits = Property(fget=_get_defaultconstraintlimits)

    ConstraintTerms = List(Instance("CIM.IEC61968.Informative.MarketOperations.ConstraintTerm"))

    RTO = Instance("CIM.IEC61968.Informative.MarketOperations.RTO",
        transient=True,
        opposite="SecurityConstraintsLinear",
        editor=InstanceEditor(name="_rtos"))

    def _get_rtos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RTO" ]
        else:
            return []

    _rtos = Property(fget=_get_rtos)

    BaseCaseConstraintLimit = Instance("CIM.IEC61968.Informative.MarketOperations.BaseCaseConstraintLimit",
        transient=True,
        opposite="SecurityConstraintSum",
        editor=InstanceEditor(name="_basecaseconstraintlimits"))

    def _get_basecaseconstraintlimits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.BaseCaseConstraintLimit" ]
        else:
            return []

    _basecaseconstraintlimits = Property(fget=_get_basecaseconstraintlimits)

    ContingencyConstraintLimits = List(Instance("CIM.IEC61968.Informative.MarketOperations.ContingencyConstraintLimit"))

    #--------------------------------------------------------------------------
    #  Begin "SecurityConstraintSum" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "intervalStartTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoices", "Market", "DefaultConstraintLimit", "ConstraintTerms", "RTO", "BaseCaseConstraintLimit", "ContingencyConstraintLimits",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.MarketOperations.SecurityConstraintSum",
        title="SecurityConstraintSum",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SecurityConstraintSum" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
