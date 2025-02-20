# Sử dụng Python base image
FROM python:3.13-slim
# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser
# Đặt thư mục làm việc
WORKDIR /app

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy tệp yêu cầu và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn dự án
COPY . .

# Expose cổng 8000
EXPOSE 8000

# Chạy lệnh khởi động server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
