import pandas as pd
from sentence_transformers import SentenceTransformer, util
from telegram import Updatefrom 
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "8124674739:AAEeF30hUe4Spq7jvTbOp4y1PMakyDscncQ"
MODEL = SentenceTransformer('paraphrase-MiniLM-L6-v2')

questions = []
answers = []
questions_embeddings = None

def