# webmaill-logging-tool
Python tools to create user email logs from webmail for Malicious Email Logging and Forensics.

The scripts uses two windows sys internal utilities.

1.procdump

2.strings

The tool creates a dump file as the user closes the browser and creates the new email logs from the corresponding memoery dump file.

The code also produces the performance test reports of the functions using memory_profiler.

