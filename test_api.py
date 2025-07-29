#!/usr/bin/env python3
"""
Test script to verify API endpoints and check for 307 redirects
"""

import requests
import json

def test_api_endpoints():
    """Test all API endpoints to check for redirects"""
    
    base_url = "http://localhost:8000"
    
    print("🔍 Testing API Endpoints...")
    print("=" * 50)
    
    # Test 1: GET /notes (should redirect to /notes/)
    print("\n1. Testing GET /notes (without trailing slash):")
    try:
        response = requests.get(f"{base_url}/notes", allow_redirects=False)
        print(f"   Status: {response.status_code}")
        print(f"   Location: {response.headers.get('Location', 'None')}")
        if response.status_code == 307:
            print("   ⚠️  This causes a 307 redirect!")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: GET /notes/ (should work directly)
    print("\n2. Testing GET /notes/ (with trailing slash):")
    try:
        response = requests.get(f"{base_url}/notes/", allow_redirects=False)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Direct access works!")
            data = response.json()
            print(f"   Notes count: {len(data)}")
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: POST /notes/ (create a test note)
    print("\n3. Testing POST /notes/ (create note):")
    try:
        test_note = {
            "title": "Test Note",
            "content": "This is a test note to verify the API.",
            "tags": ["test", "api"]
        }
        response = requests.post(f"{base_url}/notes/", json=test_note)
        print(f"   Status: {response.status_code}")
        if response.status_code == 201:
            print("   ✅ Note created successfully!")
            created_note = response.json()
            note_id = created_note.get('id') or created_note.get('_id')
            print(f"   Note ID: {note_id}")
            return note_id
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    return None

def test_note_operations(note_id):
    """Test individual note operations"""
    if not note_id:
        print("\n⚠️  Skipping note operations - no note ID available")
        return
    
    base_url = "http://localhost:8000"
    
    print(f"\n4. Testing GET /notes/{note_id}:")
    try:
        response = requests.get(f"{base_url}/notes/{note_id}")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Note retrieved successfully!")
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print(f"\n5. Testing PUT /notes/{note_id}:")
    try:
        updated_note = {
            "title": "Updated Test Note",
            "content": "This note has been updated.",
            "tags": ["test", "api", "updated"]
        }
        response = requests.put(f"{base_url}/notes/{note_id}", json=updated_note)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Note updated successfully!")
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print(f"\n6. Testing DELETE /notes/{note_id}:")
    try:
        response = requests.delete(f"{base_url}/notes/{note_id}")
        print(f"   Status: {response.status_code}")
        if response.status_code == 204:
            print("   ✅ Note deleted successfully!")
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def main():
    """Main test function"""
    print("🚀 API Endpoint Test Script")
    print("=" * 50)
    
    # Test basic endpoints
    note_id = test_api_endpoints()
    
    # Test individual note operations
    test_note_operations(note_id)
    
    print("\n" + "=" * 50)
    print("✅ Testing completed!")
    
    print("\n📋 Summary:")
    print("- If you see 307 redirects for /notes, the frontend should use /notes/")
    print("- All endpoints should return 200/201/204 status codes")
    print("- Check the backend logs for any additional errors")

if __name__ == "__main__":
    main() 