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

import unittest

from CIM14v13.IEC61970.LoadModel import \
    ConformLoad, ConformLoadGroup, LoadArea, ConformLoadSchedule

from CIM14v13.IEC61970.Meas import \
    AnalogLimit, AnalogValue, Analog

from CIM14v13.IEC61970.Protection import \
    SurgeProtector, CurrentRelay

from CIM14v13.IEC61970.Topology import \
    ConnectivityNode, TopologicalNode

from CIM14v13.IEC61970.Wires import \
    Breaker, SynchronousMachine, BusbarSection, ACLineSegment, \
    PowerTransformer, TransformerWinding, ReactiveCapabilityCurve

from CIM14v13.IEC61970.Generation.Production import \
    ThermalGeneratingUnit, GenUnitOpCostCurve, GenUnitOpSchedule, StartupModel

class CIMTestCase(unittest.TestCase):
    """Test the full CIM package.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass


    def testInstantiation(self):
        """Test element instantiation.
        """
        ThermalGeneratingUnit(oMCost=6.0, variableCost=10.0)
        GenUnitOpCostCurve(name="curve1", isNetGrossP=True)
        GenUnitOpSchedule(timeStep=1.0)
        StartupModel(name="model1", startupCost=20.0)

        ConformLoad(phases="A", pfixed=30.0)
        clg = ConformLoadGroup(description="group")
        LoadArea(name="area1")
        cls = ConformLoadSchedule(ConformLoadGroup=clg)
        self.assertEqual(cls.ConformLoadGroup, clg)

        AnalogLimit(value=100.0)
        AnalogValue(value=6.0)
        Analog(maxValue=100.0)
        SurgeProtector(normaIlyInService=True)
        CurrentRelay(inverseTimeFlag=True)

        tn = TopologicalNode(name="tn1")
        cn = ConnectivityNode(TopologicalNode=tn)
        self.assertTrue(cn.TopologicalNode, tn)

        Breaker(ratedCurrent=20.0)
        SynchronousMachine(coolantType="water")
        BusbarSection(phases="ABC")
        ACLineSegment(r=0.1, length=10.0)
        ReactiveCapabilityCurve(coolantTemperature=20.0)
        tw = TransformerWinding(windingType="primary")
        pt = PowerTransformer(TransformerWindings=[tw])
        self.assertTrue(tw in pt.TransformerWindings)


#    def testOneToOne(self):
#        """Test one-to-one bidirectional references.
#        """
#        sm1 = StartupModel()
#        tgu1 = ThermalGeneratingUnit(startup_model=sm1)
#
#        self.assertEqual(sm1.thermal_generating_unit, tgu1)
#
#        tgu2 = ThermalGeneratingUnit()
#        tgu2.set_startup_model(sm1)
#
#        self.assertNotEqual(sm1.thermal_generating_unit, tgu1)
#        self.assertTrue(sm1.thermal_generating_unit, tgu2)
#
#
#    def testOneToMany(self):
#        """Test one-to-many bidirectional references.
#        """
#        lg1 = ConformLoadGroup(name="CLG1")
#        lg2 = ConformLoadGroup(name="CLG2")
#        cl = ConformLoad(name="Load 1", load_group=lg1)
#
#        self.assertTrue(cl in lg1.energy_consumers)
#
#        cl.set_load_group(lg2)
#
#        self.assertFalse(cl in lg1.energy_consumers)
#        self.assertTrue(cl in lg1.energy_consumers)
#
#
#    def testManyToOne(self):
#        """Test many-to-one bidirectional references.
#        """
#        tw1 = TransformerWinding()
#        pt1 = PowerTransformer(transformer_windings=[tw1])
#        tw2 = TransformerWinding()
#        pt1.add_transformer_windings()
#
#        self.assertEqual(tw1.power_transformer, pt1)
#        self.assertEqual(tw2.power_transformer, pt1)
#
#        pt2 = PowerTransformer()
#        pt2.add_transformer_windings(tw2)
#
#        self.assertNotEqual(tw2.power_transformer, pt1)
#        self.assertEqual(tw2.power_transformer, pt2)
#
#
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


if __name__ == "__main__":
    unittest.main()
