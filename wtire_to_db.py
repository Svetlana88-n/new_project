import sqlite3
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.orm import declarative_base

# Получение данных
def get_postgres_creds():
    conn = sqlite3.connect('creds.db')
    cursor = conn.cursor()
    cursor.execute("SELECT url, port, user, pass FROM access")
    url, port, user, password = cursor.fetchone()
    conn.close()
    return url, port, user, password


# Определение схемы таблицы
Base = declarative_base()


class CO2Data(Base):
    __tablename__ = "kalaturskaya"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    name = Column(String)
    year = Column(Integer)
    iso_code = Column(String)
    population = Column(Integer)
    gdp = Column(Float, nullable=True)
    cement_co2 = Column(Float)
    co2 = Column(Float, nullable=True)
    co2_per_capita = Column(Float, nullable=True)
    energy_per_capita = Column(Float, nullable=True)
    oil_co2 = Column(Float, nullable=True)
    gas_co2 = Column(Float, nullable=True)


def main():
    # Получение учётных данных
    url, port, user, password = get_postgres_creds()

    # Подключение к PostgreSQL homeworks
    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks",
        pool_recycle=3600,
    )
    # Создание таблицы по схеме
    Base.metadata.create_all(engine)
    print("Таблица создана в homeworks")

    # Загрузка данных и их запись
    data = pd.read_parquet('data.parquet').head(100)
    data.to_sql(
        name="kalaturskaya",
        con=engine,
        schema="public",
        if_exists="replace",
        index=False,
    )
    print("Данные успешно записаны!")

    # Проверка
    with engine.begin() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.kalaturskaya"))
        print(f"Записано строк: {result.fetchone()[0]}")


if __name__ == "__main__":
    main()