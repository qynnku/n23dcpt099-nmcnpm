# 🏦 Final Report – Mini Project ATM

## 📌 Giới thiệu
Mini Project **ATM** được thực hiện xuyên suốt từ **Lab 01 → Lab 09** trong môn *Nhập môn Công nghệ Phần mềm*.  
Mục tiêu: áp dụng quy trình phát triển phần mềm từ phân tích, thiết kế, lập trình, kiểm thử, đến quản lý dự án bằng Agile/Scrum.  

Các chức năng chính của hệ thống:
- Đăng nhập bằng username & password (Form Login).
- Xác thực PIN và thực hiện **rút tiền**.
- Quản lý thông tin người dùng, tài khoản và giao dịch trong cơ sở dữ liệu.
- Kiểm thử tự động (Unit test & Integration test).
- Theo dõi tiến độ dự án bằng Jira.  

---

## 📌 Artifacts  

- [Use Case (Lab 02)](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab02-uc/LAB02.png)  
- [Sequence Diagram (Lab 03)](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab03-atm-diagrams/LAB03-SQ-ATM.png)  
- [Class Diagram (Lab 06)](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab06-atm-class/classdiagram-lab06.png)  
- [ERD (Lab 05)](https://drive.google.com/file/d/1C81uyR2nvn19kXrmfrY8MOVtBv293qrE/view?usp=drive_link)  
- [Database Script (Lab 05)](https://drive.google.com/file/d/1gjPwdEC-PpjKl6zRTxsOCjYPL2sDNRcb/view?usp=drive_link)  
- [Form Login (Lab 04)](https://github.com/KhangD23PTIT/NMCNPM/tree/main/labs/lab04-form-login)  
- [Withdraw Module (Lab 07)](https://drive.google.com/drive/folders/1haYaKiuJ6EwMQiPjjHxdITR_FdgFRWNA?usp=drive_link)  
- [Test (Lab 08)](https://github.com/KhangD23PTIT/NMCNPM/tree/main/labs/lab08-testing)  
- [Jira Report (Lab 09)](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab09.pdf)  

---

## 📌 Mô hình UML
1. Use Case Diagram: ![Use Case](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab02-uc/LAB02.png)  
2. Sequence Diagram: ![Sequence](https://github.com/KhangD23PTIT/NMCNPM/blob/main/labs/lab03-atm-diagrams/LAB03-SQ-ATM.png)
3. **Class Diagram**: các lớp chính gồm `ATM`, `Card`, `Account`, `Transaction`.  
4. **Package Diagram**: chia hệ thống thành UI, Controller, BankService, Hardware.  

---

## 📌 Database & Code minh hoạ
- **ERD**: mô tả quan hệ giữa `Users`, `Cards`, `Accounts`, `Transactions`.  
- **Database Script**: tạo bảng và dữ liệu mẫu để test.  
- **Code đã triển khai**:  
  - `form-login`: giao diện đăng nhập bằng HTML/CSS/JS.  
  - `withdraw`: module Python kết nối MySQL, xử lý rút tiền.  

---

## 📌 Kết quả Test & Sprint Report
- **Unit Test**: kiểm tra hàm `verify_pin()` và `withdraw()`.  
  - Case PIN đúng/sai.  
  - Case đủ tiền/không đủ tiền.  
- **Integration Test**: dùng Selenium test form login (login đúng/sai, input rỗng).  
- **Kết quả**: chạy pass tất cả test case cơ bản.  
- **Jira Sprint Report**:  
  - Epic: ATM Basic Functions.  
  - Sprint 1: Rút tiền + Xem số dư.  
  - Evidence: backlog, board, burndown chart.  

---

## 📌 Kết luận & Định hướng mở rộng
- Dự án ATM mini đã tích hợp đầy đủ từ phân tích đến lập trình, kiểm thử và quản lý.  
- Hệ thống demo chạy được: **Form Login → Rút tiền → Lưu giao dịch DB**.  
- Jira board thể hiện tiến độ nhóm và sprint report.  

👉 **Định hướng mở rộng**:  
- Thêm chức năng chuyển khoản, đổi PIN, truy vấn số dư.  
- Hoàn thiện UI/UX với framework hiện đại.  
- Nâng cao bảo mật: mã hóa mật khẩu, xác thực 2 lớp.  

---

## 📎 Nộp bài
- **GitHub repo**: [điền link repo của bạn]  
---
