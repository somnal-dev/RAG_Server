import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import routers
from app.config.server import serverConfig

# 서버 실행
app = FastAPI()

# CORS 설정 - 앱 생성 직후
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 사용
for router in routers:
    app.include_router(router)

# 서버실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=serverConfig.HOST, port=serverConfig.PORT)