
![banner](https://user-images.githubusercontent.com/29625147/161611862-9e85fa72-ea16-4800-9799-d7367fa2b3fe.png)

[![GO - README](https://img.shields.io/static/v1?label=GO&message=README&color=2ea44f)](https://github.com/DongilVision/DevOps/blob/main/README.md)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FDongilVision%2FDevOps%2Fblob%2Fmain%2Fdocker.md&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

### 실행명령어
```
docker run --gpus all -it -p 8888:8888 -p 6006:6006 --ipc=host -v $(pwd):/workspace hello:1.0 /bin/bash
docker run --rm -it --user jjy:jjy --name div_user_001 
           -p 8011:8080 -v `pwd`:/content -v /NAS2/USER-001:/content/storage div/uhome:0.1 
```
* --rm : 컨테이너사용종료시 자원을 즉시회수함.
* -it : 터미널 사용
* -v : 디렉토리연결 (외부:내부)
* -p : 포트연결 (외부:내부)
* --user : 사용자지정 
  * 도커내부에서 사용자등록과 그룹등록이 되어야 사용가능
* --name : 컨테이너이름지정
* --ipc=host : 파이토치등을 사용할때, sharedmemory를 이용하여 데이타를 교환하나, 도커내의 자원을 부족하므로 호스트사용
* --gpu all : gpu 사용여부 
  * docker run --gpus '"count=1"' [container_name]  
  * docker run --gpus '"device=0"' [container_name]
  * docker run --gpus '"device=0,1"' [container_name]
  * https://docs.docker.com/compose/gpu-support/ 
  * https://conservatory.tistory.com/12
* --network=host : host 컴퓨터의 네트워크를 사용한다.
```
docker build --network=host -t div/sus:0.1 .
docker run --rm -it --hostname _docker --name div_sus_001 div/sus:0.1 
docker run --rm -it --user jjy:jjy --hostname _docker --name div_user_001 -p 8011:8080 \
       -v `pwd`:/content -v /NAS2/USER-001:/content/storage div/sus:0.1 
docker ps
```
### 일반명령어
* docker ps [-a]
* docker images
  * docker image inspect --format "{{.Name}},{{.Image}}"
* docker attach [contained id]
* docker stop | rm | kill 
* docker -v
* docker rm -f
* docker run --cpu-share=512 --memory=1g
* docker logs [container id]

-----
## 도커작성

### 도커화일 (KST설정)
```
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get install -y net-tools iputils-ping dnsutils
RUN apt-get install -y vim git curl wget sudo 
# RUN apt-get install -y python3.8 python3-pip
# RUN pip3 install flask flask_cors flask_restx
```
### 도커화일 (User:Group)
* su, sudo 가능 확인
```
# --------------------------------------------------------------
# `pwd` 사용할때는 반드시 계정일치 필요
# --------------------------------------------------------------
RUN mkdir /content
RUN chmod 777 /content

RUN addgroup --gid 1001 jjy
RUN useradd -rm -d /home/jjy -s /bin/bash -g 1001 -G sudo -u 1001 jjy
USER jjy
WORKDIR /content
```
```
# --------------------------------------------------------------
# `pwd` 사용할때는 반드시 계정일치 필요
# --------------------------------------------------------------
RUN mkdir /content
RUN chmod 777 /content

RUN echo 'root:1234' | chpasswd
ARG USER
RUN echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}
# Set the arguments for host_id and user_id to be able to save the build artifacts
# outside the container, on host directories, as docker volumes.
ARG host_uid host_gid
RUN groupadd -g $host_gid nxp && \
    useradd -g $host_gid -m -s /bin/bash -u $host_uid $USER
USER $USER
```
### 환경설정
```
sudo usermod -aG docker $USER
visudo
```
* visudo : root 권한부여
* dns 안될경우, 특히 apt-update 않될때.
```
docker build --network=host -t div/uhome:0.1 .  
호스트 쪽의 dns를 사용하도록 한다.  
```

<details>
    <summary>자세히</summary>

원래는 docker conatiner 내에서 nvidia GPU를 사용하기 위해 nvidia-docker 혹은 nvidia-docker2를 따로 설치해줘야했다. 하지만 docker 19.03 버전부터는 docker 자체적으로 nvidia GPU를 지원하고 nvidia-docker는 사용하지 않는다.
* docker run ... --gpus "device=1,2,3" ...
* docker run ... --gpus all ... 
* 

</details>

### Docker 내에서 Docker 제어방법
* 기본적으로 -v /var/run/docker.sock:/var/run/docker.sock 사용
* pip3 install docker
* https://recordsoflife.tistory.com/635
* https://docs.docker.com/engine/api/sdk/examples/
* https://docs.docker.com/engine/api/

```
docker run -it --network=host -v /var/run/docker.sock:/var/run/docker.sock alpine
apk add curl && apk add jq
curl -s --unix-socket /var/run/docker.sock http://dummy/containers/json | jq '.'
curl --unix-socket /var/run/docker.sock http://localhost/events
curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"ubuntu", "Name":"MyJOB"}' -H 'Content-Type: application/json' http://localhost/containers/create
```

# Official Docker docs.

* https://docs.docker.com/get-docker/
* https://docs.docker.com/engine/install/ubuntu/ (Installation for Ubuntu)
* https://docs.docker.com/compose/install/ ( Installation Compose )


---
# DOCKER 설치
* https://docs.docker.com/engine/install/ubuntu/ # 공식설치

apt-get update  
apt-get remove docker docker-engine docker.io containerd runc  
apt-get install -y apt-transport-https ca-certificates curl   gnupg lsb-release  

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
... 중략
apt-get update  
apt-get install docker-ce docker-ce-cli containerd.io  

---
# DOCKER-COMPOSE 설치

@버전확인
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose






## 도커예제

* https://github.com/facebookresearch/detectron2/blob/main/docker/Dockerfile
* 도커구조.
* https://bluese05.tistory.com/53

