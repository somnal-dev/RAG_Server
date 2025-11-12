FROM python:3.11

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# 프로덕션 서버 (reload 없음)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]