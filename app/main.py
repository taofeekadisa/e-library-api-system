from fastapi import FastAPI
from .routes import user_routes, book_routes, borrow_routes


app =FastAPI(
    title="E-Library API System"
)

app.include_router(user_routes.router)
app.include_router(book_routes.router)
app.include_router(borrow_routes.router)