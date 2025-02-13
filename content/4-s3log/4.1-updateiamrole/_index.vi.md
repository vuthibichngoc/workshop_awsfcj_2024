---
title : "Tạo S3 Bucket"
date :  "2024-12-28"
weight : 1 
chapter : false
pre : " <b> 4.1 </b> "
---

## Tạo S3 Bucket

**1.** Trong AWS Management Console, thực hiện tìm kiếm dịch vụ **S3** và chọn.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.1.png)

**2.** Tạo S3 Bucket

- Chọn **Create bucket**
- Tại **Bucket name** điền ``` data-stock-prices-01 ```
- Phần còn lại để mặc định.
- Chọn **Create bucket**
- Tạo thành công.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.2.png)

**3.** Thêm folder lưu trữ dữ liệu.

- Tại **Objects** - chọn **Create folder**
- **Folder name**: ``` snowflake ```
- Chọn **Create folder**

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.3.png)

- Tạo foler thành công.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.4.png)

{{%notice tip%}}
Tên của S3 Bucket phải là duy nhất, nếu tên đã trùng hãy thử thêm chữ hoặc số ở phía sau.
{{%/notice%}}
