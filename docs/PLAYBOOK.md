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

## 6. ออกแบบ hybrid ให้เหมาะกับงาน

```text
ใช้ copilot-studio-builder ออกแบบระบบทั้งเส้นทางก่อนสร้าง components
โจทย์: ติดตามข่าวที่ได้รับอนุญาต วิเคราะห์ผลกระทบที่เกี่ยวกับผู้ใช้ แล้วส่ง Teams
คิดวิธีที่เหมาะสมเอง ไม่ต้องยึดว่าต้องใช้ SharePoint หรือสอง harness

เทียบไม่เกิน 3 แบบ รวม baseline ที่ง่ายที่สุด แล้วแนะนำแบบเดียว
แบ่งแต่ละขั้นเป็น deterministic rules, bounded prompt หรือ agent reasoning
ตรวจวิธีเรียกและส่งต่องานจากเอกสารปัจจุบันพร้อมหลักฐานใน environment
แยก Power Automate, Standard agent flows และ modern Workflows ให้ชัด
แสดง cost model ทั้งเส้นทาง, latency, ข้อจำกัด และสิ่งที่ยังไม่ทราบ
กำหนดเงื่อนไขเรียก deep reasoning, cache/batch, retry และ budget ที่บังคับใช้ได้จริง
ถ้าต้อง async ให้ระบุ job state, claim, completion และป้องกันผลซ้ำ
ใช้ template ที่ <skill-root>/assets/hybrid-architecture-template.md
บันทึกแผนที่กรอกแล้วใน business project
แล้วทำหนึ่ง vertical slice ด้วยข้อมูลสังเคราะห์และวัด baseline เทียบแบบที่เลือก
```

เปลี่ยนโจทย์เป็นงานของคุณได้ เช่น review เอกสาร, intake, case triage หรือรายงาน
แผนเป็นคำแนะนำจากข้อจำกัดและหลักฐานที่มี ต้องทดลองเส้นทางจริงก่อนอ้างว่าประหยัดกว่า

## 7. ออกแบบ SharePoint ทั้งข้อมูลและหน้าใช้งาน

```text
ใช้ copilot-studio-builder ออกแบบ SharePoint สำหรับ [ผลลัพธ์ที่ต้องการ]
อ่าน SharePoint design guide และทำ blueprint ใน business project
ตรวจของเดิมจาก metadata/export ที่มี อย่าเดา site URL หรือ internal field names

เลือก Site, Lists, Document Libraries และ content types เท่าที่จำเป็น
ทำ data dictionary พร้อมชนิดข้อมูล required/default/validation และ business key
ออกแบบ permission matrix, queries, indexes และ views ตามปริมาณข้อมูลและผู้ใช้
เสนอ home page, navigation, native web parts และ forms ให้คนทำงานสะดวก
ถ้ามีประโยชน์ ให้สร้าง column/view formatting JSON พร้อมบอกจุดที่นำไปใช้
เชื่อม Agent/Workflow ผ่าน operation และ identity ที่ตรวจได้จริง
แสดงขั้นตอน provisioning ตามเครื่องมือที่องค์กรอนุญาตและเกณฑ์ทดสอบ
แยก proposed / generated / provisioned / tenant-tested ให้ชัด
เริ่มจาก blueprint ได้ แม้ยังไม่มี agent workspace หรือสิทธิ์สร้าง site
```

ใช้ `<skill-root>/assets/sharepoint-blueprint-template.md` เป็นแบบแผน มีตัวอย่าง
column formatting ที่ `<skill-root>/assets/sharepoint-status-format.example.json`
สำหรับ state แบบ Ready / Processing / Succeeded / Failed; ปรับค่าตามคอลัมน์จริง
แล้ว preview ใน native SharePoint ก่อน save ตัวอย่างนี้ไม่ได้สร้างคอลัมน์หรือ site

## 8. One-Prompt Solution Builder

สำหรับคนที่ต้องการให้ VS Code Agent Mode ช่วย **สร้างทั้ง Solution จากโจทย์เดียว** ไม่ใช่สร้าง Agent กับ Workflow ทีละตัว:

```text
ใช้ one-prompt-solution-builder ทำงานจนได้ผลลัพธ์ที่ทดสอบได้
โจทย์: Financial News Intelligence
ทุก 30 นาที ดึงข่าวจากแหล่งที่ได้รับอนุญาต กรองข่าวซ้ำและข่าวเก่า
ใช้ deterministic rules ก่อนส่งข่าวที่เกี่ยวข้องให้ AI วิเคราะห์ผลกระทบต่อพอร์ต
แยกข้อเท็จจริง สมมติฐาน และความไม่แน่นอน แสดง source URL + เวลาของข่าว
เก็บสถานะใน SharePoint ถ้ามีเหตุผลรองรับ และส่ง Teams เฉพาะเมื่อผ่าน threshold

ตรวจ workspace, harness, PAC/extension, capability และ DLP ก่อนลงมือ
เลือก architecture ที่เรียบง่ายที่สุดที่ตอบโจทย์ได้ แล้วดำเนินการต่อโดยไม่ถาม
ให้ฉันสร้างแต่ละ component เอง ยกเว้น approval/connection ที่จำเป็นจริง
สร้าง native agent ผ่านวิธีที่รองรับ และใช้ Studio/flow tooling ที่มีอยู่จริง
หากไม่มีเครื่องมือสร้าง Workflow canvas จาก VS Code ให้สร้าง designer-ready build sheet
พร้อม typed data contracts, prompt, sample payloads, permission map และ test cases
ทดสอบ normal / no news / duplicate / source failure / invalid answer / Teams failure
รายงานสถานะจริงเป็น DESIGNED / GENERATED / LOCAL_VALIDATED / SYNCED /
PROVISIONED / PUBLISHED / TENANT_TESTED / BLOCKED พร้อมหลักฐานต่อ component
ห้ามอ้างว่าระบบ live จนกว่าจะทดสอบ trigger -> analysis -> Teams ใน tenant
```

Copilot ควรสร้าง `solution-build-plan.md` ใน **business project** ตาม
[`one-prompt-solution-template.md`](../assets/one-prompt-solution-template.md)
แล้วทำส่วนที่ทำได้ต่อทันที เอกสารนี้ไม่ใช่ไฟล์ import เข้า Copilot Studio
ต้องตรวจ connector และสิทธิ์ที่ใช้จริงก่อน publish/ส่งข้อความ

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
