---
title : "Tải dữ liệu từ S3 lên Snowflake"
date :  "2024-12-28"
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

{{% notice tip %}}
Phần này yêu cầu có tài khoản Snowflake, hãy chắc chắn rằng bạn đã có.
{{% /notice %}}

Ở phần trước, ta đã có dữ liệu chứng khoán được lưu thành các tệp .csv theo ngày và được lưu trữ trong **S3 Bucket**, bây giờ ta sẽ đưa nó lên **Snowflake** để có thể dễ quan sát, sử dụng và quản lý.

### Tạo cơ sở dữ liệu trên Snowflake

**1.** Truy cập vào trang [Snowflake](https://app.snowflake.com/) 

- Đăng nhập bằng tài khoản đã tạo.

**2.** Chọn **Create** - **SQL worksheets**

- Chạy các câu lệnh: 

``` CREATE DATABASE FCJ_STOCK_PRICES; ```

``` USE DATABASE FCJ_STOCK_PRICES; ```

![4](/images/5.fwd/5.1.1.png)

- Tạo thành công **Database**.

**3.** Thực hiện tạo một **Stage** trong **Snowflake**

``` CREATE STAGE my_stage
  URL = 's3://data-stock-prices-01/snowflake/'
  CREDENTIALS = (AWS_KEY_ID = '<<your aws key id>>' AWS_SECRET_KEY = 'your aws secret key'); 

```

![4](/images/5.fwd/5.1.2.png)

{{% notice tip %}}
Phần này bạn hãy quay lại AWS với tài khoản có quyền quản trị và lấy AWS_KEY_ID cùng với AWS_SECRET_KEY của tài khoản AWS đang lưu trữ **S3 Bucket** đã tạo từ bước trước để điền vào. 

{{% /notice %}}


Hãy thử truy cập vào IAM: Chọn thanh **Users** - Di chuyển đến **Security credentials** - Tại **Access keys** sẽ có **AWS_KEY_ID** cùng với **AWS_SECRET_KEY** (Hoặc bạn có thể tạo thêm Access keys và lấy AWS_KEY_ID cùng với AWS_SECRET_KEY từ Access keys vừa tạo để sử dụng cho đoạn lệnh trên.)

**4.** Tạo bảng stock_prices trên Snowflake

- Hãy chạy đoạn lệnh dưới đây.

```
CREATE OR REPLACE TABLE stock_prices(
    low          VARCHAR(128),  -- Sử dụng VARCHAR thay vì NUMBER
    symbol       VARCHAR(128),
    timestamp    VARCHAR(128),
    open         VARCHAR(128),
    volume       VARCHAR(128),
    high         VARCHAR(128),
    close        VARCHAR(128),
    date         VARCHAR(128)
);
```

- Tạo thành công bảng trên **Snowflake**

![4](/images/5.fwd/5.1.3.png)

**5.** Thực hiện nạp dữ liệu vào bảng.

- Hãy chạy đoạn lệnh dưới đây.

```
COPY INTO stock_prices
FROM @my_stage
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1)  
ON_ERROR = 'SKIP_FILE';  
```
- Thông báo thành công nạp dữ liệu vào bảng.

![4](/images/5.fwd/5.1.4.png)

- Sử dụng câu lệnh ``` SELECT * FROM stock_prices; ``` để xem dữ liệu đã nạp vào.

![4](/images/5.fwd/5.1.5.png)

- Dữ liệu đã được thêm vào bảng thành công.

Tiếp theo ta sẽ thực hiện thêm **EventBridge** để dữ liệu sẽ được cập nhật liên tục theo thời gian thực vào **S3 Bucket**.

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

![4](/images/5.fwd/5.1.6.png)

![4](/images/5.fwd/5.1.7.png)

{{% notice tip %}}
Như vậy, dữ liệu sẽ được cập nhật và đưa vào DynamoDB cùng S3 một cách liên tục theo từng ngày.
{{% /notice %}}