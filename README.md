## 项目简介
consul作为服务注册和健康检查，实现的微服务架构示例。  
本项目基于 python+flash，提供了 RESTful 的 API 接口，并自动注册自身至consul。

## 附录
#### 启动consul
```
docker run -d -p 8300:8300 -p 8400:8400 -p 8500:8500 -p 8600:8600 -e 'CONSUL_LOCAL_CONFIG={"skip_leave_on_interrupt": true}' --name=node0 consul:0.7.5 agent -server -client=0.0.0.0 -node=node0 -bootstrap-expect=1 -bind=127.0.0.1 -data-dir=/tmp/consul -ui
```

#### swarm mode 运行
```
docker -H 192.168.85.102:2375 service create --with-registry-auth  --name microservice-py reg.dolplay.com/data-group/microservice-sample:latest
```
