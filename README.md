# AI-Powered Calorie Tracker

A smart calorie tracking application that uses AI to analyze food items and calculate nutritional information. The application supports manual food entry, AI-based text analysis, and image recognition for food items.

## 🚀 Features

- **AI-Powered Food Recognition**: Upload an image of your food and get nutritional information
- **Smart Quantity Conversion**: Convert common measurements (cups, spoons, etc.) to grams automatically
- **Nutritional Analysis**: Get detailed nutritional information including calories, protein, carbs, and fats
- **Manual Entry**: Enter food items and quantities manually for quick tracking
- **RESTful API**: Built with FastAPI for high performance and easy integration

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI
- **AI/ML**: Google Generative AI (Gemini)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Image Processing**: Pillow
- **Deployment**: Render (with `render.yaml` configuration)

## 📦 Prerequisites

- Python 3.11+
- Poetry (for dependency management)
- PostgreSQL database
- Google Cloud API key (for Gemini AI)

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd calorie_tracker
   ```

2. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/calorie_tracker
   GOOGLE_API_KEY=your_google_ai_api_key
   ```

3. **Install dependencies**
   ```bash
   poetry install
   ```

4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

## 📚 API Endpoints

### Food Analysis
- `POST /api/food/manual_input` - Analyze food with manual entry
- `POST /api/food/ai_input` - Analyze food using AI text input
- `POST /api/food/from-image` - Analyze food from an image

### History
- `GET /api/history` - Get food log history
- `POST /api/history` - Add entry to food log

## 🤖 AI Features

The application leverages Google's Gemini AI for:
- Food recognition from images
- Natural language processing for food quantity conversion
- Smart food item identification from text descriptions

## 🧪 Testing

Run tests using pytest:
```bash
poetry run pytest
```

## 🚀 Deployment

The application includes a `render.yaml` configuration for easy deployment to Render.com. Update the environment variables in the Render dashboard after deployment.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For any questions or feedback, please contact [**Mariappan Sivakumar**] at [_spotmari2001@gmail.com_]
