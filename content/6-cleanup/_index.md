+++
title = "Clean up resources"
date = 2022
weight = 6
chapter = false
pre = "<b>6. </b>"
+++

We will take the following steps to delete the resources we created in this exercise.

## **Cleanup Process: Removing AWS and Snowflake Resources**  

To fully remove the resources created during this project, follow the structured cleanup process below.  

---

### **1. Delete the Snowflake Database**  
1. Log in to your **Snowflake** account.  
2. Navigate to **Data** → **Databases**.  
3. Locate the database created earlier.  
4. Run the following command in the SQL worksheet:  
   ```sql
   DROP DATABASE STOCK_PRICES;
   ```
5. Confirm that the database has been successfully removed.  

---

### **2. Delete IAM User**  
1. Open the **AWS Management Console** and search for **IAM**.  
2. Navigate to **Users**.  
3. Locate and select the User that were created for this project.  
4. Click **Delete** and confirm the removal of each user.  

---

### **3. Delete Lambda Functions**  
1. Go to **AWS Lambda** in the AWS Management Console.  
2. Under **Functions**, find the Lambda functions created for this project.  
3. Select the function, click **Actions**, then choose **Delete**.  
4. Confirm deletion when prompted.  

---

### **4. Delete S3 Bucket**  
1. Navigate to **Amazon S3** in the AWS Management Console.  
2. Locate the bucket created for storing stock price data.  
3. Select the bucket and click **Empty**.  
4. Type **"permanently delete"** to confirm and empty the bucket.  
5. After the bucket is emptied, click **Delete** and confirm its removal.  

---

### **5. Delete DynamoDB Table**  
1. Open the **AWS Management Console** and search for **DynamoDB**.  
2. Navigate to **Tables** and locate the table created in this project.  
3. Select the table, then choose **Delete**.  
4. Confirm the deletion and wait for the table removal process to complete.  

---

### **Final Check**  
- Ensure that all AWS resources (IAM roles, Lambda functions, S3 buckets, and DynamoDB tables) have been deleted.  
- Verify that the **Snowflake database** is no longer present.  
