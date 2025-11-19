A fully end-to-end cloud data engineering project built using AWS S3, AWS Glue, Lambda, Athena, and QuickSight, designed to ingest, transform, analyze, and visualize structured & semi-structured YouTube trending video data at scale.

This project replicates a real-world data engineering pipeline where data arrives in raw form, is processed through automated ETL pipelines, stored in a centralized data lake, and queried using a serverless architecture.

🚀 Project Summary

This project analyzes daily trending YouTube videos across multiple countries and builds a scalable cloud pipeline with:

Automated data ingestion from multiple sources

Raw → cleaned → transformed layers inside a data lake

Serverless ETL pipelines using AWS Glue + PySpark

Event-driven processing via AWS Lambda

Interactive analytics with Athena

Dashboard & insights built in QuickSight

Designed for scalability, production readiness, and industry standard best practices.

🎯 Project Goals
✔ 1. Data Ingestion

Create a modular pipeline to ingest CSV + JSON files from multiple regions.

✔ 2. ETL Transformation

Use PySpark (AWS Glue) to clean, merge, and standardize semi-structured data.

✔ 3. Data Lake Architecture

Implement a multi-zone S3 structure:

raw/

cleaned/

transformed/

✔ 4. Scalability

Use serverless AWS services that automatically scale with data volume.

✔ 5. Cloud-Native Processing

Leverage AWS to perform large-scale data transformations not possible locally.

✔ 6. Analytics & Reporting

Use Athena + QuickSight to extract insights such as:

Most trending categories

Top channels by views

Regional patterns in trending videos

Engagement metrics (likes, comments, etc.)

🛠 Tech Stack & AWS Services
Service	Purpose
Amazon S3	Central data lake for raw, cleaned, and transformed data
AWS IAM	Role-based access control
AWS Glue	PySpark ETL pipelines + Crawler for schema detection
AWS Lambda	Event-driven triggers to automate workflows
AWS Athena	Serverless SQL query engine for S3
Amazon QuickSight	Dashboard & reporting layer
📚 Dataset Used

Kaggle Dataset: YouTube Trending Videos
Contains CSV + JSON metadata for daily trending YouTube videos in multiple regions.

🔗 https://www.kaggle.com/datasets/datasnaek/youtube-new

Features:

Trending videos per region

Title, channel, tags

Likes, views, comments

category_id mapping via JSON

Publication timestamps
