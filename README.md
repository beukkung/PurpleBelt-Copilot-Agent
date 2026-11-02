# PurpleBelt — Copilot Studio Builder

**Skill สำหรับ GitHub Copilot เพื่อออกแบบ สร้าง แก้ไข ทดสอบ และเตรียม demo ของ Microsoft Copilot Studio agent**

รวม **Microsoft Skills for Copilot Studio แบบครบทั้ง repository** พร้อม skill หลักที่เพิ่ม Business/Product thinking, environment discovery, workflow reliability และ hackathon execution ใช้ได้กับหลายอุตสาหกรรมและหลายข้อจำกัด ไม่ผูกกับธนาคารใด

## สิ่งที่รวมมา

| ส่วน | รายละเอียด |
|---|---|
| Builder skill ของเรา | Outcome -> Architecture -> Native artifacts -> Verification -> Demo |
| Microsoft skills | 31 skills ครบจาก commit ที่ระบุใน lock file |
| Specialist roles | Author, Manage, Test, Advisor ทั้ง 4 ไฟล์ต้นฉบับ |
| Native references | Authoring schema, Adaptive Card schema, connector metadata |
| Templates / patterns | 18 templates และ 15 patterns ต้นฉบับ |
| Tools / evaluation | Bundled CLI, source, evaluation fixtures, scenarios และ tests |
| Copilot discovery | 32 entry points: Builder + `mcs-*` สำหรับ Microsoft skills ทุกตัว |
| Local utilities | Installer, read-only preflight, upstream integrity verification |

ต้นฉบับ Microsoft อยู่ใน `vendor/microsoft/skills-for-copilot-studio/` แบบไม่แก้เนื้อหา มี MIT license เดิมและ SHA-256/Git blob hash ทุกไฟล์ใน [upstream.lock.json](upstream.lock.json)

เริ่มอ่าน [SKILL.md](SKILL.md) และ [สารบัญ Microsoft skills](references/upstream-catalog.md)

## เริ่มใช้ใน VS Code

สิ่งที่ต้องมี: GitHub Copilot ที่รองรับ Agent Skills, Python 3.10+ สำหรับ utilities ของเรา และ Node.js 18+ สำหรับ toolkit ของ Microsoft การเชื่อม cloud ต้องมี Copilot Studio extension, สิทธิ์ environment และ license/capacity ตามงานนั้น

```bash
git clone https://github.com/beukkung/PurpleBelt-Copilot-Agent.git
cd PurpleBelt-Copilot-Agent
python -m pip install -r requirements.txt
python scripts/verify_bundle.py
```

เปิดโฟลเดอร์นี้ใน VS Code: `.github/skills/` มี discovery wrappers พร้อมแล้ว Copilot จะอ่านรายละเอียดจากต้นฉบับเฉพาะเวลาต้องใช้ หากต้องแก้ business agent ให้เปิด workspace ที่ clone จาก Studio และระบุ path ให้ชัดเจน

### ติดตั้งลงโปรเจกต์ agent ที่มีอยู่

```bash
python scripts/install.py --target "/absolute/path/to/my-agent-project"
```

ตัวติดตั้งคัดลอก bundle ที่ทำงานได้ด้วยตัวเองเข้า `.github/skills/copilot-studio-builder/` และสร้าง `mcs-*` wrappers 31 ตัวข้างกัน รองรับ path ที่มีช่องว่าง ไม่เขียนทับ skill เดิม และไม่เปิดใช้ hooks หรือ MCP โดยอัตโนมัติ

ตัวอย่าง Windows PowerShell:

```powershell
py scripts/install.py --target "C:\Projects\My Copilot Agent"
```

### ใช้ส่วนตัวข้ามโปรเจกต์

```bash
python scripts/install.py --personal --target "$HOME/.copilot/skills"
```

PowerShell:

```powershell
py scripts/install.py --personal --target "$env:USERPROFILE\.copilot\skills"
```

ถ้ามีชื่อ skill ซ้ำ ตัวติดตั้งจะหยุดก่อนเปลี่ยนไฟล์ ให้เก็บสำรองและจัดการเวอร์ชันเดิมก่อน ใช้การตั้งค่า Skills/Customizations ของ Copilot ตรวจว่า skills ถูกค้นพบแล้ว การมีไฟล์ไม่ได้รับประกันว่าโมเดลจะเรียกทุกครั้ง

## ตัวอย่างคำสั่งให้ Copilot

```text
Use copilot-studio-builder. ตรวจ agent workspace นี้ก่อน แล้วสร้าง
customer service agent ที่ค้นคำตอบจาก SharePoint และเปิด request หลังผู้ใช้ยืนยัน
เลือกวิธีตาม harness, connectors, license และ DLP ที่มีจริง
ทำหนึ่งเส้นทางให้จบ พร้อม negative cases และแยกผล local กับ tenant tests
```

