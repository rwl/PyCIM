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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Transactor(IdentifiedObject):
    """The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.
    """

    def __init__(self, MerchantAccounts=None, *args, **kw_args):
        """Initialises a new 'Transactor' instance.

        @param MerchantAccounts: All merchant accounts registered with this transactor.
        """
        self._MerchantAccounts = []
        self.MerchantAccounts = [] if MerchantAccounts is None else MerchantAccounts

        super(Transactor, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MerchantAccounts"]
    _many_refs = ["MerchantAccounts"]

    def getMerchantAccounts(self):
        """All merchant accounts registered with this transactor.
        """
        return self._MerchantAccounts

    def setMerchantAccounts(self, value):
        for p in self._MerchantAccounts:
            filtered = [q for q in p.Transactors if q != self]
            self._MerchantAccounts._Transactors = filtered
        for r in value:
            if self not in r._Transactors:
                r._Transactors.append(self)
        self._MerchantAccounts = value

    MerchantAccounts = property(getMerchantAccounts, setMerchantAccounts)

    def addMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            if self not in obj._Transactors:
                obj._Transactors.append(self)
            self._MerchantAccounts.append(obj)

    def removeMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            if self in obj._Transactors:
                obj._Transactors.remove(self)
            self._MerchantAccounts.remove(obj)

