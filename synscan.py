from scapy.all import sr1, IP, TCP

try:
    ip = IP(dst='192.168.1.100')
    tcp = TCP(dport=80, flags='S')
    ret = sr1(ip/tcp, timeout=1, verbose=0)

    print('snd: {0:#010b} ({1})'.format(bytes(tcp)[13], tcp.flags))
    print('rtn: {0:#010b} ({1})'.format(bytes(ret['TCP'])[13], ret['TCP'].flags))

except Exception as e:
    print('Exception: {0}'.format(e))