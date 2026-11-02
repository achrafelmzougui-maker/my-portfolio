# Smart Attendance — academic prototype

Python / OpenCV (YuNet and SFace) / SQLite attendance concept. This folder hosts a **browser-only workflow demo** with **fictional student records**. It does not perform face recognition, connect to a camera or store personal information.

## What the demo supports
- Teacher-reviewed Present / Absent / Late status
- Session summary and CSV export
- Resettable fictional student data
- Responsive presentation for GitHub Pages

## Limitations
The original local Python prototype performs facial matching, but does **not** include validated liveness detection. Face matching alone must not be treated as proof of real-world presence. A real deployment would need institutional authorization, consent and privacy/security review, plus human oversight. Do not commit photographs, biometric templates or SQLite student records to a public repository.

## Demo
[Open the live demo](https://achrafelmzougui-maker.github.io/my-portfolio/smart-attendance/)
