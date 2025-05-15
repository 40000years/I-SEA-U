# ใช้ Python 3.11 เป็น base image
FROM python:3.11

# ตั้งค่า environment variables เพื่อป้องกันการเขียน bytecode และให้ output ทันที
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ตั้ง working directory ใน container
WORKDIR /code

# ติดตั้ง dependencies ของระบบ (สำหรับ PostgreSQL)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# คัดลอก requirements.txt และติดตั้ง Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดไปยัง container
COPY . /code/

# รวบรวม static files
RUN python manage.py collectstatic --noinput

# เปิดพอร์ต 10000 (Render ใช้พอร์ตนี้)
EXPOSE 10000

# รัน gunicorn เพื่อให้บริการแอป
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "user_service.wsgi:application"]