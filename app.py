from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence, select

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('name', String(50)),
    Column('age', Integer)
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String(50), nullable=False)
)

metadata.create_all(engine)

ins = users.insert().values(name='jasper', age=26)
ins2 = users.insert().values(name='damares', age=30)
ins.compile().params

conn = engine.connect()
result = conn.execute(ins)
result = conn.execute(ins2)
s = select([users])
result = conn.execute(s)
for r in result:
    print(r)
