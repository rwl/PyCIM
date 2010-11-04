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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Token(IdentifiedObject):
    """The token that is transferred to the payment meter.
    """

    def __init__(self, code='', comment='', PointOfSale=None, **kw_args):
        """Initializes a new 'Token' instance.

        @param code: Coded representation of the token that is transferred to the payment meter. 
        @param comment: Free-format note relevant to this token. 
        @param PointOfSale: PointOfSale tha sold or dispensed this Token.
        """
        #: Coded representation of the token that is transferred to the payment meter.
        self.code = code

        #: Free-format note relevant to this token.
        self.comment = comment

        self._PointOfSale = None
        self.PointOfSale = PointOfSale

        super(Token, self).__init__(**kw_args)

    def getPointOfSale(self):
        """PointOfSale tha sold or dispensed this Token.
        """
        return self._PointOfSale

    def setPointOfSale(self, value):
        if self._PointOfSale is not None:
            filtered = [x for x in self.PointOfSale.Tokens if x != self]
            self._PointOfSale._Tokens = filtered

        self._PointOfSale = value
        if self._PointOfSale is not None:
            self._PointOfSale._Tokens.append(self)

    PointOfSale = property(getPointOfSale, setPointOfSale)

