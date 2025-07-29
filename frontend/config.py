# Frontend Configuration
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/notes/")

# Streamlit Configuration
STREAMLIT_SERVER_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))
STREAMLIT_SERVER_ADDRESS = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")

# App Configuration
APP_TITLE = "Notes App"
APP_ICON = "📝"
PAGE_LAYOUT = "wide"

# UI Configuration
MAX_CONTENT_PREVIEW = 200  # Maximum characters to show in note preview
CARDS_PER_ROW = 2  # Number of note cards per row (for future grid layout)

# Colors and Themes (for future customization)
THEME_COLORS = {
    "primary": "#667eea",
    "secondary": "#764ba2",
    "success": "#56ab2f",
    "warning": "#f093fb",
    "error": "#ff6b6b",
    "info": "#4facfe"
} 