from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://username:psasword@host/DB_NAME')
if engine:
    print("Conexão realizada com sucesso")


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    
    items = relationship("Item", back_populates="user")

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="items")

Base.metadata.create_all(engine)

# sessão de trabalho
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Adicionar um novo usuário
new_user = User(name='Alice')
session.add(new_user)
session.commit()

# Consultas
# Obter todos os usuários
users = session.query(User).all()


# Filtrar usuários por nome
user = session.query(User).filter_by(name='Alice').first()
print(user.name)

# inserindo itens para o usuário
item1 = Item(name='maçã', user=user)
session.add(item1)
session.commit()

# Consultando itens do usuário
user = session.query(User).filter_by(name='Alice').first()
for item in user.items:
    print(f'{item.name}')
