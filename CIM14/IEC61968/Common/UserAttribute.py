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

from CIM14.Element import Element

class UserAttribute(Element):
    """Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """

    def __init__(self, value='', sequenceNumber=0, name='', PropertyAssets=None, Transaction=None, RatingAssets=None, *args, **kw_args):
        """Initialises a new 'UserAttribute' instance.

        @param value: Value of an attribute, including unit information. 
        @param sequenceNumber: Sequence number for this attribute in a list of attributes. 
        @param name: Name of an attribute. 
        @param PropertyAssets:
        @param Transaction: Transaction for which this snapshot has been recorded.
        @param RatingAssets:
        """
        #: Value of an attribute, including unit information.
        self.value = value

        #: Sequence number for this attribute in a list of attributes.
        self.sequenceNumber = sequenceNumber

        #: Name of an attribute.
        self.name = name

        self._PropertyAssets = []
        self.PropertyAssets = [] if PropertyAssets is None else PropertyAssets

        self._Transaction = None
        self.Transaction = Transaction

        self._RatingAssets = []
        self.RatingAssets = [] if RatingAssets is None else RatingAssets

        super(UserAttribute, self).__init__(*args, **kw_args)

    _attrs = ["value", "sequenceNumber", "name"]
    _attr_types = {"value": str, "sequenceNumber": int, "name": str}
    _defaults = {"value": '', "sequenceNumber": 0, "name": ''}
    _enums = {}
    _refs = ["PropertyAssets", "Transaction", "RatingAssets"]
    _many_refs = ["PropertyAssets", "RatingAssets"]

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

