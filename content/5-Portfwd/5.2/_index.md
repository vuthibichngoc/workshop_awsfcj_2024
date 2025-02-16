---
title : "Upload data to Snowflake"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Create a Database in Snowflake  

**1.** Go to [Snowflake](https://app.snowflake.com/)  

- Log in with the created account.  

**2.** Select **Create** - **SQL worksheets**  

- Run the following commands:  

``` CREATE DATABASE STOCK_PRICES; ```  

``` USE DATABASE STOCK_PRICES; ```  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/3.png)  

- **Database created successfully.**  

**3.** Create the **stock_prices_data** table in **Snowflake** and load data into it.  

**a.** Create the stock data table.  

```
CREATE OR REPLACE TABLE stock_prices_data(
    low          VARCHAR(128),  
    symbol       VARCHAR(128),
    timestamp    VARCHAR(128),
    open         VARCHAR(128),
    volume       VARCHAR(128),
    high         VARCHAR(128),
    close        VARCHAR(128),
    date         VARCHAR(128)
);
```  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/4.png)  

- **Table created successfully in Snowflake.**  

**b.** Create an **Integration Object** to connect with S3.  

{{% notice info %}}  

An **Integration Object** in Snowflake is an external connection object that allows Snowflake to communicate with other services such as S3.  

{{% /notice %}}  

Run the following command to create an **Integration Object** to connect with S3.  

```

create or replace storage integration s3_int
  type = external_stage
  storage_provider = s3
  enabled = true
  storage_aws_role_arn = '<<Your role ARN>>'
  storage_allowed_locations = ('s3://data-stock-prices-01/snowflake/');

```

{{% notice tip %}}  
Enter the ARN of the IAM Role created in the previous step to allow Snowflake to access S3, and modify the S3 path to match your bucket name.  
{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.png)  

**c.** Check detailed information about **Storage Integration**.  

{{% notice info %}}  

**Storage Integration** is an object in Snowflake used to securely and automatically connect with external storage services like AWS S3. Instead of providing an access key and secret key to access S3, Snowflake allows the use of AWS IAM Roles to grant access securely.  

{{% /notice %}}  

Run the command:  
``` DESC INTEGRATION s3_int; ```  
to check detailed information about **Storage Integration**.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/6.png)  

{{% notice note %}}  

Save the **property_value** of the following **properties**: **STORAGE_AWS_IAM_USER_ARN**, **STORAGE_AWS_ROLE_ARN**, **STORAGE_AWS_EXTERNAL_ID**  

{{% /notice %}}  

- Go back to [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) - select **Roles** - choose the role created in the previous step.  
- Select **Trust relationship** - **Edit trust policy**  
- Enter the **property_value** of **STORAGE_AWS_ROLE_ARN** saved earlier after **"AWS"**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/7.png)  

Then, continue by selecting **Add condition**  
- Fill in the following information:  

-- **Condition key**: ``` sts:ExternalId ```  

-- **Qualifier**: ``` Default ```  

-- **Operator**: ``` StringEquals ```  

-- **Value**: Enter the **property_value** of **STORAGE_AWS_EXTERNAL_ID** saved earlier.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/8.png)  

- **Add condition**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/9.png)  

**d.** Create **File Format** to read CSV files  

Run the following command:  

```
create or replace file format csv_format
                    type = csv
                    field_delimiter = ','
                    skip_header = 1
                    null_if = ('NULL', 'null')
                    empty_field_as_null = true;
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/10.png)  

**e.** Create **External Stage** to connect with **S3**  

{{% notice info %}}  

**External Stage** is an external storage repository used by Snowflake to retrieve data from cloud storage services like Amazon S3, Google Cloud Storage, or Azure Blob Storage. It allows Snowflake to read and write data directly from/to external storage without needing to load data into Snowflake first.  

{{% /notice %}}  

Run the following command to create an **External Stage** to connect with the **S3** bucket created earlier.  

```
create or replace stage ext_csv_stage
  URL = 's3://data-stock-prices-01/snowflake/'
  STORAGE_INTEGRATION = s3_int
  file_format = csv_format;
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/11.png)  

**f.** Create **Pipe** to automatically load data  

{{% notice info %}}  

A **Pipe** in Snowflake is a mechanism to automate data loading from an External Stage (S3) into a table in Snowflake. It uses Snowpipe, a Snowflake service that automatically detects new files in cloud storage (e.g., S3) and loads data into the table immediately without requiring a manual `COPY INTO` command.  

{{% /notice %}}  

- Go back to [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) - **Roles** - select the role created in the previous step.  
- Select **Trust relationship** - **Edit trust policy**  
- Modify the content and enter the **property_value** of **STORAGE_AWS_IAM_USER_ARN** saved earlier after **"AWS"**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/13.png)  

Run the following command.

```
create or replace pipe mypipe auto_ingest=true as
copy into stock_price_data
from @ext_csv_stage
on_error = CONTINUE;

```

**g.** Execute the command ``` show pipes ``` to check **pipe**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/15.png)  

{{% notice note %}}  

Please save the information displayed in the **notification_channel** column.  

{{% /notice %}}  

- Go back to [S3](https://us-east-1.console.aws.amazon.com/s3/home?region=us-east-1)  
- Select the **bucket** used to store data that will be uploaded to **Snowflake**  
- Navigate to **Event notifications**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/16.png)  

- Click **Create event notification**  
- In **General configuration**  

-- **Event name**: ``` stock-price-event ```  

- In **Event types**  

-- Select **All object create events**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/17.png)  

- In **Destination**  

-- **Destination**: **SQS queue**  

-- **SQS queue**: enter the **notification_channel** information that was saved earlier.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/18.png)  

- **Save changes**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/19.png)  

**Event notification** has been successfully created.  

- Go back to [**Lambda**](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/discover?tab=code)  
- Select **Function**  
- Select the first function created to insert data into **DynamoDB** (in this case, the function is named **fetch_code**)  
- Navigate to **Code**  
- Select the **Test event** that was used before - choose **Edit test event** - then select **Invoke**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/20.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/21.png)  

**4.** **Results**  

- Execute the command ``` select * from stock_price_data; ``` to check if the data has been loaded from **S3** into **Snowflake**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/22.png)  

**The data from S3 has been successfully added to Snowflake.**  

{{% notice tip %}}

In the next step, we will use **Chart** in **Snowflake** to create data charts on Snowflake to help viewers easily analyze and evaluate data.

{{% /notice %}}