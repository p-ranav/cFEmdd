/*******************************************************************************
** File: sample_app_2.h
**
** Purpose:
**   This file is main hdr file for the sample_app_2 application.
**
**
*******************************************************************************/

#ifndef _sample_app_2_h_
#define _sample_app_2_h_

/*
** Required header files.
*/
#include "cfe.h"
#include "cfe_error.h"
#include "cfe_evs.h"
#include "cfe_sb.h"
#include "cfe_es.h"

#include <string.h>
#include <errno.h>
#include <unistd.h>

/***********************************************************************/

#define SAMPLE_APP_2_PIPE_DEPTH                     32

/************************************************************************
** Type Definitions
*************************************************************************/

/****************************************************************************/
/*
** Local function prototypes.
**
** Note: Except for the entry point (SAMPLE_APP_2_AppMain), these
**       functions are not called from any other source module.
*/
void SAMPLE_APP_2_AppMain(void);
void SAMPLE_APP_2_AppInit(void);
void SAMPLE_APP_2_ProcessCommandPacket(void);
void SAMPLE_APP_2_ProcessGroundCommand(void);
void SAMPLE_APP_2_ReportHousekeeping(void);
void SAMPLE_APP_2_ResetCounters(void);

boolean SAMPLE_APP_2_VerifyCmdLength(CFE_SB_MsgPtr_t msg, uint16 ExpectedLength);

#endif /* _sample_app_2_h_ */
