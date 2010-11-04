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

from CIM14v13.IEC61968.Informative.MarketOperations.MarketFactors import MarketFactors

class SecurityConstraintSum(MarketFactors):
    """Typically provided by RTO systems, constraints identified in both base case and critical contingency cases have to be transferred. A constraint has N (>=1) constraint terms. A term is represented by an instance of TerminalConstraintTerm.  The constraint expression is: minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue where: - cn is ConstraintTerm.factor  - xn is the flow at the terminal Flow into the associated equipment is positive for the purpose of ConnectivityNode NodeConstraintTerm  k is SecurityConstraintsLinear.resourceMW The units of k are assumed to be same as the units of the flows, xn.  The constants, cn, are dimensionless. With these conventions, cn and k are all positive for a typical constraint such as 'weighted sum of generation must be less than limit'. Furthermore, cn are all 1.0 for a case such as 'interface flow must be less than limit', assuming the terminals are chosen on the importing side of the interface.
    """

    def __init__(self, DefaultConstraintLimit=None, ConstraintTerms=None, RTO=None, BaseCaseConstraintLimit=None, ContingencyConstraintLimits=None, **kw_args):
        """Initializes a new 'SecurityConstraintSum' instance.

        @param DefaultConstraintLimit:
        @param ConstraintTerms:
        @param RTO:
        @param BaseCaseConstraintLimit:
        @param ContingencyConstraintLimits:
        """
        self._DefaultConstraintLimit = None
        self.DefaultConstraintLimit = DefaultConstraintLimit

        self._ConstraintTerms = []
        self.ConstraintTerms = [] if ConstraintTerms is None else ConstraintTerms

        self._RTO = None
        self.RTO = RTO

        self._BaseCaseConstraintLimit = None
        self.BaseCaseConstraintLimit = BaseCaseConstraintLimit

        self._ContingencyConstraintLimits = []
        self.ContingencyConstraintLimits = [] if ContingencyConstraintLimits is None else ContingencyConstraintLimits

        super(SecurityConstraintSum, self).__init__(**kw_args)

    def getDefaultConstraintLimit(self):
        
        return self._DefaultConstraintLimit

    def setDefaultConstraintLimit(self, value):
        if self._DefaultConstraintLimit is not None:
            self._DefaultConstraintLimit._SecurityConstraintSum = None

        self._DefaultConstraintLimit = value
        if self._DefaultConstraintLimit is not None:
            self._DefaultConstraintLimit._SecurityConstraintSum = self

    DefaultConstraintLimit = property(getDefaultConstraintLimit, setDefaultConstraintLimit)

    def getConstraintTerms(self):
        
        return self._ConstraintTerms

    def setConstraintTerms(self, value):
        for x in self._ConstraintTerms:
            x._SecurityConstraintSum = None
        for y in value:
            y._SecurityConstraintSum = self
        self._ConstraintTerms = value

    ConstraintTerms = property(getConstraintTerms, setConstraintTerms)

    def addConstraintTerms(self, *ConstraintTerms):
        for obj in ConstraintTerms:
            obj._SecurityConstraintSum = self
            self._ConstraintTerms.append(obj)

    def removeConstraintTerms(self, *ConstraintTerms):
        for obj in ConstraintTerms:
            obj._SecurityConstraintSum = None
            self._ConstraintTerms.remove(obj)

    def getRTO(self):
        
        return self._RTO

    def setRTO(self, value):
        if self._RTO is not None:
            filtered = [x for x in self.RTO.SecurityConstraintsLinear if x != self]
            self._RTO._SecurityConstraintsLinear = filtered

        self._RTO = value
        if self._RTO is not None:
            self._RTO._SecurityConstraintsLinear.append(self)

    RTO = property(getRTO, setRTO)

    def getBaseCaseConstraintLimit(self):
        
        return self._BaseCaseConstraintLimit

    def setBaseCaseConstraintLimit(self, value):
        if self._BaseCaseConstraintLimit is not None:
            self._BaseCaseConstraintLimit._SecurityConstraintSum = None

        self._BaseCaseConstraintLimit = value
        if self._BaseCaseConstraintLimit is not None:
            self._BaseCaseConstraintLimit._SecurityConstraintSum = self

    BaseCaseConstraintLimit = property(getBaseCaseConstraintLimit, setBaseCaseConstraintLimit)

    def getContingencyConstraintLimits(self):
        
        return self._ContingencyConstraintLimits

    def setContingencyConstraintLimits(self, value):
        for x in self._ContingencyConstraintLimits:
            x._SecurityConstraintSum = None
        for y in value:
            y._SecurityConstraintSum = self
        self._ContingencyConstraintLimits = value

    ContingencyConstraintLimits = property(getContingencyConstraintLimits, setContingencyConstraintLimits)

    def addContingencyConstraintLimits(self, *ContingencyConstraintLimits):
        for obj in ContingencyConstraintLimits:
            obj._SecurityConstraintSum = self
            self._ContingencyConstraintLimits.append(obj)

    def removeContingencyConstraintLimits(self, *ContingencyConstraintLimits):
        for obj in ContingencyConstraintLimits:
            obj._SecurityConstraintSum = None
            self._ContingencyConstraintLimits.remove(obj)

