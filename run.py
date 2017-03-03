from app import app
import config
import consul
import socket
import random
import string


if __name__ == "__main__":
    c = consul.Consul(host=config.consul_host, port=config.consul_port, token=None,
        scheme='http', consistency='default', dc=None, verify=True)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
    local_ip_address = s.getsockname()[0]
    c.agent.service.register(config.service_name,
        service_id=config.service_name+"-"+''.join([random.choice(string.ascii_letters) for i in range(8)]),
        address=local_ip_address,port=config.port,check=consul.Check.http(url="http://{host}:{port}/health".format(host=local_ip_address,port=config.port),interval='10s'))
    app.run(host='0.0.0.0', port=config.port, debug=False)
