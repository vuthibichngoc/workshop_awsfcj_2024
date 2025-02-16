---
title : "Thêm EventBridge (CloudWatch Events)"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Thêm EventBridge (CloudWatch Events)

**1.** Hãy trở lại AWS và chọn Lambda.

- Chọn **Function**.
- Chọn function **fetch_code**

**2.** Thêm trigger EventBridge (CloudWatch Events)

- Tới **Configuration** - chọn **Trigger**
- Chọn **Add trigger**
- **Select a source**: ``` EventBridge CloudWatch Events ``
- **Rule**: Create a new rule.
- **Rulename**: ``` every_days ```
- **Schedule expression**: ``` rate(1 day) ```
- **Add**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.6.png)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.7.png)

{{% notice info %}}
Hoàn thành xong, dữ liệu sẽ được cập nhật và đưa vào DynamoDB, S3 và Snowflake một cách liên tục theo từng ngày. Mỗi ngày, có thể kiểm tra các thông tin chứng khoán đã được cập nhật thêm theo ngày.
{{% /notice %}}