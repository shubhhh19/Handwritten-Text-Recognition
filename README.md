# ✍️ Handwritten OCR Application ✍️

<div align="center">

<img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status" />
<img src="https://img.shields.io/badge/license-MIT-blue" alt="License" />
<img src="https://img.shields.io/badge/version-1.0-orange" alt="Version" />

```
   _    _                _                  _ _   _               ___   ____ ____
  | |  | |              | |                (_) | | |             / _ \ / ___|  _ \
  | |__| | __ _ _ __  __| |_      ___ __ ___| |_| |_ ___ _ __  | | | | |   | |_) |
  |  __  |/ _` | '_ \/ _` \ \ /\ / / '__/ _ \ __| __/ _ \ '_ \ | | | | |   |  _ <
  | |  | | (_| | | | | (_| |\ V  V /| | |  __/ |_| ||  __/ | | || |_| | |___| |_) |
  |_|  |_|\__,_|_| |_|\__,_| \_/\_/ |_|  \___|\__|\__\___|_| |_(_)___/ \____|____/
```

_A powerful web application that converts handwritten text to digital format using advanced OCR technology_

</div>

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#️-technology-stack)
- [Installation](#-installation)
- [Screenshots](#-screenshots)
- [Interesting Parts During Build](#-interesting-parts-during-build)
- [Challenges and Solutions](#-challenges-and-solutions)
- [Future Updates](#-future-updates)
- [Author](#-author)
- [License](#-license)

## 🌟 Features

- ✨ **Handwritten Text Recognition**: Convert handwritten text from images to digital text
- 🌐 **Multi-language Support**: Translate extracted text into various languages
- 📝 **Text Summarization**: Coming soon! Generate concise summaries of long texts
- 🔐 **User Authentication**: Secure login and signup system
- 📁 **File Management**: Support for multiple file formats (PDF, DOCX, TXT)
- 📊 **History Tracking**: Keep track of all your OCR conversions
- ⚙️ **User Settings**: Customize your account preferences

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- SQLite
- Google Cloud Vision API
- LibreTranslate API

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/shubhhh19/Handwritten-Text-Recognition.git
cd Handwritten-Text-Recognition
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
python init_db.py
```

## 📸 Screenshots

<div align="center">
<img src="static/screenshots/home.png" alt="Home Page" width="600"/>
<img src="static/screenshots/upload.png" alt="Upload Interface" width="600"/>
<img src="static/screenshots/result.png" alt="Result Page" width="600"/>
</div>

## 🏗️ Interesting Parts During Build

1. **OCR Implementation**
   - Implemented advanced image preprocessing techniques
   - Integrated Google Cloud Vision API for accurate text recognition
   - Developed custom algorithms for handling different handwriting styles

2. **Translation System**
   - Built a robust translation pipeline using LibreTranslate API
   - Implemented language detection and automatic translation
   - Added support for multiple language pairs

3. **User Interface**
   - Created an intuitive and responsive design
   - Implemented real-time file upload preview
   - Added progress indicators for long-running operations

## 🎯 Challenges and Solutions

1. **Challenge**: Low OCR accuracy for certain handwriting styles
   - **Solution**: Implemented image preprocessing techniques including contrast enhancement and noise reduction
   - Added support for multiple image formats and quality levels

2. **Challenge**: Slow processing time for large documents
   - **Solution**: Implemented batch processing and asynchronous operations
   - Added progress tracking and status updates

3. **Challenge**: Cross-browser compatibility issues
   - **Solution**: Used modern CSS features with fallbacks
   - Implemented responsive design principles
   - Added browser-specific optimizations

## 🔮 Future Updates

1. **Coming Soon**
   - Text summarization feature
   - Advanced document analysis
   - Batch processing improvements
   - Mobile application

2. **Planned Improvements**
   - Enhanced OCR accuracy
   - Additional language support
   - Real-time collaboration features
   - API rate limiting and optimization

## 👨‍💻 Author

**Shubh Soni**
- GitHub: [@shubhhh19](https://github.com/shubhhh19)
- Email: sonishubh2004@gmail.com