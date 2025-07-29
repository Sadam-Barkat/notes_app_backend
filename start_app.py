#!/usr/bin/env python3
"""
Startup script for the Notes App
This script can start both the backend and frontend services
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import requests
        import fastapi
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies:")
        print("  Backend: pip install -r backend/requirements.txt")
        print("  Frontend: pip install -r frontend/requirements.txt")
        return False

def start_backend():
    """Start the FastAPI backend server"""
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return None
    
    print("🚀 Starting backend server...")
    try:
        # Change to backend directory and start uvicorn
        process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
            cwd=backend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Backend server started on http://localhost:8000")
        return process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_frontend():
    """Start the Streamlit frontend"""
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found")
        return None
    
    print("🚀 Starting frontend server...")
    try:
        # Change to frontend directory and start streamlit
        process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "localhost"],
            cwd=frontend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Frontend server started on http://localhost:8501")
        return process
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}")
        return None

def main():
    """Main function to start the application"""
    print("🎯 Notes App Startup Script")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Get user choice
    print("\nChoose what to start:")
    print("1. Backend only")
    print("2. Frontend only")
    print("3. Both (recommended)")
    print("4. Test API endpoints")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    backend_process = None
    frontend_process = None
    
    try:
        if choice == "1":
            backend_process = start_backend()
        elif choice == "2":
            frontend_process = start_frontend()
        elif choice == "3":
            backend_process = start_backend()
            if backend_process:
                time.sleep(2)  # Wait for backend to start
                frontend_process = start_frontend()
        elif choice == "4":
            print("\n🔍 Testing API endpoints...")
            subprocess.run([sys.executable, "test_api.py"])
            return
        elif choice == "5":
            print("👋 Goodbye!")
            return
        else:
            print("❌ Invalid choice")
            return
        
        if choice in ["1", "3"] and backend_process:
            print("\n📝 Backend API Documentation: http://localhost:8000/docs")
        
        if choice in ["2", "3"] and frontend_process:
            print("\n🌐 Frontend will open automatically in your browser")
            print("   If not, manually navigate to: http://localhost:8501")
        
        if choice == "3":
            print("\n🎉 Both services are running!")
            print("   Backend: http://localhost:8000")
            print("   Frontend: http://localhost:8501")
            print("   API Docs: http://localhost:8000/docs")
        
        # Keep the script running
        if backend_process or frontend_process:
            print("\n⏹️  Press Ctrl+C to stop all services")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n🛑 Stopping services...")
    
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
    
    finally:
        # Clean up processes
        if backend_process:
            backend_process.terminate()
            print("✅ Backend stopped")
        
        if frontend_process:
            frontend_process.terminate()
            print("✅ Frontend stopped")
        
        print("👋 All services stopped")

if __name__ == "__main__":
    main() 