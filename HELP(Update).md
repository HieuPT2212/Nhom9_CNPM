# Hướng Dẫn Cài Đặt và Sử Dụng - Jewelry Auction System

File này cung cấp hướng dẫn chi tiết để cài đặt, cấu hình và sử dụng hệ thống đấu giá trang sức trực tuyến **Jewelry Auction System**.

## Cài Đặt

### 1. Clone Repository

`git clone https://github.com/HieuPT2212/Nhom9_CNPM.git`

`cd Nhom9_CNPM`

### 2. Tạo và Kích Hoạt Môi Trường Ảo

Trên Windows:

Tạo môi trường ảo

`python -m venv .venv`

Kích hoạt môi trường ảo

`.venv\Scripts\activate`

Lưu ý: Nên dùng Command Prompt

Trên macOS/Linux:

`python3 -m venv .venv`

`.venv/bin/activate`

### 3. Cài Đặt Dependencies( Thư viện cần cho dự án)

`pip install -r requirements.txt`

### 4. Thiết Lập Cơ Sở Dữ Liệu

#### a. Tạo Database

1.Mở MySQL Workbench

2.Kết nối đến MySQL Server và tạo một database mới với tên jewelry_auction ( nếu lần đầu)

3.Cấu Hình settings.py

Mở file jewelry_auction/settings.py.

Cấu hình phần DATABASES để kết nối với database MySQL trên máy của bạn:

```python
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'jewelry_auction',  # Tên database

        'USER': 'your_mysql_username',  # Username MySQL của bạn

        'PASSWORD': 'your_mysql_password',  # Password MySQL của bạn

        'HOST': 'localhost',  # Hoặc IP address của MySQL server

        'PORT': '3306',  # Cổng mặc định của MySQL

    }

}
```

##### 5. Đồng bộ dữ liệu mẫu

Áp dụng các migrations đó vào database local mỗi khi thay đổi models hoặc lần đầu chạy dự án:

1.`python manage.py makemigrations`

2.`python manage.py migrate`

3.`python manage.py loaddata users.json feeconfigurations.json jewelries.json blogs.json auctions.json bids.json notifications.json` khuyến khích tự tạo.

Lưu ý: Cần cài biến môi trường cho mySQL.

Nhớ chạy makemigrations(export các models) và migrate(import các models) mỗi khi bạn thay đổi models để giữ cho database và code đồng bộ.

Lưu ý:

Thay your_password bằng thông tin đăng nhập MySQL của bạn.

Không commit mật khẩu lên repository.

### Cách Chạy Server

`python manage.py runserver`

Mở trình duyệt và truy cập địa chỉ [http://127.0.0.1:8000/] để kiểm tra.

Đăng nhập vào trang admin [http://127.0.0.1:8000/admin] với tài khoản superuser đã được tạo trong jewelry_auction_data.sql (liên hệ nhóm trưởng để biết thông tin đăng nhập).

# Hướng Dẫn Deploy Jewelry Auction System bằng Docker
 
File launch.json
    {
    "configurations": [
        {
            "name": "Docker: Python - Django",
            "type": "docker",
            "request": "launch",
            "preLaunchTask": "docker-run: debug",
            "python": {
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/app"
                    }
                ],
                "projectType": "django"
            }
        }
    ]
}

File tasks.json:
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "docker-build",
			"label": "docker-build",
			"platform": "python",
			"dockerBuild": {
				"tag": "nhom9cnpm:latest",
				"dockerfile": "${workspaceFolder}/Dockerfile",
				"context": "${workspaceFolder}",
				"pull": true
			}
		},
		{
			"type": "docker-run",
			"label": "docker-run: debug",
			"dependsOn": [
				"docker-build"
			],
			"python": {
				"args": [
					"runserver",
					"0.0.0.0:8000",
					"--nothreading",
					"--noreload"
				],
				"file": "jewelry_auction\\manage.py"
			}
		}
	]
}
Cấu hình Database trong file settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',  # Tên dịch vụ trong docker-compose
        'PORT': 5432,
    }
}
Sau đó chạy lệnh docker-compose up
