FROM tensorflow/tensorflow:1.6.0-devel-gpu-py3
COPY ./home/ /home/
ENV JAVA_HOME=/usr/java/jdk1.8.0_161 \
JRE_HOME=/usr/java/jdk1.8.0_161/jre \
ANT_HOME=/usr/ant/apache-ant-1.9.14 \
JOERN_HOME=/home/SySeVR/joern-0.3.1 \
PATH="$PATH:/usr/java/jdk1.8.0_161/bin:/usr/ant/apache-ant-1.9.14/bin:/home/SySeVR/joern-0.3.1"
RUN mkdir /usr/java \
&& cp -r /home/SySeVR/softdir/jdk1.8.0_161 /usr/java \
&& chmod +x /usr/java/jdk1.8.0_161/bin/java \
&& mkdir /usr/ant \
&& cp -r /home/SySeVR/softdir/apache-ant-1.9.14 /usr/ant \
&& chmod +x /usr/ant/apache-ant-1.9.14/bin/ant \
# && rm -rf /etc/apt/sources.list \
# && cp -r /home/SySeVR/softdir/sources.list /etc/apt/ \
# && rm -rf /etc/apt/sources.list.d \
&& apt-get clean \
&& apt-get update --fix-missing \
# && rm -rf /etc/profile \
# && cp -r /home/SySeVR/softdir/profile /etc \
# && cd /home/SySeVR/softdir \
# && chmod +x env.sh \
# && ./env.sh \
&& cd /home/SySeVR/joern-0.3.1 \
&& /usr/ant/apache-ant-1.9.14/bin/ant \
&& apt-get install -y python-setuptools \
&& apt-get install -y python-dev \
&& apt-get install -y python-pip \
&& apt-get install -y lsof \
&& cd /home/SySeVR/softdir/py2neo-py2neo-2.0 \
&& python2 setup.py install \
&& cd /home/SySeVR/softdir/fabsx00-py2neo-gremlin-c94d290 \
&& python2 setup.py install \
&& cd /home/SySeVR/softdir/python-joern-0.3.1 \
&& python2 setup.py install \
&& apt-get clean \
&& apt-get update --fix-missing \
&& apt-get install -y graphviz \
&& apt-get install -y libgraphviz-dev \
&& apt-get install -y pkg-config \
&& apt-get install -y python-igraph \
&& apt-get install -y python-virtualenv \
&& pip3 install xlrd \
&& pip3 install gensim==3.4 \
&& pip3 install pyyaml \
&& chmod +x /home/SySeVR/joern-0.3.1/joern \
&& chmod +x /home/SySeVR/neo4j/bin/neo4j
# && rm -rf /home/SySeVR/softdir   
