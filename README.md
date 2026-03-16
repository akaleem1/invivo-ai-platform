# InVivo AI Platform

An AI-enabled data platform for exploring compound toxicity and pharmacological properties using modern data engineering, machine learning, and natural language interfaces.

This project simulates an AI-ready research data ecosystem similar to platforms used in drug discovery and translational pharmacology environments.

The platform integrates:
	•	automated data ingestion pipelines
	•	PostgreSQL data storage
	•	machine learning toxicity modeling
	•	REST APIs for data access
	•	interactive scientific dashboards
	•	a natural language AI assistant for database queries

The goal is to demonstrate how heterogeneous research data can be transformed into an AI-driven decision support tool for scientists.

⸻

Project Overview

Modern drug discovery requires scalable systems to integrate experimental datasets, perform analysis, and enable researchers to explore insights quickly.

This project implements a simplified version of such a system.

The platform allows users to:

• ingest compound datasets through ETL pipelines
• store structured data in PostgreSQL
• run machine learning models to predict toxicity
• expose research data through a FastAPI service
• interact with datasets through a Streamlit dashboard
• query the database using natural language via an AI assistant

⸻

System Architecture
Dataset
   ↓
ETL pipeline
   ↓
PostgreSQL database
   ↓
FastAPI data service
   ↓
Streamlit research dashboard
   ↓
AI assistant (LLM → SQL → Database)

This architecture reflects how modern AI-ready data ecosystems are built in pharmaceutical research environments.

⸻

Features

Data Engineering Pipeline
	•	automated dataset ingestion
	•	data cleaning and preprocessing
	•	structured dataset generation
	•	modular ETL scripts

Technologies used:
	•	Python
	•	pandas
	•	SQLAlchemy

⸻

PostgreSQL Data Platform

The platform stores compound datasets in a relational database designed for scalable data access.
Example schema:
Table: compounds

compound
molecular_weight
logP
h_donors
h_acceptors
tpsa
toxicity_label

This allows efficient querying of pharmacological features.

⸻

Machine Learning Toxicity Model

A machine learning model predicts compound toxicity using molecular features.

Model:

Random Forest classifier

Evaluation metrics:
	•	Accuracy
	•	ROC-AUC

Example performance:
Accuracy: ~0.85
ROC-AUC: ~0.91

Feature importance analysis highlights which molecular properties contribute most strongly to toxicity predictions.

Example top predictors:
	•	molecular weight
	•	logP
	•	TPSA

⸻

FastAPI Data Service

The platform exposes the database through a REST API.
GET /compounds
GET /toxicity/{compound}
GET /filter
GET /toxic

These endpoints allow other services or applications to access the dataset.

FastAPI automatically generates interactive documentation.

⸻

Scientific Research Dashboard

A Streamlit dashboard provides interactive visualization and exploration of compound datasets.

Dashboard capabilities include:
	•	compound dataset explorer
	•	toxicity analysis
	•	feature distributions
	•	correlation heatmaps
	•	filtering compounds by physicochemical properties

Example visualizations:

• molecular feature distributions
• toxicity comparison plots
• correlation heatmaps

⸻

Natural Language AI Assistant

The platform includes an AI assistant that converts research questions into SQL queries.

Example queries:
Show toxic compounds with logP greater than 4
List compounds with molecular weight above 400
Find compounds with low TPSA

Workflow:
User question
      ↓
LLM converts question to SQL
      ↓
PostgreSQL query executed
      ↓
Results returned to user

This demonstrates how LLM-powered data access tools can improve researcher productivity.

⸻

Project Structure
invivo-ai-platform
│
├── src
│   ├── etl
│   │   ├── generate_dili_dataset.py
│   │   └── etl_pipeline.py
│   │
│   ├── database
│   │   ├── load_to_postgres.py
│   │   └── query_data.py
│   │
│   ├── models
│   │   └── toxicity_model.py
│   │
│   ├── api
│   │   ├── main.py
│   │   └── schemas.py
│   │
│   ├── ai
│   │   └── assistant.py
│   │
│   └── app
│       └── dashboard.py
│
├── data
│   ├── raw
│   └── processed
│
├── analysis
│
├── requirements.txt
└── README.md


⸻

Installation

Clone the repository:
git clone https://github.com/yourusername/invivo-ai-platform.git
cd invivo-ai-platform

Create a virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

⸻

Running the Platform

Generate Dataset
python src/etl/generate_dili_dataset.py

Run ETL Pipeline
python src/etl/etl_pipeline.py

Load Data into PostgreSQL
python src/database/load_to_postgres.py

⸻

Start API Server
uvicorn src.api.main:app --reload

API documentation:
http://127.0.0.1:8000/docs


⸻

Launch Dashboard
streamlit run src/app/dashboard.py

⸻

Technologies Used

Python
PostgreSQL
SQLAlchemy
FastAPI
Streamlit
scikit-learn
OpenAI API
pandas
seaborn
matplotlib

⸻

Future Improvements

Potential extensions include:
	•	integration of real pharmacology datasets
	•	support for gene expression and multi-omics data
	•	Nextflow pipelines for data processing
	•	deployment to cloud infrastructure
	•	improved LLM retrieval systems

⸻

Motivation

Modern pharmaceutical research increasingly relies on AI-ready data platforms capable of integrating heterogeneous datasets and enabling rapid analysis.

This project demonstrates how machine learning, databases, APIs, and AI assistants can be combined to create a scalable research data ecosystem.



















