
import ipdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import psycopg2
import argparse

from app import app


def main(args):

    db_type = args.type
    user = args.user
    pw = args.password
    host = args.host
    port = args.port 
    db = args.database

    URI = f"{db_type}://{user}:{pw}@{host}/{db}"

    engine = create_engine(URI)
    db_session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )
    app.db = db_session

    app.run(debug=True)










if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str,  default='postgresql')
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--port', type=int, default=5432)
    parser.add_argument('--database', type=str, required=True)
    args = parser.parse_args()

    main(args)
    
