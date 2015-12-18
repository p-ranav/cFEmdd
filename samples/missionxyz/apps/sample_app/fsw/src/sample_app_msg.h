/*******************************************************************************
** File:
**   sample_app_msg.h 
**
** Purpose: 
**  Define sample_app Messages and info
**
** Notes:
**
**
*******************************************************************************/
#ifndef _sample_app_msg_h_
#define _sample_app_msg_h_

/*
** sample_app command codes
*/
#define SAMPLE_NOOP_CC     1
#define SAMPLE_RESET_CC    2

/*************************************************************************/\
/*
** Definition of Table Data Structure
*/
typedef struct
{
    uint8             TblElement1;
    uint16            TblElement2;
    uint32            TblElement3;
} SAMPLE_MyFirstTable_t;

/*************************************************************************/

/*************************************************************************/\
/*
** Type definition Critical Data Store
*/
typedef struct
{
    uint32            DataPtFive;
} SAMPLE_CdsDataType_t;

/*************************************************************************/

/*************************************************************************/\
/*
** Type definition (generic "no arguments" command)
*/
typedef struct
{
    uint8            CmdHeader[CFS_SB_CMD_HDR_SIZE];
} SAMPLE_NoArgsCmd_t;

/*************************************************************************/
#endif /* _sample_app_msg_h_ */

/************************/
/*  End of File Comment */
/************************/
