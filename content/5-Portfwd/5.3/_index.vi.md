---
title : "Biểu đồ dữ liệu trong Snowflake"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Biểu đồ dữ liệu trong Snowflake

Hãy chọn **Chart** trên thanh **result** của **Snowflake** sau khi chạy câu lệnh ``` select * from stock_price_data; ```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/25.png)

- Tại đây ta có thể thực hiện việc tạo các biểu đồ dựa trên dữ liệu được lưu trong table vừa tạo.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/26.png)

Các mục bao gồm: **Chart type**, **Data**, **Appearance**

**1.** **Chart type**

{{% notice info %}}

**Chart type** cho phép người dùng chọn lựa các biểu đồ để thể hiện dữ liệu.

{{% /notice %}}

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/27.png)

-- **Line Chart** (Biểu đồ đường)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/28.png)
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/29.png)

-- **Bar Chart** (Biểu đồ cột)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/30.png)
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/31.png)

-- **Scatter Plot** (Biểu đồ phân tán)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/32.png)

-- **Heatgrid** (Bản đồ nhiệt dạng lưới)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/33.png)

-- **Scorecard** (Thẻ điểm)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/34.png)

**2.** **Data**

{{% notice info %}}

**Data** ở đây là dữ liệu được lưu trong bảng (table) hoặc truy vấn từ bảng (query). Đây là nguồn cung cấp dữ liệu để vẽ biểu đồ.

{{% /notice %}}

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/35.png)

Cho phép chọn lựa các cột dữ liệu, có thể lấy giá trị tổng (sum), lớn nhất (max), bé nhất (min),...

Có thể loại bỏ cột dữ liệu đó khỏi biểu đồ, cũng có thể thêm một cột dữ liệu mới vào.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/36.png)

**3.** **Appearance** 

{{% notice info %}}

**Appearance** (giao diện) của biểu đồ liên quan đến cách hiển thị trực quan dữ liệu. Nó không ảnh hưởng đến data nhưng giúp biểu đồ dễ hiểu hơn.

{{% /notice %}}

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/37.png)

**Ví dụ**: Thực hiện thêm tên của các cột trong đồ thị và hiển thị chú thích.

- Trước khi thực hiện thêm.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/39.png)

- Sau khi thêm.

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/38.png)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/40.png)

---

{{% notice info %}}

Tiếp theo ta sẽ thực hiện thêm **EventBridge** để dữ liệu sẽ được cập nhật liên tục theo thời gian thực vào **S3 Bucket** và **Snowflake**.

{{% /notice %}}
