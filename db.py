from sqlmodel import create_engine, Session

db_url = "postgresql://postgres:1234567890@localhost:5432/fastapi"

engine = create_engine(
    db_url,
    echo=True  # Log generated SQL
)

try:
    connection = engine.connect()
    print("Connected to the database.")
    connection.close()
except Exception as e:
    print(f"Error: {str(e)}")


def get_session():
    with Session(engine) as session:
        yield session