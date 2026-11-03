# Pick a job. Give Copilot a clear finish line.

เปิดโปรเจกต์ Agent จริงใน VS Code แล้วใช้ prompt ที่ตรงกับงาน ไม่ต้องเรียกทุก skill
พร้อมกัน ทุกตัวอย่างด้านล่างเป็นคำสั่งให้ผู้ช่วยพัฒนา ไม่ใช่ข้อความใส่ใน Agent runtime

## 1. สร้าง Standard Agent ชิ้นแรก

ต้องมี workspace ที่ clone ผ่านวิธีที่รองรับ หากยังไม่มี ให้ Copilot ช่วยตรวจ prerequisites
และ clone Agent ที่มีสิทธิ์ก่อน อย่าให้สร้าง connection IDs ขึ้นเอง

```text
ใช้ copilot-studio-builder และเส้นทาง Standard
ตรวจ workspace และเครื่องมือที่ติดตั้งก่อนแก้
สร้าง topic รับคำขอบริการ: ประเภทคำขอ รายละเอียด และหน้าสรุปให้ผู้ใช้ยืนยัน
รอบแรกใช้ synthetic input และไม่เรียก connector
ตรวจด้วย local preflight และ native diagnostics ที่ใช้ได้จริง
แสดง diff แล้วระบุขั้นตอน sync และทดสอบบนเว็บให้ครบ
สำเร็จเมื่อคุยได้หนึ่งเส้นทาง พร้อมกรณีผู้ใช้ให้ข้อมูลไม่ครบ
```

## 2. สร้าง Agent บน Microsoft Copilot harness

ต้องมี PAC CLI 2.9.3+ ตาม plugin พร้อม auth, environment และสิทธิ์จริง ใช้ path ว่าง
สำหรับการสร้างใหม่ `init` อาจสร้าง cloud resources ทันที ไม่ใช่แค่ไฟล์ local

```text
ใช้ copilot-studio-builder แล้วเลือก copilot-studio-agentic
เป้าหมาย: ช่วยอ่านบันทึกประชุมสังเคราะห์และจัดทำ action brief
ตรวจ PAC version/help, auth และความพร้อมของ harness ก่อนสร้าง
ใช้ environment และ workspace ที่ฉันระบุ; ถ้ายังขาดให้ถามเฉพาะข้อมูลที่จำเป็น
อ่าน create-agent และ architect ต้นฉบับก่อนลงมือ
สร้าง procedure ที่แยก action, owner ที่มีหลักฐาน และข้อมูลที่ยังไม่ทราบ
ห้ามเดาอีเมลบุคคลหรือวันครบกำหนด และยังไม่ส่งข้อความหรือสร้างรายการจริง
ตรวจและ sync ด้วยวิธีที่รองรับ แล้วรายงานสิ่งที่ทดสอบได้จริง
```

## 3. Debug: flow แจ้งสำเร็จแต่ข้อมูลไม่เปลี่ยน

```text
ใช้ copilot-studio-builder ตรวจ topic/tool และ flow ที่เกี่ยวข้อง
อาการ: ผู้ใช้เห็นข้อความว่าสำเร็จ แต่ record ไม่ถูกแก้
เริ่มจาก failing input และ run evidence ที่ฉันให้
ตรวจ zero-result, multiple matches, loop ที่ไม่รัน และ success flag
แก้ให้ status สะท้อนผลจริง พร้อมกรณี not_found, failed และ partial success
ตรวจ diff และทดสอบโดยไม่ replay งานเขียน/ส่งข้อความโดยไม่ดูผลข้างเคียงก่อน
```

## 4. เตรียม hackathon

```text
ใช้ PurpleBelt ผ่าน copilot-studio-builder
เวลาเหลือ 6 ชั่วโมง ทีม 3 คน เป้าหมายคือ [ผลลัพธ์ที่ผู้ใช้ต้องได้]
ตรวจ rubric, harness, channel, connector, DLP และ capacity ก่อนเลือกทางทำ
เขียน demo story แล้วเลือกหนึ่ง journey ที่ทำจบได้จริง
แบ่งงานตาม data/tool contracts และกำหนดคนดูแล cloud sync
ทำ happy path + failure path ก่อนเพิ่มฟีเจอร์
รายงาน accuracy, latency หรือ manual steps เฉพาะที่วัดได้
เก็บ demo recording และระบุ simulated data ให้ชัด
```

## 5. ประเมินการย้าย harness

```text
ใช้ copilot-studio-builder อ่าน source agent แบบ read-only ก่อน
ตรวจว่ามีประโยชน์ชัดเจนจากการย้ายไป Microsoft Copilot harness หรือไม่
ใช้ migration workflow ใน copilot-studio-plugin เป็นฐาน
เสนอ mapping ของแต่ละ behavior ไป instructions, skills, knowledge และ tools
ทำตาราง migrate / manual / skip / unsupported พร้อม connection dependencies
ใช้ acceptance cases เดิมตรวจ Agent ใหม่ และเก็บ source ไว้
ยังไม่สร้าง target จนกว่าจะระบุ environment และ workspace ที่แน่นอน
```

## อัปเดตชุดเดิม

1. อัปเดต checkout ของ PurpleBelt ด้วย `git pull` แล้วรัน integrity checks
2. ถ้าโปรเจกต์มี skills ติดตั้งอยู่แล้ว ให้สำรอง **เฉพาะชุดที่เคยติดตั้งจาก PurpleBelt**
   ไปไว้นอกโฟลเดอร์ discovery ตรวจและเก็บ customizations ก่อนย้าย อย่าเหมารวม skills
   อื่นเพียงเพราะชื่อขึ้นต้น `mcs-` หรือ `mcsa-`
3. รัน installer จาก checkout ใหม่กับโปรเจกต์จริง เลือก `--harness standard`,
   `agentic` หรือ `all` ตามต้องการ Installer จะหยุดหากยังมีชื่อที่ชนกัน
4. เปรียบเทียบกับ backup และนำ customizations กลับเฉพาะที่ยังเกี่ยวข้อง ตรวจ discovery
   ใน Copilot แล้วทดสอบหนึ่งงานเล็กก่อนใช้งานต่อ

อีกทางหนึ่งคือเปิด checkout PurpleBelt โดยตรง ซึ่งมี discovery entries ทั้งสองฝั่ง
แล้วบอก absolute path ของ business-agent workspace ให้ Copilot ชัดเจน การอัปเดต
checkout อย่างเดียวไม่อัปเดตสำเนาที่เคยติดตั้งในโปรเจกต์อื่น

## ความหมายของคำว่าเสร็จ

| รายงาน | หลักฐานขั้นต่ำ |
|---|---|
| สร้างไฟล์แล้ว | ไฟล์และ diff ที่อ่านได้ |
| Local checks ผ่าน | คำสั่งและผลตรวจที่รันจริง |
| Sync แล้ว | ผลจาก native sync operation ของ target ที่ถูกต้อง |
| Agent ทำงานแล้ว | ผลทดสอบใน tenant พร้อม tools/effects ที่ตรวจได้ |
| พร้อมใช้ใน channel | Publish และทดสอบบน channel เป้าหมาย |

Skill ไม่ได้ให้สิทธิ์ cloud และไม่เปิดใช้ connector ที่องค์กรบล็อก ข้อมูลที่ไม่สดหรือ
ไม่มี approved ingress ต้องใช้ snapshot/replay ที่ติดป้ายชัดเจน
