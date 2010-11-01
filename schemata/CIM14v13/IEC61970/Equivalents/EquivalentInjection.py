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

from CIM14v13.IEC61970.Equivalents.EquivalentEquipment import EquivalentEquipment

class EquivalentInjection(EquivalentEquipment):
    """This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the local connectivity node.
    """

    def __init__(self, regulationStatus=False, regulationCapability=False, minP=0.0, maxP=0.0, regulationTarget=0.0, *args, **kw_args):
        """Initializes a new 'EquivalentInjection' instance.

        @param regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. 
        @param regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. 
        @param minP: Maximum active power of the injection. 
        @param maxP: Minimum active power of the injection. 
        @param regulationTarget: The target voltage for voltage regulation. 
        """
        #: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. 
        self.regulationStatus = regulationStatus

        #: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. 
        self.regulationCapability = regulationCapability

        #: Maximum active power of the injection. 
        self.minP = minP

        #: Minimum active power of the injection. 
        self.maxP = maxP

        #: The target voltage for voltage regulation. 
        self.regulationTarget = regulationTarget

        super(EquivalentInjection, self).__init__(*args, **kw_args)

