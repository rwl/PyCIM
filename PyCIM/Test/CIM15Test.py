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

import unittest

import pytest

from CIM15.IEC61970.Core import \
    ConnectivityNode, Terminal

from CIM15.IEC61970.LoadModel import \
    ConformLoad, ConformLoadGroup, LoadArea, ConformLoadSchedule

from CIM15.IEC61970.Meas import \
    AnalogLimit, AnalogValue, Analog

from CIM15.IEC61970.Protection import \
    CurrentRelay, ProtectionEquipment

from CIM15.IEC61970.Topology import \
    TopologicalNode

from CIM15.IEC61970.Wires import \
    Breaker, SynchronousMachine, BusbarSection, ACLineSegment, \
    PowerTransformer, PowerTransformerEnd, ReactiveCapabilityCurve, \
    EnergyConsumer, PerLengthPhaseImpedance, PerLengthSequenceImpedance

from CIM15.IEC61970.Generation.Production import \
    ThermalGeneratingUnit, GenUnitOpCostCurve, GenUnitOpSchedule, StartupModel


from CIM15.IEC61970.WiresPhaseModel import \
    EnergyConsumerPhase, ACLineSegmentPhase


class CIMTestCase(unittest.TestCase):
    """Test the full CIM package.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass

    def test_energy_consumer_phase_sets_attributes(self):
        energy_consumer = EnergyConsumer()
        energy_consumer_phase = EnergyConsumerPhase('A', energy_consumer)
        assert energy_consumer_phase.phase == 'A'
        assert energy_consumer_phase.EnergyConsumer == energy_consumer

    def testInstantiation(self):
        """Test element instantiation.
        """
        ThermalGeneratingUnit(oMCost=6.0, variableCost=10.0)
        GenUnitOpCostCurve(name="curve1", isNetGrossP=True)
        GenUnitOpSchedule(timeStep=1.0)
        StartupModel(name="model1", startupCost=20.0)

        ConformLoad(aggregate=True, pfixed=30.0)
        clg = ConformLoadGroup(aliasName="group1")
        LoadArea(name="area1")
        cls = ConformLoadSchedule(ConformLoadGroup=clg)
        self.assertEqual(cls.ConformLoadGroup, clg)

        AnalogLimit(value=100.0)
        AnalogValue(value=6.0)
        Analog(maxValue=100.0)
        ProtectionEquipment(normallyInService=True)
        CurrentRelay(inverseTimeFlag=True)

        tn = TopologicalNode(name="tn1")
        cn = ConnectivityNode(TopologicalNode=tn)
        self.assertTrue(cn.TopologicalNode, tn)
        Terminal(connected=True)

        Breaker(ratedCurrent=20.0)
        SynchronousMachine(coolantType="water")
        BusbarSection(normallyInService=True)
        ACLineSegment(r=0.1, length=10.0)
        ReactiveCapabilityCurve(coolantTemperature=20.0)
        te = PowerTransformerEnd(x0=0.1)
        pt = PowerTransformer(PowerTransformerEnd=[te])
        self.assertTrue(te in pt.PowerTransformerEnd)


    def testOneToOne(self):
        """Test one-to-one bidirectional references.
        """
        sm1 = StartupModel()
        tgu1 = ThermalGeneratingUnit(StartupModel=sm1)

        self.assertEqual(tgu1.StartupModel, sm1)
        self.assertEqual(sm1.ThermalGeneratingUnit, tgu1)

        tgu2 = ThermalGeneratingUnit()
        tgu2.setStartupModel(sm1)

        self.assertEqual(tgu1.StartupModel, None)
        self.assertEqual(tgu2.StartupModel, sm1)
        self.assertNotEqual(sm1.ThermalGeneratingUnit, tgu1)
        self.assertTrue(sm1.ThermalGeneratingUnit, tgu2)


    def testOneToMany(self):
        """Test one-to-many bidirectional references.
        """
        lg1 = ConformLoadGroup(name="CLG1")
        lg2 = ConformLoadGroup(name="CLG2")
        cl = ConformLoad(name="Load 1", LoadGroup=lg1)

        self.assertEqual(cl.LoadGroup, lg1)
        self.assertTrue(cl in lg1.EnergyConsumers)

        cl.setLoadGroup(lg2)

        self.assertNotEqual(cl.LoadGroup, lg1)
        self.assertEqual(cl.LoadGroup, lg2)
        self.assertFalse(cl in lg1.EnergyConsumers)
        self.assertTrue(cl in lg2.EnergyConsumers)


    def testManyToOne(self):
        """Test many-to-one bidirectional references.
        """
        te1 = PowerTransformerEnd()
        te2 = PowerTransformerEnd()
        pt1 = PowerTransformer(PowerTransformerEnd=[te1])
        pt1.addPowerTransformerEnd(te2)

        self.assertTrue(te1 in pt1.PowerTransformerEnd)
        self.assertTrue(te2 in pt1.PowerTransformerEnd)
        self.assertEqual(te1.PowerTransformer, pt1)
        self.assertEqual(te2.PowerTransformer, pt1)

        pt2 = PowerTransformer()
        pt2.addPowerTransformerEnd(te2)

        self.assertTrue(te1 in pt1.PowerTransformerEnd)
        self.assertTrue(te2 in pt2.PowerTransformerEnd)
        self.assertFalse(te2 in pt1.PowerTransformerEnd)
        self.assertNotEqual(te2.PowerTransformer, pt1)
        self.assertEqual(te2.PowerTransformer, pt2)

        te3 = PowerTransformerEnd()
        pt1.setPowerTransformerEnd([te3])

        self.assertFalse(te1 in pt1.PowerTransformerEnd)
        self.assertTrue(te3 in pt1.PowerTransformerEnd)
        self.assertEqual(te1.PowerTransformer, None)
        self.assertEqual(te3.PowerTransformer, pt1)

        pt1.removePowerTransformerEnd(te3)

        self.assertFalse(te3 in pt1.PowerTransformerEnd)
        self.assertEqual(te3.PowerTransformer, None)


#    def testManyToMany(self):
#        """Test many-to-many bidirectional references.
#        """
#        sm1 = SynchronousMachine()
#        sm2 = SynchronousMachine()
#        rcc1 = ReactiveCapabilityCurve()
#        sm1.add_reactive_capability_curves(rcc1)
#        rcc2 = ReactiveCapabilityCurve(synchronous_machines=[sm2])
#
#        self.assertTrue(sm1 in rcc1.synchronous_machines)
#        self.assertTrue(rcc2 in sm2.reactive_capability_curves)


