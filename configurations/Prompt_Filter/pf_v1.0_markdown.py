from utils.table_serializer import MarkdownSerializer
from utils.table_processor import ShuffleRowsProcessor, FirstNRowsProcessor

# prompt_template = """I am preparing a dataset for public release and publication at NeurIPS. The dataset consists of publicly available data (e.g., public benchmarks, web tables, etc.). Despite being public, I want to ensure that the dataset does not inadvertently expose private or sensitive information that could lead to privacy risks (e.g., names, addresses, phone numbers, emails, personal health or financial info, or any identifying details about individuals).

# Please analyze the following text and judge whether it contains any sensitive or personally identifiable information (PII):
#     1. Does it contain any potentially sensitive or personally identifiable information (PII)?
#     2. Could this text pose a privacy risk to an individual, even if the data is publicly available?
#     3. Should this data be redacted, anonymized, or excluded from the dataset before release?
    
# If you believe the text contains sensitive or PII information, return  {"PII": "yes", "re"}, otherwise return {"PII": "no"}. No explanation is needed.

# ====BEGIN INPUT TEXT====

# {{{prompt}}}

# ====END INPUT TEXT====
# """
prompt_template = """I am preparing a dataset for public release and publication at NeurIPS. The dataset consists of publicly available data (e.g., public benchmarks, web tables, etc.). Please review the dataset, and ensure that it does not contain sensitive private information, such as ssn, credit card information, Bank account number, Driver’s license number, etc. Note that because the data is from the public web, information such as names and addresses are acceptable.
    
If you believe the text contains sensitive or PII information, return  {"PII": "yes"}, otherwise return {"PII": "no"}. No explanation is needed.

====BEGIN INPUT TEXT====
{{{prompt}}}
====END INPUT TEXT===="""


dataset_config = {
    "task": "Prompt_Filter",
    "version": "1.0",
    "tag": ["1.0"],
    # "note": "Data-Imputation. Sample 1000 test cases for each dataset.",
    "path": "/datadrive/junjie/TableBenchmarkSurvey/data/Prompt_Filter/all",
    "info": "info.json",
    "fields": {
        "prompt": {
            "type": "text",
            "name": "prompt"
        }
    }
}
