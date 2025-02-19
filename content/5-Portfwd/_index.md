---
title : "Loading Data from S3 to Snowflake"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

{{% notice tip %}}  
This section requires a Snowflake account, so make sure you have one.  
{{% /notice %}}  

In the previous section, we had stock data stored as daily `.csv` files in an **S3 Bucket**. Now, we will upload it to **Snowflake** for easier visualization, usage, and management.  

### Create an IAM Role to allow Snowflake access to S3  

**1.** In **AWS Management Console**, search for the [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) service and select it.  

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.1.png)  

**2.** At **Step 01**  

- **Trusted entity type**: **AWS account**  
- **An AWS account**: **This account**  
- **Next**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/1.png)  

**3.** At **Step 02**  

- Grant this role the **AmazonS3FullAccess** permission  
- **Next**  

**4.** At **Step 03**  

- **Role name**: ``` snowflake-stock-prices ```  
- Review the details  
- **Create role**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/2.png)  

{{% notice tip %}}  
Remember to save the ARN of this role for the next step.  
{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/23.png)  

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

- Click **Update Policy**

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

**Pipe** in Snowflake is a mechanism that enables continuous data loading from an External Stage (S3) into a table in Snowflake. It utilizes **Snowpipe**, a Snowflake service that automatically detects new files in cloud storage (e.g., S3) and loads the data into the table without requiring manual execution of the `COPY INTO` command.  

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
- Click **Test** again.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/20.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/21.png)  

**4.** **Results**  

- Execute the command ``` select * from stock_price_data; ``` to check if the data has been loaded from **S3** into **Snowflake**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/22.png)  

**The data from S3 has been successfully added to Snowflake.**  

### Observing Data in Snowflake  

Select **Chart** on the **result** bar in **Snowflake** after running the query:  
```sql
SELECT * FROM stock_price_data;
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/25.png)  

- Here, you can create charts based on the data stored in the table.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/26.png)  

The sections include: **Chart type**, **Data**, and **Appearance**  

#### **1. Chart type**  

{{% notice info %}}  

**Chart type** allows users to select different types of charts to visualize data.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/27.png)  

-- **Line Chart**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/28.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/29.png)  

-- **Bar Chart**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/30.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/31.png)  

-- **Scatter Plot**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/32.png)  

-- **Heatgrid**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/33.png)  

-- **Scorecard**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/34.png)  

#### **2. Data**  

{{% notice info %}}  

**Data** refers to the information stored in a table or retrieved through a query. This serves as the source for chart visualization.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/35.png)  

It allows you to select specific columns, aggregate values (sum, max, min, etc.), remove columns from the chart, or add new ones.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/36.png)  

#### **3. Appearance**  

{{% notice info %}}  

**Appearance** relates to the visual representation of the chart. It does not affect the data but enhances readability and interpretation.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/37.png)  

**Example**: Adding column names and legend to the chart.  

- Before adding:  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/39.png)  

- After adding:  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/38.png)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/40.png)

---

{{% notice info %}}  

Next, we will integrate **EventBridge** to ensure the data is continuously updated in real-time.  

{{% /notice %}} 

### Adding EventBridge (CloudWatch Events) 

**1.** Go back to AWS and select **Lambda**  

- Choose **Function**  
- Select the function **fetch_code**  

**2.** Add an EventBridge (CloudWatch Events) trigger  

- Go to **Configuration** - select **Trigger**  
- Click **Add trigger**  
- **Select a source**: ``` EventBridge CloudWatch Events ```  
- **Rule**: Create a new rule  
- **Rule name**: ``` every_days ```  
- **Schedule expression**: ``` rate(1 day) ```  
- Click **Add**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.6.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.7.png)  

{{% notice note %}}  
Do the same for the remaining Lambda function.  
{{% /notice %}}

{{% notice info %}}  
Once completed, the data will be updated and stored continuously on a daily basis.  
{{% /notice %}}