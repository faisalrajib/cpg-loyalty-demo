# CPG Loyalty Program Demo

End-to-end demonstration project for a Consumer Packaged Goods loyalty program.

Components:
- Airflow DAGs for orchestration
- dbt transformations
- Simple collaborative filtering recommender
- Synthetic data generator

## Quick start (local)

```bash
python scripts/generate_synthetic_data.py
docker compose up -d
# then open http://localhost:8080 (Airflow)
Made for Solutions Engineer / Data Engineer portfolio – 2026
