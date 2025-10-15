# CMC Python Intro 

Workshop notebooks for the CMC (University of Leeds).  
Put Apollo example CSVs in `data/raw/`:
- apollo_modeChoiceData.csv
- apollo_swissRouteChoiceData.csv
- apollo_drugChoiceData.csv
- apollo_timeUseData.csv

## Structure
notebooks/ — teaching notebooks  
data/raw — input CSVs (download from Apollo examples)  
data/processed — outputs (ignored by Git)  
figures/ — saved plots (ignored by Git)  
src/ — small helper utilities

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
