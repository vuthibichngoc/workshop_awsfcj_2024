---
title : "Data Charts in Snowflake"
date :  "2024-12-28"  
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

### Observing Data in Snowflake  

Select **Chart** on the **result** bar in **Snowflake** after running the query:  
```sql
SELECT * FROM stock_price_data;
```

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/25.png)  

- Here, you can create charts based on the data stored in the table.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/26.png)  

The sections include: **Chart type**, **Data**, and **Appearance**  

#### **1. Chart type**  

{{% notice info %}}  

**Chart type** allows users to select different types of charts to visualize data.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/27.png)  

-- **Line Chart**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/28.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/29.png)  

-- **Bar Chart**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/30.png)  
![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/31.png)  

-- **Scatter Plot**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/32.png)  

-- **Heatgrid**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/33.png)  

-- **Scorecard**  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/34.png)  

#### **2. Data**  

{{% notice info %}}  

**Data** refers to the information stored in a table or retrieved through a query. This serves as the source for chart visualization.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/35.png)  

It allows you to select specific columns, aggregate values (sum, max, min, etc.), remove columns from the chart, or add new ones.  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/36.png)  

#### **3. Appearance**  

{{% notice info %}}  

**Appearance** relates to the visual representation of the chart. It does not affect the data but enhances readability and interpretation.  

{{% /notice %}}  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/37.png)  

**Example**: Adding column names and legend to the chart.  

- Before adding:  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/39.png)  

- After adding:  

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/38.png)

![4](https://vuthibichngoc.github.io/workshop_awsfcj_2024/images/5.fwd/40.png)

---

{{% notice info %}}  

Next, we will add **EventBridge** to ensure that data is continuously updated in real-time into the **S3 Bucket** and **Snowflake**.  

{{% /notice %}}  
