import os
import sys
 
path = '/home/ssg/ssg/'    // 프로젝트의 루트 
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ssg.settings'  // 프로젝트 이름.settings

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

