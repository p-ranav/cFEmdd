/*******************************************************************************
** File:
**   sample_app_2_msg.h 
**
** Purpose: 
**  Define sample_app_2 Messages and info
**
** Notes:
**
**
*******************************************************************************/
#ifndef _sample_app_2_msg_h_
#define _sample_app_2_msg_h_

/*
** sample_app_2 command codes
*/
#define QQ_NOOP_CC     1
#define QQ_RESET_CC    2

/*************************************************************************/\
/*
** Type definition (generic "no arguments" command)
*/
typedef struct
{
    uint8            CmdHeader[CFS_SB_CMD_HDR_SIZE];
} QQ_NoArgsCmd_t;

/*************************************************************************/
#endif /* _sample_app_2_msg_h_ */

/************************/
/*  End of File Comment */
/************************/