```text
ใช้ copilot-studio-builder ตรวจ flow ที่บอกว่าบันทึกสำเร็จแม้หา record ไม่พบ
อ่าน definition และ topic ที่เรียกมัน แก้ให้คืน status ตามผลจริง
เพิ่มกรณี missing, duplicate, timeout และ partial success
```

```text
Use copilot-studio-builder to prepare a six-hour hackathon build.
Our goal is personalized news analysis. Identify approved data ingress,
produce the smallest working slice, then add freshness evidence and a demo plan.
```

เรียก Microsoft operation โดยตรงได้ผ่านชื่อเช่น `mcs-new-topic`, `mcs-add-action`, `mcs-add-adaptive-card`, `mcs-validate`, `mcs-manage-agent` และ `mcs-create-eval-set` โดยยังใช้กฎเรื่อง environment/evidence จาก Builder

## ขอบเขตที่ต้องเข้าใจ

- Skill นี้ช่วย **GitHub Copilot พัฒนา agent** ไม่ได้เปลี่ยน runtime ของ agent
- Toolkit Microsoft ที่รวมมาสำหรับ **standard harness**; harness อื่นต้องใช้ schema/plugin ที่ตรงกัน
- การใช้ YAML หรือ import solution ไม่ข้าม DLP, permission, license หรือ endpoint restrictions
- ไม่มี FlowStudio server/subscription, Azure hosting, API credentials หรือ premium entitlement แถมมา
- ตัวติดตั้งไม่ได้ลงทะเบียน specialist role files เป็น custom-agent personas และไม่เปิดใช้ upstream hooks
- ไฟล์ต้นฉบับบางส่วนเป็น experimental/version-specific ต้องตรวจคู่กับ diagnostics ปัจจุบัน
- Patterns ที่เกี่ยวกับ chain-of-thought เก็บไว้เพื่อความครบของ snapshot แต่ Builder กำหนดให้ใช้ concise decision/evidence logging แทน private reasoning

## ตรวจอะไรได้บ้าง

```bash
python scripts/preflight.py "/path/to/actual-agent-workspace"
```

ตรวจ syntax ของ YAML/flow JSON, duplicate keys/node IDs, inventory และ heuristic บางอย่าง เช่น success flag เริ่มเป็น true โดยไม่อ่าน connection secrets

**ผลนี้ไม่ใช่ Microsoft schema/Power Fx validation และไม่พิสูจน์ว่า agent ทำงานใน tenant แล้ว** Native LSP, authentication, deployment, DLP, tool effects และ target-channel rendering ต้องตรวจด้วยเครื่องมือ/สิทธิ์จริงตาม [Verification](references/verification.md)

เครื่องมือ schema lookup จาก Microsoft ใช้ได้แบบ local:

```bash
node vendor/microsoft/skills-for-copilot-studio/scripts/schema-lookup.bundle.js resolve AdaptiveDialog
```

อ่าน original `skills/validate/SKILL.md` และ `SETUP_GUIDE.md` ก่อน native diagnostics หรือ cloud operations; อย่าสมมติว่า local script ทุกตัวไม่มี dependencies เพิ่ม

## Quality checks ของชุดนี้

```bash
python -m unittest discover -s tests -v
python scripts/verify_bundle.py
```

ทดสอบ installer, การไม่เขียนทับไฟล์เดิม, discovery wrappers, YAML errors, ขอบเขต static checks, การไม่อ่าน connection secrets และการตรวจไฟล์ต้นฉบับถูกแก้ ไม่ใช่ live certification ของ Copilot Studio tenant

## โครงสร้าง

```text
SKILL.md                 Builder workflow
references/              Architecture, authoring, data, flows, verification, demo
scripts/                 Installer, preflight, integrity checker
assets/                  Synthetic design examples and acceptance cases
vendor/microsoft/        Complete pinned Microsoft toolkit (152 files)
.github/skills/          Copilot discovery entries
tests/                   Local tooling regression tests
upstream.lock.json       Original commit and every file hash
NOTICE.md                Attribution and integration boundaries
```

## อัปเดต Microsoft toolkit

Snapshot นี้ pin ที่ `9c42d3a612c6e06389b6e5b4eed579aaed1a8b63` วันที่ตรวจ 2026-11-02 ไม่มี auto-update ให้ review diff/license, สร้าง lock file ใหม่จาก commit ที่เลือก, regenerate catalog/wrappers และรันทดสอบก่อนเปลี่ยนเวอร์ชัน อย่าแก้ไฟล์ vendor แล้วใช้ lock เดิม

## Sources and license

Microsoft original: https://github.com/microsoft/skills-for-copilot-studio

[Sources and inspected reference builds](references/sources.md) · [Attribution](NOTICE.md) · [MIT](LICENSE)

Independent integration by beukkung. No Microsoft endorsement. No private business data or credentials are included.
