# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" This package contains the information classes that extend IEC61970::Wires package with power system resources required for distribution network modelling, including unbalanced networks.
"""

from cim14v13.iec61970.core import IdentifiedObject
from cim14v13.iec61970.core import ConductingEquipment
from cim14v13.iec61970.core import Equipment
from cim14v13.iec61970.wires import ACLineSegment
from cim14v13.iec61970.wires import RatioTapChanger
from cim14v13 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimWiresExt"

ns_uri = "http://iec.ch/TC57/CIM-generic#WiresExt"

class PerLengthPhaseImpedance(IdentifiedObject):
    """ Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.
    """
    # <<< per_length_phase_impedance
    # @generated
    def __init__(self, conductor_count=0, phase_impedance_data=None, conductor_segments=None, *args, **kw_args):
        """ Initialises a new 'PerLengthPhaseImpedance' instance.

        @param conductor_count: Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix. 
        @param phase_impedance_data: All data that belong to this conductor phase impedance.
        @param conductor_segments: All conductor segments described by this phase impedance.
        """
        # Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix. 
        self.conductor_count = conductor_count


        self._phase_impedance_data = []
        if phase_impedance_data is not None:
            self.phase_impedance_data = phase_impedance_data
        else:
            self.phase_impedance_data = []

        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []


        super(PerLengthPhaseImpedance, self).__init__(*args, **kw_args)
    # >>> per_length_phase_impedance

    # <<< phase_impedance_data
    # @generated
    def get_phase_impedance_data(self):
        """ All data that belong to this conductor phase impedance.
        """
        return self._phase_impedance_data

    def set_phase_impedance_data(self, value):
        for x in self._phase_impedance_data:
            x._phase_impedance = None
        for y in value:
            y._phase_impedance = self
        self._phase_impedance_data = value

    phase_impedance_data = property(get_phase_impedance_data, set_phase_impedance_data)

    def add_phase_impedance_data(self, *phase_impedance_data):
        for obj in phase_impedance_data:
            obj._phase_impedance = self
            self._phase_impedance_data.append(obj)

    def remove_phase_impedance_data(self, *phase_impedance_data):
        for obj in phase_impedance_data:
            obj._phase_impedance = None
            self._phase_impedance_data.remove(obj)
    # >>> phase_impedance_data

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this phase impedance.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._phase_impedance = None
        for y in value:
            y._phase_impedance = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._phase_impedance = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._phase_impedance = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments



class DistributionTransformerWinding(ConductingEquipment):
    """ Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """
    # <<< distribution_transformer_winding
    # @generated
    def __init__(self, grounded=False, xground=0.0, rground=0.0, from_winding_insulations=None, pi_impedance=None, phase_tap_changer=None, ratio_tap_changer=None, winding_info=None, transformer=None, to_winding_insulations=None, *args, **kw_args):
        """ Initialises a new 'DistributionTransformerWinding' instance.

        @param grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. 
        @param xground: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        @param rground: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        @param from_winding_insulations:
        @param pi_impedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        @param phase_tap_changer: Phase tap changer associated with this winding.
        @param ratio_tap_changer: Ratio tap changer associated with this winding.
        @param winding_info: Data for this winding.
        @param transformer: Transformer this winding belongs to.
        @param to_winding_insulations:
        """
        # (for Yn and Zn connections) True if the neutral is solidly grounded. 
        self.grounded = grounded

        # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        self.xground = xground

        # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        self.rground = rground


        self._from_winding_insulations = []
        if from_winding_insulations is not None:
            self.from_winding_insulations = from_winding_insulations
        else:
            self.from_winding_insulations = []

        self._pi_impedance = None
        self.pi_impedance = pi_impedance

        self._phase_tap_changer = None
        self.phase_tap_changer = phase_tap_changer

        self._ratio_tap_changer = None
        self.ratio_tap_changer = ratio_tap_changer

        self._winding_info = None
        self.winding_info = winding_info

        self._transformer = None
        self.transformer = transformer

        self._to_winding_insulations = []
        if to_winding_insulations is not None:
            self.to_winding_insulations = to_winding_insulations
        else:
            self.to_winding_insulations = []


        super(DistributionTransformerWinding, self).__init__(*args, **kw_args)
    # >>> distribution_transformer_winding

    # <<< from_winding_insulations
    # @generated
    def get_from_winding_insulations(self):
        """ 
        """
        return self._from_winding_insulations

    def set_from_winding_insulations(self, value):
        for x in self._from_winding_insulations:
            x._from_winding = None
        for y in value:
            y._from_winding = self
        self._from_winding_insulations = value

    from_winding_insulations = property(get_from_winding_insulations, set_from_winding_insulations)

    def add_from_winding_insulations(self, *from_winding_insulations):
        for obj in from_winding_insulations:
            obj._from_winding = self
            self._from_winding_insulations.append(obj)

    def remove_from_winding_insulations(self, *from_winding_insulations):
        for obj in from_winding_insulations:
            obj._from_winding = None
            self._from_winding_insulations.remove(obj)
    # >>> from_winding_insulations

    # <<< pi_impedance
    # @generated
    def get_pi_impedance(self):
        """ (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        """
        return self._pi_impedance

    def set_pi_impedance(self, value):
        if self._pi_impedance is not None:
            filtered = [x for x in self.pi_impedance.windings if x != self]
            self._pi_impedance._windings = filtered

        self._pi_impedance = value
        if self._pi_impedance is not None:
            self._pi_impedance._windings.append(self)

    pi_impedance = property(get_pi_impedance, set_pi_impedance)
    # >>> pi_impedance

    # <<< phase_tap_changer
    # @generated
    def get_phase_tap_changer(self):
        """ Phase tap changer associated with this winding.
        """
        return self._phase_tap_changer

    def set_phase_tap_changer(self, value):
        if self._phase_tap_changer is not None:
            self._phase_tap_changer._winding = None

        self._phase_tap_changer = value
        if self._phase_tap_changer is not None:
            self._phase_tap_changer._winding = self

    phase_tap_changer = property(get_phase_tap_changer, set_phase_tap_changer)
    # >>> phase_tap_changer

    # <<< ratio_tap_changer
    # @generated
    def get_ratio_tap_changer(self):
        """ Ratio tap changer associated with this winding.
        """
        return self._ratio_tap_changer

    def set_ratio_tap_changer(self, value):
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._winding = None

        self._ratio_tap_changer = value
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._winding = self

    ratio_tap_changer = property(get_ratio_tap_changer, set_ratio_tap_changer)
    # >>> ratio_tap_changer

    # <<< winding_info
    # @generated
    def get_winding_info(self):
        """ Data for this winding.
        """
        return self._winding_info

    def set_winding_info(self, value):
        if self._winding_info is not None:
            filtered = [x for x in self.winding_info.windings if x != self]
            self._winding_info._windings = filtered

        self._winding_info = value
        if self._winding_info is not None:
            self._winding_info._windings.append(self)

    winding_info = property(get_winding_info, set_winding_info)
    # >>> winding_info

    # <<< transformer
    # @generated
    def get_transformer(self):
        """ Transformer this winding belongs to.
        """
        return self._transformer

    def set_transformer(self, value):
        if self._transformer is not None:
            filtered = [x for x in self.transformer.windings if x != self]
            self._transformer._windings = filtered

        self._transformer = value
        if self._transformer is not None:
            self._transformer._windings.append(self)

    transformer = property(get_transformer, set_transformer)
    # >>> transformer

    # <<< to_winding_insulations
    # @generated
    def get_to_winding_insulations(self):
        """ 
        """
        return self._to_winding_insulations

    def set_to_winding_insulations(self, value):
        for x in self._to_winding_insulations:
            x._to_winding = None
        for y in value:
            y._to_winding = self
        self._to_winding_insulations = value

    to_winding_insulations = property(get_to_winding_insulations, set_to_winding_insulations)

    def add_to_winding_insulations(self, *to_winding_insulations):
        for obj in to_winding_insulations:
            obj._to_winding = self
            self._to_winding_insulations.append(obj)

    def remove_to_winding_insulations(self, *to_winding_insulations):
        for obj in to_winding_insulations:
            obj._to_winding = None
            self._to_winding_insulations.remove(obj)
    # >>> to_winding_insulations



class WindingPiImpedance(IdentifiedObject):
    """ Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """
    # <<< winding_pi_impedance
    # @generated
    def __init__(self, x=0.0, r0=0.0, b0=0.0, g=0.0, g0=0.0, x0=0.0, b=0.0, r=0.0, windings=None, *args, **kw_args):
        """ Initialises a new 'WindingPiImpedance' instance.

        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param r0: Zero sequence series resistance of the winding. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param g: Magnetizing branch conductance (G mag). 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param x0: Zero sequence series reactance of the winding. 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param r: DC resistance of the winding. 
        @param windings: All windings having this Pi impedance.
        """
        # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        self.x = x

        # Zero sequence series resistance of the winding. 
        self.r0 = r0

        # Zero sequence magnetizing branch susceptance. 
        self.b0 = b0

        # Magnetizing branch conductance (G mag). 
        self.g = g

        # Zero sequence magnetizing branch conductance. 
        self.g0 = g0

        # Zero sequence series reactance of the winding. 
        self.x0 = x0

        # Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        self.b = b

        # DC resistance of the winding. 
        self.r = r


        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []


        super(WindingPiImpedance, self).__init__(*args, **kw_args)
    # >>> winding_pi_impedance

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings having this Pi impedance.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._pi_impedance = None
        for y in value:
            y._pi_impedance = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._pi_impedance = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._pi_impedance = None
            self._windings.remove(obj)
    # >>> windings



class DistributionTransformer(Equipment):
    """ An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """
    # <<< distribution_transformer
    # @generated
    def __init__(self, transformer_info=None, transformer_observations=None, windings=None, transformer_bank=None, *args, **kw_args):
        """ Initialises a new 'DistributionTransformer' instance.

        @param transformer_info: Transformer data.
        @param transformer_observations:
        @param windings: All windings of this transformer.
        @param transformer_bank: Bank this transformer belongs to.
        """

        self._transformer_info = None
        self.transformer_info = transformer_info

        self._transformer_observations = []
        if transformer_observations is not None:
            self.transformer_observations = transformer_observations
        else:
            self.transformer_observations = []

        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []

        self._transformer_bank = None
        self.transformer_bank = transformer_bank


        super(DistributionTransformer, self).__init__(*args, **kw_args)
    # >>> distribution_transformer

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ Transformer data.
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.transformers if x != self]
            self._transformer_info._transformers = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._transformers.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info

    # <<< transformer_observations
    # @generated
    def get_transformer_observations(self):
        """ 
        """
        return self._transformer_observations

    def set_transformer_observations(self, value):
        for x in self._transformer_observations:
            x._transformer = None
        for y in value:
            y._transformer = self
        self._transformer_observations = value

    transformer_observations = property(get_transformer_observations, set_transformer_observations)

    def add_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            obj._transformer = self
            self._transformer_observations.append(obj)

    def remove_transformer_observations(self, *transformer_observations):
        for obj in transformer_observations:
            obj._transformer = None
            self._transformer_observations.remove(obj)
    # >>> transformer_observations

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings of this transformer.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._transformer = None
        for y in value:
            y._transformer = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._transformer = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._transformer = None
            self._windings.remove(obj)
    # >>> windings

    # <<< transformer_bank
    # @generated
    def get_transformer_bank(self):
        """ Bank this transformer belongs to.
        """
        return self._transformer_bank

    def set_transformer_bank(self, value):
        if self._transformer_bank is not None:
            filtered = [x for x in self.transformer_bank.transformers if x != self]
            self._transformer_bank._transformers = filtered

        self._transformer_bank = value
        if self._transformer_bank is not None:
            self._transformer_bank._transformers.append(self)

    transformer_bank = property(get_transformer_bank, set_transformer_bank)
    # >>> transformer_bank



class DistributionLineSegment(ACLineSegment):
    """ Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.
    """
    # <<< distribution_line_segment
    # @generated
    def __init__(self, conductor_info=None, sequence_impedance=None, phase_impedance=None, conductor_assets=None, *args, **kw_args):
        """ Initialises a new 'DistributionLineSegment' instance.

        @param conductor_info: Conductor data of this conductor segment.
        @param sequence_impedance: Sequence impedance of this conductor segment; used for balanced model.
        @param phase_impedance: Phase impedance of this conductor segment; used for unbalanced model.
        @param conductor_assets:
        """

        self._conductor_info = None
        self.conductor_info = conductor_info

        self._sequence_impedance = None
        self.sequence_impedance = sequence_impedance

        self._phase_impedance = None
        self.phase_impedance = phase_impedance

        self._conductor_assets = []
        if conductor_assets is not None:
            self.conductor_assets = conductor_assets
        else:
            self.conductor_assets = []


        super(DistributionLineSegment, self).__init__(*args, **kw_args)
    # >>> distribution_line_segment

    # <<< conductor_info
    # @generated
    def get_conductor_info(self):
        """ Conductor data of this conductor segment.
        """
        return self._conductor_info

    def set_conductor_info(self, value):
        if self._conductor_info is not None:
            filtered = [x for x in self.conductor_info.conductor_segments if x != self]
            self._conductor_info._conductor_segments = filtered

        self._conductor_info = value
        if self._conductor_info is not None:
            self._conductor_info._conductor_segments.append(self)

    conductor_info = property(get_conductor_info, set_conductor_info)
    # >>> conductor_info

    # <<< sequence_impedance
    # @generated
    def get_sequence_impedance(self):
        """ Sequence impedance of this conductor segment; used for balanced model.
        """
        return self._sequence_impedance

    def set_sequence_impedance(self, value):
        if self._sequence_impedance is not None:
            filtered = [x for x in self.sequence_impedance.conductor_segments if x != self]
            self._sequence_impedance._conductor_segments = filtered

        self._sequence_impedance = value
        if self._sequence_impedance is not None:
            self._sequence_impedance._conductor_segments.append(self)

    sequence_impedance = property(get_sequence_impedance, set_sequence_impedance)
    # >>> sequence_impedance

    # <<< phase_impedance
    # @generated
    def get_phase_impedance(self):
        """ Phase impedance of this conductor segment; used for unbalanced model.
        """
        return self._phase_impedance

    def set_phase_impedance(self, value):
        if self._phase_impedance is not None:
            filtered = [x for x in self.phase_impedance.conductor_segments if x != self]
            self._phase_impedance._conductor_segments = filtered

        self._phase_impedance = value
        if self._phase_impedance is not None:
            self._phase_impedance._conductor_segments.append(self)

    phase_impedance = property(get_phase_impedance, set_phase_impedance)
    # >>> phase_impedance

    # <<< conductor_assets
    # @generated
    def get_conductor_assets(self):
        """ 
        """
        return self._conductor_assets

    def set_conductor_assets(self, value):
        for x in self._conductor_assets:
            x._conductor_segment = None
        for y in value:
            y._conductor_segment = self
        self._conductor_assets = value

    conductor_assets = property(get_conductor_assets, set_conductor_assets)

    def add_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._conductor_segment = self
            self._conductor_assets.append(obj)

    def remove_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._conductor_segment = None
            self._conductor_assets.remove(obj)
    # >>> conductor_assets



class PerLengthSequenceImpedance(IdentifiedObject):
    """ Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """
    # <<< per_length_sequence_impedance
    # @generated
    def __init__(self, r0=0.0, bch=0.0, x=0.0, r=0.0, gch=0.0, x0=0.0, b0ch=0.0, g0ch=0.0, conductor_segments=None, *args, **kw_args):
        """ Initialises a new 'PerLengthSequenceImpedance' instance.

        @param r0: Zero sequence series resistance, per unit of length. 
        @param bch: Positive sequence shunt (charging) susceptance, per unit of length. 
        @param x: Positive sequence series reactance, per unit of length. 
        @param r: Positive sequence series resistance, per unit of length. 
        @param gch: Positive sequence shunt (charging) conductance, per unit of length. 
        @param x0: Zero sequence series reactance, per unit of length. 
        @param b0ch: Zero sequence shunt (charging) susceptance, per unit of length. 
        @param g0ch: Zero sequence shunt (charging) conductance, per unit of length. 
        @param conductor_segments: All conductor segments described by this sequence impedance.
        """
        # Zero sequence series resistance, per unit of length. 
        self.r0 = r0

        # Positive sequence shunt (charging) susceptance, per unit of length. 
        self.bch = bch

        # Positive sequence series reactance, per unit of length. 
        self.x = x

        # Positive sequence series resistance, per unit of length. 
        self.r = r

        # Positive sequence shunt (charging) conductance, per unit of length. 
        self.gch = gch

        # Zero sequence series reactance, per unit of length. 
        self.x0 = x0

        # Zero sequence shunt (charging) susceptance, per unit of length. 
        self.b0ch = b0ch

        # Zero sequence shunt (charging) conductance, per unit of length. 
        self.g0ch = g0ch


        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []


        super(PerLengthSequenceImpedance, self).__init__(*args, **kw_args)
    # >>> per_length_sequence_impedance

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this sequence impedance.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._sequence_impedance = None
        for y in value:
            y._sequence_impedance = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._sequence_impedance = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._sequence_impedance = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments



class TransformerBank(Equipment):
    """ An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """
    # <<< transformer_bank
    # @generated
    def __init__(self, vector_group='', transformers=None, *args, **kw_args):
        """ Initialises a new 'TransformerBank' instance.

        @param vector_group: Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        @param transformers: All transformers that belong to this bank.
        """
        # Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        self.vector_group = vector_group


        self._transformers = []
        if transformers is not None:
            self.transformers = transformers
        else:
            self.transformers = []


        super(TransformerBank, self).__init__(*args, **kw_args)
    # >>> transformer_bank

    # <<< transformers
    # @generated
    def get_transformers(self):
        """ All transformers that belong to this bank.
        """
        return self._transformers

    def set_transformers(self, value):
        for x in self._transformers:
            x._transformer_bank = None
        for y in value:
            y._transformer_bank = self
        self._transformers = value

    transformers = property(get_transformers, set_transformers)

    def add_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_bank = self
            self._transformers.append(obj)

    def remove_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_bank = None
            self._transformers.remove(obj)
    # >>> transformers



class DistributionTapChanger(RatioTapChanger):
    """ Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """
    # <<< distribution_tap_changer
    # @generated
    def __init__(self, monitored_phase='bc', target_voltage=0.0, reverse_line_drop_r=0.0, limit_voltage=0.0, reverse_line_drop_x=0.0, line_drop_r=0.0, line_drop_compensation=False, line_drop_x=0.0, band_voltage=0.0, ct_rating=0.0, pt_ratio=0.0, ct_ratio=0.0, *args, **kw_args):
        """ Initialises a new 'DistributionTapChanger' instance.

        @param monitored_phase: Phase voltage controlling this regulator, measured at regulator location. Values are: "bc", "ab", "b", "ac", "abc", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        @param target_voltage: Target voltage on the PT secondary base. 
        @param reverse_line_drop_r: Line drop compensator resistance setting for reverse power flow. 
        @param limit_voltage: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        @param reverse_line_drop_x: Line drop compensator reactance setting for reverse power flow. 
        @param line_drop_r: Line drop compensator resistance setting for normal (forward) power flow. 
        @param line_drop_compensation: If true, the line drop compensation is to be applied. 
        @param line_drop_x: Line drop compensator reactance setting for normal (forward) power flow. 
        @param band_voltage: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        @param ct_rating: Built-in current transformer primary rating. 
        @param pt_ratio: Built-in voltage transducer ratio. 
        @param ct_ratio: Built-in current transducer ratio. 
        """
        # Phase voltage controlling this regulator, measured at regulator location. Values are: "bc", "ab", "b", "ac", "abc", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.monitored_phase = monitored_phase

        # Target voltage on the PT secondary base. 
        self.target_voltage = target_voltage

        # Line drop compensator resistance setting for reverse power flow. 
        self.reverse_line_drop_r = reverse_line_drop_r

        # Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        self.limit_voltage = limit_voltage

        # Line drop compensator reactance setting for reverse power flow. 
        self.reverse_line_drop_x = reverse_line_drop_x

        # Line drop compensator resistance setting for normal (forward) power flow. 
        self.line_drop_r = line_drop_r

        # If true, the line drop compensation is to be applied. 
        self.line_drop_compensation = line_drop_compensation

        # Line drop compensator reactance setting for normal (forward) power flow. 
        self.line_drop_x = line_drop_x

        # Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        self.band_voltage = band_voltage

        # Built-in current transformer primary rating. 
        self.ct_rating = ct_rating

        # Built-in voltage transducer ratio. 
        self.pt_ratio = pt_ratio

        # Built-in current transducer ratio. 
        self.ct_ratio = ct_ratio



        super(DistributionTapChanger, self).__init__(*args, **kw_args)
    # >>> distribution_tap_changer



class PhaseImpedanceData(Element):
    """ Triplet of resistance, reactance, and susceptance matrix element values.
    """
    # <<< phase_impedance_data
    # @generated
    def __init__(self, x=0.0, sequence_number=0, b=0.0, r=0.0, phase_impedance=None, *args, **kw_args):
        """ Initialises a new 'PhaseImpedanceData' instance.

        @param x: Reactance matrix element value, per length of unit. 
        @param sequence_number: Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
        @param b: Susceptance matrix element value, per length of unit. 
        @param r: Resistance matrix element value, per length of unit. 
        @param phase_impedance: Conductor phase impedance to which this data belongs.
        """
        # Reactance matrix element value, per length of unit. 
        self.x = x

        # Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
        self.sequence_number = sequence_number

        # Susceptance matrix element value, per length of unit. 
        self.b = b

        # Resistance matrix element value, per length of unit. 
        self.r = r


        self._phase_impedance = None
        self.phase_impedance = phase_impedance


        super(PhaseImpedanceData, self).__init__(*args, **kw_args)
    # >>> phase_impedance_data

    # <<< phase_impedance
    # @generated
    def get_phase_impedance(self):
        """ Conductor phase impedance to which this data belongs.
        """
        return self._phase_impedance

    def set_phase_impedance(self, value):
        if self._phase_impedance is not None:
            filtered = [x for x in self.phase_impedance.phase_impedance_data if x != self]
            self._phase_impedance._phase_impedance_data = filtered

        self._phase_impedance = value
        if self._phase_impedance is not None:
            self._phase_impedance._phase_impedance_data.append(self)

    phase_impedance = property(get_phase_impedance, set_phase_impedance)
    # >>> phase_impedance



# <<< wires_ext
# @generated
# >>> wires_ext
