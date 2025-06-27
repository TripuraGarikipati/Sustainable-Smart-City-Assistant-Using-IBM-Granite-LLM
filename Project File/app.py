import os, threading

import pandas as pd, numpy as np

from dotenv import load_dotenv

from sklearn.linear_model import LinearRegression

from fastapi import FastAPI, Form, UploadFile, File

import uvicorn, streamlit as st, requests

from huggingface_hub import InferenceClient

import streamlit.components.v1 as comp

 

# Load Hugging Face token

load_dotenv()

HF_TOKEN =""

hf = InferenceClient(api_key=HF_TOKEN)

 

app = FastAPI()