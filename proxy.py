from pywinauto import application, Desktop
import subprocess

# subprocess.run('inetcpl.cpl', shell=True)
# dlg = Desktop(backend='uia').inetcpl
# dlg.wait('visible')
from pywinauto import application
app = application.Application()
app.start("inetcpl.cpl")