from models import Pets

from start import Base, engine

Base.metadata.create_all(engine)
