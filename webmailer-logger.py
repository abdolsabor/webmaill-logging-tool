import psutil as psutil
import subprocess
import time
import datetime
import datetime
from memory_profiler import profile



browsingprocess = ""
browserppid = ""
prcdump = ""
filein  = "proc_dump.dmp"
fileout = "strfile.txt"
getmail = ""
logs = []



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

@profile
def main():
    
    while (1):
        browserppid = if_process_is_running_by_exename("chrome.exe")
        if browserppid != 0:
            start_time = datetime.datetime.now()
            print("--- Initialize Dumping of {0}".format(browserppid))
            prcdump = "START /B procdump.exe -t -ma -o " + str(browserppid) + " proc_dump.dmp & exit"
            output = subprocess.check_output(prcdump, shell=True)
            print(output)
            print("Dump Complete")
            generatestring()
            with open(fileout) as infile:
                for line in infile:
                    if line.startswith("Mail") and line.endswith("Outlook\n"):
                        print("Email service: Outlook")
                        print(line);
                    if line.startswith("Inbox (") and line.endswith("Gmail\n"):
                        print("Email service: Gmail")
                        print(line);
                        getmail = line.split(" - ")[1];
                        print(getmail)
                    if "\"newMessage\":true" in line:
                        #print("Email service: Outlook")
                        print(line);
                        logs.append(line);
                    if "\"CreateItemJasonRequest:" in line:
                        #print("Email service: Outlook")
                        logs.append(line);
                        print(line);
            infile.close()


            file1 = open("mallogs.txt", "a")
            file1.writelines("\n\nEmail logs of" + getmail + "\n")
            file1.writelines(logs)
            file1.close()
            print("logs updated")
            end_time = datetime.datetime.now()
            print(end_time - start_time)
        else:
            print("NO browser is running")

if __name__ == "__main__":
    
    main()
