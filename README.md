# VitaminD - AI-Powered Personalized Health Coach

An intelligent health coaching application that analyzes user health data to provide personalized, evidence-based recommendations for improved wellness.

## 🚀 Features

- **AI-Powered Recommendations**: Uses advanced LLM technology with RAG pipeline for evidence-based health advice
- **Personalized Insights**: Tailored recommendations based on individual health metrics and goals
- **Health Data Management**: Upload and track various health metrics including bloodwork, diet, exercise
- **Secure Authentication**: Auth0 integration for secure user management
- **Document Processing**: PDF parsing for medical reports and lab results
- **Data Visualization**: Interactive charts and dashboards for tracking progress
- **Conversational Interface**: Chat-based AI interaction for natural health queries

## 🛠 Tech Stack

### Frontend

- **Next.js 15** with TypeScript and Turbopack
- **Tailwind CSS** for styling
- **shadcn/ui** for UI components
- **Recharts** for data visualization
- **React Hook Form + Zod** for form validation
- **Auth0** for authentication

### Backend

- **FastAPI** (Python 3.13.3) for high-performance API
- **PostgreSQL** for data storage
- **LangChain** for AI orchestration
- **OpenAI GPT-4** for recommendations
- **Pinecone** for vector storage
- **Voyage AI** for embeddings
- **AWS S3** for file storage

### Development Tools

- **pnpm** for package management
- **Uvicorn** for ASGI server
- **Alembic** for database migrations
- **pytest** for testing

## 📋 Prerequisites

- **Node.js** 18+ with pnpm
- **Python** 3.13.3
- **PostgreSQL** 15+
- **Git**

## 🏃‍♂️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ccfegenbush/vitamind.git
cd vitamind
```

### 2. Frontend Setup

```bash
# Install frontend dependencies
pnpm install

# Start the development server
pnpm dev
```

The frontend will be available at `http://localhost:3000`

### 3. Backend Setup

```bash
# Create Python virtual environment
cd backend
python3.13 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install backend dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your configuration

# Start the backend server
cd ..
pnpm backend:dev
```

The API will be available at `http://localhost:8000`

### 4. Database Setup (Optional for development)

```bash
# Install PostgreSQL (macOS with Homebrew)
brew install postgresql@15
brew services start postgresql@15

# Create database
createdb vitamind_db

# Run migrations (when implemented)
pnpm db:migrate
```

## 📜 Available Scripts

### Frontend

- `pnpm dev` - Start Next.js development server
- `pnpm build` - Build for production
- `pnpm start` - Start production server
- `pnpm lint` - Run ESLint
- `pnpm type-check` - Run TypeScript checks

### Backend

- `pnpm backend:dev` - Start FastAPI development server
- `pnpm backend:install` - Install Python dependencies
- `pnpm db:migrate` - Run database migrations

### Testing

- `pnpm test` - Run frontend tests
- `pnpm test:watch` - Run tests in watch mode

## 🏗 Project Structure

```
vitamind/
├── src/                    # Next.js frontend
│   ├── app/               # App Router pages
│   ├── components/        # React components
│   ├── lib/              # Utilities and configurations
│   └── types/            # TypeScript type definitions
├── backend/               # FastAPI backend
│   ├── app/              # Application modules
│   ├── alembic/          # Database migrations
│   ├── main.py           # FastAPI application
│   ├── requirements.txt  # Python dependencies
│   └── .env.example      # Environment variables template
├── public/               # Static assets
├── docs/                 # Documentation
└── package.json          # Frontend dependencies and scripts
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/vitamind_db

# Authentication (Auth0)
AUTH0_DOMAIN=your-auth0-domain.auth0.com
AUTH0_CLIENT_ID=your-auth0-client-id
AUTH0_CLIENT_SECRET=your-auth0-client-secret

# AI Services
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
VOYAGE_API_KEY=your-voyage-api-key

# File Storage
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=vitamind-uploads

# Application
SECRET_KEY=your-secret-key
DEBUG=True
ENVIRONMENT=development
```

## 🔒 Security & Privacy

- Health data encryption at rest and in transit
- HIPAA/GDPR compliance considerations
- Anonymous AI processing
- Comprehensive audit logging
- User consent management

## 📚 API Documentation

When the backend is running, visit:

- **Interactive docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Development Status

### ✅ Completed

- [x] Project foundation with Next.js + FastAPI
- [x] Package management setup (pnpm + pip)
- [x] Basic project structure
- [x] Development environment configuration
- [x] Python 3.13.3 compatibility
- [x] Core dependencies installation

### 🚧 In Progress

- [ ] UI component library integration
- [ ] Authentication setup (Auth0)
- [ ] Database schema design
- [ ] AI pipeline implementation

### 📋 Planned

- [ ] Health data input forms
- [ ] PDF upload and parsing
- [ ] Recommendation engine
- [ ] Dashboard and visualizations
- [ ] Chat interface
- [ ] Wearable integrations
- [ ] Mobile optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions or support, please open an issue on GitHub or contact the development team.

---

**⚠️ Disclaimer**: This application is for educational and informational purposes only. It does not provide medical advice and should not be used as a substitute for professional medical consultation.
