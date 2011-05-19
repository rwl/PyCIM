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

class Charge(IdentifiedObject):
    """A charge element associated with other entities such as tariff structures, auxiliary agreements or other charge elements. The total charge amount applicable to this instance of charge is the sum of fixed and variable portion.A charge element associated with other entities such as tariff structures, auxiliary agreements or other charge elements. The total charge amount applicable to this instance of charge is the sum of fixed and variable portion.
    """

    def __init__(self, variablePortion=0.0, kind="other", ConsumptionTariffIntervals=None, TimeTariffIntervals=None, AuxiliaryAccounts=None, ChildCharges=None, fixedPortion=None, ParentCharge=None, *args, **kw_args):
        """Initialises a new 'Charge' instance.

        @param variablePortion: The variable portion of this charge element, calculated as a percentage of the total amount of a parent charge. 
        @param kind: The kind of charge to be applied. Values are: "other", "demandCharge", "consumptionCharge", "auxiliaryCharge", "taxCharge"
        @param ConsumptionTariffIntervals: Tariff intervals to which this consumption-based charge must be levied.
        @param TimeTariffIntervals: Tariff intervals to which this time-based charge must be levied.
        @param AuxiliaryAccounts: All auxiliary accounts to which this charge must be levied.
        @param ChildCharges: All sub-components of this complex charge.
        @param fixedPortion: The fixed portion of this charge element.
        @param ParentCharge: Parent of this charge sub-component.
        """
        #: The variable portion of this charge element, calculated as a percentage of the total amount of a parent charge.
        self.variablePortion = variablePortion

        #: The kind of charge to be applied. Values are: "other", "demandCharge", "consumptionCharge", "auxiliaryCharge", "taxCharge"
        self.kind = kind

        self._ConsumptionTariffIntervals = []
        self.ConsumptionTariffIntervals = [] if ConsumptionTariffIntervals is None else ConsumptionTariffIntervals

        self._TimeTariffIntervals = []
        self.TimeTariffIntervals = [] if TimeTariffIntervals is None else TimeTariffIntervals

        self._AuxiliaryAccounts = []
        self.AuxiliaryAccounts = [] if AuxiliaryAccounts is None else AuxiliaryAccounts

        self._ChildCharges = []
        self.ChildCharges = [] if ChildCharges is None else ChildCharges

        self.fixedPortion = fixedPortion

        self._ParentCharge = None
        self.ParentCharge = ParentCharge

        super(Charge, self).__init__(*args, **kw_args)

    _attrs = ["variablePortion", "kind"]
    _attr_types = {"variablePortion": float, "kind": str}
    _defaults = {"variablePortion": 0.0, "kind": "other"}
    _enums = {"kind": "ChargeKind"}
    _refs = ["ConsumptionTariffIntervals", "TimeTariffIntervals", "AuxiliaryAccounts", "ChildCharges", "fixedPortion", "ParentCharge"]
    _many_refs = ["ConsumptionTariffIntervals", "TimeTariffIntervals", "AuxiliaryAccounts", "ChildCharges"]

    def getConsumptionTariffIntervals(self):
        """Tariff intervals to which this consumption-based charge must be levied.
        """
        return self._ConsumptionTariffIntervals

    def setConsumptionTariffIntervals(self, value):
        for p in self._ConsumptionTariffIntervals:
            filtered = [q for q in p.Charges if q != self]
            self._ConsumptionTariffIntervals._Charges = filtered
        for r in value:
            if self not in r._Charges:
                r._Charges.append(self)
        self._ConsumptionTariffIntervals = value

    ConsumptionTariffIntervals = property(getConsumptionTariffIntervals, setConsumptionTariffIntervals)

    def addConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self not in obj._Charges:
                obj._Charges.append(self)
            self._ConsumptionTariffIntervals.append(obj)

    def removeConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self in obj._Charges:
                obj._Charges.remove(self)
            self._ConsumptionTariffIntervals.remove(obj)

    def getTimeTariffIntervals(self):
        """Tariff intervals to which this time-based charge must be levied.
        """
        return self._TimeTariffIntervals

    def setTimeTariffIntervals(self, value):
        for p in self._TimeTariffIntervals:
            filtered = [q for q in p.Charges if q != self]
            self._TimeTariffIntervals._Charges = filtered
        for r in value:
            if self not in r._Charges:
                r._Charges.append(self)
        self._TimeTariffIntervals = value

    TimeTariffIntervals = property(getTimeTariffIntervals, setTimeTariffIntervals)

    def addTimeTariffIntervals(self, *TimeTariffIntervals):
        for obj in TimeTariffIntervals:
            if self not in obj._Charges:
                obj._Charges.append(self)
            self._TimeTariffIntervals.append(obj)

    def removeTimeTariffIntervals(self, *TimeTariffIntervals):
        for obj in TimeTariffIntervals:
            if self in obj._Charges:
                obj._Charges.remove(self)
            self._TimeTariffIntervals.remove(obj)

    def getAuxiliaryAccounts(self):
        """All auxiliary accounts to which this charge must be levied.
        """
        return self._AuxiliaryAccounts

    def setAuxiliaryAccounts(self, value):
        for p in self._AuxiliaryAccounts:
            filtered = [q for q in p.Charges if q != self]
            self._AuxiliaryAccounts._Charges = filtered
        for r in value:
            if self not in r._Charges:
                r._Charges.append(self)
        self._AuxiliaryAccounts = value

    AuxiliaryAccounts = property(getAuxiliaryAccounts, setAuxiliaryAccounts)

    def addAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            if self not in obj._Charges:
                obj._Charges.append(self)
            self._AuxiliaryAccounts.append(obj)

    def removeAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            if self in obj._Charges:
                obj._Charges.remove(self)
            self._AuxiliaryAccounts.remove(obj)

    def getChildCharges(self):
        """All sub-components of this complex charge.
        """
        return self._ChildCharges

    def setChildCharges(self, value):
        for x in self._ChildCharges:
            x.ParentCharge = None
        for y in value:
            y._ParentCharge = self
        self._ChildCharges = value

    ChildCharges = property(getChildCharges, setChildCharges)

    def addChildCharges(self, *ChildCharges):
        for obj in ChildCharges:
            obj.ParentCharge = self

    def removeChildCharges(self, *ChildCharges):
        for obj in ChildCharges:
            obj.ParentCharge = None

    # The fixed portion of this charge element.
    fixedPortion = None

    def getParentCharge(self):
        """Parent of this charge sub-component.
        """
        return self._ParentCharge

    def setParentCharge(self, value):
        if self._ParentCharge is not None:
            filtered = [x for x in self.ParentCharge.ChildCharges if x != self]
            self._ParentCharge._ChildCharges = filtered

        self._ParentCharge = value
        if self._ParentCharge is not None:
            if self not in self._ParentCharge._ChildCharges:
                self._ParentCharge._ChildCharges.append(self)

    ParentCharge = property(getParentCharge, setParentCharge)

