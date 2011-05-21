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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MetaBlock(IdentifiedObject):
    """A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.
    """

    def __init__(self, blockKind="powerSystemStabilizer", internal=False, proprietary=False, primitive=False, MetaBlockReference=None, MetaBlockOutput=None, MetaBlockState=None, MetaBlockSignal=None, blockType0=None, MetaBlockInput=None, blockConstant0=None, Block=None, MetaBlockParameter=None, *args, **kw_args):
        """Initialises a new 'MetaBlock' instance.

        @param blockKind: Enumeration type: StandardControlBlock, Excitation System, ... Name used to distinguish which standard control block (Integration, Summation, ...)? Values are: "powerSystemStabilizer", "automaticVoltageControl", "turbine", "govenor", "dotDotDot", "energySource", "exciter"
        @param internal: This block is intended to be used only internally within other blocks.   An example would be a summation or integrator block. Such bocks are typically also primitive, though more complex internal blocks made up of other primitive controls could be built. 
        @param proprietary: This block is a proprietary block. Only inputs, outputs and parameters are exchanged. 
        @param primitive: Iindicates this type is treated as a primitive type and therefore the internal block model can be ignored and is not typically defined in the model. Primitive blocks include such basic things as summation and standard IEEEexciter models. The exchange parties must agree on the meaning of primitive blocks according to their identification. 
        @param MetaBlockReference:
        @param MetaBlockOutput: Outputs that belong to the block.
        @param MetaBlockState:
        @param MetaBlockSignal:
        @param blockType0:
        @param MetaBlockInput: Inputs belong to a block.
        @param blockConstant0:
        @param Block:
        @param MetaBlockParameter: Paramters belong to a block.
        """
        #: Enumeration type: StandardControlBlock, Excitation System, ... Name used to distinguish which standard control block (Integration, Summation, ...)? Values are: "powerSystemStabilizer", "automaticVoltageControl", "turbine", "govenor", "dotDotDot", "energySource", "exciter"
        self.blockKind = blockKind

        #: This block is intended to be used only internally within other blocks.   An example would be a summation or integrator block. Such bocks are typically also primitive, though more complex internal blocks made up of other primitive controls could be built.
        self.internal = internal

        #: This block is a proprietary block. Only inputs, outputs and parameters are exchanged.
        self.proprietary = proprietary

        #: Iindicates this type is treated as a primitive type and therefore the internal block model can be ignored and is not typically defined in the model. Primitive blocks include such basic things as summation and standard IEEEexciter models. The exchange parties must agree on the meaning of primitive blocks according to their identification.
        self.primitive = primitive

        self._MetaBlockReference = []
        self.MetaBlockReference = [] if MetaBlockReference is None else MetaBlockReference

        self._MetaBlockOutput = []
        self.MetaBlockOutput = [] if MetaBlockOutput is None else MetaBlockOutput

        self._MetaBlockState = []
        self.MetaBlockState = [] if MetaBlockState is None else MetaBlockState

        self._MetaBlockSignal = []
        self.MetaBlockSignal = [] if MetaBlockSignal is None else MetaBlockSignal

        self._blockType0 = None
        self.blockType0 = blockType0

        self._MetaBlockInput = []
        self.MetaBlockInput = [] if MetaBlockInput is None else MetaBlockInput

        self._blockConstant0 = []
        self.blockConstant0 = [] if blockConstant0 is None else blockConstant0

        self._Block = []
        self.Block = [] if Block is None else Block

        self._MetaBlockParameter = []
        self.MetaBlockParameter = [] if MetaBlockParameter is None else MetaBlockParameter

        super(MetaBlock, self).__init__(*args, **kw_args)

    _attrs = ["blockKind", "internal", "proprietary", "primitive"]
    _attr_types = {"blockKind": str, "internal": bool, "proprietary": bool, "primitive": bool}
    _defaults = {"blockKind": "powerSystemStabilizer", "internal": False, "proprietary": False, "primitive": False}
    _enums = {"blockKind": "BlockKind"}
    _refs = ["MetaBlockReference", "MetaBlockOutput", "MetaBlockState", "MetaBlockSignal", "blockType0", "MetaBlockInput", "blockConstant0", "Block", "MetaBlockParameter"]
    _many_refs = ["MetaBlockReference", "MetaBlockOutput", "MetaBlockState", "MetaBlockSignal", "MetaBlockInput", "blockConstant0", "Block", "MetaBlockParameter"]

    def getMetaBlockReference(self):
        
        return self._MetaBlockReference

    def setMetaBlockReference(self, value):
        for x in self._MetaBlockReference:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockReference = value

    MetaBlockReference = property(getMetaBlockReference, setMetaBlockReference)

    def addMetaBlockReference(self, *MetaBlockReference):
        for obj in MetaBlockReference:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockReference(self, *MetaBlockReference):
        for obj in MetaBlockReference:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockOutput(self):
        """Outputs that belong to the block.
        """
        return self._MetaBlockOutput

    def setMetaBlockOutput(self, value):
        for x in self._MetaBlockOutput:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockOutput = value

    MetaBlockOutput = property(getMetaBlockOutput, setMetaBlockOutput)

    def addMetaBlockOutput(self, *MetaBlockOutput):
        for obj in MetaBlockOutput:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockOutput(self, *MetaBlockOutput):
        for obj in MetaBlockOutput:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockState(self):
        
        return self._MetaBlockState

    def setMetaBlockState(self, value):
        for x in self._MetaBlockState:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockState = value

    MetaBlockState = property(getMetaBlockState, setMetaBlockState)

    def addMetaBlockState(self, *MetaBlockState):
        for obj in MetaBlockState:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockState(self, *MetaBlockState):
        for obj in MetaBlockState:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockSignal(self):
        
        return self._MetaBlockSignal

    def setMetaBlockSignal(self, value):
        for x in self._MetaBlockSignal:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockSignal = value

    MetaBlockSignal = property(getMetaBlockSignal, setMetaBlockSignal)

    def addMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.MemberOf_MetaBlock = None

    def getblockType0(self):
        
        return self._blockType0

    def setblockType0(self, value):
        if self._blockType0 is not None:
            filtered = [x for x in self.blockType0.metaBlock0 if x != self]
            self._blockType0._metaBlock0 = filtered

        self._blockType0 = value
        if self._blockType0 is not None:
            if self not in self._blockType0._metaBlock0:
                self._blockType0._metaBlock0.append(self)

    blockType0 = property(getblockType0, setblockType0)

    def getMetaBlockInput(self):
        """Inputs belong to a block.
        """
        return self._MetaBlockInput

    def setMetaBlockInput(self, value):
        for x in self._MetaBlockInput:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockInput = value

    MetaBlockInput = property(getMetaBlockInput, setMetaBlockInput)

    def addMetaBlockInput(self, *MetaBlockInput):
        for obj in MetaBlockInput:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockInput(self, *MetaBlockInput):
        for obj in MetaBlockInput:
            obj.MemberOf_MetaBlock = None

    def getblockConstant0(self):
        
        return self._blockConstant0

    def setblockConstant0(self, value):
        for x in self._blockConstant0:
            x.metaBlock0 = None
        for y in value:
            y._metaBlock0 = self
        self._blockConstant0 = value

    blockConstant0 = property(getblockConstant0, setblockConstant0)

    def addblockConstant0(self, *blockConstant0):
        for obj in blockConstant0:
            obj.metaBlock0 = self

    def removeblockConstant0(self, *blockConstant0):
        for obj in blockConstant0:
            obj.metaBlock0 = None

    def getBlock(self):
        
        return self._Block

    def setBlock(self, value):
        for x in self._Block:
            x.MetaBlock = None
        for y in value:
            y._MetaBlock = self
        self._Block = value

    Block = property(getBlock, setBlock)

    def addBlock(self, *Block):
        for obj in Block:
            obj.MetaBlock = self

    def removeBlock(self, *Block):
        for obj in Block:
            obj.MetaBlock = None

    def getMetaBlockParameter(self):
        """Paramters belong to a block.
        """
        return self._MetaBlockParameter

    def setMetaBlockParameter(self, value):
        for x in self._MetaBlockParameter:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockParameter = value

    MetaBlockParameter = property(getMetaBlockParameter, setMetaBlockParameter)

    def addMetaBlockParameter(self, *MetaBlockParameter):
        for obj in MetaBlockParameter:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockParameter(self, *MetaBlockParameter):
        for obj in MetaBlockParameter:
            obj.MemberOf_MetaBlock = None

