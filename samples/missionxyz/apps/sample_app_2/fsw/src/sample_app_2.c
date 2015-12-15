/*******************************************************************************
** File: sample_app_2_app.c
**
** Purpose:
**   This file contains the source code for the sample_app_2 App.
**
*******************************************************************************/

/*
**   Include Files:
*/

#include "sample_app_2_app.h"
#include "sample_app_2_app_msg.h"
#include "sample_app_2_app_events.h"
#include "sample_app_2_version.h"

/** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/* SAMPLE_APP_2_AppMain() -- Application entry point and main process loop          */
/*                                                                            */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *  * * * * **/
void SAMPLE_APP_2_AppMain( void )
{
    int32  status;
    uint32 RunStatus = CFE_ES_APP_RUN;

    CFE_ES_PerfLogEntry(SAMPLE_APP_2_APP_PERF_ID);

    SAMPLE_APP_2_AppInit();

    /*
    ** SAMPLE_APP_2 Runloop
    */
    while (CFE_ES_RunLoop(&RunStatus) == TRUE)
    {
        CFE_ES_PerfLogExit(SAMPLE_APP_2_APP_PERF_ID);

        /* Pend on receipt of command packet -- timeout set to 500 millisecs */
        status = CFE_SB_RcvMsg(&SAMPLE_APP_2MsgPtr, SAMPLE_APP_2_CommandPipe, 500);
        
        CFE_ES_PerfLogEntry(SAMPLE_APP_2_APP_PERF_ID);

        if (status == CFE_SUCCESS)
        {
            SAMPLE_APP_2_ProcessCommandPacket();
        }

    }

    CFE_ES_ExitApp(RunStatus);

} /* End of SAMPLE_APP_2_AppMain() */
