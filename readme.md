# JupyterLab_SQLAlchemy Pattern

A simple example to set up and use SQLAlchemy in JupyterLab.

This example sets up two sqlite databases. The same pattern works with mysql databases. Example URL strings for mysql setup are shown as comments in the db_config.py file. This pattern can be extended for multiple databases.

A subset of the Chinook database is used for database 1. A very minimalist custom database, pab.sqlite, is used for database 2. The files models_chinook.py and models_pab.py in the modules folder define the SQLAlchemy declarative_base classes for the database tables.

The queries.ipynb JupyterLab notebook uses SQLAlchemy to query the two databases and display the results in Pandas DataFrames.
