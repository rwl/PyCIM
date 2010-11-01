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

from CIM14v13.IEC61968.Informative.InfAssets.Structure import Structure

class UndergroundStructure(Structure):
    """Abstract class for underground structures. Typical structure types are: BURD, Enclosure, Hand Hole, Manhole, Pad/Slab, Subsurface Enclosure, Trench, Tunnel, Vault, Pull/Splice Box.
    """

    def __init__(self, sealingWarrantyExpiresDate='', ventilation=False, material='', *args, **kw_args):
        """Initializes a new 'UndergroundStructure' instance.

        @param sealingWarrantyExpiresDate: Date sealing warranty expires. 
        @param ventilation: True if vault is ventilating. 
        @param material: Primary material of underground structure. 
        """
        #: Date sealing warranty expires. 
        self.sealingWarrantyExpiresDate = sealingWarrantyExpiresDate

        #: True if vault is ventilating. 
        self.ventilation = ventilation

        #: Primary material of underground structure. 
        self.material = material

        super(UndergroundStructure, self).__init__(*args, **kw_args)

