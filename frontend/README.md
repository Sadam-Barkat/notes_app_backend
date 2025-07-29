# Notes App Frontend

A beautiful, colorful Streamlit frontend for the Notes App backend. This application provides an intuitive and modern interface for managing your notes with full CRUD functionality.

## Features

- **Beautiful UI**: Modern gradient design with smooth animations and hover effects
- **Full CRUD Operations**: Create, Read, Update, and Delete notes
- **Search & Filter**: Search notes by title/content and filter by tags
- **Responsive Design**: Works great on different screen sizes
- **Real-time Updates**: Instant feedback for all operations
- **Tag Management**: Organize notes with custom tags
- **Date Tracking**: Automatic creation and update timestamps

## Screenshots

The app features:
- Gradient header with app branding
- Colorful note cards with hover effects
- Modern form designs with backdrop blur
- Intuitive navigation sidebar
- Search and filter functionality
- Beautiful success/error messages

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd notes_app_backend/frontend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Ensure the backend is running**:
   - Navigate to the backend directory
   - Start the FastAPI server:
     ```bash
     cd ../backend
     uvicorn app.main:app --reload
     ```

2. **Set up environment variables** (if needed):
   - Create a `.env` file in the frontend directory
   - Add any custom configuration

## Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

3. **Using the app**:
   - **View Notes**: Browse all your notes with search and filter options
   - **Create Note**: Add new notes with title, content, and tags
   - **Edit Note**: Modify existing notes
   - **Delete Note**: Remove notes with confirmation
   - **View Full Note**: See complete note content in a modal

## API Integration

The frontend communicates with the FastAPI backend at `http://localhost:8000`. Make sure:
- The backend server is running on port 8000
- CORS is properly configured (already set up in the backend)
- All API endpoints are accessible

## File Structure

```
frontend/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Customization

### Colors and Styling
The app uses custom CSS for styling. You can modify the colors and effects by editing the CSS section in `app.py`:

- **Gradients**: Change the gradient colors in the CSS classes
- **Card Design**: Modify the `.note-card` class for different card styles
- **Buttons**: Customize button styles in the `.stButton` classes
- **Animations**: Adjust transition effects and hover states

### Features
- Add new features by extending the main functions
- Modify the layout by changing the Streamlit components
- Add new pages by extending the sidebar navigation

## Troubleshooting

### Common Issues

1. **Backend Connection Error**:
   - Ensure the FastAPI server is running on port 8000
   - Check if the API_BASE_URL in app.py matches your backend URL

2. **Import Errors**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're using the correct Python environment

3. **Display Issues**:
   - Clear browser cache
   - Restart the Streamlit app
   - Check for any CSS conflicts

### Performance Tips

- The app loads all notes at once for better user experience
- Search and filtering are done client-side for instant results
- Large note collections may benefit from pagination (can be added as a feature)

## Contributing

To contribute to this frontend:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Notes App and follows the same license as the main project. 