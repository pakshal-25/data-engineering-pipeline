import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""
predicate_pushdown = "region in ('ca','gb','us')"
# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1761865244600 = glueContext.create_dynamic_frame.from_catalog(database="de_pro_1_raw", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1761865244600",push_down_predicate = predicate_pushdown)

# Script generated for node Change Schema
ChangeSchema_node1761865251477 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1761865244600, mappings=[("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "bigint"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "bigint"), ("likes", "long", "likes", "bigint"), ("dislikes", "long", "dislikes", "bigint"), ("comment_count", "long", "comment_count", "bigint"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx="ChangeSchema_node1761865251477")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=AWSGlueDataCatalog_node1761865244600, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1761865025360", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1761865248608 = glueContext.write_dynamic_frame.from_options(frame=AWSGlueDataCatalog_node1761865244600, connection_type="s3", format="glueparquet", connection_options={"path": "s3://de-pro-1-cleaned-data", "partitionKeys": ['region']}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1761865248608")

job.commit()