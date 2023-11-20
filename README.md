# Real_Time_Emotion_Detection
Real_Time_Emotion_Detection using Apache Kafka

KAFKA SETUP:

1) DOWNLOAD KAFKA 3.6.0 :  https://kafka.apache.org/downloads

2) BREW INSTALL JDK VERSION 8 OR ABOVE
   
brew install --cask adoptopenjdk/openjdk/adoptopenjdk8
export JAVA_HOME=$(/usr/libexec/java_home -v1.8)
Java -version

3) KICKSTART ZOOKEEPER

sh bin/zookeeper-server-start.sh config/zookeeper.properties
(ERROR SOL : rm -rf /tmp/zookeeper/* )

4) KICKSTART KAFKA SERVER
sh bin/kafka-server-start.sh config/server.properties

5) CREATE TOPIC

bin/kafka-topics.sh --create  --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic emotion-detection-stream
sh bin/kafka-topics.sh --list  --bootstrap-server localhost:9092

4) PRODEUCER IN CLI FOR TESTING
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic emotion-detection-stream

5) CONSUMER IN CLI FOR TESTING
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic emotion-detection-stream --partition 0

