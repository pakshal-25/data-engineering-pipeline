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

Build a mechanism to ingest data from multiple sources efficiently.

✔ 2. ETL System

Transform raw CSV and JSON data into a structured, query-ready format.

✔ 3. Centralized Data Lake

Store multi-region data in a unified S3-based data lake with raw, cleaned, and transformed layers.

✔ 4. Scalability

Ensure the pipeline scales seamlessly as data volume grows.

✔ 5. Cloud-First Architecture

Use AWS cloud services to process large datasets that cannot be handled on a local machine.

✔ 6. Reporting & Analytics

Build dashboard visualizations to answer key business questions.
Most trending categories

🛠 Services Used

⭐ Amazon S3

Object storage service providing scalability, high availability, security, and performance. Used as the data lake.

⭐ AWS IAM

Identity and Access Management service to control access to AWS resources securely.

⭐ AWS Glue

Serverless ETL tool used for:

Crawling schemas

Cleaning data

Running PySpark transformations

Preparing data for analytics

⭐ AWS Lambda

Serverless compute service used to automate ETL operations without provisioning servers.

⭐ AWS Athena

Serverless query engine used to run SQL queries directly on S3 without loading data.

⭐ Amazon QuickSight

Cloud-based BI tool used to build dashboards and visualizations from Athena datasets.
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




🔄 Pipeline Workflow
1️⃣ Upload raw YouTube trending data → S3 bucket (raw zone)
2️⃣ AWS Glue Crawler reads schema → creates metadata in Glue Catalog
3️⃣ PySpark ETL script (Glue Job) transforms data:

Clean missing fields

Parse JSON category mapping

Convert timestamps

Merge multi-region data

Write to cleaned/ and transformed/ zones

4️⃣ Lambda triggers Glue jobs automatically when new data arrives
5️⃣ Athena reads transformed data directly from S3
6️⃣ QuickSight dashboard shows insights & visualizations
📈 Dashboard Insights (QuickSight)

Examples of metrics you can visualize:

Most trending categories by region

Most popular channels

Videos with highest likes-to-views ratio

Daily trending patterns

Country-wise engagement trends
