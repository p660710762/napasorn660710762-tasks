# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v3 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08.54 | test: 6 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (วัดเฉพาะประสิทธิภาพ ไม่ตรวจแสดงผลหรือจำนวนที่นั่ง) | T-02 เสร็จ; T-10 พร้อมทำ | `backend/app/slots/router.py:get_slots`; `backend/app/slots/service.py:list_available_slots` (30 วัน) | `test_AC_BKG_05` ผ่าน แต่ไม่ตรวจการแสดงผล/จำนวนที่นั่ง; เรียกแบบ sequential | ช่องโหว่ — F-06, F-09 |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่พบการปฏิเสธจองซ้ำใน `backend/app/booking/service.py:create_booking` | ไม่มี test ของ AC-BKG-02 | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 พร้อมทำ | ไม่พบการเสนอช่วงใกล้เคียงในโค้ดปัจจุบัน | ไม่มี test ของ AC-BKG-03 | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ; T-06 รอ Q-02; การส่งข้อความอยู่ใน T-07 พร้อมทำ | `backend/app/booking/router.py:create_booking`; `backend/app/booking/service.py:create_booking`; `queue_no=None` รอ Q-02 | `test_TC_BKG_01_1_booking_success`, `test_TC_BKG_01_2_last_seat`, `test_TC_BKG_01_3_unverified_user` ผ่าน; หมายเลขคิวและการแสดงผลยังรอ Q-02; ไม่มีการตรวจส่งข้อความ | ยังไม่ถึง |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่พบ GET รายละเอียดการจอง, การแจ้งเตือน หรือคิวส่งซ้ำในโค้ดปัจจุบัน | ไม่มี test ของ AC-BKG-04 | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC ที่ตรวจการเปลี่ยนแพ็กเกจ | T-02 เสร็จ (กรอง API); T-10 พร้อมทำ (หน้าจอ) | `backend/app/slots/service.py:list_available_slots` กรองตาม `package_code`; ไม่มีหน้าจอเปลี่ยนแพ็กเกจ | `test_AC_BKG_05` ผ่านแต่ไม่ตรวจการเปลี่ยนแพ็กเกจ | ช่องโหว่ — F-07 |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ (ทดสอบแบบย่อส่วน) | `backend/app/slots/router.py:get_slots` | `test_AC_BKG_05` ผ่านแบบเรียกตามลำดับ ไม่ได้จำลองผู้ใช้พร้อมกัน 200 คน | ช่องโหว่ — F-09 |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่พบการตั้งค่า TLS ใน `backend/app/` หรือ `frontend/src/`; deployment TLS ยังไม่ได้ตรวจ | ไม่มี test | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่พบกลไกส่งซ้ำในโค้ดปัจจุบัน | ไม่มี test ของ AC-BKG-04 | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่พบการทดสอบกับผู้ใช้ใหม่ 10 คน | ไม่มี test | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 เสร็จ | `backend/app/config.py:DATABASE_URL`, `backend/app/db/session.py:engine`; ใช้ PostgreSQL ได้เมื่อกำหนด `DATABASE_URL` | `test_T01_tables_created`, `test_T01_no_national_id` ผ่านบน SQLite ตามแผนทดสอบ | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จเฉพาะตาราง; T-08 พร้อมทำ | `backend/app/db/models.py:AuditLog`; ไม่พบ middleware บันทึก audit log หรือกลไกเก็บอย่างน้อย 1 ปี | ไม่มี test ของ AC-BKG-06 | ยังไม่ถึง |
| IF-IDP-01 | AC-BKG-01 ใช้ precondition ที่ผ่านเข้าทาง mock | T-03 เสร็จ | `backend/app/auth/idp.py:get_verified_hn` ตรวจเพียง prefix จำลอง ไม่เรียก/ตรวจผลจากระบบ IDP จริง | test AC-BKG-01 ตรวจกรณีไม่มี token แล้วผ่าน แต่ไม่ได้ทดสอบการยืนยันกับ IDP | ช่องโหว่ — F-03 |
| IF-HIS-01 | ไม่มี AC | T-01 เสร็จเฉพาะ schema; T-09 พร้อมทำ | `backend/app/db/models.py:Booking` เก็บ HN และไม่มีคอลัมน์ `national_id`; ไม่พบ client/endpoint สำหรับ HIS; request/log ไม่รับหรือเขียน `national_id` แล้ว | `test_T01_no_national_id` ผ่านแต่ไม่ครอบคลุม HIS | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 พร้อมทำ | ไม่พบระบบส่งข้อความแบบ asynchronous ในโค้ดปัจจุบัน | ไม่มี test ของ AC-BKG-04 | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| `backend/app/main.py:lifespan`, `app` | CON-TECH-01 | บางส่วน | สร้าง schema และรวม routers; ไม่ติดตั้ง audit middleware |
| `GET /slots` (`backend/app/slots/router.py:get_slots`) | FR-BKG-01, FR-BKG-06 | บางส่วน | ส่งวัน เวลา และ remaining; ไม่มีหน้าจอแสดงผลตาม requirement |
| `backend/app/slots/service.py:list_available_slots` | FR-BKG-01, FR-BKG-06 | บางส่วน | กรอง package และ remaining; จำกัดช่วงล่วงหน้า 30 วันตาม FR-BKG-01 |
| `POST /bookings` (`backend/app/booking/router.py:create_booking`) | FR-BKG-04, IF-IDP-01, IF-HIS-01 | ไม่ตรงทั้งหมด | สร้าง booking; dependency เป็น mock IDP; ไม่รับหรือ log `national_id`; `queue_no` เว้นว่างรอ Q-02 |
| `DELETE /bookings/{id}` | ไม่มี | ไม่มี endpoint แล้ว | endpoint สำหรับยกเลิกที่อยู่นอกขอบเขตถูกนำออกเพื่อแก้ F-01 |
| `backend/app/booking/service.py:create_booking` | FR-BKG-04 | บางส่วน | ตัดที่นั่งและบันทึก; ไม่ส่งคำขอข้อความยืนยัน |
| `backend/app/booking/service.py:create_booking` | FR-BKG-04, Q-02 | บางส่วน | บันทึกการจองและตัดที่นั่ง; ไม่สร้างหมายเลขคิวจนกว่า Q-02 จะได้คำตอบ |
| `backend/app/auth/idp.py:get_verified_hn` | IF-IDP-01 | ไม่ตรงทั้งหมด | ตรวจ string prefix ที่กำหนดไว้ ไม่ได้ตรวจผลจากระบบยืนยันตัวตนจริง |
| `backend/app/db/models.py:Slot`, `Booking`, `AuditLog` | FR-BKG-01, FR-BKG-02, FR-BKG-04, IF-HIS-01, DOM-PDPA-01 | บางส่วน | โครงสร้างข้อมูลรองรับบาง requirement; ไม่มีข้อจำกัด unique การจองต่อคนต่อวันหรือการเก็บ audit อย่างน้อย 1 ปี |
| `backend/app/db/migrations/001_init.py:upgrade` | CON-TECH-01, DOM-PDPA-01, IF-HIS-01 | บางส่วน | สร้างตารางตาม model; การทดสอบใช้ SQLite |
| `backend/app/config.py:DATABASE_URL`, `backend/app/db/session.py:engine`, `get_db` | CON-TECH-01 | บางส่วน | อ่าน URL จาก environment แต่ fallback เป็น SQLite |
| `frontend/src/api/client.js:api.getSlots` | FR-BKG-01, FR-BKG-06 | บางส่วน | เรียก API ค้นช่วงเวลา; ไม่มีหน้าจอที่ใช้เลือก/แสดงผล |
| `frontend/src/api/client.js:api.createBooking` | FR-BKG-04, IF-IDP-01 | ไม่ครบ | ส่งคำขอจองโดยไม่ส่ง Authorization header; ยังไม่มี UI ที่ใช้ client นี้ |
| `frontend/src/App.jsx:App` | ไม่มี | ไม่ครบ | เป็นเพียงโครงหน้าจอ ไม่มีการเลือกแพ็กเกจ จอง หรือแสดงผล |
| `frontend/src/main.jsx` | ไม่มี | ตรงในฐานะ entry point | mount แอป React ตามโครง frontend |
| `backend/tests/test_AC_BKG_01.py:test_TC_BKG_01_1_booking_success`, `test_TC_BKG_01_2_last_seat`, `test_TC_BKG_01_3_unverified_user` | AC-BKG-01 | บางส่วน | ตรวจ response, การบันทึก, remaining และกรณีไม่ยืนยัน; การตรวจค่าหมายเลขคิวถูกคอมเมนต์รอ Q-02; ไม่มี UI assert |
| `backend/tests/test_AC_BKG_05.py:test_AC_BKG_05` | AC-BKG-05, NFR-PERF-01 | ไม่ครบ | เรียก request 200 ครั้งแบบ sequential จึงไม่แทนผู้ใช้พร้อมกัน 200 คน |
| `backend/tests/test_T01_schema.py:test_T01_tables_created`, `test_T01_no_national_id` | CON-TECH-01, DOM-PDPA-01, IF-HIS-01 | บางส่วน | ยืนยันตารางและการไม่มี national_id ในตาราง bookings เท่านั้น |
| `frontend/src/__tests__/setup.test.jsx` | ไม่มี AC | ไม่เกี่ยวกับ AC | ตรวจเพียงว่าโครงหน้าจอเปิดและมีหัวเรื่อง |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | กอง | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|---|
| F-03 | จริง | ละเมิด Constraint | `backend/app/auth/idp.py:get_verified_hn` | IF-IDP-01 | ยอมรับ Authorization ที่ขึ้นต้นด้วย prefix จำลองแล้วใช้ suffix เป็น HN โดยไม่รับ/ตรวจผลยืนยันจากระบบ IDP | |
| F-06 | จริง | FR ไม่มี AC | `specs/001-booking/spec.md:AC-BKG-05` | FR-BKG-01 | AC-BKG-05 ตรวจเพียง p95 ไม่ตรวจการแสดงช่วงเวลาว่างและจำนวนที่นั่งตาม FR-BKG-01 | |
| F-07 | จริง | FR ไม่มี AC | `specs/001-booking/spec.md:FR-BKG-06` | FR-BKG-06 | ไม่มี AC สำหรับการเปลี่ยนแพ็กเกจและคำนวณช่วงเวลาว่างใหม่; Q-04 เพิ่มคำถามเพื่อให้ทีมกำหนดเกณฑ์ ยังไม่มี AC ใหม่ | |
| F-08 | AI เข้าใจผิด | ข้อสรุปเกินหลักฐาน | `backend/app/`, `frontend/src/`, deployment | NFR-SEC-01 | ไม่พบ TLS configuration ใน source แต่ยังไม่ตรวจ deployment; ไม่อาจสรุปจาก source อย่างเดียวว่า TLS ใช้ไม่ได้ | |
| F-09 | จริง | test อ่อน | `backend/tests/test_AC_BKG_05.py:test_AC_BKG_05` | AC-BKG-05, NFR-PERF-01 | 200 request ถูกส่งทีละรายการ ไม่ได้จำลองผู้ใช้พร้อมกัน 200 คนตาม Given; ผลผ่านไม่ยืนยัน threshold ในภาวะโหลดที่กำหนด | |
| F-10 | ยังไม่ถึง | ยังไม่มี task/test ครอบคลุม | `specs/001-booking/spec.md:NFR-USE-01`; ไม่มี task ที่เกี่ยวข้อง | NFR-USE-01 | ยังไม่พบ task หรือการทดสอบกับผู้ใช้ใหม่ 10 คนเพื่อวัดเวลา 3 นาทีและอัตราสำเร็จ 8 ใน 10 คน | |
| F-11 | ยังไม่ถึง | รอ Q-02 | `backend/tests/test_AC_BKG_01.py:test_TC_BKG_01_1_booking_success`, `test_TC_BKG_01_2_last_seat`; T-06 | AC-BKG-01, FR-BKG-04 | ยังไม่มี UI test ยืนยันการแสดงหมายเลขคิว; T-06 รอ Q-02 ก่อนสร้างหน้าจอ และ assertions หมายเลขคิวถูกคอมเมนต์รอคำตอบ | |

