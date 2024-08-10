from PyTest.db import session
from sqlalchemy.sql.expression import desc
import PyTest.tables as tables

result_1 = session.query(tables.Films.film_id, tables.Films.title).first()

result_2 = session.query(tables.Films.film_id, tables.Films.title).all()

result_3 = session.query(tables.Films.film_id, tables.Films.title).one_or_none()

result_4 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id == 180).one_or_none()

result_5 = session.query(tables.Films.film_id, tables.Films.title).filter(
    tables.Films.film_id < 150,
    tables.Films.film_id > 100
).all()

films_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 180).subquery()

result_6 = session.query(tables.Films.title).filter(tables.Films.film_id.in_(films_ids)).all()
films_order_1 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).all()
films_order_2 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(desc(tables.Films.film_id)).all()
result_7 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).limit(1).all()
result_7 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).limit(1).offset(1).all()


print(result_1)