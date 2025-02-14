---
title : "Lưu dữ liệu vào DynamoDB"
date :  "2024-12-28"
weight : 2 
chapter : false
pre : " <b> 3.2. </b> "
---

## Lưu dữ liệu vào DynamoDB
### Tạo Lamdba function

**1.** Trong AWS Management Console, thực hiện tìm kiếm dịch vụ Lambda và chọn.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.1.png)

**2.** Tạo function trong Lambda

- Chọn **Create function**
- **Function name**: ```fetch_code```
- **Runtime**: Python 3.10
- **Architecture**: x86_64
- **Create function**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.2.png)

### Thiết lập Lamdba function

**1.** Thêm **Layer**.

- Di chuyển tới phần **Layers** sau đó click chọn **Add a layer**
- **Layer source**: AWS layers
- **AWS layers**: ``` AWSSDKPandas-Python310 ```
- **Version**: 23

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.3.png)

{{%notice tip%}}
Phần version hãy chọn version mới nhất.
{{%/notice%}}

**2.** Chỉnh sửa **timeout**.

- Đến phần **Configuration**
- Tại **General configuration** chọn **Edit**
- Tại **Timeout** hãy chỉnh cho nó lên đến 15s

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.5.png)

**3.** Thêm quyền cho function.

- Tại **Configuration** chọn **Permisstions** ở bên trái

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.png)

- Chọn phần **role name**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.4.png)

- Tới phần **Permissions** có thể thấy **Permissions policies**
- Chọn **Add permissions** - **Attach policies**
- Thực hiện thêm quyền **AmazonDynamoDBFullAccess** 
- Chọn **Add permissions**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.5.png)

**4.** Thực hiện đưa dữ liệu từ [Alphavantage](https://www.alphavantage.co/) vào bảng đã tạo trong **DynamoDB**

- Đến phần **Code** ở thanh tùy chọn.
- Thêm đoạn [SourceCode](https://vuthibichngoc.github.io/workshop_awsfcj_2024/file/fetch_code.py) vào phần **Code source** 
- Chọn **Test** - **Create new test event** - điền các thông tin và chọn **Save**
- Thực hiện chạy đoạn code.
- **Kết quả sau khi chạy**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.6.png)

### Kết quả tại DynamoDB.

- Truy cập vào [DynamoDB](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#service)
- Chọn **Tables** ở thanh tùy chọn bên trái - Click chọn Tables đã tạo từ trước.
- Tại bảng đã tạo từ trước, chọn **Explore table items** - Chọn nút **Run**

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.2.7.png)

- Kết quả đã được đưa xuống từ trang web [Alphavantage](https://www.alphavantage.co/) và lưu vào bảng **stock_prices** đã tạo từ trước ở **DynamoDB**
