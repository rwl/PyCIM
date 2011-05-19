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

from CIM15.Element import Element

class UserAttribute(Element):
    """Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """

    def __init__(self, name='', value='', sequenceNumber=0, ErpLedgerEntries=None, ProcedureDataSets=None, Transaction=None, PropertySpecification=None, Procedure=None, PropertyAssets=None, RatingSpecification=None, ErpInvoiceLineItems=None, RatingAssets=None, *args, **kw_args):
        """Initialises a new 'UserAttribute' instance.

        @param name: Name of an attribute. 
        @param value: Value of an attribute, including unit information. 
        @param sequenceNumber: Sequence number for this attribute in a list of attributes. 
        @param ErpLedgerEntries:
        @param ProcedureDataSets:
        @param Transaction: Transaction for which this snapshot has been recorded.
        @param PropertySpecification:
        @param Procedure:
        @param PropertyAssets:
        @param RatingSpecification:
        @param ErpInvoiceLineItems:
        @param RatingAssets:
        """
        #: Name of an attribute.
        self.name = name

        #: Value of an attribute, including unit information.
        self.value = value

        #: Sequence number for this attribute in a list of attributes.
        self.sequenceNumber = sequenceNumber

        self._ErpLedgerEntries = []
        self.ErpLedgerEntries = [] if ErpLedgerEntries is None else ErpLedgerEntries

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._Transaction = None
        self.Transaction = Transaction

        self._PropertySpecification = None
        self.PropertySpecification = PropertySpecification

        self._Procedure = None
        self.Procedure = Procedure

        self._PropertyAssets = []
        self.PropertyAssets = [] if PropertyAssets is None else PropertyAssets

        self._RatingSpecification = None
        self.RatingSpecification = RatingSpecification

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._RatingAssets = []
        self.RatingAssets = [] if RatingAssets is None else RatingAssets

        super(UserAttribute, self).__init__(*args, **kw_args)

    _attrs = ["name", "value", "sequenceNumber"]
    _attr_types = {"name": str, "value": str, "sequenceNumber": int}
    _defaults = {"name": '', "value": '', "sequenceNumber": 0}
    _enums = {}
    _refs = ["ErpLedgerEntries", "ProcedureDataSets", "Transaction", "PropertySpecification", "Procedure", "PropertyAssets", "RatingSpecification", "ErpInvoiceLineItems", "RatingAssets"]
    _many_refs = ["ErpLedgerEntries", "ProcedureDataSets", "PropertyAssets", "ErpInvoiceLineItems", "RatingAssets"]

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
            if self not in self._Transaction._UserAttributes:
                self._Transaction._UserAttributes.append(self)

    Transaction = property(getTransaction, setTransaction)

    def getPropertySpecification(self):
        
        return self._PropertySpecification

    def setPropertySpecification(self, value):
        if self._PropertySpecification is not None:
            filtered = [x for x in self.PropertySpecification.AssetProperites if x != self]
            self._PropertySpecification._AssetProperites = filtered

        self._PropertySpecification = value
        if self._PropertySpecification is not None:
            if self not in self._PropertySpecification._AssetProperites:
                self._PropertySpecification._AssetProperites.append(self)

    PropertySpecification = property(getPropertySpecification, setPropertySpecification)

    def getProcedure(self):
        
        return self._Procedure

    def setProcedure(self, value):
        if self._Procedure is not None:
            filtered = [x for x in self.Procedure.ProcedureValues if x != self]
            self._Procedure._ProcedureValues = filtered

        self._Procedure = value
        if self._Procedure is not None:
            if self not in self._Procedure._ProcedureValues:
                self._Procedure._ProcedureValues.append(self)

    Procedure = property(getProcedure, setProcedure)

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

    def getRatingSpecification(self):
        
        return self._RatingSpecification

    def setRatingSpecification(self, value):
        if self._RatingSpecification is not None:
            filtered = [x for x in self.RatingSpecification.Ratings if x != self]
            self._RatingSpecification._Ratings = filtered

        self._RatingSpecification = value
        if self._RatingSpecification is not None:
            if self not in self._RatingSpecification._Ratings:
                self._RatingSpecification._Ratings.append(self)

    RatingSpecification = property(getRatingSpecification, setRatingSpecification)

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

