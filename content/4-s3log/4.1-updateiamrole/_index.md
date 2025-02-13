---
title : "Create S3 Bucket"
date :  "2024-12-28"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

## Create S3 Bucket

**1.** In the AWS Management Console, search for the **S3** service and select it.

![IAM1](/images/4.s3/4.1.1.png)

**2.** Create an S3 Bucket

- Select **Create bucket**
- In the **Bucket name** field, enter ``` data-stock-prices-01 ```
- Leave the other options at their default settings.
- Click **Create bucket**
- The bucket will be created successfully.

![IAM1](/images/4.s3/4.1.2.png)

**3.** Add a folder to store data.

- Under **Objects**, click **Create folder**
- **Folder name**: ``` snowflake ```
- Click **Create folder**

![IAM1](/images/4.s3/4.1.3.png)

- The folder is created successfully.

![IAM1](/images/4.s3/4.1.4.png)

{{%notice tip%}} 
The name of the S3 bucket must be unique. If the name already exists, try adding a letter or number at the end.
{{%/notice%}}