+++
title = "Dọn dẹp tài nguyên  "
date = 2021
weight = 6
chapter = false
pre = "<b>6. </b>"
+++

Chúng ta sẽ tiến hành các bước sau để xóa các tài nguyên chúng ta đã tạo trong bài thực hành này.

## **Quy trình Dọn dẹp: Xóa Tài nguyên AWS và Snowflake**  

Để xóa hoàn toàn các tài nguyên đã tạo trong dự án này, hãy làm theo quy trình dọn dẹp có cấu trúc dưới đây.  

---

### **1. Xóa Cơ sở Dữ liệu trên Snowflake**  
1. Đăng nhập vào tài khoản **Snowflake**.  
2. Điều hướng đến **Data** → **Databases**.  
3. Tìm và chọn cơ sở dữ liệu đã tạo trước đó.  
4. Chạy lệnh SQL sau trong **SQL worksheet**:  
   ```sql
   DROP DATABASE FCJ_STOCK_PRICES;
   ```
5. Xác nhận rằng cơ sở dữ liệu đã được xóa thành công.  

---

### **2. Xóa IAM User**  
1. Mở **AWS Management Console** và tìm kiếm **IAM**.  
2. Điều hướng đến **Users**.  
3. Xác định và chọn các IAM User đã tạo trong dự án này.  
4. Nhấp vào **Delete** và xác nhận để xóa User.  

---

### **3. Xóa Hàm Lambda (Lambda Functions)**  
1. Truy cập **AWS Lambda** trong **AWS Management Console**.  
2. Dưới mục **Functions**, tìm các hàm Lambda đã tạo.  
3. Chọn hàm cần xóa, nhấp vào **Actions**, sau đó chọn **Delete**.  
4. Xác nhận xóa khi được yêu cầu.  

---

### **4. Xóa S3 Bucket**  
1. Điều hướng đến **Amazon S3** trong **AWS Management Console**.  
2. Tìm **bucket** đã tạo để lưu trữ dữ liệu chứng khoán.  
3. Chọn **bucket**, sau đó nhấp vào **Empty**.  
4. Nhập **"permanently delete"** để xác nhận và xóa toàn bộ dữ liệu trong bucket.  
5. Sau khi bucket trống, nhấp vào **Delete** và xác nhận xóa.  

---

### **5. Xóa Bảng DynamoDB**  
1. Mở **AWS Management Console** và tìm kiếm **DynamoDB**.  
2. Điều hướng đến **Tables** và tìm bảng đã tạo trong dự án này.  
3. Chọn bảng, sau đó nhấp vào **Delete**.  
4. Xác nhận việc xóa và chờ cho đến khi bảng bị xóa hoàn toàn.  

---

### **6. Kiểm tra Lần Cuối**  
- Đảm bảo rằng tất cả các tài nguyên AWS (**IAM roles, Lambda functions, S3 buckets và DynamoDB tables**) đã bị xóa.  
- Xác nhận rằng **cơ sở dữ liệu Snowflake** không còn tồn tại.  

Quy trình này giúp đảm bảo việc xóa sạch và có tổ chức tất cả các tài nguyên liên quan đến dự án.