---
title : "Tạo IAM Role"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Tạo IAM Role cho phép Snowflake truy cập vào S3

**1.** Trong **AWS Management Console**, thực hiện tìm kiếm dịch vụ [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) và chọn.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.1.png)

**2.** Tại **Step 01** 

- **Trusted entity type**: **AWS account**
- **An AWS account**: **This account**
- **Next**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/1.png)

**3.** Tại **Step 02**

- Cấp cho role này quyền **AmazonS3FullAccess**
- **Next**

**4.** Tại **Step 03**

- **Role name**: ``` snowflake-stock-prices ```
- Kiểm tra lại các thông tin
- **Create role**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/2.png)

{{% notice tip %}}
Hãy nhớ lưu lại ARN của role này để tiếp tục bước sau.
{{% /notice %}}

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/23.png)


{{% notice note %}}
Bước kế tiếp sẽ thực hiện đưa dữ liệu từ **S3** lên **Snowflake**.
{{% /notice %}}
