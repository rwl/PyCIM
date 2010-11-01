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

from CIM14v13.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class PWRSteamSupply(SteamSupply):
    """Pressurized water reactor used as a steam supply to a steam turbine
    """

    def __init__(self, coreHTLagTC1=0.0, hotLegSteamGain=0.0, coldLegLagTC=0.0, coreNeutronicsEffTC=0.0, steamFlowFG=0.0, throttlePressureFactor=0.0, hotLegToColdLegGain=0.0, throttlePressureSP=0.0, steamPressureDropLagTC=0.0, coreHTLagTC2=0.0, coldLegFG1=0.0, coldLegFBLagTC=0.0, hotLegLagTC=0.0, coldLegFBLeadTC2=0.0, pressureCG=0.0, coldLegFBLeadTC1=0.0, coldLegFG2=0.0, coreNeutronicsHT=0.0, steamPressureFG=0.0, feedbackFactor=0.0, *args, **kw_args):
        """Initializes a new 'PWRSteamSupply' instance.

        @param coreHTLagTC1: Core Heat Transfer Lag Time Constant 
        @param hotLegSteamGain: Hot Leg Steam Gain 
        @param coldLegLagTC: Cold Leg Lag Time Constant 
        @param coreNeutronicsEffTC: Core Neutronics Effective Time Constant 
        @param steamFlowFG: Steam Flow Feedback Gain 
        @param throttlePressureFactor: Throttle Pressure Factor 
        @param hotLegToColdLegGain: Hot Leg To Cold Leg Gain 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param steamPressureDropLagTC: Steam Pressure Drop Lag Time Constant 
        @param coreHTLagTC2: Core Heat Transfer Lag Time Constant 
        @param coldLegFG1: Cold Leg Feedback Gain 1 
        @param coldLegFBLagTC: Cold Leg Feedback Lag Time Constant 
        @param hotLegLagTC: Hot Leg Lag Time Constant 
        @param coldLegFBLeadTC2: Cold Leg Feedback Lead Time Constant 
        @param pressureCG: Pressure Control Gain 
        @param coldLegFBLeadTC1: Cold Leg Feedback Lead Time Constant 
        @param coldLegFG2: Cold Leg Feedback Gain 2 
        @param coreNeutronicsHT: Core Neutronics And Heat Transfer 
        @param steamPressureFG: Steam Pressure Feedback Gain 
        @param feedbackFactor: Feedback Factor 
        """
        #: Core Heat Transfer Lag Time Constant 
        self.coreHTLagTC1 = coreHTLagTC1

        #: Hot Leg Steam Gain 
        self.hotLegSteamGain = hotLegSteamGain

        #: Cold Leg Lag Time Constant 
        self.coldLegLagTC = coldLegLagTC

        #: Core Neutronics Effective Time Constant 
        self.coreNeutronicsEffTC = coreNeutronicsEffTC

        #: Steam Flow Feedback Gain 
        self.steamFlowFG = steamFlowFG

        #: Throttle Pressure Factor 
        self.throttlePressureFactor = throttlePressureFactor

        #: Hot Leg To Cold Leg Gain 
        self.hotLegToColdLegGain = hotLegToColdLegGain

        #: Throttle Pressure Setpoint 
        self.throttlePressureSP = throttlePressureSP

        #: Steam Pressure Drop Lag Time Constant 
        self.steamPressureDropLagTC = steamPressureDropLagTC

        #: Core Heat Transfer Lag Time Constant 
        self.coreHTLagTC2 = coreHTLagTC2

        #: Cold Leg Feedback Gain 1 
        self.coldLegFG1 = coldLegFG1

        #: Cold Leg Feedback Lag Time Constant 
        self.coldLegFBLagTC = coldLegFBLagTC

        #: Hot Leg Lag Time Constant 
        self.hotLegLagTC = hotLegLagTC

        #: Cold Leg Feedback Lead Time Constant 
        self.coldLegFBLeadTC2 = coldLegFBLeadTC2

        #: Pressure Control Gain 
        self.pressureCG = pressureCG

        #: Cold Leg Feedback Lead Time Constant 
        self.coldLegFBLeadTC1 = coldLegFBLeadTC1

        #: Cold Leg Feedback Gain 2 
        self.coldLegFG2 = coldLegFG2

        #: Core Neutronics And Heat Transfer 
        self.coreNeutronicsHT = coreNeutronicsHT

        #: Steam Pressure Feedback Gain 
        self.steamPressureFG = steamPressureFG

        #: Feedback Factor 
        self.feedbackFactor = feedbackFactor

        super(PWRSteamSupply, self).__init__(*args, **kw_args)

