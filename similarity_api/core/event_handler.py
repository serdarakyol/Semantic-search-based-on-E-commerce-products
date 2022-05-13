from typing import Callable

from fastapi import FastAPI
from loguru import logger
from pathlib import Path

from similarity_api.utils.utils import load_data, load_model

ROOT_DIR = str(Path(__file__).parent.parent)

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        app.state.model = load_model(ROOT_DIR + "/models/den_hepsi_burada_word2vec.model")
        app.state.product = load_data(ROOT_DIR + "/data/final_products.pkl")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        del app.state.model
        del app.state.product

    return shutdown
