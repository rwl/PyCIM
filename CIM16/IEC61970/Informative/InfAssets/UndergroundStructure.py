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

from CIM16.IEC61970.Informative.InfAssets.Structure import Structure

class UndergroundStructure(Structure):
    """Underground structure.Underground structure.
    """

    def __init__(self, hasVentilation=False, kind="trench", material='', sealingWarrantyExpiresDate='', *args, **kw_args):
        """Initialises a new 'UndergroundStructure' instance.

        @param hasVentilation: True if vault is ventilating. 
        @param kind: True if vault is ventilating. Values are: "trench", "pullbox", "vault", "burd", "subsurfaceEnclosure", "handhole", "enclosure", "tunnel", "manhole", "pad"
        @param material: Primary material of underground structure. 
        @param sealingWarrantyExpiresDate: Date sealing warranty expires. 
        """
        #: True if vault is ventilating.
        self.hasVentilation = hasVentilation

        #: True if vault is ventilating. Values are: "trench", "pullbox", "vault", "burd", "subsurfaceEnclosure", "handhole", "enclosure", "tunnel", "manhole", "pad"
        self.kind = kind

        #: Primary material of underground structure.
        self.material = material

        #: Date sealing warranty expires.
        self.sealingWarrantyExpiresDate = sealingWarrantyExpiresDate

        super(UndergroundStructure, self).__init__(*args, **kw_args)

    _attrs = ["hasVentilation", "kind", "material", "sealingWarrantyExpiresDate"]
    _attr_types = {"hasVentilation": bool, "kind": str, "material": str, "sealingWarrantyExpiresDate": str}
    _defaults = {"hasVentilation": False, "kind": "trench", "material": '', "sealingWarrantyExpiresDate": ''}
    _enums = {"kind": "UndergroundStructureKind"}
    _refs = []
    _many_refs = []

