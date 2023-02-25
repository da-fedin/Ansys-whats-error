import psutil

PROCNAME = "AnsysFWW.exe"

for my_process in psutil.process_iter():
    if my_process.name() == PROCNAME:
        print(my_process)
        print("Name:", my_process.name())
        print("PID:", my_process.pid)
        print("Executable:", my_process.exe())
        print("CPU%:", my_process.cpu_percent(interval=1))
        print("MEM%:", my_process.memory_percent())
        print("MEM%:", my_process.memory_full_info())