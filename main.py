
---

### 2. `setup.sh`
```bash
#!/bin/bash

echo "🚀 EHESPO Nonprofit Toolkit Setup"
echo "=================================="

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

echo "✅ Setup complete!"
echo "📝 Edit .env with your registrar API keys"
echo "🚀 Run: python src/main.py"
