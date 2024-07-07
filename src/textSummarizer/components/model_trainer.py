import os
from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer
from transformers import pipeline, set_seed
from datasets import load_dataset, load_from_disk
import matplotlib.pyplot as plt
from datasets import load_dataset, load_metric
import pandas as pd
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import nltk
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
import torch

from textSummarizer.entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config= config

    def train(self):
        device= "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer= AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        dataset_samsum=load_from_disk('samsum_dataset')
        trainer_args = TrainingArguments(
            output_dir='pegasus-samsum', num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, 
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
            )
        
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum['test'],
            eval_dataset=dataset_samsum['validation']
        )
        trainer.train()
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))

    
           