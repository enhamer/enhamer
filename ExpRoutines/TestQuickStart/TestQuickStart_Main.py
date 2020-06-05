# -*- coding: utf-8 -*-
#**============================================================================
#**
#**                         ENHAMER -script
#**                 THIS FILE IS PART OF THE ENHAMER
#**
#** TITLE:           TestQuickStart (Main)
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
Simple Routine for ENHAMER functionality check.
Start here initially and for troubleshooting.
"""
#%% Import Section
import logging
import Config.LoggerConfig

# Import instruments
import Instrumentation.Instrument as INSTR
import Instrumentation.TestQuickStart.TestInstrument as TST_INSTR


exp_details = { 
    'save_path'     : 'H:\X_SW\ENHAMER\_REL_PBL\\test',
    }



#################################################
#%% MAIN PROGRAM

# Config logger
loggerConfig=Config.LoggerConfig.LoggerConfig(folder=exp_details["save_path"], logLevel='DEBUG')
logger = logging.getLogger(__name__)

# Connect instruments
instrument = INSTR.Instrument()
instrument_resources = instrument.define_VISAresourceManager()

test_instrument  = instrument.create_instrument(TST_INSTR.TestInstrument, instrument_resources)



#################################################
#%% Send command and read response from the device.

test_instrument.identify()














#################################################
#%% NOTHING BELOW THIS LINE