class ACLineSegmentTests(unittest.TestCase):

    def test_ac_line_segment_phases_sets_attributes(self):
        ac_line_segment = ACLineSegment()
        ac_line_segment_phase = ACLineSegmentPhase('A', ac_line_segment)
        assert ac_line_segment_phase.phase == 'A'
        assert ac_line_segment_phase.ACLineSegment == ac_line_segment

    def test_sets_per_length_impedance_given_phase(self):
        per_length_phase_impedance = PerLengthPhaseImpedance()
        ac_line_segment = ACLineSegment(
                PhaseImpedance=per_length_phase_impedance)
        assert ac_line_segment.PerLengthImpedance == per_length_phase_impedance
        assert ac_line_segment.PhaseImpedance == per_length_phase_impedance
        assert ac_line_segment.SequenceImpedance is None

    def test_sets_per_length_impedance_given_sequence(self):
        per_length_sequence_impedance = PerLengthSequenceImpedance()
        ac_line_segment = ACLineSegment(
                SequenceImpedance=per_length_sequence_impedance)
        assert ac_line_segment.PerLengthImpedance == \
                per_length_sequence_impedance
        assert ac_line_segment.SequenceImpedance == \
                per_length_sequence_impedance
        assert ac_line_segment.PhaseImpedance is None

    def test_sets_per_length_impedance_given_phase_via_generic(self):
        per_length_phase_impedance = PerLengthPhaseImpedance()
        ac_line_segment = ACLineSegment(
                PerLengthImpedance=per_length_phase_impedance)
        assert ac_line_segment.PerLengthImpedance == per_length_phase_impedance
        assert ac_line_segment.PhaseImpedance == per_length_phase_impedance
        assert ac_line_segment.SequenceImpedance is None

    def test_sets_per_length_impedance_given_sequence_via_generic(self):
        per_length_sequence_impedance = PerLengthSequenceImpedance()
        ac_line_segment = ACLineSegment(
                PerLengthImpedance=per_length_sequence_impedance)
        assert ac_line_segment.PerLengthImpedance == per_length_sequence_impedance
        assert ac_line_segment.SequenceImpedance == per_length_sequence_impedance
        assert ac_line_segment.PhaseImpedance is None

    def test_more_than_one_impedance_returns_error(self):
        per_length_sequence_impedance = PerLengthSequenceImpedance()
        per_length_phase_impedance = PerLengthPhaseImpedance()
        with pytest.raises(ValueError):
            ac_line_segment = ACLineSegment(
                PhaseImpedance=per_length_phase_impedance,
                SequenceImpedance=per_length_sequence_impedance)


if __name__ == "__main__":
    unittest.main()
