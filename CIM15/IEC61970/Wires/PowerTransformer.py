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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class PowerTransformer(ConductingEquipment):
    """An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. The same power transformer can be modelled in two ways, namely with and without tanks: <ol> 	<li>The power transformer that uses power transformer ends directly (without tanks) is suitable for balanced three-phase models. This is typical for transmission and sub-transmission network modelling. Such a transformer will require one power transformer end for each physical winding. There must be a one-to-one association between PowerTransformerEnd and Core::Terminal.</li> 	<li>The power transformer that uses transformer tanks is suitable for an unbalanced transformer, a balanced transformer within a single tank, or a balanced transformer made up of three tanks. This is typical for distribution network modelling and the only choice when modelling an unbalanced transformer, or a transformer that has more than three windings. Power transformer modelled with tanks will require for each tank, one transformer tank end per physical winding in the tank. There may be one, two, or three phases in the transformer tank end.  Examples: 3 phases for 3-phase delta or wye connected windings, 2 for one phase-to-phase winding, and 1 for a phase-to-neutral or phase-to-ground winding.  With 1 or 2 phases, more than one transformer tank end may be associated to the same 3-phase Core::Terminal instance, while with 3 phases there should be a one-to-one association.</li> </ol> This power transformer model is flexible in order to support different kinds of data exchange requirements. There are 5 possible ways to combine available classes and their attributes: <ol> 	<li>Instance parameters - Use the r, x, r0, x0, b, b0, g, and g0 attributes on PowerTransformerEnd and ignore related TransformerStarImpedance, TransformerMeshImpedance, or TransformerCoreAdmittance. This option assumes a star connection of the series impedances. It is suitable for typical transmission, balanced three-phase transformer models, for transformers with 2 or three windings.</li> 	<li>Star instance parameters by association - Instead of the r, x, r0, x0, b, b0, g, and g0 attributes, use associations to TransformerStarImpedance and TransformerCoreAdmitance. This option is suitable in same scenarios as option 1, but when catalogue data is available for transformers.</li> 	<li>Mesh instance parameters by association: Instead of the r, x, r0, x0, b, b0, g, and g0 attributes, use associations to TransformerMeshImpedance and TransformerCoreAdmittance. This option supports transformers with more than three windings.</li> 	<li>Catalog mesh parameters by association - Instead of attributes r, x, r0, x0, b, b0, g, and g0 and associations to TransformerStarImpedance, TransformerMeshImpedance, or TransformerCoreAdmittance, use the association to TransformerEndInfo. The TransformerEnd.endNumber should match the corresponding TransformerEndInfo.endNumber, following the IEC standard convention of numbering from the highest voltage ends to the lowest, starting at 1. This matching supports higher-level use of a catalog, through just one association between TransformerTank and TransformerTankInfo, with simpler exchanges and incremental updates. The associated TransformerEndInfo will have associations to TransformerMeshImpedance and TransformerCoreAdmittance. This option supports unbalanced transformer, with more than three windings and is suitable whenever the transformer test data has been converted to an electrical model.</li> 	<li>Catalog test data by association - This is the same as option 4, except TransformerEndInfo will have associations to AssetModels::TransformerTest decendents, instead of to TransformerMeshImpedance and TransformerCoreAdmittance.  This option is suitable when the test data is available, and the receiving application is able to interpret the test data.</li> </ol> Every profile should specify which one or more of these options are supported.An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. The same power transformer can be modelled in two ways, namely with and without tanks: <ol> 	<li>The power transformer that uses power transformer ends directly (without tanks) is suitable for balanced three-phase models. This is typical for transmission and sub-transmission network modelling. Such a transformer will require one power transformer end for each physical winding. There must be a one-to-one association between PowerTransformerEnd and Core::Terminal.</li> 	<li>The power transformer that uses transformer tanks is suitable for an unbalanced transformer, a balanced transformer within a single tank, or a balanced transformer made up of three tanks. This is typical for distribution network modelling and the only choice when modelling an unbalanced transformer, or a transformer that has more than three windings. Power transformer modelled with tanks will require for each tank, one transformer tank end per physical winding in the tank. There may be one, two, or three phases in the transformer tank end.  Examples: 3 phases for 3-phase delta or wye connected windings, 2 for one phase-to-phase winding, and 1 for a phase-to-neutral or phase-to-ground winding.  With 1 or 2 phases, more than one transformer tank end may be associated to the same 3-phase Core::Terminal instance, while with 3 phases there should be a one-to-one association.</li> </ol> This power transformer model is flexible in order to support different kinds of data exchange requirements. There are 5 possible ways to combine available classes and their attributes: <ol> 	<li>Instance parameters - Use the r, x, r0, x0, b, b0, g, and g0 attributes on PowerTransformerEnd and ignore related TransformerStarImpedance, TransformerMeshImpedance, or TransformerCoreAdmittance. This option assumes a star connection of the series impedances. It is suitable for typical transmission, balanced three-phase transformer models, for transformers with 2 or three windings.</li> 	<li>Star instance parameters by association - Instead of the r, x, r0, x0, b, b0, g, and g0 attributes, use associations to TransformerStarImpedance and TransformerCoreAdmitance. This option is suitable in same scenarios as option 1, but when catalogue data is available for transformers.</li> 	<li>Mesh instance parameters by association: Instead of the r, x, r0, x0, b, b0, g, and g0 attributes, use associations to TransformerMeshImpedance and TransformerCoreAdmittance. This option supports transformers with more than three windings.</li> 	<li>Catalog mesh parameters by association - Instead of attributes r, x, r0, x0, b, b0, g, and g0 and associations to TransformerStarImpedance, TransformerMeshImpedance, or TransformerCoreAdmittance, use the association to TransformerEndInfo. The TransformerEnd.endNumber should match the corresponding TransformerEndInfo.endNumber, following the IEC standard convention of numbering from the highest voltage ends to the lowest, starting at 1. This matching supports higher-level use of a catalog, through just one association between TransformerTank and TransformerTankInfo, with simpler exchanges and incremental updates. The associated TransformerEndInfo will have associations to TransformerMeshImpedance and TransformerCoreAdmittance. This option supports unbalanced transformer, with more than three windings and is suitable whenever the transformer test data has been converted to an electrical model.</li> 	<li>Catalog test data by association - This is the same as option 4, except TransformerEndInfo will have associations to AssetModels::TransformerTest decendents, instead of to TransformerMeshImpedance and TransformerCoreAdmittance.  This option is suitable when the test data is available, and the receiving application is able to interpret the test data.</li> </ol> Every profile should specify which one or more of these options are supported.
    """

    def __init__(self, vectorGroup='', TransformerTanks=None, PowerTransformerInfo=None, PowerTransformerEnd=None, *args, **kw_args):
        """Initialises a new 'PowerTransformer' instance.

        @param vectorGroup: Vector group of the transformer for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        @param TransformerTanks: All transformers that belong to this bank.
        @param PowerTransformerInfo: Power transformer data.
        @param PowerTransformerEnd:
        """
        #: Vector group of the transformer for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.
        self.vectorGroup = vectorGroup

        self._TransformerTanks = []
        self.TransformerTanks = [] if TransformerTanks is None else TransformerTanks

        self._PowerTransformerInfo = None
        self.PowerTransformerInfo = PowerTransformerInfo

        self._PowerTransformerEnd = []
        self.PowerTransformerEnd = [] if PowerTransformerEnd is None else PowerTransformerEnd

        super(PowerTransformer, self).__init__(*args, **kw_args)

    _attrs = ["vectorGroup"]
    _attr_types = {"vectorGroup": str}
    _defaults = {"vectorGroup": ''}
    _enums = {}
    _refs = ["TransformerTanks", "PowerTransformerInfo", "PowerTransformerEnd"]
    _many_refs = ["TransformerTanks", "PowerTransformerEnd"]

    def getTransformerTanks(self):
        """All transformers that belong to this bank.
        """
        return self._TransformerTanks

    def setTransformerTanks(self, value):
        for x in self._TransformerTanks:
            x.PowerTransformer = None
        for y in value:
            y._PowerTransformer = self
        self._TransformerTanks = value

    TransformerTanks = property(getTransformerTanks, setTransformerTanks)

    def addTransformerTanks(self, *TransformerTanks):
        for obj in TransformerTanks:
            obj.PowerTransformer = self

    def removeTransformerTanks(self, *TransformerTanks):
        for obj in TransformerTanks:
            obj.PowerTransformer = None

    def getPowerTransformerInfo(self):
        """Power transformer data.
        """
        return self._PowerTransformerInfo

    def setPowerTransformerInfo(self, value):
        if self._PowerTransformerInfo is not None:
            filtered = [x for x in self.PowerTransformerInfo.PowerTransformers if x != self]
            self._PowerTransformerInfo._PowerTransformers = filtered

        self._PowerTransformerInfo = value
        if self._PowerTransformerInfo is not None:
            if self not in self._PowerTransformerInfo._PowerTransformers:
                self._PowerTransformerInfo._PowerTransformers.append(self)

    PowerTransformerInfo = property(getPowerTransformerInfo, setPowerTransformerInfo)

    def getPowerTransformerEnd(self):
        
        return self._PowerTransformerEnd

    def setPowerTransformerEnd(self, value):
        for x in self._PowerTransformerEnd:
            x.PowerTransformer = None
        for y in value:
            y._PowerTransformer = self
        self._PowerTransformerEnd = value

    PowerTransformerEnd = property(getPowerTransformerEnd, setPowerTransformerEnd)

    def addPowerTransformerEnd(self, *PowerTransformerEnd):
        for obj in PowerTransformerEnd:
            obj.PowerTransformer = self

    def removePowerTransformerEnd(self, *PowerTransformerEnd):
        for obj in PowerTransformerEnd:
            obj.PowerTransformer = None

