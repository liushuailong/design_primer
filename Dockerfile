FROM ubuntu:20.04
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip
#MySQL-Python必须得先安装这个库
RUN mkdir /slliu
#设置工作目录
WORKDIR /slliu
#将当前目录加入到工作目录中
ADD . /slliu
#install any needed pacakges in requirements.txt，你要把所有需要安装的Python模块加到这文件中。
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /slliu/requirements.txt
#对外暴露端口
EXPOSE 80 8000
#设置环境变量
ENV SPIDER=/slliu