#!/usr/bin/env python3
"""
Setup script for the AI Coaching Chatbot
This script helps configure the application and set up the environment.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detected")

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

def setup_env_file():
    """Set up the .env file"""
    env_file = Path(".env")
    template_file = Path("env_template.txt")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return
    
    if template_file.exists():
        print("📝 Creating .env file from template...")
        try:
            with open(template_file, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created successfully")
            print("⚠️  Please edit .env file and add your OpenAI API key")
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
    else:
        print("❌ env_template.txt not found")

def check_env_configuration():
    """Check if environment is properly configured"""
    print("🔍 Checking environment configuration...")
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("⚠️  OpenAI API key not configured in .env file")
        print("   Please edit .env file and add your actual API key")
        return False
    
    print("✅ Environment configuration looks good")
    return True

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    try:
        import flask
        import openai
        from dotenv import load_dotenv
        print("✅ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up AI Coaching Chatbot...")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    install_dependencies()
    
    # Test imports
    if not test_imports():
        print("❌ Setup failed due to import errors")
        sys.exit(1)
    
    # Setup environment file
    setup_env_file()
    
    # Check configuration
    config_ok = check_env_configuration()
    
    print("=" * 50)
    if config_ok:
        print("🎉 Setup completed successfully!")
        print("\nTo run the application:")
        print("  python app.py")
        print("\nThe application will be available at: http://127.0.0.1:5000")
    else:
        print("⚠️  Setup completed with warnings")
        print("Please configure your .env file before running the application")

if __name__ == "__main__":
    main()
