📊 Data Engineering YouTube Trending Video Analysis Project

A complete end-to-end cloud data engineering pipeline built using AWS (S3, Glue, Lambda, Athena, IAM, QuickSight) to ingest, process, transform, analyze, and visualize trending YouTube video data across multiple regions.

This project simulates a real-world data engineering workflow involving structured + semi-structured data, a multi-layered data lake architecture, automated ETL, and serverless analytics.

🔥 Project Overview

The goal of this project is to build a scalable and secure data pipeline that can:

✔ Ingest raw YouTube trending video data from multiple regions
✔ Clean, transform, and standardize it using PySpark
✔ Store it in a structured data lake on S3
✔ Automate ETL using AWS Glue & Lambda
✔ Query data using AWS Athena
✔ Build interactive dashboards using QuickSight

This project demonstrates industry-level data engineering skills using cloud-native tools.

🎯 Key Features
🗂️ 1. Multi-Zone Data Lake

Organized into 3 S3 zones:

/raw

/cleaned

/transformed

⚙️ 2. Serverless ETL Pipeline

AWS Glue Job written in PySpark

Glue Crawler for schema detection

Automated cleanup & transformation logic

🔔 3. Event-Driven Workflow

AWS Lambda triggers when new files are uploaded

Lambda invokes Glue jobs automatically

🔎 4. Serverless Query Engine

Athena queries data directly from S3

No need to load into a database

📊 5. Interactive Visualizations

Built in Amazon QuickSight, including:

Top trending categories

Most viewed videos

Engagement metrics (likes, comments)

Regional popularity patterns

🧰 Technologies Used
Category	Tools
Cloud	AWS S3, IAM, Lambda, Glue, Athena, QuickSight
Programming	Python, PySpark
Data	CSV, JSON (category mapping)
CLI	AWS CLI, Shell scripting
Visualization	Amazon QuickSight
📚 Dataset

Kaggle: YouTube Trending Video Dataset
Contains daily trending videos for multiple countries.

🔗 https://www.kaggle.com/datasets/datasnaek/youtube-new

Includes:

Titles, channels, tags

Views, likes, dislikes

Comment counts

Publication timestamps

Regional category mapping via JSON
