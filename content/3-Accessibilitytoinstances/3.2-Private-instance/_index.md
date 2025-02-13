---
title : "Storing Data in DynamoDB"
date :  "2024-12-28"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

## Storing Data into DynamoDB
### Create Lambda Function

**1.** In the AWS Management Console, search for the **Lambda** service and select it.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.1.png)

**2.** Create a function in Lambda

- Click **Create function**
- **Function name**: `fetch_code`
- **Runtime**: Python 3.10
- **Architecture**: x86_64
- Click **Create function**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.2.png)

### Set Up Lambda Function

**1.** Add a **Layer**.

- Navigate to the **Layers** section and click **Add a layer**
- **Layer source**: AWS layers
- **AWS layers**: `AWSSDKPandas-Python310`
- **Version**: 23

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.3.png)

{{%notice tip%}}
Select the latest version in the version section.
{{%/notice%}}

**2.** Adjust timeout.

- Go to the **Configuration** section.
- Under **General configuration**, click **Edit**.
- Set the **Timeout** to 15 seconds.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.5.png)

**3.** Add permissions for the function.

- In the **Configuration** section, select **Permissions** on the left.
- Click on the **role name**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.4.png)

- In the **Permissions** section, find **Permissions policies**.
- Click **Add permissions** - **Attach policies**.
- Add the permission **AmazonDynamoDBFullAccess**.
- Click **Add permissions**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.5.png)

**4.** Insert data from [Alphavantage](https://www.alphavantage.co/) into the table created in **DynamoDB**.

- Go to the **Code** section in the options bar.
- Add the [SourceCode](https://vuthibichngoc.github.io/workshop_awsfcj_2024/file/fetch_code.py) in the **Code source** area.
- Click **Test** - **Create new test event**, enter the necessary information, and click **Save**.
- Execute the code.
- **Result after execution**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.6.png)

### Result in DynamoDB.

- Go to [DynamoDB](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#service).
- Select **Tables** in the left-hand options bar - Click the table you created earlier.
- In the table, click **Explore table items** - Click the **Run** button.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.7.png)

- The data has been fetched from [Alphavantage](https://www.alphavantage.co/) and stored in the **stock_prices** table created earlier in **DynamoDB**.