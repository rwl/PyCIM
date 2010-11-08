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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MetaBlockConnectable(IdentifiedObject):
    """This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.
    """

    def __init__(self, StandardControlBlock_MetaBlockStateReference=None, MetaBlockOutputReference=None, MetaBlockStateReference=None, BlockInputReference=None, StandardControlBlock_MetaBlockInputReference=None, StandardControlBlock_MetaBlockParameterReference=None, MetaBlockParameterReference=None, StandardControlBlock_MetaBlockOutputReference=None, MetaBlockInputReference=None, *args, **kw_args):
        """Initialises a new 'MetaBlockConnectable' instance.

        @param StandardControlBlock_MetaBlockStateReference:
        @param MetaBlockOutputReference:
        @param MetaBlockStateReference:
        @param BlockInputReference: Each block reference input is usually tied to one (sometimes zero for optional inputs) external block inputs or internal block reference outputs.
        @param StandardControlBlock_MetaBlockInputReference:
        @param StandardControlBlock_MetaBlockParameterReference:
        @param MetaBlockParameterReference:
        @param StandardControlBlock_MetaBlockOutputReference:
        @param MetaBlockInputReference:
        """
        self._StandardControlBlock_MetaBlockStateReference = []
        self.StandardControlBlock_MetaBlockStateReference = [] if StandardControlBlock_MetaBlockStateReference is None else StandardControlBlock_MetaBlockStateReference

        self._MetaBlockOutputReference = []
        self.MetaBlockOutputReference = [] if MetaBlockOutputReference is None else MetaBlockOutputReference

        self._MetaBlockStateReference = []
        self.MetaBlockStateReference = [] if MetaBlockStateReference is None else MetaBlockStateReference

        self._BlockInputReference = []
        self.BlockInputReference = [] if BlockInputReference is None else BlockInputReference

        self._StandardControlBlock_MetaBlockInputReference = []
        self.StandardControlBlock_MetaBlockInputReference = [] if StandardControlBlock_MetaBlockInputReference is None else StandardControlBlock_MetaBlockInputReference

        self._StandardControlBlock_MetaBlockParameterReference = []
        self.StandardControlBlock_MetaBlockParameterReference = [] if StandardControlBlock_MetaBlockParameterReference is None else StandardControlBlock_MetaBlockParameterReference

        self._MetaBlockParameterReference = []
        self.MetaBlockParameterReference = [] if MetaBlockParameterReference is None else MetaBlockParameterReference

        self._StandardControlBlock_MetaBlockOutputReference = []
        self.StandardControlBlock_MetaBlockOutputReference = [] if StandardControlBlock_MetaBlockOutputReference is None else StandardControlBlock_MetaBlockOutputReference

        self._MetaBlockInputReference = []
        self.MetaBlockInputReference = [] if MetaBlockInputReference is None else MetaBlockInputReference

        super(MetaBlockConnectable, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["StandardControlBlock_MetaBlockStateReference", "MetaBlockOutputReference", "MetaBlockStateReference", "BlockInputReference", "StandardControlBlock_MetaBlockInputReference", "StandardControlBlock_MetaBlockParameterReference", "MetaBlockParameterReference", "StandardControlBlock_MetaBlockOutputReference", "MetaBlockInputReference"]
    _many_refs = ["StandardControlBlock_MetaBlockStateReference", "MetaBlockOutputReference", "MetaBlockStateReference", "BlockInputReference", "StandardControlBlock_MetaBlockInputReference", "StandardControlBlock_MetaBlockParameterReference", "MetaBlockParameterReference", "StandardControlBlock_MetaBlockOutputReference", "MetaBlockInputReference"]

    def getStandardControlBlock_MetaBlockStateReference(self):
        
        return self._StandardControlBlock_MetaBlockStateReference

    def setStandardControlBlock_MetaBlockStateReference(self, value):
        for x in self._StandardControlBlock_MetaBlockStateReference:
            x._StandardControlBlock_MetaBlockConnectable = None
        for y in value:
            y._StandardControlBlock_MetaBlockConnectable = self
        self._StandardControlBlock_MetaBlockStateReference = value

    StandardControlBlock_MetaBlockStateReference = property(getStandardControlBlock_MetaBlockStateReference, setStandardControlBlock_MetaBlockStateReference)

    def addStandardControlBlock_MetaBlockStateReference(self, *StandardControlBlock_MetaBlockStateReference):
        for obj in StandardControlBlock_MetaBlockStateReference:
            obj._StandardControlBlock_MetaBlockConnectable = self
            self._StandardControlBlock_MetaBlockStateReference.append(obj)

    def removeStandardControlBlock_MetaBlockStateReference(self, *StandardControlBlock_MetaBlockStateReference):
        for obj in StandardControlBlock_MetaBlockStateReference:
            obj._StandardControlBlock_MetaBlockConnectable = None
            self._StandardControlBlock_MetaBlockStateReference.remove(obj)

    def getMetaBlockOutputReference(self):
        
        return self._MetaBlockOutputReference

    def setMetaBlockOutputReference(self, value):
        for x in self._MetaBlockOutputReference:
            x._MetaBlockConnectable = None
        for y in value:
            y._MetaBlockConnectable = self
        self._MetaBlockOutputReference = value

    MetaBlockOutputReference = property(getMetaBlockOutputReference, setMetaBlockOutputReference)

    def addMetaBlockOutputReference(self, *MetaBlockOutputReference):
        for obj in MetaBlockOutputReference:
            obj._MetaBlockConnectable = self
            self._MetaBlockOutputReference.append(obj)

    def removeMetaBlockOutputReference(self, *MetaBlockOutputReference):
        for obj in MetaBlockOutputReference:
            obj._MetaBlockConnectable = None
            self._MetaBlockOutputReference.remove(obj)

    def getMetaBlockStateReference(self):
        
        return self._MetaBlockStateReference

    def setMetaBlockStateReference(self, value):
        for x in self._MetaBlockStateReference:
            x._MetaBlockConnectable = None
        for y in value:
            y._MetaBlockConnectable = self
        self._MetaBlockStateReference = value

    MetaBlockStateReference = property(getMetaBlockStateReference, setMetaBlockStateReference)

    def addMetaBlockStateReference(self, *MetaBlockStateReference):
        for obj in MetaBlockStateReference:
            obj._MetaBlockConnectable = self
            self._MetaBlockStateReference.append(obj)

    def removeMetaBlockStateReference(self, *MetaBlockStateReference):
        for obj in MetaBlockStateReference:
            obj._MetaBlockConnectable = None
            self._MetaBlockStateReference.remove(obj)

    def getBlockInputReference(self):
        """Each block reference input is usually tied to one (sometimes zero for optional inputs) external block inputs or internal block reference outputs.
        """
        return self._BlockInputReference

    def setBlockInputReference(self, value):
        for x in self._BlockInputReference:
            x._BlockConnectable = None
        for y in value:
            y._BlockConnectable = self
        self._BlockInputReference = value

    BlockInputReference = property(getBlockInputReference, setBlockInputReference)

    def addBlockInputReference(self, *BlockInputReference):
        for obj in BlockInputReference:
            obj._BlockConnectable = self
            self._BlockInputReference.append(obj)

    def removeBlockInputReference(self, *BlockInputReference):
        for obj in BlockInputReference:
            obj._BlockConnectable = None
            self._BlockInputReference.remove(obj)

    def getStandardControlBlock_MetaBlockInputReference(self):
        
        return self._StandardControlBlock_MetaBlockInputReference

    def setStandardControlBlock_MetaBlockInputReference(self, value):
        for x in self._StandardControlBlock_MetaBlockInputReference:
            x._StandardControlBlock_MetaBlockConnectable = None
        for y in value:
            y._StandardControlBlock_MetaBlockConnectable = self
        self._StandardControlBlock_MetaBlockInputReference = value

    StandardControlBlock_MetaBlockInputReference = property(getStandardControlBlock_MetaBlockInputReference, setStandardControlBlock_MetaBlockInputReference)

    def addStandardControlBlock_MetaBlockInputReference(self, *StandardControlBlock_MetaBlockInputReference):
        for obj in StandardControlBlock_MetaBlockInputReference:
            obj._StandardControlBlock_MetaBlockConnectable = self
            self._StandardControlBlock_MetaBlockInputReference.append(obj)

    def removeStandardControlBlock_MetaBlockInputReference(self, *StandardControlBlock_MetaBlockInputReference):
        for obj in StandardControlBlock_MetaBlockInputReference:
            obj._StandardControlBlock_MetaBlockConnectable = None
            self._StandardControlBlock_MetaBlockInputReference.remove(obj)

    def getStandardControlBlock_MetaBlockParameterReference(self):
        
        return self._StandardControlBlock_MetaBlockParameterReference

    def setStandardControlBlock_MetaBlockParameterReference(self, value):
        for x in self._StandardControlBlock_MetaBlockParameterReference:
            x._StandardControlBlock_MetaBlockConnectable = None
        for y in value:
            y._StandardControlBlock_MetaBlockConnectable = self
        self._StandardControlBlock_MetaBlockParameterReference = value

    StandardControlBlock_MetaBlockParameterReference = property(getStandardControlBlock_MetaBlockParameterReference, setStandardControlBlock_MetaBlockParameterReference)

    def addStandardControlBlock_MetaBlockParameterReference(self, *StandardControlBlock_MetaBlockParameterReference):
        for obj in StandardControlBlock_MetaBlockParameterReference:
            obj._StandardControlBlock_MetaBlockConnectable = self
            self._StandardControlBlock_MetaBlockParameterReference.append(obj)

    def removeStandardControlBlock_MetaBlockParameterReference(self, *StandardControlBlock_MetaBlockParameterReference):
        for obj in StandardControlBlock_MetaBlockParameterReference:
            obj._StandardControlBlock_MetaBlockConnectable = None
            self._StandardControlBlock_MetaBlockParameterReference.remove(obj)

    def getMetaBlockParameterReference(self):
        
        return self._MetaBlockParameterReference

    def setMetaBlockParameterReference(self, value):
        for x in self._MetaBlockParameterReference:
            x._MetaBlockConnectable = None
        for y in value:
            y._MetaBlockConnectable = self
        self._MetaBlockParameterReference = value

    MetaBlockParameterReference = property(getMetaBlockParameterReference, setMetaBlockParameterReference)

    def addMetaBlockParameterReference(self, *MetaBlockParameterReference):
        for obj in MetaBlockParameterReference:
            obj._MetaBlockConnectable = self
            self._MetaBlockParameterReference.append(obj)

    def removeMetaBlockParameterReference(self, *MetaBlockParameterReference):
        for obj in MetaBlockParameterReference:
            obj._MetaBlockConnectable = None
            self._MetaBlockParameterReference.remove(obj)

    def getStandardControlBlock_MetaBlockOutputReference(self):
        
        return self._StandardControlBlock_MetaBlockOutputReference

    def setStandardControlBlock_MetaBlockOutputReference(self, value):
        for x in self._StandardControlBlock_MetaBlockOutputReference:
            x._StandardControlBlock_MetaBlockConnectable = None
        for y in value:
            y._StandardControlBlock_MetaBlockConnectable = self
        self._StandardControlBlock_MetaBlockOutputReference = value

    StandardControlBlock_MetaBlockOutputReference = property(getStandardControlBlock_MetaBlockOutputReference, setStandardControlBlock_MetaBlockOutputReference)

    def addStandardControlBlock_MetaBlockOutputReference(self, *StandardControlBlock_MetaBlockOutputReference):
        for obj in StandardControlBlock_MetaBlockOutputReference:
            obj._StandardControlBlock_MetaBlockConnectable = self
            self._StandardControlBlock_MetaBlockOutputReference.append(obj)

    def removeStandardControlBlock_MetaBlockOutputReference(self, *StandardControlBlock_MetaBlockOutputReference):
        for obj in StandardControlBlock_MetaBlockOutputReference:
            obj._StandardControlBlock_MetaBlockConnectable = None
            self._StandardControlBlock_MetaBlockOutputReference.remove(obj)

    def getMetaBlockInputReference(self):
        
        return self._MetaBlockInputReference

    def setMetaBlockInputReference(self, value):
        for x in self._MetaBlockInputReference:
            x._MetaBlockConnectable = None
        for y in value:
            y._MetaBlockConnectable = self
        self._MetaBlockInputReference = value

    MetaBlockInputReference = property(getMetaBlockInputReference, setMetaBlockInputReference)

    def addMetaBlockInputReference(self, *MetaBlockInputReference):
        for obj in MetaBlockInputReference:
            obj._MetaBlockConnectable = self
            self._MetaBlockInputReference.append(obj)

    def removeMetaBlockInputReference(self, *MetaBlockInputReference):
        for obj in MetaBlockInputReference:
            obj._MetaBlockConnectable = None
            self._MetaBlockInputReference.remove(obj)

