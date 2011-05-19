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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class ElectricalInfo(AssetInfo):
    """Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.
    """

    def __init__(self, phaseCount=0, ratedApparentPower=0.0, phaseCode="s12N", frequency=0.0, r0=0.0, r=0.0, bil=0.0, x0=0.0, x=0.0, ratedCurrent=0.0, wireCount=0, b0=0.0, b=0.0, ratedVoltage=0.0, g=0.0, g0=0.0, isConnected=False, *args, **kw_args):
        """Initialises a new 'ElectricalInfo' instance.

        @param phaseCount: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        @param ratedApparentPower: Rated apparent power. 
        @param phaseCode: If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param frequency: Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz. 
        @param r0: Zero sequence series resistance. 
        @param r: Positive sequence series resistance. 
        @param bil: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        @param x0: Zero sequence series reactance. 
        @param x: Positive sequence series reactance. 
        @param ratedCurrent: Rated current. 
        @param wireCount: For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y. 
        @param b0: Zero sequence susceptance. 
        @param b: Positive sequence susceptance. 
        @param ratedVoltage: Rated voltage. 
        @param g: Positive sequence conductance. 
        @param g0: Zero sequence conductance. 
        @param isConnected: True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used. 
        """
        #: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
        self.phaseCount = phaseCount

        #: Rated apparent power.
        self.ratedApparentPower = ratedApparentPower

        #: If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phaseCode = phaseCode

        #: Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz.
        self.frequency = frequency

        #: Zero sequence series resistance.
        self.r0 = r0

        #: Positive sequence series resistance.
        self.r = r

        #: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
        self.bil = bil

        #: Zero sequence series reactance.
        self.x0 = x0

        #: Positive sequence series reactance.
        self.x = x

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y.
        self.wireCount = wireCount

        #: Zero sequence susceptance.
        self.b0 = b0

        #: Positive sequence susceptance.
        self.b = b

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: Positive sequence conductance.
        self.g = g

        #: Zero sequence conductance.
        self.g0 = g0

        #: True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used.
        self.isConnected = isConnected

        super(ElectricalInfo, self).__init__(*args, **kw_args)

    _attrs = ["phaseCount", "ratedApparentPower", "phaseCode", "frequency", "r0", "r", "bil", "x0", "x", "ratedCurrent", "wireCount", "b0", "b", "ratedVoltage", "g", "g0", "isConnected"]
    _attr_types = {"phaseCount": int, "ratedApparentPower": float, "phaseCode": str, "frequency": float, "r0": float, "r": float, "bil": float, "x0": float, "x": float, "ratedCurrent": float, "wireCount": int, "b0": float, "b": float, "ratedVoltage": float, "g": float, "g0": float, "isConnected": bool}
    _defaults = {"phaseCount": 0, "ratedApparentPower": 0.0, "phaseCode": "s12N", "frequency": 0.0, "r0": 0.0, "r": 0.0, "bil": 0.0, "x0": 0.0, "x": 0.0, "ratedCurrent": 0.0, "wireCount": 0, "b0": 0.0, "b": 0.0, "ratedVoltage": 0.0, "g": 0.0, "g0": 0.0, "isConnected": False}
    _enums = {"phaseCode": "PhaseCode"}
    _refs = []
    _many_refs = []

