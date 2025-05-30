import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { useState, useEffect, createContext, useContext } from 'react'
import './App.css'

// Types
interface User {
  id: string
  email: string
  is_active: boolean
  is_superuser: boolean
  is_verified: boolean
  created_at: string
}

interface AuthContextType {
  user: User | null
  setUser: (user: User | null) => void
  isLoading: boolean
  setIsLoading: (loading: boolean) => void
}

// Auth Context
const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

// Components (will be created separately)
import RegisterForm from './components/auth/RegisterForm'
import LoginForm from './components/auth/LoginForm'
import VerificationStatus from './components/auth/VerificationStatus'
import VerifyEmail from './components/auth/VerifyEmail'
import SuccessPage from './components/auth/SuccessPage'
import ErrorPage from './components/auth/ErrorPage'
import Dashboard from './components/Dashboard'

function App() {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  // Check if user is logged in on app start
  useEffect(() => {
    const token = localStorage.getItem('access_token')
    if (token) {
      // Verify token and get user info
      fetch('/api/users/me', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (response.ok) {
          return response.json()
        }
        throw new Error('Invalid token')
      })
      .then((userData: User) => {
        setUser(userData)
      })
      .catch(() => {
        localStorage.removeItem('access_token')
        setUser(null)
      })
      .finally(() => {
        setIsLoading(false)
      })
    } else {
      setIsLoading(false)
    }
  }, [])

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-lg">Loading...</div>
      </div>
    )
  }

  return (
    <AuthContext.Provider value={{ user, setUser, isLoading, setIsLoading }}>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Routes>
            {/* Public routes */}
            <Route path="/register" element={<RegisterForm />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/verify-email/:token" element={<VerifyEmail />} />
            <Route path="/verification-status" element={<VerificationStatus />} />
            <Route path="/success" element={<SuccessPage />} />
            <Route path="/error" element={<ErrorPage />} />
            
            {/* Protected routes */}
            <Route 
              path="/dashboard" 
              element={
                user && user.is_verified ? (
                  <Dashboard />
                ) : (
                  <Navigate to="/login" replace />
                )
              } 
            />
            
            {/* Default redirect */}
            <Route 
              path="/" 
              element={
                user && user.is_verified ? (
                  <Navigate to="/dashboard" replace />
                ) : (
                  <Navigate to="/login" replace />
                )
              } 
            />
          </Routes>
        </div>
      </Router>
    </AuthContext.Provider>
  )
}

export default App
