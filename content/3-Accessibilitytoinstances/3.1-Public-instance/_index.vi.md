---
title : "Tạo bảng trong DynamoDB"
date :  "2024-12-28"
weight : 1 
chapter : false
pre : " <b> 3.1. </b> "
---
### Tạo bảng trong DynamoDB

**1.** Trong AWS Management Console, thực hiện tìm kiếm dịch vụ DynamoDB và chọn.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.1.png)

- Chọn **Create table**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.4.png)

**2.** Thông tin

- **Table name**: điền ```stock-prices``` 
- **Partition key**: ```symbol```
- **Sort key**: ```timestamp```

- Chọn **Create table**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.2.png)

- Bảng được tạo thành công
![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.3.png)

{{%notice tip%}}
Tên của bảng yêu cầu không được trùng.
{{%/notice%}}
