# -*- coding: utf-8 -*-
# ********************************************************************
#
#  $Id: yocto_tvoc.py 33270 2018-11-22 08:41:15Z seb $
#
#  Implements yFindTvoc(), the high-level API for Tvoc functions
#
#  - - - - - - - - - License information: - - - - - - - - -
#
#  Copyright (C) 2011 and beyond by Yoctopuce Sarl, Switzerland.
#
#  Yoctopuce Sarl (hereafter Licensor) grants to you a perpetual
#  non-exclusive license to use, modify, copy and integrate this
#  file into your software for the sole purpose of interfacing
#  with Yoctopuce products.
#
#  You may reproduce and distribute copies of this file in
#  source or object form, as long as the sole purpose of this
#  code is to interface with Yoctopuce products. You must retain
#  this notice in the distributed source file.
#
#  You should refer to Yoctopuce General Terms and Conditions
#  for additional information regarding your rights and
#  obligations.
#
#  THE SOFTWARE AND DOCUMENTATION ARE PROVIDED 'AS IS' WITHOUT
#  WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING
#  WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, FITNESS
#  FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO
#  EVENT SHALL LICENSOR BE LIABLE FOR ANY INCIDENTAL, SPECIAL,
#  INDIRECT OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA,
#  COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR
#  SERVICES, ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT
#  LIMITED TO ANY DEFENSE THEREOF), ANY CLAIMS FOR INDEMNITY OR
#  CONTRIBUTION, OR OTHER SIMILAR COSTS, WHETHER ASSERTED ON THE
#  BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE), BREACH OF
#  WARRANTY, OR OTHERWISE.
#
# *********************************************************************


__docformat__ = 'restructuredtext en'
from yocto_api import *


#--- (YTvoc class start)
#noinspection PyProtectedMember
class YTvoc(YSensor):
    """
    The Yoctopuce class YTvoc allows you to read and configure Yoctopuce Total Volatile Organic
    Compound sensors. It inherits from YSensor class the core functions to read measurements,
    to register callback functions, to access the autonomous datalogger.

    """
    #--- (end of YTvoc class start)
    #--- (YTvoc return codes)
    #--- (end of YTvoc return codes)
    #--- (YTvoc dlldef)
    #--- (end of YTvoc dlldef)
    #--- (YTvoc yapiwrapper)
    #--- (end of YTvoc yapiwrapper)
    #--- (YTvoc definitions)
    #--- (end of YTvoc definitions)

    def __init__(self, func):
        super(YTvoc, self).__init__(func)
        self._className = 'Tvoc'
        #--- (YTvoc attributes)
        self._callback = None
        #--- (end of YTvoc attributes)

    #--- (YTvoc implementation)
    def _parseAttr(self, json_val):
        super(YTvoc, self)._parseAttr(json_val)

    @staticmethod
    def FindTvoc(func):
        """
        Retrieves a Total  Volatile Organic Compound sensor for a given identifier.
        The identifier can be specified using several formats:
        <ul>
        <li>FunctionLogicalName</li>
        <li>ModuleSerialNumber.FunctionIdentifier</li>
        <li>ModuleSerialNumber.FunctionLogicalName</li>
        <li>ModuleLogicalName.FunctionIdentifier</li>
        <li>ModuleLogicalName.FunctionLogicalName</li>
        </ul>

        This function does not require that the Total  Volatile Organic Compound sensor is online at the time
        it is invoked. The returned object is nevertheless valid.
        Use the method YTvoc.isOnline() to test if the Total  Volatile Organic Compound sensor is
        indeed online at a given time. In case of ambiguity when looking for
        a Total  Volatile Organic Compound sensor by logical name, no error is notified: the first instance
        found is returned. The search is performed first by hardware name,
        then by logical name.

        If a call to this object's is_online() method returns FALSE although
        you are certain that the matching device is plugged, make sure that you did
        call registerHub() at application initialization time.

        @param func : a string that uniquely characterizes the Total  Volatile Organic Compound sensor

        @return a YTvoc object allowing you to drive the Total  Volatile Organic Compound sensor.
        """
        # obj
        obj = YFunction._FindFromCache("Tvoc", func)
        if obj is None:
            obj = YTvoc(func)
            YFunction._AddToCache("Tvoc", func, obj)
        return obj

    def nextTvoc(self):
        """
        Continues the enumeration of Total Volatile Organic Compound sensors started using yFirstTvoc().
        Caution: You can't make any assumption about the returned Total Volatile Organic Compound sensors order.
        If you want to find a specific a Total  Volatile Organic Compound sensor, use Tvoc.findTvoc()
        and a hardwareID or a logical name.

        @return a pointer to a YTvoc object, corresponding to
                a Total  Volatile Organic Compound sensor currently online, or a None pointer
                if there are no more Total Volatile Organic Compound sensors to enumerate.
        """
        hwidRef = YRefParam()
        if YAPI.YISERR(self._nextFunction(hwidRef)):
            return None
        if hwidRef.value == "":
            return None
        return YTvoc.FindTvoc(hwidRef.value)

#--- (end of YTvoc implementation)

#--- (YTvoc functions)

    @staticmethod
    def FirstTvoc():
        """
        Starts the enumeration of Total Volatile Organic Compound sensors currently accessible.
        Use the method YTvoc.nextTvoc() to iterate on
        next Total Volatile Organic Compound sensors.

        @return a pointer to a YTvoc object, corresponding to
                the first Total Volatile Organic Compound sensor currently online, or a None pointer
                if there are none.
        """
        devRef = YRefParam()
        neededsizeRef = YRefParam()
        serialRef = YRefParam()
        funcIdRef = YRefParam()
        funcNameRef = YRefParam()
        funcValRef = YRefParam()
        errmsgRef = YRefParam()
        size = YAPI.C_INTSIZE
        #noinspection PyTypeChecker,PyCallingNonCallable
        p = (ctypes.c_int * 1)()
        err = YAPI.apiGetFunctionsByClass("Tvoc", 0, p, size, neededsizeRef, errmsgRef)

        if YAPI.YISERR(err) or not neededsizeRef.value:
            return None

        if YAPI.YISERR(
                YAPI.yapiGetFunctionInfo(p[0], devRef, serialRef, funcIdRef, funcNameRef, funcValRef, errmsgRef)):
            return None

        return YTvoc.FindTvoc(serialRef.value + "." + funcIdRef.value)

#--- (end of YTvoc functions)
