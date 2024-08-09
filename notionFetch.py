# import streamlit as st
# import pandas as pd
# import numpy as np
import os
from notion_client import Client
from dotenv import load_dotenv
load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])

block = notion.blocks.retrieve("0254931a-ccea-47c8-8099-1522f7a196e0")

lines = [line["text"]["content"] for line in block["quote"]["rich_text"]]
blockContent = " ".join(lines)
blockContent
