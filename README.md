# Jewelry Auction System - Nhom9_CNPM

Đây là repository cho dự án đấu giá trang sức trực tuyến của nhóm 9 môn Công Nghệ Phần Mềm.

## Mô Tả

Hệ thống cho phép người dùng (bao gồm Khách - Guest, Thành viên - Member, Nhân viên - Staff, Quản lý - Manager và Quản trị viên - Admin) tham gia đấu giá trang sức trực tuyến.
## Thành Viên Nhóm
( PTHiếu Update)
## Công Nghệ Sử Dụng
*   Python 3.9+
*   Django 4.2.1
*   MySQL
*   HTML, CSS, JavaScript
*   Git, GitHub
## Hướng Dẫn Sử Dụng
### Guest (Khách)
* Có thể xem danh sách trang sức đang đấu giá.

* Có thể xem chi tiết từng trang sức.

* Có thể xem các bài viết trên blog.

* Không thể tham gia đấu giá hay đăng bán trang sức.

### Member (Thành Viên)
* Có thể đăng ký tài khoản và đăng nhập.

#### Người Mua (Buyer):

* Đăng ký tham gia các phiên đấu giá.

* Đặt giá thầu cho các trang sức.

* Theo dõi trạng thái đấu giá.

* Thanh toán khi thắng đấu giá.
 
* Xem lịch sử đấu giá.

#### Người Bán (Seller):

* Gửi yêu cầu đăng ký trang sức để đấu giá.

* Nhận thông báo định giá.

* Xác nhận đồng ý/không đồng ý đấu giá.

* Xem lịch sử đấu giá của trang sức đã đăng ký.

* Chỉnh sửa thông tin cá nhân trong hồ sơ.

#### Staff (Nhân Viên)
* Tiếp nhận và xử lý yêu cầu đăng ký trang sức.

* Thực hiện định giá sơ bộ.

* Liên hệ với người bán để yêu cầu gửi trang sức.

* Xác nhận đã nhận trang sức.

* Gửi định giá cuối cùng cho Quản Lý.

* Hỗ trợ người mua và người bán.

* Bàn giao trang sức cho người mua.

#### Manager (Quản Lý)
* Phê duyệt định giá cuối cùng.

* Chọn phiên đấu giá cho trang sức.

* Tạo, chỉnh sửa, xóa phiên đấu giá.

* Phân công nhân viên phụ trách phiên đấu giá.

* Giám sát các phiên đấu giá.

* Quản lý tài khoản nhân viên.

* Xem báo cáo thống kê.

#### Admin (Quản Trị Viên)
* Quản lý tất cả các tài khoản (Member, Staff, Manager).

* Cấu hình hệ thống.

* Quản lý phí giao dịch.

* Quản lý tiền tệ (JCoin).

* Sao lưu và phục hồi dữ liệu.

* Có đầy đủ chức năng của các vai trò khác.

## Quy Trình Làm Việc

*   Sử dụng Git để quản lý mã nguồn.
*   Tạo branch mới cho mỗi tính năng hoặc bug fix: `git checkout -b <tên_branch>`.
*   Commit code thường xuyên với message rõ ràng: `git commit -m "Mô tả commit"`.
*   Tạo Pull Request khi hoàn thành tính năng hoặc bug fix để review code.
*   Merge code vào branch `main` (hoặc `develop` tùy quy định của nhóm) sau khi được review và approve.

## Liên Hệ

*   Nếu gặp lỗi hoặc có thắc mắc, hãy liên hệ với nhóm trưởng: Phan Thanh Hiếu
## Hướng Dẫn Cài Đặt và Sử Dụng

Xem chi tiết tại file [HELP.md](HELP.md).

## License
Xem chi tiết tại file [License.txt](License.txt).
