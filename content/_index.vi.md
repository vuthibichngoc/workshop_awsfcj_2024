---
title : "Xây dựng hệ thống xử lý và lưu trữ dữ liệu chứng khoán bằng AWS Lambda, DynamoDB, S3 và Snowflake"
date :  "2024-12-28"  
weight : 1 
chapter : false
---
# Xây dựng hệ thống xử lý và lưu trữ dữ liệu chứng khoán bằng AWS Lambda, DynamoDB, S3 và Snowflake

### Tổng quan

 Dự án này xây dựng một hệ thống xử lý và lưu trữ dữ liệu chứng khoán tự động bằng cách sử dụng các dịch vụ AWS và Snowflake. Hệ thống thu thập giá cổ phiếu Microsoft từ API thông qua AWS Lambda và lưu trữ vào Amazon DynamoDB. Sau đó, một Lambda function khác xử lý và chuyển đổi dữ liệu thành các file CSV, lưu vào Amazon S3. Cuối cùng, dữ liệu được đưa vào Snowflake để phục vụ phân tích và báo cáo. Hệ thống tận dụng AWS Lambda, DynamoDB, S3 và EventBrigde (CloudWatch Events) để đảm bảo thu thập, xử lý, lưu trữ dữ liệu hiệu quả và liên tục. 
 
### Nội dung

 1. [Giới thiệu](1-introduce/)
 2. [Các bước chuẩn bị](2-Prerequiste/)
 3. [Thu thập và lưu trữ dữ liệu vào DynamoDB](3-Accessibilitytoinstance/)
 4. [Chuyển đổi và lưu dữ liệu dưới dạng CSV vào S3](4-s3log/)
 5. [Tải dữ liệu từ S3 lên Snowflake](5-Portfwd/)
 6. [Dọn dẹp tài nguyên](6-cleanup/)
