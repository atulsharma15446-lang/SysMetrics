import psutil
import time


def get_cpu():
    return psutil.cpu_percent(interval=1)


def get_memory():

    memory = psutil.virtual_memory()

    return {
        "total": memory.total,
        "used": memory.used,
        "available": memory.available,
        "percent": memory.percent
    }


def get_disk():

    disk = psutil.disk_usage("/")

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }


def get_network():

    network = psutil.net_io_counters()

    return {
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv
    }


def get_uptime():

    boot_time = psutil.boot_time()

    return time.time() - boot_time


def collect_metrics():

    return {
        "cpu": get_cpu(),
        "memory": get_memory(),
        "disk": get_disk(),
        "network": get_network(),
        "uptime": get_uptime()
    }
