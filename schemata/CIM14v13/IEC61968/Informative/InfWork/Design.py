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

from CIM14v13.IEC61968.Common.Document import Document

class Design(Document):
    """A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """

    def __init__(self, kind='estimated', price=0.0, costEstimate=0.0, DesignLocationsCUs=None, WorkCostDetails=None, ErpQuoteLineItem=None, DesignLocations=None, Work=None, ErpBOMs=None, ConditionFactors=None, WorkTasks=None, *args, **kw_args):
        """Initializes a new 'Design' instance.

        @param kind: Kind of this design. Values are: "estimated", "asBuilt", "other"
        @param price: Price to customer for implementing design. 
        @param costEstimate: Estimated cost (not price) of design. 
        @param DesignLocationsCUs:
        @param WorkCostDetails:
        @param ErpQuoteLineItem:
        @param DesignLocations:
        @param Work:
        @param ErpBOMs:
        @param ConditionFactors:
        @param WorkTasks:
        """
        #: Kind of this design.Values are: "estimated", "asBuilt", "other"
        self.kind = kind

        #: Price to customer for implementing design.
        self.price = price

        #: Estimated cost (not price) of design.
        self.costEstimate = costEstimate

        self._DesignLocationsCUs = []
        self.DesignLocationsCUs = [] if DesignLocationsCUs is None else DesignLocationsCUs

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        self._Work = None
        self.Work = Work

        self._ErpBOMs = []
        self.ErpBOMs = [] if ErpBOMs is None else ErpBOMs

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        super(Design, self).__init__(*args, **kw_args)

    def getDesignLocationsCUs(self):
        
        return self._DesignLocationsCUs

    def setDesignLocationsCUs(self, value):
        for p in self._DesignLocationsCUs:
            filtered = [q for q in p.Designs if q != self]
            self._DesignLocationsCUs._Designs = filtered
        for r in value:
            if self not in r._Designs:
                r._Designs.append(self)
        self._DesignLocationsCUs = value

    DesignLocationsCUs = property(getDesignLocationsCUs, setDesignLocationsCUs)

    def addDesignLocationsCUs(self, *DesignLocationsCUs):
        for obj in DesignLocationsCUs:
            if self not in obj._Designs:
                obj._Designs.append(self)
            self._DesignLocationsCUs.append(obj)

    def removeDesignLocationsCUs(self, *DesignLocationsCUs):
        for obj in DesignLocationsCUs:
            if self in obj._Designs:
                obj._Designs.remove(self)
            self._DesignLocationsCUs.remove(obj)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x._Design = None
        for y in value:
            y._Design = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._Design = self
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._Design = None
            self._WorkCostDetails.remove(obj)

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Design = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Design = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getDesignLocations(self):
        
        return self._DesignLocations

    def setDesignLocations(self, value):
        for p in self._DesignLocations:
            filtered = [q for q in p.Designs if q != self]
            self._DesignLocations._Designs = filtered
        for r in value:
            if self not in r._Designs:
                r._Designs.append(self)
        self._DesignLocations = value

    DesignLocations = property(getDesignLocations, setDesignLocations)

    def addDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self not in obj._Designs:
                obj._Designs.append(self)
            self._DesignLocations.append(obj)

    def removeDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self in obj._Designs:
                obj._Designs.remove(self)
            self._DesignLocations.remove(obj)

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.Designs if x != self]
            self._Work._Designs = filtered

        self._Work = value
        if self._Work is not None:
            self._Work._Designs.append(self)

    Work = property(getWork, setWork)

    def getErpBOMs(self):
        
        return self._ErpBOMs

    def setErpBOMs(self, value):
        for x in self._ErpBOMs:
            x._Design = None
        for y in value:
            y._Design = self
        self._ErpBOMs = value

    ErpBOMs = property(getErpBOMs, setErpBOMs)

    def addErpBOMs(self, *ErpBOMs):
        for obj in ErpBOMs:
            obj._Design = self
            self._ErpBOMs.append(obj)

    def removeErpBOMs(self, *ErpBOMs):
        for obj in ErpBOMs:
            obj._Design = None
            self._ErpBOMs.remove(obj)

    def getConditionFactors(self):
        
        return self._ConditionFactors

    def setConditionFactors(self, value):
        for p in self._ConditionFactors:
            filtered = [q for q in p.Designs if q != self]
            self._ConditionFactors._Designs = filtered
        for r in value:
            if self not in r._Designs:
                r._Designs.append(self)
        self._ConditionFactors = value

    ConditionFactors = property(getConditionFactors, setConditionFactors)

    def addConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self not in obj._Designs:
                obj._Designs.append(self)
            self._ConditionFactors.append(obj)

    def removeConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self in obj._Designs:
                obj._Designs.remove(self)
            self._ConditionFactors.remove(obj)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x._Design = None
        for y in value:
            y._Design = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._Design = self
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._Design = None
            self._WorkTasks.remove(obj)

