import uvicorn

from api.main import app
from bot.main import dp

if __name__ == '__main__':
    dp.stop_polling()
    uvicorn.run(app, port=8000)
