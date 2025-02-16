---
title : "Đưa dữ liệu lên Snowflake"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Tạo cơ sở dữ liệu trên Snowflake

**1.** Truy cập vào trang [Snowflake](https://app.snowflake.com/) 

- Đăng nhập bằng tài khoản đã tạo.

**2.** Chọn **Create** - **SQL worksheets**

- Chạy các câu lệnh: 

``` CREATE DATABASE STOCK_PRICES; ```

``` USE DATABASE STOCK_PRICES; ```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/3.png)

- Tạo thành công **Database**.

**3.** Tạo bảng **stock_prices_data** trên **Snowflake** và đưa dữ liệu vào.

**a.** Tạo bảng dữ liệu chứng khoán.

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

- Tạo thành công bảng trên **Snowflake**

**b.** Tạo **Integration Object** kết nối với S3.

{{% notice info %}}

**Integration Object** trong Snowflake là một đối tượng kết nối bên ngoài giúp Snowflake giao tiếp với các dịch vụ khác như S3

{{% /notice %}}

Hãy thực hiện câu lệnh dưới đây để tạo **Integration Object** kết nối với S3.

```

create or replace storage integration s3_int
  type = external_stage
  storage_provider = s3
  enabled = true
  storage_aws_role_arn = '<<Your role ARN>>'
  storage_allowed_locations = ('s3://data-stock-prices-01/snowflake/');

```

{{% notice tip %}}
Điền ARN của IAM Role vừa tạo đã được lưu từ bước trước để cho phép Snowflake truy cập vào S3, sửa lại đường dẫn S3 cho phù hợp với tên bucket của bạn.
{{% /notice %}}

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.png)

**c.** Kiểm tra thông tin chi tiết về **Storage Integration**.

{{% notice info %}}

**Storage Integration** là một đối tượng trong Snowflake dùng để kết nối với dịch vụ lưu trữ bên ngoài như AWS S3 một cách bảo mật và quản lý tự động. Thay vì phải cung cấp access key và secret key để truy cập S3, Snowflake cho phép sử dụng IAM Role của AWS để cấp quyền truy cập một cách an toàn.

{{% /notice %}}

Hãy thực hiện câu lệnh 
``` DESC INTEGRATION s3_int; ``` để kiểm tra thông tin chi tiết về **Storage Integration**.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/6.png)

{{% notice note %}}

Hãy lưu lại **property_value** của các **property**: **STORAGE_AWS_IAM_USER_ARN**, **STORAGE_AWS_ROLE_ARN**, **STORAGE_AWS_EXTERNAL_ID**

{{% /notice %}}

- Trở lại [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) - chọn **Roles** - chọn role vừa tạo ở bước trước.
- Chọn **Trust relationship** - **Edit trust policy**
- Điền **property_value** của **STORAGE_AWS_ROLE_ARN** đã lưu lại từ trước vào sau **"AWS"**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/7.png)


Sau đó, tiếp tục chọn **Add condition**
- Điền các thông tin: 

-- **Condition key**: ``` sts:ExternalId ```

-- **Qualifier**: ``` Default ```

-- **Operator**: ``` StringEquals ```

-- **Value**: hãy điền **property_value** của **STORAGE_AWS_EXTERNAL_ID** đã lưu từ trước.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/8.png)

- **Add condition**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/9.png)


**d.** Tạo **File Format** để đọc csv 

Tiếp tục chạy câu lệnh bên dưới

```
create or replace file format csv_format
                    type = csv
                    field_delimiter = ','
                    skip_header = 1
                    null_if = ('NULL', 'null')
                    empty_field_as_null = true;

```
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/10.png)

**e.** Tạo **External Stage** để kết nối với **S3**

{{% notice info %}}

**External Stage** là một kho lưu trữ bên ngoài được Snowflake sử dụng để truy xuất dữ liệu từ các dịch vụ lưu trữ đám mây như Amazon S3, Google Cloud Storage, hoặc Azure Blob Storage. Nó cho phép Snowflake đọc và ghi dữ liệu trực tiếp từ/đến kho lưu trữ bên ngoài mà không cần tải dữ liệu về Snowflake trước.

{{% /notice %}}

Thực hiện đoạn lệnh dưới đây để tạo **External Stage** để kết nối với **S3** đã được tạo từ trước.

```
create or replace stage ext_csv_stage
  URL = 's3://data-stock-prices-01/snowflake/'
  STORAGE_INTEGRATION = s3_int
  file_format = csv_format;

```
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/11.png)

**f.** Tạo **Pipe** để tự động load dữ liệu 

{{% notice info %}}

**Pipe** trong Snowflake là một cơ chế tự động hóa quá trình nạp dữ liệu từ External Stage (S3) vào bảng trong Snowflake. Nó sử dụng Snowpipe, một dịch vụ của Snowflake giúp tự động phát hiện khi có tệp mới trong kho lưu trữ đám mây (ví dụ: S3) và nạp dữ liệu vào bảng ngay lập tức mà không cần chạy lệnh COPY INTO thủ công.

{{% /notice %}}


- Hãy trở lại [**IAM**](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home) - **Roles** - chọn role vừa tạo ở bước trước.
- Chọn **Trust relationship** - **Edit trust policy**
- Sửa lại nội dung, điền **property_value** của **STORAGE_AWS_IAM_USER_ARN** đã lưu lại từ trước vào sau **"AWS"**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/13.png)

Tiếp tục thực hiện câu lệnh.

```
create or replace pipe mypipe auto_ingest=true as
copy into stock_price_data
from @ext_csv_stage
on_error = CONTINUE;

```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/14.png)

**g.** Thực hiện câu lệnh ``` show pipes ``` để kiểm tra **pipe**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/15.png)

{{% notice note %}}

Hãy lưu thông tin hiển thị trong cột **notification_chanel**.

{{% /notice %}}

- Trở lại với [S3](https://us-east-1.console.aws.amazon.com/s3/home?region=us-east-1)
- Chọn **bucket** được sử dụng để lưu thông tin được dùng để đưa lên **Snowflake**
- Đến phần **Event notifications**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/16.png)

- Chọn **Create event notification**
- Tại phần **General configuration**

-- **Event name**: ``` stock-price-event ```

- Tại **Event types** 

-- Click chọn **All object create events**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/17.png)

- Tại phần **Destination**

-- **Destination**: **SQS queue**

-- **SQS queue**: hãy điền thông tin của cột **notification_chanel** vừa lưu vào.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/18.png)

- **Save changes**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/19.png)

**Event notification** đã được tạo thành công.

- Hãy trở lại với [**Lambda**](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/discover?tab=code)
- Chọn **Function**
- Chọn function đầu tiên được tạo để đưa dữ liệu vào **DynamoDB** (ở đây function của mình có tên là **fetch_code**)
- Đến phần **Code**.
- Chọn **Test event** đã sử dụng từ trước - chọn **Edit test event** - chọn **Invoke**.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/20.png)
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/21.png)

**4.** **Kết quả**.

- Thực hiện câu lệnh ``` select * from stock_price_data; ``` để xem kết quả đã được đưa từ **S3** lên **Snowflake**

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/22.png)

**Dữ liệu từ S3 đã được thêm vào Snowflake thành công.**

{{% notice tip %}}

Tại bước tiếp theo sẽ sử dụng **Chart** trong **Snowflake** để có thể tạo ra các biểu đồ dữ liệu trên Snowflake nhằm giúp người xem dễ phân tích và đánh giá dữ liệu.

{{% /notice %}}

