---
title : "Tạo IAM User"
date :  "2024-12-28"
weight : 1 
chapter : false
pre : " <b> 2.1 </b> "
---

### Tạo IAM User

Trong bước này, chúng ta sẽ cần tạo một tài khoản IAM User để sử dụng cho việc thực hiện bài thực hành này.

**1.** Trong **AWS Management Console**, thực hiện tìm kiếm dịch vụ IAM và **chọn**.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.1.png)

**2.** Trong **IAM Dashboard**, chọn Users từ menu bên trái và sau đó chọn **Create user**.

![IAM](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.5.png)

**3.** Thực hiện điền các thông tin.
 
 - **Username**: ``` user_fcj_2024 ```
 - Click chọn **Provide user access** to the AWS Management Console
 - Chọn **custom password** và nhập password cho tại khoản.
 - Tùy chọn có thể yêu cầu người dùng phải tạo mật khẩu mới khi đăng nhập hoặc không. Ở đây người dùng có thể đăng nhập vào luôn và không cần phải tạo lại mật khẩu.
 - Chọn **Next**.
![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.2..png)

**4.** Gán thêm các quyền cần thiết cho User.

- Chọn **Attach policies directly**.
- Chọn các quyền: **AmazonDynamoDBFullAccess**, **AmazonS3FullAccess**, **AWSLambda_FullAccess**, **AmazonEventBridgeFullAccess**, **IAMFullAccess**.
- Chọn **Next**.

![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.rep.png)

**5.** Xem lại các thông tin đã thêm vào.

![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.3.png)

- Chọn **Create user**.

- Người dùng đã được tạo thành công, có thể tải file cvs thông tin người dùng.

![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.4.png)

- Có thể sử dụng đường link URL để đăng nhập và sử dụng tài khoản đã tạo.