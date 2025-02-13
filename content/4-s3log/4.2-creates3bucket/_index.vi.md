---
title : "Lưu dữ liệu vào S3 Bucket"
date :  "2024-12-28"
weight : 2 
chapter : false
pre : " <b> 4.2 </b> "
---

## Lưu dữ liệu vào S3 Bucket
### Tạo Lamdba function

**1.** Trong AWS Management Console, thực hiện tìm kiếm dịch vụ Lambda và chọn.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.1.png)

**2.** Tạo function trong Lambda

- Chọn **Create function**
- **Function name**: ``` 
DTToSnowflake ```
- **Runtime**: Python 3.10
- **Architecture**: x86_64
- **Create function**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.1.png)

### Thiết lập Lamdba function

**1.** Thêm **Layer**.

- Di chuyển tới phần **Layers** sau đó click chọn **Add a layer**
- **Layer source**: AWS layers
- **AWS layers**: ``` AWSSDKPandas-Python310 ```
- **Version**: 23

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.3.png)

{{%notice tip%}}
Phần **Version** hãy chọn version mới nhất.
{{%/notice%}}


**2.** Thêm quyền cho function.

- Tại **Configuration** chọn **Permisstions** ở bên trái
- Chọn phần **role name**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.2.png)

- Tới phần **Permissions** có thể thấy **Permissions policies**
- Chọn **Add permissions** - **Attach policies**
- Thực hiện thêm quyền **AmazonDynamoDBFullAccess**, **AmazonS3FullAccess**
- Chọn **Add permissions**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.3.png)

**4.** Thêm **Trigger**.

- Tại **Configuration** chọn **Trigger** ở bên trái.
- Chọn **Add trigger**
- Tìm tiếm **DynamoDB** và chọn.
- **DynamoDB table**: hãy chọn tên bảng đã tạo ở **DynamoDB** từ bước thứ 3

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.4.png)

- Chọn **Add**

**5.** Thực hiện đưa dữ liệu từ bảng **stock_prices** trong DynamoDB vào **S3 Bucket** đã tạo.

- Đến phần **Code** ở thanh tùy chọn.
- Thêm đoạn [SourceCode](https://vuthibichngoc.github.io/workshop_awsfcj_2024/file/DTToSnowflake.py) vào phần **Code source** 
- Chọn **Test** - **Create new test event** - điền các thông tin và chọn **Save**
- Thực hiện chạy đoạn code.
- **Kết quả sau khi chạy**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.1.5.png)

### Kết quả tại S3 Bucket.

- Truy cập vào [S3 Bucket](https://us-east-1.console.aws.amazon.com/s3/get-started?region=us-east-1&bucketType=general)
- Chọn **General purpose buckets** ở thanh tùy chọn bên trái - Click chọn Tables đã tạo từ trước - chọn vào folder đã tạo.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/4.s3/4.2.6.png)

- Dữ liệu về chứng khoán đã được xử lý thành các file .csv theo ngày tháng tương ứng và lưu vào **S3 Bucket** đã tạo.
