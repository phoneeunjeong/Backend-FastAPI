from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import redis

@contextmanager
def session_scope():
    engine = create_engine(
        "mysql+mysqldb://root:wnsrl9098@localhost:3306/db_pej_test?charset=utf8",
        encoding="utf-8",
        pool_recycle=3600,
        pool_size=20,
        max_overflow=20,
        pool_pre_ping=True
    )
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()

Redis = redis.StrictRedis(host='localhost', port=6379, db=0)
