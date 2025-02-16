---
title : "Create IAM Role"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

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


{{% notice note %}}
The next step will be to move the data from **S3** to **Snowflake**.
{{% /notice %}}