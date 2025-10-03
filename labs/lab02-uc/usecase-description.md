# Use Case Description – Hệ thống quản lý đặt phòng khách sạn

## 🎯 Tổng quan
Hệ thống hỗ trợ các chức năng chính như tìm kiếm, đặt phòng, thanh toán, quản lý phòng và nhân sự. Các tác nhân gồm:
- **Khách hàng (Customer)**: Tìm phòng, đặt/hủy phòng, thanh toán.
- **Lễ tân (Receptionist)**: Quản lý đặt phòng, check-in/check-out, tạo hóa đơn.
- **Quản lý (Manager)**: Xem báo cáo, quản lý nhân viên và giá phòng.

---

## 🛏️ Use Case: Đặt phòng (Make a Reservation)
- **Tác nhân**: Khách hàng  
- **Mô tả**: Khách tìm phòng trống, nhập thông tin, chọn phòng và xác nhận đặt.  
- **Luồng chính**:
  1. Truy cập hệ thống
  2. Nhập thông tin tìm kiếm
  3. Chọn phòng và nhập thông tin cá nhân
  4. Nhận mã đặt phòng và email xác nhận  
- **Luồng thay thế**:
  - A1: Không có phòng → gợi ý khác
  - A2: Thông tin sai → yêu cầu nhập lại

---

## 🛎️ Use Case: Check-in/Check-out
- **Tác nhân**: Lễ tân  
- **Mô tả**: Thực hiện nhận/trả phòng cho khách.  
- **Luồng chính**:
  1. Khách cung cấp mã đặt phòng
  2. Tra cứu và xác nhận thông tin
  3. Check-in: cập nhật trạng thái