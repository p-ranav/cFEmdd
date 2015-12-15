__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

import os, sys, inspect

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, "templates")
# Recursively compile on template files in templates directory
os.system("/usr/local/bin/cheetah compile " + template_dir + "/*.tmpl")
cfs_templates = os.path.realpath(os.path.abspath
                                 (os.path.join
                                  (os.path.split
                                   (inspect.getfile
                                    (inspect.currentframe()
                                 )
                                )[0], "templates")
                              ))
if cfs_templates not in sys.path:
    sys.path.insert(0, cfs_templates)
# From template import *    
from app_version import *
from app_events import *
from app_msg import *
from app_source import *
from app_header import *

class cFE_Application_Generator:
    def generate(self, mission):
        print '--------------------------------------------------'
        print 'Generating cFE Application Template'
        self.mission_home = mission.mission_home
        self.apps_dir = os.path.join(self.mission_home, 'apps')
        for app in mission.apps:
            app_home = os.path.join(self.apps_dir, app.name)
            if not os.path.exists(app_home):
                os.makedirs(app_home)
            app_fsw = os.path.join(app_home, 'fsw')
            app_docs = os.path.join(app_home, 'docs')
            app_tg = os.path.join(app_home, 'test and ground')
            if not os.path.exists(app_fsw):
                os.makedirs(app_fsw)
            if not os.path.exists(app_docs):
                os.makedirs(app_docs)
            if not os.path.exists(app_tg):
                os.makedirs(app_tg)
            fsw_build = os.path.join(app_fsw, 'for_build')
            fsw_src = os.path.join(app_fsw, 'src')
            fsw_tables = os.path.join(app_fsw, 'tables')
            fsw_mission_inc = os.path.join(app_fsw, 'mission_inc')
            fsw_platform_inc = os.path.join(app_fsw, 'platform_inc')
            fsw_ut = os.path.join(app_fsw, 'unit_test')
            if not os.path.exists(fsw_build):
                os.makedirs(fsw_build)
            if not os.path.exists(fsw_src):
                os.makedirs(fsw_src)
            if not os.path.exists(fsw_tables):
                os.makedirs(fsw_tables)
            if not os.path.exists(fsw_mission_inc):
                os.makedirs(fsw_mission_inc)
            if not os.path.exists(fsw_platform_inc):
                os.makedirs(fsw_platform_inc)
            if not os.path.exists(fsw_ut):
                os.makedirs(fsw_ut)

            ###
            ## Generating App Version Header File
            ###
            version_file = app.name + '_version.h'
            version_length = 0
            for key, value in app.version.items():
                if len(key) > version_length:
                    version_length = len(key)
            for key, value in app.version.items():
                space = '    '
                for i in range(0, version_length - len(key)):
                    space += ' '
                app.version[key + space] = app.version[key]
                del app.version[key]
            version_list = []
            for key, value in app.version.items():
                version_list.append(key + value)
            version_namespace = {'application_name' : app.name,
                                 'dollar_id' : '$Id',
                                 'version' : app.version,
                                 'version_list' : version_list}
            t = app_version(searchList=[version_namespace])
            self.version = str(t)
            with open(os.path.join(fsw_src, version_file), 'w') as temp_file:
                temp_file.write(self.version)

            ###
            ## Generating App Events Header File
            ###
            events_file = app.name + '_events.h'
            event_length = 0
            for key, value in app.event_ids.items():
                if len(key) > event_length:
                    event_length = len(key)
            for key, value in app.event_ids.items():
                space = '    '
                for i in range(0, event_length - len(key)):
                    space += ' '
                app.event_ids[key + space] = app.event_ids[key]
                del app.event_ids[key]
            event_ids_list = []
            for key, value in app.event_ids.items():
                event_ids_list.append(key+value)
            event_namespace = {'application_name' : app.name,
                               'event_ids' : app.event_ids,
                               'event_ids_list' : event_ids_list}
            t = app_events(searchList=[event_namespace])
            self.events = str(t)
            with open(os.path.join(fsw_src, events_file), 'w') as temp_file:
                temp_file.write(self.events)

            ###
            ## Generating App Msg Header File
            ###
            msg_file = app.name + '_msg.h'

            # Neatly Format Command Codes
            cmd_length = 0
            for key, value in app.command_codes.items():
                if len(key) > cmd_length:
                    cmd_length = len(key)
            for key, value in app.command_codes.items():
                space = '    '
                for i in range(0, cmd_length - len(key)):
                    space += ' '
                app.command_codes[key + space] = app.command_codes[key]
                del app.command_codes[key]

            for msg in app.messages:
                field_length = 0
                for key, value in msg.fields.items():
                    if len(key) > field_length:
                        field_length = len(key)
                for key, value in msg.fields.items():
                    space = '            '
                    for i in range(0, field_length - len(key)):
                        space += ' '
                    msg.fields[key + space] = msg.fields[key]
                    del msg.fields[key]
            for msg in app.messages:
                for key, value in msg.fields.items():
                    msg.fields_list.append(key + value)
                    
            msg_namespace = {'application_name' : app.name,
                             'command_codes' : app.command_codes,
                             'command_codes_dict' : app.command_codes.items(),
                             'messages': app.messages}
            t = app_msg(searchList=[msg_namespace])
            self.msg = str(t)
            with open(os.path.join(fsw_src, msg_file), 'w') as temp_file:
                temp_file.write(self.msg)
               
            ###
            ## Generating App Source File
            ###
            app_name_caps = app.name.upper()
            c_file = app.name + '.c'
            c_namespace = {'application_name' : app.name,
                           'application_name_caps' : app_name_caps}
            t = app_source(searchList=[c_namespace])
            self.c = str(t)
            with open(os.path.join(fsw_src, c_file), 'w') as temp_file:
                temp_file.write(self.c)

            ###
            ## Generating App Header File
            ###
            h_file = app.name + '.h'
            h_namespace = {'application_name' : app.name,
                           'application_name_caps' : app_name_caps}
            t = app_header(searchList=[h_namespace])
            self.h = str(t)
            with open(os.path.join(fsw_src, h_file), 'w') as temp_file:
                temp_file.write(self.h)
                
