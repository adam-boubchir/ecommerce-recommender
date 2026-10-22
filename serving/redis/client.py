
import os

import redis
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env à la racine du projet
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


def get_redis_client() -> redis.Redis:
    """Créer un client Redis à partir des variables d'environnement."""
    host = os.getenv("REDIS_HOST", "127.0.0.1")
    port = int(os.getenv("REDIS_PORT", "6379"))
    password = os.getenv("REDIS_PASSWORD")

    if not password:
        raise RuntimeError(
            "REDIS_PASSWORD est absent du fichier .env ou de l'environnement."
        )

    return redis.Redis(
        host=host,
        port=port,
        password=password,
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
    )
