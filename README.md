# Introduction to Python for Choice Modelling Workshop (CMC, University of Leeds)

Welcome to the Introductory Python Workshop hosted by the Choice Modelling Centre (CMC) at the University of Leeds. In this series of six Jupyter notebooks, we will build a strong foundation in Python programming and demonstrate how these skills apply to discrete choice modeling using Apollo datasets (https://www.apollochoicemodelling.com/). Each notebook introduces core concepts with simple examples, then connects them to real-world choice modelling tasks. The focus is on clarity, practical relevance, and understanding the economic context behind the code.

## Repository Structure

The workshop repository is organized as follows: 
````
```
cmc-python-intro/
├─ notebooks/
│  ├─ 00_setup.ipynb          ← Setup and Tools
│  ├─ 01_python_fundamentals_choice.ipynb
│  ├─ 02_numpy_pandas_mode_choice.ipynb
│  ├─ 03_visualization_discrete_choice.ipynb
│  ├─ 04_logit_from_scratch.ipynb
│  ├─ 05_time_use_drug_choice.ipynb
│  └─ 06_exercises_solutions.ipynb
├─ data/
│  └─ raw/                    ← Raw Apollo CSV datasets (modeChoice, routeChoice, etc.)
├─ src/
│  └─ utils.py                ← Utility functions (e.g., softmax, standardize, etc.)
├─ requirements.txt           ← List of required Python packages
├─ .gitignore                 ← Files/directories to ignore in git (e.g., venv, __pycache__)
└─ README.md                  ← Overview and setup instructions for the repository
````

Each notebook is presented with detailed explanations and code. The target audience is postgraduate students and researchers at CMC, so we assume familiarity with choice modelling concepts but little to no experience with Python. Throughout, we emphasize step-by-step learning, applied examples with Apollo choice data, and interpretation of results in a choice modelling context.

Apollo datasets in `data/raw/`:
- apollo_modeChoiceData.csv
- apollo_swissRouteChoiceData.csv
- apollo_drugChoiceData.csv
- apollo_timeUseData.csv

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
