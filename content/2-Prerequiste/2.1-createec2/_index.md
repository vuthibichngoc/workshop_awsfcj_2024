---
title : "Create IAM User"
date :  "2024-12-28"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

### Create IAM User

In this step, we will need to create an IAM User account to use for this lab exercise.

**1.** In the AWS Management Console, search for the IAM service and select it.

![IAM1](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.1.png)

**2.** In the IAM Dashboard, select Users from the left menu and then click Create user.

**3.** Fill in the information.

 - Username: ``` user_fcj_2024 ```
 - Select **Provide user access to the AWS Management Console**
 - Choose **custom password** and enter the password for the account.
 - Optionally, you can require the user to create a new password when logging in, or not. Here, the user can log in directly without creating a new password.
 - Select Next.
![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.2..png)

**4.** Attach the necessary permissions for the User.

- Select **Attach policies directly**.
- Select the following permissions: **AmazonDynamoDBFullAccess**, **AmazonS3FullAccess**, **AWSLambda_FullAccess**, **AmazonEventBridgeFullAccess**, **IAMFullAccess**
- Select next.

**5.** Review the information added.

![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.3.png)

- Click **create user**.

- The user has been successfully created, and you can download the CVS file with the user information.

![IAM2](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/2.prerequisite/2.1.4.png)

- You can use the URL link to log in and use the created account.