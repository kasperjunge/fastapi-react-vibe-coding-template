# React Frontend - FastAPI-React Template

A modern React frontend built with TypeScript, Vite, and Tailwind CSS, featuring complete authentication flow and API integration with the FastAPI backend.

## 🚀 Features

- **React 18** with TypeScript for type-safe development
- **Vite** for fast development and optimized builds
- **Tailwind CSS** for utility-first styling
- **Radix UI** components for accessible UI elements
- **React Router** for client-side routing with authentication guards
- **Complete Authentication Flow** with user registration, email verification, and login
- **Environment-Aware API Client** that works seamlessly in development and production
- **Responsive Design** with mobile-first approach

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── auth/           # Authentication components
│   │   │   ├── LoginForm.tsx
│   │   │   ├── RegisterForm.tsx
│   │   │   ├── VerificationStatus.tsx
│   │   │   ├── VerifyEmail.tsx
│   │   │   ├── SuccessPage.tsx
│   │   │   └── ErrorPage.tsx
│   │   ├── ui/             # Reusable UI components
│   │   │   └── button.tsx
│   │   └── Dashboard.tsx   # Main dashboard component
│   ├── contexts/           # React contexts
│   │   └── AuthContext.tsx # Authentication state management
│   ├── lib/               # Utility libraries
│   │   └── api.ts         # API client with environment detection
│   ├── App.tsx            # Main app with routing
│   ├── main.tsx           # Entry point
│   └── index.css          # Global styles
├── public/                # Static assets
├── package.json           # Dependencies and scripts
├── vite.config.ts         # Vite configuration with proxy
├── tailwind.config.js     # Tailwind CSS configuration
├── components.json        # Shadcn/ui configuration
└── README.md             # This file
```

## 🛠️ Getting Started

### Prerequisites
- Node.js 18+ and npm
- Backend API running (see `../backend/README.md`)

### 1. Install Dependencies
```bash
npm install
```

### 2. Environment Configuration
The frontend automatically detects the backend API URL:

- **Development**: Uses Vite proxy to backend at `http://localhost:8000`
- **Production**: Uses relative paths or configured `VITE_API_URL`

No additional environment configuration needed for basic setup.

### 3. Start Development Server
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

### 4. Build for Production
```bash
npm run build
```

Built files will be in the `dist/` directory.

## 🔐 Authentication Flow

The frontend implements a complete authentication system:

### User Journey
1. **Registration** (`/register`)
   - User provides email, password, and profile info
   - System sends verification email
   - Redirects to verification status page

2. **Email Verification** (`/verification-status`)
   - Shows verification instructions
   - Allows resending verification email
   - Handles verification links from email

3. **Login** (`/login`)
   - User provides email and password
   - Receives JWT token for authenticated requests
   - Redirects based on verification status

4. **Dashboard** (`/dashboard`)
   - Protected route for verified users
   - Shows user profile and available features

### Route Protection
- **Public routes**: `/`, `/login`, `/register`
- **Semi-protected**: `/verification-status` (logged in but unverified)
- **Protected routes**: `/dashboard` (verified users only)

## 🌐 API Integration

### Environment-Aware API Client
The `src/lib/api.ts` module provides:

```typescript
// Automatic environment detection
const apiUrl = getApiUrl() // Returns '/api' in dev, configured URL in prod

// Convenient HTTP methods
export const api = {
  get: (endpoint: string) => fetch(`${apiUrl}${endpoint}`),
  post: (endpoint: string, data: any) => fetch(`${apiUrl}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }),
  // ... other methods
}

// Authenticated requests
export const authenticatedFetch = (endpoint: string, options: RequestInit = {}) => {
  const token = localStorage.getItem('token')
  return fetch(`${apiUrl}${endpoint}`, {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': token ? `Bearer ${token}` : '',
    }
  })
}
```

### Backend Integration
- **Authentication**: JWT token-based with automatic token management
- **CORS**: Configured automatically based on environment
- **Proxy**: Vite dev server proxies `/api/*` to backend in development

## 🎨 Styling & UI

### Tailwind CSS
Utility-first CSS framework with custom configuration:
- **Colors**: Custom brand colors and semantic color system
- **Typography**: Responsive text sizes and font weights
- **Components**: Pre-built component classes for consistency

### Radix UI Components
Accessible, unstyled components used for:
- Form elements (inputs, buttons, checkboxes)
- Navigation and routing
- Modal dialogs and overlays

### Component Organization
- **auth/**: Authentication-specific components with form validation
- **ui/**: Reusable, styled components based on design system
- **Main components**: Feature-specific components (Dashboard, etc.)

## 🧪 Development

### Available Scripts
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build locally
npm run lint         # Run ESLint
npm run type-check   # Run TypeScript compiler
```

### Development Tools
- **Hot Module Replacement (HMR)**: Instant updates during development
- **TypeScript**: Full type checking and IntelliSense
- **ESLint**: Code linting with React and TypeScript rules
- **Path Mapping**: Import aliases for clean imports

### Adding New Features

#### 1. New Component
```typescript
// src/components/MyComponent.tsx
import { FC } from 'react'

interface MyComponentProps {
  title: string
}

export const MyComponent: FC<MyComponentProps> = ({ title }) => {
  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-semibold">{title}</h2>
    </div>
  )
}
```

#### 2. New Route
```typescript
// Add to src/App.tsx
<Route path="/my-route" element={<MyComponent />} />
```

#### 3. API Integration
```typescript
// Use the API client
import { api } from '@/lib/api'

const fetchData = async () => {
  const response = await api.get('/my-endpoint')
  return response.json()
}
```

## 🔧 Configuration

### Vite Configuration
```typescript
// vite.config.ts highlights
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

### Environment Variables
```bash
# Optional: Custom API URL
VITE_API_URL=http://localhost:8000

# Vite automatically loads these from .env files
```

## 🐛 Troubleshooting

### Common Issues

**1. API Connection Failed**
- Ensure backend is running on `http://localhost:8000`
- Check browser console for CORS errors
- Verify proxy configuration in `vite.config.ts`

**2. Authentication Not Working**
- Check localStorage for stored token
- Verify token format in browser developer tools
- Ensure backend authentication endpoints are working

**3. Build Errors**
- Run `npm run type-check` to identify TypeScript errors
- Check for missing dependencies with `npm install`
- Verify all imports are correct

**4. Styling Issues**
- Check Tailwind classes are being applied
- Verify custom CSS doesn't conflict with Tailwind
- Use browser dev tools to inspect computed styles

### Development Server Issues
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Clear Vite cache
rm -rf .vite
npm run dev
```

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/guide/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Radix UI Documentation](https://www.radix-ui.com/docs)

## 🤝 Contributing

1. Follow the existing code style and component patterns
2. Add TypeScript types for all new components and functions
3. Use Tailwind classes instead of custom CSS when possible
4. Test authentication flows after making auth-related changes
5. Update this README when adding new features or changing structure

For detailed contribution guidelines, see `../backend/CONTRIBUTING.md`.
