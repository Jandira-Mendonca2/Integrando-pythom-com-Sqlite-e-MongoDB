import sqlalchemy
from sqlalchemy import declarative_base, Session
from sqlalchemy import relationship
from sqlalchemy import column, create_engine, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BINARY
from sqlalchemy import ForeignKey

Bank = declarative_base()

class Client(Bank):
    __tablename__ = " client_account"
    id = column(Integer, primary_key = True)
    name = column(String)
    cpf = column(String(9), nullable = False)
    address = column(String(9), nullabla = False)

    account = relationship(
        "Account", back_populates = "client", cascade = "all, delete-orphan"
    )
    def __repr__(self):
        return f"Client(id = {self.id}, name = {self.name}, cpf = {self.cpf}, address = {self.address})"

class Account(Bank):
    __tablename__= "account"
    id = column(BINARY, primary_key = True)
    tipo = column(String)
    agencia = column(String)
    num = column(Integer)
    id_client = column(Integer, ForeignKey("client_account.id"), nullable = False)

    client = relationship("User", back_populates = "address")

    def __repr__(self):
        return f"Account (id = {self.id}, tipo = {self.tipo}, agencia = {self.agencia}, num = {self.num})"

print(Client.__tablename__)
print(Account.__tablename__)

engine = create_engine("sqlite://")

base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("client_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    ana = Client(
        id= 1,
        name = "Ana",
        cpf = "012345678",
        address = "Lubango",
        account = [Account(tipo = "Poupança", agencia = "Sol", num = 345)]
    )

    session.add_all([ana])
    session.commit()

stmt = select(Client).where(Client.name.in_(["ana"]))
print("Recuperando usuários apartir de condição de filtragem: ")
for client in session.scalars(stmt):
    print(client)

stmt_account = select(Account).where(Account.client_id.in_([4]))
print("\nRecuperando conta: ")
for account in session.scalars(stmt_account):
    print(account)


