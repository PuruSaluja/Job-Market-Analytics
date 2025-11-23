graph TD
    subgraph Data Sources
        K[Kaggle Datasets]
        S[Web Scraping]
        G[Synthetic Generator]
    end

    subgraph ETL Pipeline
        I[ingest.py]
        C[clean_transform.py]
        L[load_to_sql.py]
    end

    subgraph Storage
        R[(Raw Data CSV)]
        P[(Processed Data CSV)]
        DB[(SQLite Database)]
    end

    subgraph Analysis
        NLP[skill_extraction.py]
        EDA[eda.ipynb]
        TR[job_trends.py]
    end

    subgraph Presentation
        D[Power BI Dashboard]
        Rep[Summary Report]
    end

    G -->|Generates| I
    I -->|Saves| R
    R -->|Reads| C
    C -->|Saves| P
    P -->|Reads| L
    L -->|Loads| DB
    DB -->|Reads| NLP
    NLP -->|Updates| DB
    DB -->|Reads| EDA
    DB -->|Reads| TR
    DB -->|Connects| D
    TR -->|Generates Plots| Rep
