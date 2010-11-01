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

from CIM14v13.Element import Element

class UserAttribute(Element):
    """Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """

    def __init__(self, sequenceNumber=0, value='', name='', PropertySpecification=None, RatingSpecification=None, PropertyAssets=None, RatingAssets=None, ErpLedgerEntries=None, ProcedureDataSets=None, Transaction=None, Procedure=None, PassThroughBills=None, ErpInvoiceLineItems=None, BillDeterminants=None, ErpStatementLineItems=None, *args, **kw_args):
        """Initializes a new 'UserAttribute' instance.

        @param sequenceNumber: Sequence number for this attribute in a list of attributes. 
        @param value: Value of an attribute, including unit information. 
        @param name: Name of an attribute. 
        @param PropertySpecification:
        @param RatingSpecification:
        @param PropertyAssets:
        @param RatingAssets:
        @param ErpLedgerEntries:
        @param ProcedureDataSets:
        @param Transaction: Transaction for which this snapshot has been recorded.
        @param Procedure:
        @param PassThroughBills:
        @param ErpInvoiceLineItems:
        @param BillDeterminants:
        @param ErpStatementLineItems:
        """
        #: Sequence number for this attribute in a list of attributes. 
        self.sequenceNumber = sequenceNumber

        #: Value of an attribute, including unit information. 
        self.value = value

        #: Name of an attribute. 
        self.name = name

        self._PropertySpecification = None
        self.PropertySpecification = PropertySpecification

        self._RatingSpecification = None
        self.RatingSpecification = RatingSpecification

        self._PropertyAssets = []
        self.PropertyAssets = [] if PropertyAssets is None else PropertyAssets

        self._RatingAssets = []
        self.RatingAssets = [] if RatingAssets is None else RatingAssets

        self._ErpLedgerEntries = []
        self.ErpLedgerEntries = [] if ErpLedgerEntries is None else ErpLedgerEntries

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._Transaction = None
        self.Transaction = Transaction

        self._Procedure = None
        self.Procedure = Procedure

        self._PassThroughBills = []
        self.PassThroughBills = [] if PassThroughBills is None else PassThroughBills

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._BillDeterminants = []
        self.BillDeterminants = [] if BillDeterminants is None else BillDeterminants

        self._ErpStatementLineItems = []
        self.ErpStatementLineItems = [] if ErpStatementLineItems is None else ErpStatementLineItems

        super(UserAttribute, self).__init__(*args, **kw_args)

    def getPropertySpecification(self):
        
        return self._PropertySpecification

    def setPropertySpecification(self, value):
        if self._PropertySpecification is not None:
            filtered = [x for x in self.PropertySpecification.AssetProperites if x != self]
            self._PropertySpecification._AssetProperites = filtered

        self._PropertySpecification = value
        if self._PropertySpecification is not None:
            self._PropertySpecification._AssetProperites.append(self)

    PropertySpecification = property(getPropertySpecification, setPropertySpecification)

    def getRatingSpecification(self):
        
        return self._RatingSpecification

    def setRatingSpecification(self, value):
        if self._RatingSpecification is not None:
            filtered = [x for x in self.RatingSpecification.Ratings if x != self]
            self._RatingSpecification._Ratings = filtered

        self._RatingSpecification = value
        if self._RatingSpecification is not None:
            self._RatingSpecification._Ratings.append(self)

    RatingSpecification = property(getRatingSpecification, setRatingSpecification)

    def getPropertyAssets(self):
        
        return self._PropertyAssets

    def setPropertyAssets(self, value):
        for p in self._PropertyAssets:
            filtered = [q for q in p.Properties if q != self]
            self._PropertyAssets._Properties = filtered
        for r in value:
            if self not in r._Properties:
                r._Properties.append(self)
        self._PropertyAssets = value

    PropertyAssets = property(getPropertyAssets, setPropertyAssets)

    def addPropertyAssets(self, *PropertyAssets):
        for obj in PropertyAssets:
            if self not in obj._Properties:
                obj._Properties.append(self)
            self._PropertyAssets.append(obj)

    def removePropertyAssets(self, *PropertyAssets):
        for obj in PropertyAssets:
            if self in obj._Properties:
                obj._Properties.remove(self)
            self._PropertyAssets.remove(obj)

    def getRatingAssets(self):
        
        return self._RatingAssets

    def setRatingAssets(self, value):
        for p in self._RatingAssets:
            filtered = [q for q in p.Ratings if q != self]
            self._RatingAssets._Ratings = filtered
        for r in value:
            if self not in r._Ratings:
                r._Ratings.append(self)
        self._RatingAssets = value

    RatingAssets = property(getRatingAssets, setRatingAssets)

    def addRatingAssets(self, *RatingAssets):
        for obj in RatingAssets:
            if self not in obj._Ratings:
                obj._Ratings.append(self)
            self._RatingAssets.append(obj)

    def removeRatingAssets(self, *RatingAssets):
        for obj in RatingAssets:
            if self in obj._Ratings:
                obj._Ratings.remove(self)
            self._RatingAssets.remove(obj)

    def getErpLedgerEntries(self):
        
        return self._ErpLedgerEntries

    def setErpLedgerEntries(self, value):
        for p in self._ErpLedgerEntries:
            filtered = [q for q in p.UserAttributes if q != self]
            self._ErpLedgerEntries._UserAttributes = filtered
        for r in value:
            if self not in r._UserAttributes:
                r._UserAttributes.append(self)
        self._ErpLedgerEntries = value

    ErpLedgerEntries = property(getErpLedgerEntries, setErpLedgerEntries)

    def addErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            if self not in obj._UserAttributes:
                obj._UserAttributes.append(self)
            self._ErpLedgerEntries.append(obj)

    def removeErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            if self in obj._UserAttributes:
                obj._UserAttributes.remove(self)
            self._ErpLedgerEntries.remove(obj)

    def getProcedureDataSets(self):
        
        return self._ProcedureDataSets

    def setProcedureDataSets(self, value):
        for p in self._ProcedureDataSets:
            filtered = [q for q in p.Properties if q != self]
            self._ProcedureDataSets._Properties = filtered
        for r in value:
            if self not in r._Properties:
                r._Properties.append(self)
        self._ProcedureDataSets = value

    ProcedureDataSets = property(getProcedureDataSets, setProcedureDataSets)

    def addProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self not in obj._Properties:
                obj._Properties.append(self)
            self._ProcedureDataSets.append(obj)

    def removeProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self in obj._Properties:
                obj._Properties.remove(self)
            self._ProcedureDataSets.remove(obj)

    def getTransaction(self):
        """Transaction for which this snapshot has been recorded.
        """
        return self._Transaction

    def setTransaction(self, value):
        if self._Transaction is not None:
            filtered = [x for x in self.Transaction.UserAttributes if x != self]
            self._Transaction._UserAttributes = filtered

        self._Transaction = value
        if self._Transaction is not None:
            self._Transaction._UserAttributes.append(self)

    Transaction = property(getTransaction, setTransaction)

    def getProcedure(self):
        
        return self._Procedure

    def setProcedure(self, value):
        if self._Procedure is not None:
            filtered = [x for x in self.Procedure.ProcedureValues if x != self]
            self._Procedure._ProcedureValues = filtered

        self._Procedure = value
        if self._Procedure is not None:
            self._Procedure._ProcedureValues.append(self)

    Procedure = property(getProcedure, setProcedure)

    def getPassThroughBills(self):
        
        return self._PassThroughBills

    def setPassThroughBills(self, value):
        for p in self._PassThroughBills:
            filtered = [q for q in p.UserAttributes if q != self]
            self._PassThroughBills._UserAttributes = filtered
        for r in value:
            if self not in r._UserAttributes:
                r._UserAttributes.append(self)
        self._PassThroughBills = value

    PassThroughBills = property(getPassThroughBills, setPassThroughBills)

    def addPassThroughBills(self, *PassThroughBills):
        for obj in PassThroughBills:
            if self not in obj._UserAttributes:
                obj._UserAttributes.append(self)
            self._PassThroughBills.append(obj)

    def removePassThroughBills(self, *PassThroughBills):
        for obj in PassThroughBills:
            if self in obj._UserAttributes:
                obj._UserAttributes.remove(self)
            self._PassThroughBills.remove(obj)

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for p in self._ErpInvoiceLineItems:
            filtered = [q for q in p.UserAttributes if q != self]
            self._ErpInvoiceLineItems._UserAttributes = filtered
        for r in value:
            if self not in r._UserAttributes:
                r._UserAttributes.append(self)
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self not in obj._UserAttributes:
                obj._UserAttributes.append(self)
            self._ErpInvoiceLineItems.append(obj)

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self in obj._UserAttributes:
                obj._UserAttributes.remove(self)
            self._ErpInvoiceLineItems.remove(obj)

    def getBillDeterminants(self):
        
        return self._BillDeterminants

    def setBillDeterminants(self, value):
        for p in self._BillDeterminants:
            filtered = [q for q in p.UserAttributes if q != self]
            self._BillDeterminants._UserAttributes = filtered
        for r in value:
            if self not in r._UserAttributes:
                r._UserAttributes.append(self)
        self._BillDeterminants = value

    BillDeterminants = property(getBillDeterminants, setBillDeterminants)

    def addBillDeterminants(self, *BillDeterminants):
        for obj in BillDeterminants:
            if self not in obj._UserAttributes:
                obj._UserAttributes.append(self)
            self._BillDeterminants.append(obj)

    def removeBillDeterminants(self, *BillDeterminants):
        for obj in BillDeterminants:
            if self in obj._UserAttributes:
                obj._UserAttributes.remove(self)
            self._BillDeterminants.remove(obj)

    def getErpStatementLineItems(self):
        
        return self._ErpStatementLineItems

    def setErpStatementLineItems(self, value):
        for p in self._ErpStatementLineItems:
            filtered = [q for q in p.UserAttributes if q != self]
            self._ErpStatementLineItems._UserAttributes = filtered
        for r in value:
            if self not in r._UserAttributes:
                r._UserAttributes.append(self)
        self._ErpStatementLineItems = value

    ErpStatementLineItems = property(getErpStatementLineItems, setErpStatementLineItems)

    def addErpStatementLineItems(self, *ErpStatementLineItems):
        for obj in ErpStatementLineItems:
            if self not in obj._UserAttributes:
                obj._UserAttributes.append(self)
            self._ErpStatementLineItems.append(obj)

    def removeErpStatementLineItems(self, *ErpStatementLineItems):
        for obj in ErpStatementLineItems:
            if self in obj._UserAttributes:
                obj._UserAttributes.remove(self)
            self._ErpStatementLineItems.remove(obj)

