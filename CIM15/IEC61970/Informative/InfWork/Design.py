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

from CIM15.IEC61968.Common.Document import Document

class Design(Document):
    """A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """

    def __init__(self, costEstimate=0.0, kind="asBuilt", price=0.0, DesignLocations=None, WorkCostDetails=None, ConditionFactors=None, WorkTasks=None, ErpBOMs=None, Work=None, DesignLocationsCUs=None, ErpQuoteLineItem=None, *args, **kw_args):
        """Initialises a new 'Design' instance.

        @param costEstimate: Estimated cost (not price) of design. 
        @param kind: Kind of this design. Values are: "asBuilt", "other", "estimated"
        @param price: Price to customer for implementing design. 
        @param DesignLocations:
        @param WorkCostDetails:
        @param ConditionFactors:
        @param WorkTasks:
        @param ErpBOMs:
        @param Work:
        @param DesignLocationsCUs:
        @param ErpQuoteLineItem:
        """
        #: Estimated cost (not price) of design.
        self.costEstimate = costEstimate

        #: Kind of this design. Values are: "asBuilt", "other", "estimated"
        self.kind = kind

        #: Price to customer for implementing design.
        self.price = price

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._ErpBOMs = []
        self.ErpBOMs = [] if ErpBOMs is None else ErpBOMs

        self._Work = None
        self.Work = Work

        self._DesignLocationsCUs = []
        self.DesignLocationsCUs = [] if DesignLocationsCUs is None else DesignLocationsCUs

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        super(Design, self).__init__(*args, **kw_args)

    _attrs = ["costEstimate", "kind", "price"]
    _attr_types = {"costEstimate": float, "kind": str, "price": float}
    _defaults = {"costEstimate": 0.0, "kind": "asBuilt", "price": 0.0}
    _enums = {"kind": "DesignKind"}
    _refs = ["DesignLocations", "WorkCostDetails", "ConditionFactors", "WorkTasks", "ErpBOMs", "Work", "DesignLocationsCUs", "ErpQuoteLineItem"]
    _many_refs = ["DesignLocations", "WorkCostDetails", "ConditionFactors", "WorkTasks", "ErpBOMs", "DesignLocationsCUs"]

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

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x.Design = None
        for y in value:
            y._Design = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.Design = self

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.Design = None

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
            x.Design = None
        for y in value:
            y._Design = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.Design = self

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.Design = None

    def getErpBOMs(self):
        
        return self._ErpBOMs

    def setErpBOMs(self, value):
        for x in self._ErpBOMs:
            x.Design = None
        for y in value:
            y._Design = self
        self._ErpBOMs = value

    ErpBOMs = property(getErpBOMs, setErpBOMs)

    def addErpBOMs(self, *ErpBOMs):
        for obj in ErpBOMs:
            obj.Design = self

    def removeErpBOMs(self, *ErpBOMs):
        for obj in ErpBOMs:
            obj.Design = None

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.Designs if x != self]
            self._Work._Designs = filtered

        self._Work = value
        if self._Work is not None:
            if self not in self._Work._Designs:
                self._Work._Designs.append(self)

    Work = property(getWork, setWork)

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

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Design = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem.Design = None
            self._ErpQuoteLineItem._Design = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