สรุปการทบทวน: **ยืนยันแล้วยังเปิด** F-03, F-06, F-07, F-09; **ยังไม่ถึง/รอคำตอบ** F-10, F-11; **AI เข้าใจผิดหรือสรุปเกินหลักฐาน** F-08. F-01, F-02, F-04, F-05 ปิดแล้วและย้ายไปหัวข้อ 4. ช่องโหว่ระดับ spec ที่ยังยืนยันคือ FR-BKG-01 มีเพียง AC ความเร็ว (F-06) และ FR-BKG-06 ไม่มี AC (F-07).

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร | ทีมตัดสิน |
|---|---|---|---|
| F-01 | ลบ endpoint `DELETE /bookings/{id}` และ service ยกเลิก/คืนที่นั่งออก | ตรวจ router/service หลังแก้และ `pytest -v` ผ่าน 6 tests; ไม่มี endpoint ยกเลิกในโค้ด | |
| F-02 | เอา `national_id` ออกจาก request model และข้อความ application log | ตรวจ source `backend/app/booking/router.py` แล้วไม่รับ/ไม่ log ข้อมูลนี้; Q-03 เปิดไว้ถามนโยบายเพิ่มเติม | |
| F-04 | ลบ `next_queue_no` และไม่กำหนดรูปแบบ/วิธีนับ โดยเก็บ `queue_no=None` รอ Q-02 | ตรวจ service ไม่มี `A001` หรือการนับรายวัน; test assertions ถูกคอมเมนต์รอ Q-02; `pytest -v` ผ่าน 6 tests | |
| F-05 | เปลี่ยน `DAYS_AHEAD` จาก 14 เป็น 30 ตาม FR-BKG-01 | ตรวจ `backend/app/slots/service.py`; `pytest -v` ผ่าน 6 tests | |
| F-08 | ถอนข้อสรุปว่า NFR-SEC-01 ถูกละเมิด เพราะ source code อย่างเดียวไม่ยืนยัน TLS ที่ deployment | จัดเป็น AI เข้าใจผิด/สรุปเกินหลักฐาน; การตั้งค่า deployment ยังต้องตรวจ | |
