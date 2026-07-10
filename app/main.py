
from fastapi import FastAPI

from app.database.database import engine
from app.models import user, service
from app.routes import auth, user as user_routes, service as service_routes

# create all database tables
user.Base.metadata.create_all(bind=engine)
service.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user_routes.router)
app.include_router(service_routes.router)