/*
 * CFS Mission Model
 * Author: Pranav Srinivas Kumar
 * Date: 2015.12.14
 */

grammar CFS_Mission;

/*
 * This is the start of the cFE Mission Model
 */
start
    :
        (application)*
        EOF
    ;

/*
 * cFE Application
 */
application
    :
        'application' (' ')* app_name (' ')*
         (' ')* '{' (' ')*
        ( perf_ids )*     // Performance ID's
        ( msg_ids )*     // Message ID's        
        ( event_ids )*     // Event ID's
        ( command_codes )* // Packet Command Codes
        ( msg )*          // Message Types
        ( versions )*      // Version Number
        '}'
    ;

// Name of Application
app_name
    :
        ID
    ;

// Performance IDs
perf_ids
    :
         (' ')* 'perfIDs' (' ')*
         (' ')* '{'  (' ')*
        ( perf_id )+
         (' ')* '}'  (' ')*
    ;

perf_id
    :
        ( (' ')* perf_id_name  (' ')* '='  (' ')* perf_value  (' ')* ';'  (' ')*)
    ;

perf_id_name
    :
        ID
    ;

perf_value
    :
        ID
    ;

// Message IDs
msg_ids
    :
         (' ')* 'msgIDs'  (' ')*
         (' ')* '{'  (' ')*
        ( msg_id )+
         (' ')* '}' (' ')*
    ;

msg_id
    :
        ( (' ')* msg_id_name (' ')* '=' (' ')* msg_value (' ')* ';' (' ')*)
    ;

msg_id_name
    :
        ID
    ;

msg_value
    :
        ID
    ;


// Event IDs
event_ids
    :
         (' ')* 'eventIDs' (' ')*
         (' ')* '{' (' ')*
        ( event_id )+
         (' ')* '}' (' ')*
    ;

event_id
    :
        ( (' ')* id_name (' ')* '=' (' ')* id_value (' ')* ';' (' ')*)
    ;   

// Event ID Name
id_name
    :
        ID
    ;

// Event ID Value
id_value
    :
        ID
    ;

// Packet Command Codes
command_codes
    :
         (' ')* 'commandCodes' (' ')*
         (' ')* '{' (' ')*
        ( command_code )+
         (' ')* '}' (' ')*
    ;

command_code
    :
         (  (' ')* cmd_name  (' ')* '='  (' ')* cmd_value  (' ')* ';'  (' ')* )
    ;

// Command Code Name
cmd_name
    :
        ID
    ;

// Command Code Value
cmd_value
    :
        ID
    ;

// Application Data Structures
msg
    :
         (' ')* msgtype (' ')* 'msg'  (' ')* msgname  (' ')*
         (' ')* '{'  (' ')*
        ( field )+
         (' ')* '}' (' ')*
    ;

// Data structure type
msgtype
    :
        ('table' | 'critical' | 'command' | 'housekeeping' | 'global')
    ;

msgname
    :
        (ID ((' ')* ID)* )
    ;

// Message Fields
field
    :
        ( (' ')* datatype (' ')* fieldname  (' ')* ';'  (' ')* )
    ;

// Datatype of Message
datatype
    :
        ID
    ;

fieldname
    :
        ID
    ;

// Version
versions
    :
         (' ')* 'version' (' ')*
         (' ')* '{' (' ')*
        ( version )+
         (' ')* '}'  (' ')*
    ;

version
    :
        (  (' ')* version_name  (' ')* '='  (' ')* version_value  (' ')* ';'  (' ')*)
    ;

// Version Name
version_name
    :
        ID
    ;

// Value of event or command code
version_value
    :
        ID
    ;

/* An ID - One or more alphanumeric characters
 * that must start with either an alphabet/underscore
 */
ID
    :   
        ('a'..'z' | 'A'..'Z' | '0'..'9' | '_' | '.')
        ('a'..'z' | 'A'..'Z' | '0'..'9' | '_' | '.' | '[' | ']' )*
    ;

// A digit - any number between 0 and 9
fragment DIGIT
    :   
        '0'..'9'
    ;

// An integer - one or more digits
INT
    :   
        DIGIT+
    ;

// A double-precision floating point number
DOUBLE
    :   
        (DIGIT)+ '.' (DIGIT)*
    ;

// White spaces and escape codes are ignored
WS
    :   
        ( (' ')*
        | '\t'
        | '\r'
        | '\n'
        ) -> channel(HIDDEN)
    ;

// Paragraph comments are ignored
COMMENT
    :   
        '/*' .*? '*/' -> skip
    ;

// Line comments are ignored
LINE_COMMENT
    :   
        '//' ~[\r\n]* -> skip
    ;
