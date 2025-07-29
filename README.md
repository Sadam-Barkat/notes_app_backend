# Notes App - Full Stack Application

A complete notes management application with a FastAPI backend and Streamlit frontend. This application provides a beautiful, modern interface for creating, organizing, and managing your notes with full CRUD functionality.

## 🎯 Features

### Backend (FastAPI)
- **RESTful API**: Complete CRUD operations for notes
- **MongoDB Integration**: Scalable NoSQL database storage
- **Async Operations**: High-performance asynchronous operations
- **Input Validation**: Pydantic models for data validation
- **CORS Support**: Cross-origin resource sharing enabled
- **Auto-generated Documentation**: Interactive API docs at `/docs`

### Frontend (Streamlit)
- **Beautiful UI**: Modern gradient design with smooth animations
- **Responsive Design**: Works great on all screen sizes
- **Search & Filter**: Find notes by title, content, or tags
- **Real-time Updates**: Instant feedback for all operations
- **Tag Management**: Organize notes with custom tags
- **Date Tracking**: Automatic timestamps for creation and updates

## 🏗️ Architecture

```
notes_app_backend/
├── backend/                 # FastAPI Backend
│   ├── app/
│   │   ├── db/
│   │   │   └── mongo.py    # MongoDB connection
│   │   ├── models/
│   │   │   └── note_model.py # Pydantic models
│   │   ├── routes/
│   │   │   └── note_routes.py # API endpoints
│   │   ├── utils/
│   │   │   └── helpers.py  # Utility functions
│   │   └── main.py         # FastAPI application
│   ├── requirements.txt    # Backend dependencies
│   └── README.md          # Backend documentation
├── frontend/               # Streamlit Frontend
│   ├── app.py             # Main Streamlit application
│   ├── config.py          # Configuration settings
│   ├── requirements.txt   # Frontend dependencies
│   └── README.md         # Frontend documentation
├── start_app.py           # Startup script for both services
├── test_api.py            # API testing script
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MongoDB (local or Atlas)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Sadam-Barkat/notes_app_backend.git
cd notes_app_backend
```

### 2. Set Up Backend
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with your MongoDB URI
echo "MONGODB_URI=your_mongodb_connection_string" > .env
```

### 3. Set Up Frontend
```bash
# Navigate to frontend directory
cd ../frontend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Start the Application

#### Option A: Using the Startup Script (Recommended)
```bash
# From the root directory
python start_app.py
```

#### Option B: Manual Start
```bash
# Terminal 1 - Start Backend
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Start Frontend
cd frontend
streamlit run app.py --server.port 8501
```

### 5. Access the Application
- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/notes/` | Get all notes |
| GET | `/notes/{id}` | Get note by ID |
| POST | `/notes/` | Create new note |
| PUT | `/notes/{id}` | Update note |
| DELETE | `/notes/{id}` | Delete note |

### Note Schema
```json
{
  "title": "string",
  "content": "string",
  "tags": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## 🎨 Frontend Features

### User Interface
- **Gradient Header**: Beautiful app branding with gradient background
- **Note Cards**: Colorful cards with hover effects and animations
- **Modern Forms**: Clean form designs with backdrop blur effects
- **Sidebar Navigation**: Intuitive navigation between pages
- **Search & Filter**: Real-time search and tag-based filtering

### Functionality
- **Create Notes**: Add new notes with title, content, and tags
- **View Notes**: Browse all notes with search and filter options
- **Edit Notes**: Modify existing notes inline
- **Delete Notes**: Remove notes with confirmation dialog
- **Tag Management**: Organize notes with custom tags
- **Responsive Design**: Works on desktop, tablet, and mobile

## 🔧 Configuration

### Backend Configuration
Create a `.env` file in the `backend/` directory:
```env
MONGODB_URI=mongodb://localhost:27017/notes_app_db
# or for MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/notes_app_db
```

### Frontend Configuration
Create a `.env` file in the `frontend/` directory:
```env
API_BASE_URL=http://localhost:8000/notes/
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
```

## 🛠️ Development

### Backend Development
```bash
cd backend
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload

# Run tests (if available)
pytest
```

### Frontend Development
```bash
cd frontend
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

# Customize styling by editing the CSS in app.py
```

## 🐛 Troubleshooting

### Common Issues

1. **MongoDB Connection Error**
   - Verify your MongoDB URI in the `.env` file
   - Ensure MongoDB is running (local) or accessible (Atlas)
   - Check network connectivity

2. **Port Already in Use**
   - Change ports in the configuration files
   - Kill existing processes using the ports

3. **Import Errors**
   - Ensure all dependencies are installed
   - Verify you're using the correct Python environment
   - Check Python version compatibility

4. **CORS Errors**
   - Backend CORS is configured to allow all origins
   - For production, update CORS settings in `main.py`

### Performance Tips
- Use MongoDB indexes for better query performance
- Implement pagination for large note collections
- Consider caching for frequently accessed data
- Optimize database queries

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Streamlit for the beautiful frontend framework
- MongoDB for the scalable database solution
- Pydantic for data validation
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the API documentation at `/docs`
3. Open an issue on GitHub
4. Check the individual README files in `backend/` and `frontend/` directories

## 🔒 Security

- Environment variables are properly ignored by `.gitignore`
- API keys and sensitive data are protected
- CORS is configured for development (update for production)
- Input validation is implemented using Pydantic

---

**Happy Note-Taking! 📝✨**

## 👨‍💻 Author

**Sadam Barkat**
- Email: sadambarkat405@gmail.com
- GitHub: [@Sadam-Barkat](https://github.com/Sadam-Barkat)

---

*This project was created as a full-stack notes application with modern web technologies.* 