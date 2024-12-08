import time
import os
import psutil

# 获取所有进程信息
for proc in psutil.process_iter(['pid', 'name', 'status']):
    if 'python' in proc.info['name']:  # 筛选出Python进程
        if proc.info['status'] == psutil.STATUS_RUNNING:
            print(f"PID: {proc.pid}, Name: {proc.info['name']}, Status: Running")
        elif proc.info['status'] == psutil.STATUS_SLEEPING:
            print(f"PID: {proc.pid}, Name: {proc.info['name']}, Status: Sleeping")
        else:
            print(f"PID: {proc.pid}, Name: {proc.info['name']}, Status: {proc.info['status']}")

max_memory_usage = 0
max_memory_pid = None

max_running_time = 0
max_running_time_pid = None

# 获取所有进程信息
for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'create_time']):
    if 'python' in proc.info['name']:  # 筛选出Python进程
        memory_usage = proc.info['memory_info'].rss
        running_time = psutil.Process(proc.pid).create_time()

        # 查找内存占用最大的Python进程
        if memory_usage > max_memory_usage:
            max_memory_usage = memory_usage
            max_memory_pid = proc.pid

        # 查找运行时间最长的Python进程
        if running_time > max_running_time:
            max_running_time = running_time
            max_running_time_pid = proc.pid

if max_memory_pid:
    print(f"内存占用最大的Python进程PID: {max_memory_pid}, 内存占用: {max_memory_usage} bytes")
else:
    print("未找到正在运行的Python进程")

if max_running_time_pid:
    print(f"运行时间最长的Python进程PID: {max_running_time_pid}, 运行时间: {max_running_time} seconds")
else:
    print("未找到正在运行的Python进程")

# 获取当前Python文件的PID
current_pid = os.getpid()
print("当前Python文件的PID是:", current_pid)

print(f"当前被检测Python文件的PID: {max_memory_pid}")
# 检查是否还在运行
while True:
    try:
        process = psutil.Process(max_memory_pid)
        if process.is_running():
            print("Python文件还在运行")
        else:
            print("Python文件已经完成运行")
            break
    except psutil.NoSuchProcess:
        print("Python文件已经完成运行")
        break
    time.sleep(30)
