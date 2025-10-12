import socket 

with open('targets.txt', 'r') as hosts: 
    for host in hosts: 
        ip, port = host.strip().split(':') 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print (f'Attempting to connect to {ip} on port {port}...') 
        
        try: 
            s.connect((ip, int(port))) 
            print(f'{ip} on port {port} is available ✅') 
        except socket.error as error: 
            print(f'{ip} on port {port} failed: {error} ❌') 
        
        finally: s.close()
