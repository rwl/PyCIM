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

from CIM15.IEC61968.Assets.Asset import Asset

class StructureSupport(Asset):
    """Support for structure assets.Support for structure assets.
    """

    def __init__(self, anchorRodCount=0, length=0.0, anchorRodLength=0.0, direction=0.0, anchorKind="concrete", kind="guy", size='', SecuredStructure=None, *args, **kw_args):
        """Initialises a new 'StructureSupport' instance.

        @param anchorRodCount: (if anchor) Number of rods used. 
        @param length: Length of this support structure. 
        @param anchorRodLength: (if anchor) Length of rod used. 
        @param direction: Direction of this support structure. 
        @param anchorKind: (if anchor) Kind of anchor. Values are: "concrete", "helix", "unknown", "multiHelix", "screw", "rod", "other"
        @param kind: Kind of structure support. Values are: "guy", "anchor"
        @param size: Size of this support structure. 
        @param SecuredStructure:
        """
        #: (if anchor) Number of rods used.
        self.anchorRodCount = anchorRodCount

        #: Length of this support structure.
        self.length = length

        #: (if anchor) Length of rod used.
        self.anchorRodLength = anchorRodLength

        #: Direction of this support structure.
        self.direction = direction

        #: (if anchor) Kind of anchor. Values are: "concrete", "helix", "unknown", "multiHelix", "screw", "rod", "other"
        self.anchorKind = anchorKind

        #: Kind of structure support. Values are: "guy", "anchor"
        self.kind = kind

        #: Size of this support structure.
        self.size = size

        self._SecuredStructure = None
        self.SecuredStructure = SecuredStructure

        super(StructureSupport, self).__init__(*args, **kw_args)

    _attrs = ["anchorRodCount", "length", "anchorRodLength", "direction", "anchorKind", "kind", "size"]
    _attr_types = {"anchorRodCount": int, "length": float, "anchorRodLength": float, "direction": float, "anchorKind": str, "kind": str, "size": str}
    _defaults = {"anchorRodCount": 0, "length": 0.0, "anchorRodLength": 0.0, "direction": 0.0, "anchorKind": "concrete", "kind": "guy", "size": ''}
    _enums = {"anchorKind": "AnchorKind", "kind": "StructureSupportKind"}
    _refs = ["SecuredStructure"]
    _many_refs = []

    def getSecuredStructure(self):
        
        return self._SecuredStructure

    def setSecuredStructure(self, value):
        if self._SecuredStructure is not None:
            filtered = [x for x in self.SecuredStructure.StructureSupportInfos if x != self]
            self._SecuredStructure._StructureSupportInfos = filtered

        self._SecuredStructure = value
        if self._SecuredStructure is not None:
            if self not in self._SecuredStructure._StructureSupportInfos:
                self._SecuredStructure._StructureSupportInfos.append(self)

    SecuredStructure = property(getSecuredStructure, setSecuredStructure)

