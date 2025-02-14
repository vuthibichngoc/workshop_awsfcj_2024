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

In the previous section, we stored stock data as `.csv` files by date in an **S3 Bucket**. Now, we will load it into **Snowflake** for easier visualization, usage, and management.  

### Create a Database in Snowflake  

**1.** Go to [Snowflake](https://app.snowflake.com/)  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.8.png)

- Log in with your existing account.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.7.png)

**2.** Select **Create** → **SQL worksheets**  

- Run the following commands:  

```sql
CREATE DATABASE FCJ_STOCK_PRICES;
```

```sql
USE DATABASE FCJ_STOCK_PRICES;
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.1.png)  

- The **Database** is successfully created.  

**3.** Create a **Stage** in **Snowflake**  

```sql
CREATE STAGE my_stage
  URL = 's3://data-stock-prices-01/snowflake/'
  CREDENTIALS = (AWS_KEY_ID = '<<your aws key id>>' AWS_SECRET_KEY = 'your aws secret key'); 
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.2.png)  

{{% notice tip %}}  
For this step, go back to AWS with an admin account and retrieve the `AWS_KEY_ID` and `AWS_SECRET_KEY` associated with the AWS account storing the **S3 Bucket** created in the previous step.  
{{% /notice %}}  

To obtain these credentials, navigate to IAM: Select **Users** → Go to **Security credentials** → Under **Access keys**, you will find your **AWS_KEY_ID** and **AWS_SECRET_KEY**. (Alternatively, you can create a new access key and use the newly generated credentials for the above command.)  

**4.** Create the ```stock_prices``` table in **Snowflake**

- Run the following SQL command:  

```sql
CREATE OR REPLACE TABLE stock_prices(
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

- The **stock_prices** table is successfully created in **Snowflake**.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.3.png)  

**5.** Load data into the table  

- Run the following command:  

```sql
COPY INTO stock_prices
FROM @my_stage
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1)  
ON_ERROR = 'SKIP_FILE';  
```

- Data loading is successful.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.4.png)  

- Use the command ```SELECT * FROM stock_prices;``` to verify the data.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.9.png)

- The data has been successfully loaded into the table.  

Next, we will configure **EventBridge** to continuously update data in **S3 Bucket** in real time.  

### Add EventBridge (CloudWatch Events)  

**1.** Go back to AWS and select Lambda.  

- Click on **Functions**.  
- Select the function **fetch_code**.  

**2.** Add an EventBridge (CloudWatch Events) trigger  

- Go to **Configuration** → **Trigger**  
- Click **Add trigger**  
- **Select a source**: ```EventBridge CloudWatch Events```
- **Rule**: Create a new rule  
- **Rule name**: ```every_days``` 
- **Schedule expression**: ```rate(1 day)```  
- Click **Add**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.6.png)  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.7.png)  

{{% notice tip %}}  
With this setup, data will be continuously updated and inserted into **DynamoDB** and **S3** on a daily basis.  
{{% /notice %}}  

