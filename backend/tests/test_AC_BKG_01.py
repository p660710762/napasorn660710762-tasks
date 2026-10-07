# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from app.db.models import Booking
from tests.conftest import AUTH


def test_TC_BKG_01_1_booking_success(client, db, make_slot):
    """TC-BKG-01-1: การจองสำเร็จเมื่อมีที่นั่งว่าง 1 ที่"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then
    assert res.status_code == 201
    payload = res.json()
    assert payload["queue_no"]
    db.refresh(slot)
    assert slot.remaining == 0
    assert db.query(Booking).count() == 1


def test_TC_BKG_01_2_last_seat(client, db, make_slot):
    """TC-BKG-01-2: จองช่วงเวลาที่เหลือ 1 ที่สุดท้ายต้องลดเหลือ 0 และไม่ซ้อนคิว"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then
    assert res.status_code == 201
    payload = res.json()
    assert payload["queue_no"] == "A001"
    db.refresh(slot)
    assert slot.remaining == 0
    assert db.query(Booking).count() == 1


def test_TC_BKG_01_3_unverified_user(client, db, make_slot):
    """TC-BKG-01-3: ผู้ใช้ที่ยังไม่ยืนยันตัวตนต้องถูกปฏิเสธและไม่บันทึก"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id})

    # Then
    assert res.status_code == 401
    assert res.json()["detail"] == "ยังไม่ได้ยืนยันตัวตน"
    db.refresh(slot)
    assert slot.remaining == 1
    assert db.query(Booking).count() == 0
