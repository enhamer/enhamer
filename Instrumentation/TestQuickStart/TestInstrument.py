# -*- coding: utf-8 -*-
#**============================================================================
#**
#**                         ENHAMER -Library
#**                 THIS FILE IS PART OF THE ENHAMER
#**
#** TITLE:           Test-Instrument (library)
#**
#** AUTHOR:          Marcin J. Kraśny (m.j.krasny@nuigalway.ie)
#**
#**					 Advanced Biological Imaging Laboratory
#**                  School of Physics
#**                  College of Science and Engineering
#**                  National University of Ireland, Galway
#**
#** SOURCE URL       https://github.com/enhamer/enhamer
#** COPYRIGHT        © M.J.Kraśny
#** LICENSE          MIT
#** CREDITS          NEMESIS - Novel Energy Materials, Engineering Science 
#**                  and Integrated Systems
#**                  Department of Mechanical Engineering
#**					 University of Bath, UK
#**
#**============================================================================
#**============================================================================
"""
Basic library for Test-Instrument.
It's independent of any device, so any instrumentation such as an oscilloscope,
signal generator, ammeter or voltmeter can be used. The only requirement is 
the device must connect with a PC via a VISA protocol.
Library is designed to perform an initial test of user configuration and device 
connection with SCPI commands over TCPIP(LAN)/USB protocol.

Please connect and test your device prior to running this script as advised by 
the vendor of your instrumentation.
For more information, please visit: https://github.com/enhamer/enhamer
"""

import visa as pyvisa

import logging
import Instrumentation.Instrument as INSTR

from Instrumentation.StatusCodes import StatusCodes as Status


# DEFINE CONSTANTS ==================================================

DEVICE_NAME     = 'Test-Instrument' # Instrument's alias name

VISA_ADDRESS    = "USB0::0x2A8D::0x0396::CN59047589::0::INSTR"
                # VISA_ADDRESS = "TCPIP0::IP-address::inst0::INSTR"
                # Information is avaliable i.e. from:
                # Keysight IO Libraries Connection Expert

GLOBAL_TOUT     = 2024 # I/O timeout set in milliseconds

#====================================================================



class TestInstrument(INSTR.Instrument):
    """
    TestInstrument class provides an interacting interface
    for instrument control.
    """
        
    def __init__(self, instrument_resources):
        self.logger = logging.getLogger(__name__)
        
        self.DEVICE_NAME  = DEVICE_NAME
        self.GLOBAL_TOUT  = GLOBAL_TOUT
        self.VISA_ADDRESS = VISA_ADDRESS
        
        self.instrument_resources = instrument_resources
        
        self.INSTRUMENT_STATUS = Status.Disconnected
        self.logger.info('Creating an instance of: '+ self.DEVICE_NAME + ' ' + str(self.INSTRUMENT_STATUS))
        
        self._connect_instrument(instrument_resources)
    

    
    def identify(self):
        """
        Ask instrument to introduce itself.
        """
        s_command = '*IDN'
        response = self.send_query(s_command)
            
        if response[0] == pyvisa.constants.StatusCode.success:
            self.INSTRUMENT_STATUS = Status.OK
            response = response[1]
                
        else:
            self.logger.error('Unable to identify: ' + s_command + ' ' + str(response[0]))
            self.INSTRUMENT_STATUS = Status.Error
        
        return response