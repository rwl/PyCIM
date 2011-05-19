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

class Seal(IdentifiedObject):
    """Physically controls access to AssetContainers.Physically controls access to AssetContainers.
    """

    def __init__(self, appliedDateTime='', sealNumber='', kind="lead", condition="open", AssetContainer=None, *args, **kw_args):
        """Initialises a new 'Seal' instance.

        @param appliedDateTime: Date and time this seal has been applied. 
        @param sealNumber: (reserved word) Seal number. 
        @param kind: Kind of seal. Values are: "lead", "other", "steel", "lock"
        @param condition: Condition of seal. Values are: "open", "broken", "other", "missing", "locked"
        @param AssetContainer: Asset container to which this seal is applied.
        """
        #: Date and time this seal has been applied.
        self.appliedDateTime = appliedDateTime

        #: (reserved word) Seal number.
        self.sealNumber = sealNumber

        #: Kind of seal. Values are: "lead", "other", "steel", "lock"
        self.kind = kind

        #: Condition of seal. Values are: "open", "broken", "other", "missing", "locked"
        self.condition = condition

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        super(Seal, self).__init__(*args, **kw_args)

    _attrs = ["appliedDateTime", "sealNumber", "kind", "condition"]
    _attr_types = {"appliedDateTime": str, "sealNumber": str, "kind": str, "condition": str}
    _defaults = {"appliedDateTime": '', "sealNumber": '', "kind": "lead", "condition": "open"}
    _enums = {"kind": "SealKind", "condition": "SealConditionKind"}
    _refs = ["AssetContainer"]
    _many_refs = []

    def getAssetContainer(self):
        """Asset container to which this seal is applied.
        """
        return self._AssetContainer

    def setAssetContainer(self, value):
        if self._AssetContainer is not None:
            filtered = [x for x in self.AssetContainer.Seals if x != self]
            self._AssetContainer._Seals = filtered

        self._AssetContainer = value
        if self._AssetContainer is not None:
            if self not in self._AssetContainer._Seals:
                self._AssetContainer._Seals.append(self)

    AssetContainer = property(getAssetContainer, setAssetContainer)

