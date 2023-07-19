# Sử dụng một image cơ sở Python có sẵn
FROM python:3.9

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép các tệp tin cần thiết vào container
COPY requirements.txt .

# Cài đặt các gói phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép các tệp tin dự án vào container
COPY app.py .
COPY utils.py .
COPY config.py .
COPY views views
COPY templates templates
COPY static static

# Mở cổng 5000 để truy cập ứng dụng Flask
EXPOSE 5000

# Chạy ứng dụng Flask với Gunicorn khi container được khởi chạy
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]