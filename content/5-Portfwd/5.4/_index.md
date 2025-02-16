---
title : "Adding EventBridge (CloudWatch Events)"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Adding EventBridge (CloudWatch Events) 

**1.** Go back to AWS and select **Lambda**  

- Choose **Function**  
- Select the function **fetch_code**  

**2.** Add an EventBridge (CloudWatch Events) trigger  

- Go to **Configuration** - select **Trigger**  
- Click **Add trigger**  
- **Select a source**: ``` EventBridge CloudWatch Events ```  
- **Rule**: Create a new rule  
- **Rule name**: ``` every_days ```  
- **Schedule expression**: ``` rate(1 day) ```  
- Click **Add**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.6.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/5.1.7.png)  

{{% notice info %}}  

Once completed, the data will be updated and automatically sent to **DynamoDB, S3, and Snowflake** daily. Each day, you can check the newly updated stock information.  

{{% /notice %}}
