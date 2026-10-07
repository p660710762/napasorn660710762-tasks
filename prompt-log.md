# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 08.15 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- โหมด: ร่าง (ยังไม่มีแถวใน test-cases.md ที่มีสถานะ "ใช้ได้" สำหรับ AC-BKG-01)
- TC ID ที่เสนอ: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- ผลลัพธ์: เพิ่ม 3 แถวร่างใน specs/001-booking/test-cases.md โดยยึดจาก spec.md และ plan.md ข้อ 4 / 6
- ไม่มีการเขียนโค้ด test เนื่องจากยังไม่เปลี่ยนสถานะเป็น "ใช้ได้"
- ต้องตรวจแถวในตาราง แก้ได้ตามต้องการ แล้วเปลี่ยนสถานะเป็น "ใช้ได้" ก่อน จากนั้นสั่ง /testcases อีกครั้ง

---

## 2569-10-07 08.25 คำสั่ง: เปลี่ยนสถานะ TC-BKG-01-* จาก "ร่าง" เป็น "ใช้ได้" และเขียนโค้ด test ตามแถวที่ตรวจแล้ว

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- โหมด: เขียน test
- TC ID ที่ใช้งาน: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- ผลลัพธ์: อัปเดตสถานะเป็น "ใช้ได้" ใน specs/001-booking/test-cases.md และเพิ่ม test 3 ตัวลง backend/tests/test_AC_BKG_01.py
- รันผล: `cd backend && pytest -q tests/test_AC_BKG_01.py`

---

## 2569-10-07 08.28 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- โหมด: เขียน test จากแถวสถานะ "ใช้ได้"
- TC ID: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3 (มี test หลังบ้านอยู่ครบแล้ว)
- ปรับ test_TC_BKG_01_2_last_seat ให้ตรวจว่ามีหมายเลขคิวและตรงกับค่าที่บันทึก แทนการกำหนดรูปแบบ A001 ซึ่งยังรอ Q-02
- ผลทดสอบหลังบ้าน: `cd backend && pytest -v` — 6 passed, 1 warning
- ผลทดสอบหน้าจอ: `cd frontend && npm test` — 1 passed (มีเฉพาะ setup test; ยังไม่มี AC-BKG-01 UI test เพราะ T-06 รอ Q-02 และยังไม่มี BookingResult)

---

## 2569-10-07 08.32 คำสั่ง: /verify specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ตรวจโค้ดทุกไฟล์ที่มีใน `backend/app/`, `frontend/src/`, `backend/tests/` และ `frontend/src/__tests__/` เทียบกับ spec, plan, tasks และ test cases
- ผลทดสอบ: `cd backend && pytest -v` — 6 passed, 0 failed, 1 warning; ไม่รัน Vitest เพราะมีเพียง setup test ไม่มี test หน้าจอนอกจาก setup
- ผลตามรอยไปข้างหน้า: 15 ID — ครบ 1, ยังไม่ถึง 6, รอ 0, ช่องโหว่ 8
- ข้อค้นพบใหม่: F-01 ถึง F-11 ใน `specs/001-booking/rtm.md`
- สร้าง RTM; ไม่แก้ spec, plan, tasks, test หรือโค้ดระบบ

---

## 2569-10-07 08.38 คำสั่ง: ทบทวนข้อค้นพบ /verify และแยก จริง / ยังไม่ถึง / AI เข้าใจผิด

- ตรวจ `specs/001-booking/rtm.md` ทีละแถวในหัวข้อ 3 และเทียบกับ spec/task
- จัดกอง: จริง F-01, F-03, F-04, F-05, F-06, F-07, F-09; ยังไม่ถึง F-10, F-11; AI เข้าใจผิดหรือสรุปเกินหลักฐาน F-02, F-08
- แก้ F-01 เป็นชนิด "อ้าง ID ผิดเรื่อง": DELETE ยกเลิกคิวอ้าง FR-BKG-04 ซึ่งพูดถึงการยืนยันจอง และขัดกับ Out of scope
- ยืนยันช่องโหว่ spec ที่ระบุ: FR-BKG-01 มี AC-BKG-05 ตรวจเฉพาะความเร็ว (F-06); FR-BKG-06 ไม่มี AC (F-07)
- รัน `git restore -- backend/tests/test_AC_BKG_01.py` ตามคำสั่งตรวจสถานะ; หลังคำสั่ง `git status --short` ไม่พบไฟล์ใน `backend/app/`, `backend/tests/` หรือ `frontend/src/` ที่เปลี่ยน จึงไม่มี diff ของระบบ/test ที่เหลือให้คืน
- ไม่ได้รัน test ซ้ำ เพราะรอบนี้เป็นการทบทวนและจัดประเภท RTM เท่านั้น

---

## 2569-10-07 08.44 แก้ข้อค้นพบ F-01

- คำสั่ง: ปิดข้อค้นพบทีละข้อจาก /verify
- แก้เฉพาะ `backend/app/booking/router.py` และ `backend/app/booking/service.py`: นำ endpoint/service สำหรับยกเลิกการจองที่อยู่ใน Out of scope ออก
- ผล `cd backend && pytest -v`: 6 passed, 0 failed; 1 warning จาก Starlette/httpx

---

## 2569-10-07 08.46 แก้ข้อค้นพบ F-05

- คำสั่ง: ปิดข้อค้นพบทีละข้อจาก /verify
- แก้เฉพาะ `backend/app/slots/service.py`: เปลี่ยนช่วงค้นหาจาก 14 วันเป็น 30 วันตาม FR-BKG-01
- ผล `cd backend && pytest -v`: 6 passed, 0 failed; 1 warning จาก Starlette/httpx

---

## 2569-10-07 08.48 แก้ข้อค้นพบ F-04

- คำสั่ง: ปิดข้อค้นพบทีละข้อจาก /verify
- แก้เฉพาะ `backend/app/booking/service.py`: งดสร้างรูปแบบหมายเลขคิวที่ยังรอ Q-02 และเก็บ `queue_no` เป็นค่าว่าง
- ผลครั้งแรก `cd backend && pytest -v`: 2 failed เพราะ test เดิมยืนยันว่าต้องมี queue_no และต้องเป็น A001
- ตามคำสั่งเฉพาะกรณี เปลี่ยน assertion เลขคิวใน test_TC_BKG_01_1 และ test_TC_BKG_01_2 เป็นคอมเมนต์ "รอ Q-02" เท่านั้น ไม่เปลี่ยน assertion ส่วนอื่น
- ผลหลังปรับ: `cd backend && pytest -v` — 6 passed, 0 failed; 1 warning จาก Starlette/httpx
