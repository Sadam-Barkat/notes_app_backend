import streamlit as st
import requests
import json
from datetime import datetime
import time
from typing import List, Dict, Any

# Page configuration
st.set_page_config(
    page_title="Notes App",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .note-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease;
    }
    
    .note-card:hover {
        transform: translateY(-5px);
    }
    
    .tag {
        background: rgba(255,255,255,0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.8rem;
        color: white;
    }
    
    .success-message {
        background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    
    .error-message {
        background: linear-gradient(90deg, #ff6b6b 0%, #ee5a52 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    
    .form-container {
        background: rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .delete-btn {
        background: linear-gradient(90deg, #ff6b6b 0%, #ee5a52 100%) !important;
    }
    
    .edit-btn {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%) !important;
    }
    
    .view-btn {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
API_BASE_URL = "http://localhost:8000/notes/"

def make_api_request(method: str, endpoint: str = "", data: Dict = None) -> Dict:
    """Make API request to the backend"""
    # Build URL properly to avoid redirects
    if endpoint:
        url = f"{API_BASE_URL.rstrip('/')}/{endpoint}"
    else:
        url = API_BASE_URL  # Keep the trailing slash for the base URL
    
    # Debug: Print the URL being called
    print(f"DEBUG: Making {method} request to: {url}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        
        response.raise_for_status()
        return {"success": True, "data": response.json() if response.content else None}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def format_datetime(dt_str: str) -> str:
    """Format datetime string for display"""
    try:
        dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return dt_str

def display_note_card(note: Dict[str, Any], show_actions: bool = True):
    """Display a note in a beautiful card format"""
    # Get the note ID - handle both 'id' and '_id' fields
    note_id = note.get('id') or note.get('_id')
    
    with st.container():
        st.markdown(f"""
        <div class="note-card">
            <h3 style="color: white; margin-bottom: 1rem;">{note.get('title', 'Untitled')}</h3>
            <p style="color: rgba(255,255,255,0.9); margin-bottom: 1rem; line-height: 1.6;">
                {note.get('content', '')[:200]}{'...' if len(note.get('content', '')) > 200 else ''}
            </p>
            <div style="margin-bottom: 1rem;">
                {''.join([f'<span class="tag">{tag}</span>' for tag in note.get('tags', [])])}
            </div>
            <div style="color: rgba(255,255,255,0.7); font-size: 0.8rem;">
                Created: {format_datetime(note.get('created_at', ''))}<br>
                Updated: {format_datetime(note.get('updated_at', ''))}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if show_actions:
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("View", key=f"view_{note_id}", help="View full note"):
                    st.write(f"DEBUG: View button clicked for note ID: {note_id}")
                    st.session_state.view_note = note
                    st.rerun()
            with col2:
                if st.button("Edit", key=f"edit_{note_id}", help="Edit note"):
                    st.session_state.edit_note = note
                    st.rerun()
            with col3:
                if st.button("Delete", key=f"delete_{note_id}", help="Delete note"):
                    st.session_state.delete_note = note
                    st.rerun()

def create_note_form():
    """Form for creating a new note"""
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.subheader("Create New Note")
    
    with st.form("create_note_form"):
        title = st.text_input("Title", placeholder="Enter note title...")
        content = st.text_area("Content", placeholder="Enter note content...", height=200)
        tags_input = st.text_input("Tags", placeholder="Enter tags separated by commas...")
        
        submitted = st.form_submit_button("Create Note")
        
        if submitted:
            if title and content:
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []
                
                note_data = {
                    "title": title,
                    "content": content,
                    "tags": tags
                }
                
                result = make_api_request("POST", data=note_data)
                
                if result["success"]:
                    st.success("Note created successfully!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"Error creating note: {result['error']}")
            else:
                st.error("Please fill in both title and content fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def edit_note_form(note: Dict[str, Any]):
    """Form for editing an existing note"""
    # Get the note ID - handle both 'id' and '_id' fields
    note_id = note.get('id') or note.get('_id')
    
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.subheader("Edit Note")
    
    with st.form("edit_note_form"):
        title = st.text_input("Title", value=note.get('title', ''), placeholder="Enter note title...")
        content = st.text_area("Content", value=note.get('content', ''), placeholder="Enter note content...", height=200)
        tags_input = st.text_input("Tags", value=", ".join(note.get('tags', [])), placeholder="Enter tags separated by commas...")
        
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Update Note")
        with col2:
            if st.form_submit_button("Cancel"):
                st.session_state.edit_note = None
                st.rerun()
        
        if submitted:
            if title and content:
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []
                
                note_data = {
                    "title": title,
                    "content": content,
                    "tags": tags
                }
                
                result = make_api_request("PUT", endpoint=note_id, data=note_data)
                
                if result["success"]:
                    st.success("Note updated successfully!")
                    st.session_state.edit_note = None
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"Error updating note: {result['error']}")
            else:
                st.error("Please fill in both title and content fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def view_note_modal(note: Dict[str, Any]):
    """Modal for viewing a full note"""
    # Debug: Print the note data
    st.write("DEBUG: Note data received:", note)
    
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.subheader("View Note")
    
    # Display note data in a more robust way
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
        <h3 style="color: white; margin-bottom: 1rem;">{note.get('title', 'Untitled')}</h3>
        <p style="color: rgba(255,255,255,0.9); line-height: 1.8; white-space: pre-wrap;">
            {note.get('content', '')}
        </p>
        <div style="margin: 1rem 0;">
            {''.join([f'<span class="tag">{tag}</span>' for tag in note.get('tags', [])])}
        </div>
        <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
            <strong>Created:</strong> {format_datetime(note.get('created_at', ''))}<br>
            <strong>Updated:</strong> {format_datetime(note.get('updated_at', ''))}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Also display as JSON for debugging
    if st.checkbox("Show raw data", key="show_raw_data"):
        st.json(note)
    
    if st.button("Close", key="close_view"):
        st.session_state.view_note = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def delete_note_modal(note: Dict[str, Any]):
    """Modal for confirming note deletion"""
    # Get the note ID - handle both 'id' and '_id' fields
    note_id = note.get('id') or note.get('_id')
    
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.subheader("Delete Note")
    
    st.warning(f"Are you sure you want to delete the note '{note.get('title', 'Untitled')}'?")
    st.info("This action cannot be undone.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, Delete"):
            result = make_api_request("DELETE", endpoint=note_id)
            
            if result["success"]:
                st.success("Note deleted successfully!")
                st.session_state.delete_note = None
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"Error deleting note: {result['error']}")
    
    with col2:
        if st.button("Cancel"):
            st.session_state.delete_note = None
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main application
def main():
    # Initialize session state
    if 'view_note' not in st.session_state:
        st.session_state.view_note = None
    if 'edit_note' not in st.session_state:
        st.session_state.edit_note = None
    if 'delete_note' not in st.session_state:
        st.session_state.delete_note = None
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; text-align: center; margin: 0;">Notes App</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0;">Organize your thoughts beautifully</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## Navigation")
        page = st.radio(
            "Choose a page:",
            ["View Notes", "Create Note"],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### Quick Stats")
        
        # Get notes count
        notes_result = make_api_request("GET")
        if notes_result["success"]:
            notes_count = len(notes_result["data"])
            st.metric("Total Notes", notes_count)
        else:
            st.error("Unable to fetch notes count")
    
    # Main content
    if page == "View Notes":
        st.header("Your Notes")
        
        # Check for modals first
        if st.session_state.view_note:
            view_note_modal(st.session_state.view_note)
        elif st.session_state.edit_note:
            edit_note_form(st.session_state.edit_note)
        elif st.session_state.delete_note:
            delete_note_modal(st.session_state.delete_note)
        else:
            # Display notes
            notes_result = make_api_request("GET")
            
            if notes_result["success"]:
                notes = notes_result["data"]
                
                # Debug: Show the structure of the first note if available
                if notes and st.checkbox("Debug: Show note structure", key="debug_structure"):
                    st.json(notes[0])
                
                if not notes:
                    st.info("No notes found. Create your first note!")
                else:
                    # Search and filter
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        search_term = st.text_input("Search notes...", placeholder="Search by title or content")
                    with col2:
                        tag_filter = st.selectbox("Filter by tag", ["All"] + list(set([tag for note in notes for tag in note.get('tags', [])])))
                    
                    # Filter notes
                    filtered_notes = notes
                    if search_term:
                        filtered_notes = [note for note in filtered_notes 
                                        if search_term.lower() in note.get('title', '').lower() 
                                        or search_term.lower() in note.get('content', '').lower()]
                    
                    if tag_filter != "All":
                        filtered_notes = [note for note in filtered_notes 
                                        if tag_filter in note.get('tags', [])]
                    
                    if filtered_notes:
                        st.markdown(f"**Showing {len(filtered_notes)} of {len(notes)} notes**")
                        
                        for note in filtered_notes:
                            display_note_card(note)
                    else:
                        st.info("No notes match your search criteria.")
            else:
                st.error(f"Error fetching notes: {notes_result['error']}")
    
    elif page == "Create Note":
        create_note_form()

if __name__ == "__main__":
    main() 