import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuth } from '../../App'

interface LoginFormData {
  username: string // FastAPI-Users expects 'username' field for email
  password: string
}

interface ApiError {
  detail: string | { code: string; reason: string }
}

const LoginForm = () => {
  const navigate = useNavigate()
  const { setUser } = useAuth()
  const [formData, setFormData] = useState<LoginFormData>({
    username: '',
    password: '',
  })
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const validateForm = (): boolean => {
    if (!formData.username.trim()) {
      setError('Email is required')
      return false
    }
    if (!formData.password.trim()) {
      setError('Password is required')
      return false
    }
    if (!/\S+@\S+\.\S+/.test(formData.username)) {
      setError('Please enter a valid email address')
      return false
    }
    return true
  }

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
    if (error) setError('')
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!validateForm()) return

    setIsLoading(true)
    setError('')

    try {
      // Login with form data (FastAPI OAuth2 expects form data, not JSON)
      const formDataToSend = new FormData()
      formDataToSend.append('username', formData.username)
      formDataToSend.append('password', formData.password)

      const response = await fetch('/api/auth/jwt/login', {
        method: 'POST',
        body: formDataToSend,
      })

      if (response.ok) {
        const tokenData = await response.json()
        
        // Store the access token
        localStorage.setItem('access_token', tokenData.access_token)
        
        // Get user information
        const userResponse = await fetch('/api/users/me', {
          headers: {
            'Authorization': `Bearer ${tokenData.access_token}`
          }
        })
        
        if (userResponse.ok) {
          const userData = await userResponse.json()
          setUser(userData)
          
          // Redirect based on verification status
          if (userData.is_verified) {
            navigate('/dashboard')
          } else {
            navigate('/verification-status', { 
              state: { email: userData.email } 
            })
          }
        } else {
          setError('Failed to get user information')
        }
      } else {
        const errorData: ApiError = await response.json()
        
        if (typeof errorData.detail === 'string') {
          switch (errorData.detail) {
            case 'LOGIN_BAD_CREDENTIALS':
              setError('Invalid email or password')
              break
            case 'LOGIN_USER_NOT_VERIFIED':
              setError('Please verify your email before logging in')
              break
            default:
              setError(errorData.detail)
          }
        } else {
          setError('Login failed. Please try again.')
        }
      }
    } catch {
      setError('Network error. Please check your connection and try again.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Sign in to your account
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Or{' '}
            <Link
              to="/register"
              className="font-medium text-indigo-600 hover:text-indigo-500"
            >
              create a new account
            </Link>
          </p>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="username" className="sr-only">
                Email address
              </label>
              <input
                id="username"
                name="username"
                type="email"
                autoComplete="email"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Email address"
                value={formData.username}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Password"
                value={formData.password}
                onChange={handleInputChange}
              />
            </div>
          </div>

          {error && (
            <div className="rounded-md bg-red-50 p-4">
              <div className="text-sm text-red-700">{error}</div>
            </div>
          )}

          <div className="flex items-center justify-between">
            <Link
              to="/forgot-password"
              className="text-sm text-indigo-600 hover:text-indigo-500"
            >
              Forgot your password?
            </Link>
          </div>

          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? (
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              ) : null}
              {isLoading ? 'Signing in...' : 'Sign in'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default LoginForm 