---
title : "Building a Stock Data Processing and Storage System using AWS Lambda, DynamoDB, S3, and Snowflake"
date :  "2024-12-28"
weight : 1 
chapter : false
---
# Building a Stock Data Processing and Storage System using AWS Lambda, DynamoDB, S3, and Snowflake

### Overall
 This project builds an automated stock data processing and storage system using AWS services and Snowflake. It retrieves Microsoft stock prices via an API using AWS Lambda and stores the data in Amazon DynamoDB. Another Lambda function processes and converts the data into CSV files, which are then stored in Amazon S3. Finally, the data is loaded into Snowflake for further analysis and reporting. This system leverages AWS Lambda, DynamoDB, S3, and CloudWatch Events to ensure efficient data collection, transformation, and storage. 

### Content
 1. [Introduction ](1-introduce/)
 2. [Preparation](2-prerequiste/)
 3. [Collecting and Storing Data in DynamoDB](3-accessibilitytoinstances/)
 4. [Transforming and Storing Data as CSV in S3](4-s3log/)
 5. [Loading Data from S3 to Snowflake](5-Portfwd/)
 6. [Clean up resources](6-cleanup/)
