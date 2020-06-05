# -*- coding: utf-8 -*-
#**============================================================================
#**
#**                         ENHAMER -Library
#**                 THIS FILE IS PART OF THE ENHAMER
#**
#** TITLE:           Logger-Config (Cfg Files)
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
Logger Configuration
"""

import logging 
import time


class LoggerConfig(object):
    """
    Logger settings and config.
    """    
    
    def __init__(self, logger=None, folder = 'logs', logLevel='DEBUG'):
                
        folder = folder
        name_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        file_extension = '.log'
        
        self.logFileName = folder + '\\logs\\' + name_time + file_extension 
                   
        self.logger = logging.getLogger() # logger or logging.getLogger()
        self.configure_logger(self.logFileName, logLevel)


    def configure_logger(self, logFileName, logLevel):
        """
        Configure general logger.
        """
        # create logger
        #log = logging.getLogger() # no name for the root logger
        #self.logger.setLevel(logging.DEBUG) # global/general log level
        
        self.logger.setLevel(logLevel) #global/general log level
         
        # Logging Levels
        # Level	   Value
        # CRITICAL	50
        # ERROR	    40
        # WARNING	30
        # INFO	    20
        # DEBUG	    10
        # NOTSET	 0
        
        # create formatter
        fileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(message)s')
        consoleformatter = logging.Formatter('%(name)s - %(levelname)s  - %(message)s')
        
        # create file handler (sends logging output to a disk file) and set level
        log_file_hdlr = logging.FileHandler(logFileName, mode='a', encoding=None, delay=False)
        log_file_hdlr.setLevel(logLevel)
        
        # add formatter to log_file_hdlr
        log_file_hdlr.setFormatter(fileformatter)
        
        # add log_file_hdlr to logger
        self.logger.addHandler(log_file_hdlr)
        
        
        # create console handler (sends logging output to a standard output) and set level
        log_console_hdlr = logging.StreamHandler()
        log_console_hdlr.setLevel(logLevel)
        
        # add formatter to log_file_hdlr
        log_console_hdlr.setFormatter(consoleformatter)
        
        # add log_file_hdlr to logger
        self.logger.addHandler(log_console_hdlr)
    
        return True
    

    def set_exp_logger(self, folder, logFileName, logLevel):
        """
        Configure new experiment logger.
        """
        name_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        file_extension = '.log'
        
        logFileName = folder + '\\' + name_time + '_' + logFileName + file_extension 
        
        
        fileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(message)s')

        # create file handler (sends logging output to a disk file) and set level
        log_file_hdlr = logging.FileHandler(logFileName, mode='a', encoding=None, delay=False)
        log_file_hdlr.setLevel(logLevel)
        
        # add formatter to log_file_hdlr
        log_file_hdlr.setFormatter(fileformatter)
        
        # add log_file_hdlr to logger
        self.logger.addHandler(log_file_hdlr)
        
        return True
        

    def reset_last_logger(self):
        """
        Remove last logger from the liat (the most recent one).
        """
        print('reset_last_logger')
        last_hndl = len(self.logger.handlers)-1
        x = self.logger.handlers[last_hndl]
        
        x = self.logger.handlers[last_hndl]
        self.logger.removeHandler(x)
        x.flush()
        x.close()


    def _reset_loggers(self):
        """
        Clear all loggers from the list.
        """
        
        # print('reset logers')
        
        x = list(self.logger.handlers)
        
        for i in x:
            self.logger.removeHandler(i)
            i.flush()
            i.close()