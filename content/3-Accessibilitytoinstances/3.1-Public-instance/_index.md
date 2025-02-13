---
title : "Create table in DynamoDB"
date :  "2024-12-28"
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

### Creating a Table in DynamoDB

**1.** In the AWS Management Console, search for the **DynamoDB** service and select it.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.1.png)

- Click **Create table**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.4.png)

**2.** Information

- **Table name**: Enter `stock-prices`
- **Partition key**: `symbol`
- **Sort key**: `timestamp`

- Click **Create table**.

![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.2.png)

- The table has been successfully created.
![dy](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/3.connect/3.1.3.png)

{{%notice tip%}}
The table name must be unique.
{{%/notice%}}