### clash代理（访问外网，拉取东西）

```
git clone https://gitee.com/pc-dev/clash-for-linux.git

进入clash-for-linux文件夹下启动代理软件（机场链接已经配置好）
./onestep.sh

配置环境（只对当前窗口有效）
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

```



### install go（go环境）

```
下载 go sdk
wget https://dl.google.com/go/go1.21.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.3.linux-amd64.tar.gz
sudo ln -s /usr/local/go/bin/* /usr/bin/
```

```
往bashrc文件末尾加入系统环境变量配置命令，以便每次启动系统时自动配置
sudo vim ~/.bashrc
// add
export GOPATH="$HOME/go"
export PATH="$PATH:/usr/local/go/bin:$GOPATH/bin"

生效文件
source ~/.bashrc

go环境变量添加
go env -w GOPROXY=https://goproxy.cn,direct
```



### install docker and docker-compose

安装[参考](https://cloud.tencent.com/document/product/213/46000#C_XgAwZpjht292j2EOU2t)，具体操作如下

```
# 添加docker软件源
sudo apt-get update
sudo apt-get -y install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL https://mirrors.cloud.tencent.com/docker-ce/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://mirrors.cloud.tencent.com/docker-ce/linux/ubuntu/ \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

# 安装docker和docker-compose
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 查看安装情况
docker info

# 查看运行情况（一般安装完就在运行了，没运行就systemctl start docker）
systemctl status docker
```



允许普通用户使用docker

```
// 创建docker用户组
sudo groupadd docker
// 将用户添加进入用户组
sudo usermod -aG docker $USER
// 更新激活组权限
newgrp docker

```



docker proxy（允许docker走代理）

```
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo vim /etc/systemd/system/docker.service.d/proxy.conf

// add into proxy.conf
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7890"
Environment="HTTPS_PROXY=http://127.0.0.1:7890"
Environment="NO_PROXY=localhost,127.0.0.1"

// 重启docker
sudo systemctl daemon-reload
sudo systemctl restart docker

```





### 拉取实验镜像

```
# 事先已经将fabric和PC-Fabric需要的镜像生成并上传到了个人镜像仓库里了，如果没有需要自己通过源代码生成镜像
# 下载镜像
sudo docker login --username=0530suyb registry.cn-beijing.aliyuncs.com
sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-orderer:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-orderer:latest hyperledger/fabric-orderer:latest

sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-peer:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-peer:latest hyperledger/fabric-peer:latest

sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-tools:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-tools:latest hyperledger/fabric-tools:latest

sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-orderer-pc:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-orderer-pc:latest hyperledger/fabric-orderer-pc:latest

sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-peer-pc:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-peer-pc:latest hyperledger/fabric-peer-pc:latest

sudo docker pull registry.cn-beijing.aliyuncs.com/0530suyb/fabric-tools-pc:latest
sudo docker tag registry.cn-beijing.aliyuncs.com/0530suyb/fabric-tools-pc:latest hyperledger/fabric-tools-pc:latest

```



### caliper

```
# 安装指定版本node和npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

source ~/.bashrc

nvm install 20.15.1
nvm use 20.15.1
node -v
npm -v

```



```
# 从仓库拉取测试的caliper工程
git clone https://gitee.com/pc-dev/caliper_all.git

# 进入caliper_all目录，绑定fabric的测试框架
# 正常caliper测试需要安装caliper-cli，不过提前都安装好了，都在caliper_all内。
# 如果运行下面的安装指令，会覆盖掉自己加入的dp-chain测试框架，因此不要运行。
# npm install --only=prod @hyperledger/caliper-cli@0.5.0
npx caliper bind --caliper-bind-sut fabric:2.2

# 测试pc-ledger时（也是dp-chain，也是pc-p3-chain），要换绑PC-ledger的测试框架
npx caliper bind --caliper-bind-sut dp-chain

// 接下来就可以用caliper测试了
```



### git clone

```
# 把fabric和pc-fabric的测试网络部署文件夹拉取
git clone https://gitee.com/pc-dev/fabric-testing.git
git clone https://gitee.com/pc-dev/fabric-testing-pc.git

# pc-ledger源码
git clone https://gitee.com/pc-dev/pc-p3-chain.git
```



### scp传输文件

```
scp -r file root@IP:/file/path
```



### test-network各组织配置多peer节点

1. 组织organizations/ccp-generate.sh和organizations/cryptogen内yaml配置文件修改，以生成更多节点证书
2. docker/docker-compose-test-net.yaml添加新增peer节点的容器信息
3. 修改scripts下脚本的内容

