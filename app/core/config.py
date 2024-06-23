from decouple import config

SQLALCHEMY_DATABASE_URL = config("DATABASE_URL")
FRONTEND_URL = config("FRONTEND_URL")
JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = config("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = config("JWT_REFRESH_TOKEN_EXPIRE_MINUTES")
