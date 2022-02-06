"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import call
import platform


def host_ping(iplist: list):
    result = dict()

    for ip in iplist:
        COMMAND = f'ping -n 4 {ip}' if platform.system().lower() == 'windows' else f'ping -c 4 {ip}'
        result_code = call(COMMAND)
        result[str(ip)] = "Узел недоступен" if result_code else "Узел доступен"

    return result


if __name__ == "__main__":
    start_ip = int(ip_address("8.8.8.8"))
    end_ip = int(ip_address("8.8.8.8") + 2)
    iplist = [ip_address(el) for el in range(start_ip, end_ip + 1)]
    result = host_ping(iplist)
    print(result)
    