# Self-Study Discussion 24.1
# Thinking Like a Data Scientist: Handling Big Data with Mosquitto, ThingsBoard, and Kafka

One resource that helped me significantly throughout this module was the official **Apache Kafka Documentation**.

**Resource:**
https://kafka.apache.org/documentation/

Kafka was one of the more complex technologies introduced in the module because it requires understanding producers, consumers, topics, brokers, partitions, and event-streaming architectures. The Kafka documentation helped me understand how data moves through a producer-consumer pipeline and how topics are used to organize streaming data. This resource was especially useful while working on Project 24.2, where I built a Kafka producer that published vehicle coordinate data and a Node.js consumer that processed those messages.

Another valuable resource was the **ThingsBoard Documentation**.

**Resource:**
https://thingsboard.io/docs/

This documentation helped me understand Rule Chains, Root Rule Chains, REST API nodes, and alarm processing. During Projects 24.1 Parts 1 and 2, I used the documentation along with troubleshooting logs to better understand how telemetry and alarm data flow through ThingsBoard into Firebase.

One practical tip I would share is to become comfortable reading logs and error messages. During this module I encountered SSL certificate trust issues between ThingsBoard and Firebase as well as Kafka client compatibility issues in Node.js. Carefully reading the error messages ultimately led me to the correct solutions. Debugging skills are often just as important as coding skills in real-world data engineering projects.

These resources helped me better understand streaming architectures and will remain useful references for future IoT, telemetry, and event-streaming projects.