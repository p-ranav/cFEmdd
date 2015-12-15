/*******************************************************************************
** File: sample_app_app.c
**
** Purpose:
**   This file contains the source code for the sample_app App.
**
*******************************************************************************/

/*
**   Include Files:
*/

#include "sample_app_app.h"
#include "sample_app_app_msg.h"
#include "sample_app_app_events.h"
#include "sample_app_version.h"

/** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/* SAMPLE_APP_AppMain() -- Application entry point and main process loop          */
/*                                                                            */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *  * * * * **/
void SAMPLE_APP_AppMain( void )
{
    int32  status;
    uint32 RunStatus = CFE_ES_APP_RUN;

    CFE_ES_PerfLogEntry(SAMPLE_APP_APP_PERF_ID);

    SAMPLE_APP_AppInit();

    /*
    ** SAMPLE_APP Runloop
    */
    while (CFE_ES_RunLoop(&RunStatus) == TRUE)
    {
        CFE_ES_PerfLogExit(SAMPLE_APP_APP_PERF_ID);

        /* Pend on receipt of command packet -- timeout set to 500 millisecs */
        status = CFE_SB_RcvMsg(&SAMPLE_APPMsgPtr, SAMPLE_APP_CommandPipe, 500);
        
        CFE_ES_PerfLogEntry(SAMPLE_APP_APP_PERF_ID);

        if (status == CFE_SUCCESS)
        {
            SAMPLE_APP_ProcessCommandPacket();
        }

    }

    CFE_ES_ExitApp(RunStatus);

} /* End of SAMPLE_APP_AppMain() */
