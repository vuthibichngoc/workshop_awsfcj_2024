---
title : "Store Data into S3 Bucket"
date :  "2024-12-28"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

## Save Data to S3 Bucket

### Create Lambda Function

**1.** In the AWS Management Console, search for the **Lambda** service and select it.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.1.png)

**2.** Create a function in Lambda

- Select **Create function**
- **Function name**: ``` DTToSnowflake ```
- **Runtime**: Python 3.10
- **Architecture**: x86_64
- Click **Create function**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.1.png)

### Set Up Lambda Function

**1.** Add a layer.

- Navigate to the **Layers** section and click **Add a layer**
- **Layer source**: AWS layers
- **AWS layers**: ``` AWSSDKPandas-Python310 ```
- **Version**: 23

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.3.png)

{{%notice tip%}} 
Make sure to choose the latest version.
{{%/notice%}}

**2.** Add permissions to the function.

- In the **Configuration** section, select **Permissions** on the left
- Click on the **role name**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.2.png)

- In the **Permissions** section, you should see **Permissions policies**
- Click **Add permissions** → **Attach policies**
- Add the **AmazonDynamoDBFullAccess**, **AmazonS3FullAccess** permissions
- Click **Add permissions**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.3.png)

**4.** Add Trigger.

- In the **Configuration** section, select **Trigger** on the left.
- Click **Add trigger**
- Search for **DynamoDB** and select it.
- **DynamoDB table**: choose the table name created in **DynamoDB** from step 3.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.4.png)

- Click **Add**

**5.** Fetch data from the **stock_prices** table in DynamoDB and save it to the **S3 Bucket** created.

- Go to the **Code** section in the options bar.
- Add the [SourceCode](https://vuthibichngoc.github.io/workshop_awsfcj_2024/file/DTToSnowflake.py) to the **Code source**
- Click **Test** → **Create new test event** → fill in the required details and click **Save**
- Run the code.
- **Result after running**:

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.5.png)

### Results in the S3 Bucket

- Access the [S3 Bucket](https://us-east-1.console.aws.amazon.com/s3/get-started?region=us-east-1&bucketType=general)
- In the left menu, click **General purpose buckets** → Select the previously created table → Navigate to the folder you created.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.6.png)

- Stock data has been processed into .csv files by the respective date and stored in the created **S3 Bucket**.
