
import json
from io import StringIO
import os
import pickle as pkl
import joblib
import time
import sys
import subprocess
import numpy as np
import pandas as pd
import numpy as np
import boto3
import sagemaker
import helper
import json
import os
import pickle as pkl
import numpy as np
import ast
from sagemaker.serializers import CSVSerializer

boto_session = boto3.Session()
region= boto_session.region_name

#The feature list is passed as an environemnt variable to the script- feature list is defined by the client.
feature_list=os.environ['feature_list']
feature_list=ast.literal_eval(feature_list)



def model_fn(model_dir):
    print ('processing - in model_fn')
    return None



def input_fn(request_body, request_content_type):
    print(request_content_type)
    """
    The SageMaker XGBoost model server receives the request data body and the content type,
    and invokes the `input_fn`.
    Return a DMatrix (an object that can be passed to predict_fn).
    """
    if request_content_type == "text/csv":
        params =request_body.split(',')
        id_dict={'customer_id':params[0].strip(), 'product_id':params[1].strip()}
        start = time.time()
        recs= helper.get_latest_featureset_values(id_dict, feature_list)
        end= time.time()
        duration= end-start
        print("time to lookup features from two feature stores:", duration)
        records= [e for e in recs.values()]
        return [records]
    else:
        raise ValueError("{} not supported by script!".format(request_content_type))
        

def predict_fn(input_data, model):
    """
    SageMaker XGBoost model server invokes `predict_fn` on the return value of `input_fn`.
    Return a two-dimensional NumPy array where the first columns are predictions
    and the remaining columns are the feature contributions (SHAP values) for that prediction.
    """
    return input_data
