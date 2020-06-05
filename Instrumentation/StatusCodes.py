# -*- coding: utf-8 -*-
#**============================================================================
#**
#**                         ENHAMER -Library
#**                 THIS FILE IS PART OF THE ENHAMER
#**
#** TITLE:           StatusCodes
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
System status codes.
"""
import enum as enum_type

class StatusCodes(enum_type.Enum):
    Error        = -1
    OK           = 0 
    Connected    = 1
    Disconnected = 2
    
    Busy         = 4
    NotFound     = 5
    TimeOut      = 6
    BadParam     = 7