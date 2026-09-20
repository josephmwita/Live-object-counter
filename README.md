# Live Object Counter 

Real-time object detection that just WORKS. Point your webcam at anything — it sees it, labels it, and counts it. No files saved, no records kept.

Built by Joseph Mwita

### Live Demo
![demo](https://user-images.githubusercontent.com/placeholder/demo.gif)
> Show it a bottle → `bottle: 1`  
> Show it your phone playing traffic → `car: 5, person: 2`

### What it does
- ✅ Opens webcam automatically
- ✅ Detects 80+ objects (person, car, bottle, laptop, phone...)
- ✅ Live counting — `Total: 3 objects | person: 2 | car: 1`
- ✅ No saving, no tracking, no records
- ✅ Works on any laptop

### Run it in 30 seconds
```bash
pip install ultralytics opencv-python
python detect.py
