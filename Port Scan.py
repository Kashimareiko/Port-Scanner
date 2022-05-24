import asyncio
from random import SystemRandom

def run(tasks, *, loop=None):
    """Run Tasks"""
    if loop is None:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(asyncio.wait(tasks))

async def scanner(ip, port, loop=None):
    fut = asyncio.open_connection(ip, port, loop=loop)

    try:
        reader, writer = await asyncio.wait_for(fut, timeout=0.5)
        print("{}:{} Connected".format(ip, port))
    except asyncio.TimeoutError:
        pass
    except Exception as exc:
        print('Error Scanning {}:{} {}'.format(ip, port, exc))

def scan(ips, ports, randomize=False):
    """Scanning the ports"""
    loop = asyncio.get_event_loop()
    if randomize:
        rdev = SystemRandom()
        ips = rdev.shuffle(ips)
        ports = rdev.shuffle(ports)

    run([scanner(ip, port) for port in ports for ip in ips])

ips = input("IP Address being scanned: ")
STEP = 256
for r in range(STEP+1, 65535, STEP):
        ports = [str(r) for r in list(range(r-STEP, r))]
scan(ips, ports)


def run(tasks, *, loop=None):
    """Run"""
    if loop is None:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(asyncio.wait(tasks))

async def scanner(ip, port, loop=None):
    fut = asyncio.open_connection(ip, port, loop=loop)

    try:
        reader, writer = await asyncio.wait_for(fut, timeout=0.5)
        print("{}:{} Connected".format(ip, port))
    except asyncio.TimeoutError:
        pass
    except Exception as exc:
        print('Error Scanning {}:{} {}'.format(ip, port, exc))