# -*- coding: utf-8 -*-
#**============================================================================
#**
#**                         ENHAMER -Library
#**                 THIS FILE IS PART OF THE ENHAMER
#**
#** TITLE:           Instrument (library)
#**
#** AUTHOR:          Marcin J. Kraśny
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
Abstract class acting as an universal wrapper for VISA communication.
"""

import logging
import visa as pyvisa

from Instrumentation.StatusCodes import StatusCodes as Status


logger = logging.getLogger(__name__)
pyvisa_logger = logging.getLogger('pyvisa')
pyvisa_logger.setLevel(logging.INFO)    


class Instrument(object):
    
    def __init__(self):
        self.logger = logger
    
    def define_VISAresourceManager(self):
        """ 
        Define install directory of VISA Resource Manager.
        
        VISA directory will need to be changed if VISA backend was not 
        installed in a default directory.
        By default the path is: 
        rm = visa.ResourceManager('C:\\Windows\\System32\\visa32.dll')
        Due to that a simplified command: rm = visa.ResourceManager() is valid.
        """
        
        instrument_resources = pyvisa.ResourceManager()
        
        self.logger.info(instrument_resources.session)
        self.logger.info(instrument_resources.list_resources())
        
        return instrument_resources
    
    
    def create_instrument(self, InstrumentClass, instrument_resources):
        """
        Create an instrument handler to the device.
        """
        instr_hndl  = InstrumentClass(instrument_resources)
        return instr_hndl


    def _connect_instrument(self, instrument_resources):
        """
        Establish connection between Instrument and VISA controller.
        """
        
        logger.info('Connect instrument: '+ self.DEVICE_NAME)
        
        try:
            self.instrument = instrument_resources.open_resource(self.VISA_ADDRESS)
            
        except pyvisa.VisaIOError as err:
            logger.error('Unable to connect to ' + self.DEVICE_NAME + ' VISA Address: ' + self.VISA_ADDRESS)
            logger.error(err)
            
            self.INSTRUMENT_STATUS = Status.Error
            
        else:
            logger.info(self.DEVICE_NAME + ' ' + str(self.INSTRUMENT_STATUS))
            self.INSTRUMENT_STATUS = Status.Connected
            self._set_visa_setup()
            # self.clear_error_que()
            # self.whoIm = self.identify()
        
        return self.INSTRUMENT_STATUS
    
    
    def _disconnect_instrument(self):
        """
        Disconnect instrument from VISA controller.
        """    
        self.instrument.close()
    
    
    def _set_visa_setup(self):
        """
        Initial configuration of the instrument (i.e. timeout, 
                                                 command termination).
        """
        logger.info('Initial VISA setup of: '+ self.DEVICE_NAME)
        
        self.instrument.timeout = self.GLOBAL_TOUT
        #self.instrument.encoding = 'latin_1' # alternatively use: utf-8 
        #self.instrument.read_termination = '\n'
        #self.instrument.write_termination = '\n'
        self.instrument.clear() # Clear the instrument bus
        
    

    def send_command(self, s_command, s_value=''):
        """ 
        Writes command to the instrument.
        """
        
        logger.info('Send_command: ' + s_command + ' ' + str(s_value))
        
        r_ins_status = 0 # returned instrument status
        
        try:
            self.instrument.write('%s %s' % (s_command, str(s_value)))
        
        except pyvisa.VisaIOError as err:  
            
            r_ins_status = self.instrument.last_status
            
            logger.error(self.DEVICE_NAME+ ': ' + 'Unable to send command: ' + str(r_ins_status))
            logger.error(err)
            
        else:
            r_ins_status = self.instrument.last_status
            
        return r_ins_status         
        
            
    def send_query(self, s_query, add_qm = True):
        """ 
        Writes query to the instrument, then reads its respond.
        """
        
        r_ins_status = 0 # returned instrument status
        r_response = 0
        
        
        if add_qm:
            s_query = s_query +'?'
        
        logger.info(self.DEVICE_NAME+ ': ' + 'Send_query: ' + s_query)
        
        try:
            r_response = self.instrument.query(s_query)    
        
        except pyvisa.VisaIOError as err: 
            
            r_ins_status = self.instrument.last_status
            
            logger.error(self.DEVICE_NAME+ ': ' + 'Unable to send query ' + str(r_ins_status))
            logger.error(err)
        
        else:
        
            logger.info(self.DEVICE_NAME+ ': ' + 'Response: ' + r_response)
            r_ins_status = self.instrument.last_status
            
        return r_ins_status, r_response   