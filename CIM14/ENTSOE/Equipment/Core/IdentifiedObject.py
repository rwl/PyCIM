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

from CIM14.ENTSOE.Equipment.Element import Element

class IdentifiedObject(Element):
    """This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    def __init__(self, description='', name='', aliasName='', pathName='', *args, **kw_args):
        """Initialises a new 'IdentifiedObject' instance.

        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name attribute is required except for the following classes:   FossilFuel, HydorPump, LoadResponseCharacteristic, MutualCoupling, ReactiveCapabilityCurve, RegulatingControl, SynchronousMachine, TopologicalIsland, ConductingEquipment, Conductor, ConnectivityNodeContainer, Curve, Equipment, EquipmentContainer, EquivalentEquipment, REgulatingCondEq, TapChanger, BaseVoltage, Terminal, TransformerWinding, RatioTapChanger, PhaseTapChanger, OperationalLimitSet, CurrentLimit, and VoltageLimit. 
        @param aliasName: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        @param pathName: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        """
        #: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
        self.description = description

        #: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name attribute is required except for the following classes:   FossilFuel, HydorPump, LoadResponseCharacteristic, MutualCoupling, ReactiveCapabilityCurve, RegulatingControl, SynchronousMachine, TopologicalIsland, ConductingEquipment, Conductor, ConnectivityNodeContainer, Curve, Equipment, EquipmentContainer, EquivalentEquipment, REgulatingCondEq, TapChanger, BaseVoltage, Terminal, TransformerWinding, RatioTapChanger, PhaseTapChanger, OperationalLimitSet, CurrentLimit, and VoltageLimit.
        self.name = name

        #: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
        self.aliasName = aliasName

        #: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
        self.pathName = pathName

        super(IdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["description", "name", "aliasName", "pathName"]
    _attr_types = {"description": str, "name": str, "aliasName": str, "pathName": str}
    _defaults = {"description": '', "name": '', "aliasName": '', "pathName": ''}
    _enums = {}
    _refs = []
    _many_refs = []

