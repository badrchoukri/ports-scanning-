from scapy.all import * 


SYN_ACK = 0x12
RST_ACK = 0x14


def Syn_scan():
    
    ports = []
    host = input("host that you want to scan : ")
        
    while True :
        x = input("ports to scan (entre stop if you finished): ")

        if x.lower() == 'stop':
            break
        
        try:
            port = int(x)
            if 0 < port <= 65535 :
                ports.append(port)
            else : 
                print("-------------port must be 0 < port <= 65535-------------")
        except ValueError :
            print("Invalid port number.")


    ans, uans = sr(IP(dst=host)/TCP(sport=5555 ,dport=ports , flags="S"),timeout=2,verbose=0 )


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"open ports in {host} : ")
    for (s_ans,r_ans) in ans:
        if s_ans[TCP].dport == r_ans[TCP].sport :
            if r_ans[TCP].flags == SYN_ACK:
                print(f"the port {s_ans[TCP].dport} is open.")

        
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"close ports in {host} :")
        if r_ans[TCP].flags == RST_ACK:
            print(f"port {s_ans[TCP].dport} is closed.")

    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"filtred ports in {host}: ")
    for s_uans in uans:
        if send:
            print(f"port {s_uans[TCP].dport} is filtred.")


Syn_scan()


